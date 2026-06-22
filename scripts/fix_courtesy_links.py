#!/usr/bin/env python3
"""One-shot cleanup for `X[YZ]({% link people/F.md %})` where YZ is a 2-char CJK
courtesy/alt name (not the primary name).

For each occurrence:
  - parse F.md to determine the target's name list (primary first)
  - if YZ equals the primary name → leave alone (a normal full-name link with
    arbitrary preceding text)
  - else if YZ is a known courtesy/alt name and the preceding char X equals the
    target's surname → expand the link to enclose the full name `[XYZ](...)`
  - else if YZ is a known courtesy/alt name and X does NOT match the surname →
    the bracketed fragment was matched inside an unrelated name (e.g. 介石 inside
    蒋介石) → unwrap to plain text `XYZ`
  - otherwise leave alone
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PEOPLE_DIR = ROOT / "people"
POSTS_DIR = ROOT / "_posts"

LINK_PAT = re.compile(
    r"([㐀-鿿])"
    r"\[([㐀-鿿]{2,3})\]"
    r"\(\{\{\s*site\.baseurl\s*\}\}\{%\s*link\s+(people/[A-Za-z0-9_-]+\.md)\s*%\}\)"
)

TITLE_PAT = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)


def parse_title_names(target_md: Path) -> list[str]:
    if not target_md.exists():
        return []
    text = target_md.read_text(encoding="utf-8")
    m = TITLE_PAT.search(text)
    if not m:
        return []
    title = m.group(1).replace("，", ",").replace("、", ",")
    out: list[str] = []
    for p in title.split(","):
        p = p.strip()
        p = re.sub(r"^(字|别名|別名|原名|本名|号|號|又名)\s*[:：]?\s*", "", p)
        if p:
            out.append(p)
    return out


def process(path: Path) -> int:
    text = path.read_text(encoding="utf-8")

    def repl(m: re.Match) -> str:
        prefix = m.group(1)
        inner = m.group(2)
        target = m.group(3)
        names = parse_title_names(ROOT / target)
        if not names:
            return m.group(0)
        primary = names[0]
        if inner == primary:
            return m.group(0)  # primary-name link — leave alone
        if inner not in names:
            return m.group(0)  # unrelated CJK fragment — leave alone
        surname = primary[0]
        full = prefix + inner
        link_target = m.group(0)[m.group(0).index("("):]
        if prefix == surname:
            return f"[{full}]{link_target}"
        # Surname mismatch — bare courtesy fragment matched inside a different name.
        return full

    new_text, count = LINK_PAT.subn(repl, text)
    if count and new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return count


def main() -> None:
    files = sorted(POSTS_DIR.glob("*.md")) + sorted(PEOPLE_DIR.glob("*.md"))
    total = 0
    for f in files:
        n = process(f)
        if n:
            print(f"  {f.relative_to(ROOT)}: {n} link(s) processed")
            total += n
    print(f"\nProcessed {total} link site(s) across {len(files)} files.")


if __name__ == "__main__":
    main()
