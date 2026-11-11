# 01. The hit pipeline

The damage page says: "Every hit goes through these steps in order." (M-0117). This file writes each step as a map on (damage, defender state), states what the composition does, and lists what the text leaves open.

## The seven maps

Write the HP a defender loses from a raw hit $d$ as

$$
\Phi = A \circ F \circ \mu \circ R \circ \rho \circ K \circ I .
$$

| Step | Map | Mechanic | Definition | Side effects | Open |
|---|---|---|---|---|---|
| 1 | $I$ immunity | M-0118 | $I(d) = 0$ if any active blocker covers this damage source (the table of M-0140 to M-0166), else $d$ | a Flak jacket or Mirror is used up (M-0130, M-0134) | U-0120: which blocker is consumed when several apply |
| 2 | $K$ attacker Kick bonus | M-0119 | $K(d) = \lfloor 11d/10 \rfloor$ if the attacker is live on Kick and the source is one of the listed weapons, else $d$ | none | U-0010 (staff ticks); C-0100: the intro states a general 10% bonus, the pipeline lists weapons only |
| 3 | $\rho$ mirror | M-0120, M-0135 | if the defender has a Mirror forcefield and the source is reflectable, the defender takes 0 and the whole hit, before any reduction, goes to the attacker | Mirror used up | U-0005: does the reflected hit run the attacker's own pipeline? |
| 4 | $R$ reductions | M-0121, M-0122 | $R(d) = r_{\text{Kick}}(h_P(d))$, with $h_P(d) = \lfloor d/2 \rfloor$ for a nuke on a Protection contestant, else $d$; $r_{\text{Kick}} = R_A$ or $R_B$ if the defender is live, else identity | none | U-0001 (reading A or B), U-0100 (where the rounding sits) |
| 5 | $\mu$ minimum | M-0123 | $\mu(d) = \max(d, 1)$ for a hit that got through steps 1 and 3 | none | U-0002 (which sources are hits), U-0103 |
| 6 | $F$ fortress | M-0124 | $F(d) = d - \min(d, f)$, with $f$ the remaining durability of a fortress the defender stands within | $f \leftarrow f - \min(d, f)$, shared by everyone in range, "whoever built it" | U-0102 (several fortresses) |
| 7 | $A$ armor | M-0125 | $A(d) = d - \min(d, a)$, with $a$ the armor's remaining durability (15 new, M-0126 and the items page) | $a \leftarrow a - \min(d, a)$; armor breaks at 0 | U-0101 (does the excess of the breaking hit pass?) |

The arithmetic of steps 2 and 4 is settled in `theory/02-rounding-and-arithmetic.md`: T-0001 (single reading of the bonus), T-0002 (two readings of the reduction), T-0003 (order of halving and Kick reduction), T-0004 (when the minimum matters).

## T-0007: fortress and armor as one ordered pool

**Theorem T-0007.** Take a defender with a fortress of remaining durability $f$ and armor of remaining durability $a$, hit in order by $x_1, \dots, x_m \ge 1$ (values after step 5), with no repair or decay in between. Under reading A of U-0101 (excess of the hit that breaks a layer passes to the next layer):

- HP lost after the $j$-th hit: $\max(S_j - f - a,\ 0)$ with $S_j = x_1 + \dots + x_j$;
- fortress durability left: $f - \min(S_j, f)$; armor durability left: $a - \min(\max(S_j - f, 0), a)$.

*Proof.* By induction on $j$. Each layer absorbs $\min(x, \text{remaining})$ and passes the rest, so after any prefix the fortress has absorbed $\min(S_j, f)$ and the armor $\min(\max(S_j - f, 0), a)$: if the claim holds after $j-1$ hits, the $j$-th hit first fills what is left of the fortress, then what is left of the armor, then reaches HP, which is exactly the claim for $S_j = S_{j-1} + x_j$. $\square$

*Consequence.* Under reading A, the order and size of the hits do not matter: a fresh body armor (15) plus a full fortress (30) absorb the first 45 HP of damage of any kind they cover, whether it comes as one 45 HP hit or as forty-five 1 HP ticks. Under reading B (the excess of the hit that breaks the armor is lost), a large hit on nearly broken armor is partly wasted, so big hits lose value against armor: the defender saves at most one hit's overflow over the whole sequence.

*Caveats.* The fortress is shared with everyone within 20 m, so $f$ falls with other contestants' hits too. Armor enchantment changes $a$ over time (+10 up to 45, then -1 every 20 min down to 15, merchant page), which this theorem excludes. Whether 1 HP ticks reach steps 6 and 7 at all is U-0002. A trapped gift ignores body armor (items page), against the damage page's "Body Armor works on every kind of damage" (C-0102).

*Label:* `DERIVED` for the arithmetic; `CONDITIONAL` on U-0101 for the game. *Test:* `sim/tests/test_pipeline_theorems.py` (property test plus exhaustive check of all sequences of up to 3 hits of 1 to 12 HP; a deliberately wrong closed form is caught on 12 of 12 sample cases).

## What the pipeline does not say

| Question | Unknown |
|---|---|
| Do zone ticks, poison, bleeding, zombie drain, the robot, Eddie's loss, the revive cost and Retribution go through the pipeline? | U-0002 |
| Is the Kick reduction a floor of the result or of the removed part? | U-0001 |
| Does a reflected hit run the attacker's pipeline? | U-0005 |
| Which blocker is consumed when two apply? | U-0120 |
| Can steps 6 and 7 absorb the last HP that step 5 guarantees? | U-0103 |
| Does armor's breaking hit pass its excess? | U-0101 |

Contradictions bearing on the pipeline: C-0100 (scope of the Kick attack bonus), C-0101 and C-0200 (trapped gift and mirror), C-0102 and C-0201 (trapped gift and armor), C-0103 and C-0600 (Death Ward scope).
