"""Prover test for T-0007 (theory/01-hit-pipeline.md): fortress then armor as absorbing layers.

Steps 6 and 7 of the hit pipeline (M-0124, M-0125) applied hit by hit are compared
with the closed form, for every sequence drawn by hypothesis and exhaustively for
short sequences. Checks our model of the rule, not the game.
"""
import itertools

from hypothesis import given, strategies as st


def layered(hits, f, a, overflow_passes=True, trace=None):
    """Apply fortress (durability f) then armor (durability a) to each hit in order; return HP lost.

    trace, if a list, receives (lost, f, a, overflow lost to reading B) after each hit.
    """
    lost = 0
    for x in hits:
        wasted = 0
        took = min(x, f)
        f -= took
        x -= took
        took = min(x, a)
        breaks = a > 0 and took == a
        a -= took
        x -= took
        if breaks and not overflow_passes:
            wasted, x = x, 0  # U-0101 reading B: the excess of the hit that breaks the armor is lost
        lost += x
        if trace is not None:
            trace.append((lost, f, a, wasted))
    return lost


def closed_form_a(hits, f, a):
    """U-0101 reading A: HP lost after the sequence = max(S - f - a, 0), S = total damage."""
    return max(sum(hits) - f - a, 0)


@given(st.lists(st.integers(1, 60), max_size=30), st.integers(0, 30), st.integers(0, 45))
def test_t0007_reading_a_closed_form(hits, f, a):
    assert layered(hits, f, a) == closed_form_a(hits, f, a)


def check_prefixes(hits, f, a):
    """Every prefix: HP lost, fortress left and armor left match the three closed forms of T-0007."""
    trace = []
    layered(hits, f, a, trace=trace)
    s_j = 0
    for x, (lost, f_left, a_left, _) in zip(hits, trace):
        s_j += x
        assert lost == max(s_j - f - a, 0)
        assert f_left == f - min(s_j, f)
        assert a_left == a - min(max(s_j - f, 0), a)


@given(st.lists(st.integers(1, 60), max_size=30), st.integers(0, 30), st.integers(0, 45))
def test_t0007_reading_a_layers_left(hits, f, a):
    check_prefixes(hits, f, a)


def test_t0007_reading_a_exhaustive_short_sequences():
    # Every fortress 0..30 (M-0529) and armor 0..45 (enchanted, M-0339) for up to 2 hits of 1..12 HP,
    # and boundary durabilities for 3 hits.
    for n in range(3):
        for hits in itertools.product(range(1, 13), repeat=n):
            for f in range(31):
                for a in range(46):
                    check_prefixes(hits, f, a)
    for hits in itertools.product(range(1, 13), repeat=3):
        for f in (0, 1, 5, 29, 30):
            for a in (0, 1, 7, 14, 15, 44, 45):
                check_prefixes(hits, f, a)


@given(st.lists(st.integers(1, 60), max_size=30), st.integers(0, 30), st.integers(1, 45))
def test_t0007_reading_b_saves_exactly_the_breaking_overflow(hits, f, a):
    # Reading B differs from A by exactly the overflow of the single hit that breaks the armor (0 if it never breaks).
    trace = []
    lost_b = layered(hits, f, a, overflow_passes=False, trace=trace)
    wasted = [w for *_, w in trace if w]
    assert len(wasted) <= 1
    assert layered(hits, f, a) - lost_b == sum(wasted)
