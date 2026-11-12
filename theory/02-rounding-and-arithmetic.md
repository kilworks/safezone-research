# 02. Rounding and arithmetic

> **Adversarial review, 2026-11-11:** T-0004 was found BROKEN by a fresh reviewer and corrected the same day. A second fresh reviewer re-attacked the corrected version (exhaustive check of d = 1..4999 over every modifier and reading) and found it UPHELD. The other theorems on this page were UPHELD at the first review.

The wiki states its percentage rules in words: "10% more, rounded down", "50% less", "15% more, rounded down", "10% higher, rounded up". This file turns each into exact integer arithmetic, proves which phrasings have a single meaning and which have two, and measures where code written with floating-point numbers would drift from the exact rule.

Tests: `sim/tests/test_arith_theorems.py` (exhaustive). Drift table: `analysis/scripts/float_drift.py`, output `analysis/results/float_drift.json`. Implementation: `sim/safezone_sim/arith.py`.

## A lemma used everywhere

**Lemma.** For every integer $n$ and real $x$, $\lfloor n + x \rfloor = n + \lfloor x \rfloor$ and $\lfloor -x \rfloor = -\lceil x \rceil$.

Both follow from the definition of the floor as the largest integer not above its argument.

## T-0001: the attacker's Kick bonus has a single reading

**Theorem T-0001.** For every integer $d \ge 0$: $\lfloor 11d/10 \rfloor = d + \lfloor d/10 \rfloor$.

*Rule:* M-0119 (pipeline step 2), quote "deal 10% more, rounded down".
*Proof.* $11d/10 = d + d/10$ and $d$ is an integer, so the lemma gives the result. $\square$
*Consequence.* "10% more, rounded down" means the same whether the total or the bonus is rounded. The bonus is $\lfloor d/10 \rfloor$, so it adds nothing to hits of 9 HP or less: a live attacker's bow (5 HP), knife (5 HP), fake chest (5 HP) and Zarok's axe at full health (5 HP) do exactly what an offline attacker's do. A 10 HP hit becomes 11, a 20 HP hit 22. These are base values: an enchanted weapon deals +10 (M-0338), so an enchanted bow hits for 15 and a live attacker's for 16.
*Label:* `DERIVED`. *Test:* `test_t0001_kick_attack_single_reading`, every $d$ in $0..10000$.

## T-0002: the defender's Kick reduction has two readings

**Theorem T-0002.** Let $R_A(d) = \lfloor 9d/10 \rfloor$ (the result is rounded down) and $R_B(d) = d - \lfloor d/10 \rfloor$ (the removed 10% is rounded down). For every integer $d \ge 0$:

$$
R_A(d) = d - \lceil d/10 \rceil, \qquad R_B(d) - R_A(d) = \mathbb{1}[10 \nmid d].
$$

*Rule:* M-0122 (pipeline step 4b), quote "Being live on Kick then takes off 10%, rounded down."; open question U-0001.
*Proof.* $\lfloor d - d/10 \rfloor = d + \lfloor -d/10 \rfloor = d - \lceil d/10 \rceil$ by the lemma. Then $R_B - R_A = \lceil d/10 \rceil - \lfloor d/10 \rfloor$, which is 0 when $10 \mid d$ and 1 otherwise. $\square$
*Consequence.* Under A, every hit from 2 to 10 HP loses exactly 1 HP and a 1 HP hit is reduced to 0 (then raised back to 1 by the minimum step, T-0004). Under B, hits below 10 HP are not reduced at all. So "you take 10% less damage" is worth either about 1 HP on every small hit or nothing on small hits. Zone ticks of 1 HP are unchanged under both readings.
*Label of the theorem:* `DERIVED`. *Label of the in-game behavior:* `CONDITIONAL` on U-0001. *Test:* `test_t0002_kick_defense_two_readings`.

## T-0003: Protection's nuke halving and the Kick reduction almost commute

The damage page orders step 4 as: halve a nuke for a Protection contestant, round down, then apply the Kick reduction (M-0121, M-0122; where exactly the "damage left is rounded down" sits is U-0100). Does the order matter?

**Theorem T-0003.** Let $H(d) = \lfloor d/2 \rfloor$. For every integer $d \ge 0$:

- under reading A, $R_A(H(d)) - H(R_A(d)) = -\mathbb{1}[d \bmod 20 \in \{3,5,7,9\}]$;
- under reading B, $R_B(H(d)) - H(R_B(d)) = \mathbb{1}[d \bmod 20 \in \{10,12,14,16,18\}]$.

*Proof.* For $R \in \{R_A, R_B\}$ we have $R(x+10) = R(x) + 9$ and $R(x+20) = R(x)+18$, and $H(x+20) = H(x)+10$, $H(x+18) = H(x)+9$. Hence both $g_1 = R \circ H$ and $g_2 = H \circ R$ satisfy $g(d+20) = g(d) + 9$, so $g_1 - g_2$ has period 20. Checking $d = 0, \dots, 19$ gives the residues above; the test checks every $d$ up to 10000. $\square$
*Consequence.* The viewer nuke of 20 HP gives 9 HP to a live Protection contestant in either order and under either reading. The order matters only for admin nukes with other damage values, and then by exactly 1 HP.
*Label:* `DERIVED` for the arithmetic; the order itself is `DOCUMENTED` (M-0117). *Test:* `test_t0003_protection_nuke_and_kick_order`.

## T-0004: when the 1 HP minimum changes the outcome

**Theorem T-0004.** With the documented order of step 4, the minimum step (M-0123, "A hit that gets through always does at least 1 HP") changes the step-5 output (not necessarily the final HP loss, since fortress and armor come after) of a raw hit $d \ge 1$ exactly in these cases:

| Defender state | Reading A | Reading B |
|---|---|---|
| live on Kick | $d = 1$ | never |
| Protection, nuke, offline | $d = 1$ | $d = 1$ |
| Protection, nuke, live, two successive floors (U-0100 reading A) | $d \in \{1,2,3\}$ | $d = 1$ |
| Protection, nuke, live, one final floor $\lfloor 9d/20 \rfloor$ (U-0100 reading B) | $d \in \{1,2\}$ | not defined by U-0100 B |
| any other | never | never |

*Proof.* The minimum changes the outcome iff the reduced value is 0 while $d \ge 1$. $R_A(d) = 0 \iff 9d < 10 \iff d = 1$; $R_B(d) = d - \lfloor d/10 \rfloor \ge 1$ for $d \ge 1$; $H(d) = 0 \iff d = 1$; $R_A(H(d)) = 0 \iff H(d) \le 1 \iff d \le 3$; with one final floor, $\lfloor 9d/20 \rfloor = 0 \iff 9d < 20 \iff d \le 2$; $R_B(H(d)) = 0 \iff H(d) = 0 \iff d = 1$. The attacker's Kick bonus (step 2) leaves every row unchanged: $\lfloor 11d/10 \rfloor = d$ for $d \le 9$, and every row only involves $d \le 3$. $\square$
*Consequence.* The minimum step matters only for hits of 3 HP or less. No documented attack deals that little except the 1 HP ticks (zone, unsafe circle, robot, poison, bleeding, airstrike fire, zombie drain) and the 2 HP ticks (guard zombies, tear gas), plus Wizard staff ticks if a staff area ticks (U-0010). Whether those ticks are "hits" that go through the pipeline is U-0002. Whether fortress and armor can still absorb that last HP is U-0103.
*Label:* `DERIVED` for each row as stated; which row applies is `CONDITIONAL` on U-0100, which column on U-0001, the minimum acting at step 5 on M-0123 reading A (reading B puts it after steps 6 and 7), and the in-game relevance on U-0002. *Test:* `test_t0004_minimum_step_changes_outcome_only_for_tiny_hits`.

## T-0005: Piety's potion bonus has a single reading

**Theorem T-0005.** For every integer $x \ge 0$: $\lfloor 115x/100 \rfloor = x + \lfloor 15x/100 \rfloor$.

*Proof.* The lemma with $n = x$. $\square$
*Consequence.* Piety potions heal $5, 11, 23, 46$ HP for the small, medium, large and gigantic tiers (base $5, 10, 20, 40$). The small potion gains nothing from the bonus ($5.75$ rounds down to 5).
*Label:* `DERIVED`, given that potion tiers and the Piety rule are `DOCUMENTED`. *Test:* `test_t0005_piety_bonus_readings_coincide`.

## T-0006: the merchant ladder

**Theorem T-0006.** If the $k$-th purchase ($k = 0, 1, \dots$) of an inventory slot or of +10 max HP costs $40 + 10k$ blood tokens, the first $n$ purchases cost $C(n) = 5n^2 + 35n$. In particular $C(10) = 850$ (max HP from 100 to 200). One max-HP point bought at purchase $k$ costs $4 + k$ tokens.

*Proof.* $\sum_{k=0}^{n-1}(40 + 10k) = 40n + 10\,n(n-1)/2 = 5n^2 + 35n$. $\square$
*Ingenuity.* Ingenuity pays 10% more, rounded up. Every ladder price is a multiple of 10, so $\lceil 11p/10 \rceil = 11p/10$ exactly, and the ten max-HP purchases cost $1.1 \times 850 = 935$ tokens.
*Label:* `DERIVED`; whether the slot and HP ladders share one counter is a question of the merchant formalization. *Test:* `test_t0006_merchant_ladder`.

## Floating-point drift (H-0001)

The servers compute in some language, most likely with IEEE 754 binary64 numbers. A programmer writing `Math.floor(x * 1.1)` instead of exact integer arithmetic gets a different answer whenever the binary64 product lands just below or above an integer. `analysis/scripts/float_drift.py` measures this for every multiplier the wiki states, over the whole domain of each quantity, in Python and in Node.js (both use binary64 and agree on every value):

| Rule | Code a programmer might write | Domain | Values where it differs from the exact rule |
|---|---|---|---|
| Kick attack bonus | `Math.floor(d * 1.1)` | $0..500$ | none |
| Kick defense, reading A | `Math.floor(d * 0.9)` | $0..500$ | none |
| Protection nuke, Protection potions, Eddie's +50% | `Math.floor(x * 0.5)` | $0..500$ | none |
| Eddie's -30% (floor or ceil), Death 5%, Death 60% cap, 20% alive, crown 20% | `* 0.3`, `* 0.05`, `* 0.6`, `* 0.2` | their domains | none |
| Piety +15% | `Math.floor(h * 1.15)` | $0..400$ | 100, 180, 200, 220, 340, 360, 380, 400 |
| Ingenuity prices | `Math.ceil(p * 1.1)` | $1..400$ | 19 values: 50, 90, 100, 110, 170, ..., 400 |

**Hypothesis H-0001 (Ingenuity price drift).** If the server computes Ingenuity prices as `ceil(price * 1.1)` in binary64, an Ingenuity contestant pays one blood token more than the rule at base prices 50, 90, 100 and 110: Dual Wield (base 50) costs 56 instead of 55, and the ten max-HP upgrades cost 939 tokens instead of 935. Test: one Ingenuity merchant screen in a VOD (U-0006). *Label:* `HYPOTHESIS`.

The Piety drift values (100, 180, ...) are not potion heals: the four documented heals 5, 10, 20, 40 are unaffected, so the Piety drift cannot happen with the documented potions.
