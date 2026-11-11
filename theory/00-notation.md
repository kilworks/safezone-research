# 00. Notation and conventions

This file fixes the symbols used in every other file of `theory/` and in the Codex.

## Source of the rules

Every rule comes from the official wiki snapshot of 2026-11-11 (`corpus/manifest.json`). Older captures in `corpus/diffs/` describe an earlier edition of the event and are history only: no theorem, model or simulation uses them.

## Symbols

| Symbol | Meaning | Unit |
|---|---|---|
| $h$ | current HP of a contestant | HP (integer) |
| $M$ | maximum HP of a contestant | HP (integer) |
| $d$ | an integer amount of damage before a step of the hit pipeline | HP |
| $t$ | time since an event | seconds (integer unless stated) |
| $p$ | a merchant base price | blood tokens (integer) |
| $k$ | number of previous purchases of the same upgrade | count |
| $n$ | number of trials, purchases or contestants, as stated locally | count |
| $\lfloor x \rfloor$, $\lceil x \rceil$ | floor and ceiling | |
| $\mathbb{1}[P]$ | 1 if $P$ holds, else 0 | |
| $a \mid b$ | $a$ divides $b$ | |
| $\Phi(d, s)$ | HP actually lost by a defender in state $s$ from a raw hit $d$ | HP |

All HP, damage, prices and durations are integers unless a record in `kb/` proves otherwise. Percentages are written as exact fractions: "10% less, rounded down" is $\lfloor 9d/10 \rfloor$ or $d - \lfloor d/10 \rfloor$, never $0.9d$.

## Identifiers

| Prefix | What | Where |
|---|---|---|
| `M-xxxx` | a formal mechanic | `kb/mechanics/` |
| `U-xxxx` | an open question (unknown) | `kb/unknowns/` |
| `E-xxxx` | an evidence record | `kb/evidence/` |
| `C-xxxx` | a contradiction between sources | `kb/contradictions/` |
| `T-xxxx` | a theorem, stated in `theory/` | `theory/*.md`, tested in `sim/tests/` |
| `H-xxxx` | a hypothesis about the implementation | `theory/*.md` |
| `RE-xxxx` | a reverse-engineering finding | `re/findings/` |
| clause id (`wiki-damage-047`) | one sentence or table row of a wiki page | `corpus/clauses/` |

## Confidence labels

Every statement carries one label: `DOCUMENTED` (the wiki says it, verbatim quote), `DERIVED` (follows from documented rules alone, with a proof or an exhaustive test), `CONDITIONAL` (follows from documented rules plus one named reading of an unknown), `CORROBORATED` (independent evidence agrees), `HYPOTHESIS` (plausible, unproven, with the test that would decide it), `CONTRADICTED` (sources disagree) and `UNKNOWN`.

## Proof by exhaustion

When a claim is about integers in a bounded domain, the proof is a committed test that checks every value. When the domain is unbounded but the claim is periodic (for example a difference of two floor expressions that repeats every 20 values), the proof states the period algebraically and the test checks one full period, plus a margin. A test checks our model of a rule, never the game: where a test is the only evidence, the text says so.
