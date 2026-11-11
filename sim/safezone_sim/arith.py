"""Exact integer arithmetic for percentage rules (no floating point anywhere).

The wiki states rules as "x% more/less, rounded down/up". These helpers compute
them exactly on integers; theory/02-rounding-and-arithmetic.md proves their
identities and analysis/scripts/float_drift.py measures where binary64 code drifts.
"""


def pct_floor(x: int, num: int, den: int = 100) -> int:
    """floor(x * num / den), exact."""
    return x * num // den


def pct_ceil(x: int, num: int, den: int = 100) -> int:
    """ceil(x * num / den), exact."""
    return -(-x * num // den)


def kick_attack(d: int) -> int:
    """Attacker live on Kick: +10%, rounded down (one reading, T-0001)."""
    return pct_floor(d, 110)


def kick_defense(d: int, reading: str = "A") -> int:
    """Defender live on Kick: -10%, rounded down. A floors the result, B floors the removed part (U-0001, T-0002)."""
    return pct_floor(d, 90) if reading == "A" else d - pct_floor(d, 10)


def halve(d: int) -> int:
    """50% less, rounded down (Protection against a nuke)."""
    return d // 2


def ladder_price(k: int) -> int:
    """k-th merchant purchase of a slot or of +10 max HP, k = 0, 1, ... (T-0006)."""
    return 40 + 10 * k


def ladder_total(n: int) -> int:
    """Total price of the first n purchases: 5n^2 + 35n (T-0006)."""
    return 5 * n * n + 35 * n
