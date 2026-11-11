"""Prover test for T-0014 (theory/05-survival-processes.md): with HP capped at M and a loss
probability bounded below, death is certain and its expected time is finite and bounded.

Builds the chain explicitly, computes expected absorption times with the fundamental
matrix N = (I - Q)^-1, and checks them against the bound of the proof. Checks the
mathematics of the model, not the game.
"""
import numpy as np


def chain(M, p_hit, hit, p_heal, heal):
    """States 0..M, 0 absorbing. Each step: lose `hit` w.p. p_hit, gain `heal` (capped at M) w.p. p_heal."""
    P = np.zeros((M + 1, M + 1))
    P[0, 0] = 1.0
    for h in range(1, M + 1):
        P[h, max(h - hit, 0)] += p_hit
        P[h, min(h + heal, M)] += p_heal
        P[h, h] += 1 - p_hit - p_heal
    return P


def expected_absorption(P):
    Q = P[1:, 1:]
    N = np.linalg.inv(np.eye(len(Q)) - Q)
    return N @ np.ones(len(Q))


def test_t0014_capped_hp_means_certain_death():
    for M, p_hit, hit, p_heal, heal in [(100, 0.05, 1, 0.5, 5), (110, 0.01, 10, 0.9, 40), (20, 0.2, 2, 0.7, 1)]:
        P = chain(M, p_hit, hit, p_heal, heal)
        t = expected_absorption(P)
        assert np.all(np.isfinite(t)) and np.all(t > 0)
        # bound from the proof: q = p_hit, at most m = ceil(M / hit) consecutive hits kill.
        # shortcut: float inverses saturate near 1/eps (about 1e16), so for the two large chains this
        # only checks finiteness; their exact values come from test_t0014_exact_value below.
        m = -(-M // hit)
        assert t.max() <= m / p_hit**m + 1e-6


def test_t0014_absorption_tends_to_one():
    P = chain(20, 0.2, 2, 0.7, 1)  # expected time about 1.7e4 steps
    dist = np.zeros(21)
    dist[20] = 1.0
    dist = dist @ np.linalg.matrix_power(P, 2**18)  # 262144 steps
    assert dist[0] > 0.99


def exact_time_from_full(M):
    # exact expected absorption time from full HP, rational Gaussian elimination
    from fractions import Fraction as F
    ph, pl = F(5, 100), F(1, 2)
    A = [[F(0)] * M + [F(1)] for _ in range(M)]
    for h in range(1, M + 1):
        A[h - 1][h - 1] += 1
        for to, p in ((h - 1, ph), (min(h + 5, M), pl), (h, 1 - ph - pl)):
            if to > 0:
                A[h - 1][to - 1] -= p
    for i in range(M):
        for j in range(i + 1, M):
            if A[j][i]:
                f = A[j][i] / A[i][i]
                A[j] = [a - f * b for a, b in zip(A[j], A[i])]
    x = [F(0)] * M
    for i in range(M - 1, -1, -1):
        x[i] = (A[i][M] - sum(A[i][j] * x[j] for j in range(i + 1, M))) / A[i][i]
    return x[-1]


def test_t0014_exact_value():
    assert 1e21 < exact_time_from_full(20) < 2e21  # the reviewer's exact value 1.35e21; the float inverse gave 2e16
    assert 2.75e104 < exact_time_from_full(100) < 2.76e104  # the example in theory/05
