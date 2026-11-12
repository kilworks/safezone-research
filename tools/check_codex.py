"""Check that every Codex line carrying a number also carries its source.

A line passes if it has no digit once ids, links, clause ids, dates and
LaTeX-free markup are removed, or if it cites an id (M-, U-, C-, T-, E-)
or an analysis/results/ path. Structural counts written by build_codex.py
itself (rules per family, labels per page) are exempt: they describe the
Codex, not the game.

Usage: python tools/check_codex.py [--lang ko] [--verbose]
Exit code: number of failing lines (capped at 255).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ID = re.compile(r"\b[MUCTE]-\d{4}\b")
RESULTS = re.compile(r"analysis/results/")
STRIP = [
    re.compile(r"\]\([^)]*\)"),             # link targets
    re.compile(r"<a id=\"[^\"]*\"></a>"),   # anchors
    re.compile(r"https?://\S+"),            # bare urls
    re.compile(r"`wiki-[a-z0-9-]+`"),       # clause ids
    re.compile(r"\b[A-Z]{1,3}-\d{4}\b"),    # any record id (RE-0001, P-...)
    re.compile(r"\b20\d\d-\d\d-\d\d\b"),    # snapshot dates
    re.compile(r"^#+ "),                    # heading markers
    re.compile(r"[\w./-]+\.md"),           # file names in link text
]
# Lines build_codex.py writes about the Codex itself.
STRUCTURAL = [
    re.compile(r"^- \[[^\]]+\]\([^)]*\): \d+ rules$"),
    re.compile(r"^This page gathers \d+ rules"),
    re.compile(r"^이 페이지는 규칙 \d+개"),
    re.compile(r"^- \[[^\]]+\]\([^)]*\): 규칙 \d+개$"),
    re.compile(r"^Open questions by priority: "),
    re.compile(r"^우선순위별 미해결 질문"),
]


def failing_lines(path):
    # A theorem page is one T record: every line is its statement, proof or label.
    if path.parent.name == "theorems":
        return
    in_code = False
    parent_sourced = False
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        sourced = bool(ID.search(line) or RESULTS.search(line))
        if line.startswith("- "):
            parent_sourced = sourced
        elif not line.startswith("  "):
            parent_sourced = False
        # An indented sub-bullet (the Korean translation of a quote) shares its parent's source.
        if in_code or sourced or (line.startswith("  ") and parent_sourced):
            continue
        if any(p.search(line) for p in STRUCTURAL):
            continue
        rest = line
        for p in STRIP:
            rest = p.sub("", rest)
        if re.search(r"\d", rest):
            yield n, line


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="en", choices=["en", "ko"])
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    base = ROOT / ("codex" if args.lang == "en" else "ko/codex")
    bad = 0
    for path in sorted(base.rglob("*.md")):
        for n, line in failing_lines(path):
            bad += 1
            if args.verbose or bad <= 40:
                print(f"{path.relative_to(ROOT).as_posix()}:{n}: {line[:160]}")
    print(f"check_codex ({args.lang}): {bad} line(s) with a number and no source")
    return min(bad, 255)


if __name__ == "__main__":
    sys.exit(main())
