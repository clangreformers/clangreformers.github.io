#!/usr/bin/env python3
"""Insert Jekyll links to people/glossary pages on first mention in posts/people files.

Strategy:
- Build per-language registry (English, 简体中文, 繁體中文) mapping name patterns to a
  Jekyll {% link %} target.
- For each markdown file in _posts and people, scan the body (skip frontmatter) and
  replace the FIRST occurrence of each name with a link, unless that name already
  appears inside an existing markdown link / image / autolink, or the file itself IS
  the target page.
"""
from __future__ import annotations
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PEOPLE_DIR = ROOT / "people"
GLOSSARY_DIR = ROOT / "glossary"
POSTS_DIR = ROOT / "_posts"

LANG_EN = "English"
LANG_CN = "简体中文"
LANG_TW = "繁體中文"


def parse_frontmatter(text: str) -> tuple[dict, int]:
    """Return (frontmatter dict, end index of frontmatter incl. trailing newline)."""
    if not text.startswith("---"):
        return {}, 0
    end = text.find("\n---", 3)
    if end == -1:
        return {}, 0
    fm_text = text[3:end]
    fm = {}
    for line in fm_text.splitlines():
        m = re.match(r"^\s*([A-Za-z_][\w-]*)\s*:\s*(.*?)\s*$", line)
        if m:
            fm[m.group(1)] = m.group(2)
    # advance past "\n---\n"
    body_start = end + len("\n---")
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    return fm, body_start


def detect_lang(path: Path) -> str:
    name = path.name
    if name.endswith("-cn.md"):
        return LANG_CN
    if name.endswith("-tw.md"):
        return LANG_TW
    return LANG_EN


def base_slug(path: Path) -> str:
    """Return the filename without language suffix and extension."""
    s = path.stem
    if s.endswith("-cn") or s.endswith("-tw"):
        s = s[:-3]
    return s


def link_target_for_people(path: Path) -> str:
    """Return Jekyll link path like people/anwenzhuo.md keyed off the lang variant."""
    return f"people/{path.name}"


def link_target_for_glossary(path: Path) -> str:
    return f"glossary/{path.name}"


# ---------- name extraction ----------

def split_chinese_title(title: str) -> list[str]:
    """Extract names from Chinese title like '陈懋治，字中平,  仲平' or '杜子劲, 别名杜同力'."""
    # Normalise full-width commas, etc.
    t = title.replace("，", ",").replace("、", ",")
    parts = [p.strip() for p in t.split(",") if p.strip()]
    out = []
    for p in parts:
        # Strip prefixes like '字', '别名', '別名', '原名'
        p = re.sub(r"^(字|别名|別名|原名|号|號)\s*[:：]?\s*", "", p)
        if p:
            out.append(p)
    return out


def split_english_title(title: str) -> list[str]:
    """Extract names from English title like 'Sun Chongyi, also Weiyi' or
    'Fu Yan (courtesy name Jieshi)' or 'Shuda Wang, also Shankai Wang'."""
    # Drop parenthetical content first
    t = re.sub(r"\([^)]*\)", "", title)
    # Split on commas
    parts = [p.strip() for p in t.split(",") if p.strip()]
    out: list[str] = []
    if not parts:
        return out
    primary = parts[0]
    out.append(primary)
    primary_tokens = primary.split()
    # primary tokens give us the surname (one of the tokens). We'll heuristically
    # treat the shorter token as surname for Chinese names.
    # Find surname: for two-token names, surname is whichever token is also in the
    # filename slug start; default: first token.
    for extra in parts[1:]:
        # Drop leading 'also' / 'styled' / 'courtesy name' etc.
        extra = re.sub(r"^(also( known as)?|styled|courtesy name)\s+", "", extra, flags=re.I)
        if extra:
            out.append(extra)
    return out


def english_name_variants(name: str, slug: str) -> list[str]:
    """Given an English full name and the slug (surname+given pinyin), return search variants."""
    name = name.strip()
    tokens = name.split()
    variants = {name}
    if len(tokens) == 2:
        a, b = tokens
        # Determine which is surname by comparing with slug (lowercased no spaces)
        joined_ab = (a + b).lower()
        joined_ba = (b + a).lower()
        slug_lc = slug.lower()
        # The slug is surname+given for our people files.
        if joined_ab == slug_lc:
            # a=surname, b=given → also add "b a"
            variants.add(f"{b} {a}")
        elif joined_ba == slug_lc:
            # b=surname, a=given → also add "b a"
            variants.add(f"{b} {a}")
        else:
            # unknown ordering, just add reverse too
            variants.add(f"{b} {a}")
    return list(variants)


# ---------- file scanning ----------

def load_file_meta(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm, body_start = parse_frontmatter(text)
    return {
        "path": path,
        "text": text,
        "fm": fm,
        "body_start": body_start,
        "lang": detect_lang(path),
        "slug": base_slug(path),
    }


def build_registries() -> dict[str, list[tuple[str, str, str]]]:
    """Return per-language list of (search_term, link_target, source_file_name).
    source_file_name is used to skip self-linking.
    Sorted by length desc so longer names are matched first.
    """
    reg: dict[str, list[tuple[str, str, str]]] = {LANG_EN: [], LANG_CN: [], LANG_TW: []}

    # People
    for f in sorted(PEOPLE_DIR.glob("*.md")):
        if f.name in {"people.md", "people-cn.md", "people-tw.md"}:
            continue
        meta = load_file_meta(f)
        title = meta["fm"].get("title", "").strip()
        if not title:
            continue
        lang = meta["lang"]
        slug = meta["slug"]
        target = link_target_for_people(f)
        if lang == LANG_EN:
            names = split_english_title(title)
            variants: list[str] = []
            for n in names:
                variants.extend(english_name_variants(n, slug))
            seen = set()
            for v in variants:
                if v in seen:
                    continue
                seen.add(v)
                reg[lang].append((v, target, f.name))
        else:
            names = split_chinese_title(title)
            for n in names:
                # only meaningful CJK names (>=2 chars)
                if len(n) >= 2:
                    reg[lang].append((n, target, f.name))

    # Glossary
    for f in sorted(GLOSSARY_DIR.glob("*.md")):
        if f.name in {"glossary.md", "glossary-cn.md", "glossary-tw.md"}:
            # the glossary index itself — skip as a search target
            continue
        meta = load_file_meta(f)
        title = meta["fm"].get("title", "").strip()
        if not title:
            continue
        lang = meta["lang"]
        target = link_target_for_glossary(f)
        reg[lang].append((title, target, f.name))

    # Sort by length desc to match the longest variant first
    for lang in reg:
        reg[lang].sort(key=lambda t: -len(t[0]))
    return reg


# ---------- linking ----------

# Regions in body where we must NOT inject a link: existing markdown links,
# images, autolinks, code spans, fenced code blocks.
def masked_spans(body: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    patterns = [
        r"```.*?```",                # fenced code
        r"`[^`\n]+`",                # inline code
        r"!\[[^\]]*\]\([^)]*\)",     # images
        r"\[[^\]]*\]\([^)]*\)",      # markdown links
        r"\[[^\]]*\]\[[^\]]*\]",     # reference-style links
        r"<https?://[^>]+>",        # autolinks
        r"https?://\S+",            # bare URLs
        r"\{%[^%]*%\}",             # liquid tags
        r"\{\{[^}]*\}\}",           # liquid output
        r"<[^>]+>",                  # html tags
    ]
    for pat in patterns:
        for m in re.finditer(pat, body, flags=re.DOTALL):
            spans.append((m.start(), m.end()))
    spans.sort()
    # merge
    merged: list[tuple[int, int]] = []
    for s, e in spans:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return merged


def in_spans(pos: int, end: int, spans: list[tuple[int, int]]) -> bool:
    # binary-ish scan, but list is small
    for s, e in spans:
        if pos < e and end > s:
            return True
        if s > end:
            break
    return False


def make_link(text: str, target: str) -> str:
    return f"[{text}]({{{{ site.baseurl }}}}{{% link {target} %}})"


def is_cjk(ch: str) -> bool:
    return "㐀" <= ch <= "鿿"


def find_first_match(body: str, term: str, lang: str, spans: list[tuple[int, int]]) -> int | None:
    """Find first index in body where term occurs as a whole word/phrase, outside masked spans."""
    if lang == LANG_EN:
        # word boundary on both sides (treat ASCII)
        pattern = r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])"
    else:
        # For CJK: ensure not adjacent to another CJK char that would extend the name
        pattern = re.escape(term)
    for m in re.finditer(pattern, body):
        s, e = m.start(), m.end()
        if lang != LANG_EN:
            # avoid mid-name matches by checking neighbours aren't CJK letters (already handled
            # because exact match of full title; for safety, allow it)
            pass
        if in_spans(s, e, spans):
            continue
        return s
    return None


def link_file(path: Path, registry: dict[str, list[tuple[str, str, str]]]) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body_start = parse_frontmatter(text)
    if body_start == 0:
        return False
    lang = detect_lang(path)
    entries = registry.get(lang, [])
    if not entries:
        return False
    header = text[:body_start]
    body = text[body_start:]

    # Build masked spans once, but they change as we insert links. We'll rebuild
    # the spans after each insertion (cheap given small file sizes).
    changed = False
    # Track targets already linked to avoid double-linking the same target.
    linked_targets: set[str] = set()
    for existing in re.finditer(r"\{%\s*link\s+([^\s%]+)\s*%\}", body):
        linked_targets.add(existing.group(1))

    # Iterate entries; for each, attempt one insertion.
    for term, target, source_name in entries:
        # Skip if this file IS the target page (compare by stem)
        if path.name == source_name:
            continue
        if target in linked_targets:
            continue
        spans = masked_spans(body)
        idx = find_first_match(body, term, lang, spans)
        if idx is None:
            continue
        replacement = make_link(term, target)
        body = body[:idx] + replacement + body[idx + len(term):]
        linked_targets.add(target)
        changed = True

    if changed:
        path.write_text(header + body, encoding="utf-8")
    return changed


def main():
    registry = build_registries()
    # Quick log of registry sizes
    for lang in (LANG_EN, LANG_CN, LANG_TW):
        print(f"  [{lang}] {len(registry[lang])} terms")

    files: list[Path] = []
    files.extend(sorted(POSTS_DIR.glob("*.md")))
    files.extend(sorted(PEOPLE_DIR.glob("*.md")))

    modified = 0
    for f in files:
        if link_file(f, registry):
            modified += 1
            print(f"updated: {f.relative_to(ROOT)}")
    print(f"\nModified {modified} of {len(files)} files.")


if __name__ == "__main__":
    main()
