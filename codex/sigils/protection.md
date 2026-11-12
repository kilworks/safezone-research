# Sigil of Protection

## Summary

Rules that name the Sigil of Protection, as the wiki states them on 2026-11-11.

### In plain words

Protection is the "tank" class. Its stats are the plain ones, 100 maximum HP and 3 inventory slots ([M-0605](../rules/sigil.md#m-0605)), but it comes with the longest immunity list in the game: poison, drones, missiles, C4, landmines, trapped gifts, airstrikes and their fire, gunship bombs and Protection retribution ([M-0640](../rules/sigil.md#m-0640)). Nukes are not blocked, but they deal 50% less to you ([M-0643](../rules/damage.md#m-0643)), rounded down ([M-0121](../rules/damage.md#m-0121)). Poison in particular cannot touch you ([M-0175](../rules/poison.md#m-0175)).

It does not make you invincible. You still take zone, unsafe circle, robot, weapon, fake chest, tear gas, zombie, bleeding, cyclops and bounty damage ([M-0641](../rules/sigil.md#m-0641)). So the sigil is strong against the viewer-driven explosive attacks and poison, and not against a person with a weapon or against the shrinking zone.

The costs are in healing. Potions heal you 50% less ([M-0645](../rules/healing.md#m-0645)), while bandages last 1.1x as long ([M-0646](../rules/healing.md#m-0646)). In exchange, your immunity pays: a drone, missile, C4 or landmine hit earns one blood token, an airstrike or gunship hit earns 1, and a nuke hit earns twenty, but only when your own protection does the blocking ([M-0642](../rules/economy.md#m-0642)).

Two active features turn you into a threat. You can place a landmine where you stand once every 2 hours; it deals 15 HP to everyone within 10 m and kills every zombie in range ([M-0644](../rules/sigil.md#m-0644)). And when you die, everyone within 30 m (98 ft) takes 20 HP ([M-0647](../rules/sigil.md#m-0647)).

What a player would feel: calm while others are being bombed, then pressure from the things that are not blocked. Strongest as written: the immunity list ([M-0640](../rules/sigil.md#m-0640)) and the nuke cut ([M-0643](../rules/damage.md#m-0643)). Weakest: the potion penalty ([M-0645](../rules/healing.md#m-0645)) and the open exposure to zone and weapons ([M-0641](../rules/sigil.md#m-0641)).

What is unknown: whether the 50% potion cut rounds down or up ([U-0618](../unknowns.md#u-0618)), and which heals count as potions ([U-0617](../unknowns.md#u-0617)). It is open whether bandages heal more in total or the same amount over a longer time ([U-0619](../unknowns.md#u-0619)). It is open whether the landmine ability is ready at the pick ([U-0621](../unknowns.md#u-0621)). It is open whether the unlisted blocks pay tokens ([U-0620](../unknowns.md#u-0620)). Where the rounding sits in the damage steps is open ([U-0100](../unknowns.md#u-0100)), and so is how odd nuke damage is rounded ([U-0402](../unknowns.md#u-0402)).

This page gathers 12 rules (5 `DOCUMENTED`, 7 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0121"></a>

### M-0121: Pipeline step 4a: Protection sigil halves nuke damage

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0121](../rules/damage.md#m-0121) `wiki-damage-044`: "A Protection contestant takes 50% less from a nuke." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0121](../rules/damage.md#m-0121) `wiki-damage-045`: "The damage left is rounded down." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0121](../rules/damage.md#m-0121) `wiki-damage-062`: "The Protection sigil is not immune to nukes, but takes 50% less from them." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0121](../rules/damage.md#m-0121) reading A: `if defender sigil is Protection and source is nuke: d := floor(d/2); other sources unchanged`
- [M-0121](../rules/damage.md#m-0121) domain: d integer >= 0
- [M-0121](../rules/damage.md#m-0121) parameter `nuke_reduction`: 50 percent

**Interactions:** [M-0117](../rules/damage.md#m-0117)

**Open questions:**

- [U-0100](../unknowns.md#u-0100) (low): Where does 'The damage left is rounded down' apply in step 4: to the Protection 50% result only, or as one final floor after all reductions, with the Kick 10% computed on the unrounded value?

Notes ([M-0121](../rules/damage.md#m-0121)): 'Not immune to nukes, but takes 50% less'. The Protection page treats the same rule (50% less); no mismatch found. Where the floor applies is [U-0100](../unknowns.md#u-0100). The Flak jacket ([M-0130](../rules/items.md#m-0130)) blocks the nuke before this step.

<a id="m-0175"></a>

### M-0175: Protection sigil fully immune to poison

Label: `DOCUMENTED`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0175](../rules/poison.md#m-0175) `wiki-poison-006`: "Protection sigil: fully immune" ([source](https://iceposeidon.com/safezone/wiki/poison#immunity))

**Formal model:**

- [M-0175](../rules/poison.md#m-0175) reading A: `sigil = Protection: poisoned never becomes true`

Notes ([M-0175](../rules/poison.md#m-0175)): The damage table Poison row lists Protection: consistent.

<a id="m-0407"></a>

### M-0407: Nuke damage cut for the Protection sigil

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0407](../rules/viewer.md#m-0407) `wiki-attacks-016`: "The Protection sigil is not immune, but takes 50% less." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))

**Formal model:**

- [M-0407](../rules/viewer.md#m-0407) reading A: `d -> floor(d/2)`
- [M-0407](../rules/viewer.md#m-0407) reading B: `d -> ceil(d/2)`
- [M-0407](../rules/viewer.md#m-0407) reading C: `d -> d/2`
- [M-0407](../rules/viewer.md#m-0407) domain: d integer HP of the nuke, default 20 gives 10 under all readings

**Interactions:** [M-0405](../rules/viewer.md#m-0405), [M-0406](../rules/viewer.md#m-0406)

**Open questions:**

- [U-0402](../unknowns.md#u-0402) (low): Nuke damage cut for the Protection sigil: '50% less' of 20 HP is 10 HP, but how are odd admin-set damages rounded, and is the cut applied before or after other reductions?

Notes ([M-0407](../rules/viewer.md#m-0407)): Protection is not immune to nukes (unlike missiles). Cross-family: Protection sigil page, damage pipeline order.

<a id="m-0605"></a>

### M-0605: Protection base stats: 100 max HP, 3 inventory slots

Label: `DOCUMENTED`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0605](../rules/sigil.md#m-0605) `wiki-sigils-protection-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/protection))
- [M-0605](../rules/sigil.md#m-0605) `wiki-sigils-protection-003`: "100 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/protection))
- [M-0605](../rules/sigil.md#m-0605) `wiki-sigils-protection-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/protection))
- [M-0605](../rules/sigil.md#m-0605) `wiki-sigils-protection-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/protection))

**Formal model:**

- [M-0605](../rules/sigil.md#m-0605) reading A: `maxHP = 100; inventory_slots = 3`
- [M-0605](../rules/sigil.md#m-0605) domain: start of event
- [M-0605](../rules/sigil.md#m-0605) parameter `max_hp`: 100
- [M-0605](../rules/sigil.md#m-0605) parameter `inventory_slots`: 3

Notes ([M-0605](../rules/sigil.md#m-0605)): Merchant upgrades (+10 max HP, inventory slots) change these during play; this record is the base value only. The merchant page caps slots at 13, or 20 for Endurance.

<a id="m-0640"></a>

### M-0640: Protection immunity list

Label: `DOCUMENTED`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0640](../rules/sigil.md#m-0640) `wiki-sigils-protection-008`: "Immune to poison, drones, missiles, C4, landmines, trapped gifts, airstrikes and their fire, gunship bombs and Protection retribution." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0640](../rules/sigil.md#m-0640) `wiki-sigils-protection-006`: "Immune to" ([source](https://iceposeidon.com/safezone/wiki/sigils/protection))
- [M-0640](../rules/sigil.md#m-0640) `wiki-sigils-protection-007`: "Poison, drones, missiles, C4, landmines, airstrikes, gunships" ([source](https://iceposeidon.com/safezone/wiki/sigils/protection))
- [M-0640](../rules/sigil.md#m-0640) `wiki-damage-008`: "| Poison | Shield, Safety bubble, Sleeping Bag, Protection, Anti poison, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [M-0640](../rules/sigil.md#m-0640) `wiki-damage-018`: "| Drone | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [M-0640](../rules/sigil.md#m-0640) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [M-0640](../rules/sigil.md#m-0640) `wiki-damage-026`: "| Airstrike fire | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [M-0640](../rules/sigil.md#m-0640) `wiki-damage-031`: "| Protection retribution | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0640](../rules/sigil.md#m-0640) reading A: `blocked(source, c) = true for source in {poison, drone, missile, C4, landmine, trapped gift, airstrike impact, airstrike fire, gunship bomb, Protection retribution} when sigil(c) = protection`

**Consequences:** [T-0707](../theorems/T-0707.md)

**Contradictions:** [C-0601](../unknowns.md#c-0601), [C-0602](../unknowns.md#c-0602)

Notes ([M-0640](../rules/sigil.md#m-0640)): The full sentence and the damage table agree. The label line is shorter, see [C-0601](../unknowns.md#c-0601). Mentions of immunity on the attacks page (missile, airstrike, gunship) agree. Nuke is not immune: [M-0643](../rules/damage.md#m-0643).

<a id="m-0641"></a>

### M-0641: Protection still takes zone, circle, robot and weapon damage

Label: `DOCUMENTED`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0641](../rules/sigil.md#m-0641) `wiki-sigils-protection-009`: "Still takes zone, unsafe circle, robot, weapon, fake chest, tear gas, zombie, bleeding, cyclops and bounty damage." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))

**Formal model:**

- [M-0641](../rules/sigil.md#m-0641) reading A: `no Protection blocker for sources {zone, unsafe circle, robot, weapon, fake chest, tear gas, zombie, bleeding, cyclops, bounty}`

**Contradictions:** [C-0602](../unknowns.md#c-0602)

Notes ([M-0641](../rules/sigil.md#m-0641)): Consistent with the damage table, where Protection appears in none of these rows.

<a id="m-0642"></a>

### M-0642: Protection blood tokens from immunity blocks

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0642](../rules/economy.md#m-0642) `wiki-sigils-protection-010`: "A drone, missile, C4 or landmine hit earns one blood token, and an airstrike or gunship hit earns 1, but only when your own immunity blocks it." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0642](../rules/economy.md#m-0642) `wiki-sigils-protection-011`: "A nuke hit earns twenty when your damage cut applies." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0642](../rules/economy.md#m-0642) `wiki-sigils-protection-012`: "A hit already blocked by something else earns nothing." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))

**Formal model:**

- [M-0642](../rules/economy.md#m-0642) reading A: `tokens += 1 per blocked hit of {drone, missile, C4, landmine, airstrike, gunship}; += 20 per nuke hit that reaches the 50% reduction; += 0 if another blocker already stopped the hit`
- [M-0642](../rules/economy.md#m-0642) reading B: `A plus airstrike fire ticks pay`
- [M-0642](../rules/economy.md#m-0642) parameter `tokens_per_block`: 1
- [M-0642](../rules/economy.md#m-0642) parameter `tokens_per_nuke`: 20

**Interactions:** [M-0640](../rules/sigil.md#m-0640), [M-0643](../rules/damage.md#m-0643)

**Open questions:**

- [U-0620](../unknowns.md#u-0620) (medium): Protection blood tokens from blocked hits: do airstrike fire ticks, a landmine of its own, and the unlisted immunities (trapped gift, poison, retribution) pay tokens?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0642](../rules/economy.md#m-0642)): Poison, trapped gift and Protection retribution are in the immunity list but not in the token list. The nuke bonus is 20 tokens. Whether a sigil landmine of its own pays is not stated.

<a id="m-0643"></a>

### M-0643: Protection takes 50% less from nukes

Label: `DOCUMENTED`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0643](../rules/damage.md#m-0643) `wiki-sigils-protection-013`: "Nukes deal 50% less damage to you." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0643](../rules/damage.md#m-0643) `wiki-damage-044`: "A Protection contestant takes 50% less from a nuke." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0643](../rules/damage.md#m-0643) `wiki-damage-045`: "The damage left is rounded down." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0643](../rules/damage.md#m-0643) `wiki-attacks-016`: "The Protection sigil is not immune, but takes 50% less." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))

**Formal model:**

- [M-0643](../rules/damage.md#m-0643) reading A: `d -> floor(d/2) (reduction step 4, before the Kick live reduction)`
- [M-0643](../rules/damage.md#m-0643) domain: d integer

**Contradictions:** [C-0602](../unknowns.md#c-0602)

Notes ([M-0643](../rules/damage.md#m-0643)): Order against the Kick live reduction and the 1 HP minimum is given by the damage page (steps 4 and 5). Where the Kick 10% applies, see [U-0001](../unknowns.md#u-0001).

<a id="m-0644"></a>

### M-0644: Protection landmine placement ability

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0644](../rules/sigil.md#m-0644) `wiki-sigils-protection-014`: "Place a landmine where you stand once every 2h." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0644](../rules/sigil.md#m-0644) `wiki-sigils-protection-015`: "It deals 15 HP to everyone within 10m (33ft) when another contestant or a zombie steps in, and kills every zombie in range." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0644](../rules/sigil.md#m-0644) `wiki-weapons-021`: "It deals 15 HP to everyone in range, you included, and kills every zombie in range." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))

**Formal model:**

- [M-0644](../rules/sigil.md#m-0644) reading A: `every 7200 s the contestant may place a landmine at their position; trigger when another contestant or a zombie is within 10 m; deals 15 HP to everyone within 10 m; kills zombies within 10 m`
- [M-0644](../rules/sigil.md#m-0644) domain: seconds, metres, HP
- [M-0644](../rules/sigil.md#m-0644) parameter `cooldown_s`: 7200
- [M-0644](../rules/sigil.md#m-0644) parameter `damage_hp`: 15
- [M-0644](../rules/sigil.md#m-0644) parameter `radius_m`: 10

**Open questions:**

- [U-0621](../unknowns.md#u-0621) (medium): Protection landmine ability: ready at the sigil pick or after 2h, does the 2h start at placement, and is it the item Landmine (stack of 5, Kick live bonus, enchant, visibility)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0644](../rules/sigil.md#m-0644)): The 15 HP and 10 m match the item landmine. Protection is itself immune to landmines, so its own mine does not hurt it.

<a id="m-0645"></a>

### M-0645: Protection potions heal 50% less

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0645](../rules/healing.md#m-0645) `wiki-sigils-protection-016`: "Potions heal you 50% less." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))

**Formal model:**

- [M-0645](../rules/healing.md#m-0645) reading A: `heal -> floor(h/2)`
- [M-0645](../rules/healing.md#m-0645) reading B: `heal -> ceil(h/2)`
- [M-0645](../rules/healing.md#m-0645) reading C: `heal -> h/2 exact`
- [M-0645](../rules/healing.md#m-0645) domain: h integer: health potion tiers 5, 10, 20, 40; Eddie's potion 50% of max HP

**Consequences:** [T-0402](../theorems/T-0402.md)

**Open questions:**

- [U-0617](../unknowns.md#u-0617) (high): Protection 'Potions heal you 50% less': which heals are 'potions' (health potions, Eddie's potion, God's Fruit, bandages, healing circle)?
- [U-0618](../unknowns.md#u-0618) (low): Protection potion heal 'less 50%': rounding when the tier is odd (Small potion 5 HP)?

Notes ([M-0645](../rules/healing.md#m-0645)): Scope (which items count as potions) is [U-0617](../unknowns.md#u-0617).

<a id="m-0646"></a>

### M-0646: Protection bandages last 1.1x as long

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0646](../rules/healing.md#m-0646) `wiki-sigils-protection-017`: "Bandages last 1.1x as long." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0646](../rules/healing.md#m-0646) `wiki-items-049`: "Heals 10 HP over 2min." ([source](https://iceposeidon.com/safezone/wiki/items#bandage))

**Formal model:**

- [M-0646](../rules/healing.md#m-0646) reading A: `bandage: 10 HP total over 132 s`
- [M-0646](../rules/healing.md#m-0646) reading B: `bandage: 11 HP total over 132 s at the old rate`
- [M-0646](../rules/healing.md#m-0646) domain: seconds, HP
- [M-0646](../rules/healing.md#m-0646) parameter `duration_factor`: 1.1
- [M-0646](../rules/healing.md#m-0646) parameter `base_duration_s`: 120

**Open questions:**

- [U-0619](../unknowns.md#u-0619) (medium): Protection 'Bandages last 1.1x as long': same total heal over a longer time, or same rate over a longer time?

Notes ([M-0646](../rules/healing.md#m-0646)): Cross reference: the bandage item page (heals 10 HP over 2 min).

<a id="m-0647"></a>

### M-0647: Protection retribution on death

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0647](../rules/sigil.md#m-0647) `wiki-sigils-protection-018`: "Retribution: when you die, everyone within 30m (98ft) of you takes 20 HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0647](../rules/sigil.md#m-0647) `wiki-damage-031`: "| Protection retribution | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0647](../rules/sigil.md#m-0647) reading A: `on death of a Protection contestant: every other contestant within 30 m takes 20 HP (blockers of the damage table apply)`
- [M-0647](../rules/sigil.md#m-0647) domain: metres, HP
- [M-0647](../rules/sigil.md#m-0647) parameter `radius_m`: 30
- [M-0647](../rules/sigil.md#m-0647) parameter `damage_hp`: 20

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0647](../rules/sigil.md#m-0647)): Other Protection contestants are immune. Whether a Protection contestant revived later is unaffected is not stated. Whether the killer or the dying contestant is included is not stated.

## Simulation check

Theorems with tests in `sim/tests/`: [T-0402](../theorems/T-0402.md), [T-0707](../theorems/T-0707.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0100](../unknowns.md#u-0100), [U-0402](../unknowns.md#u-0402), [U-0617](../unknowns.md#u-0617), [U-0618](../unknowns.md#u-0618), [U-0619](../unknowns.md#u-0619), [U-0620](../unknowns.md#u-0620), [U-0621](../unknowns.md#u-0621)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
