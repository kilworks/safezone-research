"""Prover test for T-0007 (theory/01-hit-pipeline.md): fortress then armor as absorbing layers.

Steps 6 and 7 of the hit pipeline (M-0124, M-0125) applied hit by hit are compared
with the closed form, for every sequence drawn by hypothesis and exhaustively for
short sequences. Checks our model of the rule, not the game.
"""
import itertools

from hypothesis import given, strategies as st


def layered(hits, f, a, overflow_passes=True):
    """Apply fortress (durability f) then armor (durability a) to each hit in order; return HP lost."""
    lost = 0
    for x in hits:
        took = min(x, f)
        f -= took
        x -= took
        took = min(x, a)
        breaks = a > 0 and took == a
        a -= took
        x -= took
        if breaks and not overflow_passes:
            x = 0  # U-0101 reading B: the excess of the hit that breaks the armor is lost
        lost += x
    return lost


def closed_form_a(hits, f, a):
    """U-0101 reading A: HP lost after the sequence = max(S - f - a, 0), S = total damage."""
    return max(sum(hits) - f - a, 0)


@given(st.lists(st.integers(1, 60), max_size=30), st.integers(0, 30), st.integers(0, 45))
def test_t0007_reading_a_closed_form(hits, f, a):
    assert layered(hits, f, a) == closed_form_a(hits, f, a)


def test_t0007_reading_a_exhaustive_short_sequences():
    for n in range(4):
        for hits in itertools.product(range(1, 13), repeat=n):
            for f in (0, 5, 30):
                for a in (0, 7, 15):
                    assert layered(hits, f, a) == closed_form_a(hits, f, a)


@given(st.lists(st.integers(1, 60), max_size=30), st.integers(0, 30), st.integers(1, 45))
def test_t0007_reading_b_saves_at_most_one_hit(hits, f, a):
    # Reading B differs from A by the overflow of the single hit that breaks the armor.
    lost_a, lost_b = layered(hits, f, a), layered(hits, f, a, overflow_passes=False)
    assert 0 <= lost_a - lost_b <= max(hits, default=0)
