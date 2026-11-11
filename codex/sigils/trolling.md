# Sigil of Trolling

## Summary

Rules that name the Sigil of Trolling, as the wiki states them on 2026-11-11.

### In plain words

Trolling is the "prankster" class. It has plain stats, 100 maximum HP and 3 inventory slots ([M-0530](../rules/sigil.md#m-0530)), and its whole identity is making other people's lives annoying, then getting paid for the damage ([M-0531](../rules/economy.md#m-0531)).

The pranks come in three kinds. The fake chest looks like a care package; you can place up to 2 per rolling hour and each vanishes after 1 hour ([M-0532](../rules/items.md#m-0532)). Whoever claims it takes 5 HP damage and cannot claim chests for 1 hour, while you heal 5 HP; a Shield blocks the damage but not the lockout ([M-0533](../rules/damage.md#m-0533)). If the victim has a Mirror, the reflected fake chest locks you out instead ([M-0238](../rules/items.md#m-0238)). The fake gravestone copies the gravestone of an eliminated contestant, and each contestant who tries to loot it is poisoned once; you place one, then wait 2 hours ([M-0534](../rules/items.md#m-0534)). The unsafe circle is a 50 m (164 ft) circle you can place inside a safe zone for 20 minutes, with a 2 hour cooldown, and nobody alive, you included, may be inside when you place it ([M-0535](../rules/zone.md#m-0535)).

Inside the circle, anyone also inside a safe zone takes 1 HP every 2 seconds with no grace period ([M-0536](../rules/damage.md#m-0536)). After the first hit, they also lose one random defense item or unique craft every five seconds while they stay inside and are not immune ([M-0537](../rules/items.md#m-0537)). Guardian angel, Safety bubble, Reality Shield and Death Ward block it, and a Shield does not ([M-0538](../rules/damage.md#m-0538)).

You also earn blood tokens: one per 5 HP dealt to other players and one per crate destroyed ([M-0531](../rules/economy.md#m-0531)). And viewers' care packages have a 3% chance to land next to you instead ([M-0539](../rules/viewer.md#m-0539)).

Strongest as written: the circle turns a safe zone into a place where defenses wear away ([M-0537](../rules/items.md#m-0537)), and the fake chest costs victims both HP and chest access ([M-0533](../rules/damage.md#m-0533)). Weakest: it has no stat bonus ([M-0530](../rules/sigil.md#m-0530)), and a victim with the right defense simply ignores the circle ([M-0538](../rules/damage.md#m-0538)).

What is unknown: the wiki disagrees on whether a Reality Shield stops the circle ([M-0538](../rules/damage.md#m-0538), [C-0502](../unknowns.md#c-0502)). It also disagrees about whether the 3% diversion covers any care package or only viewer ones ([M-0432](../rules/viewer.md#m-0432), [C-0403](../unknowns.md#c-0403)). Open questions include whether 50 m is a radius or a diameter ([U-0535](../unknowns.md#u-0535)), whether the cooldown starts at placement ([U-0536](../unknowns.md#u-0536)), what exactly counts as damage dealt for tokens ([U-0529](../unknowns.md#u-0529)), whether fake chest placements slide or refill ([U-0530](../unknowns.md#u-0530)), and what the lockout also blocks ([U-0531](../unknowns.md#u-0531)).

This page gathers 12 rules (2 `DOCUMENTED`, 9 `CONDITIONAL`, 1 `UNKNOWN`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0238"></a>

### M-0238: Mirror reflects a fake chest

Label: `DOCUMENTED`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0238](../rules/items.md#m-0238) `wiki-items-056`: "A reflected fake chest also locks the troll out of chests instead of you." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))

**Formal model:**

- [M-0238](../rules/items.md#m-0238) reading A: `a reflected fake chest locks the troll out of chests, not the target`
- [M-0238](../rules/items.md#m-0238) domain: fake chest event

**Interactions:** [M-0237](../rules/items.md#m-0237)

<a id="m-0432"></a>

### M-0432: Care package Trolling diversion

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0432](../rules/viewer.md#m-0432) `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))

**Formal model:**

- [M-0432](../rules/viewer.md#m-0432) reading A: `each care package: with probability 0.03 it lands within 5m of a Trolling contestant instead`
- [M-0432](../rules/viewer.md#m-0432) domain: p = 3%, distance <= 5 m
- [M-0432](../rules/viewer.md#m-0432) parameter `p`: 0.03
- [M-0432](../rules/viewer.md#m-0432) parameter `radius`: 5 m

**Interactions:** [M-0431](../rules/viewer.md#m-0431)

**Open questions:**

- [U-0411](../unknowns.md#u-0411) (medium): Care package Trolling rule: does the 3% roll apply to each package separately (including the 5 of an emergency airdrop, Endurance packages and merchant packages), is 'within 5m' the same as 'next to', and which Trolling contestant is chosen when several exist?

**Contradictions:** [C-0403](../unknowns.md#c-0403)

Notes ([M-0432](../rules/viewer.md#m-0432)): Trolling page wording: 'Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead' ([C-0403](../unknowns.md#c-0403)).

<a id="m-0530"></a>

### M-0530: Trolling base max HP and inventory slots

Label: `DOCUMENTED`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0530](../rules/sigil.md#m-0530) `wiki-sigils-trolling-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling))
- [M-0530](../rules/sigil.md#m-0530) `wiki-sigils-trolling-003`: "100 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling))
- [M-0530](../rules/sigil.md#m-0530) `wiki-sigils-trolling-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling))
- [M-0530](../rules/sigil.md#m-0530) `wiki-sigils-trolling-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling))

**Formal model:**

- [M-0530](../rules/sigil.md#m-0530) reading A: `maxHP_trolling = 100; slots_trolling = 3`
- [M-0530](../rules/sigil.md#m-0530) domain: integer HP and slot counts at event start
- [M-0530](../rules/sigil.md#m-0530) parameter `max_hp`: 100
- [M-0530](../rules/sigil.md#m-0530) parameter `slots`: 3

Notes ([M-0530](../rules/sigil.md#m-0530)): Labels read in pairs (Max HP then 100 HP, Slots then 3).

<a id="m-0531"></a>

### M-0531: Trolling blood token income

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0531](../rules/economy.md#m-0531) `wiki-sigils-trolling-006`: "Earn one blood token per 5 HP dealt to other players and per crate destroyed, whoever spawned it." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))

**Formal model:**

- [M-0531](../rules/economy.md#m-0531) reading A: `tokens += floor(D_total / 5) over cumulative HP lost by other players because of the contestant, plus 1 per crate destroyed whoever spawned it`
- [M-0531](../rules/economy.md#m-0531) reading B: `tokens += floor(d / 5) per hit, remainder discarded`
- [M-0531](../rules/economy.md#m-0531) reading C: `D counts the nominal hit before armor, fortress and Kick reduction`
- [M-0531](../rules/economy.md#m-0531) reading D: `periodic damage from the contestant's traps counts or not, per [U-0529](../unknowns.md#u-0529)`
- [M-0531](../rules/economy.md#m-0531) domain: d integer HP per hit; crate count integer
- [M-0531](../rules/economy.md#m-0531) parameter `hp_per_token`: 5
- [M-0531](../rules/economy.md#m-0531) parameter `tokens_per_crate`: 1
- [M-0531](../rules/economy.md#m-0531) parameter `hp_basis`: UNKNOWN, see [U-0528](../unknowns.md#u-0528)
- [M-0531](../rules/economy.md#m-0531) parameter `source_scope`: UNKNOWN, see [U-0529](../unknowns.md#u-0529)

**Interactions:** [M-0528](../rules/items.md#m-0528), [M-0533](../rules/damage.md#m-0533), [M-0536](../rules/damage.md#m-0536)

**Open questions:**

- [U-0528](../unknowns.md#u-0528) (high): Trolling 'one blood token per 5 HP dealt to other players': is the remainder carried, and is 'dealt' the nominal hit or the HP that actually got through (after armor, fortress, Kick reduction)?
- [U-0529](../unknowns.md#u-0529) (high): Trolling income scope: which damage counts as 'HP dealt to other players' (weapons, fake chest, unsafe circle ticks, poison from the fake gravestone, reflected hits), and which crates count as 'crate destroyed, whoever spawned it'?
- [U-0001](../unknowns.md#u-0001) (critical): Does the defender's Kick-live 10% reduction floor the result (A) or the removed 10% (B)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0531](../rules/economy.md#m-0531)): 'other players' excludes the Trolling contestant and zombies. A fake chest claim deals 5 HP, a Kick-live defender takes 4 or 5 depending on [U-0001](../unknowns.md#u-0001), so one claim may pay 0 or 1 token depending on readings.

<a id="m-0532"></a>

### M-0532: Fake chest placement

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0532](../rules/items.md#m-0532) `wiki-sigils-trolling-007`: "Fake chest: place up to 2 per rolling hour." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0532](../rules/items.md#m-0532) `wiki-sigils-trolling-008`: "It looks like a care package." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0532](../rules/items.md#m-0532) `wiki-sigils-trolling-011`: "It vanishes after 1h." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))

**Formal model:**

- [M-0532](../rules/items.md#m-0532) reading A: `place(fake chest) allowed iff fewer than 2 placements in the previous 3600 s; it looks like a care package; it vanishes 3600 s after placement`
- [M-0532](../rules/items.md#m-0532) reading B: `two charges regained one per 1800 s`
- [M-0532](../rules/items.md#m-0532) reading C: `2 per clock hour`
- [M-0532](../rules/items.md#m-0532) domain: time in seconds
- [M-0532](../rules/items.md#m-0532) parameter `limit`: 2
- [M-0532](../rules/items.md#m-0532) parameter `window_s`: 3600
- [M-0532](../rules/items.md#m-0532) parameter `lifetime_s`: 3600
- [M-0532](../rules/items.md#m-0532) parameter `limit_semantics`: UNKNOWN, see [U-0530](../unknowns.md#u-0530)

**Interactions:** [M-0517](../rules/sigil.md#m-0517), [M-0533](../rules/damage.md#m-0533)

**Open questions:**

- [U-0530](../unknowns.md#u-0530) (medium): Fake chest 'up to 2 per rolling hour': sliding window over placement times, or two charges that refill?

Notes ([M-0532](../rules/items.md#m-0532)): Since it lasts 1 h, the active count under reading A is at most 2. Only Ingenuity recognizes fakes ([M-0517](../rules/sigil.md#m-0517)). Location constraints and the item shown are not stated.

<a id="m-0533"></a>

### M-0533: Fake chest claim effect

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-009`: "A contestant who claims it takes 5 HP damage and cannot claim chests for 1h." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-010`: "You heal 5 HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-012`: "A Shield blocks the damage but not the lockout." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0533](../rules/damage.md#m-0533) `wiki-items-056`: "A reflected fake chest also locks the troll out of chests instead of you." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))

**Formal model:**

- [M-0533](../rules/damage.md#m-0533) reading A: `claim(fake chest by contestant v): v takes 5 HP through the hit pipeline (Kick bonus applies to the troll's hit, reductions apply to v); v cannot claim chests for 3600 s; the troll heals 5 HP; a Shield blocks the damage but not the lockout`
- [M-0533](../rules/damage.md#m-0533) reading B: `troll heals only when damage is not blocked`
- [M-0533](../rules/damage.md#m-0533) reading C: `lockout covers care packages and crates too`
- [M-0533](../rules/damage.md#m-0533) domain: damage integer 5 before modifiers; lockout 3600 s
- [M-0533](../rules/damage.md#m-0533) parameter `damage_hp`: 5
- [M-0533](../rules/damage.md#m-0533) parameter `lockout_s`: 3600
- [M-0533](../rules/damage.md#m-0533) parameter `troll_heal_hp`: 5
- [M-0533](../rules/damage.md#m-0533) parameter `lockout_scope`: UNKNOWN, see [U-0531](../unknowns.md#u-0531)
- [M-0533](../rules/damage.md#m-0533) parameter `heal_condition`: UNKNOWN, see [U-0532](../unknowns.md#u-0532)

**Interactions:** [M-0504](../rules/items.md#m-0504), [M-0531](../rules/economy.md#m-0531), [M-0532](../rules/items.md#m-0532)

**Open questions:**

- [U-0531](../unknowns.md#u-0531) (medium): Fake chest lockout 'cannot claim chests for 1h': does it block care packages and crates too, does a second claim extend it, and do blockers other than a Shield (Safety bubble, Sleeping Bag, Body armor) also leave it standing?
- [U-0532](../unknowns.md#u-0532) (medium): Trolling fake chest 'You heal 5 HP': fixed 5 HP at claim time, or the damage that actually landed, and does it happen when the victim is protected or the chest is reflected?
- [U-0001](../unknowns.md#u-0001) (critical): Does the defender's Kick-live 10% reduction floor the result (A) or the removed 10% (B)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0533](../rules/damage.md#m-0533)): Damage page row: fake chest is stopped by Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects) and Body armor (absorbs); the Kick bonus list includes the fake chest. Protection contestants still take fake chest damage. With a Mirror forcefield the whole effect returns to the troll including the lockout (items page).

<a id="m-0534"></a>

### M-0534: Fake gravestone

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0534](../rules/items.md#m-0534) `wiki-sigils-trolling-013`: "Fake gravestone: place one, then wait 2h before the next." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0534](../rules/items.md#m-0534) `wiki-sigils-trolling-014`: "It copies the gravestone of an eliminated contestant, or of a random living one while nobody is eliminated." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0534](../rules/items.md#m-0534) `wiki-sigils-trolling-015`: "Each contestant who tries to loot it is poisoned once." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))

**Formal model:**

- [M-0534](../rules/items.md#m-0534) reading A: `place at most one; next placement allowed 7200 s after placement; copy = gravestone of an eliminated contestant chosen by the troll, else a random living contestant's if nobody is eliminated; each contestant who tries to loot it is poisoned once (first attempt only)`
- [M-0534](../rules/items.md#m-0534) reading B: `2 h wait counted from the moment the previous fake disappears`
- [M-0534](../rules/items.md#m-0534) reading C: `copy chosen at random among eliminated contestants`
- [M-0534](../rules/items.md#m-0534) domain: time in seconds
- [M-0534](../rules/items.md#m-0534) parameter `cooldown_s`: 7200
- [M-0534](../rules/items.md#m-0534) parameter `lifetime_s`: UNKNOWN, see [U-0533](../unknowns.md#u-0533)
- [M-0534](../rules/items.md#m-0534) parameter `copy_source`: UNKNOWN, see [U-0534](../unknowns.md#u-0534)
- [M-0534](../rules/items.md#m-0534) parameter `poison`: once per contestant

**Interactions:** [M-0517](../rules/sigil.md#m-0517)

**Open questions:**

- [U-0533](../unknowns.md#u-0533) (medium): Fake gravestone: how long does it last, and does the 2 h wait start at placement or when the previous one disappears?
- [U-0534](../unknowns.md#u-0534) (low): Fake gravestone copy source: when someone is eliminated, who chooses which eliminated contestant is copied?

Notes ([M-0534](../rules/items.md#m-0534)): Poison details (1 HP every 1 min 30 s, resets, does not stack) are on the poison page; a fake gravestone is one of the two poisoning sources there. A Mirror forcefield turns it back on the attacker. Ingenuity recognizes fakes. Death-sigil robbing of a fake gravestone is not described.

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

<a id="m-0536"></a>

### M-0536: Unsafe circle damage

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-017`: "Anyone inside it who is also inside a safe zone takes zone damage with no grace period" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-022`: "It hurts like the outside of the safe zone: 1 HP every 2s, first hit one interval after you enter, with no grace period." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-023`: "Only the part inside a safe zone hurts: outside every safe zone you take normal zone damage only." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))

**Formal model:**

- [M-0536](../rules/damage.md#m-0536) reading A: `for contestant v in circle and in a safe zone: after 2 s inside, 1 HP every 2 s; no 5 s grace; outside every safe zone only normal zone damage (first tick after the ordinary grace)`
- [M-0536](../rules/damage.md#m-0536) reading B: `timer persists across moving between the inside-zone and outside-zone parts`
- [M-0536](../rules/damage.md#m-0536) reading C: `global 2 s ticks`
- [M-0536](../rules/damage.md#m-0536) domain: t >= 0 s since entry; 1 HP per tick
- [M-0536](../rules/damage.md#m-0536) parameter `interval_s`: 2
- [M-0536](../rules/damage.md#m-0536) parameter `damage_hp`: 1
- [M-0536](../rules/damage.md#m-0536) parameter `grace_s`: 0
- [M-0536](../rules/damage.md#m-0536) parameter `first_hit`: one interval after entry

**Interactions:** [M-0537](../rules/items.md#m-0537), [M-0538](../rules/damage.md#m-0538)

**Open questions:**

- [U-0537](../unknowns.md#u-0537) (high): Unsafe circle damage clock: is the first hit 2 s after each entry (timer resets on exit) or does a global 2 s phase continue? Does moving between the part of the circle inside a safe zone and the outside part reset it?
- [U-0003](../unknowns.md#u-0003) (medium): Zone damage: is the first tick at 5 s or at 7 s after leaving the safe zone?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0536](../rules/damage.md#m-0536)): Hazmat suit lengthens each zone damage interval by 2 s (items page) and the damage page lists it as slowing unsafe circle damage; Body armor absorbs. The ordinary zone damage first tick is [U-0003](../unknowns.md#u-0003).

<a id="m-0537"></a>

### M-0537: Unsafe circle defense item loss

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-017`: "loses one defense item or unique craft every five seconds, equipped Body Armor included" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-024`: "After your first hit, you lose one random defense item or unique craft every five seconds while you stay inside and are not immune." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-025`: "Defense items are Shields, Safety Bubbles, Guardian Angels, Hazmat Suits, Body Armor, Mirror Forcefields, Flak Jackets, Gas Masks, Zombie Repellents, Anti Poisons and Sleeping Bags." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0537](../rules/items.md#m-0537) `wiki-sigils-trolling-026`: "Equipped Body Armor is not safe." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))

**Formal model:**

- [M-0537](../rules/items.md#m-0537) reading A: `from the first hit, every 5 s while inside and not immune: remove one random item from {Shield, Safety Bubble, Guardian Angel, Hazmat Suit, Body Armor, Mirror Forcefield, Flak Jacket, Gas Mask, Zombie Repellent, Anti Poison, Sleeping Bag} or a unique craft; first loss at t_hit + 5 s`
- [M-0537](../rules/items.md#m-0537) reading B: `first loss at the first hit`
- [M-0537](../rules/items.md#m-0537) reading C: `clock from entry`
- [M-0537](../rules/items.md#m-0537) domain: 5 s period; random uniform over the held qualifying items (distribution not stated)
- [M-0537](../rules/items.md#m-0537) parameter `period_s`: 5
- [M-0537](../rules/items.md#m-0537) parameter `defense_item_types`: 11
- [M-0537](../rules/items.md#m-0537) parameter `fate`: UNKNOWN, see [U-0539](../unknowns.md#u-0539)
- [M-0537](../rules/items.md#m-0537) parameter `clock_start`: UNKNOWN, see [U-0538](../unknowns.md#u-0538)

**Interactions:** [M-0536](../rules/damage.md#m-0536)

**Open questions:**

- [U-0538](../unknowns.md#u-0538) (high): Unsafe circle item loss: when does the first loss happen relative to entry and to the first hit?
- [U-0539](../unknowns.md#u-0539) (medium): Unsafe circle item loss: is the lost item destroyed or dropped, does 'not immune' pause the clock or just skip the loss, and are active effects (not inventory) affected?

**Contradictions:** [C-0503](../unknowns.md#c-0503)

Notes ([M-0537](../rules/items.md#m-0537)): Equipped Body Armor is explicitly not safe. The defense list excludes the sigil abilities Reality Shield and Death Ward. Uniformity of the random choice is not stated.

<a id="m-0538"></a>

### M-0538: Unsafe circle blockers

Label: `UNKNOWN`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0538](../rules/damage.md#m-0538) `wiki-sigils-trolling-027`: "A Guardian angel, a Safety bubble, a Reality Shield or a Death Ward blocks it." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0538](../rules/damage.md#m-0538) `wiki-sigils-trolling-028`: "A Shield does not." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0538](../rules/damage.md#m-0538) `wiki-damage-006`: "Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0538](../rules/damage.md#m-0538) reading A: `unsafe circle damage and item loss are blocked by Guardian angel, Safety bubble, Reality Shield or Death Ward (Trolling page); a Shield does not`
- [M-0538](../rules/damage.md#m-0538) reading B: `damage table row: blocked by Safety bubble, Guardian angel, Death Ward; Hazmat suit slows; Body armor absorbs; Reality Shield not in the row`
- [M-0538](../rules/damage.md#m-0538) domain: boolean block per defender state
- [M-0538](../rules/damage.md#m-0538) parameter `shield_blocks`: false
- [M-0538](../rules/damage.md#m-0538) parameter `reality_shield_blocks`: contradicted, see [C-0502](../unknowns.md#c-0502)

**Interactions:** [M-0536](../rules/damage.md#m-0536), [M-0537](../rules/items.md#m-0537)

**Contradictions:** [C-0502](../unknowns.md#c-0502)

Notes ([M-0538](../rules/damage.md#m-0538)): The Reality Shield is the only mismatch. The damage page notes (a different clause) also say a Safety bubble and a Reality Shield block zone, unsafe circle and robot damage, which supports reading A.

<a id="m-0539"></a>

### M-0539: Trolling care package diversion

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0539](../rules/viewer.md#m-0539) `wiki-sigils-trolling-020`: "Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0539](../rules/viewer.md#m-0539) `wiki-attacks-079`: "A care package drops a random item at a random point in the safe zones." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))
- [M-0539](../rules/viewer.md#m-0539) `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))

**Formal model:**

- [M-0539](../rules/viewer.md#m-0539) reading A: `each viewer care package: with probability 0.03 it lands within 5 m of a Trolling contestant instead of a random point in the safe zones`
- [M-0539](../rules/viewer.md#m-0539) reading B: `crates also roll`
- [M-0539](../rules/viewer.md#m-0539) reading C: `each Trolling contestant rolls separately`
- [M-0539](../rules/viewer.md#m-0539) domain: per package; probability 0.03
- [M-0539](../rules/viewer.md#m-0539) parameter `p`: 0.03
- [M-0539](../rules/viewer.md#m-0539) parameter `landing_radius_m`: 5
- [M-0539](../rules/viewer.md#m-0539) parameter `scope`: UNKNOWN, see [U-0540](../unknowns.md#u-0540)

**Open questions:**

- [U-0540](../unknowns.md#u-0540) (medium): Trolling care package diversion '3% chance to land next to a Trolling contestant': which packages roll, how is the contestant chosen with several Trolling contestants, and is the draw once per package?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

**Contradictions:** [C-0501](../unknowns.md#c-0501)

Notes ([M-0539](../rules/viewer.md#m-0539)): The attacks page gives the 5 m distance; the Trolling page does not. Scope mismatch is contradiction [C-0501](../unknowns.md#c-0501).

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0001](../unknowns.md#u-0001), [U-0002](../unknowns.md#u-0002), [U-0003](../unknowns.md#u-0003), [U-0015](../unknowns.md#u-0015), [U-0411](../unknowns.md#u-0411), [U-0528](../unknowns.md#u-0528), [U-0529](../unknowns.md#u-0529), [U-0530](../unknowns.md#u-0530), [U-0531](../unknowns.md#u-0531), [U-0532](../unknowns.md#u-0532), [U-0533](../unknowns.md#u-0533), [U-0534](../unknowns.md#u-0534), [U-0535](../unknowns.md#u-0535), [U-0536](../unknowns.md#u-0536), [U-0537](../unknowns.md#u-0537), [U-0538](../unknowns.md#u-0538), [U-0539](../unknowns.md#u-0539), [U-0540](../unknowns.md#u-0540)

## Confidence

`UNKNOWN`: the lowest label among the rules on this page.
