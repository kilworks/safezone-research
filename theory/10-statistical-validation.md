# 10. Statistical validation from public observations

The wiki states five probabilities. Nobody outside the organizers can read the server's random number generator, so the only way to check them is to count outcomes in public stream VODs. This file says how many observations each check needs, what a realistic small sample can and cannot show, and how to record an observation.

Every number below comes from `analysis/scripts/sample_sizes.py` (output `analysis/results/sample_sizes.json`, deterministic, no random seed involved).

## 10.1 The stated probabilities

| Name | Stated $p_0$ | Clause | Alternative $p_1$ worth detecting |
|---|---|---|---|
| Eddie's potion heals | 0.10 | `wiki-items` (Eddie's potion) | 0.15 |
| Zombie breaks a health potion | 0.10 | `wiki-zombies` | 0.15 |
| Zombie destroys a crafted item | 0.40 | `wiki-zombies`, `wiki-sigils-ingenuity` | 0.50 |
| Greed chest gives a Shield | 0.25 | `wiki-sigils-greed` | 0.35 |
| Care package lands next to a Trolling contestant | 0.03 | `wiki-attacks`, `wiki-sigils-trolling` | 0.06 |

The alternatives are a choice of this project (a deviation large enough to matter for strategy), not a claim about the game.

## 10.2 One-sided test of a stated probability

We observe $n$ independent trials and $k$ successes, and test $H_0: p = p_0$ against $H_1: p = p_1 > p_0$ at level $\alpha = 0.05$ with power $1 - \beta = 0.8$.

**Normal approximation.** The classical sample size is

$$
n = \left( \frac{z_{1-\alpha}\sqrt{p_0(1-p_0)} + z_{1-\beta}\sqrt{p_1(1-p_1)}}{p_1 - p_0} \right)^2 ,
$$

with $z_q$ the standard normal quantile. Hypotheses: independent trials with a common $p$, and $n$ large enough that the binomial is close to normal under both hypotheses.

**Exact binomial test.** The approximation is poor for small $p$. The script also finds the smallest $n$ for which the exact one-sided binomial test (reject when $k \ge k^*$, with $P(K \ge k^* \mid p_0) \le \alpha$) has power at least 0.8 at $p_1$. The power of an exact test is not monotone in $n$ (it saws up and down as $k^*$ jumps), so "smallest $n$" is the first $n$ that reaches the target, not a guarantee for every larger $n$.

| Name | $n$ (normal) | $n$ (exact binomial) |
|---|---|---|
| Eddie's potion heals | 252.2, so 253 | 270 |
| Zombie breaks a health potion | 252.2, so 253 | 270 |
| Zombie destroys a crafted item | 150.5, so 151 | 158 |
| Greed chest gives a Shield | 124.0, so 125 | 129 |
| Care package next to Trolling | 256.5, so 257 | 282 |

The master prompt's worked value ($n \approx 253$ Eddie's potion drinks) is reproduced. The exact test needs 270.

## 10.3 What small samples can show

Public VODs will rarely show 250 drinks of Eddie's potion. With a sample of 30 trials whose observed rate equals the stated one, the exact Clopper-Pearson (1934) 95% interval is:

| Name | $k / n$ | 95% interval |
|---|---|---|
| Eddie's potion heals | 3 / 30 | [0.021, 0.265] |
| Zombie destroys a crafted item | 12 / 30 | [0.227, 0.594] |
| Greed chest gives a Shield | 8 / 30 | [0.123, 0.459] |
| Care package next to Trolling | 1 / 30 | [0.001, 0.172] |

So 30 observations can catch a gross error (for example an Eddie's potion that heals half the time) but cannot tell 10% from 20%. Small samples are still useful in two ways: a single impossible outcome refutes a reading outright (an HP change that no reading of a rule allows), and a Beta-Binomial posterior with a stated prior accumulates evidence across VODs. With a uniform $\mathrm{Beta}(1,1)$ prior and $k$ successes in $n$ trials, the posterior is $\mathrm{Beta}(1+k, 1+n-k)$.

When observations arrive one at a time, Wald's sequential probability ratio test (Wald, 1945) stops as soon as the evidence is decisive. With log-likelihood ratio $\Lambda_n = k \ln(p_1/p_0) + (n-k)\ln\big((1-p_1)/(1-p_0)\big)$, accept $H_1$ when $\Lambda_n \ge \ln\big((1-\beta)/\alpha\big)$ and $H_0$ when $\Lambda_n \le \ln\big(\beta/(1-\alpha)\big)$.

## 10.4 Deterministic rules decided by a single observation

Several open questions need one clean observation, not a sample, because each reading predicts a different integer:

| Unknown | Observation that decides it |
|---|---|
| U-0001 (Kick-live defender rounding) | A live contestant hit for 5 HP loses 4 (reading A) or 5 (reading B). |
| U-0003 (first zone tick) | Seconds between leaving the zone and the first HP loss: 5 or 7. |
| U-0006 (Ingenuity prices) | An Ingenuity merchant screen showing Dual Wield at 55 (exact) or 56 (binary64, H-0001). |
| U-0010 (wizard staff ticks) | HP readout during a staff area: one 10 HP drop or several smaller ones. |

Assumption for every row: the stream overlay shows HP and prices exactly. If it rounds or lags, the observation is void.

## 10.5 Observation protocol for VOD loggers

One line per event, in a CSV with these columns:

| Column | Content |
|---|---|
| `vod_url` | public VOD URL |
| `t_vod` | timestamp in the VOD (hh:mm:ss) |
| `event` | `eddie_drink`, `zombie_drain_tick`, `potion_broken`, `craft_destroyed`, `greed_chest_claim`, `care_package_drop`, `hit`, `merchant_screen` |
| `outcome` | the observed result (`heal` or `loss`, `broken` or `kept`, price shown, ...) |
| `hp_before`, `hp_after`, `max_hp` | as shown on screen, integers |
| `modifiers` | visible state: live on Kick, sigil, armor durability, shield, bubble, fortress |
| `notes` | anything that makes the line doubtful |

Never record where a contestant is: no map coordinates, street names, landmarks or screenshots of a map. `SCOPE.md` forbids collecting anyone's position, and no rule check above needs it.

## 10.6 Monte Carlo precision

For simulated probabilities near 0.5, the half-width of a 95% interval is $1.96\sqrt{0.25/n}$; $n = 38{,}416$ runs give $\pm 0.005$. Comparisons between sigils use common random numbers; derived statistics use the bootstrap (Efron, 1979); sensitivity to unknown parameters is ranked with Sobol indices (Sobol, 1993) using Saltelli estimators.

## Status

No observation has been logged yet. `analysis/results/` holds no observed data; every probability above remains `DOCUMENTED` (stated by the wiki) and none is `CORROBORATED`.
