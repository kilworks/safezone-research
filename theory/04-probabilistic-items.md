# 04. Probabilistic items: Eddie's potion and every stated chance

> **Adversarial review, 2026-11-12:** two fresh reviewers found T-0402, T-0404, T-0406 and T-0407 BROKEN. Corrected the same day: T-0402 now names U-0103, U-0209, U-0338, U-0339 and every reading of U-0617 and U-0618; T-0404(b) now names the readings of U-0004 (its first example failed under reading C; a new example holds under readings A and C); the false claim of T-0406 ("when not drinking means certain failure, drinking now is optimal") is replaced by the true one (never drinking is then not optimal) and a counterexample; T-0407 states both forms of the per-encounter roll. The other theorems were relabeled where a reading was missing.

A handful of rules in the wiki involve luck: Eddie's potion (10% to heal half your max HP, otherwise lose 30%), zombies breaking health potions (10%) and destroying crafts (40%), the Greed chest Shield (25%) and the Trolling care package diversion (3%). This chapter answers two questions a player cares about. First, what exactly does one roll do, with whole-number HP and every rounding rule spelled out? Second, when is it rational to take the gamble? For Eddie's potion the answer is not "when the average is positive": the average HP change is positive exactly at the HP levels where a drink kills you nine times out of ten. The right question is whether drinking raises your probability of surviving, and that depends on what is about to happen to you (theory/05).

Everything here is computed with exact fractions (`fractions.Fraction`), never with floating point. Tests: `sim/tests/test_04_probabilistic.py`, helpers in `sim/safezone_sim/ch04.py`. A test checks our model of a rule, never the game itself.

Notation is that of `theory/00-notation.md`: $M$ max HP, $h$ current HP, both integers. For Eddie's potion we write $g$ for the heal amount, $\ell$ for the loss amount, $h^+ = \min(M, h + g)$ for HP after a success and $h^-$ for HP after a failure.

## 4.1 One drink of Eddie's potion

The rule (M-0208, items page, clauses `wiki-items-011` and `wiki-items-012`): "A gamble: 10% chance to heal 50% of your max HP." "Otherwise you lose 30% of your max HP." The damage page lists "Eddie's Potion backfire" as stopped by "Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" (M-0165, `wiki-damage-030`). Open: how 50% and 30% are rounded (U-0204), whether the heal is capped at max HP (U-0203), whether the loss can kill and whether the hit pipeline applies to it (U-0004, U-0002).

### T-0400: when rounding matters, and which max HP values exist

**Theorem T-0400.** (a) For every integer $M \ge 1$, the three roundings of U-0204 (floor, ceiling, round half up) give the same heal $g$ if and only if $M$ is even, and the same loss $\ell$ if and only if $10 \mid M$. So all readings of U-0204 agree exactly when $10 \mid M$, and then $g = M/2$, $\ell = 3M/10$. Round half up differs from floor on the loss exactly when $M \bmod 10 \in \{2, 3, 5, 6, 9\}$.
(b) If max HP changes only through the sigil bases (Greed 90, Piety 110, every other sigil 100: M-0508, M-0500, M-0515, M-0530, M-0602 to M-0606) and the merchant's +10 upgrades capped at 200, or 220 for Piety (M-0333), then the reachable max HP values are $\{90, 100, 110, \dots, 220\}$, all multiples of 10, under both readings of U-0330 (no purchase limit: up to 220; 10 purchases at most: up to 210).

| $M$ | 90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 | 190 | 200 | 210 | 220 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| heal $g$ | 45 | 50 | 55 | 60 | 65 | 70 | 75 | 80 | 85 | 90 | 95 | 100 | 105 | 110 |
| loss $\ell$ | 27 | 30 | 33 | 36 | 39 | 42 | 45 | 48 | 51 | 54 | 57 | 60 | 63 | 66 |

*Proof.* (a) $M/2$ is an integer iff $M$ is even; otherwise its fractional part is $1/2$, and floor differs from ceiling and from round half up. $3M/10$ is an integer iff $10 \mid 3M$, iff $10 \mid M$ since $\gcd(3, 10) = 1$; otherwise floor and ceiling differ. Round half up equals floor iff the fractional part of $3M/10$, which is $(3M \bmod 10)/10$, is below $1/2$, iff $3M \bmod 10 \in \{1, 2, 3, 4\}$, iff $M \bmod 10 \in \{7, 4, 1, 8\}$; with $M \bmod 10 = 0$ (integer) that leaves $\{2, 3, 5, 6, 9\}$ where they differ. (b) Bases are multiples of 10 and each upgrade adds 10. $\square$

*Scope of (b).* The clauses of the 2026-11-11 corpus that mention max HP are the sigil base labels and the Piety and Greed sentences, the +10 upgrade and its cap, Eddie's potion, the Death gravestone heal of 5% of max HP, the Death 60% cap and Healing regeneration up to max HP (found by a text search of `corpus/clauses/`); none changes max HP other than the bases and the upgrade. That is the absence of a rule in the text, not proof that the game has no other modifier.

*Label:* (a) `DERIVED`. (b) `CONDITIONAL` on "no other max-HP modifier exists" (not recorded as a U-id; the corpus states none). Under (b) every reading of U-0204 gives the same numbers, so the rest of the chapter uses $g = M/2$, $\ell = 3M/10$ for reachable $M$ and checks every other integer $M$ from 4 to 220 under all nine rounding pairs. *Test:* `test_t0400_rounding_readings_and_reachable_max_hp` (every $M$ from 1 to 220, nine rounding pairs).

### T-0401: the exact law of one drink, and why the average misleads

Base model: no blocker, no armor, not live on Kick, the loss can kill (U-0004 reading A), the heal is capped at $M$ (U-0203 reading A), the 10% roll is independent of everything else (open question Q4.1 below). Then $h^+ = \min(M, h + g)$ with probability $1/10$ and $h^- = \max(h - \ell, 0)$ with probability $9/10$.

*Modelling choice (not a rule of the game):* HP 0 is death (M-0107), and throughout this chapter death counts as failure, so survival probabilities satisfy $S(0) = 0$. The game lets other contestants revive a dead contestant within 10 minutes (M-0108, M-0112; open: U-0011, U-0107, U-0108), so death is not always final. Counting a revival as survival would raise $S(0)$ above 0 by an amount that depends on who is nearby; every result below that uses $S(0) = 0$ is about not dying, not about staying in the event.

**Theorem T-0401.** Let $a = \min(g, M - h)$ (HP actually gained on a success) and $b = \min(\ell, h)$ (HP actually lost on a failure).

(a) The HP change $\Delta h$ takes the value $+a$ with probability $1/10$ and $-b$ with probability $9/10$, so
$$\mathbb{E}[\Delta h] = \frac{a - 9b}{10}, \qquad \operatorname{Var}(\Delta h) = \frac{9\,(a + b)^2}{100},$$
and the drink kills with probability $9/10$ if $h \le \ell$, never if $h > \ell$.

(b) For every $M$ from 4 to 220 and every rounding pair of U-0204: $\mathbb{E}[\Delta h] > 0$ if and only if $h \le h_E := \lfloor (g - 1)/9 \rfloor$, and every such $h$ is at most $\ell$, so whenever the expected HP change is positive, a drink kills with probability $9/10$. For $h \ge \ell$, $\mathbb{E}[\Delta h] \le (g - 9\ell)/10 < 0$, with equality for $\ell \le h \le M - g$; for reachable $M$ this maximum is $-11M/50$ ($-22$ HP at $M = 100$).

(c) Under U-0004 reading C (the loss cannot take HP below 1), $b = \min(\ell, h - 1)$, the drink never kills, and $\mathbb{E}[\Delta h] > 0$ iff $h \le h_E + 1$.

For reachable $M$, $h_E = 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12$ for $M = 90, 100, \dots, 220$. At $M = 100$: from full HP $\mathbb{E}[\Delta h] = -27$ with variance 81 (standard deviation 9); from $h = 50$, $-22$; from $h = 1$, $+41/10$ HP while dying with probability $9/10$.

*Proof.* (a) Two-point law: mean $\frac{1}{10}a - \frac{9}{10}b$; variance $p(1-p)(a+b)^2$ with $p = 1/10$. Death iff $h - \ell \le 0$. (b) If $h \ge \ell$ then $b = \ell$ and $a \le g$, so $\mathbb{E} \le (g - 9\ell)/10$, with equality iff $a = g$, iff $h \le M - g$ (the range $\ell \le h \le M - g$ is nonempty for reachable $M$, since $3M/10 \le M/2$; the test checks that the maximum is attained). $g < 9\ell$ for $M \ge 4$ (the test checks every case; by hand $g \le M/2 + 1 < 27M/10 - 9 \le 9\ell$ once $M \ge 5$). If $h < \ell$ then $b = h$ and $\mathbb{E} > 0$ iff $a > 9h$. If $9h \ge g$, then $a \le g \le 9h$: not positive. If $9h < g$, then $h \le (g-1)/9 < M/18$, so $M - h > 9h$ and $a = \min(g, M - h) > 9h$: positive. Each such $h$ is below $M/18 < \ell$ (checked for every $M \ge 4$ by the test). (c) Same argument with $b = \min(\ell, h - 1)$: positive iff $9(h - 1) < g$. $\square$

*Consequence.* "Positive expected HP" is the wrong criterion. The average is positive only because a dead contestant cannot lose more than the HP they had: at 1 HP you risk 1 HP to win 50. A contestant who drinks at low HP is not making a good bet on HP; they are trading a 90% chance of death now for a 10% chance of a large heal, and only survival probabilities can say whether that trade is good (T-0403).

*Label:* (a) and (b) `CONDITIONAL` on U-0004 reading A, U-0203 reading A and the roll being a true 1/10 draw (Q4.1). (c) `CONDITIONAL` on U-0004 reading C, U-0203 reading A and Q4.1. Parts (a), (b) and (c) each hold under every reading of U-0204 (all nine rounding pairs are tested); the list of $h_E$ values for reachable $M$ also uses T-0400(b). *Test:* `test_t0401_exact_law_of_one_drink` (every $M$ from 4 to 220, every $h \le M$, nine rounding pairs, both readings of U-0004).

### T-0402: the potion under protection

The damage table (M-0165) says a Shield, a Safety bubble or a Sleeping Bag stops the backfire and Body armor absorbs it. If that is read literally (U-0004 reading B, Eddie's loss is a hit in the sense of U-0002), the potion changes nature.

**Theorem T-0402.** Assume the loss $\ell$ runs through the hit pipeline (M-0117): Kick reduction at step 4 (if live), then Body armor of remaining durability $\alpha$ at step 7, which absorbs $\min(L, \alpha)$ of the loss $L$ that reaches it (U-0101 reading A). Write $L = \ell$ if not live, $L = \lfloor 9\ell/10 \rfloor$ (U-0001 reading A) or $L = \ell - \lfloor \ell/10 \rfloor$ (reading B) if live.

(a) With an active Shield, Sleeping Bag immunity, or while standing inside a Safety bubble (the bubble protects "Everyone inside", M-0213), $\Delta h = +a$ with probability $1/10$ and $0$ with probability $9/10$: $\mathbb{E}[\Delta h] = a/10 \ge 0$, and the drink never kills. A vulnerable contestant gets no protection from a Shield or Safety bubble (M-0129, M-0326). When several blockers apply, which one is used up is U-0120; it does not change HP.

(b) With armor of remaining durability $\alpha$ read as a depleting pool (U-0209 reading A), the HP lost on a failure is $\min(\max(L - \alpha, 0), h)$ and the armor loses $\min(L, \alpha)$ durability, provided the minimum of 1 HP is applied at step 5, before armor (U-0103 reading A; M-0123 reading A). Fresh armor ($\alpha = 15$, M-0217) at $M = 100$ turns the loss of 30 into 15 ($\mathbb{E}[\Delta h] = -17/2$ at $h = 50$). Armor enchanted to durability 45 (M-0339) absorbs the whole loss for every reachable $M \le 150$ ($\ell \le 45$): HP never drops, and the expected durability spent per drink is $9\ell/10$ (27 at $M = 100$). Three conditions on that sentence: 45 is reachable only if the enchantment can be bought three times (U-0338 readings A or C; under reading B one purchase gives at most 25, which absorbs no reachable $\ell$ fully since $\ell \ge 27$); 45 is a peak, since enchanted armor loses one durability every twenty minutes down to 15 (M-0339; clock details U-0339); and under U-0103 reading B (the 1 HP minimum applies to the final loss, M-0123 reading B) a fully absorbed failure still costs exactly 1 HP, so HP drops by 1 on each failure ($\mathbb{E}[\Delta h] = 41/10$ at $M = 100$, $h = 50$, $\alpha \ge 30$). Under U-0209 reading B (a per-hit cap of 15, never depleted) each failure loses $\max(L - 15, 0)$ HP, or at least 1 HP under U-0103 reading B, and no durability is spent.

(c) The two Kick readings give the same $L$ iff $10 \mid \ell$ (T-0002); among reachable $M$, iff $M \in \{100, 200\}$. Otherwise the Kick reduction of reading B removes one HP less than that of reading A, so the loss $L$ that remains is one HP larger under reading B:

| $M$ | 90 | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 | 190 | 200 | 210 | 220 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $L$, reading A | 24 | 27 | 29 | 32 | 35 | 37 | 40 | 43 | 45 | 48 | 51 | 54 | 56 | 59 |
| $L$, reading B | 25 | 27 | 30 | 33 | 36 | 38 | 41 | 44 | 46 | 49 | 52 | 54 | 57 | 60 |

(d) A Protection contestant, if "Potions heal you 50% less" covers Eddie's potion (U-0617 reading B or C; not under reading A), heals $g_P = \lfloor g/2 \rfloor$, $\lceil g/2 \rceil$ or exactly $g/2$ (M-0645 readings A, B, C; U-0618). For reachable $M$ the three agree, $g_P = M/4$, iff $20 \mid M$; for $M \in \{90, 110, \dots, 210\}$ they differ, and reading C leaves a non-integer HP after a success ($g_P = 55/2$ at $M = 110$). T-0401(a) and the positive-mean part of T-0401(b) hold with $g_P$ in place of $g$ and $h_E = \lceil g_P/9 \rceil - 1$ (the largest $h$ with $9h < g_P$; for integer $g_P$ this is $\lfloor (g_P - 1)/9 \rfloor$): $h_E = 2$ at $M = 100$; at $M = 110$, $h_E = 2$ under floor and $3$ under ceiling or exact.

*Proof.* (a) A blocker sets the hit to 0 at step 1 (M-0118), so the failure branch leaves $h$ unchanged. (b) Step 4 then step 7 with U-0101 reading A and U-0209 reading A, as in T-0007; under U-0103 reading A step 5 only raises a loss of 0 to 1 before armor, and $L \ge 24$ for reachable $M$, so it changes nothing; under U-0103 reading B the final loss is $\max(1, \cdot)$. (c) T-0002: $R_B(d) - R_A(d) = \mathbb{1}[10 \nmid d]$; the table is computed. (d) The argument of T-0401(b) for $h < \ell$ uses only $9h < g$ versus $9h \ge g$ and $g < M/2 + 1$, which hold with $g_P \le g$; the test checks every reachable $M$ under the three readings. $\square$

*Consequence.* Under this reading, drinking while shielded is a free 10% lottery on a heal of half your max HP, and an enchanted armor makes it nearly free. Whether the game agrees is exactly U-0004; one VOD of a shielded contestant drinking decides (a).

*Label:* every part `CONDITIONAL` on U-0004 reading B, U-0002 (Eddie's loss is a hit), M-0165 reading A, U-0203 reading A and Q4.1. (a) also: the Safety bubble only while inside it (M-0213), and U-0120 for which blocker is used up. (b) also U-0101 reading A, U-0209 reading A, U-0103 reading A or C for "HP never drops" (reading B stated), U-0338 reading A or C and U-0339 for durability 45. (c) U-0001. (d) U-0617 reading B or C, and U-0618 (each of its readings stated). Whether a fortress (pipeline step 6) also absorbs the backfire is part of U-0004: the damage table does not list it. *Test:* `test_t0402_potion_under_protection`.

## 4.2 When to drink: a one-step stopping problem

A contestant holding one Eddie's potion chooses when, if ever, to drink it. Drinking is irreversible. We model its effect as instant: the wiki states no delay and no cooldown, and that absence is an open question (Q4.2), not a rule. Write $S(x)$ for the probability of surviving (to a horizon, or to any goal) from HP $x$ if the potion is not drunk now and never later. The survival model is that of theory/05: HP is a Markov chain on $\{0, \dots, M\}$, 0 absorbing. T-0014 says that death is certain over an infinite horizon when, from every state $1, \dots, M$, one step loses at least $c \ge 1$ HP with probability at least $q > 0$; every environment used below has a loss with positive probability from every state, so it meets that hypothesis, and $S$ is always a finite-horizon quantity $S_T$. The horizon $T$ and the environment are free parameters (U-0009 for the event duration); nothing below invents them.

### T-0403: the decision boundary for one drink

**Theorem T-0403.** Let $S : \{0, \dots, M\} \to [0, 1]$ be nondecreasing with $S(0) = 0$. The value of drinking now and never again is $D(h) = \frac{1}{10}S(h^+) + \frac{9}{10}S(h^-)$. Drinking now is strictly better than never drinking iff $D(h) > S(h)$, which reads:

(a) under U-0004 reading A, for $h \le \ell$ (a failure kills): $S(h^+) > 10\,S(h)$. In particular, at an HP where a failure kills, never drink if $S(h) \ge 1/10$;
(b) under reading A, for $h > \ell$: $S(h^+) - S(h) > 9\,\bigl(S(h) - S(h - \ell)\bigr)$: the survival gained on a success must exceed nine times the survival lost on a failure;
(c) under reading C, the same as (b) with $h^- = \max(h - \ell, 1)$;
(d) whatever the reading, a necessary condition is $S(h) < \frac{1}{10} + \frac{9}{10}S(h^-)$.

*Proof.* (a) $S(h^-) = S(0) = 0$, so $D(h) > S(h)$ iff $S(h^+)/10 > S(h)$. If $S(h) \ge 1/10$ then $10S(h) \ge 1 \ge S(h^+)$. (b), (c) Subtract $S(h) = \frac{1}{10}S(h) + \frac{9}{10}S(h)$ from $D(h)$ and multiply by 10. (d) $S(h^+) \le 1$. $\square$

This is the precise form of the rule "drink only as a last resort". It needs no assumption about the environment beyond monotonicity of $S$. Monotonicity holds when every step applies a shift $\delta$ drawn with probabilities that do not depend on HP, clipped to $[0, M]$, with 0 absorbing. Proof by coupling: run two contestants at $x \le y$ with the same draws; if $x = 0$ it stays 0, otherwise $\mathrm{clip}(x + \delta) \le \mathrm{clip}(y + \delta)$ because clipping is nondecreasing, so the order $x \le y$ is kept at every step, and $y$ is alive whenever $x$ is; hence $S_T(x) \le S_T(y)$. We do not claim monotonicity for environments whose moves depend on HP.

*Label:* `DERIVED` (a statement about the model). Applying it in the game is `CONDITIONAL` on U-0004 (which of (a) or (c)) and needs $S$, which depends on the environment and on U-0009. *Test:* `test_t0403_one_drink_decision_boundary` (every $h$, both readings of U-0004, for $S_T$ computed exactly in 144 chains at $M = 100$: losses 1 to 20, loss probabilities $1/10$ to $1/2$, with or without healing, horizons 5 to 40).

### T-0404: holding is worth waiting, and the boundary is not a threshold

**Theorem T-0404.** Consider a pure-loss environment: each step HP changes by $\delta \in \{-c_1, \dots, -c_k, 0\}$ with fixed probabilities, clipped at 0 (0 absorbing), and let $c = \max_i c_i$. A contestant holds one potion and may drink at the start of any step, with $t$ steps left.

(a) If $h > c$ (the next step cannot kill), waiting one step is at least as good as drinking now, under U-0004 reading A or C. Hence some optimal policy drinks only at an HP where the next step can kill ($h \le c$).

(b) The set of HP values where drinking now beats never drinking need not be an interval $\{1, \dots, h^*\}$, under reading A or C of U-0004.
Example 1 (readings A and C): $M = 100$, one step loses 30 HP with probability $1/2$ (otherwise nothing), $t = 10$. Drinking now beats never drinking exactly for $h \in \{1, \dots, 30\} \cup \{41, \dots, 60\}$, while the optimal holder drinks with 10 steps left exactly for $h \in \{1, \dots, 30\}$: at 41 to 60 HP a drink beats never drinking, but waiting is better still, as (a) predicts since $h > c$.
Example 2 (reading A only): $M = 100$, one step loses 20 HP with probability $1/4$ (otherwise nothing), $t = 10$. Under reading A, drinking now beats never drinking exactly for $h \in \{11, \dots, 20\}$, and this is also the set where the optimal holder drinks with 10 steps left: at 5 HP the contestant waits, at 15 HP they drink. Under reading C the same environment gives $\{1, \dots, 20\}$, an interval, for both sets.

*Proof.* (a) Let $o(x)$ denote the random HP after drinking at $x$. Survival without the potion, $S_t$, is nondecreasing in HP (T-0403). For a shift $\delta \le 0$ with $h + \delta \ge 1$: on a success, $\min(M, h + \delta + g) \ge \min(M, h + g) + \delta$; on a failure, reading A gives $\max(h + \delta - \ell, 0) = \max(h - \ell + \delta, 0)$ if $h - \ell \ge 1$, and drinking first leaves the contestant dead otherwise, and reading C gives $\max(h + \delta - \ell, 1) \ge \max(h - \ell, 1) + \delta$. So "move, then drink" leaves HP at least as high as "drink, then move", outcome by outcome, and by monotonicity of $S_{t-1}$:
$$\text{wait} \;\ge\; \sum_\delta p_\delta \sum_o \Pr(o)\, S_{t-1}(o(h + \delta)) \;\ge\; \sum_o \Pr(o) \sum_\delta p_\delta\, S_{t-1}(\mathrm{clip}(o(h) + \delta)) = \text{drink now},$$
where $\mathrm{clip}$ keeps HP in $[0, M]$ and 0 is absorbing.
The first inequality holds because the holder who waits may still drink next step. (b) Example 2 first. Survival without drinking from $x \le 20$ is $(3/4)^{10} = 59049/1048576 \approx 0.0563$; from 51 to 60 HP it is $\Pr(\text{at most 2 hits in 10}) \approx 0.5256 < 10 \times 0.0563$; from 61 to 70 HP it is $\Pr(\text{at most 3 hits}) \approx 0.7759 > 0.5631$. A success from $h \le 10$ lands in 51..60, from $11 \le h \le 20$ in 61..70; by T-0403(a) only the second group drinks (reading A); under reading C a failure leaves 1 HP, worth $(3/4)^{10}$, and every $h \le 20$ drinks. Example 1: survival without drinking is $1/1024$, $11/1024$, $56/1024$, $176/1024$ from HP in $1..30$, $31..60$, $61..90$, $91..100$ (at most 0, 1, 2, 3 hits in 10). For $h \le 30$ a success lands in $51..80$, so $D \ge (11/10)/1024 > 1/1024$ whether a failure kills (reading A) or leaves 1 HP (reading C). For $h \ge 31$ a failure leaves $h - 30 \ge 1$ under both readings. For $31 \le h \le 40$: $D = (56/10 + 9/10)/1024 < 11/1024$. For $41 \le h \le 60$: $D = (176/10 + 9/10)/1024 > 11/1024$. For $61 \le h \le 90$, $D \le (176/10 + 9 \cdot 11/10)/1024 < 56/1024$, and for $h \ge 91$, $D \le (176/10 + 9 \cdot 56/10)/1024 < 176/1024$. The holder's set is computed exactly by backward induction. $\square$

*Consequence.* "Drink below some HP threshold" is not the rule. What matters is how many more hits a success buys: damage comes in chunks, and a heal that does not cross a chunk boundary is worth little. The pure-loss hypothesis in (a) matters for the proof: with healing in the environment, a heal after a drink can be capped differently. In 135 holder problems with healing (`test_t0404_heal_sweep_supports_hypothesis`: losses 1 to 35, heals 5 to 40, horizons 5 to 20, reading A) no optimal drink above $c$ was found, which supports (a) for those chains but proves nothing beyond them: `HYPOTHESIS` outside pure-loss environments.

*Label:* (a) `CONDITIONAL` on U-0004 reading A or C, U-0203 reading A (the proof uses the cap $\min(M, \cdot)$) and Q4.2 (instant drink). (b) `CONDITIONAL` on U-0203 reading A and U-0004 reading A or C (example 2: reading A only). In both parts the environment is a free parameter, not a rule of the game. *Test:* `test_t0404_waiting_dominates_and_no_threshold` ((a): 16 pure-loss environments, horizons 5, 10, 20, readings A and C, 96 holder problems solved exactly by backward induction; (b): both examples, each under both readings).

### T-0405: repeated drinks toward a target

Sometimes survival is a threshold: for example, a contestant who must cross a stretch outside the zone needs a known number of HP (T-0008), and less is certain death. Then $S(x) = \mathbb{1}[x \ge k]$ and the problem becomes: with $n$ potions and $h < k$, drink until HP is at least $k$, potions run out, or death. How large $n$ can be is set by the inventory: 3 slots by default (M-0200), more only by buying slots (M-0332) or if Eddie's potions stack (U-0200 reading B; under reading A, M-0201, each takes a slot). The theorem holds for any $n$; the test sweeps $n \le 6$ as a model parameter.

**Theorem T-0405.** Under U-0004 reading A and U-0203 reading A, let $J = \lfloor (h - 1)/\ell \rfloor$ be the number of failures a contestant at $h$ survives, and suppose one success is enough after any of them: $\min(M, h - j\ell + g) \ge k$ for $j = 0, \dots, \min(J, n-1)$. Then with $m = \min(n, J + 1)$:

(a) the probability of reaching $k$ is $1 - (9/10)^m$;
(b) the number of drinks $D$ used satisfies $\Pr(D = i) = (9/10)^{i-1}/10$ for $i < m$ and $\Pr(D = m) = (9/10)^{m-1}$, so $\mathbb{E}[D] = 10\,(1 - (9/10)^m)$;
(c) under reading C (no death; HP after $j$ failures is $\max(h - j\ell, 1)$, and the hypothesis is read with that value), $J$ is unbounded: $m = n$, and with unlimited potions $D$ is geometric with mean 10 and variance 90.

Example at $M = 100$, $h = 40$, $k = 60$: $J = 1$ (40 then 10 HP), and 10 + 50 = 60 reaches $k$, so with two or more potions the chance is $19/100$. Separately, for reachable $M$ a contestant at full HP has $J = 3$: the fourth failure in a row kills, so at most 4 drinks can be taken before death under reading A (used in T-0406). The closed form above does not apply at full HP, since it needs $h < k \le M$.

*Proof.* Each drink is an independent trial with success probability $1/10$. Under the hypothesis, the first success reaches $k$; before it, the $j$-th failure leaves $h - j\ell$, alive iff $j \le J$. The process stops at the first success, at death (failure number $J + 1$) or when the $n$ potions are gone, so at most $m$ trials happen and success has probability $1 - (9/10)^m$. The law of $D$ is that of a geometric variable truncated at $m$; $\mathbb{E}[D] = \sum_{i=0}^{m-1} (9/10)^i$. $J = 3$ at $h = M$ because $3 \cdot 3M/10 \le M - 1 < 4 \cdot 3M/10$ for $M \ge 10$, with $\ell = 3M/10$ for reachable $M$ (T-0400(b)). $\square$

*Label:* `CONDITIONAL` on U-0004 (reading A for (a), (b); C for (c)), U-0203 reading A, Q4.1 (independent rolls) and Q4.2 (back-to-back drinks, no cooldown). The value $J = 3$ at full HP also uses T-0400(b). *Test:* `test_t0405_repeated_drinks_toward_a_target` (dynamic programming over every reachable $M$, every third $h$, every fourth $k$, $n \le 6$, both readings, against the closed form), `test_t0405_examples`.

### T-0406: Dubins and Savage do not apply

Lester E. Dubins and Leonard J. Savage, *How to Gamble If You Must: Inequalities for Stochastic Processes* (McGraw-Hill, 1965), study a gambler who wants to reach a fixed goal. In their red-and-black game, a gambler with fortune $f$ may stake any amount $s$ up to $f$, wins $s$ with probability $w$ and loses $s$ with probability $1 - w$, and may play as often as they like; when $w < 1/2$ (subfair), bold play (stake everything, or just enough to reach the goal) maximizes the probability of reaching the goal. We cite the book, not a numbered theorem in it: we have not verified the exact statement, its theorem number or page, so the table below lists features of the red-and-black setting as just described. H1 to H4 are part of that setting. H5 and H6 are further differences between the setting and the potion; we do not claim that the bold-play result needs them (it may well hold with a limited number of plays), and the conclusion of T-0406 does not use them.

| Feature of red-and-black | Eddie's potion | Holds? |
|---|---|---|
| H1. The objective is to reach a fixed goal fortune; nothing else counts. | Survival is a probability $S(x)$ that depends on HP and on the environment, not an indicator of a goal. Only the threshold case of T-0405 has this form. | Only in the threshold case. |
| H2. The gambler chooses the stake, any amount up to their fortune. | No choice: a drink always risks $\ell = 3M/10$ (or all remaining HP) to win $g = M/2$ (capped). The only decisions are whether and when to drink. | Fails. |
| H3. Even-money bets: win $s$ or lose $s$. | Win $g$, lose $\ell$: odds $5{:}3$ for every reachable $M$. | Fails. |
| H4. Subfair: each bet has negative expected gain. | Negative for $h > h_E$, positive for $h \le h_E$ (T-0401(b)): the cap on the loss makes the bet superfair in HP at low HP. | Fails at low HP. |
| H5. Fortune changes only through bets, and time does not matter. | HP is drained between drinks by the environment (zone, poison, zombies, attacks), and the horizon matters (T-0404). | Fails unless the environment is frozen. |
| H6. Unlimited play. | At most as many drinks as potions carried (3 items by default, M-0200; slot upgrades, M-0332; whether Eddie's potions stack is U-0200), and no more than $J + 1$ under reading A (T-0405). | Fails. |

**Theorem T-0406.** (a) The potion decision is not an instance of subfair red-and-black: H2 and H3 fail for every reachable $M$, and H4 fails for every $h \le h_E$. So the bold-play result gives no conclusion here. (H5 fails in any environment that drains HP and H6 whenever the number of potions is finite; these are listed for completeness only.)
(b) What remains true without it: if never drinking means certain failure ($S(h) = 0$) and a success would give a positive chance ($S(h^+) > 0$), then never drinking is not optimal, since drinking now already gives $D(h) \ge S(h^+)/10 > 0 = S(h)$ (T-0403). It does not follow that drinking now is optimal: waiting may be better (T-0404(a)). Example under U-0004 reading A: $M = 100$, each step loses 10 or 20 HP with probability $1/2$ each, $t = 7$ steps left, $h = 70$. Then $S_7(70) = 0$ (seven steps lose at least 70) and $S_7(100) = 29/128$, so drinking now gives $29/1280$, but the optimal holder gets $99/1280$ by waiting: after one step HP is 60 or 50, a success still lands on 100 HP (the cap), and only 6 steps remain instead of 7.
In every case the answer comes from T-0403 and T-0404 with the actual $S$.

*Proof.* (a) H2: the outcome of a drink depends on $M$ and $h$ only (M-0208). H3: $g/\ell = (M/2)/(3M/10) = 5/3$ for every reachable $M$ (T-0400). H4: T-0401(b). H5 and H6: by definition of the environment and of the inventory. (b) The optimal value is at least the value of drinking now, $D(h) = \frac{1}{10}S(h^+) + \frac{9}{10}S(h^-) \ge S(h^+)/10 > 0$. The example is computed exactly by backward induction. $\square$

The only resemblance is qualitative: in both settings a player who is losing anyway prefers a large risky step to doing nothing. Saying more would be overclaiming.

*Label:* (a) `CONDITIONAL`: H2 and H3 rest on M-0208 (itself `CONDITIONAL` on U-0204) and, for "every reachable $M$", on T-0400(b); the H4 failure rests on T-0401(b), so on U-0004 reading A (reading C shifts the region to $h \le h_E + 1$, T-0401(c)) and U-0203 reading A. (b) `DERIVED` for the model given $S(0) = 0$; the example is `CONDITIONAL` on U-0004 reading A, U-0203 reading A and Q4.2, with the environment a free parameter. *Test:* `test_t0406_red_and_black_hypotheses_fail` checks the numerical facts of (a) (odds 5:3, the superfair region, the cap $J + 1$ on drinks; the other rows are definitions, not computations) and, for (b), that never drinking is not optimal wherever $S_t(h) = 0 < S_t(h^+)$ in the example environment for $t = 2$ to 8, and the counterexample to "drinking now is optimal".

*Review notice:* BROKEN by the second adversarial review (2026-11-12): the H4 row says the bet is negative above $h_E$, but T-0401(b) only gives $E \le 0$ there, and $E = 0$ at $M = 90, h = 5$ and $M = 180, h = 10$. The conclusion of (a) is unaffected. To fix next session.

## 4.3 Zombies: broken potions and destroyed crafts

"Zombies have a 10% chance to break one of your health potions, and a 40% chance to destroy crafted items" (M-0443, M-0444, `wiki-zombies-004`); "Unique crafts [...] have a 40% chance to be destroyed by Zombie hits" (M-0520, `wiki-sigils-ingenuity-012`; scope mismatch C-0404). What a "roll" is stays open: per drain tick, per encounter, per zombie, per craft (U-0426, U-0427, U-0518). A regular zombie drains 1 HP every 10 s up to 30 HP per contestant (M-0441, M-0442, T-0010); a guard zombie 2 HP every 5 s (M-0449).

### T-0407: laws of the zombie rolls

**Theorem T-0407.** Assume each roll is an independent trial.

(a) Potion break, one roll per drain tick (U-0426 reading A): the number of ticks until the first break is geometric with $p = 1/10$: mean 10 ticks (100 s next to one regular zombie), variance 90. Over the 30 ticks a single zombie can drain (U-0008 reading A), no potion breaks with probability $(9/10)^{30} \approx 0.0424$. A contestant holding $k$ health potions loses $\min(k, B)$ of them, $B \sim \mathrm{Binomial}(30, 1/10)$: expected $2.9638$ for a Piety stack of $k = 6$ (M-0506), $2.3626$ for $k = 3$. Under reading B (one roll per zombie and contestant) a zombie breaks a potion with probability $1/10$ in total.

(b) Craft destruction, every craft rolls on every hit (U-0518 reading A, U-0427 reading C): each craft lasts a geometric number of hits with $p = 2/5$: mean $5/2$ hits (25 s next to one regular zombie, 12.5 s next to a guard zombie), variance $15/4$. A craft survives 10 hits with probability $(3/5)^{10} \approx 0.0060$ and a full 30-hit encounter with probability $(3/5)^{30} \approx 2.2 \times 10^{-7}$.
One roll per hit destroying one random craft (U-0518 reading B, U-0427 reading A): with $c$ crafts, $\min(c, B')$ are destroyed, $B' \sim \mathrm{Binomial}(n, 2/5)$ after $n$ hits: for $c = 5$, an expected $3.7649$ after 10 hits and $4.9981$ after 30; at least one of the five survives 30 hits with probability $\Pr(B' < 5) \approx 0.0015$.
One roll per encounter (U-0518 reading C) has two forms, and the wiki does not say which. If the one roll destroys one random craft (U-0427 reading B), a given craft among $c$ held survives an encounter with probability $1 - (2/5)/c$ ($23/25$ for $c = 5$), and some craft is lost with probability $2/5$. If instead each craft rolls once per encounter (a per-craft form of U-0518 reading C, not one of the readings of U-0427), each survives with probability $3/5$.

Scope of every line above. Under U-0518 reading D (a hit blocked by a Shield, repellent or bubble does not roll) and U-0426 reading C (a potion roll only when HP is actually lost), the number of rolls $n$ is the number of hits that get through, not the number of ticks; the formulas hold with that $n$. Under U-0616 reading A a Necromancy contestant makes no rolls at all. Which items are "crafted items" (all crafts, or only Ingenuity unique crafts) is contradiction C-0404; the formulas count whichever items are in scope.

*Proof.* Independent trials with probability $p$: the waiting time to the first success is geometric, mean $1/p$, variance $(1-p)/p^2$; the number of successes in $n$ trials is binomial; a roll that would remove an item when none is left removes nothing, hence the minimum. One roll destroying one of $c$ crafts chosen uniformly hits a given craft with probability $p/c$. Ticks are 10 s apart for a regular zombie and 5 s for a guard zombie. The values are exact fractions computed in the test. $\square$

*Consequence.* Under any per-hit reading, crafts do not survive sustained zombie contact; under the per-encounter readings they usually do. Which one holds changes the value of every Ingenuity craft, and a single VOD of an Ingenuity contestant near a zombie decides it (U-0518).

*Label:* `CONDITIONAL` on U-0426 or U-0427 and U-0518 (reading as stated in each line), U-0518 reading D and U-0426 reading C for what counts as a roll, U-0616 (Necromancy), C-0404 (scope of "crafted items"), U-0008 reading A for the 30-tick encounter, U-0425 for the tick timing, Q4.1 (independent rolls) and Q4.3 (the 30-tick figures assume rolls stop once the zombie has drained its 30 HP cap from that contestant). The wiki does not say which craft a single roll destroys; the uniform choice behind $1 - (2/5)/c$ is a modelling choice (the counts $\min(c, B')$ do not depend on it). *Test:* `test_t0407_zombie_rolls`.

## 4.4 Chests and care packages

### T-0408: the Greed chest Shield and the Trolling diversion

"Each real chest you claim has a 25% chance to give you a Shield for 20min. No roll while you are vulnerable." (M-0513). "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." (M-0432, attacks page); the Trolling page says "Each crate or care package from viewers" and "next to" (M-0539; contradictions C-0403, C-0501).

**Theorem T-0408.** Assume independent rolls.

(a) Greed: the number of real-chest claims (while not vulnerable) until the first Shield is geometric with $p = 1/4$: mean 4, variance 12. At least one Shield in $n$ claims has probability $1 - (3/4)^n$: $7/16$ for 2 claims, $37/64$ for 3 (the first $n$ above one half), and at least $9/10$ from $n = 9$. Under U-0511 reading B (each Shield adds 20 min), a claim is worth 5 Shield minutes in expectation. Under readings A (refresh) and C (ignored) overlapping Shields waste time, and under reading D (independent Shields coexist) two Shields active at once protect no more than one, so in those three readings 5 minutes per claim is an upper bound on protected time. In every reading a Vulnerability Dart removes the Shield early (M-0215), which can only lower the figure further.

(b) Trolling, one 3% roll per package (U-0540 reading A): packages until the first diversion are geometric with $p = 3/100$: mean $100/3 \approx 33.3$, variance $9700/9 \approx 1077.8$; a better-than-even chance of at least one diversion needs 23 packages, and $9/10$ needs 76. If the 5 packages of an emergency airdrop (M-0418) each roll (U-0411 readings A or B), at least one is diverted with probability $1 - (97/100)^5 \approx 0.1413$. If instead each of $N$ Trolling contestants rolls separately (U-0540 reading C), a package is diverted with probability $1 - (97/100)^N$ ($591/10000$ for $N = 2$).

*Proof.* Geometric and binomial laws as in T-0407; the thresholds are the smallest $n$ with $1 - (1-p)^n \ge 1/2$ or $\ge 9/10$, found by exact computation. Under reading B of U-0511 the Shield time is $20$ min times a binomial count, mean $20/4 = 5$ min per claim; overlap can only reduce it. $\square$

*Label:* (a) the geometric and binomial results `CONDITIONAL` on Q4.1 (independent rolls) only; the Shield minutes also on U-0511 (each reading stated); the time to a Shield is not computable yet, since how often real chests appear is unknown (U-0015). (b) `CONDITIONAL` on Q4.1, U-0540 and U-0411, with C-0403 and C-0501 open. *Test:* `test_t0408_greed_shield_and_trolling_diversion`.

## 4.5 Random rules without a stated law

These rules say "random" but give no distribution. Each distribution is a free parameter; no theorem is stated.

| Rule | Mechanic | Free parameter | Unknown |
|---|---|---|---|
| Care package and airdrop contents | M-0325, M-0418, M-0431 | item distribution | U-0323, U-0412 |
| Piety chest or crate gives a random health potion | M-0503 | tier weights; under the uniform reading the expected nominal heal is $85/4 = 21.25$ HP with the Piety bonus (5, 11, 23, 46; T-0005), $75/4$ without (`test_section_4_5_piety_uniform_baseline`) | U-0504, U-0505 |
| Bounty: random target, random health potion reward | M-0423, M-0424 | target and tier distributions | U-0418 |
| Merchant return after 30 min to 1 h | M-0321 | delay law in $[30, 60]$ min | U-0320 |
| Missile lands at a random spot near the aim point | M-0403 | landing offset law | U-0400 |
| Unsafe circle: one random defense item or craft lost every 5 s | M-0537 | which item | U-0539, C-0503 |
| Fake gravestone copies a random living contestant | M-0534 | choice rule | U-0534 |
| Horde, healing circle, gunship, merchant positions | M-0408, M-0445, M-0419, M-0415, M-0321 | spatial laws | U-0403, U-0413 |

## Open questions

Recorded unknowns this chapter depends on: U-0004 (can the loss kill, does the pipeline apply), U-0204 (rounding, irrelevant for reachable max HP by T-0400), U-0203 (heal cap), U-0002 (which sources are hits), U-0001 (Kick reduction), U-0101 (armor overflow), U-0103 (where the 1 HP minimum applies), U-0209 (armor pool or per-hit cap), U-0338 and U-0339 (armor enchantment and decay), U-0120 (which blocker is used up), U-0617 and U-0618 (Protection and potions), U-0011, U-0107 and U-0108 (revival, behind the choice $S(0) = 0$), U-0330 (HP upgrade limit), U-0200 (stacking), U-0009 (event duration, the horizon of $S_T$), U-0426, U-0427, U-0518 (zombie rolls), U-0616 (Necromancy immunity), C-0404 (which crafts), U-0008 and U-0425 (zombie cap and tick timing), U-0511 and U-0015 (Greed Shield overlap, chest rules), U-0540 and U-0411 (Trolling diversion scope), and those of section 4.5.

Open questions found while writing this chapter, not yet recorded in `kb/unknowns/` (they need U-ids; until then the labels above cite them as Q4.1 to Q4.3):

- Q4.1. Are successive random rolls independent with exactly the stated probability, or does the game use a pseudo-random scheme (for example a guaranteed success after a run of failures)? Every geometric and binomial law in T-0401, T-0405, T-0407 and T-0408 assumes independence. A tally of Eddie's potion or Greed chest outcomes in VODs would test it.
- Q4.2. Is Eddie's potion instant, and can it be drunk back to back, or is there a delay, a cooldown or a limit? Section 4.2 and T-0404 to T-0406 assume an instant effect, T-0405 back-to-back drinks. The 3 active item effects cap (M-0203) does not obviously apply to an instant effect.
- Q4.3. Do zombie potion-break and craft rolls continue after a zombie has drained its 30 HP cap from that contestant (M-0442)? T-0407's 30-tick figures assume they stop.
