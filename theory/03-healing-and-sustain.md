# 03. Healing and sustain

A contestant who cannot outrun damage has to out-heal it. This chapter answers four questions a player asks before drinking, bandaging or standing by a fire: how many HP does this heal really give me, how much of it is wasted because HP cannot go above the maximum, how long until I am full again, and which steady damage can this source hold off, and for how long. It also settles one economic question with documented prices: should a Piety contestant drink a potion or sell it for blood tokens.

Tests: `sim/tests/test_03_healing.py` (exhaustive over the stated domains). Model: `sim/safezone_sim/ch03.py`. A passing test checks our model of the rules, never the game itself.

## 3.0 Conventions for this chapter

$M$ is max HP, $h$ current HP, $m = M - h$ the missing HP. A heal of nominal size $x$ restores

$$
\text{restored}(x, m) = \min(x, m), \qquad \text{waste}(x, m) = \max(x - m, 0)
$$

under U-0203 reading A (HP is capped at max HP after every heal). Under U-0203 reading B, HP can exceed $M$ and nothing is wasted; every "waste" statement below is `CONDITIONAL` on reading A.

**Reachable max HP.** Base max HP is 90 (Greed, M-0508), 100 (most sigils, M-0602 to M-0606, M-0530, M-0515) or 110 (Piety, M-0500); each merchant upgrade adds 10 (M-0333), up to 200, or 220 for Piety. If no other max-HP modifier exists, every reachable $M$ lies in $\{90, 100, \dots, 220\}$, all multiples of 10. This assumption is used in T-0300 and is `CONDITIONAL` on it (and on U-0330 for how many upgrades each sigil can buy).

**Single-shot heals in the KB**, with their nominal size $x$ (all `DOCUMENTED` unless a reading is named):

| Source | Nominal heal | Records |
|---|---|---|
| Health potion, small / medium / large / gigantic | 5 / 10 / 20 / 40 HP | M-0207 |
| Same, Piety contestant | 5 / 11 / 23 / 46 HP | M-0505, T-0005 |
| Same, Protection contestant | 2 or 3 or 2.5 / 5 / 10 / 20 HP | M-0645, U-0618, T-0300 |
| Everything potion (Ingenuity craft) | tier of the potion used | M-0526 |
| Bandage | 10 HP over 2 min (10, 11 or 12 HP for Protection, by the reading pair of T-0303) | M-0233, M-0646, U-0214, U-0619 |
| Campfire (Ingenuity craft) | pool of 5 / 10 / 20 / 40 HP at 1 HP per second, Piety and Protection changes do not apply | M-0525, U-0520 |
| Healing circle (viewer) | 25 HP, 1 min after it appears | M-0419, U-0413 |
| God's Fruit (admin) | 20 HP, 5 min after launch, within 100 m, "even at full HP" | M-0434 |
| Bounty claim (hunter) | 10 HP and a random health potion | M-0424 |
| Fake chest (the troll) | 5 HP | M-0533, U-0532 |
| Death: rob a gravestone | 5% of max HP | M-0611, U-0600 |
| Death: a contestant dies within 50 m | 1 HP per contestant eliminated so far, capped at 60% of max HP when 20% or fewer are alive | M-0613, M-0614, U-0601, U-0602, U-0603 |
| Healing: heal ability on another contestant | 1 HP, cooldown 10 min | M-0651, U-0623 |
| Healing: regeneration | 1 HP every 30 min, up to max HP | M-0652, U-0007, T-0011 |
| Necromancy: own zombie drain | the drained HP "goes to you", up to 30 HP per zombie per victim | M-0635, U-0613 (chapter 07) |
| Eddie's potion, 10% branch | 50% of max HP | M-0208 (chapter 04) |
| Revive | the target comes back with 5 HP, the reviver pays 5 HP | M-0656, U-0625 |

## 3.1 What rounding changes, and what it does not

### T-0300: where the rounding of a heal matters

Which heals Protection's "Potions heal you 50% less" (M-0645) cuts is U-0617: A, health potions only; B, health potions and Eddie's potion; C, every item heal (the record lists health potions, Eddie's potion, God's Fruit, bandages and the healing circle). The theorem covers all three.

**Theorem T-0300.** For every reachable max HP $M \in \{90, 100, \dots, 220\}$ (for Protection, $M \in \{100, \dots, 200\}$), the rounding readings of a heal give different HP in exactly these cases:

1. *Protection, small potion (every reading of U-0617).* Floor, ceiling and the exact half (U-0618 readings A, B, C) give 2, 3 or 2.5 HP. On the medium, large and gigantic tiers they agree (5, 10, 20 HP).
2. *Protection, Eddie's potion (U-0617 B or C).* The 10% branch heals $M/2$, and the cut halves it to $M/4$. The three readings differ if and only if $M \equiv 10 \pmod{20}$, by floor and ceiling 1 HP apart with the exact value half-way: at $M = 110$, 27, 28 or 27.5 HP.
3. *Protection, healing circle (U-0617 C).* Half of 25 HP is 12, 13 or 12.5 HP. Half of God's Fruit (20 HP) and of a bandage's 10 HP total is a whole number. Whether the cut is applied to a bandage's total or to each 1 HP or 2 HP tick (where the floor reading gives 0 or 1 HP per tick) is not decided by any record; T-0303 assumes the bandage is not cut (U-0617 A or B).
4. *Death's gravestone rob.* $\lfloor M/20 \rfloor$, $\lceil M/20 \rceil$ and the exact $M/20$ (U-0600 readings A, B, D) differ if and only if $M \equiv 10 \pmod{20}$: floor and ceiling by exactly 1 HP, the exact value half-way. Round half up (reading C) equals the ceiling. For a Death contestant ($M$ from 100 to 200) the floor reading gives 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10 HP.
5. *No other case.* Without the Protection cut, $M/2$ (Eddie's heal), $3M/10$ (Eddie's loss) and $6M/10$ (Death's 60% cap) are integers, so every rounding reading of U-0204 and of U-0603 gives one value. The Piety bonus has a single reading by T-0005 and is not restated here.

*Hypotheses.* Max HP only changes through the base values and +10 upgrades. The list of heals is the table of section 3.0.

*Proof.* Write $M = 10j$. (1) $x/2$ is an integer exactly when $x$ is even; among 5, 10, 20, 40 only 5 is odd. (2) $M/4 = 5j/2$ is an integer iff $j$ is even, i.e. $20 \mid M$; otherwise it is a half-integer. (3) 25 is odd; 20 and 10 are even. (4) $5M/100 = j/2$, the same parity argument; round half up of a half-integer goes up. (5) $M/2 = 5j$, $3M/10 = 3j$, $6M/10 = 6j$. $\square$

*Consequence.* Off the grid the readings split (for example $3 \cdot 95/10 = 28.5$), so any future max-HP modifier that is not a multiple of 10 reopens U-0204 and U-0603.

*Label:* `CONDITIONAL` on the reachable-$M$ assumption (M-0333, U-0330); items 2 and 3 name the reading of U-0617 they need. *Test:* `test_t0300_where_heal_rounding_matters` (every reachable $M$, every heal of the list, every reading of U-0617, U-0618 and U-0600; the set of cases that split is asserted exactly).

*Review notice:* BROKEN by the second adversarial review (2026-11-12): section 3.0 gives a Protection bandage total of 10, 11 or 12 HP under the reading pairs of T-0303, but item 3 and its test take the total as 10. To fix next session.

### T-0301: a bonus commutes with the cap, a cut does not

Piety's rule "Health potions heal you 15% more, rounded down" (M-0505) does not say whether the bonus is applied to the potion's tier or to the HP the potion would actually restore (U-0503 readings A and C). Protection's "Potions heal you 50% less" (M-0645) has the same gap.

**Theorem T-0301.** Let $g$ be a non-decreasing map on integers with $g(y) \ge y$ for every $y \ge 0$. For all integers $x, m \ge 0$:

$$
\min\big(m,\ g(\min(x, m))\big) = \min\big(m,\ g(x)\big).
$$

For the Protection cut $p(y) = \lfloor y/2 \rfloor$ (or $\lceil y/2 \rceil$), the two orders differ exactly when $x > m$, $p(x) > p(m)$ and $m > p(m)$; when they differ, cutting the restored amount gives less.

*Proof.* If $x \le m$ both sides are equal term by term. If $x > m$, the left side is $\min(m, g(m)) = m$ because $g(m) \ge m$; the right side is $\min(m, g(x)) = m$ because $g(x) \ge g(m) \ge m$. For the cut, with $x > m$ the left side is $p(m)$ (as $p(m) \le m$) and the right side is $\min(m, p(x)) \ge p(m)$; they differ iff both $m$ and $p(x)$ exceed $p(m)$. $\square$

*Label:* `DERIVED` (a statement about integer maps, not about the game).

*Consequence* (`CONDITIONAL` on U-0203 reading A). With HP capped, the three readings of U-0503 give the same HP for a Piety contestant at every HP level: the order of "bonus" and "cap" never matters. They still differ for blood tokens if the token counter uses the nominal heal (U-0501). For Protection the order is a real ambiguity: a gigantic potion drunk at 10 missing HP restores 10 HP if the cut applies to the tier heal ($\min(10, 20)$) and only 5 HP if it applies to the restored amount ($\lfloor 10/2 \rfloor$). This ambiguity has no U-id yet (open question 1 at the end of the chapter).

*Test:* `test_t0301_bonus_commutes_with_the_cap_but_a_cut_does_not` ($m$ in 0..230, $x$ in 0..119, three boosts including Piety's, both cut readings).

## 3.2 HP per blood token and per slot

No merchant clause of the 2026-11-11 snapshot (`wiki-merchant-001` to `wiki-merchant-058` in `corpus/clauses/wiki-merchant.yaml`) mentions a potion, so the merchant sells no health potion as far as the wiki says (M-0324 is only a partial price list); a care package costs 10 blood tokens but holds "one random item" (M-0325, U-0323), so no price in blood tokens per HP of healing is documented. Two documented exchanges exist.

**Max HP upgrades.** With $k$ upgrades already bought ($k = 0$ for the first), the next +10 max HP costs $40 + 10k$ tokens (M-0333, T-0006), and $\lceil 11(40 + 10k)/10 \rceil = 44 + 11k$ for an Ingenuity contestant (M-0323, reading A; under its binary64 reading B the base prices 50, 90, 100 and 110 come out 1 token higher, U-0006; how the surcharge applies to the ladders is U-0322). Whether the upgrade also raises current HP by 10 is U-0331. Under reading B it is a heal of 10 HP that is never wasted (max HP rises by the same amount), at $1/(4 + k)$ HP per token, or $10/(44 + 11k)$ for Ingenuity. Under reading A it heals nothing and adds 10 HP of room. `CONDITIONAL` on U-0331 (and U-0322 for Ingenuity).

**Piety potion conversion.** A Piety contestant can convert a small, medium, large or gigantic potion into $c = 1, 2, 3, 4$ blood tokens; converted potions "do not count as healing" (M-0502). Drinking it instead heals 5, 11, 23 or 46 HP (T-0005) and earns "one blood token per 5 HP healed" (M-0501). What "HP healed" means is U-0501: A, effective HP after the bonus; B, nominal after the bonus (overheal counts); C, nominal before the bonus; D, effective HP with the bonus part removed, modeled as $\min(m, x)$. Whether the remainder carries between heals is U-0500 (A cumulative, B floored per event, C like B with each tick of a heal over time as its own event). A potion is one event, so for a potion C gives the same tokens as B.

### T-0302: drink or convert

**Theorem T-0302.** Let a Piety contestant with missing HP $m$ hold a potion of tier conversion value $c$. Drinking earns at least $c$ tokens, whatever remainder the token counter carries, if and only if the token basis is nominal (U-0501 B or C), or it is effective (A or D) and $m \ge 5c$, that is 5, 10, 15 or 20 missing HP for the small, medium, large or gigantic tier. At full deficit drinking earns 1, 2, 4, 9 tokens (bases A, B) or 1, 2, 4, 8 (C, D), against 1, 2, 3, 4 for converting.

*Proof.* A drink adds $q$ to the counter, with $q = \min(m, \lfloor 1.15x \rfloor)$ (A), $\lfloor 1.15x \rfloor$ (B), $x$ (C) or $\min(m, x)$ (D). With carried remainder $R \in \{0, \dots, 4\}$ the drink earns $\lfloor (R + q)/5 \rfloor - \lfloor R/5 \rfloor = \lfloor (R+q)/5 \rfloor \ge \lfloor q/5 \rfloor$, with equality at $R = 0$ (which is also the per-event reading U-0500 B). So drinking earns at least $c$ for every carry iff $\lfloor q/5 \rfloor \ge c$, iff $q \ge 5c$. Nominal bases: $\lfloor 1.15x \rfloor \ge x$ and $x = 5, 10, 20, 40 \ge 5c = 5, 10, 15, 20$. Effective bases: $\min(m, \cdot) \ge 5c$ iff $m \ge 5c$, since both caps ($x$ and $\lfloor 1.15x \rfloor$) are at least $5c$. $\square$

*Consequence.* Under every reading, once the contestant is missing at least $5c$ HP a drink gives at least as many tokens as a sale and the HP on top; for the large and gigantic tiers at a large deficit it gives strictly more tokens (4 against 3, 8 or 9 against 4). Selling only pays in tokens when the contestant is nearly full and the counter uses effective HP. The theorem compares one potion at one moment: a potion kept is also insurance and can be broken by a zombie (M-0443), which the comparison leaves out.

**HP per slot.** All Piety health potions share one slot, up to 6 (M-0506): at most $6 \times 46 = 276$ HP in one slot, more than any reachable Piety max HP (220), or $6 \times 4 = 24$ tokens if converted. For other sigils one potion per slot under U-0200 A (at most 40 HP; 20 for Protection); under U-0200 B the stack size is unknown.

*Label:* `CONDITIONAL` on U-0500 and U-0501 (the theorem covers all their readings), and on M-0501 counting potion heals (it names "any source except revives"). *Test:* `test_t0302_piety_drink_or_convert` (every Piety max HP, every missing HP, every tier, basis and carry).

## 3.3 Heals over time: time to full

### T-0303: the bandage clock

"Heals 10 HP over 2min. Taking damage does not stop it." (M-0233). The tick schedule is U-0214: A, 1 HP at 12, 24, ..., 120 s; B, 1 HP at 0, 12, ..., 108 s; C, 2 HP at 24, 48, ..., 120 s; D, continuous at 1/12 HP per second, a whole HP showing each time one more HP has accrued. Protection bandages "last 1.1x as long" (M-0646), read three ways by U-0619: A, the same 10 HP over 132 s (every tick time times 1.1); B, the same rate for 132 s; C, 132 s rounded to the tick grid of the bandage. For B we count the whole ticks that fit in 132 s; for C we take both directions of the rounding, since the record does not say which.

**Theorem T-0303.** With each tick capped at max HP and no damage, a bandage restores $m$ missing HP after the time in the table, and wastes its total minus $m$ (total 10 HP unless stated). Write $f_X(m)$ for the time under U-0214 reading $X$:

| Reading | Time to full (s) | Total (HP) |
|---|---|---|
| U-0214 A | $f_A(m) = 12m$ | 10 |
| U-0214 B | $f_B(m) = 12(m - 1)$ | 10 |
| U-0214 C | $f_C(m) = 24 \lceil m/2 \rceil$ | 10 |
| U-0214 D | $f_D(m) = 12m$ | 10 |
| Protection, U-0619 A, with U-0214 $X$ | $\tfrac{11}{10} f_X(m)$: $13.2m$, $13.2(m - 1)$, $26.4 \lceil m/2 \rceil$, $13.2m$ | 10 |
| Protection, U-0619 B, with U-0214 $X$ | $f_X(m)$ | 11 for A, B, D; 10 for C |
| Protection, U-0619 C, with U-0214 $X$ | $f_X(m)$ | 11 for A, B, D; 10 or 12 for C |

A deficit above the total is never filled by one bandage. Across the readings, the time to fill a given $m \le 10$ spreads by 12 s for even $m$ and 24 s for odd $m$ (U-0214 B against C); for a Protection contestant, across every pair of a U-0619 and a U-0214 reading, it spreads by $(6m + 60)/5$ s for even $m$ and $(6m + 126)/5$ s for odd $m$, at most 36 s (at $m = 9$: 96 s under U-0619 B or C with U-0214 B, 132 s under U-0619 A with U-0214 C).

*Proof.* The $k$-th HP arrives at the $k$-th tick time of each schedule; reading C delivers HP in pairs, so the $m$-th HP arrives with tick $\lceil m/2 \rceil$; reading D reaches $m$ HP at $m$ divided by the rate. U-0619 A multiplies every tick time by 1.1. Under U-0619 B and C the ticks keep their times, and only the number of ticks changes: $132/12 = 11$ ticks on a 12 s grid; on the 24 s grid of U-0214 C, $132/24 = 5.5$, so 5 whole ticks (B, and C rounded down) or 6 (C rounded up). Under U-0214 D there is no grid and C is B. With no damage, HP paid after HP is full is wasted, which leaves the total minus $m$. The spreads are the differences of the largest and smallest rows, computed for every $m$. $\square$

*Consequence.* The schedules differ on the time to full by up to 24 s (36 s for Protection), which only matters when the bandage races a damage tick. While a bandage lasts (2 min, Protection 132 s) it gives $1/12$ HP per second (Protection U-0619 A: $5/66$); by T-0305 that is enough to hold off poison ($1/90$) and bleeding ($1/300$) for that time, but not one zombie ($1/10$). Bleeding stops with the bandage (M-0234); poison does not, and resumes when the bandage ends. If Protection's 50% cut covers bandages (U-0617 reading C), every Protection row above changes again (T-0300, item 3).

*Label:* `CONDITIONAL` on U-0214, U-0619 (every reading in the table), U-0617 A or B, and U-0203 reading A. *Test:* `test_t0303_bandage_time_to_full` (every reading pair, every $m$ up to the total, time and waste; reading D is built as a separate 0.2 s grid, not from the A ticks; the two spreads are asserted for every $m$).

### T-0304: the Campfire pool

"Heals everyone within 10m (33ft) 1 HP per second from one shared pool equal to the potion's heal. It burns out when the pool is empty or after 10min." (M-0525). How the pool drains is U-0520: A, each person in range with missing HP draws 1 HP per second; B, the pool pays 1 HP per second in total, "split among those in range"; C, everyone in range draws 1 HP per second, full HP or not. Reading B leaves open whether a full-HP bystander takes a share, which is the U-0520 question itself, so we keep both: B1, the 1 HP goes only to people missing HP (modelled as 1 HP to one of them per second, in turn); B2, it is split equally among everyone in range, full or not, and a share above a person's deficit is lost (exact fractions of HP, as in U-0618 reading C). The pool $P$ is 5, 10, 20 or 40.

*Model.* The fire is lit at second 0 and heals at whole seconds 1, 2, ..., 600; "burns out ... after 10min" is read as a last heal at second 600 (inclusive), a modelling choice the wiki does not fix. Damage that falls on the same second as a heal lands first.

**Theorem T-0304.** (a) *Group at rest.* Let $n$ contestants with missing HP $m_1, \dots, m_n$ stay in range, with no damage. Under U-0520 A and B1 the fire restores exactly $\min(P, \sum m_i)$ HP within $P \le 40$ s, whatever the order in which a nearly empty pool serves people. Under B2 the pool is empty after exactly $P$ s and restores $\sum_i \min(m_i, P/n)$ HP, which can be less than $\min(P, \sum m_i)$. Under C the pool is empty after exactly $\lceil P/n \rceil$ s whatever the deficits and restores at most $\min(P, \sum m_i)$; a lone owner at full HP wastes all of it.

(b) *Standby against a steady drain.* A lone contestant at full HP stands by the fire and is hit for $a$ HP at seconds $s, s + b, s + 2b, \dots$ ($1 \le s$, $a \le b$), at most $N$ times ($N \ge 1$, or no limit). Let $K = \lceil P/a \rceil$. Under U-0520 A (and B1, which is the same for one person), HP never falls below $M - a$ while the pool lasts, and:

- if $N \ge K$ (or no limit), the pool pays its last HP at second $T_{\text{end}} = s + (K - 1)(b - a) + P - 1$;
- if $N < K$, the pool pays $Na$ HP in all, the last at second $T_{\text{end}} = s + (N - 1)b + a - 1$, and the fire burns out at 600 s with $P - Na$ HP left;

provided $T_{\text{end}} \le 600$; otherwise the fire burns out at 600 s with more HP left. Under B2 and C the pool is empty at $P$ s whatever happens.

*Proof.* (a) Under A and B1 each second moves at least one HP from the pool to a contestant who is missing HP, and only to such a contestant, so the transfer stops at $\min(P, \sum m_i)$, after at most $P$ seconds, long before the 600 s limit. Under B2 the pool loses 1 HP per second and each person receives $1/n$ of it per second until full, so person $i$ receives $\min(m_i, P/n)$ over the $P$ seconds; the sum is at most $\min(P, \sum m_i)$, with equality only when no share is lost. Under C the pool loses $n$ HP per second (the last second possibly fewer), so it lasts $\lceil P/n \rceil$ s; only draws by a contestant missing HP restore anything. (b) Since $a \le b$, each hit is refilled 1 HP per second, starting the second it lands, before the next one lands, so HP returns to $M$ between hits and the pool pays exactly the damage taken. If $N \ge K$, the $K$-th hit is the first after which the pool cannot refill fully; it lands at $s + (K - 1)b$ with $P - (K - 1)a$ HP left, paid one per second. If $N < K$, the last hit lands at $s + (N - 1)b$ and is refilled in $a$ seconds; then nothing draws. Under B2 and C a lone contestant draws 1 HP every second regardless. $\square$

*Examples (gigantic potion, $P = 40$, reading A).* Outside the zone (1 HP every 2 s, M-0101, fire lit when the contestant leaves): first tick at 5 s (M-0101 A) or 7 s (B), so the fire refills every tick and pays its last HP at 83 s or 85 s, against 40 s of burning under B2 or C. Next to one zombie (1 HP every 10 s, M-0441, phase $s$ from 1 to 10 s, at most 30 HP per zombie and contestant, `wiki-zombies-003` in M-0635): the zombie stops at 30 HP, the pool pays its last HP at $s + 290$ s and burns out at 600 s with 10 HP left. A guard zombie (2 HP every 5 s, $s$ from 1 to 5 s, at most 30 HP per contestant, M-0449): $s + 71$ s, 10 HP left. Without these caps the times would be $s + 390$ s and $s + 96$ s, pool empty; how the caps count is U-0008. Poison (1 HP every 90 s, M-0170) would need 3,600 s, so the fire burns out at 600 s with 34 HP unused if the first tick is at 90 s (M-0170 A) and 33 HP if it is at 0 s (M-0170 B, the tick at 0 s landing before the fire's first heal).

*Consequence.* Reading A makes the Campfire a 10-minute reserve that absorbs damage as it comes; readings B2 and C make it a burst that is partly or wholly wasted on anyone at full HP nearby. The Ingenuity owner earns one blood token per HP the fire heals (M-0521); under U-0519 A that is the HP restored, under U-0519 B the pool consumed, and the two differ only when HP is wasted (readings B2 and C). Whether the fire's healing pays Piety tokens is U-0502.

*Label:* `CONDITIONAL` on U-0520 (each part names its reading, B split into B1 and B2 as above), on the per-second model with the inclusive 600 s limit and the hit first in a shared second, on everyone staying in range, and for the examples on the M-0101 and M-0170 reading named and on U-0008. *Test:* `test_t0304_campfire_pool` (every tier; groups of 1 to 3 with deficits up to 45; every tie order; drains with $a \le 3$, $b$ up to 30, three phases per $b$, hit limits $1$, $K - 1$, $K$ and none; every example).

### Other heals: time to full

`CONDITIONAL` on U-0203 reading A throughout. A potion of size $x$ fills $m$ missing HP at once with $\lceil m/x \rceil$ potions. A healing circle fills up to 25 HP 60 s after it appears, if the contestant is inside at that moment (U-0413). God's Fruit fills up to 20 HP 300 s after launch, within 100 m; U-0203 does not cover the fruit, and whether its heal is capped is open question 2, so "up to 20 HP" is the capped reading, chosen here and not documented. A Healing contestant's ability gives 1 HP per 600 s per healer (M-0651), except from inside a smoke cloud, where a contestant "cannot heal ... other contestants" (M-0227; whether Thermal goggles lift that restriction is U-0213). Regeneration (U-0007 reading A, fixed clock with unknown phase $\varphi \in \{1, \dots, 1800\}$ s) fills $m$ HP at $\varphi + 1800(m - 1)$ s: about 50 hours for 100 HP.

## 3.4 Sustain: which steady damage a heal can hold off

### T-0305: the sustain dichotomy

Model a contestant who loses $a$ HP every $b$ s (at $b, 2b, \dots$) and heals $c$ HP every $e$ s (at $\varphi, \varphi + e, \dots$ with $1 \le \varphi \le e$), HP capped at $M$, starting at $h \le M$, death at 0 HP. In a shared second the hit may land before or after the heal. Write $\lambda = a/b$ (damage rate) and $r = c/e$ (heal rate), and $g = \gcd(a, c)$.

**Theorem T-0305.**
1. If $r \ge \lambda$ and $h > a + c - g$, the contestant never dies, and HP never falls below $h - (a + c - g)$.
2. If $r < \lambda$, the contestant dies at a time $\tau$ with
$$
\frac{hb}{a} \le \tau \le \frac{h + a + c}{\lambda - r}.
$$

So the largest steady damage rate a renewable heal can hold off forever is its own rate $r$, with no exception at equality.

*Proof.* (1) Fix a moment just after a hit (HP is lowest just after hits). Let $t_0$ be the last earlier moment at which a heal was capped, so HP was $M \ge h$ then, or $t_0 = 0$ with HP $h$ if no heal was ever capped. Since $t_0$ nothing was capped, so HP now is the start value plus $\Delta = cH - aD$, where $H$ and $D$ count heals and hits since $t_0$, and $L = t - t_0$. Three cases. From the start: $D \le \lfloor t/b \rfloor \le \lambda t$ and $H \ge t/e - 1$ (as $\varphi \le e$), so $\Delta \ge (r - \lambda)t - c > -(a + c)$. After a capped heal, hit first in shared seconds: a hit at $t_0$ came before the heal and is not counted, so the hits counted are those at $t, t - b, t - 2b, \dots$ that lie after $t_0$, and $D = \lceil L/b \rceil < L/b + 1$ (this is not $\le L/b$ in general: $b = 10$, a capped heal at $t_0 = 5$ and a hit at $t = 10$ give $D = 1 > L/b = 1/2$); the heals counted lie strictly between $t_0$ and $t$, so $H \ge \lceil L/e \rceil - 1 \ge L/e - 1$; hence $\Delta > c(L/e - 1) - a(L/b + 1) = (r - \lambda)L - a - c \ge -(a+c)$. After a capped heal, heal first: $D \le \lfloor L/b \rfloor + 1$ and $H = \lfloor L/e \rfloor > L/e - 1$, so $\Delta > (r - \lambda)L - a - c \ge -(a + c)$. In every case $\Delta > -(a + c)$, and $\Delta$ is a multiple of $g$, so $\Delta \ge -(a + c) + g$. HP is therefore at least $h - (a + c - g) \ge 1$. (2) Heals never lower HP, so HP $\ge h - a\lfloor t/b \rfloor$ and death needs $a \lfloor t/b \rfloor \ge h$, so $t \ge hb/a$. On the other side the total healed by time $t$ is at most $c\,(\lfloor (t - \varphi)/e \rfloor + 1) < rt + c$ and the damage is $a \lfloor t/b \rfloor > \lambda t - a$, so HP $< h + a + c - (\lambda - r)t$, which is at most 0 once $t \ge (h + a + c)/(\lambda - r)$. $\square$

*Tightness.* In the test domain ($a, c \le 3$; $b, e \le 6$; $M \le 9$; both orders), the dip $a + c - g$ is reached, and a contestant starting at exactly $h = a + c - g$ can die, for every pair $(a, c)$. Dropping $+c$ from the upper bound of part 2 makes it false: the test finds cases that die after $(h + a)/(\lambda - r)$. Whether the dip is reached for every $a$ and $c$ is not claimed.

*Corollary (several heal sources).* Replace the single heal by sources $j = 1, \dots, k$, each healing $c_j$ HP every $e_j$ s from a phase $1 \le \varphi_j \le e_j$, with any order inside a shared second. Write $r = \sum_j c_j/e_j$, $C = \sum_j c_j$ and $g = \gcd(a, c_1, \dots, c_k)$. If $r \ge \lambda$ and $h > a + C - g$ the contestant never dies and HP never falls below $h - (a + C - g)$; if $r < \lambda$ death comes at a time $\tau$ with $hb/a \le \tau \le (h + a + C)/(\lambda - r)$. *Proof.* The proof of the theorem, with one count $H_j$ per source: the source that was capped at $t_0$ obeys the bounds used there, and every other source has at least $\lceil L/e_j \rceil - 1 \ge L/e_j - 1$ heals strictly between $t_0$ and $t$ (at least $t/e_j - 1$ from the start, since $\varphi_j \le e_j$), so $\Delta > (r - \lambda)L - a - C$; part 2 uses $\sum_j c_j(\lfloor (t - \varphi_j)/e_j \rfloor + 1) < rt + C$. $\square$ *Label:* `DERIVED` for the model. *Test:* `test_t0305_corollary_several_heal_sources` (two sources, $a \in \{1, 2\}$, $c_1, c_2 \in \{1, 2\}$, $b, e_1, e_2 \le 4$, every pair of phases, $M \le 7$, both orders).

*Documented rates (HP per second, exact).* Damage: outside the zone, unsafe circle (M-0536), airstrike fire (M-0413), robot (M-0523): $1/2$; outside with a Hazmat suit (M-0209): $1/4$; tear gas (M-0410): $1/5$; guard zombie (M-0449): $2/5$, at most 30 HP per contestant; zombie (M-0441): $1/10$ each, at most 30 HP per zombie and contestant (`wiki-zombies-003`, M-0635); poison (M-0170): $1/90$; bleeding (M-0336): $1/300$; cyclops (M-0426): 2. The two zombie drains are therefore finite adversaries (30 HP each; how the cap counts is U-0008), and the dichotomy applies to them only until the cap is reached. Renewable heals: regeneration $1/1800$ (M-0652, U-0007 A), one healer's ability $1/600$ (M-0651; not from inside a smoke cloud, M-0227, U-0213). Finite heals: bandage $1/12$ for 2 min, Campfire 1 per person while the pool lasts (T-0304).

*Consequences* (`CONDITIONAL` on the readings named in each record).
- No renewable heal holds off any documented periodic damage: even regeneration plus one healer's ability ($1/450$) is below bleeding ($1/300$), the slowest damage. By the corollary, two healers on cooldown plus regeneration ($7/1800 \ge 6/1800$) cancel bleeding, which the ability cures anyway (M-0651); this also needs the healers to heal on a fixed 600 s clock, which is a modelling choice.
- A bandage ($1/12$) is faster than poison and bleeding, so while it lasts (2 min) the HP it pays exceeds what they take; it holds off nothing faster. After it ends, poison resumes; bleeding was cured by the bandage (M-0234).
- A Campfire (1 HP per second) is faster than every documented damage except the cyclops; how long it lasts against each is T-0304, not T-0305.
- Necromancy's drain transfer gives its owner up to $1/10$ HP per second per zombie and victim, 30 HP at most per pair (M-0635, U-0008, U-0613); chapter 07 treats it.

*Interaction with the hit pipeline.* If periodic ticks are hits (U-0002 A) and the defender is live on Kick, 1 HP ticks stay 1 HP under both readings of U-0001 (T-0002, T-0004), so the rates above do not change for them. Two-HP ticks become 1 HP under U-0001 A and stay 2 under B, halving tear gas and guard zombie rates under A; a cyclops hit of 10 becomes 9 under both. Body armor and a fortress absorb the first $f + a_{\text{armor}}$ HP of covered damage under T-0007, which acts like a larger starting $h$ in part 2 and does not change any rate; this carries T-0007's own conditions (U-0101 reading A, M-0217 reading A and U-0102, U-0103 reading A, M-0529 reading A) and the open question of which damage kinds armor covers (C-0102). These pipeline remarks are not proved or tested in this chapter; they restate T-0002, T-0004 and T-0007.

*Label:* `DERIVED` for the model; its use for Safe Zone is `CONDITIONAL` on the damage and heal sources being fixed-interval ticks with the stated phases, and on the readings of each rate's record. *Test:* `test_t0305_sustain_dichotomy` (exhaustive over $a, c \in \{1,2,3\}$, $b, e \in 1..6$, every phase, $M \le 9$, every $h \le M$, both orders; a repeated state (HP, time mod $\operatorname{lcm}(b, e)$) proves survival forever).

### T-0306: Healing regeneration under damage (extends T-0011)

Reading B of U-0007 says "damage" restarts the timer. Whether a periodic tick (zone, poison, bleeding, a zombie drain) is "damage" in that sense is not settled: U-0002 asks whether periodic drains go through the hit pipeline at all, and U-0332 whether a bleeding tick counts as a hit (its reading A: "ticks are plain damage events"). We call *ticks reset* the reading in which every periodic tick restarts the timer (natural under U-0002 A), and *ticks do not reset* the reading in which only discrete hits do (possible under U-0002 B or C). No record decides it.

**Theorem T-0306.** (a) Under U-0007 reading B with ticks reset, a Healing contestant who takes damage at least once every 1,799 s never regenerates after the first hit; at exactly 1,800 s the result depends on the same-second order (the hit first: no regeneration). Every documented periodic damage source (T-0305 list) qualifies while it lasts. With ticks do not reset, a periodic source does not stop regeneration at all, and only discrete hits count.

(b) Under U-0007 reading A (fixed clock), regeneration is slower than every documented periodic damage, so by T-0305 it holds none of them off. Against bleeding alone (1 HP every 300 s, first tick 300 s after the hit, U-0332 A), from 100 of 100 HP, death comes between 35,700 s and 36,000 s (9 h 55 min to 10 h) over every phase of the regeneration clock and both same-second orders, against 30,000 s (8 h 20 min) without regeneration. Under reading B with ticks reset, bleeding suppresses regeneration and death comes at 30,000 s. Under reading B with ticks do not reset, the Deep Cut hit at second 0 is the last reset, regeneration runs at 1,800, 3,600, ... s, and death comes at 35,700 s.

*Proof.* (a) The timer reaches 1,800 s only after 1,800 s without a reset. (b) $1/1800 < 1/300$; the death times are computed exactly for each of the 1,800 phases and both orders (event-driven, integer seconds), and lie inside the bounds of T-0305 part 2, $[30000, 36720]$. Reading B with ticks do not reset is reading A with phase 1,800. $\square$

*Consequence.* Regeneration helps only between fights, at 48 HP a day at most (T-0011). A Healing contestant who can heal herself (U-0623 reading C) cures her own bleeding and poison every 10 min, which matters far more than regeneration. Where the regeneration clock starts (event start or sigil pick) is open (M-0601).

*Label:* (a) `CONDITIONAL` on U-0007 reading B and on the ticks-reset reading (U-0002, U-0332), each case named; (b) `CONDITIONAL` on U-0332 reading A and on U-0007 reading A, or on reading B with the tick reading named. *Test:* `test_t0306_regeneration_extended` (both tick readings).

## 3.5 Revival

A revive is the only way back from 0 HP: the target returns with 5 HP and the reviver pays 5 HP (M-0656), within 10 min of the death (M-0655, U-0011), with the revive caps of M-0653 and M-0654 (U-0107, U-0624) and the open question of who may revive whom (U-0108, C-0105). Under U-0625 reading A the pair's total HP is unchanged by the revive. If the cost is a hit (U-0002 A) and the reviver is live on Kick, it is 4 HP under U-0001 A ($\lfloor 45/10 \rfloor$) and 5 under B, and body armor can absorb it. Revives never pay Piety tokens (M-0501); a Healing reviver earns 20 tokens per revive (M-0650). `CONDITIONAL` on the U-ids named.

## Open questions

The chapter depends on these recorded unknowns: U-0001, U-0002, U-0006, U-0007, U-0008, U-0011, U-0014 (healing circle price), U-0101, U-0102, U-0103 (through T-0007), U-0107, U-0108, U-0200, U-0203, U-0204, U-0213 (goggles and the smoke heal restriction), U-0214, U-0322, U-0323, U-0330, U-0331, U-0332, U-0401 (whether an EMP stops a healing circle), U-0413, U-0500, U-0501, U-0502, U-0503, U-0519, U-0520, U-0532, U-0600, U-0601, U-0602, U-0603, U-0613, U-0617, U-0618, U-0619, U-0622, U-0623, U-0624, U-0625; contradictions C-0102 and C-0105.

Open questions not yet recorded in `kb/unknowns/` (this chapter's review could not write to `kb/`; each needs a U-id in the next KB pass):

1. **Protection cut and the cap (T-0301).** Is "Potions heal you 50% less" (M-0645) applied to the potion's tier heal, then capped, or to the HP the potion would restore? A gigantic potion at 10 missing HP gives 10 HP or 5 HP.
2. **God's Fruit at full HP.** In "heals 20 HP and is cured of poison, even at full HP" (M-0434), does "even at full HP" attach to the cure only (the heal is capped), or does the heal take HP above max HP? U-0203 covers potions, bandages and Eddie's potion, not God's Fruit. (M-0434 carries the label `DOCUMENTED` while its own notes say overheal is unspecified; this chapter uses the capped reading and says so where it does.)
3. **Periodic ticks and the regeneration timer (T-0306).** Under U-0007 reading B, does a zone, poison, bleeding or zombie tick restart the 30 min timer, or only a discrete hit? Neither U-0002 nor U-0332 asks it in these words.
4. **Protection cut on a bandage, per tick or on the total (T-0300, item 3).** Under U-0617 reading C, is 50% taken off each 1 HP or 2 HP tick (a floor reading then pays 0 or 1 HP per tick) or off the 10 HP total?
