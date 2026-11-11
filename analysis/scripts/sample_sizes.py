"""Section 8.11: how many observed trials a VOD logger needs to test each stated probability.

For each probability p0 the wiki states, and a deviation p1 worth detecting, computes
the one-sided normal-approximation sample size (level alpha, power 1 - beta), then
checks it with the exact binomial test: the smallest n whose exact one-sided test
(critical count from the binomial tail at p0) reaches the target power at p1.
Also gives, for small samples a VOD can realistically provide, the exact
Clopper-Pearson 95% interval width when the observed rate equals p0.

Writes analysis/results/sample_sizes.json. Usage: py -3 analysis/scripts/sample_sizes.py
"""
import json
import math
from pathlib import Path

from scipy.stats import beta, binom, norm

ROOT = Path(__file__).resolve().parents[2]
ALPHA, POWER = 0.05, 0.80
# name, stated probability, alternative worth detecting, source page
CASES = [
    ("eddie_heal", 0.10, 0.15, "items#eddies_potion: 10% chance to heal"),
    ("zombie_potion_break", 0.10, 0.15, "zombies: 10% chance to break a health potion"),
    ("zombie_craft_destroy", 0.40, 0.50, "zombies and ingenuity: 40% chance to destroy crafted items"),
    ("greed_chest_shield", 0.25, 0.35, "greed: 25% chance to give a Shield"),
    ("trolling_care_package", 0.03, 0.06, "attacks and trolling: 3% chance to land next to a Trolling contestant"),
]


def normal_n(p0, p1):
    za, zb = norm.ppf(1 - ALPHA), norm.ppf(POWER)
    return ((za * math.sqrt(p0 * (1 - p0)) + zb * math.sqrt(p1 * (1 - p1))) / (p1 - p0)) ** 2


def exact_n(p0, p1, n_max=20_000):
    """Smallest n where the exact one-sided binomial test at level ALPHA has power >= POWER at p1."""
    for n in range(1, n_max):
        k = int(binom.isf(ALPHA, n, p0)) + 1  # reject when successes >= k; P(X >= k | p0) <= ALPHA
        if binom.sf(k - 1, n, p0) <= ALPHA and binom.sf(k - 1, n, p1) >= POWER:
            return n
    return None


def clopper_pearson(k, n, conf=0.95):
    a = (1 - conf) / 2
    lo = 0.0 if k == 0 else beta.ppf(a, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(1 - a, k + 1, n - k)
    return lo, hi


def main():
    rows = []
    for name, p0, p1, src in CASES:
        nn, ne = normal_n(p0, p1), exact_n(p0, p1)
        small = {}
        for n in (10, 30, 100):
            k = round(p0 * n)
            lo, hi = clopper_pearson(k, n)
            small[n] = {"k": k, "cp95": [round(lo, 4), round(hi, 4)]}
        rows.append({"name": name, "p0": p0, "p1": p1, "source": src, "alpha": ALPHA, "power": POWER,
                     "n_normal": round(nn, 2), "n_normal_ceil": math.ceil(nn), "n_exact_binomial": ne,
                     "small_samples": small})
        print(f"{name:22s} p0={p0} p1={p1}: n_normal={nn:.1f} (ceil {math.ceil(nn)}), n_exact={ne}; "
              f"n=30 at p0 -> CP95 {small[30]['cp95']}")
    out = ROOT / "analysis" / "results" / "sample_sizes.json"
    out.write_text(json.dumps({"method": __doc__.strip().splitlines()[0], "cases": rows}, indent=1) + "\n",
                   "utf-8", newline="\n")


if __name__ == "__main__":
    main()
