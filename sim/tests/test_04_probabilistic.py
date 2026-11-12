"""Prover tests for theory/04-probabilistic-items.md (T-0400..T-0408).

Exact rational arithmetic throughout (fractions.Fraction). Each test enumerates the integer
domain the theorem talks about, or the stated sweep of free parameters. These tests check our
model of the rules, not the game.
"""
import itertools
import math
from fractions import Fraction as F
from functools import lru_cache

from safezone_sim.ch04 import (P_HEAL, ROUNDINGS, binom_pmf, drink_value, eddie_amounts, eddie_outcomes,
                               expected_min, geometric_moments, moments, optimal_hold, p_at_least_one,
                               reachable_max_hp, survival)

REACHABLE = sorted(reachable_max_hp())
PAIRS = list(itertools.product(ROUNDINGS, ROUNDINGS))


def assert_geometric(p, mean, var, terms=1500, tol=F(1, 10 ** 9)):
    """Check (mean, var) of the first-success time against partial sums of its law P(N = i) = (1-p)^(i-1) p,
    which do not use the closed forms 1/p and (1-p)/p^2."""
    m1 = m2 = F(0)
    w = p
    for i in range(1, terms):
        m1 += i * w
        m2 += i * i * w
        w *= 1 - p
    assert abs(m1 - mean) < tol and abs(m2 - m1 ** 2 - var) < tol
    assert geometric_moments(p) == (mean, var)


def test_t0400_rounding_readings_and_reachable_max_hp():
    for M in range(1, 221):
        heals = {eddie_amounts(M, r, "floor")[0] for r in ROUNDINGS}
        losses = {eddie_amounts(M, "floor", r)[1] for r in ROUNDINGS}
        assert (len(heals) == 1) == (M % 2 == 0)
        assert (len(losses) == 1) == (M % 10 == 0)
        half_differs = eddie_amounts(M, "floor", "half_up")[1] != eddie_amounts(M, "floor", "floor")[1]
        assert half_differs == (M % 10 in {2, 3, 5, 6, 9})
    assert REACHABLE == list(range(90, 221, 10))
    assert sorted(reachable_max_hp(purchase_limit=10)) == list(range(90, 211, 10))
    for M in REACHABLE:
        assert {eddie_amounts(M, a, b) for a, b in PAIRS} == {(M // 2, 3 * M // 10)}


def law_closed_form(M, h, g, l, kill):
    a = min(g, M - h)
    b = min(l, h) if kill == "A" else min(l, h - 1)
    return F(a - 9 * b, 10), F(9 * (a + b) ** 2, 100)


def test_t0401_exact_law_of_one_drink():
    for kill in "AC":
        for M in range(4, 221):
            for hr, lr in PAIRS:
                g, l = eddie_amounts(M, hr, lr)
                h_E = (g - 1) // 9
                assert h_E <= l and g < 9 * l
                positive = []
                for h in range(1, M + 1):
                    out = eddie_outcomes(M, h, g, l, kill=kill)
                    mean, var = moments(out, h)
                    assert (mean, var) == law_closed_form(M, h, g, l, kill)
                    p_dead = sum(p for p, x in out if x == 0)
                    assert p_dead == (F(9, 10) if kill == "A" and h <= l else 0)
                    if mean > 0:
                        positive.append(h)
                    if kill == "A" and h >= l:
                        bound = F(g - 9 * l, 10)
                        assert mean <= bound < 0 and (mean == bound) == (h <= M - g)
                assert positive == list(range(1, h_E + 1 + (kill == "C")))
    # reachable M: the maximum over h >= l is -11M/50, and the h_E list of the chapter
    for M in REACHABLE:
        g, l = eddie_amounts(M)
        assert max(moments(eddie_outcomes(M, h, g, l), h)[0] for h in range(l, M + 1)) == F(-11 * M, 50)
    assert [(eddie_amounts(M)[0] - 1) // 9 for M in REACHABLE] == [4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12]
    assert moments(eddie_outcomes(100, 100, 50, 30), 100) == (-27, 81)
    assert moments(eddie_outcomes(100, 50, 50, 30), 50)[0] == -22
    assert moments(eddie_outcomes(100, 1, 50, 30), 1)[0] == F(41, 10)


def armor_by_units(h, L, alpha, min1):
    """Independent model of steps 7 and the final minimum: the loss L arrives one HP at a time and the armor
    pool takes each unit while it lasts (U-0209 A); under U-0103 B a hit that got through costs at least 1 HP.
    Returns (HP after, durability spent)."""
    pool, hp = alpha, h
    for _ in range(L):
        if pool:
            pool -= 1
        elif hp:
            hp -= 1
    if min1 and L and hp == h:
        hp -= 1
    return hp, alpha - pool


def test_t0402_potion_under_protection():
    for M in REACHABLE:
        g, l = eddie_amounts(M)
        for h in range(1, M + 1):
            # (a) a blocker: free lottery, never kills, even with the final 1 HP minimum
            for min1 in (False, True):
                out = eddie_outcomes(M, h, g, l, blocked=True, min1=min1)
                assert moments(out, h)[0] == F(min(g, M - h), 10) and all(x >= h for _, x in out)
        # (b) against the unit-by-unit model: HP lost min(max(L - alpha, 0), h), durability spent min(L, alpha)
        for h in sorted(set(range(1, M + 1, 3)) | {l - 1, l, l + 1, M}):
            for alpha in (0, 1, 14, 15, 16, 25, 26, 27, 30, 44, 45, 46, 66):
                for kick in (None, "A", "B"):
                    L = {None: l, "A": 9 * l // 10, "B": l - l // 10}[kick]
                    for min1 in (False, True):
                        down = eddie_outcomes(M, h, g, l, armor=alpha, kick=kick, min1=min1)[1][1]
                        hp, spent = armor_by_units(h, L, alpha, min1)
                        assert down == hp and spent == min(L, alpha)
                        if not min1:
                            assert h - down == min(max(L - alpha, 0), h)
        assert (eddie_outcomes(M, M, g, l, armor=45)[1][1] == M) == (M <= 150)
        # U-0103 reading B: full absorption still costs exactly 1 HP
        assert (eddie_outcomes(M, M, g, l, armor=45, min1=True)[1][1] == M - 1) == (M <= 150)
        assert l > 25  # U-0338 reading B: one enchantment (durability 25) never absorbs a whole reachable loss
    assert moments(eddie_outcomes(100, 50, 50, 30, armor=15), 50)[0] == F(-17, 2)
    assert moments(eddie_outcomes(100, 50, 50, 30, armor=30, min1=True), 50)[0] == F(41, 10)
    assert F(9, 10) * min(30, 45) == 27  # expected durability spent at M = 100, armor 45
    # (c) Kick table and the equality set
    LA = [9 * eddie_amounts(M)[1] // 10 for M in REACHABLE]
    LB = [eddie_amounts(M)[1] - eddie_amounts(M)[1] // 10 for M in REACHABLE]
    assert LA == [24, 27, 29, 32, 35, 37, 40, 43, 45, 48, 51, 54, 56, 59]
    assert LB == [25, 27, 30, 33, 36, 38, 41, 44, 46, 49, 52, 54, 57, 60]
    assert [M for M, a, b in zip(REACHABLE, LA, LB) if a == b] == [100, 200]
    assert all(b - a == 1 for a, b in zip(LA, LB) if a != b)
    # (d) Protection halves the heal, three readings of M-0645 / U-0618: floor, ceil, exact
    h_E_found = {}
    for M in REACHABLE:
        g, l = eddie_amounts(M)
        halves = (F(g // 2), F(-(-g // 2)), F(g, 2))
        assert (len(set(halves)) == 1) == (M % 20 == 0)
        for name, gP in zip(("floor", "ceil", "exact"), halves):
            positive = [h for h in range(1, M + 1) if moments(eddie_outcomes(M, h, gP, l), h)[0] > 0]
            h_E = math.ceil(gP / 9) - 1
            assert positive == list(range(1, h_E + 1)) and h_E <= l
            h_E_found[M, name] = h_E
    assert [h_E_found[100, r] for r in ("floor", "ceil", "exact")] == [2, 2, 2]
    assert [h_E_found[110, r] for r in ("floor", "ceil", "exact")] == [2, 3, 3]


def chains():
    """The swept environments: lose c w.p. q, heal a w.p. r, else nothing; horizon T. Free parameters."""
    for c, q, (a, r), T in itertools.product([1, 5, 10, 20], [F(1, 10), F(1, 4), F(1, 2)],
                                             [(0, F(0)), (5, F(1, 4)), (20, F(1, 10))], [5, 10, 20, 40]):
        yield c, ([(q, -c), (r, a), (1 - q - r, 0)] if r else [(q, -c), (1 - q, 0)]), T


def test_t0403_one_drink_decision_boundary():
    M = 100
    g, l = eddie_amounts(M)
    count = 0
    for c, moves, T in chains():
        S = survival(M, T, moves)
        assert S[0] == 0 and all(S[x] <= S[x + 1] for x in range(M))
        for kill in "AC":
            for h in range(1, M + 1):
                D = drink_value(S, eddie_outcomes(M, h, g, l, kill=kill))
                hp = min(M, h + g)
                better = D > S[h]
                if kill == "A" and h <= l:
                    assert better == (S[hp] > 10 * S[h])
                    if S[h] >= F(1, 10):
                        assert not better
                else:
                    hm = h - l if kill == "A" else max(h - l, 1)
                    assert better == (S[hp] - S[h] > 9 * (S[h] - S[hm]))
                hm_any = max(h - l, 0 if kill == "A" else 1)
                if better:
                    assert S[h] < F(1, 10) + F(9, 10) * S[hm_any]
        count += 1
    assert count == 144


def test_t0404_waiting_dominates_and_no_threshold():
    M = 100
    g, l = eddie_amounts(M)
    envs = [[(q, -c), (1 - q, 0)] for c in (1, 5, 10, 20, 35) for q in (F(1, 10), F(1, 4), F(1, 2))]
    envs.append([(F(1, 4), -5), (F(1, 10), -20), (F(13, 20), 0)])
    for moves, T, kill in itertools.product(envs, (5, 10, 20), "AC"):
        c = max(-d for _, d in moves)
        _, _, drink_set = optimal_hold(M, T, moves, g, l, kill=kill)
        assert all(x <= c for _, x in drink_set), (moves, T, kill)
    # (b) both examples, each under both readings of U-0004: (drink-now set, holder's set with 10 steps left)
    def sets(moves, kill):
        S = survival(M, 10, moves)
        now = [h for h in range(1, M + 1) if drink_value(S, eddie_outcomes(M, h, g, l, kill=kill)) > S[h]]
        _, _, hold = optimal_hold(M, 10, moves, g, l, kill=kill)
        return now, sorted(x for t, x in hold if t == 10)

    ex1 = [(F(1, 2), -30), (F(1, 2), 0)]
    S = survival(M, 10, ex1)
    assert [S[x] for x in (1, 31, 61, 91)] == [F(1, 1024), F(11, 1024), F(56, 1024), F(176, 1024)]
    for kill in "AC":
        assert sets(ex1, kill) == (list(range(1, 31)) + list(range(41, 61)), list(range(1, 31)))
    ex2 = [(F(1, 4), -20), (F(3, 4), 0)]
    assert survival(M, 10, ex2)[10] == F(3, 4) ** 10 == F(59049, 1048576)
    assert sets(ex2, "A") == (list(range(11, 21)), list(range(11, 21)))
    assert sets(ex2, "C") == (list(range(1, 21)), list(range(1, 21)))


def test_t0404_heal_sweep_supports_hypothesis():
    """Evidence for the HYPOTHESIS part of T-0404, not a proof: chains with healing."""
    M = 100
    g, l = eddie_amounts(M)
    n = 0
    for c, q, (a, r), T in itertools.product([1, 5, 10, 20, 35], [F(1, 10), F(1, 4), F(1, 2)],
                                             [(5, F(1, 4)), (20, F(1, 10)), (40, F(1, 4))], [5, 10, 20]):
        _, _, drink_set = optimal_hold(M, T, [(q, -c), (r, a), (1 - q - r, 0)], g, l)
        assert all(x <= c for _, x in drink_set)
        n += 1
    assert n == 135


def test_t0405_repeated_drinks_toward_a_target():
    for kill in "AC":
        for M in REACHABLE:
            g, l = eddie_amounts(M)
            floor = 0 if kill == "A" else 1

            @lru_cache(maxsize=None)
            def P(h, n, k):
                """(probability of reaching k, expected drinks) drinking while below k."""
                if h >= k:
                    return F(1), F(0)
                if h == 0 or n == 0:
                    return F(0), F(0)
                ps, ds = P(min(M, h + g), n - 1, k)
                pf, df = P(max(h - l, floor), n - 1, k)
                return P_HEAL * ps + (1 - P_HEAL) * pf, 1 + P_HEAL * ds + (1 - P_HEAL) * df

            checked = 0
            for h in range(1, M, 3):
                J = (h - 1) // l
                for k in range(h + 1, M + 1, 4):
                    for n in range(1, 7):
                        m = min(n, J + 1) if kill == "A" else n
                        # HP after j failures: h - j*l (reading A, alive for j <= J), max(h - j*l, 1) (reading C)
                        if all(min(M, max(h - j * l, floor) + g) >= k for j in range(m)):
                            assert P(h, n, k) == (1 - F(9, 10) ** m, 10 * (1 - F(9, 10) ** m))
                            checked += 1
            assert checked > 100
        if kill == "A":
            assert all((M - 1) // eddie_amounts(M)[1] == 3 for M in REACHABLE)
    assert_geometric(P_HEAL, 10, 90)  # (c) unlimited potions under reading C


def test_t0405_examples():
    g, l = eddie_amounts(100)
    assert (40 - 1) // l == 1 and 40 - l + g == 60
    assert p_at_least_one(P_HEAL, 2) == F(19, 100)


def test_t0406_red_and_black_hypotheses_fail():
    for M in REACHABLE:
        g, l = eddie_amounts(M)
        assert F(g, l) == F(5, 3)                       # H3: odds 5:3, not even money
        assert moments(eddie_outcomes(M, 1, g, l), 1)[0] > 0  # H4: superfair at h = 1
        assert moments(eddie_outcomes(M, M, g, l), M)[0] < 0  # subfair at full HP
        assert (M - 1) // l + 1 == 4                    # H6: at most 4 drinks from full HP under reading A
    # (b) S(h) = 0 < S(h+) makes never drinking non-optimal, but not drinking now optimal
    M, (g, l) = 100, eddie_amounts(100)
    moves = [(F(1, 2), -10), (F(1, 2), -20)]
    waits = 0
    for T in range(2, 9):
        V, _, drink_set = optimal_hold(M, T, moves, g, l)
        S = survival(M, T, moves)
        for h in range(1, M + 1):
            if S[h] == 0 < S[min(M, h + g)]:
                D = drink_value(S, eddie_outcomes(M, h, g, l))
                assert V[h] >= D >= S[min(M, h + g)] / 10 > 0 == S[h]
                waits += (T, h) not in drink_set
    assert waits > 0
    V, _, drink_set = optimal_hold(M, 7, moves, g, l)
    S = survival(M, 7, moves)
    assert (S[70], S[100]) == (0, F(29, 128))
    assert drink_value(S, eddie_outcomes(M, 70, g, l)) == F(29, 1280)
    assert V[70] == F(99, 1280) and (7, 70) not in drink_set


def test_t0407_zombie_rolls():
    p_break, p_craft = F(1, 10), F(2, 5)
    assert_geometric(p_break, 10, 90)
    assert_geometric(p_craft, F(5, 2), F(15, 4))
    assert abs(float(F(9, 10) ** 30) - 0.0424) < 5e-5
    # per encounter: one roll destroying one of c crafts chosen uniformly, by enumeration of the chosen craft
    for c in range(1, 7):
        survive = (1 - p_craft) + p_craft * F(sum(1 for chosen in range(c) if chosen != 0), c)
        assert survive == 1 - p_craft / c
    assert 1 - p_craft / 5 == F(23, 25)

    def lost_by_chain(k, n, p):
        """Expected items lost, by a chain on the number of items left (independent of binomial sums)."""
        dist = {k: F(1)}
        for _ in range(n):
            new = {}
            for left, q in dist.items():
                if left:
                    new[left - 1] = new.get(left - 1, 0) + q * p
                    new[left] = new.get(left, 0) + q * (1 - p)
                else:
                    new[0] = new.get(0, 0) + q
            dist = new
        return sum(q * (k - left) for left, q in dist.items()), dist.get(k, 0)

    for k, n, p, approx in [(6, 30, p_break, 2.9638), (3, 30, p_break, 2.3626),
                            (5, 10, p_craft, 3.7649), (5, 30, p_craft, 4.9981)]:
        e, _ = lost_by_chain(k, n, p)
        assert e == expected_min(k, n, p) and abs(float(e) - approx) < 5e-5
    assert abs(float(sum(binom_pmf(30, p_craft)[:5])) - 0.0015) < 5e-5
    assert abs(float(F(3, 5) ** 10) - 0.0060) < 5e-5
    assert F(3, 5) ** 30 < F(23, 10 ** 8) and F(3, 5) ** 30 > F(22, 10 ** 8)


def test_t0408_greed_shield_and_trolling_diversion():
    p_shield, p_div = F(1, 4), F(3, 100)
    assert_geometric(p_shield, 4, 12)
    assert_geometric(p_div, F(100, 3), F(9700, 9))
    assert p_at_least_one(p_shield, 2) == F(7, 16) and p_at_least_one(p_shield, 3) == F(37, 64)

    def first_n(p, target):
        return next(n for n in range(1, 10 ** 4) if p_at_least_one(p, n) >= target)

    assert (first_n(p_shield, F(1, 2)), first_n(p_shield, F(9, 10))) == (3, 9)
    assert (first_n(p_div, F(1, 2)), first_n(p_div, F(9, 10))) == (23, 76)
    assert abs(float(p_at_least_one(p_div, 5)) - 0.1413) < 5e-5
    assert p_at_least_one(p_div, 2) == F(591, 10000)
    # U-0511 reading B: expected Shield minutes per claim = 20 * E[Binomial(n, 1/4)] / n = 5
    for n in range(1, 13):
        assert sum(q * 20 * j for j, q in enumerate(binom_pmf(n, p_shield))) / n == 5


def test_section_4_5_piety_uniform_baseline():
    """Section 4.5 (not a theorem): expected nominal heal of a uniformly random tier, with and without Piety."""
    tiers = [5, 10, 20, 40]
    assert sum(F(x * 115 // 100, 4) for x in tiers) == F(85, 4)
    assert sum(F(x, 4) for x in tiers) == F(75, 4)
