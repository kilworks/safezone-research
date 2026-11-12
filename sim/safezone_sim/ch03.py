"""Model of healing and sustain for theory/03-healing-and-sustain.md (T-0300..T-0306).

Every function is one reading of a rule, named after its kb/ record. Integer HP and seconds,
exact fractions where a rule is fractional. This models the rules, not the game.
"""
from fractions import Fraction
from math import lcm

TIERS = {"small": 5, "medium": 10, "large": 20, "gigantic": 40}  # M-0207
CONVERT = {"small": 1, "medium": 2, "large": 3, "gigantic": 4}  # M-0502

# Reachable max HP: base 90 (Greed, M-0508), 100, 110 (Piety, M-0500), +10 per upgrade,
# cap 200 or 220 for Piety (M-0333), assuming no other max-HP modifier exists.
REACHABLE_M = {"greed": range(90, 201, 10), "piety": range(110, 221, 10), "other": range(100, 201, 10)}
ALL_M = sorted(set().union(*REACHABLE_M.values()))


def piety(x):
    """Piety potion bonus, +15% rounded down (M-0505, one reading by T-0005)."""
    return x * 115 // 100


def protection(x, reading="A"):
    """Protection potion cut, 50% less (M-0645, U-0618): A floor, B ceil, C exact fraction."""
    return {"A": x // 2, "B": -(-x // 2), "C": Fraction(x, 2)}[reading]


def pct(M, num, reading):
    """num% of M (U-0204, U-0600, U-0603): A floor, B ceil, C round half up, D exact fraction."""
    q = Fraction(M * num, 100)
    return {"A": q.numerator // q.denominator, "B": -(-q.numerator // q.denominator),
            "C": (2 * q.numerator + q.denominator) // (2 * q.denominator), "D": q}[reading]


def restored(x, m):
    """HP a heal of x restores at missing HP m when HP caps at max (U-0203 reading A)."""
    return min(x, m)


def drink_tokens(tier, m, basis, carry=0):
    """Piety blood tokens from drinking one potion at missing HP m (M-0501).

    basis is the U-0501 reading: A effective HP after the bonus, B nominal after the bonus,
    C nominal before the bonus, D effective HP without the bonus part. carry is the remainder
    held by a cumulative counter (U-0500 A, 0..4); carry 0 is also U-0500 B (per event floor).
    """
    x = TIERS[tier]
    q = {"A": min(m, piety(x)), "B": piety(x), "C": x, "D": min(m, x)}[basis]
    return (carry + q) // 5 - carry // 5


# Bandage ticks (M-0233, U-0214): HP per tick, spacing s, first tick, number of ticks. D is continuous.
BANDAGE = {"A": (1, 12, 12, 10), "B": (1, 12, 0, 10), "C": (2, 24, 24, 5)}

# Which heals Protection's "Potions heal you 50% less" (M-0645) cuts, per U-0617 reading.
PROTECTION_SCOPE = {"A": {"potion"}, "B": {"potion", "eddie"},
                    "C": {"potion", "eddie", "bandage", "circle", "fruit"}}


def bandage_schedule(reading, protection_reading=None, round_up=False):
    """Bandage ticks as a list of (time s, HP) under U-0214, for a Protection contestant under U-0619.

    U-0619 A: same ticks, spacing times 1.1 (10 HP over 132 s). B: same spacing, the ticks that fit in
    132 s (whole ticks only). C: 132 s rounded to the tick grid, down, or up with round_up.
    U-0214 D: continuous 1/12 HP per second, on a 0.2 s grid so every whole-HP time is exact.
    """
    if reading == "D":
        dur = 120 if protection_reading is None else 132
        total = 11 if protection_reading in ("B", "C") else 10  # no grid: C is B
        n = dur * 5
        return [(Fraction(k, 5), Fraction(total, n)) for k in range(1, n + 1)]
    hp, s, first, n = BANDAGE[reading]
    if protection_reading == "A":
        s, first = Fraction(11 * s, 10), Fraction(11 * first, 10)
    elif protection_reading in ("B", "C"):
        q = Fraction(132, s)
        n = -(-q.numerator // q.denominator) if protection_reading == "C" and round_up else q.numerator // q.denominator
    return [(first + s * k, hp) for k in range(n)]


def bandage_time_to_full(schedule, m):
    """Seconds after use until m missing HP are restored (per-tick cap, no damage); None if never."""
    got = 0
    for t, hp in schedule:
        got += hp
        if got >= m:
            return t
    return None


def bandage_waste(schedule, m):
    """HP the bandage pays above the missing HP m, tick by tick, with HP capped at max (U-0203 A)."""
    room, waste = m, 0
    for _, hp in schedule:
        g = min(hp, room)
        room, waste = room - g, waste + hp - g
    return waste


def campfire_static(pool, deficits, reading, tiebreak=0, limit=600):
    """Total HP restored by a Campfire (M-0525, U-0520) to people standing in range, no damage.

    A: each person with missing HP draws 1 HP/s from the pool. B1: the pool pays 1 HP/s in total to
    those missing HP (one person per second, in turn). B2: the pool pays 1 HP/s in total, split equally
    among everyone in range, full HP or not (exact fractions; a share above the deficit is wasted).
    C: everyone in range draws 1 HP/s, full HP or not (a full draw is wasted).
    tiebreak rotates who is served first when the pool cannot serve everyone in a second.
    Returns (HP restored, seconds until the pool is empty or nobody draws, pool left).
    """
    d = list(deficits)
    n, total, t = len(d), 0, 0
    if reading == "B2":
        d = [Fraction(x) for x in d]
        while t < limit and pool > 0:
            t, pool = t + 1, pool - 1
            for i in range(n):
                g = min(Fraction(1, n), d[i])
                d[i], total = d[i] - g, total + g
        return total, t, pool
    while t < limit and pool > 0:
        order = [(i + tiebreak + t) % n for i in range(n)]
        if reading == "B1":
            order = [i for i in order if d[i] > 0][:1]
        elif reading == "A":
            order = [i for i in order if d[i] > 0]
        if not order:
            break
        t += 1
        for i in order:
            if pool == 0:
                break
            pool -= 1
            if d[i] > 0:
                d[i] -= 1
                total += 1
    return total, t, pool


def campfire_standby(pool, M, a, b, reading, first=None, hits=None, limit=600):
    """A lone contestant at full HP by a Campfire lit at second 0, hit for a HP at first, first + b, ...

    first defaults to b; hits caps the number of hits (a drain cap such as 30 HP, M-0449), None for no cap.
    Each second: damage first, then the campfire heals 1 HP (seconds 1 to limit, inclusive) if the reading
    lets it draw: A and B1 only when HP is below max, B2 and C every second (one person: the share is 1 HP).
    Returns (last second the pool paid out, minimum HP seen, pool left).
    """
    first = b if first is None else first
    hp, low, last, n = M, M, 0, 0
    for t in range(0, limit + 1):
        if pool == 0:
            break
        if t >= first and (t - first) % b == 0 and (hits is None or n < hits):
            hp, n = hp - a, n + 1
            low = min(low, hp)
        if t >= 1 and (reading in ("A", "B1") and hp < M or reading in ("B2", "C")):
            pool -= 1
            last = t
            hp = min(M, hp + 1)
    return last, low, pool


def sustain(h, M, a, b, c, e, phi, order="dh", more=()):
    """Deterministic capped HP: a HP lost at b, 2b, ...; c HP healed (capped at M) at phi, phi+e, ...

    more: extra heal sources (c, e, phi), each periodic the same way. order "dh": in a shared second
    damage lands first (death checked before the heals); "hd": the heals land first. Capping heals one
    by one equals capping their sum, since HP <= M. Event-driven, with cycle detection on
    (HP, t mod lcm of all periods) once every source has started: a repeated state proves the
    trajectory periodic, so the contestant survives forever.
    Returns ("dies", t, min HP) or ("lives", None, min HP over the whole future).
    """
    heals = [(c, e, phi), *more]
    L = lcm(b, *(x[1] for x in heals))
    start = max(x[2] for x in heals)
    nd, nh, hp, low, seen = b, [x[2] for x in heals], h, h, set()
    while True:
        t = min(nd, *nh)
        hit = nd == t
        if hit:
            nd += b
        gain = 0
        for j, (cj, ej, _) in enumerate(heals):
            if nh[j] == t:
                gain, nh[j] = gain + cj, nh[j] + ej
        if order == "hd":
            hp = min(M, hp + gain)
        if hit:
            hp -= a
            low = min(low, hp)
            if hp <= 0:
                return "dies", t, hp
        if order == "dh":
            hp = min(M, hp + gain)
        if t >= start:
            key = (hp, t % L)
            if key in seen:
                return "lives", None, low
            seen.add(key)


def regen_with_reset(damage_every, horizon, period=1800):
    """Healing regeneration under U-0007 reading B: each damage restarts the 1800 s timer.

    Damage lands every damage_every seconds (first at damage_every); in a shared second the
    damage comes first. Counts regeneration ticks (HP below max assumed) over [1, horizon].
    """
    since, ticks = 0, 0
    for t in range(1, horizon + 1):
        since += 1
        if t % damage_every == 0:
            since = 0
        if since == period:
            ticks, since = ticks + 1, 0
    return ticks
