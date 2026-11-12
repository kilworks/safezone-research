"""Prover tests for theory/03-healing-and-sustain.md (T-0300..T-0306).

Each test enumerates every case of a bounded domain (exact integers and fractions, no floats)
or a domain the proof shows to be sufficient. They check our model of the rules, not the game.
"""
from fractions import Fraction
from math import gcd

from safezone_sim.ch03 import (ALL_M, CONVERT, PROTECTION_SCOPE, REACHABLE_M, TIERS, bandage_schedule,
                               bandage_time_to_full, bandage_waste, campfire_standby, campfire_static,
                               drink_tokens, pct, piety, protection, regen_with_reset, sustain)


def cdiv(x, y):
    return -(-x // y)


def test_t0300_where_heal_rounding_matters():
    # Protection cut (M-0645, U-0618 readings A, B, C) on every heal U-0617 may put in scope, every Protection M
    split = set()
    for scope, kinds in PROTECTION_SCOPE.items():
        for M in REACHABLE_M["other"]:
            heals = [(name, "potion", x) for name, x in TIERS.items()] + [
                ("eddie", "eddie", pct(M, 50, "A")), ("bandage total", "bandage", 10),
                ("healing circle", "circle", 25), ("god's fruit", "fruit", 20)]
            for name, kind, x in heals:
                assert pct(M, 50, "A") == pct(M, 50, "B")  # M/2 itself is an integer on the grid
                values = {protection(x, r) for r in "ABC"} if kind in kinds else {x}
                if len(values) > 1:
                    split.add((scope, name, M))
                    assert sorted(values) == [Fraction(x // 2), Fraction(x, 2), Fraction(cdiv(x, 2))]
    tenmod20 = [M for M in REACHABLE_M["other"] if M % 20 == 10]
    expected = {(s, "small", M) for s in "ABC" for M in REACHABLE_M["other"]}
    expected |= {(s, "eddie", M) for s in "BC" for M in tenmod20}
    expected |= {("C", "healing circle", M) for M in REACHABLE_M["other"]}
    assert split == expected
    assert [protection(5, r) for r in "ABC"] == [2, 3, Fraction(5, 2)]
    assert [protection(55, r) for r in "ABC"] == [27, 28, Fraction(55, 2)]  # M = 110, Eddie, U-0617 B or C
    # 5% of max HP (Death rob, M-0611, U-0600): A, B, D differ exactly when M = 10 mod 20; C equals B
    for M in ALL_M:
        lo, hi, half_up, exact = (pct(M, 5, r) for r in "ABCD")
        if M % 20 == 10:
            assert hi - lo == 1 and lo < exact < hi
        else:
            assert lo == hi == exact
        assert half_up == hi
    assert [pct(M, 5, "A") for M in REACHABLE_M["other"]] == [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
    # 50%, 30%, 60% of max HP (Eddie, M-0208; Death cap, M-0614), uncut: one value on every reachable M
    for M in ALL_M:
        for num in (50, 30, 60):
            assert pct(M, num, "A") == pct(M, num, "B") == pct(M, num, "C") == pct(M, num, "D")
    # the hypothesis "M is a multiple of 10" is needed: off the grid the readings split
    assert pct(95, 30, "A") != pct(95, 30, "B")


def test_t0301_bonus_commutes_with_the_cap_but_a_cut_does_not():
    boosts = [piety, lambda y: y + y // 10, lambda y: 2 * y]  # non-decreasing, g(y) >= y
    for m in range(0, 231):
        for x in range(0, 120):
            for g in boosts:
                assert min(m, g(min(x, m))) == min(m, g(x))  # U-0503 readings A, B, C agree on HP
            # Protection cut (M-0645): halving the effective heal vs halving the tier heal
            for rd in "AB":
                eff, nominal = protection(min(x, m), rd), min(m, protection(x, rd))
                differ = x > m and protection(x, rd) > protection(m, rd) and m > protection(m, rd)
                assert (eff != nominal) == differ
                assert eff <= nominal
    assert (protection(10, "A"), min(10, protection(40, "A"))) == (5, 10)  # gigantic at 10 missing HP


def test_t0302_piety_drink_or_convert():
    for M in REACHABLE_M["piety"]:
        for m in range(0, M):
            for tier, c in CONVERT.items():
                for basis in "ABCD":
                    yields = [drink_tokens(tier, m, basis, carry) for carry in range(5)]
                    assert min(yields) == yields[0]  # a carried remainder never lowers the yield
                    always = yields[0] >= c
                    assert always == (basis in "BC" or m >= 5 * c)
    full = {b: [drink_tokens(t, 220, b) for t in TIERS] for b in "ABCD"}
    assert full == {"A": [1, 2, 4, 9], "B": [1, 2, 4, 9], "C": [1, 2, 4, 8], "D": [1, 2, 4, 8]}
    assert [piety(x) for x in TIERS.values()] == [5, 11, 23, 46]  # T-0005, reused


def test_t0303_bandage_time_to_full():
    base = {"A": lambda m: 12 * m, "B": lambda m: 12 * (m - 1), "C": lambda m: 24 * cdiv(m, 2),
            "D": lambda m: 12 * m}
    for rd, f in base.items():
        sched = bandage_schedule(rd)  # D is built as a 0.2 s grid of 1/60 HP, not from the A ticks
        assert sum(hp for _, hp in sched) == 10 and max(t for t, _ in sched) <= 120
        for m in range(1, 11):
            assert bandage_time_to_full(sched, m) == f(m)
            assert bandage_waste(sched, m) == 10 - m
        assert bandage_time_to_full(sched, 11) is None
        # Protection (M-0646, U-0619): A stretches every time by 1.1, B and C keep the times and change the total
        prot_a = bandage_schedule(rd, "A")
        assert sum(hp for _, hp in prot_a) == 10
        for m in range(1, 11):
            assert bandage_time_to_full(prot_a, m) == Fraction(11, 10) * f(m)
            assert bandage_waste(prot_a, m) == 10 - m
        for pr, up in (("B", False), ("C", False), ("C", True)):
            sched = bandage_schedule(rd, pr, up)
            total = 11 if rd != "C" else 12 if up else 10
            assert sum(hp for _, hp in sched) == total
            for m in range(1, total + 1):
                assert bandage_time_to_full(sched, m) == f(m)
                assert bandage_waste(sched, m) == total - m
            assert bandage_time_to_full(sched, total + 1) is None
    # spread of the time to full across readings, for each missing HP m
    plain = [[bandage_time_to_full(bandage_schedule(r), m) for r in "ABCD"] for m in range(1, 11)]
    assert [max(v) - min(v) for v in plain] == [24 if m % 2 else 12 for m in range(1, 11)]
    combos = [bandage_schedule(r, pr, up) for r in "ABCD"
              for pr, up in (("A", False), ("B", False), ("C", False), ("C", True))]
    prot = [[bandage_time_to_full(s, m) for s in combos] for m in range(1, 11)]
    assert [max(v) - min(v) for v in prot] == [
        Fraction(6 * m + 126, 5) if m % 2 else Fraction(6 * m + 60, 5) for m in range(1, 11)]
    assert max(max(v) - min(v) for v in prot) == 36  # at m = 9


def test_t0304_campfire_pool():
    for P in TIERS.values():
        for n in (1, 2, 3):
            grids = [(d,) for d in range(46)] if n == 1 else [
                (d1, d2) for d1 in range(0, 46, 3) for d2 in range(0, 46, 5)] if n == 2 else [
                (d1, d2, d3) for d1 in range(0, 25, 4) for d2 in range(0, 25, 6) for d3 in (0, 1, 7, 40)]
            for ds in grids:
                for tb in range(n):
                    for rd in ("A", "B1"):  # U-0520 A, and B shared only by those missing HP
                        got, t, _ = campfire_static(P, ds, rd, tb)
                        assert got == min(P, sum(ds)) and t <= P
                    got, t, left = campfire_static(P, ds, "C", tb)  # C: burns n HP/s whatever
                    assert t == -(-P // n) and left == 0 and got <= min(P, sum(ds))
                # B shared by everyone in range (B2): each gets P/n at most
                got, t, left = campfire_static(P, ds, "B2")
                assert (got, t, left) == (sum(min(Fraction(d), Fraction(P, n)) for d in ds), P, 0)
                assert got <= min(P, sum(ds))
        assert campfire_static(P, (0,), "C") == (0, P, 0)  # a lone full-HP owner wastes it all
    assert campfire_static(40, (0, 30), "B2")[0] == 20 < campfire_static(40, (0, 30), "B1")[0] == 30
    for P in TIERS.values():  # standby against a drain of a HP every b s from phase s, at most N hits
        for a in (1, 2, 3):
            K = cdiv(P, a)
            for b in range(a, 31):
                for s in sorted({1, (b + 1) // 2, b}):
                    for N in sorted({None, K - 1, K, 1} - {0}, key=lambda v: -1 if v is None else v):
                        last, low, left = campfire_standby(P, 100, a, b, "A", s, N)
                        assert low == 100 - a
                        if N is None or N >= K:
                            end, rest = s + (K - 1) * (b - a) + P - 1, 0
                        else:
                            end, rest = s + (N - 1) * b + a - 1, P - N * a
                        assert (last, left) == (end, rest) if end <= 600 else left > rest
                        assert campfire_standby(P, 100, a, b, "B1", s, N) == (last, low, left)
                        for rd in ("B2", "C"):
                            assert campfire_standby(P, 100, a, b, rd, s, N)[0] == P
    # examples, gigantic potion (P = 40), reading A
    assert [campfire_standby(40, 100, 1, 2, "A", s)[0] for s in (5, 7)] == [83, 85]  # M-0101 A, B
    for s in range(1, 11):  # one zombie, 30 HP cap (wiki-zombies-003 in M-0635), any phase
        assert campfire_standby(40, 100, 1, 10, "A", s, 30) == (s + 290, 99, 10)
    for s in range(1, 6):  # guard zombie, 30 HP cap (M-0449)
        assert campfire_standby(40, 100, 2, 5, "A", s, 15) == (s + 71, 98, 10)
    assert [campfire_standby(40, 100, 1, 90, "A", s)[2] for s in (90, 0)] == [34, 33]  # M-0170 A, B


def test_t0305_sustain_dichotomy():
    needs_c = False
    for a in (1, 2, 3):
        for c in (1, 2, 3):
            dip = a + c - gcd(a, c)
            worst_dip, dead_at_dip = 0, False
            for b in range(1, 7):
                for e in range(1, 7):
                    lam, r = Fraction(a, b), Fraction(c, e)
                    for phi in range(1, e + 1):
                        for M in range(1, 10):
                            for h in range(1, M + 1):
                                for order in ("dh", "hd"):
                                    fate, t, low = sustain(h, M, a, b, c, e, phi, order)
                                    if r >= lam and fate == "lives":
                                        worst_dip = max(worst_dip, h - low)
                                    if r >= lam and h > dip:
                                        assert fate == "lives" and low >= h - dip
                                    if r >= lam and h == dip and fate == "dies":
                                        dead_at_dip = True
                                    if r < lam:
                                        assert fate == "dies"
                                        assert Fraction(h, 1) / lam <= t <= (h + a + c) / (lam - r)
                                        needs_c |= t > (h + a) / (lam - r)
            assert worst_dip == dip and dead_at_dip  # the bound is attained in this domain
    assert needs_c  # dropping +c from the upper bound of part 2 makes it false
    # proof step, hit first after a capped heal at t0: hits in (t0, t] number ceil(L/b) < L/b + 1, can exceed L/b
    over = False
    for b in range(1, 13):
        for t0 in range(0, 3 * b):
            for t in range(b, 6 * b, b):
                if t > t0:
                    L, D = t - t0, sum(1 for k in range(1, t // b + 1) if t0 < k * b)
                    assert D == cdiv(L, b) and D < Fraction(L, b) + 1
                    over |= D > Fraction(L, b)
    assert over and sustain(9, 9, 1, 10, 1, 5, 5, "dh")[0] == "lives"  # b = 10, e = 5: D = 1 > L/b = 1/2
    # documented rates, HP per second (exact): the largest renewable heal is below every periodic damage
    damage = {"zone": Fraction(1, 2), "hazmat zone": Fraction(1, 4), "tear gas": Fraction(1, 5),
              "guard zombie": Fraction(2, 5), "zombie": Fraction(1, 10), "poison": Fraction(1, 90),
              "bleeding": Fraction(1, 300), "cyclops": Fraction(2)}
    regen, ability = Fraction(1, 1800), Fraction(1, 600)
    assert regen + ability < min(damage.values()) == Fraction(1, 300)
    assert min(k for k in range(10) if regen + k * ability >= damage["bleeding"]) == 2
    bandage = Fraction(10, 120)
    assert {k for k, v in damage.items() if v <= bandage} == {"poison", "bleeding"}
    assert {k for k, v in damage.items() if v <= 1} == set(damage) - {"cyclops"}


def test_t0305_corollary_several_heal_sources():
    for a in (1, 2):
        for b in range(1, 5):
            for c1 in (1, 2):
                for c2 in (1, 2):
                    dip = a + c1 + c2 - gcd(gcd(a, c1), c2)
                    for e1 in range(1, 5):
                        for e2 in range(1, 5):
                            lam, r = Fraction(a, b), Fraction(c1, e1) + Fraction(c2, e2)
                            for p1 in range(1, e1 + 1):
                                for p2 in range(1, e2 + 1):
                                    for M in range(1, 8):
                                        for h in range(1, M + 1):
                                            for order in ("dh", "hd"):
                                                fate, t, low = sustain(h, M, a, b, c1, e1, p1, order,
                                                                       more=((c2, e2, p2),))
                                                if r >= lam and h > dip:
                                                    assert fate == "lives" and low >= h - dip
                                                if r < lam:
                                                    assert fate == "dies"
                                                    assert h / lam <= t <= (h + a + c1 + c2) / (lam - r)


def test_t0306_regeneration_extended():
    # U-0007 reading B: damage at least every 1799 s means no regeneration ever
    for g in range(1, 1800):
        assert regen_with_reset(g, 3 * 1800) == 0
    assert regen_with_reset(1800, 3 * 1800) == 0  # a shared second: the damage resets first
    assert regen_with_reset(1801, 3 * 1801) > 0
    # reading A: bleeding (1 HP per 300 s, M-0336) against regeneration from 100 of 100 HP
    times = set()
    for phi in range(1, 1801):
        for order in ("dh", "hd"):
            fate, t, _ = sustain(100, 100, 1, 300, 1, 1800, phi, order)
            assert fate == "dies" and 30_000 <= t <= 102 * 360
            times.add(t)
    assert (min(times), max(times)) == (35_700, 36_000)
    assert sustain(100, 100, 1, 300, 0, 1800, 1)[1] == 30_000  # bleeding alone: 100 ticks
    # reading B with ticks that do not restart the timer: only the Deep Cut hit at 0 does, so phase 1800
    assert {sustain(100, 100, 1, 300, 1, 1800, 1800, o)[1] for o in ("dh", "hd")} == {35_700}
