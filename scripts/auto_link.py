#!/usr/bin/env python3
"""Insert Jekyll links to people/glossary pages in posts/people files.

Strategy:
- Build per-language registry (English, 简体中文, 繁體中文) mapping name patterns to a
  Jekyll {% link %} target.
- For each markdown file in _posts and people, scan the body (skip frontmatter) and
  link every mention of a person (glossary terms: FIRST mention only), unless it already
  appears inside an existing markdown link / image / autolink, or the file itself IS
  the target page.
- People names come from the page title ('王述达，字善愷' → 王述达, 王善愷) plus an
  optional `aka:` frontmatter list of other names (曾用名、字、号…), e.g.
  `aka: 善恺、渭宜`. Bare alt names get the person's surname prepended.
- Inside raw HTML blocks (where kramdown does not parse markdown) links are
  written as <a> tags; existing markdown links there are rewritten too.
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

# Generated variants that name someone else and must never be linked.
EXCLUDED_TERMS = {
    "Yan Fu",  # reversed 'Fu Yan' (傅严), but also 严复, a different person
    # glossary/references*.md titles; these words are used as section headings.
    "References", "参考资料", "參考資料",
}


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
    """Extract name variants from a Chinese title like '陈懋治，字中平,  仲平' or '杜子劲, 别名杜同力'.

    Returns variants suitable for full-name matching. The primary (first) name yields
    its surname; subsequent tokens that don't already start with that surname are
    expanded to surname+token (e.g., '傅严，字介石' → ['傅严', '傅介石']). Bare
    courtesy/alt names are NOT returned alone, since 2-char fragments like '介石' can
    appear inside unrelated names (e.g., '蒋介石').
    """
    t = title.replace("，", ",").replace("、", ",")
    parts = [p.strip() for p in t.split(",") if p.strip()]
    cleaned: list[str] = []
    for p in parts:
        p = re.sub(r"^(字|别名|別名|原名|本名|号|號|又名)\s*[:：]?\s*", "", p)
        if p:
            cleaned.append(p)
    if not cleaned:
        return []
    primary = cleaned[0]
    return [primary] + expand_chinese_aliases(primary, cleaned[1:])


def expand_chinese_aliases(primary: str, aliases: list[str]) -> list[str]:
    """Turn alt names into full-name variants: aliases already starting with the
    primary name's surname are kept as-is, others get the surname prepended
    (e.g. primary '王述达', alias '善愷' → '王善愷')."""
    out: list[str] = []
    if not primary:
        return out
    surname = primary[0]
    for extra in aliases:
        if not extra:
            continue
        if extra.startswith(surname):
            out.append(extra)
        else:
            out.append(surname + extra)
    return out


def split_aka(value: str) -> list[str]:
    """Split an `aka:` frontmatter value like '王善恺, 善愷、孙渭宜' into names."""
    value = value.strip().strip("\"'")
    t = value.replace("，", ",").replace("、", ",")
    return [p.strip() for p in t.split(",") if p.strip()]


def split_english_title(title: str, slug: str, aka: list[str] | None = None) -> list[str]:
    """Extract names from English title like 'Sun Chongyi, also Weiyi' or
    'Fu Yan (courtesy name Jieshi)' or 'Shuda Wang, also Shankai Wang'.

    Like the Chinese variant, bare alt names ('Weiyi') are expanded with the
    surname ('Sun Weiyi') rather than matched alone, since a lone given name like
    'Bing' also appears inside unrelated names ('Shen Bing').
    """
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
    # The slug is surname+given pinyin, so the surname is the primary-name token
    # the slug starts with; default: first token.
    surname = next((tok for tok in primary_tokens if slug.lower().startswith(tok.lower())),
                   primary_tokens[0])
    for extra in parts[1:] + (aka or []):
        # Drop leading 'also' / 'styled' / 'courtesy name' etc.
        extra = re.sub(r"^(also( known as)?|styled|(courtesy|style|original) name)\s+", "",
                       extra, flags=re.I)
        tokens = extra.split()
        if not tokens:
            continue
        if any(tok.lower() == surname.lower() for tok in tokens):
            out.append(extra)
        else:
            # 'Zuo Xiong' → 'Zhao Zuoxiong'
            out.append(f"{surname} {''.join(tokens).capitalize()}")
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
        # Optional `aka:` frontmatter lists other names the person is known by
        # (曾用名、字、号…) that are not in the title.
        aka = split_aka(meta["fm"].get("aka", ""))
        if lang == LANG_EN:
            names = split_english_title(title, slug, aka)
            variants: list[str] = []
            for n in names:
                variants.extend(english_name_variants(n, slug))
            seen = set()
            for v in variants:
                if v in seen or v in EXCLUDED_TERMS:
                    continue
                seen.add(v)
                reg[lang].append((v, target, f.name))
        else:
            names = split_chinese_title(title)
            if names:
                names += expand_chinese_aliases(names[0], aka)
            for n in dict.fromkeys(names):
                # only meaningful CJK names (>=2 chars). Bare courtesy names are
                # already filtered upstream by split_chinese_title (only full
                # surname+given-name variants are emitted).
                if len(n) >= 2:
                    reg[lang].append((n, target, f.name))

    # Glossary
    for f in sorted(GLOSSARY_DIR.glob("*.md")):
        if f.name in {"glossary.md", "glossary-cn.md", "glossary-tw.md"}:
            # the glossary index itself — skip as a search target
            continue
        meta = load_file_meta(f)
        title = meta["fm"].get("title", "").strip()
        if not title or title in EXCLUDED_TERMS:
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
        r"<a\b[^>]*>.*?</a>",        # html anchors (incl. their text)
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


def make_html_link(text: str, target: str) -> str:
    return f'<a href="{{{{ site.baseurl }}}}{{% link {target} %}}">{text}</a>'


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(\{\{\s*site\.baseurl\s*\}\}\{%\s*link\s+([^\s%]+)\s*%\}\)")
HTML_LINK_RE = re.compile(r'<a href="\{\{\s*site\.baseurl\s*\}\}\{%\s*link\s+([^\s%]+)\s*%\}">([^<]+)</a>')

# kramdown leaves the content of block-level HTML raw (no markdown parsing)
# unless the element carries markdown="1".
HTML_BLOCK_TAGS = {
    "address", "article", "aside", "blockquote", "center", "dd", "details", "div",
    "dl", "dt", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4",
    "h5", "h6", "header", "li", "nav", "ol", "p", "pre", "section", "summary",
    "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul",
}
HTML_VOID_TAGS = {"area", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "wbr"}
HTML_TAG_RE = re.compile(r"<(/?)([A-Za-z][A-Za-z0-9]*)\b([^>]*)>")
MARKDOWN_ATTR_RE = re.compile(r"""\bmarkdown\s*=\s*["']?(1|block|span)""")


def raw_html_spans(body: str) -> list[tuple[int, int]]:
    """Return spans of body inside block-level HTML where markdown is not parsed,
    so a markdown link there would render literally."""
    spans: list[tuple[int, int]] = []
    stack: list[tuple[str, bool]] = []  # (tag, has markdown="1")
    raw_start: int | None = None

    def is_raw() -> bool:
        return bool(stack) and not any(md for _, md in stack)

    for m in HTML_TAG_RE.finditer(body):
        closing, tag, attrs = m.group(1) == "/", m.group(2).lower(), m.group(3)
        was_raw = is_raw()
        if closing:
            if any(t == tag for t, _ in stack):
                while stack and stack.pop()[0] != tag:
                    pass
        elif tag not in HTML_VOID_TAGS and not attrs.rstrip().endswith("/"):
            line_start = body.rfind("\n", 0, m.start()) + 1
            at_line_start = body[line_start:m.start()].strip() == ""
            # An HTML block only starts with a block-level tag at line start;
            # once inside one, every element nests.
            if stack or (tag in HTML_BLOCK_TAGS and at_line_start):
                stack.append((tag, bool(MARKDOWN_ATTR_RE.search(attrs))))
        now_raw = is_raw()
        if not was_raw and now_raw:
            raw_start = m.end()
        elif was_raw and not now_raw and raw_start is not None:
            spans.append((raw_start, m.start()))
            raw_start = None
    if raw_start is not None:
        spans.append((raw_start, len(body)))
    return spans


def fix_markdown_links_in_html(body: str) -> str:
    """Rewrite our markdown links that sit inside raw HTML blocks as <a> tags."""
    raw = raw_html_spans(body)
    for m in reversed(list(MD_LINK_RE.finditer(body))):
        if in_spans(m.start(), m.end(), raw):
            body = body[:m.start()] + make_html_link(m.group(1), m.group(2)) + body[m.end():]
    return body


def is_cjk(ch: str) -> bool:
    return "㐀" <= ch <= "鿿"


def find_first_match(body: str, term: str, lang: str, spans: list[tuple[int, int]]) -> int | None:
    """Find first index in body where term occurs as a whole word/phrase, outside masked spans."""
    if lang == LANG_EN:
        # word boundary on both sides (treat ASCII)
        pattern = r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])"
    else:
        # For CJK: literal match. We enforce CJK-neighbour boundaries below for
        # short (≤2 char) terms, since fragments like 谢冰 can appear inside
        # unrelated names like 谢冰莹.
        pattern = re.escape(term)
    short_cjk = lang != LANG_EN and len(term) <= 2
    for m in re.finditer(pattern, body):
        s, e = m.start(), m.end()
        if short_cjk:
            prev_ch = body[s - 1] if s > 0 else ""
            next_ch = body[e] if e < len(body) else ""
            if (prev_ch and is_cjk(prev_ch)) or (next_ch and is_cjk(next_ch)):
                continue
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
    body = fix_markdown_links_in_html(text[body_start:])
    changed = body != text[body_start:]

    # Build masked spans once, but they change as we insert links. We'll rebuild
    # the spans after each insertion (cheap given small file sizes).
    # Track (term, target) pairs already linked. Different name variants for the
    # same target (e.g. 王述达 / 王善愷) should each get their own first-mention
    # link, so we key on the surface term, not the target.
    linked_pairs: set[tuple[str, str]] = set()
    for existing in MD_LINK_RE.finditer(body):
        linked_pairs.add((existing.group(1), existing.group(2)))
    for existing in HTML_LINK_RE.finditer(body):
        linked_pairs.add((existing.group(2), existing.group(1)))

    # Iterate entries. People names are linked at every mention; glossary terms
    # only at their first mention, since they recur too often to link each time.
    for term, target, source_name in entries:
        # Skip if this file IS the target page (compare by stem)
        if path.name == source_name:
            continue
        link_all = target.startswith("people/")
        if not link_all and (term, target) in linked_pairs:
            continue
        while True:
            spans = masked_spans(body)
            idx = find_first_match(body, term, lang, spans)
            if idx is None:
                break
            if in_spans(idx, idx + len(term), raw_html_spans(body)):
                replacement = make_html_link(term, target)
            else:
                replacement = make_link(term, target)
            body = body[:idx] + replacement + body[idx + len(term):]
            linked_pairs.add((term, target))
            changed = True
            if not link_all:
                break

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
