"""Closed forms of theory/07-zombies-and-pursuit.md (T-0700..T-0707), exact rational arithmetic.

Every function is a formula from the chapter; sim/tests/test_07_zombies.py checks each one against
an independent simulation. These check our model of the rules, never the game.
"""
from fractions import Fraction as F
from math import ceil, floor

U = F(14, 10)  # zombie speed, m/s (M-0440)
REGULAR = dict(rho=F(5), period=F(10), dmg=1, cap=30, u=U)  # M-0441, M-0442
GUARD = dict(rho=F(10), period=F(5), dmg=2, cap=30)  # M-0449; speed 0 or U per U-0429


ESCORT_MAX_SPEED = U  # T-0706: an escort keeps up with a target no faster than this
MINE_RADIUS = 10  # M-0307


def distance_line(r0, v, u, t):
    """T-0700 (b), (d): r0 + (v - u) t, the upper bound under pursuit and the lower bound
    under straight flight."""
    return r0 + (v - u) * t


def cone_half_angle(w, u=1.4):
    """T-0700 (c): half-angle (radians) of the headings that do not lose ground at speed w >= u."""
    from math import acos
    return acos(u / w)


def escort_join_time(r, v, u=U):
    """T-0706 (b): a death zombie r metres from its owner (owner speed at most v < u) joins it by then."""
    return r / (u - v)


def mine_safe_distance(rho=5):
    """T-0707 (b): beyond this distance from the mine (5 sqrt 5 = 11.18 m), a zombie walking
    straight at the contestant dies before it is within rho. A walk toward E enters the mine
    disk heading inward, so it triggers at least sqrt(x^2 - R^2) from E (tangent walk)."""
    from math import sqrt
    return sqrt(MINE_RADIUS ** 2 + rho ** 2)


def mine_drain_window(x, rho=5, u=U):
    """T-0707 (d): longest time within drain range before the trigger, for 10 < x <= 5 sqrt 5."""
    from math import sqrt
    return (rho - sqrt(x * x - MINE_RADIUS ** 2)) / float(u)


def contact_ticks(L, phi, period, closed=True):
    """Drain ticks landing in a contact interval [0, L] (closed range) or [0, L) (open range).

    Ticks fall at phi, phi + period, ... (U-0425): phi = 0 is reading B0 (first drain at contact),
    phi = period is reading B1 (first drain one period after contact), phi in [0, period) is
    reading A (the zombie's own clock, phase unknown).
    """
    if closed:
        return floor((L - phi) / period) + 1 if phi <= L else 0
    return ceil((L - phi) / period) if phi < L else 0


def escape_time(v, r0, rho, u):
    """T-0701: time in range when fleeing at v > u from distance r0 <= rho (the game's value)."""
    assert v > u and 0 <= r0 <= rho
    return (rho - r0) / (v - u)


def escape_drain(v, r0, phi, z=REGULAR, u=None, closed=True):
    """T-0702: HP drained while escaping, before armor, Kick reduction and blockers."""
    u = z.get("u", U) if u is None else u
    n = contact_ticks(escape_time(v, r0, z["rho"], u), phi, z["period"], closed)
    return z["dmg"] * min(n, z["cap"] // z["dmg"])


def zero_drain_speed(r0, z=REGULAR, u=None):
    """T-0702: under B1 and closed range the escape costs 0 HP iff v > this speed."""
    u = z.get("u", U) if u is None else u
    return u + (z["rho"] - r0) / z["period"]


def min_zombies_to_kill(h, cap=30):
    """T-0703 (a): under U-0008 reading A, n zombies alone can kill from h HP only if n >= this."""
    return -(-h // cap)


def death_time_window(h, n, period=10, dmg=1):
    """T-0703 (b): death time of a contestant with h HP held in range of n zombies from t = 0.

    Returns (B0 time, B1 time); reading A (any phases) lies in between. None if the cap forbids.
    """
    if h > 30 * n:
        return None
    k = -(-h // (n * dmg))  # ticks needed per zombie
    return period * (k - 1), period * k


def reach_radius(rho, u, v, lifetime):
    """T-0701 (d): largest start distance from which a pure-pursuit zombie reaches range rho
    within its lifetime against a contestant moving at speed v < u who flees optimally."""
    return rho + (u - v) * lifetime


def separation_gain_per_window(vmax, u=U, window=60):
    """T-0704 (b): most a contestant can gain on a pure-pursuit zombie in one speed window."""
    return window * (vmax - u)


def guard_in_range(px, py, closed=True):
    """T-0705: is the point (px, py) within 10 m of a guard at (10, 0), gravestone at the origin.

    Uses the polar form s <= 20 cos(beta), that is px^2 + py^2 <= 20 px."""
    lhs, rhs = px * px + py * py, 20 * px
    return lhs <= rhs if closed else lhs < rhs
