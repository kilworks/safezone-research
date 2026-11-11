"""Prover tests for the arithmetic theorems of theory/02-rounding-and-arithmetic.md.

Each test is an exhaustive check over a domain that the theorem's proof shows to be
sufficient (a full period, or the whole finite game domain). A passing test checks
our model of the rule, not the game itself.
"""
import math

from safezone_sim.arith import halve, kick_attack, kick_defense, ladder_price, ladder_total, pct_ceil, pct_floor

D_MAX = 10_000  # far above any damage, HP or price the KB allows


def test_t0001_kick_attack_single_reading():
    for d in range(D_MAX + 1):
        assert kick_attack(d) == d + d // 10  # rounding the total = rounding the bonus
    assert all(kick_attack(d) == d for d in range(10))  # corollary: no bonus below 10


def test_t0002_kick_defense_two_readings():
    for d in range(D_MAX + 1):
        a, b = kick_defense(d, "A"), kick_defense(d, "B")
        assert a == d - math.ceil(d / 10) == d - (-(-d // 10))
        assert b - a == (d % 10 != 0)
    assert [kick_defense(d, "A") for d in range(1, 11)] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert [kick_defense(d, "B") for d in range(1, 10)] == list(range(1, 10))


def test_t0003_protection_nuke_and_kick_order():
    # Both orders satisfy g(d + 20) = g(d) + 9, so their difference is 20-periodic:
    # checking one period proves the statement for every d >= 0. We check far beyond.
    for reading, residues, sign in (("A", {3, 5, 7, 9}, -1), ("B", {10, 12, 14, 16, 18}, 1)):
        for d in range(D_MAX + 1):
            documented = kick_defense(halve(d), reading)  # wiki order: halve, round, then Kick
            swapped = halve(kick_defense(d, reading))
            assert kick_defense(halve(d + 20), reading) == documented + 9
            assert documented - swapped == (sign if d % 20 in residues else 0)
        assert kick_defense(halve(20), reading) == halve(kick_defense(20, reading)) == 9  # viewer nuke


def test_t0004_minimum_step_changes_outcome_only_for_tiny_hits():
    def raised(reduce):
        return [d for d in range(1, D_MAX + 1) if reduce(d) == 0]

    assert raised(lambda d: kick_defense(d, "A")) == [1]
    assert raised(lambda d: kick_defense(d, "B")) == []
    assert raised(halve) == [1]
    assert raised(lambda d: kick_defense(halve(d), "A")) == [1, 2, 3]
    assert raised(lambda d: kick_defense(halve(d), "B")) == [1]


def test_t0005_piety_bonus_readings_coincide():
    for x in range(D_MAX + 1):
        assert pct_floor(x, 115) == x + pct_floor(x, 15)
    assert [pct_floor(x, 115) for x in (5, 10, 20, 40)] == [5, 11, 23, 46]


def test_t0006_merchant_ladder():
    for n in range(0, 101):
        assert ladder_total(n) == sum(ladder_price(k) for k in range(n))
    assert ladder_total(10) == 850
    assert sum(pct_ceil(ladder_price(k), 110) for k in range(10)) == 935  # Ingenuity, exact arithmetic
    assert sum(math.ceil(ladder_price(k) * 1.1) for k in range(10)) == 939  # H-0001, binary64 code
