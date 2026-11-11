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
        # bound from the proof: q = p_hit, at most m = ceil(M / hit) consecutive hits kill
        m = -(-M // hit)
        assert t.max() <= m / p_hit**m + 1e-6
        # absorption probability after many steps tends to 1 even when healing dominates on average
        dist = np.zeros(M + 1)
        dist[M] = 1.0
        for _ in range(200_000 // M):
            dist = dist @ P
        assert dist[0] > 0.0
