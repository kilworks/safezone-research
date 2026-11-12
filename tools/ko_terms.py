"""One terminology rule for the Korean edition: viewer attacks and the fake chest are written in Korean.

Rule: in Korean prose, the names below use the Korean term on the right. English stays only where it
is a quotation or a formal token: inside "..." or '...', `code`, $math$, {formal sets}, link targets,
identifiers (missile_damage), formal calls (blockers(Missile)), and a gloss in parentheses right after a Korean word ("핵폭탄(nuke)").
A Korean particle that follows the replaced word is fixed to match the new final syllable.

Usage: python tools/ko_terms.py [--apply]
Without --apply, lists the English uses left and exits with their count (capped at 255).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TERMS = [  # longest first
    ("airstrike impact", "공습 충격"), ("airstrike fire", "공습 화재"), ("gunship bomb", "건십 폭탄"),
    ("cyclops attack", "사이클롭스 공격"), ("bounty mark", "현상금 표시"),
    ("fake chests", "가짜 상자"), ("fake chest", "가짜 상자"),
    ("tear gas", "최루 가스"),
    ("airstrikes", "공습"), ("airstrike", "공습"),
    ("gunships", "건십"), ("gunship", "건십"),
    ("missiles", "미사일"), ("missile", "미사일"),
    ("bounties", "현상금"), ("bounty", "현상금"),
    ("cyclopes", "사이클롭스"), ("cyclops", "사이클롭스"),
    ("nukes", "핵"), ("nuke", "핵"),
]
WORD = re.compile(r"(?<![A-Za-z0-9_-])(" + "|".join(re.escape(e) for e, _ in TERMS) + r")(?![A-Za-z0-9_-])", re.I)
KO = {e: k for e, k in TERMS}
# Protected spans: quotations, code, math, formal sets, link targets.
PROTECT = re.compile(r'^\s*[A-Za-z_ ]+:(?=\s|$)|"[^"\n]*"|\'[^\'\n]*\'|`[^`\n]*`|\$[^$\n]*\$|\{[^}\n]*\}|\]\([^)\n]*\)|[A-Za-z_]+\([^)\n]*\)')
# (particle after a final consonant, particle after a vowel)
PARTICLES = [("으로", "로"), ("이랑", "랑"), ("과", "와"), ("을", "를"), ("은", "는"), ("이", "가")]


def final_consonant(syllable):
    code = ord(syllable) - 0xAC00
    return 0 <= code < 11172 and code % 28 != 0, 0 <= code < 11172 and code % 28 == 8  # (has batchim, batchim is ㄹ)


def particle(word, rest):
    """(original particle at the start of rest, the right one after word); ('', '') if none."""
    has, rieul = final_consonant(word[-1])
    for cons, vow in PARTICLES:
        for p in (cons, vow):
            if rest.startswith(p):
                nxt = rest[len(p):len(p) + 1]
                if cons == "이" and nxt and "가" <= nxt <= "힣":
                    return "", ""  # copula (이며, 이다), not the subject particle
                if cons == "으로":
                    return p, "로" if (not has or rieul) else "으로"
                return p, cons if has else vow
    return "", ""


def convert(line):
    """Return (new line, number of replacements)."""
    spans = [m.span() for m in PROTECT.finditer(line)]
    out, i, n = [], 0, 0
    for m in WORD.finditer(line):
        s, e = m.span()
        if any(a <= s < b for a, b in spans):
            continue
        if s > 1 and line[s - 1] == "(" and "가" <= line[s - 2] <= "힣":
            continue  # gloss after a Korean word
        ko = KO[m.group(1).lower()]
        old, new = particle(ko, line[e:])
        out += [line[i:s], ko, new]
        i = e + len(old)
        n += 1
    out.append(line[i:])
    return "".join(out), n


def files():
    yield from sorted((ROOT / "ko/i18n").glob("*.yaml"))
    yield from sorted((ROOT / "ko/theory").glob("*.md"))
    yield ROOT / "ko/README.md"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    apply = "--apply" in sys.argv
    total = 0
    for path in files():
        lines = path.read_text(encoding="utf-8").split("\n")
        changed = 0
        for k, line in enumerate(lines):
            new, n = convert(line)
            if n:
                changed += n
                if not apply:
                    print(f"{path.relative_to(ROOT).as_posix()}:{k + 1}: {line.strip()[:140]}")
                lines[k] = new
        if apply and changed:
            path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        total += changed
    print(f"ko_terms: {total} English use(s) {'replaced' if apply else 'left'}")
    return 0 if apply else min(total, 255)


if __name__ == "__main__":
    sys.exit(main())
