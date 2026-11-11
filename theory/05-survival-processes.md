# 05. Survival processes: clocks and the capped-HP chain

> **Adversarial review, 2026-11-11: T-0008, T-0009, T-0014 BROKEN, fixes pending.** T-0008: Hazmat with a delayed first tick gives a third value, 4h+3; the fortress clause ignores M-0529 (a fortress may block zone damage entirely). T-0009: (b) holds only if the first tick comes 90 s after (re)poisoning (U-0115 reading A); under a first tick at t=0 each re-poisoning ticks at once. The condition is the meaning of 'timer' in M-0171, not U-0116. T-0014: the proof stands, but the example value 2e16 was a floating-point saturation artifact of np.linalg.inv; the exact value, 2.75e104, is now computed with fractions and corrected below. test_markov.py does not test absorption tending to 1. Other theorems on this page were UPHELD.

Two kinds of results: deterministic clocks (how long a fixed damage source takes to kill or to reach its cap), and one structural theorem about HP capped at a maximum. Tests: `sim/tests/test_clocks.py`, `sim/tests/test_markov.py`.

## 5.1 Deterministic clocks

Each clock assumes the source acts alone, with no healing and nothing that blocks it.

### T-0008: time to die outside the zone

Outside the safe zone a contestant loses 1 HP every 2 s after a 5 s grace (M-0101). When is the first tick (U-0003)?

**Theorem T-0008.** From HP $h \ge 1$, death comes at $T_A(h) = 2h + 3$ s if the first tick lands at 5 s (reading A), or $T_B(h) = 2h + 5$ s if it lands at 7 s (reading B). From 100 HP: 203 s or 205 s; from 220 HP: 443 s or 445 s. With a Hazmat suit (each interval 2 s longer, M-0209; whether the first tick also moves is U-0205), the interval is 4 s and death comes at $4h + 1$ s or $4h + 5$ s.

*Proof.* Ticks land at $t_1, t_1 + 2, \dots$; the $h$-th tick is at $t_1 + 2(h-1)$. With $t_1 = 5$ that is $2h + 3$; with $t_1 = 7$, $2h + 5$. Same with interval 4. $\square$
*Consequences.* Being live on Kick changes nothing here: a 1 HP tick is unchanged under both readings of the Kick reduction (T-0002, T-0004). If zone ticks go through the pipeline (U-0002), a fortress and armor add $2(f + a)$ s by T-0007 (fresh armor: 30 s). A Shield does not help (M-0128).
*Label:* `CONDITIONAL` on U-0003 (and U-0205 for the Hazmat line). *Test:* `test_t0008_zone_time_to_death`.

### T-0009: the poison clock, and a dead mechanic

Poison deals 1 HP every 90 s (M-0170); "Getting poisoned again resets the timer, it doesn't stack" (M-0171); a Poison Dart poisons "for 20 HP over 30min" (M-0315).

**Theorem T-0009.** (a) The dart's numbers agree with the poison page: 20 ticks at 90 s intervals end exactly at 1800 s = 30 min. (b) If re-poisoning restarts the 90 s tick clock, a contestant who is re-poisoned at least once every 89 s never takes any poison damage.

*Proof.* (a) Ticks at $90, 180, \dots, 1800$ s: 20 ticks, the last at 1800 s. (b) The next tick is due 90 s after the last restart; a restart every 89 s or less comes first every time. $\square$
*Consequence.* Under reading "reset the tick clock", chaining Poison Darts or fake gravestones on the same target is worse than useless: each new poisoning delays the damage the previous one would have done. Under the other reading of U-0116 (the reset restores the total but keeps the tick schedule), chaining keeps the damage flowing. One observation of a re-poisoned contestant decides it.
*Label:* (a) `DERIVED`; (b) `CONDITIONAL` on U-0116 and U-0115. *Test:* `test_t0009_poison_clock`.

### T-0010: zombie and guard-zombie caps

**Theorem T-0010.** One zombie within 5 m drains 1 HP every 10 s up to 30 HP (M-0441, M-0442): it reaches its cap after 300 s of continuous contact. A guard zombie drains 2 HP every 5 s up to 30 HP (M-0449): it reaches its cap after 75 s. With $n$ zombies, total drain is at most $30n$ HP per contestant, if the cap is per zombie lifetime (U-0008).

*Proof.* 30 ticks of 1 HP at 10 s intervals end at 300 s; 15 ticks of 2 HP at 5 s intervals end at 75 s (first tick one interval after contact; U-0425). $\square$
*Label:* `CONDITIONAL` on U-0008 and U-0425. *Test:* `test_t0010_zombie_drain_clocks`.

### T-0011 and T-0012: slow clocks

**Theorem T-0011.** Healing regeneration (1 HP every 30 min, M-0652) gives at most 48 HP per day. *Label:* `CONDITIONAL` on U-0007 (whether damage resets the timer).

**Theorem T-0012.** Armor enchantment decays from 45 to 15 at 1 per 20 min (M-0339): 30 steps, 10 hours. *Label:* `CONDITIONAL` on U-0339.

*Test:* `test_t0011_t0012_slow_clocks` (arithmetic only).

### T-0013: walking away from a zombie

Zombies move at 1.4 m/s (M-0440) and drain within 5 m. A contestant moving straight away at $v > 1.4$ m/s from distance $r_0 \le 5$ m leaves drain range after $(5 - r_0)/(v - 1.4)$ s, in a straight-line pursuit model. At a brisk 2 m/s from contact, that is 8.3 s, before the first 10 s tick (under the reading that the first tick comes one interval after contact). Below 1.4 m/s a zombie always catches up, and it chases "at any distance": a stationary contestant is always reached.

*Label:* `CONDITIONAL` on U-0425 (tick timing); the pursuit model is a simplification (straight line, no obstacles), not a rule. *Test:* `test_t0013_zombie_escape` checks the arithmetic only.

## 5.2 HP capped at a maximum: death is certain, and the question is when

HP lives on $\{0, 1, \dots, M\}$; 0 is absorbing (elimination, ignoring revival); healing above $M$ is wasted. Model a fixed environment as a Markov chain on HP with transition matrix $P$.

**Theorem T-0014.** Suppose that from every state $h \in \{1, \dots, M\}$, one step loses at least $c \ge 1$ HP with probability at least $q > 0$. Then from every state the chain reaches 0 with probability 1, and the expected time to reach it is at most $m / q^m$ steps, where $m = \lceil M / c \rceil$.

*Proof.* From any state, $m$ consecutive losses of at least $c$ reach 0; this has probability at least $q^m$. Split time into blocks of $m$ steps: each block kills with probability at least $q^m$ whatever happened before, so survival after $k$ blocks is at most $(1 - q^m)^k \to 0$, and the expected number of blocks is at most $1/q^m$. $\square$

This is the discrete form of a classical fact from risk theory: a surplus process with a reflecting upper barrier (here, max HP) is ruined with probability 1 (the dividend-barrier models of ruin theory; reference not verified here). The proof above does not depend on that literature.

*Consequence: "will I eventually die" is the wrong question.* The bound can be astronomically large. `sim/tests/test_markov.py` computes the exact expected time to death $t = N\mathbf{1}$, $N = (I - Q)^{-1}$, for example chains: with $M = 100$, a 1 HP loss with probability 0.05 per step and a 5 HP heal with probability 0.5, the expected time from full HP is about $2.75 \times 10^{104}$ steps ($10^{104.44}$, computed exactly with rational arithmetic by Gaussian elimination; the $2 \times 10^{16}$ first printed here was a floating-point saturation artifact of a float matrix inverse). Death is certain and irrelevant. The quantities that matter for the Codex are the finite-horizon survival $\Pr(\tau > T)$ over the event's duration $T$ (unknown: U-0009) and the expected time to death $\mathbb{E}[\tau]$, both computed by the simulator for each scenario.

*Label:* `DERIVED` (a mathematical fact about the model). Its use for Safe Zone is `CONDITIONAL` on the environment having a loss probability bounded below, which holds whenever any damage source can reach the contestant. *Test:* `test_t0014_capped_hp_means_certain_death`.

## 5.3 Last survivor

Winning means outliving every other contestant. Lifetimes are dependent (shared zone, shared viewers, combat), so multiplying independent survival curves gives only a baseline. The simulator estimates win probabilities directly.
