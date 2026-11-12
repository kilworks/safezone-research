"""Exact models for theory/04-probabilistic-items.md (T-0400..T-0408).

Everything is rational (fractions.Fraction); no floating point. Each function names
the kb/ mechanic it models. A test on these functions checks the model, not the game.
"""
from fractions import Fraction as F

P_HEAL = F(1, 10)  # M-0208 "10% chance to heal"


def rnd(x: F, how: str) -> int:
    """Round a non-negative rational: 'floor', 'ceil' or 'half_up' (U-0204 readings A, B, C)."""
    q, r = divmod(x.numerator, x.denominator)
    if r == 0 or how == "floor":
        return q
    if how == "ceil":
        return q + 1
    return q + (1 if 2 * r >= x.denominator else 0)  # half_up


ROUNDINGS = ("floor", "ceil", "half_up")


def eddie_amounts(M: int, heal_rnd: str = "floor", loss_rnd: str = "floor") -> tuple[int, int]:
    """(g, l): heal 50% and loss 30% of max HP M, each rounded its own way (M-0208, U-0204)."""
    return rnd(F(M, 2), heal_rnd), rnd(F(3 * M, 10), loss_rnd)


def sigil_bases() -> dict[str, int]:
    """Base max HP per sigil (M-0500 Piety 110, M-0508 Greed 90, every other sigil 100)."""
    return {"piety": 110, "greed": 90, "other": 100}


def reachable_max_hp(purchase_limit: int | None = None) -> set[int]:
    """Max HP values reachable by base plus +10 upgrades, capped at 200 (220 Piety) (M-0333, U-0330).

    purchase_limit None: only the cap binds (U-0330 reading A); an integer: at most that many purchases (reading B).
    """
    out = set()
    for sigil, base in sigil_bases().items():
        cap = 220 if sigil == "piety" else 200
        k = 0
        while base + 10 * k <= cap and (purchase_limit is None or k <= purchase_limit):
            out.add(base + 10 * k)
            k += 1
    return out


def eddie_outcomes(M, h, g, l, kill="A", cap=True, blocked=False, armor=0, kick=None, min1=False):
    """List of (probability, new HP) for one drink at HP h (1 <= h <= M).

    kill: 'A' the loss can kill (U-0004 A/B); 'C' the loss cannot take HP below 1 (U-0004 C).
    cap: heal capped at M (U-0203 A) or not (B).
    blocked: an active Shield, Safety bubble or Sleeping Bag stops the backfire (M-0165, U-0004 B).
    armor: remaining Body armor durability absorbing the loss (M-0165, M-0125, U-0101 A, U-0209 A).
    kick: None, or 'A'/'B' for the defender Kick reduction applied to the loss (U-0001, U-0004 B).
    min1: an unblocked loss removes at least 1 HP after armor (M-0123 reading B, U-0103 reading B).
    g may be a Fraction (U-0618 reading C).
    """
    up = min(M, h + g) if cap else h + g
    loss = 0 if blocked else l
    if kick == "A":
        loss = 9 * loss // 10
    elif kick == "B":
        loss = loss - loss // 10
    loss = max(loss - armor, 0)
    if min1 and not blocked:
        loss = max(loss, 1)
    floor = 1 if kill == "C" else 0
    down = max(h - loss, floor) if loss else h
    return [(P_HEAL, up), (1 - P_HEAL, down)]


def moments(outcomes, h):
    """Exact mean and variance of the HP change."""
    mean = sum(p * (x - h) for p, x in outcomes)
    var = sum(p * (x - h - mean) ** 2 for p, x in outcomes)
    return mean, var


def survival(M, T, moves):
    """S[x] = probability of being alive (HP >= 1) after T steps from HP x, x = 0..M.

    moves: list of (probability, delta) summing to 1; HP is clipped to [0, M] and 0 is absorbing
    (the T-0014 chain of theory/05).
    """
    S = [F(0)] + [F(1)] * M
    for _ in range(T):
        S = [F(0)] + [sum(p * S[min(max(x + d, 0), M)] for p, d in moves) for x in range(1, M + 1)]
    return S


def drink_value(S, outcomes):
    """Survival probability if the potion is drunk now and never again."""
    return sum(p * S[x] for p, x in outcomes)


def optimal_hold(M, T, moves, g, l, kill="A"):
    """Holding one potion with T steps left: V[t][x] optimal survival, and the set of (t, x) where drinking is optimal.

    At each step the holder may drink (instantly, before the step's move) or wait. Backward induction.
    """
    S = [F(0)] + [F(1)] * M  # no potion, 0 steps left
    V = S[:]                 # potion held, 0 steps left: drinking cannot raise alive-ness at the horizon
    drink_set = set()
    for t in range(1, T + 1):
        S_new = [F(0)] + [sum(p * S[min(max(x + d, 0), M)] for p, d in moves) for x in range(1, M + 1)]
        V_new = [F(0)]
        for x in range(1, M + 1):
            wait = sum(p * V[min(max(x + d, 0), M)] for p, d in moves)
            drink = drink_value(S_new, eddie_outcomes(M, x, g, l, kill=kill))
            if drink > wait:
                drink_set.add((t, x))
            V_new.append(max(wait, drink))
        S, V = S_new, V_new
    return V, S, drink_set


def p_at_least_one(p: F, n: int) -> F:
    """P(at least one success in n independent trials of probability p)."""
    return 1 - (1 - p) ** n


def geometric_moments(p: F) -> tuple[F, F]:
    """Mean and variance of the number of trials until the first success: 1/p, (1-p)/p^2."""
    return 1 / p, (1 - p) / p ** 2


def binom_pmf(n: int, p: F) -> list[F]:
    from math import comb
    return [comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]


def expected_min(k: int, n: int, p: F) -> F:
    """E[min(k, Binomial(n, p))]: items lost when each of n rolls removes one of k items with probability p."""
    return sum(q * min(k, j) for j, q in enumerate(binom_pmf(n, p)))
