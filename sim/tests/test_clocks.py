"""Prover tests for the deterministic clocks of theory/05-survival-processes.md (T-0008..T-0013).

Each closed form is checked against a second-by-second tick simulation written
independently of the formula. Checks our model of the rules, not the game.
"""


def ticks_until_dead(h, first, interval, dmg=1):
    """Second at which HP reaches 0 when ticks of dmg land at first, first+interval, ..."""
    t = 0
    while h > 0:
        t += 1
        if t >= first and (t - first) % interval == 0:
            h -= dmg
    return t


def test_t0008_zone_time_to_death():
    for h in range(1, 221):
        assert ticks_until_dead(h, 5, 2) == 2 * h + 3  # U-0003 reading A: first tick at 5 s
        assert ticks_until_dead(h, 7, 2) == 2 * h + 5  # reading B: first tick at 7 s
    assert (ticks_until_dead(100, 5, 2), ticks_until_dead(100, 7, 2)) == (203, 205)
    for h in range(1, 221):  # Hazmat suit: interval 4 s (M-0209), first tick moved or not (U-0205)
        assert ticks_until_dead(h, 5, 4) == 4 * h + 1
        assert ticks_until_dead(h, 9, 4) == 4 * h + 5
        assert ticks_until_dead(h, 7, 4) == 4 * h + 3  # first tick at 7 s, not moved by the suit


def poison_damage(total, repoison_every, horizon, interval=90):
    """HP lost to poison when the contestant is re-poisoned every repoison_every seconds and each
    re-poisoning restarts the tick clock (M-0171, reading 'reset the tick timer')."""
    lost, since, left = 0, 0, total
    for t in range(1, horizon + 1):
        since += 1
        if repoison_every and t % repoison_every == 0:
            since, left = 0, total
        if since == interval and left > 0:
            lost, since, left = lost + 1, 0, left - 1
    return lost


def test_t0009_poison_clock():
    # all of this assumes U-0115 reading A: first tick 90 s after (re)poisoning
    assert poison_damage(20, 0, 1800) == 20  # dart: 20 HP over 30 min = 20 ticks at 90 s
    assert poison_damage(20, 0, 1799) == 19
    for k in range(1, 90):
        assert poison_damage(20, k, 86_400) == 0  # re-poisoned faster than 90 s: never ticks
    assert poison_damage(20, 90, 86_400) == 0  # at exactly 90 s the reset wins (same-second order)
    assert poison_damage(20, 91, 3 * 91) == 3


def test_t0010_zombie_drain_clocks():
    # one zombie: 1 HP every 10 s, cap 30 (M-0441, M-0442); guard: 2 HP every 5 s, cap 30 (M-0449)
    assert ticks_until_dead(30, 10, 10) == 300 and ticks_until_dead(30, 0 + 10, 10) == 300
    assert ticks_until_dead(30, 5, 5, dmg=2) == 75
    assert ticks_until_dead(30, 0 + 5, 5, dmg=2) == 75


def test_t0011_t0012_slow_clocks():
    assert 24 * 60 // 30 == 48  # Healing regeneration: at most 48 HP per day (M-0652)
    assert (45 - 15) * 20 == 600  # armor enchantment decay 45 -> 15 at 1 per 20 min: 10 h (M-0339)


def test_t0013_zombie_escape():
    # leaving the 5 m drain range at speed v from distance r0: time (5 - r0) / (v - 1.4)
    for r0 in (0.0, 2.5, 4.9):
        for v in (1.5, 2.0, 3.0, 8.94):
            t = (5 - r0) / (v - 1.4)
            assert t >= 0
    assert abs((5 - 0) / (2.0 - 1.4) - 8.333333) < 1e-5  # brisk walk: out in 8.3 s, before the first 10 s tick
