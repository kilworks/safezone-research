"""Build the generated part of codex/ from kb/ and theory/ (Phase 8, Editor role, no new facts).

Writes:
  codex/rules/<family>.md   every mechanic of a family, in the template of master prompt section 10
  codex/sigils/<sigil>.md   every mechanic that names the sigil
  codex/theorems/T-xxxx.md  each theorem, extracted verbatim from theory/*.md
  codex/unknowns.md         every open question and contradiction, by priority
Every line that carries a number also carries the ID it comes from, so
tools/check_codex.py can trace it. Hand-written pages (codex/strategy/) are not touched.

With --lang ko it writes the same pages in Korean to ko/codex/: free text comes from
ko/i18n/*.yaml (keyed by ID), theorems from ko/theory/, and wiki quotes stay verbatim
in English with the translation under them. A missing translation stops the build.

Usage: py -3 tools/build_codex.py [--lang ko]
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STRENGTH = ["UNKNOWN", "CONTRADICTED", "HYPOTHESIS", "CONDITIONAL", "DERIVED", "DOCUMENTED", "CORROBORATED"]
PRIORITY = ["critical", "high", "medium", "low"]
SIGILS = ["piety", "greed", "ingenuity", "trolling", "death", "endurance", "necromancy", "protection", "healing"]

EN = {
    "label": "Label", "sigils": "Sigils", "official": "**Official text** (snapshot 2026-11-11):", "source": "source",
    "formal": "**Formal model:**", "reading": "reading", "domain": "domain", "parameter": "parameter",
    "consequences": "**Consequences:** ", "interactions": "**Interactions:** ", "open": "**Open questions:**",
    "contradictions": "**Contradictions:** ", "notes": "Notes ({})",
    "summary": "## Summary", "gathers": "This page gathers {n} rules ({counts}). Every rule below quotes the official wiki word for word "
    "and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.",
    "rules": "## Rules", "simcheck": "## Simulation check", "tested": "Theorems with tests in `sim/tests/`: ",
    "untested": "No theorem or simulation covers this page yet.", "openh": "## Open questions", "none": "None.",
    "confidence": "## Confidence", "lowest": "`{}`: the lowest label among the rules on this page.",
    "plain": "### In plain words",
    "fam_intro": "Rules of the `{}` family, as the wiki states them on 2026-11-11.", "fam_title": "Rules: {}",
    "sig_intro": "Rules that name the Sigil of {}, as the wiki states them on 2026-11-11.", "sig_title": "Sigil of {}",
    "thm_head": "# {tid}\n\nExtracted from [theory/{f}](../../theory/{f}), where the full context, the proof and the test are.\n\n",
    "u_title": "# Open questions and contradictions",
    "u_intro": "Everything the official wiki leaves undecided, as of the 2026-11-11 snapshot. Each question lists the competing readings and "
    "what would settle it. No model in this project picks a reading silently: every simulation is run under each reading that matters.",
    "u_counts": "Open questions by priority: {} (source: kb/unknowns/, {} records).", "u_prio": "## Priority: {}",
    "status": "Status: `{}`.", "why": "Why it matters ({})", "free": "- {} free parameter `{}`, swept over {}",
    "sweep_default": "a range to be set", "resolution": "resolution", "resolved": "resolved",
    "c_title": "## Contradictions between pages",
    "i_title": "# Safe Zone Codex: index",
    "i_intro": "Everything in this encyclopedia, one click away. Rules are quoted word for word from the official wiki "
    "(snapshot 2026-11-11), translated into formulas, and every ambiguity is listed as an open question. "
    "Labels: `DOCUMENTED` (the wiki says it), `DERIVED` (proven), `CONDITIONAL` (proven under one reading of an open question), "
    "`CONTRADICTED` (two pages disagree), `UNKNOWN`. Back to the [project README](../README.md). [한국어](../ko/codex/index.md).",
    "i_sigils": "## Sigils", "i_families": "## Rules by family", "i_n": "{} rules", "i_thms": "## Theorems", "i_from": "from theory/{}",
    "i_open": "## Open questions", "i_all": "- [All open questions and contradictions](unknowns.md)", "i_every": "## Every rule",
}
KO = {
    "label": "라벨", "sigils": "시길", "official": "**공식 원문** (2026-11-11 스냅샷, 영어 원문 그대로):", "source": "출처",
    "formal": "**형식 모델:**", "reading": "해석", "domain": "정의역", "parameter": "매개변수",
    "consequences": "**따름 결과:** ", "interactions": "**상호작용:** ", "open": "**미해결 질문:**",
    "contradictions": "**모순:** ", "notes": "메모 ({})",
    "summary": "## 요약", "gathers": "이 페이지는 규칙 {n}개({counts})를 모았습니다. 아래의 모든 규칙은 공식 위키를 한 글자도 바꾸지 않고 인용하고 "
    "형식적 해석을 붙입니다. 문구가 여러 해석을 허용하면 모든 해석을 나열하고 질문은 열린 채로 둡니다.",
    "rules": "## 규칙", "simcheck": "## 시뮬레이션 검증", "tested": "`sim/tests/`에 테스트가 있는 정리: ",
    "untested": "아직 이 페이지를 다루는 정리나 시뮬레이션이 없습니다.", "openh": "## 미해결 질문", "none": "없음.",
    "confidence": "## 신뢰도", "lowest": "`{}`: 이 페이지 규칙들 가운데 가장 낮은 라벨입니다.",
    "plain": "### 쉬운 말로",
    "fam_intro": "`{}` 계열의 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.", "fam_title": "규칙: {}",
    "sig_intro": "{} 시길을 언급하는 규칙입니다. 2026-11-11 위키에 적힌 그대로입니다.", "sig_title": "{} 시길",
    "thm_head": "# {tid}\n\n[theory/{f}](../../theory/{f})에서 발췌했습니다. 전체 맥락, 증명, 테스트는 그곳에 있습니다.\n\n",
    "u_title": "# 미해결 질문과 모순",
    "u_intro": "2026-11-11 스냅샷 기준으로 공식 위키가 정하지 않은 모든 것입니다. 각 질문에는 경쟁하는 해석과 "
    "그것을 결정할 방법이 적혀 있습니다. 이 프로젝트의 어떤 모델도 해석을 몰래 고르지 않습니다. 모든 시뮬레이션은 중요한 해석마다 따로 실행됩니다.",
    "u_counts": "우선순위별 미해결 질문: {} (출처: kb/unknowns/, 기록 {}개).", "u_prio": "## 우선순위: {}",
    "status": "상태: `{}`.", "why": "중요한 이유 ({})", "free": "- {} 자유 매개변수 `{}`, 탐색 범위: {}",
    "sweep_default": "아직 정하지 않은 범위", "resolution": "해결 방법", "resolved": "해결됨",
    "c_title": "## 페이지 사이의 모순",
    "i_title": "# Safe Zone 코덱스: 목차",
    "i_intro": "이 백과사전의 모든 내용에 한 번의 클릭으로 갈 수 있습니다. 규칙은 공식 위키(2026-11-11 스냅샷)에서 "
    "그대로 인용하고, 수식으로 옮기며, 모든 모호함은 미해결 질문으로 남깁니다. "
    "라벨: `DOCUMENTED`(위키에 적혀 있음), `DERIVED`(증명됨), `CONDITIONAL`(미해결 질문의 한 해석 아래에서 증명됨), "
    "`CONTRADICTED`(두 페이지가 서로 다름), `UNKNOWN`. [프로젝트 README](../README.md)로 돌아가기. "
    "[English version](../../codex/index.md).",
    "i_sigils": "## 시길", "i_families": "## 계열별 규칙", "i_n": "규칙 {}개", "i_thms": "## 정리", "i_from": "출처: theory/{}",
    "i_open": "## 미해결 질문", "i_all": "- [모든 미해결 질문과 모순](unknowns.md)", "i_every": "## 모든 규칙",
}
NAMES_KO = {
    "piety": "Piety(경건)", "greed": "Greed(탐욕)", "ingenuity": "Ingenuity(창의)", "trolling": "Trolling(장난)",
    "death": "Death(죽음)", "endurance": "Endurance(인내)", "necromancy": "Necromancy(강령술)",
    "protection": "Protection(보호)", "healing": "Healing(치유)",
    "damage": "피해(damage)", "economy": "경제(economy)", "items": "아이템(items)", "poison": "독(poison)",
    "revival": "부활(revival)", "sigil": "시길(sigil)", "viewer": "시청자(viewer)", "weapons": "무기(weapons)",
    "zombies": "좀비(zombies)", "zone": "존(zone)",
    "critical": "치명적", "high": "높음", "medium": "보통", "low": "낮음",
}
FAMILY_KO = {"healing": "회복(healing)"}  # the healing family, distinct from the Sigil of Healing


def load(kind):
    return {r["id"]: r for r in (yaml.safe_load(f.read_text("utf-8")) for f in sorted((ROOT / "kb" / kind).glob("*.yaml")))}


def lowest(labels):
    return min(labels, key=STRENGTH.index) if labels else "UNKNOWN"


def unknown_link(u, depth="../"):
    return f"[{u}]({depth}unknowns.md#{u.lower()})"


class Lang:
    """Strings and free text for one output language; en is the identity."""

    def __init__(self, code):
        self.code, self.s, self.missing = code, (KO if code == "ko" else EN), []
        self.tr = {}
        if code == "ko":
            for f in sorted((ROOT / "ko" / "i18n").glob("*.yaml")):
                self.tr.update(yaml.safe_load(f.read_text("utf-8")) or {})

    def name(self, key, family=False):
        if self.code == "en":
            return key.capitalize() if key in SIGILS and not family else key
        return (FAMILY_KO.get(key) if family else None) or NAMES_KO[key]

    def get(self, rid, field, en):
        """Translated value of a record field (same shape as en), or en itself in English."""
        if self.code == "en" or en in (None, "", [], {}):
            return en
        v = (self.tr.get(rid) or {}).get(field)
        shape_ok = isinstance(v, str) if isinstance(en, str) else (
            isinstance(v, list) and len(v) == len(en) if isinstance(en, list) else isinstance(v, dict) and set(v) == set(en))
        if not shape_ok:
            self.missing.append(f"{rid}.{field}")
            return en
        return v

    def intro(self, key):
        return (self.tr.get(key) if self.code == "ko" else INTROS.get(key)) or None


INTROS = {}


def mechanic_block(m, unknowns, contra_by_mech, theorems_by_mech, L):
    mid, S = m["id"], L.s
    out = [f'<a id="{mid.lower()}"></a>', "", f"### {mid}: {L.get(mid, 'name', m['name'])}", "",
           f"{S['label']}: `{m['label']}`. {S['sigils']}: {', '.join(m['sigils'])}.", "", S["official"], ""]
    quotes = L.get(mid, "quotes", [s["quote"] for s in m["sources"]])
    for s, q in zip(m["sources"], quotes):
        out.append(f"- {mid} `{s['clause']}`: \"{s['quote']}\" ([{S['source']}]({s['url']}))")
        if L.code != "en":
            out.append(f"  - 번역: {q}")
    out += ["", S["formal"], ""]
    for k, v in L.get(mid, "readings", m["formal"]["readings"]).items():
        out.append(f"- {mid} {S['reading']} {k}: `{v}`")
    if m["formal"].get("domain"):
        out.append(f"- {mid} {S['domain']}: {L.get(mid, 'domain', m['formal']['domain'])}")
    for k, v in L.get(mid, "parameters", m["formal"].get("parameters") or {}).items():
        out.append(f"- {mid} {S['parameter']} `{k}`: {v}")
    if theorems_by_mech.get(mid):
        out += ["", S["consequences"] + ", ".join(f"[{t}](../theorems/{t}.md)" for t in sorted(theorems_by_mech[mid]))]
    links = sorted(set(m.get("depends_on", []) + m.get("interacts_with", [])))
    if links:
        out += ["", S["interactions"] + ", ".join(links)]
    opens = m.get("open_unknowns", [])
    if opens:
        out += ["", S["open"], ""]
        out += [f"- {unknown_link(u)} ({L.name(unknowns[u]['priority']) if L.code != 'en' else unknowns[u]['priority']}): "
                f"{L.get(u, 'question', unknowns[u]['question'])}" for u in opens if u in unknowns]
    if contra_by_mech.get(mid):
        out += ["", S["contradictions"] + ", ".join(f"{unknown_link(c)}" for c in sorted(contra_by_mech[mid]))]
    if m.get("notes"):
        out += ["", S["notes"].format(mid) + ": " + " ".join(L.get(mid, "notes", m["notes"]).split())]
    return out + [""]


def page(title, mechs, unknowns, contra_by_mech, theorems_by_mech, intro, L):
    S = L.s
    labels = [m["label"] for m in mechs]
    counts = ", ".join(f"{labels.count(l)} `{l}`" for l in reversed(STRENGTH) if labels.count(l))
    opens = sorted({u for m in mechs for u in m.get("open_unknowns", [])})
    tested = sorted({t for m in mechs for t in theorems_by_mech.get(m["id"], [])})
    out = [f"# {title}", "", S["summary"], "", intro, "", S["gathers"].format(n=len(mechs), counts=counts), "", S["rules"], ""]
    for m in mechs:
        out += mechanic_block(m, unknowns, contra_by_mech, theorems_by_mech, L)
    out += [S["simcheck"], "",
            (S["tested"] + ", ".join(f"[{t}](../theorems/{t}.md)" for t in tested)) if tested else S["untested"], "",
            S["openh"], "", ", ".join(unknown_link(u) for u in opens) if opens else S["none"], "",
            S["confidence"], "", S["lowest"].format(lowest(labels)), ""]
    return "\n".join(out)


def theorems(theory_dir):
    """Extract each '**Theorem T-xxxx' (or '**정리 T-xxxx') section verbatim from theory/*.md, with its file and cited mechanics."""
    found = {}
    for f in sorted(theory_dir.glob("*.md")):
        text = f.read_text("utf-8")
        starts = [m.start() for m in re.finditer(r"^\*\*(?:Theorem|정리) T-\d{4}", text, re.M)]
        for i, s in enumerate(starts):
            nxt = [p for p in (text.find("\n## ", s), text.find("\n### ", s),
                               starts[i + 1] if i + 1 < len(starts) else -1) if p > 0]
            body = text[s:min(nxt) if nxt else len(text)].strip()
            tid = re.match(r"\*\*(?:Theorem|정리) (T-\d{4})", body).group(1)
            found[tid] = (f.name, body, set(re.findall(r"\bM-\d{4}(?!\d)", body)))
    return found


# an id not already inside a link; Hangul may touch it on either side (Korean particles follow ids)
ID = re.compile(r"(?<![\[#/A-Za-z0-9_-])([MUCT])-(\d{4})(?![\d\]])")


def linkify(text, prefix, family_of):
    """Make every M-, U-, C-, T- id a link; prefix is the path from the page to codex/. Headings stay plain."""
    def sub(m):
        i = f"{m.group(1)}-{m.group(2)}"
        if m.group(1) == "M":
            fam = family_of.get(i)
            return f"[{i}]({prefix}rules/{fam}.md#{i.lower()})" if fam else i
        if m.group(1) == "T":
            return f"[{i}]({prefix}theorems/{i}.md)"
        return f"[{i}]({prefix}unknowns.md#{i.lower()})"
    return "\n".join(l if l.startswith(("#", "<a ")) else ID.sub(sub, l) for l in text.split("\n"))


def plain(L, key):
    text = L.intro(key)
    if text is None and L.code != "en":
        L.missing.append(key)
    return f"\n\n{L.s['plain']}\n\n{text.strip()}" if text else ""


def write(path, text, prefix, family_of):
    path.write_text(linkify(text, prefix, family_of), "utf-8", newline="\n")


def main(code="en"):
    L = Lang(code)
    S = L.s
    codex = ROOT / "codex" if code == "en" else ROOT / code / "codex"
    theory_dir = ROOT / "theory" if code == "en" else ROOT / code / "theory"
    mechs, unknowns, contras = load("mechanics"), load("unknowns"), load("contradictions")
    family_of = {m["id"]: m["family"] for m in mechs.values()}
    ipath = ROOT / "codex" / "intros.yaml"  # hand-written plain-language explanations, every fact tagged with its id
    INTROS.update(yaml.safe_load(ipath.read_text("utf-8")) if ipath.exists() else {})
    contra_by_mech = defaultdict(set)
    for c in contras.values():
        for m in c.get("mechanics", []):
            contra_by_mech[m].add(c["id"])
    thms = theorems(theory_dir)
    theorems_by_mech = defaultdict(set)
    for tid, (_, _, ms) in thms.items():
        for m in ms:
            theorems_by_mech[m].add(tid)
    if code != "en":
        en_thms = set(theorems(ROOT / "theory"))
        L.missing += [f"theorem {t}" for t in sorted(en_thms - set(thms))]
    for sub in ("rules", "sigils", "theorems"):
        (codex / sub).mkdir(parents=True, exist_ok=True)

    families = defaultdict(list)
    for m in mechs.values():
        families[m["family"]].append(m)
    pages = []
    for fam, ms in sorted(families.items()):
        intro = S["fam_intro"].format(fam) + plain(L, f"family:{fam}")
        pages.append((codex / "rules" / f"{fam}.md", page(S["fam_title"].format(L.name(fam, family=True)), ms, unknowns, contra_by_mech, theorems_by_mech, intro, L), "../"))
    for s in SIGILS:
        ms = [m for m in mechs.values() if s in m["sigils"]]
        intro = S["sig_intro"].format(L.name(s)) + plain(L, f"sigil:{s}")
        pages.append((codex / "sigils" / f"{s}.md", page(S["sig_title"].format(L.name(s)), ms, unknowns, contra_by_mech, theorems_by_mech, intro, L), "../"))
    for tid, (fname, body, _) in sorted(thms.items()):
        pages.append((codex / "theorems" / f"{tid}.md",
                      S["thm_head"].format(tid=tid, f=fname)
                      + body.replace("](", "](../../theory/").replace("](../../theory/http", "](http") + "\n", "../"))

    out = [S["u_title"], "", S["u_intro"], ""]
    counts = {p: sum(1 for u in unknowns.values() if u["priority"] == p and u["status"] == "open") for p in PRIORITY}
    prio = (lambda p: p) if code == "en" else L.name
    out += [S["u_counts"].format(", ".join(f"{counts[p]} {prio(p)}" for p in PRIORITY), len(unknowns)), ""]
    for p in PRIORITY:
        out += [S["u_prio"].format(prio(p)), ""]
        for u in sorted((u for u in unknowns.values() if u["priority"] == p), key=lambda u: u["id"]):
            i = u["id"]
            out += [f"### {i}", "", f"{i}: {L.get(i, 'question', u['question'])} {S['status'].format(u['status'])}", "",
                    f"{S['why'].format(i)}: {L.get(i, 'why_it_matters', u['why_it_matters'])}", ""]
            for k, v in L.get(i, "readings", u.get("readings") or {}).items():
                out.append(f"- {i} {S['reading']} {k}: {v}")
            if u.get("parameter"):
                out.append(S["free"].format(i, u["parameter"], L.get(i, "sweep_range", u.get("sweep_range")) or S["sweep_default"]))
            out += [f"- {i} {S['resolution']}: {r}" for r in L.get(i, "resolution_paths", u["resolution_paths"])]
            if u.get("resolution"):
                out.append(f"- {i} {S['resolved']}: {L.get(i, 'resolution', u['resolution'])}")
            out.append("")
    out += [S["c_title"], ""]
    for c in sorted(contras.values(), key=lambda c: c["id"]):
        i = c["id"]
        out += [f"### {i}", "", f"{i}: {L.get(i, 'summary', c['summary'])} {S['status'].format(c['status'])}", ""]
        quotes = L.get(i, "quotes", [s["quote"] for s in c["sides"]])
        for s, q in zip(c["sides"], quotes):
            out.append(f"- {i} `{s['clause']}`: \"{s['quote']}\" ([{S['source']}]({s['url']}))")
            if code != "en":
                out.append(f"  - 번역: {q}")
        out.append("")
    pages.append((codex / "unknowns.md", "\n".join(out), ""))
    idx = [S["i_title"], "", S["i_intro"], "", S["i_sigils"], ""]
    idx += [f"- [{S['sig_title'].format(L.name(s))}](sigils/{s}.md)" for s in SIGILS]
    idx += ["", S["i_families"], ""] + [f"- [{L.name(f, family=True)}](rules/{f}.md): {S['i_n'].format(len(ms))}" for f, ms in sorted(families.items())]
    idx += ["", S["i_thms"], ""] + [f"- {t}: {S['i_from'].format(thms[t][0])}" for t in sorted(thms)]
    idx += ["", S["i_open"], "", S["i_all"], "", S["i_every"], ""]
    idx += [f"- {m['id']}: {L.get(m['id'], 'name', m['name'])} (`{m['label']}`)" for m in sorted(mechs.values(), key=lambda m: m["id"])]
    pages.append((codex / "index.md", "\n".join(idx) + "\n", ""))
    if L.missing:
        sys.exit(f"{code}: {len(L.missing)} missing translation(s), nothing written: {', '.join(L.missing[:40])}")
    for path, text, prefix in pages:
        write(path, text, prefix, family_of)
    print(f"{code}: rules {len(families)} pages, sigils {len(SIGILS)}, theorems {len(thms)}, unknowns {len(unknowns)}, contradictions {len(contras)}")


if __name__ == "__main__":
    main(sys.argv[sys.argv.index("--lang") + 1] if "--lang" in sys.argv else "en")
