# 07. Zombies and pursuit

A zombie walks at 1.4 m/s toward the nearest contestant and drains anyone within 5 m. A player who sees one coming wants three answers: can I outrun it, how many HP will it cost me if I try, and when is a group of zombies deadly. This chapter answers them exactly, as functions of the player's speed $v$ and starting distance $r_0$, under every reading of the timing rules the wiki leaves open. It then follows the same geometry into three places where it changes play: the guard zombie at a gravestone, the zombies a Necromancy contestant raises, and a landmine used against zombies.

It builds on T-0010 (drain clocks and caps) and T-0013 (the straight-line escape time $(5 - r_0)/(v - 1.4)$), which are not restated. The new result behind everything else is T-0701: the straight-line escape of T-0013 is not a simplification. In the open plane it is the best any contestant can do against a chasing zombie, and the chase is the best a zombie can do against it.

No figure for human walking or running speed is used anywhere: no primary gait-science source was checked, so $v$ stays a free parameter, and example values (1.5, 2, 3 m/s) are inputs, not claims about people. This is geometry about points in a plane, never tracking of real people (`SCOPE.md`). Tests: `sim/tests/test_07_zombies.py`, helper formulas `sim/safezone_sim/ch07.py`. Every test checks our model of the rules, not the game.

## 7.0 The rules and the model

Every zombie rule in the KB, and where this chapter uses it:

| Rule | Records | Used in |
|---|---|---|
| Chase the nearest valid contestant, at any distance, at 1.4 m/s | M-0440, U-0424 | T-0700, T-0701, T-0706, T-0707 |
| Drain 1 HP every 10 s within 5 m | M-0441, U-0425, U-0002 | T-0702, T-0703 |
| At most 30 HP per zombie per contestant | M-0442, U-0008 | T-0702, T-0703 |
| Guard zombie: 10 m from the gravestone, 2 HP every 5 s within 10 m, cap 30, 1 h | M-0449, M-0633, U-0429, U-0615 | T-0702, T-0703, T-0705 |
| Horde: 50 ownerless zombies at random points in the safe zones, 20 min | M-0408, M-0445, U-0403 | T-0701, T-0703 |
| Necromancy: summon where you stand (3 per 6 h), a zombie within 10 m on any death, 5 where you stand on a horde | M-0446, M-0447, M-0448, M-0631, M-0632, M-0634 | T-0706 |
| Necromancy: own zombies drain to the owner; owner fully immune | M-0635, M-0636, U-0613, U-0614, U-0616, C-0401 | T-0706 |
| A zombie disappears when its time runs out | M-0450, U-0403, U-0612 | T-0701, T-0703, T-0706 |
| Landmine triggered by a zombie within 10 m, kills zombies in range; C4 is not triggered | M-0307, M-0451, M-0452, M-0640, M-0644 | T-0707 |
| Blockers: Shield, Safety bubble, Reality Shield, own Sleeping Bag, Necromancy, repellent; body armor absorbs | M-0145, M-0213, M-0220, M-0435, M-0454, M-0455, C-0205, C-0402 | T-0702 (remark) |
| Zombie Killer craft: kills the next ten zombies within 10 m, stops drain until then | M-0453, M-0527, U-0430, U-0522 | Section 7.7 (remark) |
| Blasts and tear gas kill zombies; EMP blocks hordes but leaves zombies on the map; Mirror ignores zombies; Protection takes zombie damage | M-0410, M-0451, M-0222, M-0400, M-0402, M-0241, M-0641 | not needed for the geometry |
| 10% potion break, 40% craft destruction | M-0443, M-0444, M-0520, U-0426, U-0427, U-0518, C-0404 | chapter 04 (planned) |
| Blood tokens from zombies | M-0521, M-0630, U-0519, U-0613 | T-0706 (consequence); chapter 06 |

**The pursuit model.** Positions are points of the plane, distance is Euclidean, there are no obstacles. A zombie moves at speed at most $u$; a contestant at speed at most $v$. Motions are Lipschitz paths (bounded speed), so the distance $d(t)$ between a zombie and a contestant is Lipschitz and has a derivative at almost every time. *Pure pursuit* means: whenever $d > 0$, the zombie moves at exactly speed $u$ straight toward its target's current position. This is our reading of "chase ... at 1.4m/s" (M-0440); whether zombies follow paths around terrain is part of U-0424. At $d = 0$ the direction to the target is undefined and the law says nothing; every result below is a statement about every motion that obeys the law wherever $d > 0$. Such motions exist: for a fixed Lipschitz contestant path $E$, the right side $u(E(t) - Z)/|E(t) - Z|$ is continuous in $(t, Z)$ and locally Lipschitz in $Z$ wherever $Z \ne E(t)$, so by the Picard-Lindelof theorem the pursuit has a unique solution up to the first time $d = 0$, and after that a target no faster than $u$ is followed by $Z = E$ (T-0700(b)). Existence after a capture by a contestant who then outruns the zombie is not argued here and no theorem needs it. For regular zombies $u = 1.4$ m/s. For guard zombies $u = 0$ if they stand still (U-0429 reading A) or $u = 1.4$ if they chase (reading B).

**Drain timing, one formula for every reading.** Let contact start at $t = 0$ (the zombie appears within range, or the contestant enters it). Drain ticks land at $\varphi, \varphi + P, \varphi + 2P, \dots$ with period $P$ (10 s regular, 5 s guard). The readings of U-0425 become values of the first-tick offset $\varphi$:

| Reading | Meaning | $\varphi$ |
|---|---|---|
| B1 | per zombie-contestant timer from entry, first drain one period later (the reading used in T-0010) | $\varphi = P$ |
| B0 | per pair timer, first drain at the moment of contact (asked by U-0425, not among its listed readings: open question Q7-1) | $\varphi = 0$ |
| A | each zombie has its own clock; its phase relative to the contact is unknown | $\varphi \in [0, P)$, free |
| C | each zombie's clock starts at its spawn | $\varphi = P$ if contact starts at the spawn, otherwise a value of A |

**Boundary.** "Within 5m" may include exactly 5 m (closed range, $d \le \rho$) or not (open range, $d < \rho$). U-0300 asks this for weapons and traps only; for zombie drain it is open question Q7-2. The formal fields of two KB records already write the closed form (M-0441 domain $d \le 5$ m, M-0307 reading A $d \le 10$ m); that is a formalization choice in those records, not something their quotes settle. Both cases are carried; they differ only on boundary values.

**Open questions not yet in `kb/unknowns/`.** This chapter cannot add records, so it names them Q7-1 to Q7-5 (listed at the end) and cites them by these names until they get U-ids.

## 7.1 Pursuit geometry

### T-0700: how fast the distance changes

**Theorem T-0700.** Let $d(t) = |E(t) - Z(t)|$ for a contestant $E$ and a zombie $Z$, and, where $d > 0$, let $e = (E - Z)/d$ be the unit vector pointing from the zombie to the contestant.

(a) At almost every time with $d > 0$: $d' = e \cdot E' - e \cdot Z'$.

(b) Under pure pursuit, $d' = e \cdot E' - u \le |E'| - u$. If the contestant never moves faster than $u$, the distance never increases, and once it is 0 it stays 0.

(c) *Escape cone.* Under pure pursuit, at a given instant the distance is not decreasing if and only if $e \cdot E' \ge u$: the contestant moves at a speed $w \ge u$ in a direction within $\arccos(u/w)$ of "directly away from the zombie". For $u = 1.4$ the half-angle is 21.04 degrees at $w = 1.5$ m/s, 45.57 at 2 m/s, 62.18 at 3 m/s and 80.99 at 8.94 m/s (computed).

(d) *Straight flight.* If the contestant runs in a straight line at speed $v$, directly away from the zombie's position at time 0, then whatever path the zombie takes (any path with speed at most $u$, pursuit or not), $d(t) \ge d(0) + (v - u)t$.

(e) *Feedback flight.* If the contestant always runs at speed $v$ directly away from the zombie's current position, then whatever path the zombie takes, $d' \ge v - u$. For $v \ge u$ the distance never decreases.

(f) The broader statement "a contestant faster than the zombie never loses ground, whatever path the contestant takes" is false. Under pure pursuit, running across the zombie's line ($e \cdot E' = 0$) loses ground at rate $u$, and running toward it at rate $u + v$.

*Proof.* (a) $d^2 = (E - Z) \cdot (E - Z)$; differentiating, $2 d d' = 2 (E - Z) \cdot (E' - Z')$, then divide by $2d$. The distance is Lipschitz, $|d(t) - d(s)| \le (u + v)|t - s|$, so it is differentiable almost everywhere and equals the integral of its derivative. (b) Pure pursuit is $Z' = u e$, so $e \cdot Z' = u$, and $e \cdot E' \le |E'|$ (Cauchy-Schwarz). If $|E'| \le u$, then $d' \le 0$ wherever $d > 0$. Suppose $d(t_0) = 0$ and $d(t_1) > 0$ for some $t_1 > t_0$; let $s$ be the last time before $t_1$ with $d(s) = 0$. On $(s, t_1]$ the distance is positive, so $d' \le 0$ there and $d(t_1) \le d(s) = 0$: a contradiction. (c) Write $E' = w(\cos\theta)\,e + w(\sin\theta)\,e^\perp$; by (b), $d' = w\cos\theta - u$, which is at least 0 if and only if $\cos\theta \ge u/w$. (d) Let $e_0$ be the direction away from $Z(0)$, so $E(t) = Z(0) + (d(0) + vt)e_0$. By the triangle inequality, $d(t) \ge |E(t) - Z(0)| - |Z(t) - Z(0)| \ge (d(0) + vt) - ut$. If $d(0) = 0$, any fixed direction gives the same bound. (e) Put $E' = v e$ in (a): $d' = v - e \cdot Z' \ge v - u$. (f) Put $e \cdot E' = 0$ or $e \cdot E' = -v$ in (b). $\square$

*Label:* `DERIVED` (facts about points moving in the plane, with $u$ a parameter; no game rule enters). Parts (d) and (e) need no pursuit model at all. Reading these facts as facts about zombies uses M-0440 and U-0424; that step is made, and labeled, in T-0701 to T-0707. *Test:* `test_t0700_distance_rate` (simulated paths against the bounds, the escape cone by finite differences, the counterexample of (f)).

### T-0701: the escape time is the value of a game

**Theorem T-0701.** Take a zombie with drain radius $\rho$ and speed $u$, and a contestant with speed at most $v$ who starts at distance $r_0$.

(a) If $v > u$ and $r_0 \le \rho$, let $\tau^* = (\rho - r_0)/(v - u)$. A contestant who flees in a straight line, directly away from where the zombie stood at time 0, is at distance more than $\rho$ at every time after $\tau^*$, whatever the zombie does. Against a pure-pursuit zombie, every contestant path stays at distance at most $\rho$ during all of $[0, \tau^*]$, and below $\rho$ during $[0, \tau^*)$. So the contestant is in range on $[0, \tau^*]$ under the closed range and on $[0, \tau^*)$ under the open range (Q7-2; empty when $r_0 = \rho$), and under both conventions $\tau^*$ is the exact value of the contest "time spent in range": the contestant cannot do better than straight flight, and the zombie cannot do better than pure pursuit. T-0013's formula is this $\tau^*$ for $\rho = 5$, $u = 1.4$.

(b) If $v \le u$ and $r_0 \le \rho$, a pure-pursuit zombie keeps the contestant in range for as long as it exists and keeps the same target.

(c) If $v < u$ and $r_0 > \rho$, a pure-pursuit zombie is within $\rho$ of the contestant after at most $(r_0 - \rho)/(u - v)$ s, whatever path the contestant takes; a contestant standing still is reached after exactly $(r_0 - \rho)/u$ s. If $v = u$, straight flight keeps the distance at least $r_0$, so the zombie never reaches range.

(d) *Reach radius.* Let the zombie have $\Lambda$ seconds left to live at time 0 (M-0450), and say it reaches range within its lifetime if $d(t) \le \rho$ at some $t \le \Lambda$ (closed range, the zombie still existing at the instant $\Lambda$). Against a contestant whose speed is at most $v < u$, the zombie reaches range within its lifetime, whatever the contestant does, if and only if $r_0 \le \rho + (u - v)\Lambda$. Under the open range, or if the zombie is already gone at the instant $\Lambda$, the boundary case (distance exactly $\rho$ exactly at expiry) does not count, and the condition is $r_0 < \rho + (u - v)\Lambda$. A contestant standing still at distance $r_0$ when a horde zombie is released is reached from up to 1685 m if the 20 min count from the release ($\Lambda = 1200$ s, M-0408, U-0403); a zombie with less time left reaches less far. Over the sweep of U-0612 (60 s to 86400 s) the reach radius of a regular zombie against a stationary contestant runs from 89 m to 120965 m.

*Proof.* (a) Straight flight: by T-0700(d), $d(t) \ge r_0 + (v - u)t > \rho$ for $t > \tau^*$. Pure pursuit: let $g(t) = r_0 + (v - u)t$. Suppose $d(t_1) > g(t_1)$ for some $t_1$, and let $s$ be the last time before $t_1$ with $d(s) \le g(s)$; then $d(s) = g(s)$ by continuity. On $(s, t_1]$ we have $d > g \ge 0$, so by T-0700(b) $d' \le v - u = g'$ there, hence $d(t_1) - g(t_1) \le d(s) - g(s) = 0$, a contradiction. So $d \le g$, and $g(t) \le \rho$ for $t \le \tau^*$, with $g(t) < \rho$ for $t < \tau^*$. Under straight flight against pursuit both move on one line and $d = g$, so $d(\tau^*) = \rho$ exactly: the closed and open conventions differ at that one instant only. (b) T-0700(b). (c) The same comparison gives $d(t) \le r_0 - (u - v)t$, which reaches $\rho$ at $(r_0 - \rho)/(u - v)$. A stationary target makes the pursuit a straight walk, so equality holds at $v = 0$. For $v = u$, T-0700(d) gives $d(t) \ge r_0$. (d) If $r_0 \le \rho + (u - v)\Lambda$, (c) gives a time at most $\Lambda$ with $d \le \rho$; if $r_0 < \rho + (u - v)\Lambda$, the same comparison gives $d(t) \le r_0 - (u - v)t < \rho$ for $t$ between $(r_0 - \rho)/(u - v)$ and $\Lambda$, a nonempty interval below $\Lambda$, so the open conventions are met too. If $r_0 > \rho + (u - v)\Lambda$, straight flight at speed $v$ keeps $d(t) \ge r_0 - (u - v)t > \rho$ for all $t \le \Lambda$; if $r_0 = \rho + (u - v)\Lambda$, it keeps $d(t) \ge \rho$ for $t \le \Lambda$ with equality only at $t = \Lambda$. $\square$

*Consequence.* "At any distance" (M-0440) makes every contestant slower than 1.4 m/s a target that will be reached, unless the zombie expires first or picks someone nearer; (d) says how far "any distance" reaches in practice, once the lifetime is known (U-0403, U-0612).

*Label:* `CONDITIONAL` on M-0440 (speed 1.4 m/s), U-0424 (pure pursuit, open plane, same target throughout), U-0429 for guard zombies, Q7-2 for which boundary instants count as in range (the value $\tau^*$ is the same under both), and U-0403 and U-0612 for the time left in (d). A target switch can only end the contact earlier; the straight-flight half of (a) holds for any zombie motion. *Test:* `test_t0701_escape_value` (an exact pursuit on one line in fractions over a grid of $v$ and $r_0$, checking the closed range on $[0, \tau^*]$ and the open range on $[0, \tau^*)$; simulated pursuit against random contestant paths; simulated zombie paths against straight flight; slower contestants for (b) and (c), including $v = u$; the reach radius and its boundary case in exact fractions).

## 7.2 HP lost while escaping

### T-0702: the exact drain of an escape

Let contact start at $t = 0$ with the zombie at distance $r_0 \le \rho$, the contestant flee at speed $v > u$, and $L = \tau^* = (\rho - r_0)/(v - u)$ (T-0701). Each tick drains $\delta$ HP (1 regular, 2 guard), and a zombie drains at most 30 HP from one contestant (M-0442, M-0449), that is $c = 30/\delta$ ticks.

**Theorem T-0702.** When the contestant flees in a straight line and the zombie pursues (the pair of strategies of T-0701), the number of drain ticks that land is

$$
N(L, \varphi) = \begin{cases} \lfloor (L - \varphi)/P \rfloor + 1 & \text{if } \varphi \le L \\ 0 & \text{otherwise} \end{cases} \quad \text{(closed range)}, \qquad N = \begin{cases} \lceil (L - \varphi)/P \rceil & \text{if } \varphi < L \\ 0 & \text{otherwise} \end{cases} \quad \text{(open range)},
$$

and the drain is $D = \delta \cdot \min(N, c)$ HP, before blockers, armor and the Kick reduction.

(a) For every $\varphi \in [0, P]$ (closed range), $N \in \{\lfloor L/P \rfloor, \lfloor L/P \rfloor + 1\}$: reading B1 gives the lower value, B0 the upper one, and reading A either one.

(b) If the unknown phase of reading A is taken as uniform on $[0, P)$ (a modelling assumption, not a rule), then $\mathbb{E}[N] = L/P$ exactly and $\Pr(N = \lfloor L/P \rfloor + 1) = L/P - \lfloor L/P \rfloor$, for $L < cP$ (before the cap can bind).

(c) Regular zombie ($\rho = 5$, $P = 10$, $u = 1.4$), reading B1, closed range: the escape costs 0 HP if and only if $v > 1.4 + (5 - r_0)/10$ m/s, that is 1.9 m/s from contact ($r_0 = 0$), 1.65 m/s from 2.5 m, 1.5 m/s from 4 m. With the open range, "if and only if $v \ge$" the same value. Under B0 no speed avoids the first HP.

(d) Guard zombie ($\rho = 10$, $P = 5$, $\delta = 2$), reading B1, closed range: 0 HP if and only if $v > (10 - r_0)/5$ when the guard stands still (U-0429 A), 2 m/s from the guard's own position; and $v > 1.4 + (10 - r_0)/5$ when it chases (U-0429 B), 3.4 m/s from contact.

(e) *No path does better, no chase does worse.* Against a pure-pursuit zombie, no contestant path with speed at most $v$ takes fewer than $N$ ticks, under every reading. Against straight flight, no zombie motion forces more than $N$ ticks under readings A and B1. Under B0 a zombie that left and re-entered range would start a new timer with an immediate drain at each entry; pure pursuit never does that against straight flight (the distance only grows), so the value $N$ stands, but the guarantee against arbitrary zombie motion fails under B0.

*Proof.* A tick at $\varphi + jP$ ($j = 0, 1, \dots$) lands while the contestant is in range, that is at a time at most $L$ (closed range) or below $L$ (open range), because under straight flight against pursuit $d(t) = r_0 + (v - u)t$ (both move on one line). Counting the integers $j \ge 0$ with $\varphi + jP \le L$ gives $\lfloor (L - \varphi)/P \rfloor + 1$; with $<$ it gives $\lceil (L - \varphi)/P \rceil$. (a) For $\varphi \in [0, P]$, $(L - \varphi)/P$ lies in $[L/P - 1, L/P]$, so its floor is $\lfloor L/P \rfloor - 1$ or $\lfloor L/P \rfloor$; when $\varphi > L$ we have $L < P$ and $N = 0 = \lfloor L/P \rfloor$. (b) $\int_0^P N(\varphi)\,d\varphi = \sum_{j \ge 0} \left|\{\varphi \in [0, P) : \varphi \le L - jP\}\right| = \sum_{j \ge 0} \min(\max(L - jP, 0), P) = L$; divide by $P$. The probability follows because $N$ takes only the two values of (a). (c) and (d): under B1 and the closed range, $N = 0$ if and only if $L < P$; solve for $v$. (e) By T-0701, against pursuit the contestant is in range on all of $[0, L]$ whatever path is taken, and extra contact only adds ticks. Against straight flight the contact lies inside $[0, L]$; under A the ticks sit on a fixed grid; under B1 each separate contact of length $\ell_i$ gives $\lfloor \ell_i / P \rfloor$ ticks and $\sum_i \lfloor \ell_i/P \rfloor \le \lfloor L/P \rfloor$. $\square$

Worked values (computed by `sim/safezone_sim/ch07.py`, closed range, before the cap binds; $v$ values are inputs, not human speeds):

| zombie | $r_0$ (m) | $v$ (m/s) | $L$ (s) | B1 (HP) | B0 (HP) | A, mean with uniform phase |
|---|---|---|---|---|---|---|
| regular | 0 | 1.5 | 50 | 5 | 6 | 5 |
| regular | 0 | 1.6 | 25 | 2 | 3 | 2.5 |
| regular | 0 | 1.8 | 12.5 | 1 | 2 | 1.25 |
| regular | 0 | 1.9 | 10 | 1 (open: 0) | 2 | 1 |
| regular | 0 | 2 | 25/3 = 8.33 | 0 | 1 | 0.833 |
| regular | 0 | 3 | 25/8 = 3.125 | 0 | 1 | 0.3125 |
| regular | 2.5 | 1.6 | 12.5 | 1 | 2 | 1.25 |
| regular | 2.5 | 2 | 25/6 = 4.17 | 0 | 1 | 0.417 |
| guard, still | 0 | 1.5 | 20/3 = 6.67 | 2 | 4 | |
| guard, still | 0 | 3 | 10/3 = 3.33 | 0 | 2 | |
| guard, chasing | 0 | 1.5 | 100 | 30 (cap) | 30 (cap) | |
| guard, chasing | 0 | 2 | 50/3 = 16.67 | 6 | 8 | |
| guard, chasing | 0 | 3 | 6.25 | 2 | 4 | |

*Consequences.* (1) For a single regular zombie the stakes are small: under B1 a contestant at 1.9 m/s or faster from contact loses nothing, and under every reading the loss is $L/10$ HP on average, plus or minus one tick. The cap of 30 HP binds only if the escape takes 300 s, that is $v \le 1.4 + 5/300 \approx 1.4167$ m/s from contact. (2) Starting distance matters as much as speed: 2.5 m of head start halves $L$. (3) For guard zombies, whether they chase (U-0429) decides everything: at 1.5 m/s a still guard costs 2 HP (B1), a chasing one its full 30 HP cap.

*What $D$ becomes in HP.* $D$ is the drain before protections. A Shield, a Safety bubble, a Reality Shield, sleeping in one's own Sleeping Bag, the Necromancy sigil or a Zombie repellent make it 0 (M-0145, M-0213, M-0435, M-0454, M-0636; for the repellent see C-0205 and C-0402); body armor absorbs it (M-0145), by T-0007 if drains are hits (U-0002). For a contestant live on Kick, a 1 HP tick is unchanged under both readings of U-0001 (T-0002). A 2 HP guard tick becomes 1 HP under U-0001 reading A ($\lfloor 9 \cdot 2/10 \rfloor = 1$, T-0002) if drains go through the pipeline (U-0002 reading A), and stays 2 HP under reading B. Whether the 30 HP cap counts the nominal drain or the HP actually lost after armor and the Kick reduction is open question Q7-4.

*Label:* `CONDITIONAL` on U-0425 (the value of $\varphi$; B0 is open question Q7-1, not a reading listed in that record), U-0008 (the cap per zombie per contestant), U-0424 (pure pursuit), U-0429 for guard zombies, and Q7-2 (closed or open range; compare U-0300). Part (b) adds the assumption of a uniform phase, which is a `HYPOTHESIS` about the implementation. *Test:* `test_t0702_escape_drain_exact` (an independent tick-by-tick simulation in exact fractions over 80 speeds, 21 starting distances, 10 phases and both boundaries, for regular, still guard and chasing guard zombies; the exact phase average; the thresholds; the table).

## 7.3 Many zombies at once

### T-0703: how many zombies kill, and how fast

**Theorem T-0703.** Let $n$ regular zombies keep a contestant with $h$ HP in range from $t = 0$ on (for example a contestant standing still or slower than 1.4 m/s: T-0701(b)), all contacts starting at 0, no blockers and no body armor, and every zombie existing for the whole contact. Call the contestant killed when the drained total reaches $h$: this is the death-at-0-HP model of T-0014 (0 HP absorbing); no KB record quotes the HP at which a contestant dies, so it is a modelling convention. A 1 HP tick is not changed by the 1 HP minimum (M-0123), nor by the Kick reduction under either reading of U-0001 (T-0002), so neither enters.

(a) Under U-0008 reading A (the 30 HP cap holds per zombie per contestant over the zombie's whole life), these zombies drain at most $30n$ HP from this contestant in total, so they can kill from $h$ HP only if $n \ge \lceil h/30 \rceil$. One zombie cannot kill anyone with 31 HP or more. At the base maximum HP of each sigil (90 for Greed, M-0508; 100 for most, M-0602 to M-0606 and M-0515, M-0530; 110 for Piety, M-0500) it takes 3, 4 and 4 zombies; at 200 HP, the highest maximum HP the merchant sells to sigils other than Piety, it takes 7, and at 220 HP, the Piety ceiling, it takes 8 (M-0333: "Maximum HP goes up to 200, or 220 for Piety"). Guard zombies have the same cap of 30 (M-0449) and count the same way under U-0615 reading A; under U-0615 reading B all guard zombies together count once.

(b) If $h \le 30n$, let $k = \lceil h/n \rceil$. Death comes at $10k$ s under B1, at $10(k - 1)$ s under B0, and at a time in $[10(k-1), 10k]$ under reading A, whatever the phases. A horde of 50 in range kills from 100 HP in 10 to 20 s and from 220 HP in 40 to 50 s; four zombies kill from 100 HP in 240 to 250 s.

(c) A regular zombie needs 300 s of contact (B1) or 290 s (B0) to drain its full 30 HP, a guard zombie 75 s or 70 s. Count a zombie as existing up to and including the instant it expires (the convention of T-0701(d)). A contact that starts $\Lambda$ seconds before the zombie expires holds $N(\Lambda, \varphi)$ ticks (T-0702, closed range), so the lifetime cuts the drain whenever $\Lambda$ is below those times. A horde zombie (20 min, M-0408) gives its full cap only to a contact that starts at most 900 s (B1) or 910 s (B0) after its release, if the 20 min count from the release (U-0403); a contact starting 1000 s after the release drains 20 HP (B1) or 21 HP (B0). A guard zombie (1 h, M-0633) gives its full cap to a contact starting at most 3525 s (B1) or 3530 s (B0) after it appears. Summoned, death and horde-bonus zombies have an unknown lifetime (U-0612, swept from 60 s to 86400 s), and the same subtraction applies.

(d) Under U-0008 reading B (the cap holds per encounter), the bound of (a) holds within one continuous contact only, since each new contact with the same zombie brings a fresh cap. Under reading C (the cap holds per time window of unknown length $W$), at most $30n$ HP per window. Under both, only the drain rate and the lifetime remain as bounds: under timing readings A and B1 one zombie drains at most $\lfloor \Lambda/10 \rfloor + 1$ ticks from one contestant over $\Lambda$ seconds of life, so the lifetime is the only bound on the total. Under B0 a contestant who leaves and re-enters range restarts the timer with an immediate drain at each entry (T-0702(e)), and not even this rate bound is proven.

*Proof.* (a) Sum the caps. (b) By T-0702(a), in $[0, t]$ each zombie has drained $\lfloor t/10 \rfloor$ or $\lfloor t/10 \rfloor + 1$ times, whatever its phase. At $t = 10k$ each has at least $k$ ticks, so the total is at least $nk \ge h$. At any $t < 10(k - 1)$ each has at most $k - 1$ ticks and the total is at most $n(k - 1) < h$, because $k - 1 < h/n$. With every $\varphi = P$ (B1) the $k$-th tick of every zombie is at $10k$, and with every $\varphi = 0$ (B0) it is at $10(k - 1)$. No zombie needs more than $k$ ticks, and $k \le 30$ because $h \le 30n$ means $h/n \le 30$. (c) T-0010 for B1; under B0 the 30th tick of 1 HP is at 290 s and the 15th tick of 2 HP at 70 s. A contact of length $\Lambda$ holds $N(\Lambda, \varphi)$ ticks by T-0702; subtract the needed contact time from 1200 s and 3600 s. (d) Reading of the records for the caps. For the rate: under A the ticks of one zombie sit on one grid of period 10 s, so at most $\lfloor \Lambda/10 \rfloor + 1$ fall in $[0, \Lambda]$; under B1 separate contacts of lengths $\ell_i$ give $\sum_i \lfloor \ell_i/10 \rfloor \le \lfloor \Lambda/10 \rfloor$ ticks, as in T-0702(e). $\square$

*Consequence.* Under the lifetime reading of the cap, zombies alone can kill only in groups: a lone zombie is a 30 HP tax, not a death sentence, while a horde of 50 caps at 1500 HP per contestant. If all 50 are within 5 m of a contestant at once from $t = 0$ (with no blocker, no armor and the death model above), they kill from any $h \le 250$ HP within 50 s under B1, by (b) with $k \le 5$; every maximum HP the merchant allows is at most 220 (M-0333), and whether current HP can exceed maximum HP is U-0203. In play, zombies chase the nearest contestant (M-0440), so 50 at once on one contestant is the extreme case, not the typical one. The reading of U-0008 is decisive for slow contestants, since under reading B a single long-lived zombie that a contestant keeps re-meeting has no cap at all, only its lifetime. (This consequence is `CONDITIONAL` on the same records as the theorem.)

*Label:* `CONDITIONAL` on U-0008 (reading A for (a) to (c)), U-0425 (the three timing cases), U-0615 for guards, U-0403 and U-0612 for (c), M-0333 for the 200 and 220 HP ceilings, and the death-at-0-HP model (a modelling convention, as in T-0014). *Test:* `test_t0703_many_zombies` (tick-event simulation for every $h$ from 1 to 220 and every $n$ from 1 to 60, under B0 and B1, and random phases of A for every eleventh $h$, with the cap; for (c), contacts cut by the lifetime for every start second, against the latest starts that still reach the cap; for (d), the rate bound under A and B1 over random contact patterns).

## 7.4 The speed rule

The wiki: "Moving too fast counts as being outside: faster than 20mph (8.94m/s) on average over 1min" (M-0105) "or faster than 30mph (13.41m/s) over any 15s" (M-0106). How the average is taken is U-0112; what happens after a violation is U-0113.

### T-0704: what the 8.94 m/s speed rule implies for zombies

**Theorem T-0704.** (a) Every zero-drain escape of T-0702 can be run without breaking the speed rule. Every zero-drain threshold under B1 (at most 1.9 m/s for a regular zombie, 2 m/s for a still guard, 3.4 m/s for a chasing guard, all from contact) is below 8.94 m/s. The rule is not a hard limit: moving faster "counts as being outside" (M-0105), at a cost set by U-0113. At 8.94 m/s from contact, the time in range of a regular zombie is $5/7.54 = 250/377 \approx 0.663$ s and of a chasing guard $\approx 1.326$ s. Under B0 even the fastest legal escape pays the first tick.

(b) Under U-0112 reading A (the average is the path length over a sliding 60 s window, threshold 8.94 m/s), a contestant who never breaks the 1 min rule gains at most $60 \times 8.94 - 60 \times 1.4 = 452.4$ m on a pure-pursuit zombie in any 60 s window during which the zombie never reaches them ($d > 0$ throughout). With the exact threshold of reading B, $20$ mph $= 5588/625 = 8.9408$ m/s (international mile of 1609.344 m), the bound is $56556/125 = 452.448$ m. Straight flight at the threshold speed reaches the bound.

(c) The condition $d > 0$ in (b) cannot be dropped. A contestant who stands still in contact for 15 s (the zombie on them, distance 0) and then runs straight at $536.4/45 = 11.92$ m/s for 45 s respects both speed rules under reading A (60 s mean exactly 8.94, every 15 s mean at most 11.92 < 13.41) and gains $536.4 - 1.4 \times 45 = 473.4$ m in that window: the time spent at distance 0 costs the contestant nothing, because the zombie cannot close a gap that is already 0.

*Proof.* (a) Compare the numbers of T-0702(c) and (d) with 8.94; $L = 5/(8.94 - 1.4)$ and $10/(8.94 - 1.4)$. (b) Where $d > 0$, T-0700(b) gives $d' \le |E'| - u$; integrating over the window, $d(t + 60) - d(t) \le \int_t^{t+60} |E'| \, ds - 60u$, and the path length is at most $60 \times 8.94$ under reading A. Equality holds for straight flight at constant speed, where both move on one line. (c) During the first 15 s the distance stays 0 (T-0700(b), the contestant does not move); afterwards both move on one line and the distance grows at $11.92 - 1.4$ m/s for 45 s. $\square$

Under reading C of U-0112 (endpoint displacement instead of path length), a winding path can be longer than 536.4 m in one window, and T-0700(b) bounds the gain by path length, not displacement. No bound is proven here for that reading.

*Label:* (a) `CONDITIONAL` on U-0425 and U-0429 (through T-0702), with the 8.94 m/s value `DOCUMENTED` (M-0105); the cost of going faster is U-0113. (b) and (c) `CONDITIONAL` on U-0112 reading A (B for the exact value), and U-0424. *Test:* `test_t0704_speed_rule` (exact fractions; collinear equality case; random paths whose path length over the 60 s window is exactly $60 \times 8.94$ m, the 1 min rule only: the 15 s rule is not enforced there, and enforcing it would only remove paths, so the bound is unaffected; the counterexample of (c) in exact fractions).

## 7.5 Guard zombies and the gravestone

When a contestant dies within 50 m of a Necromancy contestant, "a guard zombie appears 10m (33ft) from the gravestone" and drains "everyone within 10m" (M-0449, M-0633). The two 10s interact. Read the spawn distance as exactly 10 m (whether it is exact is open question Q7-3) and the guard as standing still (U-0429 reading A).

### T-0705: the gravestone sits on the edge of the guard's range

**Theorem T-0705.** Put the gravestone at the origin and the guard at $G$ with $|G| = 10$. A point at distance $s \ge 0$ from the gravestone, in a direction at angle $\beta$ from the direction of the guard, is within 10 m of the guard if and only if $s \le 20 \cos\beta$. The guard's drain disk is the disk of diameter 20 m that has the gravestone on its edge. Hence:

(a) The gravestone itself is exactly 10 m from the guard: drained under the closed range, not under the open range.

(b) No point on the far side of the gravestone (the closed half-plane facing away from the guard, $\cos\beta \le 0$), other than the gravestone itself, is in range. A looter who approaches from the side opposite the guard and stays strictly on that side is never drained; reaching the gravestone itself brings them back to the boundary case of (a).

(c) If the guard's direction is uniformly distributed (an assumption: the wiki gives no direction), a contestant standing at a fixed distance $s \in (0, 20]$ from the gravestone when the guard appears is in its range with probability $\arccos(s/20)/\pi$: 0.4841 at 1 m, 0.4681 at 2 m, 0.4196 at 5 m, $1/3$ at 10 m, and 0 beyond 20 m. As $s \to 0$ it tends to $1/2$.

*Proof.* $|P - G|^2 = s^2 - 20 s \cos\beta + 100$, which is at most 100 if and only if $s^2 \le 20 s\cos\beta$, that is $s = 0$ or $s \le 20\cos\beta$. (a) $s = 0$ gives equality. (b) If $s > 0$ and $\cos\beta \le 0$, then $s^2 > 0 \ge 20 s\cos\beta$. (c) With $\beta$ uniform on $[0, 2\pi)$ the condition $\cos\beta \ge s/20$ holds on an arc of length $2\arccos(s/20)$. $\square$

*Consequence.* Whether a looter at the grave is drained turns on a boundary convention, and the side of approach matters more than the distance. With a still guard, leaving the range from the guard's own position costs 0 HP under B1 above 2 m/s (T-0702(d)); from the gravestone ($r_0 = 10$ only if the guard appears at exactly 10 m, Q7-3; then $L = 0$) it costs 0 HP under B1, 0 HP under A unless the phase is exactly 0, and one tick of 2 HP under B0 with the closed range. If guards chase (U-0429 reading B), this theorem describes only the moment the guard appears.

*Label:* `CONDITIONAL` on U-0429 reading A, Q7-3 (the exact 10 m spawn distance) and Q7-2 (the closed or open range). Part (c) adds the uniform direction, a `HYPOTHESIS`. *Test:* `test_t0705_guard_disk` (every point of a half-metre lattice over a 50 m square, compared with the direct distance; the probability against rotated guards).

## 7.6 Zombies raised by Necromancy

A Necromancy contestant raises zombies "where you stand" (Summon, M-0446, M-0631; horde bonus, M-0448, M-0634) and "within 10m" on any death (M-0447, M-0632), is "Fully immune from zombies" (M-0636; the zombies page omits it, C-0401), and receives the HP its zombies drain (M-0635). Which contestants are "valid" targets is U-0424: reading A excludes contestants currently immune, reading B counts every living contestant and applies immunity only when draining.

The model needs one more convention, *K*: a zombie keeps its current target unless another contestant becomes strictly nearer (ties keep the target). U-0424 asks how often the nearest is re-evaluated, not how ties are broken, so K is our modelling choice, a `HYPOTHESIS` about the implementation. In T-0706(a) it matters only at instants when another contestant stands exactly where the target stands.

### T-0706: under one reading, a Necromancer's zombies follow their owner

**Theorem T-0706.** (a) Under U-0424 reading B and convention K, a zombie at distance 0 from its target keeps that target, and stays at distance 0, for as long as the target moves at 1.4 m/s or slower and the zombie exists.

(b) So, under reading B and K, a zombie summoned or raised by a horde bonus starts on its owner and stays on an owner who moves at 1.4 m/s or slower until the zombie disappears (M-0450). Its lifetime is unknown (U-0612, swept from 60 s to 86400 s), so an escort may last as little as a minute. While it lasts, the owner, immune, carries the zombie with them: every other contestant within 5 m of the owner is within 5 m of the zombie and is drained. With $k$ such escorts, a visitor loses $k$ HP per 10 s, up to 30 HP per escort (U-0008), and the owner receives it (M-0635, U-0613) and earns one blood token per HP drained (M-0630, measured as in U-0613 reading D). A death zombie that appears $r \le 10$ m from its owner and keeps the owner as its target until it reaches them (for example when no other contestant becomes strictly nearer to the zombie before then) reaches the owner within $r/(1.4 - v)$ s if the owner moves at speed at most $v < 1.4$ (at most 7.14 s for a still owner at $r = 10$), and then becomes an escort. Being the nearest contestant at the moment of appearance is not enough: with a still owner, a death zombie 10 m away and another contestant 11 m from the zombie on the far side, running straight at it at 3 m/s, the two gaps shrink at 1.4 and 1.6 m/s, are both 3 m after 5 s, and from then on the other contestant is strictly nearer, before the zombie reaches the owner at 7.14 s (computed).

(c) Under reading A, the immune owner is never a target (this is the reading itself). The owner's zombies chase the nearest non-immune contestant at any distance; where they go depends on the other contestants, never on the owner, so no escort in the sense of (b) exists.

(d) An owner who walks straight on at $v > 1.4$ m/s leaves an escort behind at a rate of at least $v - 1.4$ (T-0700(d)), and the zombie may then switch to a nearer contestant.

The theorem is about continuous motion. An implementation that moves zombies and picks targets in discrete steps of $\Delta t$ seconds lets the owner get up to $1.4\,\Delta t$ m ahead of an escort between steps, so a bystander who comes closer than that to the zombie could take it over (`HYPOTHESIS` about the implementation; the step length is unknown).

The same argument applies to any contestant immune to zombies under reading B and K (Shield, Safety bubble, own Sleeping Bag, M-0454; repellent under M-0455 reading A): a zombie that reaches a slow immune contestant stays on them while it exists, and drains anyone within 5 m of them who is not immune too. Inside a Safety bubble everyone is immune (M-0213), so only contestants outside the bubble and within 5 m are drained.

*Proof.* (a) While the target is unchanged and moves at speed at most $u = 1.4$, T-0700(b) says the distance never increases and stays 0 once it is 0. A switch would need another contestant strictly nearer than distance 0, which is impossible. (b) Summon and horde-bonus zombies appear "where you stand", at distance 0, where the owner is a nearest contestant; apply (a). Drain range is the disk of radius 5 m around the zombie's position, which is the owner's position. For a death zombie that keeps the owner as its target, T-0701(c) with $\rho = 0$ gives the time $r/(1.4 - v)$; computed: $10/1.4 = 7.14$ s. In the example, the gaps are $10 - 1.4t$ and $11 - 1.6t$, equal at $t = 5$. (c) Under reading A an immune contestant is not valid, so not a target, and the pursuit law involves only the zombie and its target. (d) T-0700(d) bounds the gap from below. $\square$

*Consequence.* Reading B turns the Necromancy sigil into a 5 m drain aura that moves with its owner for as long as each zombie lives (U-0612) and pays the owner in HP and blood tokens (M-0635, M-0630, U-0613); reading A sends its zombies away to hunt. One observation of a summoned zombie (does it stay with its owner?) decides this, and through it a large part of the sigil's value. (This consequence is `CONDITIONAL` on the same records as the theorem, plus M-0521 for blood tokens in general.)

*Label:* `CONDITIONAL` on U-0424 reading B for (a), (b) and (d), reading A for (c), convention K (a `HYPOTHESIS`), M-0636 owner immunity (C-0401), U-0612 and U-0403 for how long an escort lasts, U-0008, U-0613 and U-0614. *Test:* `test_t0706_escort` (reading B: discretized pursuit with random owner paths at speeds up to 1.4 m/s and moving bystanders, the escort and its drain set; reading A: (c) follows from the reading, so only its consequence is checked, a zombie leaving a still owner for a bystander 30 m away, against reading B where the same zombie stays; a fast owner; death zombies with a moving bystander, checking the join time whenever the owner stays the target and that both outcomes occur, plus the takeover example).

## 7.7 Landmines against zombies

A Landmine is placed "where you stand", "triggers when another contestant or a zombie comes within 10m", deals 15 HP "to everyone in range, you included" and "kills every zombie in range" (M-0307, M-0451, M-0452). A Protection contestant is immune to landmines (M-0640) and can place one every 2 h (M-0644, U-0621).

### T-0707: a landmine shields a contestant who stands far enough behind it

Take a contestant standing still at $E$, their own landmine at $M$ with $x = |E - M|$, and one zombie that targets $E$ by pure pursuit from a start $Z_0$ outside the mine's 10 m disk and outside the 5 m drain disk; no other contestant comes within 10 m of the mine. Closed ranges throughout (the open reading only moves the boundary cases). Parts (b) to (d) assume $x > 10$: the contestant stands outside the mine's 10 m.

**Theorem T-0707.** (a) Against a contestant standing still, the pursuit path is the straight segment from $Z_0$ to $E$.

(b) *Entry lemma.* Let $x > 10$. If the segment comes within 10 m of $M$, the zombie is at least $\sqrt{x^2 - 100}$ m from $E$ when it sets the mine off, and this is sharp: a walk that just grazes the mine's disk triggers it at exactly that distance.

(c) If $x > 5\sqrt{5} \approx 11.18$ m and the segment comes within 10 m of $M$, the mine goes off and kills the zombie before it is ever within 5 m of $E$, and $E$, more than 10 m from the mine, takes no blast damage. The contestant loses 0 HP under every timing reading. The threshold $5\sqrt{5} = \sqrt{10^2 + 5^2}$ is sharp: for $10 < x < 5\sqrt{5}$ a grazing walk is within 5 m of $E$ before it triggers the mine, and at $x = 5\sqrt{5}$ a grazing walk triggers it at the very instant it is exactly 5 m from $E$ (in drain range for that one instant under the closed range of Q7-2, never under the open range).

(d) If $10 < x \le 5\sqrt{5}$ and the segment comes within 10 m of $M$, the zombie can be within 5 m of $E$ before the mine goes off for at most $(5 - \sqrt{x^2 - 100})/1.4$ s, which is under $25/7 \approx 3.57$ s (0 s at $x = 5\sqrt{5}$, 0.298 s at $x = 11$, 1.285 s at $x = 10.5$, computed): 0 HP under B1, at most one tick under A and B0. If the segment does not come within 10 m of $M$, the mine never goes off and this part says nothing: at $x = 11$, a zombie walking in from the side opposite the mine passes no closer than 11 m to it and reaches $E$.

(e) The segment does come within 10 m of $M$ whenever $|Z_0 - E| \ge x$ and the angle at $E$ between the directions to $Z_0$ and to $M$ is at most $\arcsin(10/x)$: a cone of half-angle 63.43 degrees at $x = 5\sqrt{5}$, 56.44 at $x = 12$, 41.81 at $x = 15$, 30 at $x = 20$ and 19.47 at $x = 30$ (computed).

(f) A Protection contestant can stand on its own mine ($x = 0$): the first zombie that walks in from outside 10 m sets it off at 10 m, before it is within 5 m, whatever path it takes, and the blast kills every zombie then within 10 m. The contestant loses 0 HP to those zombies under every timing reading and takes no blast damage (M-0640). A zombie that arrives after the blast is covered only if the mine has a use left (U-0304).

*Proof.* (a) With $E$ fixed, the direction $e$ from the zombie to $E$ does not change as the zombie moves along it, so the path is a straight segment, walked at constant speed with the distance to $E$ decreasing. (b) Let $P$ be the first point of the segment within 10 m of $M$; it lies on the circle $|P - M| = 10$, and since the zombie was outside just before, its direction of travel does not point away from the centre: with $a = E - P$ (the rest of the walk, along that direction) and $b = M - P$, we have $a \cdot b \ge 0$. Then $x^2 = |a - b|^2 = |a|^2 - 2a \cdot b + 100$, so $|P - E|^2 = |a|^2 = x^2 - 100 + 2a \cdot b \ge x^2 - 100$, with equality when $a \cdot b = 0$, a walk tangent to the circle. (c) By (b) the trigger happens at a distance $\sqrt{x^2 - 100} > 5$ from $E$ or more, and along the segment the distance to $E$ only decreases, so no earlier point is within 5 m of $E$. The blast covers points within 10 m of $M$, and $x > 10$. A tangent walk triggers at $\sqrt{x^2 - 100}$, which is below 5 when $x < 5\sqrt{5}$ and equal to 5 when $x = 5\sqrt{5}$. (d) The zombie is within 5 m of $E$ before the trigger only while its distance to $E$ falls from 5 to at least $\sqrt{x^2 - 100}$, at 1.4 m/s. A contact shorter than one period $P$ holds at most one tick, and none under B1. If the segment stays more than 10 m from $M$, nothing in the model sets the mine off, and the zombie walks on to $E$. (e) The point of the ray from $E$ toward $Z_0$ nearest to $M$ lies at distance $x\cos\alpha$ from $E$ and $x\sin\alpha \le 10$ from $M$, where $\alpha$ is the angle; it is on the segment because $x\cos\alpha \le x \le |Z_0 - E|$. (f) A path from more than 10 m to within 5 m of $M = E$ passes through distance exactly 10 m first (intermediate value theorem), whatever the path; the first such zombie triggers the mine there, and Protection is immune to the blast (M-0640). $\square$

*Consequence.* Placed between a contestant and an approaching zombie, a landmine is a free kill: stand still more than 11.18 m behind it, with the zombie inside the cone of (e), and the zombie dies on the way in. The naive bound from the triangle inequality ($x > 10 + 5 = 15$ m) is not sharp, because a walk toward the contestant enters the mine's disk on its far side. A Protection contestant gets the same for every direction by standing on its own mine. The same "10 m before 5 m" argument as (f) is why the Ingenuity Zombie Killer, which kills zombies that come within 10 m (M-0453, M-0527), stops a walking zombie before it can drain; zombies that appear inside 10 m (horde zombies at random points, M-0445; death zombies within 10 m of a Necromancer, M-0447) never "come within" and are covered by neither argument: whether such a zombie sets off a landmine is open question Q7-5, and whether the Zombie Killer counts it is U-0522. One mine kills only the zombies inside its blast at that moment; under U-0304 reading A (single use) it is then used up.

*Label:* (b) and (e) `DERIVED` (plane geometry). (a), (c), (d) and the use of (b) and (e) for zombies `CONDITIONAL` on U-0424 (pure pursuit, the zombie keeping $E$ as its target), U-0300 for the mine's 10 m (closed; under the open reading a grazing walk never sets the mine off), Q7-2 for the 5 m drain boundary and, for (d), U-0425. (f) `CONDITIONAL` on U-0300, M-0640 (Protection immune to landmines), U-0621 and, for zombies arriving after the first blast, U-0304; it needs no pursuit model. *Test:* `test_t0707_landmine` (entry points of straight walks from a lattice of starts and from grazing starts, solved as a quadratic, for nine mine distances including $x = 5\sqrt{5}$ and three directions; walks that miss the mine disk checked against their closest approach, with the $x = 11$ example as a control; the cone condition in exact rational arithmetic; random zombie paths for (f)).

## Open questions

Recorded unknowns and contradictions this chapter depends on:

- U-0425: drain timing (the offset $\varphi$; decides B0, B1 or A in T-0702, T-0703, T-0707(d)).
- U-0008: the 30 HP cap per lifetime, per encounter or per window (T-0702, T-0703).
- U-0424: what "chase" and "valid" mean, re-evaluation of the nearest target, terrain (every theorem of 7.1, T-0706, T-0707).
- U-0429: guard zombies still or chasing (T-0702(d), T-0705); U-0615: guard cap per guard or shared (T-0703).
- U-0403, U-0612: zombie lifetimes, and whether a horde's 20 min count from its release (T-0701(d), T-0703(c), how long an escort lasts in T-0706).
- U-0112: how the speed average is taken (T-0704(b)); U-0113: what a speed violation costs.
- U-0002, U-0001: whether drains are hits and the Kick reduction (remark after T-0702).
- U-0300: inclusive or exclusive ranges for traps (T-0707); U-0304: landmine uses; U-0621: Protection's landmine.
- U-0613, U-0614, U-0616, C-0401: what a Necromancy owner receives and how far the immunity goes (T-0706).
- U-0430, U-0522: Zombie Killer counting (Section 7.7 remark).
- C-0205, C-0402, U-0431: whether a repellent removes a contestant from targeting (T-0706, last paragraph).
- Deferred to other chapters: U-0426, U-0427, U-0518, C-0404 (potion break, craft destruction: chapter 04), U-0519, U-0611 (zombie income and summon counting: chapter 06).

Open questions not yet recorded in `kb/unknowns/`, cited in this chapter by local names until they get U-ids:

- Q7-1. Does the first drain land at the moment of contact (reading B0)? U-0425 asks when the first drain occurs but lists no reading with a drain at contact (T-0702, T-0703, T-0707(d)).
- Q7-2. Is the zombie drain range closed ($d \le 5$, $d \le 10$) or open? U-0300 asks the same for weapons, traps, the merchant and the sleeping bag, not for zombie drain; M-0441 and M-0307 write the closed form in their formal fields without a quote that settles it (T-0701, T-0702, T-0705, T-0707).
- Q7-3. Does a guard zombie appear at exactly 10 m from the gravestone, and in which direction? With a 10 m drain range this decides whether the gravestone itself is drained (T-0705).
- Q7-4. Does the 30 HP cap count the nominal drain or the HP actually lost after body armor and the Kick reduction (remark after T-0702)?
- Q7-5. Does a zombie that appears inside a landmine's 10 m (a horde zombie, a death zombie) set it off, given that it never "comes within" (Section 7.7)? M-0307's note already flags that a trigger by a contestant immune to landmines is unstated.
