"""Reject forbidden characters in committed text, and unlabeled recommendations.

1. No em dash (U+2014), en dash (U+2013) or curly quotes (U+2018, U+2019, U+201C,
   U+201D) in any tracked text file.
2. In codex/strategy/, every sentence that ranks or recommends carries a label.

Usage: py -3 tools/lint_text.py
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BAD = {chr(0x2014): "em dash", chr(0x2013): "en dash", chr(0x2018): "curly quote", chr(0x2019): "curly quote",
       chr(0x201C): "curly quote", chr(0x201D): "curly quote"}  # chr() so this file passes its own check
TEXT = {".md", ".py", ".yaml", ".yml", ".json", ".jsonl", ".toml", ".txt", ".csv", ".gitignore"}
LABELS = re.compile(r"`?(DOCUMENTED|DERIVED|CONDITIONAL|CORROBORATED|HYPOTHESIS|CONTRADICTED|UNKNOWN)`?")
RANKING = re.compile(r"\b(best|worst|should|recommend|tier|rank|better than|stronger than|prefer)\b", re.I)


def tracked():
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard"],
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return [ROOT / p for p in out.splitlines() if (ROOT / p).suffix in TEXT or (ROOT / p).name in TEXT]


def main():
    errors = []
    for f in tracked():
        if not f.exists():
            continue
        for n, line in enumerate(f.read_text("utf-8", "replace").splitlines(), 1):
            for ch, name in BAD.items():
                if ch in line:
                    errors.append(f"{f.relative_to(ROOT)}:{n}: {name}")
            if "codex/strategy/" in f.relative_to(ROOT).as_posix():
                for sent in re.split(r"(?<=[.!?])\s+", line):
                    if RANKING.search(sent) and not LABELS.search(line):
                        errors.append(f"{f.relative_to(ROOT)}:{n}: ranking or recommendation without a label")
                        break
    for e in errors:
        print(e)
    print(f"lint_text: {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
