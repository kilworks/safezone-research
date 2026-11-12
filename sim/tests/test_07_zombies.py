"""Prover tests for theory/07-zombies-and-pursuit.md (T-0700..T-0707).

Each closed form of sim/safezone_sim/ch07.py is checked against an independent computation:
a tick-by-tick count in exact fractions, a discretized pursuit, or a direct distance. The
discrete pursuit used here (contestant moves, then the zombie steps u*dt toward the new position,
never overshooting) satisfies the continuous bounds exactly, so tolerances are float noise only.
These tests check our model of the rules, never the game.
"""
import heapq
import math
import random
from fractions import Fraction as F

from safezone_sim.ch07 import (
    ESCORT_MAX_SPEED, GUARD, REGULAR, U, cone_half_angle, contact_ticks, death_time_window,
    distance_line, escape_drain, escape_time, escort_join_time, guard_in_range, mine_drain_window,
    mine_safe_distance, min_zombies_to_kill, reach_radius, separation_gain_per_window, zero_drain_speed,
)

u = 1.4
TOL = 1e-9


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def step_toward(z, target, speed, dt):
    d = dist(z, target)
    if d <= speed * dt:
        return target
    k = speed * dt / d
    return (z[0] + (target[0] - z[0]) * k, z[1] + (target[1] - z[1]) * k)


def move(p, heading, speed, dt):
    return (p[0] + speed * dt * math.cos(heading), p[1] + speed * dt * math.sin(heading))


# ---------- T-0700 ----------

def test_t0700_distance_rate():
    rng = random.Random(700)
    dt = 0.05
    for trial in range(300):
        v = rng.choice([0.0, 0.7, 1.4, 2.0, 3.0, rng.uniform(0, 4)])
        r0 = rng.uniform(0.5, 10)
        straight = trial % 3 == 0  # straight flight reaches the bound with equality
        z, e = (0.0, 0.0), (r0, 0.0)
        heading = 0.0
        for k in range(1, 401):
            if not straight and k % 20 == 1:
                heading = rng.uniform(0, 2 * math.pi)
            e = move(e, heading, v if straight else rng.uniform(0, v), dt)
            z = step_toward(z, e, u, dt)
            # (b) pursuit: d <= r0 + (v - u) t, clipped at 0
            assert dist(z, e) <= max(distance_line(r0, v, u, k * dt), 0) + TOL
            if straight:
                g = distance_line(r0, v, u, k * dt)
                assert g <= 0 or abs(dist(z, e) - g) < 1e-6
    for trial in range(300):
        v = rng.choice([1.4, 2.0, 3.0, rng.uniform(1.4, 4)])
        r0 = rng.uniform(0.5, 10)
        chase = trial % 3 == 0  # a zombie running straight after the contestant reaches equality
        z, e1, e2 = (0.0, 0.0), (r0, 0.0), (r0, 0.0)
        z2 = (0.0, 0.0)
        zh = 0.0
        for k in range(1, 401):
            # (d) straight flight away from Z(0), zombie on any path of speed <= u
            e1 = move(e1, 0.0, v, dt)
            if chase:
                z = move(z, 0.0, u, dt)
            else:
                if k % 10 == 1:
                    zh = rng.uniform(0, 2 * math.pi)
                z = move(z, zh, rng.uniform(0, u), dt)
            assert dist(z, e1) >= distance_line(r0, v, u, k * dt) - TOL
            if chase:
                assert abs(dist(z, e1) - distance_line(r0, v, u, k * dt)) < 1e-6
            # (e) feedback flight: directly away from the zombie's current position, d never decreases
            before = dist(z2, e2)
            away = math.atan2(e2[1] - z2[1], e2[0] - z2[0])
            e2 = move(e2, away, v, dt)
            z2 = move(z2, rng.uniform(0, 2 * math.pi), rng.uniform(0, u), dt)
            assert dist(z2, e2) >= before + (v - u) * dt - TOL
    # (c) escape cone, by a finite difference of continuous pursuit
    h = 1e-6
    for w in (1.5, 2.0, 3.0, 8.94):
        half = cone_half_angle(w, u)
        for deg in range(0, 181):
            th = math.radians(deg)
            e = move((10.0, 0.0), th, w, h)
            z = step_toward((0.0, 0.0), (10.0, 0.0), u, h)
            rate = (dist(z, e) - 10.0) / h
            assert abs(rate - (w * math.cos(th) - u)) < 1e-4
            if th < half - 1e-3:
                assert rate > 0
            if th > half + 1e-3:
                assert rate < 0
    # (f) a faster contestant still loses ground when running across or toward the zombie
    for th, expected in ((math.pi / 2, -u), (math.pi, -(u + 3.0))):
        e = move((10.0, 0.0), th, 3.0, h)
        z = step_toward((0.0, 0.0), (10.0, 0.0), u, h)
        assert abs((dist(z, e) - 10.0) / h - expected) < 1e-4


# ---------- T-0701 ----------

def test_t0701_escape_value():
    rng = random.Random(701)
    # (a) exact pursuit on one line in fractions: within rho on [0, tau], below rho on [0, tau) only
    step = F(1, 20)
    for v in [U + F(k, 10) for k in range(1, 21)]:
        for r0 in [F(m, 4) for m in range(21)]:
            tau = escape_time(v, r0, F(5), U)
            xe, xz = r0, F(0)
            for k in range(int(tau / step) + 40):
                d, t = xe - xz, k * step
                assert (d <= 5) == (t <= tau)  # closed range: in range on [0, tau]
                assert (d < 5) == (t < tau)  # open range: in range on [0, tau), empty if r0 = 5
                xe += v * step
                xz += min(U * step, xe - xz)
    dt = 0.01
    for trial in range(120):
        v = rng.uniform(1.5, 4.0)
        r0 = rng.uniform(0, 5)
        tau = float(escape_time(F(v), F(r0), F(5), U))
        # pursuit against any contestant path: in range throughout [0, tau]
        z, e, heading = (0.0, 0.0), (r0, 0.0), 0.0
        straight = trial % 2 == 0
        k = 0
        while (k + 1) * dt <= tau:
            k += 1
            if not straight and k % 50 == 1:
                heading = rng.uniform(0, 2 * math.pi)
            e = move(e, heading, v, dt)
            z = step_toward(z, e, u, dt)
            assert dist(z, e) <= 5 + TOL
        if straight:  # and straight flight leaves right after tau: the bound is the value
            e = move(e, 0.0, v, 2 * dt)
            z = step_toward(z, e, u, 2 * dt)
            assert dist(z, e) > 5
        # straight flight against any zombie path: out of range after tau
        z, e, zh = (0.0, 0.0), (r0, 0.0), 0.0
        for k in range(1, int(tau / dt) + 300):
            e = move(e, 0.0, v, dt)
            if k % 10 == 1:
                zh = rng.uniform(-0.3, 0.3)  # zombie wanders roughly after the contestant
            z = move(z, zh, u, dt)
            if k * dt > tau + 1e-6:
                assert dist(z, e) > 5
    # (b), (c): slower contestants, pursuit closes in by (r0 - rho)/(u - v)
    for trial in range(80):
        v = rng.uniform(0, 1.3)
        r0 = rng.uniform(5.5, 30)
        bound = (r0 - 5) / (u - v)
        z, e, heading = (0.0, 0.0), (r0, 0.0), 0.0
        reached, t = None, 0.0
        for k in range(1, int(bound / dt) + 5):
            if k % 50 == 1:
                heading = rng.uniform(0, 2 * math.pi)
            e = move(e, heading, v, dt)
            z = step_toward(z, e, u, dt)
            if reached is None and dist(z, e) <= 5 + TOL:
                reached = k * dt
            if reached is not None:
                assert dist(z, e) <= 5 + TOL  # (b): once in range, never out again
        assert reached is not None and reached <= bound + dt
    # (b) v <= u and r0 <= rho: under pursuit the distance never grows, whatever the path
    for trial in range(60):
        v = u if trial % 3 == 0 else rng.uniform(0, u)
        r0 = rng.uniform(0, 5)
        z, e, heading = (0.0, 0.0), (r0, 0.0), 0.0
        for k in range(1, 2001):
            if k % 50 == 1:
                heading = rng.uniform(0, 2 * math.pi)
            e = move(e, heading, v, dt)
            z = step_toward(z, e, u, dt)
            assert dist(z, e) <= r0 + TOL
    # (c) v = u: straight flight keeps the distance at least r0 against any zombie path
    for trial in range(60):
        r0 = rng.uniform(5.5, 30)
        z, e, zh = (0.0, 0.0), (r0, 0.0), 0.0
        for k in range(1, 2001):
            e = move(e, 0.0, u, dt)
            if k % 10 == 1:
                zh = rng.uniform(-0.5, 0.5)
            z = move(z, zh, rng.uniform(0, u), dt)
            assert dist(z, e) >= r0 - TOL
    # (d) reach radius, exact: collinear pursuit against straight flight in fractions
    for v in (F(0), F(1, 2), F(1)):
        for lifetime in (60, 300, 1200):
            R = reach_radius(F(5), U, v, lifetime)
            for start, reached_by_end in ((R, True), (R + F(1, 10), False)):
                d, step = start, F(1, 10)
                for _ in range(lifetime * 10):
                    d += (v - U) * step
                assert (d <= 5) == reached_by_end
                if start == R:
                    assert d == 5  # the boundary case: exactly rho exactly at expiry, not reached if open
    assert reach_radius(5, U, 0, 1200) == 1685
    assert (reach_radius(5, U, 0, 60), reach_radius(5, U, 0, 86400)) == (89, 120965)


# ---------- T-0702 ----------

def simulate_drain(v, r0, phi, rho, period, dmg, cap, uu, closed):
    """Walk the ticks one by one: straight flight against pursuit keeps both on one line."""
    ticks, t = 0, phi
    while True:
        d = r0 + (v - uu) * t
        if not (d <= rho if closed else d < rho):
            return dmg * min(ticks, cap // dmg)
        ticks, t = ticks + 1, t + period


def count_ticks(L, phi, period):
    n, t = 0, phi
    while t <= L:
        n, t = n + 1, t + period
    return n


def test_t0702_escape_drain_exact():
    kinds = [(REGULAR, U, [F(m, 4) for m in range(21)]),
             (GUARD, F(0), [F(m, 2) for m in range(21)]),
             (GUARD, U, [F(m, 2) for m in range(21)])]
    for z, uu, r0s in kinds:
        P = z["period"]
        phases = [F(0), P, P / 3, 2 * P / 3] + [P * j / 7 for j in range(1, 7)]
        for k in range(1, 81):
            v = uu + F(k, 20)
            for r0 in r0s:
                L = escape_time(v, r0, z["rho"], uu)
                lo = z["dmg"] * min(math.floor(L / P), z["cap"] // z["dmg"])
                hi = z["dmg"] * min(math.floor(L / P) + 1, z["cap"] // z["dmg"])
                for phi in phases:
                    for closed in (True, False):
                        want = simulate_drain(v, r0, phi, z["rho"], P, z["dmg"], z["cap"], uu, closed)
                        assert escape_drain(v, r0, phi, z, u=uu, closed=closed) == want
                        if closed:
                            assert lo <= want <= hi  # (a)
                assert escape_drain(v, r0, P, z, u=uu) == lo  # B1 is the lower value
                assert escape_drain(v, r0, F(0), z, u=uu) == hi  # B0 the upper one
    # (b) uniform phase: the exact average over phi in [0, P) is L / P (before the cap)
    for P in (F(10), F(5)):
        for L in [F(n, 7) for n in range(0, 7 * 60)]:
            cuts = sorted({F(0), P} | {L - j * P for j in range(int(L / P) + 2) if 0 < L - j * P < P})
            mean = sum((b - a) * count_ticks(L, (a + b) / 2, P) for a, b in zip(cuts, cuts[1:])) / P
            assert mean == L / P
    # (c), (d) thresholds: just above, 0 HP under B1; exactly at it, one tick (closed) or none (open)
    for z, uu, r0, thr in ((REGULAR, U, F(0), F(19, 10)), (REGULAR, U, F(5, 2), F(33, 20)),
                           (REGULAR, U, F(4), F(3, 2)), (GUARD, F(0), F(0), F(2)), (GUARD, U, F(0), F(17, 5))):
        assert zero_drain_speed(r0, z, u=uu) == thr
        assert escape_drain(thr + F(1, 1000), r0, z["period"], z, u=uu) == 0
        assert escape_drain(thr, r0, z["period"], z, u=uu) == z["dmg"]
        assert escape_drain(thr, r0, z["period"], z, u=uu, closed=False) == 0
    # the worked table of the chapter
    table = [(REGULAR, U, 0, F(3, 2), 5, 6), (REGULAR, U, 0, F(8, 5), 2, 3), (REGULAR, U, 0, F(9, 5), 1, 2),
             (REGULAR, U, 0, F(19, 10), 1, 2), (REGULAR, U, 0, F(2), 0, 1), (REGULAR, U, 0, F(3), 0, 1),
             (REGULAR, U, F(5, 2), F(8, 5), 1, 2), (REGULAR, U, F(5, 2), F(2), 0, 1),
             (GUARD, F(0), 0, F(3, 2), 2, 4), (GUARD, F(0), 0, F(3), 0, 2),
             (GUARD, U, 0, F(3, 2), 30, 30), (GUARD, U, 0, F(2), 6, 8), (GUARD, U, 0, F(3), 2, 4)]
    for z, uu, r0, v, b1, b0 in table:
        assert (escape_drain(v, F(r0), z["period"], z, u=uu), escape_drain(v, F(r0), F(0), z, u=uu)) == (b1, b0)
    assert escape_drain(F(19, 10), F(0), F(10), closed=False) == 0


# ---------- T-0703 ----------

def simulate_death(h, phases, period=10, cap_ticks=30):
    """Death time of h HP under zombies ticking at their phases; None if the caps run out first."""
    events = heapq.merge(*[[phi + j * period for j in range(cap_ticks)] for phi in phases])
    total = 0
    for t in events:
        total += 1
        if total >= h:
            return t
    return None


def test_t0703_many_zombies():
    rng = random.Random(703)
    for n in range(1, 61):
        for h in range(1, 221):
            w = death_time_window(h, n)
            if h > 30 * n:  # (a) the caps cannot kill
                assert w is None and n < min_zombies_to_kill(h)
                assert simulate_death(h, [0] * n) is None
                continue
            assert w is not None and n >= min_zombies_to_kill(h)
            assert simulate_death(h, [0] * n) == w[0]  # B0
            assert simulate_death(h, [10] * n) == w[1]  # B1
            if h % 11 == 0:  # reading A, random phases
                t = simulate_death(h, [F(rng.randrange(10000), 1000) for _ in range(n)])
                assert w[0] <= t <= w[1]
    for n in range(1, 9):  # (a) without the formula: n zombies drain exactly 30n before stopping
        assert simulate_death(30 * n + 1, [0] * n) is None and simulate_death(30 * n, [0] * n) is not None
    assert {h: min_zombies_to_kill(h) for h in (30, 31, 90, 100, 110, 200, 220)} == \
        {30: 1, 31: 2, 90: 3, 100: 4, 110: 4, 200: 7, 220: 8}
    assert (death_time_window(100, 50), death_time_window(220, 50), death_time_window(100, 4)) == \
        ((10, 20), (40, 50), (240, 250))
    # (c) contact needed for a full cap
    assert (simulate_death(30, [0]), simulate_death(30, [10])) == (290, 300)
    assert (simulate_death(15, [0], 5, 15), simulate_death(15, [5], 5, 15)) == (70, 75)

    # (c) a contact cut by the lifetime: ticks start + phi + jP that land by the expiry (closed lifetime)
    def before_expiry(start, life, phi, period, cap):
        return sum(1 for j in range(cap) if start + phi + j * period <= life)
    for life, period, cap, latest in ((1200, 10, 30, {10: 900, 0: 910}), (3600, 5, 15, {5: 3525, 0: 3530})):
        for phi, last in latest.items():
            full = [s for s in range(life + 1) if before_expiry(s, life, phi, period, cap) == cap]
            assert max(full) == last and full == list(range(last + 1))
            for s in range(0, life + 1, 7):
                assert before_expiry(s, life, phi, period, cap) == min(contact_ticks(life - s, phi, period), cap)
    assert (before_expiry(1000, 1200, 10, 10, 30), before_expiry(1000, 1200, 0, 10, 30)) == (20, 21)
    # (d) the rate bound over a lifetime: A (one grid) and B1 (timer restarts at each entry)
    for _ in range(300):
        life = rng.randrange(10, 2000)
        cuts = sorted(rng.uniform(0, life) for _ in range(2 * rng.randrange(1, 8)))
        contacts = list(zip(cuts[::2], cuts[1::2]))
        phi = rng.uniform(0, 10)
        grid = sum(1 for j in range(life // 10 + 2) if any(a <= phi + 10 * j <= b for a, b in contacts))
        b1 = sum(sum(1 for j in range(1, 300) if a + 10 * j <= b) for a, b in contacts)
        assert grid <= life // 10 + 1 and b1 <= life // 10


# ---------- T-0704 ----------

def test_t0704_speed_rule():
    exact = F(20 * 1609344, 3600 * 1000)  # 20 mph in m/s, international mile
    assert exact == F(5588, 625)
    assert separation_gain_per_window(F(894, 100)) == F(2262, 5)  # 452.4 m
    assert separation_gain_per_window(exact) == F(56556, 125)  # 452.448 m
    assert escape_time(F(894, 100), 0, F(5), U) == F(250, 377)
    for z, uu in ((REGULAR, U), (GUARD, F(0)), (GUARD, U)):  # (a) every B1 threshold is legal
        assert zero_drain_speed(F(0), z, u=uu) < F(894, 100)
        assert escape_drain(F(894, 100), F(0), z["period"], z, u=uu) == 0
        assert escape_drain(F(894, 100), F(0), F(0), z, u=uu) == z["dmg"]  # B0 still pays one tick
    # (b) equality: straight flight at the threshold for 60 s against pursuit, exact
    d, vmax = F(3), F(894, 100)
    for _ in range(600):
        d += (vmax - U) / 10
    assert d - 3 == separation_gain_per_window(vmax)
    # (b) bound: random paths of path length exactly 536.4 m in the window (the 1 min rule only;
    # the 15 s rule is not enforced, it would only remove paths) never gain more
    rng = random.Random(704)
    dt = 0.05
    for _ in range(200):
        z, e, heading = (0.0, 0.0), (3.0, 0.0), 0.0
        speeds = [rng.uniform(0, 1) for _ in range(1200)]
        scale = 8.94 * 60 / (sum(speeds) * dt)
        for k in range(1200):
            if k % 40 == 0:
                heading = rng.gauss(0, 0.8)
            e = move(e, heading, speeds[k] * scale, dt)
            z = step_toward(z, e, u, dt)
        assert dist(z, e) - 3.0 <= float(separation_gain_per_window(F(894, 100))) + 1e-6
    # (c) with a contact inside the window the bound fails: 15 s still at distance 0, then 45 s at 11.92 m/s
    speed = F(5364, 10) / 45
    assert speed == F(298, 25) and speed < F(1341, 100) and (45 * speed) / 60 == F(894, 100)
    d = F(0)
    for _ in range(150):  # 15 s in contact: the zombie stays on the contestant
        d = max(d - U / 10, F(0))
    for _ in range(450):
        d += (speed - U) / 10
    assert d == F(4734, 10) and d > separation_gain_per_window(F(894, 100))


# ---------- T-0705 ----------

def test_t0705_guard_disk():
    for a in range(-50, 51):
        for b in range(-50, 51):
            px, py = F(a, 2), F(b, 2)
            d2 = (px - 10) ** 2 + py ** 2  # guard at (10, 0), gravestone at the origin
            assert guard_in_range(px, py) == (d2 <= 100)
            assert guard_in_range(px, py, closed=False) == (d2 < 100)
            if px <= 0 and (a, b) != (0, 0):
                assert not guard_in_range(px, py)  # (b) far side of the grave
    assert guard_in_range(0, 0) and not guard_in_range(0, 0, closed=False)  # (a)
    M = 20000
    for s in (1, 2, 5, 10, 15, 19):  # (c) rotate the guard, keep the looter fixed at (s, 0)
        hits = sum((s - 10 * math.cos(2 * math.pi * k / M)) ** 2 + (10 * math.sin(2 * math.pi * k / M)) ** 2 <= 100
                   for k in range(M))
        assert abs(hits / M - math.acos(s / 20) / math.pi) <= 2 / M
    assert abs(math.acos(10 / 20) / math.pi - 1 / 3) < 1e-12


# ---------- T-0706 ----------

def keep_or_switch(zombie, pos, target):
    """Convention K: keep the target unless another contestant is strictly nearer (ties keep it)."""
    best = min(pos, key=lambda c: dist(zombie, pos[c]))
    return best if target is None or dist(zombie, pos[best]) < dist(zombie, pos[target]) else target


def run_escort(rng, steps=2000, dt=0.05):
    """Reading B: the immune owner is a valid target. Targets are chosen with every position taken
    at the same instant, then everyone moves."""
    owner = (0.0, 0.0)
    others = [(rng.uniform(-30, 30), rng.uniform(-30, 30)) for _ in range(5)]
    others = [p for p in others if dist(p, owner) > 3]
    zombie, target = owner, "owner"
    heading, speed = 0.0, 0.0
    out = []
    for k in range(steps):
        if k % 20 == 0:
            heading = rng.uniform(0, 2 * math.pi)
            speed = float(ESCORT_MAX_SPEED) if k % 60 == 0 else rng.uniform(0, float(ESCORT_MAX_SPEED))
        target = keep_or_switch(zombie, {"owner": owner, **dict(enumerate(others))}, target)
        owner = move(owner, heading, speed, dt)
        others = [move(p, rng.uniform(0, 2 * math.pi), rng.uniform(0, 1.0), dt) for p in others]
        zombie = step_toward(zombie, {"owner": owner, **dict(enumerate(others))}[target], u, dt)
        out.append((owner, zombie, target, others))
    return out


def test_t0706_escort():
    rng = random.Random(706)
    for _ in range(40):
        for owner, zombie, target, others in run_escort(rng):  # (a), (b) under reading B
            assert target == "owner" and dist(owner, zombie) <= TOL
            assert [dist(p, zombie) <= 5 for p in others] == [dist(p, owner) <= 5 for p in others]
    # (c) is reading A itself (the immune owner is not a candidate); only its consequence is checked:
    # a still owner, one still bystander 30 m away. Reading A sends the zombie away, reading B keeps it.
    dt = 0.05
    for reading, stays in (("A", False), ("B", True)):
        owner, by, zombie, target = (0.0, 0.0), (30.0, 0.0), (0.0, 0.0), None
        for _ in range(600):
            pos = {"by": by} if reading == "A" else {"owner": owner, "by": by}
            target = keep_or_switch(zombie, pos, target)
            zombie = step_toward(zombie, pos[target], u, dt)
        assert (dist(owner, zombie) <= TOL) == stays
        assert stays or dist(owner, zombie) > 5
    # (d) a fast owner walking straight on leaves the escort behind at v - 1.4
    dt, v = 0.05, 2.0
    owner, zombie = (0.0, 0.0), (0.0, 0.0)
    for k in range(1, 401):
        owner = move(owner, 0.3, v, dt)
        zombie = step_toward(zombie, owner, u, dt)
        assert abs(dist(owner, zombie) - (v - u) * k * dt) < 1e-6
    # (b) death zombies r <= 10 m away join an owner slower than 1.4 m/s within r / (1.4 - v)
    for _ in range(200):
        r, v = rng.uniform(0.5, 10), rng.choice([0.0, rng.uniform(0, 1.2)])
        flee = rng.random() < 0.5  # an owner walking straight away is the slowest case
        ang = rng.uniform(0, 2 * math.pi)
        owner, zombie = (0.0, 0.0), (r * math.cos(ang), r * math.sin(ang))
        heading, t = ang + math.pi, 0.0
        while dist(owner, zombie) > TOL:
            if not flee and int(t / dt) % 20 == 0:
                heading = rng.uniform(0, 2 * math.pi)
            owner = move(owner, heading, v, dt)
            zombie = step_toward(zombie, owner, u, dt)
            t += dt
        assert t <= float(escort_join_time(F(r), F(v))) + dt + 1e-9
        if flee:
            assert t >= float(escort_join_time(F(r), F(v))) - 1e-6
    assert abs(float(escort_join_time(F(10), F(0))) - 7.142857) < 1e-6
    # (b) with a moving bystander, nearest at appearance is not enough; the bound holds when the owner
    # stays the target until the join, and both outcomes occur (the hypothesis is not vacuous)
    kept = switched = 0
    for _ in range(300):
        r, v = rng.uniform(0.5, 10), rng.choice([0.0, rng.uniform(0, 1.2)])
        ang, bang = rng.uniform(0, 2 * math.pi), rng.uniform(0, 2 * math.pi)
        owner, zombie = (0.0, 0.0), (r * math.cos(ang), r * math.sin(ang))
        gap = r + rng.uniform(0.5, 8)  # the owner is strictly nearest at appearance
        by = (zombie[0] + gap * math.cos(bang), zombie[1] + gap * math.sin(bang))
        bspeed, heading, target, t = rng.uniform(0, 3), rng.uniform(0, 2 * math.pi), "owner", 0.0
        while dist(owner, zombie) > TOL:
            target = keep_or_switch(zombie, {"owner": owner, "by": by}, target)
            if target != "owner":
                break
            owner = move(owner, heading, v, dt)
            by = move(by, math.atan2(zombie[1] - by[1], zombie[0] - by[0]), bspeed, dt)
            zombie = step_toward(zombie, owner, u, dt)
            t += dt
        if target == "owner":
            kept += 1
            assert t <= float(escort_join_time(F(r), F(v))) + dt + 1e-9
        else:
            switched += 1
    assert kept > 30 and switched > 30
    # the takeover example of (b): still owner, zombie 10 m away, a contestant 11 m from the zombie
    # running straight at it at 3 m/s becomes strictly nearer after 5 s, before the join at 7.14 s
    owner, zombie, by, target, t, h = (0.0, 0.0), (10.0, 0.0), (21.0, 0.0), "owner", 0.0, 0.001
    while dist(owner, zombie) > TOL:
        target = keep_or_switch(zombie, {"owner": owner, "by": by}, target)
        if target != "owner":
            break
        by = move(by, math.pi, 3.0, h)
        zombie = step_toward(zombie, owner, u, h)
        t += h
    assert target == "by" and abs(t - 5) < 0.01 and t < float(escort_join_time(F(10), F(0)))


# ---------- T-0707 ----------

def entry_distance(z0, m, R=10):
    """Distance to E = origin at which the straight walk from z0 to E first enters disk(m, R)."""
    L = math.hypot(*z0)
    w = (-z0[0] / L, -z0[1] / L)
    b = w[0] * (z0[0] - m[0]) + w[1] * (z0[1] - m[1])
    c = (z0[0] - m[0]) ** 2 + (z0[1] - m[1]) ** 2 - R * R
    disc = b * b - c
    if disc < 0:
        return None
    s = -b - math.sqrt(disc)
    return L - s if 0 <= s <= L else None


def segment_gap(z0, m):
    """Closest distance from the point m to the segment from z0 to E = origin."""
    s = min(max((z0[0] * m[0] + z0[1] * m[1]) / (z0[0] ** 2 + z0[1] ** 2), 0.0), 1.0)
    return math.hypot(s * z0[0] - m[0], s * z0[1] - m[1])


def test_t0707_landmine():
    starts = [(a, b) for a in range(-60, 61, 3) for b in range(-60, 61, 3)]
    assert abs(mine_safe_distance() - 5 * math.sqrt(5)) < 1e-12
    # control for the hypothesis of (d): at x = 11, a walk from the far side never meets the mine disk
    # and reaches E, so no bound on the time within 5 m holds without it
    assert entry_distance((-30.0, 0.0), (11.0, 0.0)) is None and segment_gap((-30.0, 0.0), (11.0, 0.0)) == 11.0
    for x in (10.5, 11.0, 11.1, mine_safe_distance(), 11.3, 12.0, 15.0, 20.0, 30.0):
        for psi in (0.0, 0.7, 2.0):
            m = (x * math.cos(psi), x * math.sin(psi))
            graze = math.asin(10 / x) - 1e-9  # a walk that just grazes the mine disk (tangent)
            tangents = [(3 * x * math.cos(psi + s * graze), 3 * x * math.sin(psi + s * graze)) for s in (1, -1)]
            for z0 in starts + tangents:
                if dist(z0, m) <= 10 or math.hypot(*z0) <= 5:
                    continue
                at = entry_distance(z0, m)
                if at is None:  # the walk misses the mine disk: outside the hypothesis of (b) to (d)
                    assert segment_gap(z0, m) > 10 - 1e-9
                    continue
                assert at >= math.sqrt(x * x - 100) - 1e-6  # the entry lemma: tangent walks are worst
                if x > mine_safe_distance():  # (c): trigger before the zombie is within 5 m
                    assert at > 5
                else:  # (d): time within 5 m before the trigger
                    assert max(0.0, 5 - at) / u <= mine_drain_window(x) + 1e-6
            for z0 in tangents:  # the lemma and the bound of (d) are reached by tangent walks
                assert abs(entry_distance(z0, m) - math.sqrt(x * x - 100)) < 1e-3
                if x <= mine_safe_distance():
                    assert abs(max(0.0, 5 - entry_distance(z0, m)) / u - mine_drain_window(x)) < 1e-3
                if x == mine_safe_distance():  # (c) at the threshold: trigger exactly at 5 m from E
                    assert abs(entry_distance(z0, m) - 5) < 1e-3 and abs(mine_drain_window(x)) < 1e-12
    # (e) the cone condition implies the segment meets the mine disk, exact rationals
    for m in ((F(15), F(0)), (F(16), F(0)), (F(12), F(16)), (F(18), F(24))):
        x2 = m[0] ** 2 + m[1] ** 2
        for a in range(-60, 61, 2):
            for b in range(-60, 61, 2):
                z2 = a * a + b * b
                dot, cross = a * m[0] + b * m[1], a * m[1] - b * m[0]
                if z2 >= x2 and dot >= 0 and cross ** 2 <= 100 * z2:
                    t = min(max(dot / z2, 0), 1)
                    assert (t * a - m[0]) ** 2 + (t * b - m[1]) ** 2 <= 100
    # (f) Protection on its own mine: any zombie path meets 10 m before 5 m
    rng = random.Random(707)
    for _ in range(300):
        r, ang = rng.uniform(10.5, 40), rng.uniform(0, 2 * math.pi)
        z, first10, first5 = (r * math.cos(ang), r * math.sin(ang)), None, None
        for k in range(3000):
            z = move(z, math.atan2(-z[1], -z[0]) + rng.uniform(-1.5, 1.5), rng.uniform(0, u), 0.1)
            if first10 is None and math.hypot(*z) <= 10:
                first10 = k
            if first5 is None and math.hypot(*z) <= 5:
                first5 = k
        assert first5 is None or (first10 is not None and first10 < first5)
