# Rules: zone

## Summary

Rules of the `zone` family, as the wiki states them on 2026-11-11.

### In plain words

The zone family is the rule that keeps everyone moving and honest. Contestants must stay inside the safe zone, which is tracked by the GPS in their phone. The organizer can move it, so it can change in size or speed, or even split apart ([M-0100](../rules/zone.md#m-0100)).

The main penalty is simple. When you are outside, after 5 seconds you start taking 1 HP damage every 2 seconds ([M-0101](../rules/zone.md#m-0101)).

There are two ways to be "outside" without actually stepping out. Moving too fast counts as being outside: faster than 20 mph on average over 1 minute ([M-0105](../rules/zone.md#m-0105)), or faster than 30 mph over any 15 seconds ([M-0106](../rules/zone.md#m-0106)). And if your phone stops sending GPS updates while your last known location was inside a safe zone, you start taking damage after 15 minutes, or 30 minutes if you are live on Kick ([M-0104](../rules/zone.md#m-0104)). The longer offline grace for Kick-live contestants is the same rule stated on its own ([M-0103](../rules/zone.md#m-0103)).

The Trolling sigil can turn part of a safe zone into a danger area: its unsafe circle is placed inside a safe zone for 20 minutes, with a 2 hour cooldown ([M-0535](../rules/zone.md#m-0535)).

What defenses exist? A Hazmat suit makes each zone damage interval 2 s longer while you carry it ([M-0209](../rules/items.md#m-0209)). Guardian angel gives immunity to zone damage for 10 minutes ([M-0210](../rules/items.md#m-0210)). A Safety bubble makes everyone inside immune to damage, zone damage included ([M-0213](../rules/items.md#m-0213)). A Shield does not block zone damage ([M-0128](../rules/damage.md#m-0128)).

Strongest as written: it applies to everyone equally, and is not tied to any sigil ([M-0101](../rules/zone.md#m-0101)). Weakest: it depends on a phone and GPS, which can fail through no fault of the player ([M-0104](../rules/zone.md#m-0104)).

What is unknown: whether the first tick comes at 5 seconds or at 7 seconds ([U-0003](../unknowns.md#u-0003)). It is open what damage applies once the offline grace ends ([U-0110](../unknowns.md#u-0110)), and whether a later GPS update resets the grace timer ([U-0111](../unknowns.md#u-0111)). It is open how the speed averaging works, as a sliding window, a fixed window or a ratio ([U-0112](../unknowns.md#u-0112)), and what exactly happens when the speed rule trips ([U-0113](../unknowns.md#u-0113)). With several safe zones, it is open whether damage starts when you are outside every zone or when you leave the one you were last in ([U-0114](../unknowns.md#u-0114)). Unsafe circle details, radius or diameter and when the cooldown starts, are open too ([U-0535](../unknowns.md#u-0535), [U-0536](../unknowns.md#u-0536)).

This page gathers 7 rules (7 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0100"></a>

### M-0100: Safe zone is moved by the organizer (size, speed, split)

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0100](../rules/zone.md#m-0100) `wiki-004`: "it can change in size or speed, or even split apart" ([source](https://iceposeidon.com/safezone/wiki))

**Formal model:**

- [M-0100](../rules/zone.md#m-0100) reading A: `zone geometry is an exogenous organizer-controlled process Z(t); no rule given`
- [M-0100](../rules/zone.md#m-0100) parameter `zone_process`: UNKNOWN, see [U-0114](../unknowns.md#u-0114)

**Open questions:**

- [U-0114](../unknowns.md#u-0114) (high): The zone can 'split apart': with several safe zones, is 'leave a safezone' damage triggered when outside every zone (A) or when leaving the zone you were last in (B)?

Notes ([M-0100](../rules/zone.md#m-0100)): Only the existence of resizing, speeding and splitting is stated. Geometry stays abstract.

<a id="m-0101"></a>

### M-0101: Outside-the-safezone damage tick

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0101](../rules/zone.md#m-0101) `wiki-005`: "after 5s you will start taking 1 HP damage every 2s (30 HP per minute)" ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- [M-0101](../rules/zone.md#m-0101) reading A: `t_out >= 5: HP loss 1 at t_out = 5, 7, 9, ... (first tick at 5 s)`
- [M-0101](../rules/zone.md#m-0101) reading B: `t_out >= 5: HP loss 1 at t_out = 7, 9, 11, ... (first tick after one more interval)`
- [M-0101](../rules/zone.md#m-0101) domain: t_out integer seconds since leaving every safezone, t_out >= 0
- [M-0101](../rules/zone.md#m-0101) parameter `grace_s`: 5
- [M-0101](../rules/zone.md#m-0101) parameter `interval_s`: 2
- [M-0101](../rules/zone.md#m-0101) parameter `tick_hp`: 1

**Consequences:** [T-0304](../theorems/T-0304.md)

**Open questions:**

- [U-0003](../unknowns.md#u-0003) (medium): Zone damage: is the first tick at 5 s or at 7 s after leaving the safe zone?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?
- [U-0114](../unknowns.md#u-0114) (high): The zone can 'split apart': with several safe zones, is 'leave a safezone' damage triggered when outside every zone (A) or when leaving the zone you were last in (B)?

Notes ([M-0101](../rules/zone.md#m-0101)): The 30 HP per minute figure is 60/2 and holds for both readings. Whether the tick is a hit in the 7-step pipeline is [U-0002](../unknowns.md#u-0002); with Kick live, 1 HP after floor reductions is raised to 1 by the minimum only if [U-0002](../unknowns.md#u-0002) puts the tick in the pipeline. The unsafe circle (Trolling sigil page) is stated to hurt the same way; compare in a later cross-page pass.

<a id="m-0103"></a>

### M-0103: Kick-live status doubles the offline grace period (15 to 30 min)

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0103](../rules/zone.md#m-0103) `wiki-006`: "you have a longer offline grace period, so if your phone dies, you have 30min instead of 15min before you start taking damage" ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- [M-0103](../rules/zone.md#m-0103) reading A: `grace_s = 1800 if live on Kick else 900`
- [M-0103](../rules/zone.md#m-0103) domain: live in {true, false}
- [M-0103](../rules/zone.md#m-0103) parameter `grace_live_s`: 1800
- [M-0103](../rules/zone.md#m-0103) parameter `grace_base_s`: 900

**Open questions:**

- [U-0111](../unknowns.md#u-0111) (high): Offline grace timer semantics: is it measured from the last GPS update only, does a later GPS update reset it, and is 'live on Kick' evaluated at the moment the GPS stops (A), at the expiry (B), or continuously with fractional accrual (C)?
- [U-0012](../unknowns.md#u-0012) (medium): How is Kick-live status detected, and with what latency?

Notes ([M-0103](../rules/zone.md#m-0103)): The moment at which live status is read is the open point ([U-0111](../unknowns.md#u-0111)).

<a id="m-0104"></a>

### M-0104: GPS offline grace before damage

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0104](../rules/zone.md#m-0104) `wiki-009`: "If your phone stops sending GPS updates, and your last known location was inside a safezone, you start taking damage after 15min, or 30min if you are live on Kick." ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- [M-0104](../rules/zone.md#m-0104) reading A: `if last fix inside a safezone: damage begins at T_off >= grace (900 s, or 1800 s if live)`
- [M-0104](../rules/zone.md#m-0104) reading B: `if last fix inside a safezone: damage begins at T_off > grace (strict)`
- [M-0104](../rules/zone.md#m-0104) reading C: `if last fix outside every safezone: no grace, the ordinary outside rule runs (not stated, assumed from the condition)`
- [M-0104](../rules/zone.md#m-0104) domain: T_off integer seconds since the last GPS update
- [M-0104](../rules/zone.md#m-0104) parameter `grace_base_s`: 900
- [M-0104](../rules/zone.md#m-0104) parameter `grace_live_s`: 1800
- [M-0104](../rules/zone.md#m-0104) parameter `damage_after_grace`: UNKNOWN, see [U-0110](../unknowns.md#u-0110)

**Open questions:**

- [U-0110](../unknowns.md#u-0110) (high): After the offline grace ends ('you start taking damage after 15min'), what damage applies: the outside-circle rule (5 s grace then 1 HP every 2 s), an immediate tick cadence, or something else?
- [U-0111](../unknowns.md#u-0111) (high): Offline grace timer semantics: is it measured from the last GPS update only, does a later GPS update reset it, and is 'live on Kick' evaluated at the moment the GPS stops (A), at the expiry (B), or continuously with fractional accrual (C)?
- [U-0012](../unknowns.md#u-0012) (medium): How is Kick-live status detected, and with what latency?

Notes ([M-0104](../rules/zone.md#m-0104)): Reading C is stated only by the conditional clause 'and your last known location was inside a safezone'; what happens otherwise is not written. Same numbers as the intro Kick sentence (15 and 30 min): consistent.

<a id="m-0105"></a>

### M-0105: Speed rule: mean speed over 1 min above 20 mph counts as outside

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0105](../rules/zone.md#m-0105) `wiki-010`: "Moving too fast counts as being outside: faster than 20mph (8.94m/s) on average over 1min" ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- [M-0105](../rules/zone.md#m-0105) reading A: `violation if mean_speed over a 60 s window > 8.94 m/s, windows sliding`
- [M-0105](../rules/zone.md#m-0105) reading B: `violation if mean_speed over a 60 s window > 8.9408 m/s (exact 20 mph)`
- [M-0105](../rules/zone.md#m-0105) reading C: `window displacement endpoint to endpoint rather than path length`
- [M-0105](../rules/zone.md#m-0105) domain: speed in m/s, window 60 s
- [M-0105](../rules/zone.md#m-0105) parameter `threshold_ms`: 8.94
- [M-0105](../rules/zone.md#m-0105) parameter `window_s`: 60

**Consequences:** [T-0704](../theorems/T-0704.md)

**Open questions:**

- [U-0112](../unknowns.md#u-0112) (high): Speed rule averaging: is '20mph on average over 1min' a sliding window, a fixed window, or a ratio of distance to time; is '30mph over any 15s' the same average on a 15 s window or a peak speed; are comparisons strict; are 8.94 and 13.41 m/s the exact thresholds?
- [U-0113](../unknowns.md#u-0113) (medium): 'Moving too fast counts as being outside': when the speed rule trips, does the 5 s grace and 1 HP per 2 s apply as outside, starting when, and does it end the instant speed drops back?

<a id="m-0106"></a>

### M-0106: Speed rule: speed above 30 mph over any 15 s counts as outside

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0106](../rules/zone.md#m-0106) `wiki-010`: "or faster than 30mph (13.41m/s) over any 15s" ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- [M-0106](../rules/zone.md#m-0106) reading A: `violation if mean_speed over some 15 s window > 13.41 m/s`
- [M-0106](../rules/zone.md#m-0106) reading B: `violation if peak speed during any 15 s window > 13.41 m/s`
- [M-0106](../rules/zone.md#m-0106) reading C: `exact threshold 13.4112 m/s`
- [M-0106](../rules/zone.md#m-0106) domain: speed in m/s, window 15 s
- [M-0106](../rules/zone.md#m-0106) parameter `threshold_ms`: 13.41
- [M-0106](../rules/zone.md#m-0106) parameter `window_s`: 15

**Open questions:**

- [U-0112](../unknowns.md#u-0112) (high): Speed rule averaging: is '20mph on average over 1min' a sliding window, a fixed window, or a ratio of distance to time; is '30mph over any 15s' the same average on a 15 s window or a peak speed; are comparisons strict; are 8.94 and 13.41 m/s the exact thresholds?
- [U-0113](../unknowns.md#u-0113) (medium): 'Moving too fast counts as being outside': when the speed rule trips, does the 5 s grace and 1 HP per 2 s apply as outside, starting when, and does it end the instant speed drops back?

Notes ([M-0106](../rules/zone.md#m-0106)): Two separate windows (1 min mean at 8.94, 15 s at 13.41). The printed m/s values are rounded from 8.9408 and 13.4112.

<a id="m-0535"></a>

### M-0535: Unsafe circle placement

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-016`: "Unsafe circle: place a 50m (164ft) circle inside a safe zone for 20min." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-018`: "Cooldown 2h." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-019`: "No living contestant, you included, may be inside the circle when you place it." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0535](../rules/zone.md#m-0535) `wiki-sigils-trolling-021`: "A Trolling contestant can place an unsafe circle inside a safe zone." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))

**Formal model:**

- [M-0535](../rules/zone.md#m-0535) reading A: `place(circle, centre c) with radius 50 m, c inside a safe zone, no living contestant inside it at placement, the placer included; lasts 1200 s; next placement allowed 7200 s after placement`
- [M-0535](../rules/zone.md#m-0535) reading B: `diameter 50 m (radius 25 m)`
- [M-0535](../rules/zone.md#m-0535) reading C: `cooldown 7200 s starts when the circle ends`
- [M-0535](../rules/zone.md#m-0535) domain: time in seconds; radius in metres
- [M-0535](../rules/zone.md#m-0535) parameter `size_m`: UNKNOWN, see [U-0535](../unknowns.md#u-0535)
- [M-0535](../rules/zone.md#m-0535) parameter `duration_s`: 1200
- [M-0535](../rules/zone.md#m-0535) parameter `cooldown_s`: 7200
- [M-0535](../rules/zone.md#m-0535) parameter `cooldown_anchor`: UNKNOWN, see [U-0536](../unknowns.md#u-0536)

**Interactions:** [M-0536](../rules/damage.md#m-0536), [M-0537](../rules/items.md#m-0537)

**Open questions:**

- [U-0535](../unknowns.md#u-0535) (high): Unsafe circle '50m (164ft) circle': is 50 m the radius or the diameter?
- [U-0536](../unknowns.md#u-0536) (low): Unsafe circle 'Cooldown 2h' with a 20 min duration: does the cooldown start at placement or when the circle ends?

Notes ([M-0535](../rules/zone.md#m-0535)): 'inside a safe zone' is checked at placement in the text; the safe zone moves, and only the part inside a safe zone hurts ([M-0536](../rules/damage.md#m-0536)).

## Simulation check

Theorems with tests in `sim/tests/`: [T-0304](../theorems/T-0304.md), [T-0704](../theorems/T-0704.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0003](../unknowns.md#u-0003), [U-0012](../unknowns.md#u-0012), [U-0110](../unknowns.md#u-0110), [U-0111](../unknowns.md#u-0111), [U-0112](../unknowns.md#u-0112), [U-0113](../unknowns.md#u-0113), [U-0114](../unknowns.md#u-0114), [U-0535](../unknowns.md#u-0535), [U-0536](../unknowns.md#u-0536)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
