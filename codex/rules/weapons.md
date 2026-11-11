# Rules: weapons

## Summary

Rules of the `weapons` family, as the wiki states them on 2026-11-11.

This page gathers 24 rules (2 `DOCUMENTED`, 22 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0300: Weapon sources

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0300 `wiki-weapons-002`: "Contestants find them in chests, care packages and crates." ([source](https://iceposeidon.com/safezone/wiki/weapons))

**Formal model:**

- M-0300 reading A: `weapon items enter play only through chests, care packages and crates (plus trades and merchant care packages stated elsewhere)`
- M-0300 domain: item acquisition

**Open questions:**

- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

Notes (M-0300): Chest, care package and crate rules are not on this page (U-0015). Trading and the merchant care package are stated on other pages.

### M-0301: Weapon slot membership

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0301 `wiki-weapons-003`: "Melee weapons, bows, staffs and Poison Darts fit a weapon slot." ([source](https://iceposeidon.com/safezone/wiki/weapons))
- M-0301 `wiki-merchant-040`: "Weapon and worn equipment slots do not use inventory space." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0301 reading A: `melee weapons, bows, staffs and Poison Darts go in a weapon slot; weapon slots and worn equipment do not use inventory space`
- M-0301 domain: item placement

Notes (M-0301): C4, landmines, drones and arrows are not listed as weapon slot items; they use inventory slots. See M-0334 for the second weapon slot.

### M-0302: C4 placement and blast

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0302 `wiki-weapons-004`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- M-0302 `wiki-weapons-005`: "Place it where you stand, then detonate it at any time." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- M-0302 `wiki-weapons-006`: "It deals 20 HP to everyone within 10m (33ft), you included." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))

**Formal model:**

- M-0302 reading A: `place at own position; detonate at any later time; every contestant with distance <= 10 m from the C4 (placer included) takes 20 HP`
- M-0302 domain: distance in metres, damage in HP
- M-0302 parameter `c4_damage_hp`: 20
- M-0302 parameter `c4_radius_m`: 10

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?
- [U-0304](../unknowns.md#u-0304) (medium): How many uses do the drone, C4, landmine and Poison Dart have when not enchanted?

Notes (M-0302): Zombies do not set off C4 (other page); blasts kill zombies in range (zombies page).

### M-0303: C4 trapped gift (Ingenuity attach)

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0303 `wiki-weapons-007`: "With the Ingenuity sigil you can attach one C4 to another item you hold, once every 16h." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- M-0303 `wiki-weapons-009`: "Detonate it while another contestant holds that item." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- M-0303 `wiki-weapons-010`: "Only that contestant takes 23 HP." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- M-0303 `wiki-weapons-011`: "It does not hurt you while you hold the item." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))

**Formal model:**

- M-0303 reading A: `attach one C4 to another item held, at most once per 16h; detonate while another contestant holds it: only that contestant takes 23 HP; the owner is not hurt while holding it`
- M-0303 domain: HP, hours
- M-0303 parameter `trapped_gift_c4_damage_hp`: 23
- M-0303 parameter `attach_cooldown_h`: 16

**Open questions:**

- [U-0301](../unknowns.md#u-0301) (medium): Is the 'once every 16h' Ingenuity trap attachment limit one shared timer for C4 and landmine, or one timer per kind, and does it start at attachment or at detonation?

Notes (M-0303): 23 HP is recorded as stated, no derivation. Trapped gifts appear in other pages' blocker tables (Shield, Sleeping Bag, Protection, Mirror) and in the Kick bonus list.

### M-0304: C4 visibility

Label: `CONDITIONAL`. Sigils: all, ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0304 `wiki-weapons-008`: "Only you can see the trap." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- M-0304 `wiki-weapons-014`: "Only you and Sigil of Ingenuity contestants can see it." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))

**Formal model:**

- M-0304 reading A: `a placed C4 is visible only to its owner and Sigil of Ingenuity contestants; the trapped gift is visible only to the owner`
- M-0304 reading B: `'Only you can see the trap' describes the placed C4 (the later sentence repeating it with Ingenuity added)`

**Open questions:**

- [U-0302](../unknowns.md#u-0302) (low): Does 'Only you can see the trap.' (C4 section) describe the trapped gift (item with attached C4) or the placed C4?

Notes (M-0304): Unlike the landmine, no proximity visibility for other contestants and no viewer visibility is stated for C4.

### M-0305: C4 stacking and slot

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0305 `wiki-weapons-012`: "Landmines and C4 stack: up to 5 of each share one inventory slot, and you can carry at most 5 of each." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- M-0305 `wiki-weapons-013`: "An enchanted one uses its own slot." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))

**Formal model:**

- M-0305 reading A: `up to 5 C4 in one inventory slot; carry at most 5 C4; an enchanted C4 takes its own slot`
- M-0305 domain: integer counts
- M-0305 parameter `c4_stack`: 5
- M-0305 parameter `c4_carry_max`: 5

**Open questions:**

- [U-0303](../unknowns.md#u-0303) (medium): How do the 'up to 5 of each share one slot / carry at most 5 of each' caps interact with 'An enchanted one uses its own slot'?

Notes (M-0305): Same sentence is on the items page (identical wording, no contradiction).

### M-0306: Drone strike

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0306 `wiki-weapons-015`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/weapons#drone))
- M-0306 `wiki-weapons-016`: "Strike any contestant you can see, at any distance." ([source](https://iceposeidon.com/safezone/wiki/weapons#drone))
- M-0306 `wiki-weapons-017`: "It hits for 10 HP after 30s." ([source](https://iceposeidon.com/safezone/wiki/weapons#drone))

**Formal model:**

- M-0306 reading A: `strike a contestant you can see at any distance; the hit of 10 HP lands 30 s after use`
- M-0306 domain: HP, seconds
- M-0306 parameter `drone_damage_hp`: 10
- M-0306 parameter `drone_delay_s`: 30
- M-0306 parameter `drone_uses`: UNKNOWN, see U-0304

**Open questions:**

- [U-0304](../unknowns.md#u-0304) (medium): How many uses do the drone, C4, landmine and Poison Dart have when not enchanted?
- [U-0305](../unknowns.md#u-0305) (high): Drone: after use, is the target fixed at launch and hit 30s later regardless of what happens, or does the drone need the target to stay visible or alive?

Notes (M-0306): 'Usable' label only. Drones are blocked by Shield, Safety Bubble, Sleeping Bag, Protection, Mirror and Body Armor per the damage tables (other page).

### M-0307: Landmine placement, trigger and blast

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0307 `wiki-weapons-018`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0307 `wiki-weapons-019`: "Place it where you stand." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0307 `wiki-weapons-020`: "It triggers when another contestant or a zombie comes within 10m (33ft)." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0307 `wiki-weapons-021`: "It deals 15 HP to everyone in range, you included, and kills every zombie in range." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))

**Formal model:**

- M-0307 reading A: `placed at own position; triggers when another contestant or a zombie is at distance <= 10 m; deals 15 HP to everyone in range, placer included, and kills every zombie in range`
- M-0307 domain: distance in metres, damage in HP
- M-0307 parameter `landmine_damage_hp`: 15
- M-0307 parameter `landmine_radius_m`: 10

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?
- [U-0304](../unknowns.md#u-0304) (medium): How many uses do the drone, C4, landmine and Poison Dart have when not enchanted?

Notes (M-0307): Whether a trigger by a contestant immune to landmines (Protection) still explodes is not stated.

### M-0308: Landmine trapped gift (Ingenuity attach)

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0308 `wiki-weapons-022`: "With the Ingenuity sigil you can attach one landmine to an item you use on yourself, once every 16h." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0308 `wiki-weapons-024`: "It fires when another contestant uses that item, the item is used up and its effect does not apply." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0308 `wiki-weapons-025`: "Only that contestant takes 11 HP." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))

**Formal model:**

- M-0308 reading A: `attach one landmine to an item used on yourself, at most once per 16h; it fires when another contestant uses that item: the item is used up, its effect does not apply, only that contestant takes 11 HP`
- M-0308 domain: HP, hours
- M-0308 parameter `trapped_gift_landmine_damage_hp`: 11
- M-0308 parameter `attach_cooldown_h`: 16

**Open questions:**

- [U-0301](../unknowns.md#u-0301) (medium): Is the 'once every 16h' Ingenuity trap attachment limit one shared timer for C4 and landmine, or one timer per kind, and does it start at attachment or at detonation?
- [U-0306](../unknowns.md#u-0306) (medium): Which items count for the Ingenuity landmine attachment 'an item you use on yourself'?

Notes (M-0308): 11 HP is recorded as stated, no derivation.

### M-0309: Landmine visibility

Label: `CONDITIONAL`. Sigils: all, ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0309 `wiki-weapons-023`: "Only you can see the trap." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0309 `wiki-weapons-026`: "Other contestants see it only within 20m (66ft) of it." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0309 `wiki-weapons-027`: "A Sigil of Ingenuity always sees it." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0309 `wiki-weapons-028`: "Viewers always see it." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))

**Formal model:**

- M-0309 reading A: `the owner sees it; other contestants see it only within 20 m of it; Sigil of Ingenuity contestants always see it; viewers always see it`
- M-0309 domain: distance in metres
- M-0309 parameter `other_see_radius_m`: 20

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?

Notes (M-0309): 'Only you can see the trap' follows the attach sentence and is the trapped gift (item), by position; the placed landmine rule is the next sentences.

### M-0310: Landmine stacking and slot

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0310 `wiki-weapons-029`: "Landmines and C4 stack: up to 5 of each share one inventory slot, and you can carry at most 5 of each." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- M-0310 `wiki-weapons-030`: "An enchanted one uses its own slot." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))

**Formal model:**

- M-0310 reading A: `up to 5 landmines in one inventory slot; carry at most 5; an enchanted landmine takes its own slot`
- M-0310 domain: integer counts
- M-0310 parameter `landmine_stack`: 5
- M-0310 parameter `landmine_carry_max`: 5

**Open questions:**

- [U-0303](../unknowns.md#u-0303) (medium): How do the 'up to 5 of each share one slot / carry at most 5 of each' caps interact with 'An enchanted one uses its own slot'?

### M-0311: Bow

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0311 `wiki-weapons-031`: "Equippable" ([source](https://iceposeidon.com/safezone/wiki/weapons#bow))
- M-0311 `wiki-weapons-032`: "Hits for 5 HP within 20m (66ft), cooldown 5s." ([source](https://iceposeidon.com/safezone/wiki/weapons#bow))
- M-0311 `wiki-weapons-033`: "Each shot uses one arrow." ([source](https://iceposeidon.com/safezone/wiki/weapons#bow))
- M-0311 `wiki-weapons-034`: "You cannot shoot without arrows." ([source](https://iceposeidon.com/safezone/wiki/weapons#bow))
- M-0311 `wiki-weapons-035`: "The bow has unlimited uses and never breaks." ([source](https://iceposeidon.com/safezone/wiki/weapons#bow))

**Formal model:**

- M-0311 reading A: `hit for 5 HP at distance <= 20 m; cooldown 5 s; each shot uses one arrow; no shot without arrows; unlimited uses, never breaks`
- M-0311 domain: HP, metres, seconds
- M-0311 parameter `bow_damage_hp`: 5
- M-0311 parameter `bow_range_m`: 20
- M-0311 parameter `bow_cooldown_s`: 5

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?
- [U-0307](../unknowns.md#u-0307) (high): Cooldown semantics (bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): does it start at the attempt or at the hit, and is it per weapon item or per contestant (Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (high): Is a use (weapon use, arrow, Deep Cut charge, enchanted use) consumed by an attack that is blocked, reflected, out of range or missing?

Notes (M-0311): The bow is on the Kick bonus and Mirror lists of other pages.

### M-0312: Arrows and stacks

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0312 `wiki-weapons-036`: "Ammo for the bow." ([source](https://iceposeidon.com/safezone/wiki/weapons#arrow))
- M-0312 `wiki-weapons-037`: "A chest drop holds 10." ([source](https://iceposeidon.com/safezone/wiki/weapons#arrow))
- M-0312 `wiki-weapons-038`: "Arrows stack: new arrows join the stack you already carry, up to 10 per stack, so they need no extra slot." ([source](https://iceposeidon.com/safezone/wiki/weapons#arrow))
- M-0312 `wiki-weapons-039`: "Arrows above that start a new stack, which uses a slot." ([source](https://iceposeidon.com/safezone/wiki/weapons#arrow))

**Formal model:**

- M-0312 reading A: `a chest drop holds 10 arrows; arrows join the stack carried up to 10 per stack; arrows above that start a new stack that takes a slot`
- M-0312 domain: integer counts
- M-0312 parameter `chest_drop_arrows`: 10
- M-0312 parameter `arrow_stack`: 10

Notes (M-0312): A new stack uses an inventory slot (3 base, items page). Chest rules are U-0015.

### M-0313: Wizard staff area

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0313 `wiki-weapons-040`: "Equippable" ([source](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
- M-0313 `wiki-weapons-041`: "Pick a spot on the map within 50m (164ft) of you to place a 10m (33ft) damage area, on top of contestants too." ([source](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
- M-0313 `wiki-weapons-042`: "It lasts 5s and deals 10 HP in total to everyone inside, you included." ([source](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))

**Formal model:**

- M-0313 reading A: `pick a spot at distance <= 50 m from the user; a 10 m area (radius or diameter, see U-0312) lasts 5 s and deals 10 HP in total to everyone inside, the user included`
- M-0313 domain: HP, metres, seconds
- M-0313 parameter `staff_placement_range_m`: 50
- M-0313 parameter `staff_area_m`: 10
- M-0313 parameter `staff_duration_s`: 5
- M-0313 parameter `staff_total_damage_hp`: 10

**Open questions:**

- [U-0010](../unknowns.md#u-0010) (medium): Wizard staff '10 HP in total over 5 s': one hit or several ticks?
- [U-0312](../unknowns.md#u-0312) (medium): Wizard staff: is '10m damage area' a radius or a diameter?
- [U-0313](../unknowns.md#u-0313) (medium): Wizard staff: does a contestant who is inside the area for only part of the 5s take the full 10 HP or only a share, and do contestants who enter after placement take damage?
- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?

Notes (M-0313): The spot may be on top of contestants. 'Wizard Staff area' is a row in the damage tables of another page.

### M-0314: Wizard staff cost, cooldown, durability

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0314 `wiki-weapons-043`: "Each use costs 2 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
- M-0314 `wiki-weapons-044`: "Cooldown 20min." ([source](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))
- M-0314 `wiki-weapons-045`: "The staff never breaks." ([source](https://iceposeidon.com/safezone/wiki/weapons#wizard_staff))

**Formal model:**

- M-0314 reading A: `each use costs 2 blood tokens; cooldown 20 min; never breaks (unlimited uses)`
- M-0314 domain: blood tokens, minutes
- M-0314 parameter `staff_cost_tokens`: 2
- M-0314 parameter `staff_cooldown_min`: 20

**Open questions:**

- [U-0314](../unknowns.md#u-0314) (low): Wizard staff 'Each use costs 2 blood tokens': does Ingenuity's 10% surcharge apply to it, and what happens with fewer than 2 tokens?
- [U-0307](../unknowns.md#u-0307) (high): Cooldown semantics (bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): does it start at the attempt or at the hit, and is it per weapon item or per contestant (Dual Wield)?

### M-0315: Poison Dart

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0315 `wiki-weapons-046`: "EquippableUsable" ([source](https://iceposeidon.com/safezone/wiki/weapons#poison_dart))
- M-0315 `wiki-weapons-047`: "Poison a nearby contestant for 20 HP over 30min." ([source](https://iceposeidon.com/safezone/wiki/weapons#poison_dart))

**Formal model:**

- M-0315 reading A: `poison a nearby contestant for 20 HP over 30 min (the poison page gives 1 HP every 1min 30s, which is 20 ticks in 30 min)`
- M-0315 domain: HP, minutes
- M-0315 parameter `dart_total_hp`: 20
- M-0315 parameter `dart_duration_min`: 30
- M-0315 parameter `dart_range_m`: UNKNOWN, see U-0309
- M-0315 parameter `dart_uses`: UNKNOWN, see U-0304

**Open questions:**

- [U-0309](../unknowns.md#u-0309) (high): What is the range of 'nearby' for the Poison Dart, Zarok's axe and Huge machete?
- [U-0315](../unknowns.md#u-0315) (medium): Poison Dart: if a poisoned contestant is darted again (or hit by a Fake gravestone), does the new poison restart a full 20 HP schedule, replace what remains, or add?
- [U-0316](../unknowns.md#u-0316) (low): Poison Dart: with '20 HP over 30min' and the poison page's 1 HP every 1min 30s, is the first tick at 1min 30s or immediately?
- [U-0304](../unknowns.md#u-0304) (medium): How many uses do the drone, C4, landmine and Poison Dart have when not enchanted?
- [U-0318](../unknowns.md#u-0318) (medium): What do the labels Equippable and Usable mean for the Poison Dart and Zarok's axe, which carry both?

Notes (M-0315): Cross-check with the poison page: 30 min / 90 s = 20 ticks of 1 HP = 20 HP, consistent, no contradiction. The dart is not on the Kick bonus list of the damage page. Re-poisoning resets the timer and does not stack (poison page).

### M-0316: Assassin's knife

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0316 `wiki-weapons-048`: "Equippable" ([source](https://iceposeidon.com/safezone/wiki/weapons#assassins_knife))
- M-0316 `wiki-weapons-049`: "Stabs a contestant within 10m (33ft) for 5 HP." ([source](https://iceposeidon.com/safezone/wiki/weapons#assassins_knife))
- M-0316 `wiki-weapons-050`: "2 uses, cooldown 5s." ([source](https://iceposeidon.com/safezone/wiki/weapons#assassins_knife))

**Formal model:**

- M-0316 reading A: `stab a contestant at distance <= 10 m for 5 HP; 2 uses; cooldown 5 s`
- M-0316 domain: HP, metres, seconds
- M-0316 parameter `knife_damage_hp`: 5
- M-0316 parameter `knife_range_m`: 10
- M-0316 parameter `knife_uses`: 2
- M-0316 parameter `knife_cooldown_s`: 5

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?
- [U-0307](../unknowns.md#u-0307) (high): Cooldown semantics (bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): does it start at the attempt or at the hit, and is it per weapon item or per contestant (Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (high): Is a use (weapon use, arrow, Deep Cut charge, enchanted use) consumed by an attack that is blocked, reflected, out of range or missing?

### M-0317: Zarok's axe

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0317 `wiki-weapons-051`: "EquippableUsable" ([source](https://iceposeidon.com/safezone/wiki/weapons#zaroks_axe))
- M-0317 `wiki-weapons-052`: "Hits a nearby contestant for 5 HP at full health, rising to 25 HP as your health drops." ([source](https://iceposeidon.com/safezone/wiki/weapons#zaroks_axe))
- M-0317 `wiki-weapons-053`: "Single use." ([source](https://iceposeidon.com/safezone/wiki/weapons#zaroks_axe))

**Formal model:**

- M-0317 reading A: `hit a nearby contestant; damage 5 HP at full health, rising to 25 HP as the wielder's health drops (curve in U-0310); single use`
- M-0317 reading B: `damage depends on the target's health instead of the wielder's`
- M-0317 domain: HP integer, 1 <= h <= max HP
- M-0317 parameter `axe_min_damage_hp`: 5
- M-0317 parameter `axe_max_damage_hp`: 25
- M-0317 parameter `axe_range_m`: UNKNOWN, see U-0309
- M-0317 parameter `axe_uses`: 1

**Open questions:**

- [U-0309](../unknowns.md#u-0309) (high): What is the range of 'nearby' for the Poison Dart, Zarok's axe and Huge machete?
- [U-0310](../unknowns.md#u-0310) (high): Zarok's axe: how does damage go from 5 HP at full health to 25 HP as the wielder's health drops (linear, stepwise, relative to max HP, where is 25 reached)?
- [U-0311](../unknowns.md#u-0311) (medium): Zarok's axe: how is a non-integer damage value rounded?
- [U-0318](../unknowns.md#u-0318) (medium): What do the labels Equippable and Usable mean for the Poison Dart and Zarok's axe, which carry both?

Notes (M-0317): 'your health' is read as the wielder's; reading B is kept because the sentence follows 'Hits a nearby contestant'.

### M-0318: Huge machete

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0318 `wiki-weapons-054`: "Equippable" ([source](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))
- M-0318 `wiki-weapons-055`: "Only admins can give it out." ([source](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))
- M-0318 `wiki-weapons-056`: "Hits a nearby contestant for 10 HP." ([source](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))
- M-0318 `wiki-weapons-057`: "10 uses, cooldown 5s." ([source](https://iceposeidon.com/safezone/wiki/weapons#huge_machete))

**Formal model:**

- M-0318 reading A: `only admins can give it out; hits a nearby contestant for 10 HP; 10 uses; cooldown 5 s`
- M-0318 domain: HP, seconds
- M-0318 parameter `machete_damage_hp`: 10
- M-0318 parameter `machete_range_m`: UNKNOWN, see U-0309
- M-0318 parameter `machete_uses`: 10
- M-0318 parameter `machete_cooldown_s`: 5

**Open questions:**

- [U-0309](../unknowns.md#u-0309) (high): What is the range of 'nearby' for the Poison Dart, Zarok's axe and Huge machete?
- [U-0307](../unknowns.md#u-0307) (high): Cooldown semantics (bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): does it start at the attempt or at the hit, and is it per weapon item or per contestant (Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (high): Is a use (weapon use, arrow, Deep Cut charge, enchanted use) consumed by an attack that is blocked, reflected, out of range or missing?

Notes (M-0318): The merchant page's enchantment text and Deep Cut list name 'machete'; this is read as the Huge machete.

### M-0319: Long sword

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0319 `wiki-weapons-058`: "Equippable" ([source](https://iceposeidon.com/safezone/wiki/weapons#long_sword))
- M-0319 `wiki-weapons-059`: "Hits a contestant within 10m (33ft) for 10 HP." ([source](https://iceposeidon.com/safezone/wiki/weapons#long_sword))
- M-0319 `wiki-weapons-060`: "3 uses, cooldown 10s." ([source](https://iceposeidon.com/safezone/wiki/weapons#long_sword))

**Formal model:**

- M-0319 reading A: `hit a contestant at distance <= 10 m for 10 HP; 3 uses; cooldown 10 s`
- M-0319 domain: HP, metres, seconds
- M-0319 parameter `sword_damage_hp`: 10
- M-0319 parameter `sword_range_m`: 10
- M-0319 parameter `sword_uses`: 3
- M-0319 parameter `sword_cooldown_s`: 10

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?
- [U-0307](../unknowns.md#u-0307) (high): Cooldown semantics (bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): does it start at the attempt or at the hit, and is it per weapon item or per contestant (Dual Wield)?
- [U-0308](../unknowns.md#u-0308) (high): Is a use (weapon use, arrow, Deep Cut charge, enchanted use) consumed by an attack that is blocked, reflected, out of range or missing?

### M-0336: Deep Cut bleeding

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0336 `wiki-merchant-042`: "Deep Cut: 20 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0336 `wiki-merchant-043`: "Your next bow, knife, long sword, axe, machete or drone hit, or Poison Dart, causes bleeding: 1 HP every five minutes until a bandage or a Healing contestant cures it." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0336 `wiki-merchant-044`: "One charge." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0336 `wiki-merchant-045`: "Bleeding does not stack." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0336 reading A: `one charge; the next hit with a bow, knife, long sword, axe, machete or drone, or the next Poison Dart, causes bleeding of 1 HP every 5 min until a bandage or a Healing contestant cures it; bleeding does not stack`
- M-0336 domain: HP, minutes
- M-0336 parameter `deep_cut_cost_tokens`: 20
- M-0336 parameter `bleed_hp`: 1
- M-0336 parameter `bleed_interval_min`: 5

**Open questions:**

- [U-0332](../unknowns.md#u-0332) (medium): Deep Cut: when is the first bleeding tick, does a new hit while bleeding reset the timer, how long does the charge last unused, and does a bleeding tick count as a hit?
- [U-0308](../unknowns.md#u-0308) (high): Is a use (weapon use, arrow, Deep Cut charge, enchanted use) consumed by an attack that is blocked, reflected, out of range or missing?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0336): Staff, C4 and landmine are not in the list. Bandage and Healing cures are stated on the Bandage and Healing pages.

### M-0337: Weapon enchantment (general rule)

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0337 `wiki-merchant-046`: "Weapon enchantment: 15 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0337 `wiki-merchant-047`: "Twice the uses and +10 damage for two hours." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0337 `wiki-merchant-048`: "After two hours the weapon loses the bonus damage and keeps the uses it had before or the uses it has left, whichever is lower." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0337 `wiki-merchant-049`: "If you use up the enchanted uses first, a knife, machete or long sword goes back with one use left; a single-use weapon is used up." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0337 `wiki-merchant-055`: "For every other weapon, if two hours pass first, the bonus ends and the item stays as a normal item." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0337 `wiki-merchant-056`: "You can have one enchanted weapon, or two with Dual Wield." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))

**Formal model:**

- M-0337 reading A: `15 tokens; twice the uses and +10 damage for 2 h; after 2 h the weapon loses the bonus and keeps min(uses before, uses left); if the enchanted uses run out first, a knife, machete or long sword returns with 1 use left and a single-use weapon is used up; for every other weapon, if 2 h pass first the bonus ends and the item is normal; one enchanted weapon, two with Dual Wield`
- M-0337 domain: HP, hours, integer uses
- M-0337 parameter `weapon_enchant_cost_tokens`: 15
- M-0337 parameter `weapon_enchant_bonus_hp`: 10
- M-0337 parameter `weapon_enchant_duration_h`: 2

**Open questions:**

- [U-0333](../unknowns.md#u-0333) (high): Weapon enchantment 'Twice the uses ... keeps the uses it had before or the uses it has left, whichever is lower': twice what, and what is 'the uses it had before'?
- [U-0334](../unknowns.md#u-0334) (medium): Enchantment clocks: does the 2 hours start at purchase or at applying it to a weapon, and does 'For every other weapon, if two hours pass first' also bound the Zarok's axe, Poison Dart, C4, landmine and drone?
- [U-0337](../unknowns.md#u-0337) (medium): Enchantment limit 'one enchanted weapon, or two with Dual Wield': does it count C4, landmine, drone and Poison Dart, which are not weapon slot items?
- [U-0308](../unknowns.md#u-0308) (high): Is a use (weapon use, arrow, Deep Cut charge, enchanted use) consumed by an attack that is blocked, reflected, out of range or missing?
- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?

Notes (M-0337): Specific weapons override this general rule in M-0338. Base 15 is not one of the binary64 trouble prices for Ingenuity.

### M-0338: Weapon enchantment per-weapon bonuses

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0338 `wiki-merchant-050`: "Zarok's Axe and Poison Dart get +10 damage for two uses, then they are used up." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0338 `wiki-merchant-051`: "Landmines and C4 get +20 damage and +10m (33ft) radius for one use, then they are used up." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0338 `wiki-merchant-052`: "Drones get +10 damage for one use, then they are used up." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0338 `wiki-merchant-053`: "A bow gets +10 damage for five shots or two hours." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0338 `wiki-merchant-054`: "A Wizard Staff gets +10 damage and +10m (33ft) area radius for five uses, with no time limit." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))

**Formal model:**

- M-0338 reading A: `Zarok's Axe and Poison Dart: +10 damage for two uses then used up; Landmines and C4: +20 damage and +10 m radius for one use then used up; Drones: +10 damage for one use then used up; bow: +10 damage for five shots or two hours; Wizard Staff: +10 damage and +10 m area radius for five uses, no time limit`
- M-0338 domain: HP, metres, integer uses
- M-0338 parameter `axe_dart_bonus_hp`: 10
- M-0338 parameter `axe_dart_uses`: 2
- M-0338 parameter `trap_bonus_hp`: 20
- M-0338 parameter `trap_bonus_radius_m`: 10
- M-0338 parameter `drone_bonus_hp`: 10
- M-0338 parameter `bow_bonus_hp`: 10
- M-0338 parameter `bow_bonus_shots`: 5
- M-0338 parameter `staff_bonus_hp`: 10
- M-0338 parameter `staff_bonus_radius_m`: 10
- M-0338 parameter `staff_enchant_uses`: 5

**Open questions:**

- [U-0317](../unknowns.md#u-0317) (medium): What does 'Poison Dart ... +10 damage for two uses' mean for a damage-over-time item?
- [U-0334](../unknowns.md#u-0334) (medium): Enchantment clocks: does the 2 hours start at purchase or at applying it to a weapon, and does 'For every other weapon, if two hours pass first' also bound the Zarok's axe, Poison Dart, C4, landmine and drone?
- [U-0335](../unknowns.md#u-0335) (low): Enchanted bow 'five shots or two hours': whichever first, or whichever last?
- [U-0336](../unknowns.md#u-0336) (medium): Enchanted C4 or landmine: is the '+10m radius' applied to the trigger distance too, and does the enchantment carry onto a trapped gift made with an enchanted trap?
- [U-0304](../unknowns.md#u-0304) (medium): How many uses do the drone, C4, landmine and Poison Dart have when not enchanted?
- [U-0312](../unknowns.md#u-0312) (medium): Wizard staff: is '10m damage area' a radius or a diameter?

Notes (M-0338): Enchanted staff: whether '+10 damage' adds to the 10 HP total of the area (20 HP total) is part of U-0010 (ticks) and not separately stated.

### M-0523: Robot craft damage and movement

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0523 `wiki-sigils-ingenuity-015`: "For ten minutes it deals 1 HP every 2s to other players within 10m (33ft)." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
- M-0523 `wiki-sigils-ingenuity-017`: "Leave it still or pick a player to follow at 1.4m/s (3.13mph)." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))

**Formal model:**

- M-0523 reading A: `robot active for 600 s; global 2 s clock; each tick: every other player within 10 m takes 1 HP; robot stays still or follows a chosen player at 1.4 m/s`
- M-0523 reading B: `per-target timer, first hit 2 s after entry`
- M-0523 reading C: `per-target, first hit at entry then every 2 s`
- M-0523 domain: t in 0..600 s; distance in metres; speed 1.4 m/s (3.13 mph)
- M-0523 parameter `duration_s`: 600
- M-0523 parameter `interval_s`: 2
- M-0523 parameter `damage_hp`: 1
- M-0523 parameter `radius_m`: 10
- M-0523 parameter `speed_mps`: 1.4
- M-0523 parameter `clock`: UNKNOWN, see U-0527

**Interactions:** M-0522, M-0524

**Open questions:**

- [U-0527](../unknowns.md#u-0527) (medium): Robot 'deals 1 HP every 2s to other players within 10m': is the 2 s clock global or per target, and does the first hit come immediately or after one interval?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

**Contradictions:** [C-0500](../unknowns.md#c-0500)

Notes (M-0523): 'other players' excludes the owner. The robot is a damage-table source (another page); whether its damage passes the 7-step hit pipeline is U-0002. A merchant item lets a contestant give a robot a target (items page). Blockers are in M-0524.

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0006](../unknowns.md#u-0006), [U-0010](../unknowns.md#u-0010), [U-0015](../unknowns.md#u-0015), [U-0300](../unknowns.md#u-0300), [U-0301](../unknowns.md#u-0301), [U-0302](../unknowns.md#u-0302), [U-0303](../unknowns.md#u-0303), [U-0304](../unknowns.md#u-0304), [U-0305](../unknowns.md#u-0305), [U-0306](../unknowns.md#u-0306), [U-0307](../unknowns.md#u-0307), [U-0308](../unknowns.md#u-0308), [U-0309](../unknowns.md#u-0309), [U-0310](../unknowns.md#u-0310), [U-0311](../unknowns.md#u-0311), [U-0312](../unknowns.md#u-0312), [U-0313](../unknowns.md#u-0313), [U-0314](../unknowns.md#u-0314), [U-0315](../unknowns.md#u-0315), [U-0316](../unknowns.md#u-0316), [U-0317](../unknowns.md#u-0317), [U-0318](../unknowns.md#u-0318), [U-0332](../unknowns.md#u-0332), [U-0333](../unknowns.md#u-0333), [U-0334](../unknowns.md#u-0334), [U-0335](../unknowns.md#u-0335), [U-0336](../unknowns.md#u-0336), [U-0337](../unknowns.md#u-0337), [U-0527](../unknowns.md#u-0527)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
