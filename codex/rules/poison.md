# Rules: poison

## Summary

Rules of the `poison` family, as the wiki states them on 2026-11-11.

### In plain words

Poison is the slow, nagging damage in the game: not a big hit, but a clock that keeps ticking until something stops it. This family explains how you get poisoned, how it hurts, and what ends it.

How you get it: you can be poisoned by a Poison dart or a Fake gravestone, and by nothing else ([M-0173](../rules/poison.md#m-0173)). Once poisoned, you lose 1 HP every 1 minute 30 seconds ([M-0170](../rules/poison.md#m-0170)). Getting poisoned again resets the timer and does not stack ([M-0171](../rules/poison.md#m-0171)). Poison ends only when it has done all its damage, or if it is cured ([M-0172](../rules/poison.md#m-0172)). So an uncured poison is a fixed total bill, paid slowly ([M-0172](../rules/poison.md#m-0172)).

How to stop it: poison can be cured by Anti poison, Healing healing, or God's Fruit ([M-0174](../rules/poison.md#m-0174)). Anti poison cures poison and makes you immune to it for 10 minutes ([M-0221](../rules/poison.md#m-0221)). Other protections work before the poison lands: the Reality Shield stops new poison while you stand inside it ([M-0177](../rules/poison.md#m-0177)), and the Protection sigil is fully immune ([M-0175](../rules/poison.md#m-0175)). A Mirror forcefield turns a Poison Dart or a fake gravestone back on the attacker ([M-0180](../rules/poison.md#m-0180)). A Shield or a Safety bubble works differently: it does not stop the poison from landing, but blocks each poison step while it lasts ([M-0136](../rules/poison.md#m-0136), [M-0179](../rules/poison.md#m-0179)).

What a player would feel: a slow loss of 1 HP every 90 seconds ([M-0170](../rules/poison.md#m-0170)) until the total is paid or a cure lands ([M-0172](../rules/poison.md#m-0172)). Good against poison: Anti poison for a clean fix ([M-0221](../rules/poison.md#m-0221)), Protection for permanent safety ([M-0175](../rules/poison.md#m-0175)), a Mirror for sending it back ([M-0180](../rules/poison.md#m-0180)).

Weakest point of the poison itself as the rules read: it is slow ([M-0170](../rules/poison.md#m-0170)), it does not stack ([M-0171](../rules/poison.md#m-0171)), and it has several known counters ([M-0174](../rules/poison.md#m-0174)).

What is unknown: whether the first 1 HP lands at once or after the first interval ([U-0115](../unknowns.md#u-0115)). It is open whether a second poisoning only restarts the countdown or also refills the damage still to come ([U-0116](../unknowns.md#u-0116)). It is open whether a step blocked by a Shield or Safety bubble counts as damage done or just delays the poison ([U-0117](../unknowns.md#u-0117)). It is open whether sleeping in your own Sleeping Bag prevents new poison, blocks ticks, or both ([U-0118](../unknowns.md#u-0118)). Whether a mirrored poison goes through the attacker's own protections is open too ([U-0005](../unknowns.md#u-0005)).

This page gathers 13 rules (6 `DOCUMENTED`, 7 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0136"></a>

### M-0136: Shield or Safety bubble blocks each poison step, not the landing

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0136](../rules/poison.md#m-0136) `wiki-damage-056`: "A Shield or a Safety Bubble does not stop poison from landing, but blocks each poison step while it lasts." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0136](../rules/poison.md#m-0136) reading A: `poisoned := true on hit; each poison tick is blocked while Shield or Safety bubble is active`

**Interactions:** [M-0179](../rules/poison.md#m-0179)

**Open questions:**

- [U-0117](../unknowns.md#u-0117) (high): A Shield or Safety bubble 'blocks each poison step while it lasts': is a blocked step consumed (counts toward 'all its damage') or skipped (poison extended)? Does the countdown continue while protected?

Notes ([M-0136](../rules/poison.md#m-0136)): Same as the Poison page immunity text ([M-0179](../rules/poison.md#m-0179)).

<a id="m-0170"></a>

### M-0170: Poison tick: 1 HP every 1min 30s

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0170](../rules/poison.md#m-0170) `wiki-poison-001`: "Poison damages you for 1 HP every 1min 30s." ([source](https://iceposeidon.com/safezone/wiki/poison))

**Formal model:**

- [M-0170](../rules/poison.md#m-0170) reading A: `while poisoned: HP loss 1 at t_p = 90, 180, ...`
- [M-0170](../rules/poison.md#m-0170) reading B: `first loss at t_p = 0`
- [M-0170](../rules/poison.md#m-0170) domain: t_p seconds since poisoning
- [M-0170](../rules/poison.md#m-0170) parameter `tick_hp`: 1
- [M-0170](../rules/poison.md#m-0170) parameter `interval_s`: 90

**Consequences:** [T-0304](../theorems/T-0304.md), [T-0305](../theorems/T-0305.md)

**Open questions:**

- [U-0115](../unknowns.md#u-0115) (medium): Poison: does the first 1 HP land at once, after 1min 30s, or on a fixed global 90 s phase?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0170](../rules/poison.md#m-0170)): Equals 20 HP per 30 min, matching the other page that says a Poison Dart poisons for 20 HP over 30min (a derivation for later, not asserted here). Kick reduction is moot at 1 HP (min 1 only if poison is a hit, [U-0002](../unknowns.md#u-0002)).

<a id="m-0171"></a>

### M-0171: Re-poisoning resets the timer and does not stack

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0171](../rules/poison.md#m-0171) `wiki-poison-002`: "Getting poisoned again resets the timer, it doesn't stack." ([source](https://iceposeidon.com/safezone/wiki/poison))

**Formal model:**

- [M-0171](../rules/poison.md#m-0171) reading A: `poison again: countdown := 90 s; damage_remaining unchanged`
- [M-0171](../rules/poison.md#m-0171) reading B: `countdown := 90 s and damage_remaining := total`
- [M-0171](../rules/poison.md#m-0171) parameter `total_hp`: UNKNOWN, see [U-0116](../unknowns.md#u-0116)

**Consequences:** [T-0009](../theorems/T-0009.md)

**Open questions:**

- [U-0116](../unknowns.md#u-0116) (high): Poison 'Getting poisoned again resets the timer, it doesn't stack': does the reset only restart the 90 s countdown, or also restore the total damage still to be dealt? What is the total?

<a id="m-0172"></a>

### M-0172: Poison ends when all damage is done or when cured

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0172](../rules/poison.md#m-0172) `wiki-poison-003`: "Poison ends only when it has done all its damage, or if it is cured." ([source](https://iceposeidon.com/safezone/wiki/poison))

**Formal model:**

- [M-0172](../rules/poison.md#m-0172) reading A: `poisoned := false iff damage_dealt = total or cure event`
- [M-0172](../rules/poison.md#m-0172) parameter `total_hp`: UNKNOWN, see [U-0116](../unknowns.md#u-0116)

**Open questions:**

- [U-0116](../unknowns.md#u-0116) (high): Poison 'Getting poisoned again resets the timer, it doesn't stack': does the reset only restart the 90 s countdown, or also restore the total damage still to be dealt? What is the total?
- [U-0117](../unknowns.md#u-0117) (high): A Shield or Safety bubble 'blocks each poison step while it lasts': is a blocked step consumed (counts toward 'all its damage') or skipped (poison extended)? Does the countdown continue while protected?

Notes ([M-0172](../rules/poison.md#m-0172)): Whether a blocked tick counts as damage done is [U-0117](../unknowns.md#u-0117).

<a id="m-0173"></a>

### M-0173: Poison sources: Poison dart and Fake gravestone

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0173](../rules/poison.md#m-0173) `wiki-poison-004`: "You can be poisoned by a Poison dart or a Fake gravestone." ([source](https://iceposeidon.com/safezone/wiki/poison))

**Formal model:**

- [M-0173](../rules/poison.md#m-0173) reading A: `poison events come from exactly two sources: Poison dart, Fake gravestone`

Notes ([M-0173](../rules/poison.md#m-0173)): Other pages say a zone of effect or another item may poison; this page lists only these two ('can be poisoned by').

<a id="m-0174"></a>

### M-0174: Poison cures: Anti poison, Healing healing, God's Fruit

Label: `DOCUMENTED`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0174](../rules/poison.md#m-0174) `wiki-poison-005`: "Poison can be cured by: Anti poison, Healing healing, or God's Fruit" ([source](https://iceposeidon.com/safezone/wiki/poison))

**Formal model:**

- [M-0174](../rules/poison.md#m-0174) reading A: `cure events: Anti poison, a heal by a Healing contestant, God's Fruit`

Notes ([M-0174](../rules/poison.md#m-0174)): Attribution kept as written: 'Healing healing' = healing by the Healing sigil.

<a id="m-0175"></a>

### M-0175: Protection sigil fully immune to poison

Label: `DOCUMENTED`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0175](../rules/poison.md#m-0175) `wiki-poison-006`: "Protection sigil: fully immune" ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0175](../rules/poison.md#m-0175) reading A: `sigil = Protection: poisoned never becomes true`

Notes ([M-0175](../rules/poison.md#m-0175)): The damage table Poison row lists Protection: consistent.

<a id="m-0176"></a>

### M-0176: Anti poison: no new poison while it lasts

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0176](../rules/poison.md#m-0176) `wiki-poison-007`: "Anti poison: no new poison while it lasts." ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0176](../rules/poison.md#m-0176) reading A: `while Anti poison active: new poison events ignored; existing poison unaffected by this clause`

Notes ([M-0176](../rules/poison.md#m-0176)): Cure and immunity: the items page says the Anti poison cures poison and gives 10 min immunity; this page lists the cure separately ([M-0174](../rules/poison.md#m-0174)). Duration is on the items page.

<a id="m-0177"></a>

### M-0177: Reality Shield: no new poison while standing inside it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0177](../rules/poison.md#m-0177) `wiki-poison-008`: "Reality Shield: no new poison while you stand inside it." ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0177](../rules/poison.md#m-0177) reading A: `position inside Reality Shield: new poison events ignored`

<a id="m-0178"></a>

### M-0178: Sleeping in your own Sleeping Bag (poison immunity list)

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0178](../rules/poison.md#m-0178) `wiki-poison-009`: "Sleeping in your own Sleeping Bag" ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0178](../rules/poison.md#m-0178) reading A: `asleep in own bag: no new poison`
- [M-0178](../rules/poison.md#m-0178) reading B: `asleep in own bag: poison ticks blocked`
- [M-0178](../rules/poison.md#m-0178) reading C: `both`

**Open questions:**

- [U-0118](../unknowns.md#u-0118) (low): 'Sleeping in your own Sleeping Bag' appears as a label in the Poison immunity list with no verb: does it prevent new poison, block each step, or both?

Notes ([M-0178](../rules/poison.md#m-0178)): Label only, no verb in the snapshot.

<a id="m-0179"></a>

### M-0179: Shield or Safety bubble does not stop poisoning but blocks its damage

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0179](../rules/poison.md#m-0179) `wiki-poison-010`: "A Shield or a Safety bubble does not stop you from being poisoned, but blocks the poison damage" ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0179](../rules/poison.md#m-0179) reading A: `poison events are accepted; ticks blocked while Shield or Safety bubble active`

**Interactions:** [M-0136](../rules/poison.md#m-0136)

**Open questions:**

- [U-0117](../unknowns.md#u-0117) (high): A Shield or Safety bubble 'blocks each poison step while it lasts': is a blocked step consumed (counts toward 'all its damage') or skipped (poison extended)? Does the countdown continue while protected?

Notes ([M-0179](../rules/poison.md#m-0179)): Same as the damage page note ([M-0136](../rules/poison.md#m-0136)): no mismatch found.

<a id="m-0180"></a>

### M-0180: Mirror forcefield turns Poison Dart or fake gravestone back on the attacker

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0180](../rules/poison.md#m-0180) `wiki-poison-011`: "A Mirror forcefield turns a Poison Dart or a fake gravestone back on the attacker." ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0180](../rules/poison.md#m-0180) reading A: `defender mirror active and source in {Poison Dart, fake gravestone}: the attacker is poisoned, defender is not`

**Interactions:** [M-0120](../rules/damage.md#m-0120), [M-0135](../rules/damage.md#m-0135)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0180](../rules/poison.md#m-0180)): The items page adds that against an attacker with a mirror the dart still poisons the attacker and their mirror stays. Not duplicated.

<a id="m-0221"></a>

### M-0221: Anti poison

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0221](../rules/poison.md#m-0221) `wiki-items-033`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#anti_poison))
- [M-0221](../rules/poison.md#m-0221) `wiki-items-034`: "Cures poison and makes you immune to it for 10min." ([source](https://iceposeidon.com/safezone/wiki/items#anti_poison))
- [M-0221](../rules/poison.md#m-0221) `wiki-poison-007`: "Anti poison: no new poison while it lasts." ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0221](../rules/poison.md#m-0221) reading A: `on use: current poison is cured; for 10min no new poison can be applied`
- [M-0221](../rules/poison.md#m-0221) domain: t in [0, 600) seconds
- [M-0221](../rules/poison.md#m-0221) parameter `duration`: 10min

**Interactions:** [M-0205](../rules/items.md#m-0205)

## Simulation check

Theorems with tests in `sim/tests/`: [T-0009](../theorems/T-0009.md), [T-0304](../theorems/T-0304.md), [T-0305](../theorems/T-0305.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0005](../unknowns.md#u-0005), [U-0115](../unknowns.md#u-0115), [U-0116](../unknowns.md#u-0116), [U-0117](../unknowns.md#u-0117), [U-0118](../unknowns.md#u-0118)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
