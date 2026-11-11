# Safe Zone Codex (work in progress)

A formal reconstruction of the rule system of Safe Zone, the IRL survival event hosted by Ice Poseidon, built from the official wiki (https://iceposeidon.com/safezone/wiki, snapshot of 2026-11-11). Every rule is quoted word for word, translated into a formal definition, and every ambiguity is kept open as a list of competing readings until evidence settles it.

**Status: WIP.** Phases 0 to 3 are done; theory, simulator, strategy and the final Codex review are partial. Nothing here is endorsed by the organizers.

## What is done

| Part | State |
|---|---|
| Corpus (`corpus/`) | 20 wiki pages fetched politely, hashed in `corpus/manifest.json`; 607 clauses in `corpus/clauses/` |
| Knowledge base (`kb/`) | 296 mechanics, 204 open questions, 26 contradictions between pages; all 607 clauses covered (`tools/check_kb.py --coverage` passes) |
| Reverse engineering (`re/findings/`) | The wiki's client code holds no game data (RE-0001); API hosts recorded, never called (RE-0003) |
| Theory (`theory/`) | 00 notation, 01 hit pipeline, 02 rounding, 05 survival clocks, 10 statistical validation; theorems T-0001 to T-0014 |
| Tests (`sim/tests/`) | 15 tests, exhaustive or property-based, one per theorem |
| Codex (`codex/`) | Generated from the KB by `tools/build_codex.py`: rules by family, one page per sigil, one page per theorem, `codex/unknowns.md` |

## Not done yet

Theory 03, 04, 06 to 09 (healing, Eddie's potion, economy, zombies, sigil game theory, viewer economics); the simulator engine; tier lists and strategy (`codex/strategy/`); `tools/check_codex.py`; an adversarial review of every theorem and Codex page. Viewer attack prices and the number of contestants are not on the wiki, so viewer economics and last-survivor models wait on them (`codex/unknowns.md`, U-0014 and U-0009).

## How to read it

Start with `codex/unknowns.md` (what the wiki leaves open), then `codex/sigils/` and `codex/rules/`. Each statement carries a label: `DOCUMENTED` (the wiki says it), `DERIVED` (proven from documented rules), `CONDITIONAL` (proven under one named reading of an open question), `HYPOTHESIS`, `CONTRADICTED`, `UNKNOWN`.

A few results so far:

- Being live on Kick gives no attack bonus on hits of 9 HP or less (T-0001); the defensive 10% either removes 1 HP from nearly every small hit or nothing at all, depending on a rounding the wiki does not settle (T-0002, U-0001).
- If re-poisoning restarts the poison tick clock, re-poisoning a target every 89 seconds or less means it never takes poison damage (T-0009, conditional on U-0116).
- With max HP capped, death is certain in the long run but can take astronomically long; the useful number is survival over the event's duration (T-0014).
- If the server computes Ingenuity prices in floating point, an Ingenuity contestant pays 939 instead of 935 tokens for ten max-HP upgrades (H-0001, checkable on one merchant screen).

## Reproduce

```
py -3 -m venv .venv
.venv\Scripts\python -m pip install numpy scipy pyyaml jsonschema pytest hypothesis matplotlib
.venv\Scripts\python -m pytest sim -q
.venv\Scripts\python tools\check_kb.py --coverage
.venv\Scripts\python tools\lint_text.py
.venv\Scripts\python tools\build_codex.py
```

## Scope and ethics

See `SCOPE.md`. Only public wiki pages are read, at most one request per second. No game API is called. No contestant's location is collected. Older snapshots (October 2026, an earlier edition) are kept as history in `corpus/diffs/` and never used as rules. All rule text belongs to its authors and is quoted with its source URL and date.
