# Rules: items

## Summary

Rules of the `items` family, as the wiki states them on 2026-11-11.

This page gathers 67 rules (21 `DOCUMENTED`, 40 `CONDITIONAL`, 6 `CONTRADICTED`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0126: Body armor scope: every kind of damage, only one carried

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0126 `wiki-damage-071`: "Body Armor works on every kind of damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- M-0126 `wiki-damage-072`: "You can carry only one." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0126 reading A: `armor applies to all damage sources listed in the table with '(absorbs)'`
- M-0126 reading B: `armor applies to every source without exception (literal)`
- M-0126 parameter `max_carried`: 1

**Open questions:**

- [U-0122](../unknowns.md#u-0122) (medium): Wiki-damage-002 reads 'Reality Shield block every kind of damage. absorbs every kind of damage.' (scrambled): which sentence belongs to which item (Reality Shield blocks every kind, Body armor absorbs every kind)?

**Contradictions:** [C-0102](../unknowns.md#c-0102)

Notes (M-0126): The table has no 'Body armor' entry for the Trapped gift row and the items page says 'A trapped gift ignores it': C-0102.

### M-0127: Reality Shield and Body armor header sentence (scrambled)

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0127 `wiki-damage-002`: "Reality Shield block every kind of damage. absorbs every kind of damage." ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- M-0127 reading A: `Reality Shield: blocks every kind of damage; Body armor: absorbs every kind of damage`

**Open questions:**

- [U-0122](../unknowns.md#u-0122) (medium): Wiki-damage-002 reads 'Reality Shield block every kind of damage. absorbs every kind of damage.' (scrambled): which sentence belongs to which item (Reality Shield blocks every kind, Body armor absorbs every kind)?

Notes (M-0127): The sentence is garbled in the snapshot ('Reality Shield block every kind of damage. absorbs every kind of damage.'); the table has no Reality Shield column.

### M-0130: Flak jacket blocks the next missile, nuke, airstrike impact or gunship bomb, then is consumed

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0130 `wiki-damage-063`: "A Flak jacket blocks the next missile, nuke, airstrike impact or gunship bomb, then is used up." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- M-0130 `wiki-damage-064`: "It does not block airstrike fire." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- M-0130 `wiki-damage-065`: "A hit already blocked by something else does not use it up." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0130 reading A: `if source in {missile, nuke, airstrike impact, gunship bomb} and jacket held and no other blocker applied: d := 0 and jacket consumed; airstrike fire not blocked`

**Interactions:** M-0118

**Open questions:**

- [U-0120](../unknowns.md#u-0120) (high): When several blockers apply to one hit (Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection), which one is the 'blocker' and which items are consumed? The only stated rule is 'a hit already blocked by something else does not use [the Flak jacket] up'.

Notes (M-0130): Matches the table rows (Missile, Nuke, Airstrike impact, Gunship bomb list Flak jacket; Airstrike fire does not).

### M-0131: Gas mask blocks tear gas

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0131 `wiki-damage-066`: "A Gas mask blocks tear gas." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0131 reading A: `blocks(Gas mask) includes tear gas`

Notes (M-0131): Consistent with the Tear gas row.

### M-0132: Sleeping Bag immunity: within 15 m of own bag, all damage except zone, unsafe circle, robot

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0132 `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0132 reading A: `if asleep and dist(self, own_bag) <= 15 m: immune to every source except {outside circle, unsafe circle, robot}`
- M-0132 domain: dist in metres
- M-0132 parameter `radius_m`: 15

**Open questions:**

- [U-0120](../unknowns.md#u-0120) (high): When several blockers apply to one hit (Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection), which one is the 'blocker' and which items are consumed? The only stated rule is 'a hit already blocked by something else does not use [the Flak jacket] up'.

**Contradictions:** [C-0104](../unknowns.md#c-0104)

Notes (M-0132): Merchant page adds a 65 s delay, flashbangs and excludes only zone and unsafe circle (no robot): C-0105. Immunity is absent from the damage table rows of those three sources, as stated.

### M-0134: Mirror forcefield is used up by the first attack it reflects

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0134 `wiki-damage-069`: "A Mirror Forcefield is used up by the first attack it reflects." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0134 reading A: `mirror consumed on its first reflection; blocked or non-reflectable attacks do not consume it`

**Interactions:** M-0120

### M-0200: Inventory capacity of 3 items

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0200 `wiki-items-002`: "You can carry up to 3 items, some items can stack (such as C4/Landmines/Arrows)." ([source](https://iceposeidon.com/safezone/wiki/items#inventory))

**Formal model:**

- M-0200 reading A: `slots_used <= 3 (base capacity)`
- M-0200 domain: slots_used integer 0..3
- M-0200 parameter `capacity`: 3

**Interactions:** M-0201, M-0219

Notes (M-0200): Base value from the Items page. Other pages give different capacities for some sigils (Endurance 10, Ingenuity 2 plus 5 craft slots); those belong to the sigil families.

### M-0201: Which items stack in one slot

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0201 `wiki-items-002`: "You can carry up to 3 items, some items can stack (such as C4/Landmines/Arrows)." ([source](https://iceposeidon.com/safezone/wiki/items#inventory))

**Formal model:**

- M-0201 reading A: `stackable = {C4, Landmines, Arrows} only; every other item takes one slot per unit`
- M-0201 reading B: `the list is open ('such as'): other items (mirror forcefields, non-Piety potions, ...) may also stack`
- M-0201 domain: item kinds; stack sizes: C4/landmines 5 and arrows 10 per the weapons page

**Interactions:** M-0200, M-0202, M-0236

**Open questions:**

- [U-0200](../unknowns.md#u-0200) (medium): Which items stack in one slot beyond C4, landmines and arrows (non-Piety health potions, mirror forcefields, others)?

Notes (M-0201): Stack sizes are not on the Items page; the weapons page gives 5 for C4 and landmines and 10 per arrow stack.

### M-0202: Piety health potion stack of 6

Label: `DOCUMENTED`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0202 `wiki-items-003`: "Piety contestants stack up to 6 health potions in one slot." ([source](https://iceposeidon.com/safezone/wiki/items#inventory))

**Formal model:**

- M-0202 reading A: `all health potions of a Piety contestant share one slot, count <= 6`
- M-0202 domain: potion count 0..6

**Interactions:** M-0207

Notes (M-0202): Equal to the Piety page (all your health potions share one inventory slot, up to 6). For other contestants the Items page says nothing about potion stacking (see U-0200).

### M-0203: Cap of 3 active item effects

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0203 `wiki-items-004`: "You can have at most 3 active item effects at once." ([source](https://iceposeidon.com/safezone/wiki/items#effects))

**Formal model:**

- M-0203 reading A: `count(active item effects of a contestant) <= 3 at all times`
- M-0203 domain: integer 0..3
- M-0203 parameter `cap`: 3

**Interactions:** M-0204, M-0205, M-0206

### M-0204: Item refused at the effect cap

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0204 `wiki-items-005`: "At the limit, the item is refused and you keep it." ([source](https://iceposeidon.com/safezone/wiki/items#effects))

**Formal model:**

- M-0204 reading A: `using an item that would add an effect when count == 3: use rejected, the item stays in the inventory, state unchanged`
- M-0204 domain: count 0..3; item usage event

**Interactions:** M-0203, M-0205

**Open questions:**

- [U-0202](../unknowns.md#u-0202) (medium): How do effects not named in the cap lists behave: EMP (10min), Thermal goggles (carried), Body armor, Sleeping Bag, health potions? And what happens when a Hazmat suit is picked up at the cap?

Notes (M-0204): Hazmat suit counts 'while you carry it' (no use action), so the page does not say what happens when it is picked up at the cap (U-0202).

### M-0205: Effects that count toward the cap

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0205 `wiki-items-006`: "These count: a Shield, a Guardian angel, a Mirror forcefield, Anti poison immunity, a Flak jacket, a Gas mask, Zombie repellent, and a Hazmat suit while you carry it." ([source](https://iceposeidon.com/safezone/wiki/items#effects))

**Formal model:**

- M-0205 reading A: `counted = Shield, Guardian angel, Mirror forcefield, Anti poison immunity, Flak jacket, Gas mask, Zombie repellent, Hazmat suit (while carried); nothing else`
- M-0205 reading B: `same list but each Mirror forcefield counts separately (several can stack)`
- M-0205 reading C: `same list but all Mirror forcefields together count once`
- M-0205 domain: set of effect kinds; multiplicity of mirrors open

**Interactions:** M-0203, M-0206

**Open questions:**

- [U-0201](../unknowns.md#u-0201) (medium): Do several mirror forcefields count as one effect or each as one toward the 3-effect cap?
- [U-0202](../unknowns.md#u-0202) (medium): How do effects not named in the cap lists behave: EMP (10min), Thermal goggles (carried), Body armor, Sleeping Bag, health potions? And what happens when a Hazmat suit is picked up at the cap?

Notes (M-0205): Not named in either list: EMP (timed 10min), Thermal goggles (also 'while you carry them'), Body armor, Sleeping Bag, Health potions. See U-0202.

### M-0206: Effects that do not count toward the cap

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0206 `wiki-items-007`: "These do not count: Safety Bubbles, smoke bombs, bandages, crafts, merchant upgrades, and effects that do not come from using an item, such as a Greed chest shield." ([source](https://iceposeidon.com/safezone/wiki/items#effects))

**Formal model:**

- M-0206 reading A: `not counted = Safety Bubbles, smoke bombs, bandages, crafts, merchant upgrades, and effects not coming from using an item (example: Greed chest shield)`
- M-0206 domain: set of effect kinds

**Interactions:** M-0203, M-0205

Notes (M-0206): A Greed chest shield is a separate effect from the Shield item; whether it blocks like a Shield belongs to the Greed page.

### M-0209: Hazmat suit lengthens zone damage interval

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0209 `wiki-items-013`: "While you carry it, each zone damage interval is 2s longer." ([source](https://iceposeidon.com/safezone/wiki/items#hazmat_suit))

**Formal model:**

- M-0209 reading A: `while carried: outside-zone damage interval = 2s + 2s = 4s, grace/first tick unchanged`
- M-0209 reading B: `while carried: every interval 4s and the first tick is also delayed by 2s`
- M-0209 reading C: `while carried: +2s also applies to unsafe circle and robot damage intervals (the damage page lists Hazmat suit (slows) for outside circle, unsafe circle and robot)`
- M-0209 domain: carry state boolean; interval s in seconds
- M-0209 parameter `added_interval`: 2s
- M-0209 parameter `base_interval`: 2s (zone page: 1 HP every 2s)

**Consequences:** [T-0008](../theorems/T-0008.md)

**Interactions:** M-0205

**Open questions:**

- [U-0205](../unknowns.md#u-0205) (high): Hazmat suit '+2s per interval': which damage sources and which timings (first tick, grace) does it lengthen?
- [U-0003](../unknowns.md#u-0003) (medium): Zone damage: is the first tick at 5 s or at 7 s after leaving the safe zone?

Notes (M-0209): Damage per tick is unchanged, so the zone drain rate halves (1 HP per 4s) under the plain reading. Hazmat counts toward the 3-effect cap while carried.

### M-0210: Guardian angel zone immunity

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0210 `wiki-items-014`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#guardian_angel))
- M-0210 `wiki-items-015`: "Immune to zone damage for 10min." ([source](https://iceposeidon.com/safezone/wiki/items#guardian_angel))

**Formal model:**

- M-0210 reading A: `for 10min after use, damage from being outside the safe zone = 0`
- M-0210 reading B: `same, and unsafe circle damage = 0 as well`
- M-0210 domain: t in [0, 600) seconds after use
- M-0210 parameter `duration`: 10min

**Interactions:** M-0205, M-0211

**Open questions:**

- [U-0206](../unknowns.md#u-0206) (medium): Does Guardian angel 'zone damage' include unsafe circle damage?

Notes (M-0210): The damage page table lists Guardian angel against both 'Outside the circle' and 'Unsafe circle', while the Items page says only 'zone damage'; the Shield sentence on the same page names zone and unsafe circle separately.

### M-0211: Guardian angel end condition

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0211 `wiki-items-016`: "Ends when another contestant attacks you, even if a shield or bubble blocks the hit." ([source](https://iceposeidon.com/safezone/wiki/items#guardian_angel))

**Formal model:**

- M-0211 reading A: `ends at the first attack by another contestant whose target is you, whether or not it is blocked by Shield or Safety bubble; viewer and admin attacks excluded`
- M-0211 reading B: `A, and also non-damaging hostile actions (steal, Vulnerability Dart, flashbang) and triggers of your own placed traps by others`
- M-0211 reading C: `ends only when an attack would actually have damaged you before blocks, i.e. an attack that is neutralized earlier (miss, smoke, mirror) does not end it`
- M-0211 domain: events: attack(attacker!=you, target=you)

**Interactions:** M-0210

**Open questions:**

- [U-0207](../unknowns.md#u-0207) (high): What counts as 'attacks you' for ending a Guardian angel?

Notes (M-0211): Explicit: a blocked hit still ends it. Open: what counts as 'attacks you' for area effects, traps, poison ticks, drones and reflected attacks.

### M-0212: Safety bubble creation, size, duration

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0212 `wiki-items-017`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
- M-0212 `wiki-items-018`: "Creates a 10m (33ft) bubble where you stand for 10min." ([source](https://iceposeidon.com/safezone/wiki/items#safety_bubble))

**Formal model:**

- M-0212 reading A: `bubble = disc of radius 10 m centred on the user at the use point, lasting 600 s`
- M-0212 reading B: `bubble = disc of diameter 10 m, radius 5 m`
- M-0212 domain: positions abstract; t in [0, 600)
- M-0212 parameter `size`: 10 m (33 ft)
- M-0212 parameter `duration`: 10min

**Interactions:** M-0213, M-0214

**Open questions:**

- [U-0208](../unknowns.md#u-0208) (medium): Is the Safety bubble '10m' a radius or a diameter?

### M-0213: Safety bubble immunity

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0213 `wiki-items-019`: "Everyone inside is immune to damage and zombies, zone damage included." ([source](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
- M-0213 `wiki-items-020`: "A trapped gift still hurts the holder." ([source](https://iceposeidon.com/safezone/wiki/items#safety_bubble))

**Formal model:**

- M-0213 reading A: `for every contestant inside: damage = 0 and zombies cannot hurt, including zone damage; exception: a trapped gift still hurts the holder`
- M-0213 domain: inside(position, bubble) boolean

**Interactions:** M-0212, M-0214, M-0247

Notes (M-0213): Damage page: a Safety bubble does not stop poison from landing but blocks each poison step. Flashbang is not stopped by it (flashbang section). Boundary inclusion not stated.

### M-0214: Safety bubble and vulnerable contestants

Label: `CONTRADICTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0214 `wiki-items-021`: "It does not protect a vulnerable contestant, and you cannot use it while vulnerable." ([source](https://iceposeidon.com/safezone/wiki/items#safety_bubble))

**Formal model:**

- M-0214 reading A: `a vulnerable contestant gets no bubble protection and cannot use a bubble; the bubble itself stays for others`
- M-0214 reading B: `the Vulnerability Dart pops every bubble they own or stand in (merchant page), bubble gone for everyone`
- M-0214 domain: vulnerable boolean

**Interactions:** M-0212, M-0213, M-0216

**Contradictions:** [C-0204](../unknowns.md#c-0204)

Notes (M-0214): See C-0204. The Items page only says the vulnerable contestant is unprotected; the merchant page says the dart pops the bubble.

### M-0215: Shield duration and vulnerability

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0215 `wiki-items-022`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#shield))
- M-0215 `wiki-items-024`: "You cannot use it while vulnerable, and a Vulnerability Dart removes it." ([source](https://iceposeidon.com/safezone/wiki/items#shield))

**Formal model:**

- M-0215 reading A: `Shield lasts 20min; cannot be used while vulnerable; a Vulnerability Dart removes it`
- M-0215 domain: t in [0, 1200) seconds
- M-0215 parameter `duration`: 20min

**Interactions:** M-0205, M-0216

### M-0216: Shield damage exclusions

Label: `CONTRADICTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0216 `wiki-items-023`: "Immune to damage for 20min, except zone damage and unsafe circle damage." ([source](https://iceposeidon.com/safezone/wiki/items#shield))
- M-0216 `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0216 reading A: `Shield blocks all damage except zone damage and unsafe circle damage`
- M-0216 reading B: `Shield blocks all damage except zone, unsafe circle and robot damage (damage page)`
- M-0216 domain: damage source kinds

**Interactions:** M-0215

**Contradictions:** [C-0202](../unknowns.md#c-0202)

Notes (M-0216): See C-0202. Poison: the Shield does not stop poison from landing but blocks each step (damage page). Flashbang not stopped by a Shield.

### M-0217: Body armor absorption pool

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0217 `wiki-items-025`: "Equippable" ([source](https://iceposeidon.com/safezone/wiki/items#body_armor))
- M-0217 `wiki-items-026`: "Absorbs up to 15 HP of damage." ([source](https://iceposeidon.com/safezone/wiki/items#body_armor))
- M-0217 `wiki-damage-055`: "Body armor absorbs what is left, until it breaks." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- M-0217 reading A: `armor holds a pool of 15 HP: each hit loses min(pool, damage_left) HP from the pool, then pool-=absorbed; broken at 0`
- M-0217 reading B: `armor absorbs up to 15 HP per hit and is never depleted`
- M-0217 domain: pool integer 0..15
- M-0217 parameter `capacity`: 15 HP

**Interactions:** M-0218, M-0219

**Open questions:**

- [U-0209](../unknowns.md#u-0209) (high): Is the 15 HP of Body armor a depleting pool or a per-hit cap, and how is a partly absorbed hit handled?

Notes (M-0217): 'Until it breaks' on the damage page supports a depleting pool (A), but a partly absorbed hit is not specified. Pipeline order belongs to the damage page.

### M-0218: Trapped gift ignores Body armor

Label: `CONTRADICTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0218 `wiki-items-027`: "A trapped gift ignores it." ([source](https://iceposeidon.com/safezone/wiki/items#body_armor))
- M-0218 `wiki-damage-071`: "Body Armor works on every kind of damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0218 reading A: `trapped gift damage bypasses Body armor`
- M-0218 reading B: `Body armor works on every kind of damage, including trapped gift`
- M-0218 domain: damage source kinds

**Interactions:** M-0217

**Contradictions:** [C-0201](../unknowns.md#c-0201)

Notes (M-0218): See C-0201. The damage page table row for Trapped gift also omits Safety bubble and Body armor, which matches A.

### M-0219: Body armor equip slot and carry limit

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0219 `wiki-items-028`: "It goes into your armor slot when you get it." ([source](https://iceposeidon.com/safezone/wiki/items#body_armor))
- M-0219 `wiki-items-029`: "Carry at most one, including equipped armor." ([source](https://iceposeidon.com/safezone/wiki/items#body_armor))
- M-0219 `wiki-merchant-040`: "Weapon and worn equipment slots do not use inventory space." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0219 `wiki-merchant-041`: "Carry at most one Body Armor." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0219 reading A: `armor goes to the armor slot on pick-up, not an inventory slot; at most 1 armor total including the equipped one; extra armor is refused`
- M-0219 reading B: `a second armor replaces or swaps with the equipped one`
- M-0219 domain: armor count 0..1

**Interactions:** M-0200, M-0217

**Open questions:**

- [U-0210](../unknowns.md#u-0210) (low): What happens when you get a second Body armor while one is equipped or carried?

### M-0220: Zombie repellent

Label: `CONTRADICTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0220 `wiki-items-030`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
- M-0220 `wiki-items-031`: "Use it to stop zombies hurting you for 20min." ([source](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
- M-0220 `wiki-items-032`: "It only protects you." ([source](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
- M-0220 `wiki-zombies-019`: "Zombie repellent: use it and zombies ignore you for 20min." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

**Formal model:**

- M-0220 reading A: `20min after use: zombie damage to you = 0; zombies still target and chase you`
- M-0220 reading B: `20min after use: zombies ignore you entirely (not a valid target), they chase others`
- M-0220 reading C: `applies to you only, never to others nearby`
- M-0220 domain: t in [0, 1200) seconds
- M-0220 parameter `duration`: 20min

**Interactions:** M-0205

**Contradictions:** [C-0205](../unknowns.md#c-0205)

Notes (M-0220): See C-0205. 'Stop zombies hurting you' (Items) versus 'zombies ignore you' (zombies page). 'It only protects you' holds in all readings.

### M-0226: Smoke bomb area, duration, effect on others

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0226 `wiki-items-040`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
- M-0226 `wiki-items-041`: "Blacks out the map and blocks attacks for other contestants within 50m (164ft) of you for 20min." ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
- M-0226 `wiki-items-042`: "Any other contestant inside it cannot attack at all: no targeted attacks, staff areas, C4, landmines or flashbangs." ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))

**Formal model:**

- M-0226 reading A: `cloud = disc of radius 50 m fixed where it was set off, 20min; other contestants inside have map blacked out and cannot attack (targeted attacks, staff areas, C4, landmines, flashbangs)`
- M-0226 reading B: `same but centre follows the user`
- M-0226 domain: positions abstract; t in [0, 1200) seconds
- M-0226 parameter `radius`: 50 m
- M-0226 parameter `duration`: 20min

**Interactions:** M-0227, M-0228, M-0229, M-0231

**Open questions:**

- [U-0211](../unknowns.md#u-0211) (medium): Is the smoke bomb cloud fixed where it was set off or does it follow the user?

### M-0227: Smoke bomb restrictions from inside

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0227 `wiki-items-043`: "From inside it you also cannot heal or steal from other contestants, send a trade request, throw a Vulnerability Dart, fire a merchant missile or give a robot a target." ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))

**Formal model:**

- M-0227 reading A: `an other contestant inside the cloud also cannot: heal or steal from other contestants, send a trade request, throw a Vulnerability Dart, fire a merchant missile, give a robot a target`
- M-0227 domain: action set

**Interactions:** M-0226

### M-0228: Smoke bomb outside targeting block

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0228 `wiki-items-044`: "Nobody outside can target anyone inside it either, drones included." ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))

**Formal model:**

- M-0228 reading A: `nobody outside can target anyone inside the cloud, drones included, the setter included`
- M-0228 reading B: `the setter can still be targeted from outside`
- M-0228 domain: target position inside cloud

**Interactions:** M-0226

**Open questions:**

- [U-0212](../unknowns.md#u-0212) (medium): Can the contestant who set off the smoke bomb be targeted from outside the cloud?

### M-0229: Smoke bomb setter exemption

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0229 `wiki-items-045`: "The contestant who set it off is not affected and can still attack from inside it, including others inside." ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))

**Formal model:**

- M-0229 reading A: `the contestant who set it off is unaffected and can attack from inside, others inside included`
- M-0229 domain: setter boolean

**Interactions:** M-0226, M-0228

### M-0231: Thermal goggles versus smoke bomb

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0231 `wiki-items-046`: "Thermal goggles see through it." ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))
- M-0231 `wiki-items-067`: "While you carry them, smoke bombs do not black out your map or block your attacks." ([source](https://iceposeidon.com/safezone/wiki/items#thermal_goggles))

**Formal model:**

- M-0231 reading A: `carried goggles: no map blackout and no attack block from smoke for the carrier; the restrictions of M-0227 still apply`
- M-0231 reading B: `carried goggles: no smoke restriction of any kind for the carrier, including those of M-0227`
- M-0231 domain: carry boolean

**Interactions:** M-0226, M-0227

**Open questions:**

- [U-0213](../unknowns.md#u-0213) (medium): Does Thermal goggles' exemption cover only smoke attack blocks and blackout, or also the inside-cloud restrictions on healing, stealing and trading?
- [U-0202](../unknowns.md#u-0202) (medium): How do effects not named in the cap lists behave: EMP (10min), Thermal goggles (carried), Body armor, Sleeping Bag, health potions? And what happens when a Hazmat suit is picked up at the cap?

Notes (M-0231): Attacks page (cyclops): weapons and drones cannot hit it inside a cloud unless you hold Thermal goggles.

### M-0232: Thermal goggles see illusion copies

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0232 `wiki-items-068`: "You also see through illusions: copies of contestants show as copies, not as real contestants." ([source](https://iceposeidon.com/safezone/wiki/items#thermal_goggles))
- M-0232 `wiki-attacks-052`: "Thermal goggles show them as copies." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))

**Formal model:**

- M-0232 reading A: `while carried, illusion copies show as copies, not as real contestants`
- M-0232 domain: carry boolean

### M-0235: Mirror forcefield reflects next attack

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0235 `wiki-items-052`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
- M-0235 `wiki-items-053`: "Reflects the next attack back at the attacker." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
- M-0235 `wiki-damage-041`: "A Mirror forcefield sends the whole hit back to the attacker instead, before any reduction." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- M-0235 reading A: `the next reflectable attack on you is sent back at the attacker, whole hit, before any reduction; attacker's own pipeline applies`
- M-0235 reading B: `reflected hit skips the attacker's defenses and bypasses their pipeline`
- M-0235 domain: attack event

**Interactions:** M-0236, M-0237, M-0239, M-0240, M-0241

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

### M-0236: Mirror forcefields stack

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0236 `wiki-items-054`: "Several stack." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
- M-0236 `wiki-damage-069`: "A Mirror Forcefield is used up by the first attack it reflects." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0236 reading A: `several mirrors can be held; one reflection consumes exactly one`
- M-0236 reading B: `several mirrors can be held; the first reflection consumes all`
- M-0236 reading C: `several mirrors give several successive reflections`
- M-0236 domain: mirror count n >= 0

**Interactions:** M-0201, M-0205, M-0247

**Open questions:**

- [U-0201](../unknowns.md#u-0201) (medium): Do several mirror forcefields count as one effect or each as one toward the 3-effect cap?
- [U-0215](../unknowns.md#u-0215) (medium): When several mirror forcefields are held, does one reflection consume one, all, or reflect several times?
- [U-0200](../unknowns.md#u-0200) (medium): Which items stack in one slot beyond C4, landmines and arrows (non-Piety health potions, mirror forcefields, others)?

Notes (M-0236): Flashbang is the only case stated: several forcefields are all used up (M-0247).

### M-0237: Mirror reflect list

Label: `CONTRADICTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0237 `wiki-items-055`: "Only reflects Poison Darts, fake gravestones, knives, Zarok's axes, long swords, machetes, bows, staffs, drones, C4, landmines, flashbangs and fake chests." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
- M-0237 `wiki-damage-070`: "It only reflects Poison Darts, fake gravestones, bows, wizard staffs, knives, long swords, Zarok's axes, machetes, drones, C4, landmines, flashbangs and fake chests, and never your own explosives." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- M-0237 `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- M-0237 reading A: `reflected = Poison Darts, fake gravestones, knives, Zarok's axes, long swords, machetes, bows, staffs, drones, C4, landmines, flashbangs, fake chests`
- M-0237 reading B: `A plus trapped gift (damage page table lists Mirror forcefield (reflects) on the Trapped gift row)`
- M-0237 domain: 13 attack kinds in A; trapped gift status open

**Interactions:** M-0235

**Contradictions:** [C-0200](../unknowns.md#c-0200)

Notes (M-0237): Items list and damage-page sentence agree on 13 kinds; the damage page table adds trapped gift. See C-0200. Damage page also: never your own explosives.

### M-0238: Mirror reflects a fake chest

Label: `DOCUMENTED`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- M-0238 `wiki-items-056`: "A reflected fake chest also locks the troll out of chests instead of you." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))

**Formal model:**

- M-0238 reading A: `a reflected fake chest locks the troll out of chests, not the target`
- M-0238 domain: fake chest event

**Interactions:** M-0237

### M-0239: Mirror against an attacker mirror

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0239 `wiki-items-057`: "If the attacker also has one, the attack does nothing and both are used up, except a reflected Poison Dart or fake gravestone: it still poisons the attacker and their own mirror stays." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))

**Formal model:**

- M-0239 reading A: `if the attacker also has a mirror: attack does nothing, both mirrors used up; exception reflected Poison Dart or fake gravestone: poisons the attacker and their mirror stays (defender's mirror used)`
- M-0239 reading B: `exception variant: the attacker's mirror stays and the defender's mirror is also kept`
- M-0239 domain: both parties hold >= 1 mirror

**Interactions:** M-0235, M-0247

**Open questions:**

- [U-0217](../unknowns.md#u-0217) (low): Mirror versus mirror and flashbang: if the thrower also holds a mirror, is the thrower blinded?
- [U-0215](../unknowns.md#u-0215) (medium): When several mirror forcefields are held, does one reflection consume one, all, or reflect several times?

### M-0240: Mirror duration and end

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0240 `wiki-items-058`: "No time limit." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
- M-0240 `wiki-items-059`: "Ends when it reflects an attack or when you die." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))

**Formal model:**

- M-0240 reading A: `no timer; ends when it reflects an attack or when you die`
- M-0240 domain: mirror state

**Interactions:** M-0235, M-0241

### M-0241: Mirror ignores viewer, admin, zone and zombie damage

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0241 `wiki-items-060`: "Never reflects viewer or admin attacks, such as missiles, nukes and gas, or the zone and zombies." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
- M-0241 `wiki-items-061`: "These do not use it up." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))

**Formal model:**

- M-0241 reading A: `never reflects viewer or admin attacks (missiles, nukes, gas), zone damage or zombies; these do not use it up`
- M-0241 domain: damage source kinds

**Interactions:** M-0235

### M-0242: Flak jacket blocks one explosive hit

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0242 `wiki-items-062`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#flak_jacket))
- M-0242 `wiki-items-063`: "Use it to block the next missile, nuke, airstrike or gunship hit on you." ([source](https://iceposeidon.com/safezone/wiki/items#flak_jacket))
- M-0242 `wiki-items-064`: "It stays active until a hit uses it up." ([source](https://iceposeidon.com/safezone/wiki/items#flak_jacket))
- M-0242 `wiki-damage-063`: "A Flak jacket blocks the next missile, nuke, airstrike impact or gunship bomb, then is used up." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- M-0242 `wiki-attacks-034`: "A Flak jacket blocks the strike, but not the fire." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
- M-0242 `wiki-attacks-041`: "A Flak jacket blocks one bomb." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))

**Formal model:**

- M-0242 reading A: `blocks the next missile, nuke, airstrike impact or gunship bomb that reaches the holder; used up by that hit; airstrike fire not blocked`
- M-0242 reading B: `A, but a hit already blocked by Shield/Safety bubble/Sleeping Bag also consumes it`
- M-0242 reading C: `A, but a hit already blocked earlier does not consume it`
- M-0242 domain: hit event of listed kinds

**Interactions:** M-0205

**Open questions:**

- [U-0216](../unknowns.md#u-0216) (medium): Does a Flak jacket get used up by a hit already blocked by another defense (Shield, Safety bubble, Sleeping Bag)?

Notes (M-0242): Items page names 'airstrike or gunship hit'; attacks page narrows to the strike and one bomb (not the fire).

### M-0243: Gas mask

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0243 `wiki-items-065`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#gas_mask))
- M-0243 `wiki-items-066`: "Use it to become immune to tear gas for 10min." ([source](https://iceposeidon.com/safezone/wiki/items#gas_mask))
- M-0243 `wiki-damage-066`: "A Gas mask blocks tear gas." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- M-0243 reading A: `for 10min after use, tear gas does nothing to the user`
- M-0243 domain: t in [0, 600) seconds
- M-0243 parameter `duration`: 10min

**Interactions:** M-0205

### M-0244: Flashbang blinds nearby contestants

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0244 `wiki-items-069`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))
- M-0244 `wiki-items-070`: "Blinds every other contestant within 30m (98ft) of you for 30s." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))

**Formal model:**

- M-0244 reading A: `at use: every other contestant within 30 m of the user is blinded for 30 s; re-hit while blinded: no extension`
- M-0244 reading B: `re-hit while blinded resets the timer to 30 s`
- M-0244 reading C: `re-hit while blinded adds another 30 s`
- M-0244 domain: distance d <= 30 m (boundary inclusion open)
- M-0244 parameter `radius`: 30 m
- M-0244 parameter `duration`: 30s

**Interactions:** M-0245, M-0246, M-0247

**Open questions:**

- [U-0218](../unknowns.md#u-0218) (low): If a contestant is blinded and hit by another flashbang, is the blind extended, reset or ignored?

### M-0245: Blind restrictions

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0245 `wiki-items-071`: "Blinded contestants can only move: they cannot see the map, use, place or aim items, attack, steal, loot, claim, craft or start a trade." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))
- M-0245 `wiki-items-072`: "They can still close a trade." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))
- M-0245 `wiki-items-073`: "Effects already active keep working." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))

**Formal model:**

- M-0245 reading A: `blinded: movement only; cannot see map, use/place/aim items, attack, steal, loot, claim, craft, start a trade; can still close a trade; already active effects keep working`
- M-0245 domain: blind boolean

**Interactions:** M-0244

### M-0246: Flashbang immunities and non-blockers

Label: `CONTRADICTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0246 `wiki-items-074`: "Shields and safety bubbles do not stop it." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))
- M-0246 `wiki-items-075`: "Sleeping contestants are immune." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))
- M-0246 `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0246 reading A: `Shields and Safety bubbles do not stop it; sleeping contestants are immune`
- M-0246 reading B: `immunity only after 65 s of sleep in own Sleeping Bag (merchant page)`
- M-0246 domain: sleep state, sleep duration

**Interactions:** M-0244

**Contradictions:** [C-0203](../unknowns.md#c-0203)

Notes (M-0246): See C-0203. 'Sleeping contestants are immune' versus 'After 65 seconds of sleep you are immune to flashbangs'.

### M-0247: Flashbang against mirror forcefields

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0247 `wiki-items-076`: "A mirror forcefield is used up and blinds you instead." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))
- M-0247 `wiki-items-077`: "Several forcefields are all used up, but you are blinded only once." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))

**Formal model:**

- M-0247 reading A: `a mirror is used up and blinds the thrower; several mirrors among victims are all used up; thrower blinded once`
- M-0247 reading B: `A, and a thrower holding a mirror too is not blinded (attacker-mirror rule M-0239 wins)`
- M-0247 reading C: `A, and a thrower holding a mirror is blinded (flashbang rule wins)`
- M-0247 domain: victims with mirrors m >= 0

**Interactions:** M-0236, M-0239, M-0244

**Open questions:**

- [U-0217](../unknowns.md#u-0217) (low): Mirror versus mirror and flashbang: if the thrower also holds a mirror, is the thrower blinded?
- [U-0201](../unknowns.md#u-0201) (medium): Do several mirror forcefields count as one effect or each as one toward the 3-effect cap?
- [U-0215](../unknowns.md#u-0215) (medium): When several mirror forcefields are held, does one reflection consume one, all, or reflect several times?

### M-0326: Vulnerability Dart

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0326 `wiki-merchant-015`: "Vulnerability Dart: 25 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0326 `wiki-merchant-016`: "Throw it at a contestant within 10m." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0326 `wiki-merchant-017`: "It removes their Shield and pops every Safety Bubble they own or stand in, and stops Shields and Safety Bubbles protecting them for 10 minutes." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0326 `wiki-merchant-018`: "They cannot use a Shield or a Safety Bubble while vulnerable." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0326 reading A: `throw at a contestant at distance <= 10 m; removes their Shield, pops every Safety Bubble they own or stand in, and for 10 min Shields and Safety Bubbles do not protect them and they cannot use one`
- M-0326 domain: metres, minutes
- M-0326 parameter `dart_cost_tokens`: 25
- M-0326 parameter `dart_range_m`: 10
- M-0326 parameter `vulnerable_duration_min`: 10

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?
- [U-0324](../unknowns.md#u-0324) (medium): Vulnerability Dart: does a second dart on an already vulnerable contestant reset, extend or do nothing, and is the 10 minutes counted from the throw or the impact?

Notes (M-0326): Safety Bubbles popped include ones that other contestants also stand in. A Safety Bubble from inside one cannot be thrown (Safety Bubble page).

### M-0327: Sleeping Bag ownership

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0327 `wiki-merchant-020`: "Sleeping Bag: 30 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0327 `wiki-merchant-025`: "Only you can pick up your bag." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0327 `wiki-merchant-026`: "You can have only one Sleeping Bag, held or placed." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0327 `wiki-merchant-027`: "It cannot be dropped or stolen, only destroyed by you." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0327 `wiki-merchant-028`: "Greed can still steal your other items while you sleep." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0327 reading A: `30 tokens; only the owner can pick up the bag; at most one bag held or placed; it cannot be dropped or stolen, only destroyed by its owner; Greed can still steal other items from a sleeper`
- M-0327 parameter `sleeping_bag_cost_tokens`: 30

Notes (M-0327): Consistent with the Greed page ('Sleeping Bags cannot be stolen, but you can steal from a sleeping contestant').

### M-0328: Sleeping Bag sleep window and incapacity

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0328 `wiki-merchant-021`: "Place it and sleep from 18:00 to 06:00 local solar time, for eight hours of sleep in total." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0328 `wiki-merchant-022`: "While you sleep within 15m of your bag, you cannot act." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0328 `wiki-merchant-024`: "Wake up to act." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0328 reading A: `place the bag and sleep from 18:00 to 06:00 local solar time, eight hours of sleep in total; while sleeping within 15 m of the bag you cannot act; wake up to act`
- M-0328 domain: hours, metres
- M-0328 parameter `sleep_window`: 18:00 to 06:00 local solar time
- M-0328 parameter `sleep_total_h`: 8
- M-0328 parameter `sleep_radius_m`: 15

**Open questions:**

- [U-0325](../unknowns.md#u-0325) (high): Sleeping Bag: what are the 'sleep from 18:00 to 06:00 ... for eight hours of sleep in total' rules?
- [U-0326](../unknowns.md#u-0326) (low): 'Local solar time': local to what (the contestant's position, the event location, one reference city)?
- [U-0327](../unknowns.md#u-0327) (high): Sleeping Bag: is the 65 s of sleep continuous, what happens when the sleeper leaves the 15m radius, wakes up or is hit, and does waking end the immunity at once?
- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?

### M-0329: Sleeping Bag immunity

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0329 `wiki-merchant-019`: "A contestant who has slept in their Sleeping Bag for 65 seconds cannot be targeted." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0329 `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0329 reading A: `after 65 s of sleep: cannot be targeted, immune to flashbangs and to all damage except zone and unsafe circle damage`
- M-0329 domain: seconds
- M-0329 parameter `sleep_immunity_delay_s`: 65

**Open questions:**

- [U-0327](../unknowns.md#u-0327) (high): Sleeping Bag: is the 65 s of sleep continuous, what happens when the sleeper leaves the 15m radius, wakes up or is hit, and does waking end the immunity at once?
- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?

**Contradictions:** [C-0300](../unknowns.md#c-0300), [C-0301](../unknowns.md#c-0301)

Notes (M-0329): Conflicts with other pages: robot damage exception (C-0300) and the 65 s delay versus immediate immunity (C-0301).

### M-0330: Sleeping Bag lockout

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0330 `wiki-merchant-029`: "After your bag protects you, you cannot sleep in a bag again for 20 minutes, even if you pick it up and place it again." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0330 reading A: `after the bag protects you, no sleeping in any bag for 20 min, even after picking it up and placing it again`
- M-0330 domain: minutes
- M-0330 parameter `sleep_lockout_min`: 20

**Open questions:**

- [U-0328](../unknowns.md#u-0328) (high): Sleeping Bag: when does the 20-minute 'cannot sleep again' lockout start (the moment the bag first protects, when you wake, or at the last blocked damage)?

### M-0331: Merchant missile

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0331 `wiki-merchant-030`: "Missile: 10 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0331 `wiki-merchant-031`: "Launch a standard missile at an exact map location." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0331 `wiki-merchant-032`: "It lands 30 seconds after launch." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0331 reading A: `10 tokens; launch a standard missile at an exact map location; it lands 30 s after launch`
- M-0331 domain: tokens, seconds
- M-0331 parameter `missile_cost_tokens`: 10
- M-0331 parameter `missile_delay_s`: 30
- M-0331 parameter `missile_damage_hp`: UNKNOWN, see U-0340

**Open questions:**

- [U-0340](../unknowns.md#u-0340) (high): What damage and radius does the merchant 'standard missile' have, given it lands at an exact location after 30 s?
- [U-0321](../unknowns.md#u-0321) (medium): Which merchant purchases need a free inventory slot ('Items need a free inventory slot')?

Notes (M-0331): A Smoke bomb blocks firing it from inside the bomb (Smoke bomb page).

### M-0335: Body armor carry limit

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0335 `wiki-merchant-041`: "Carry at most one Body Armor." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0335 reading A: `at most one Body Armor carried`

Notes (M-0335): The Body Armor page says 'Carry at most one, including equipped armor', same rule.

### M-0339: Armor enchantment and decay

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0339 `wiki-merchant-057`: "Armor enchantment: 30 blood tokens. +10 durability, up to 45." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0339 `wiki-merchant-058`: "It then loses one durability every twenty minutes, down to 15." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))

**Formal model:**

- M-0339 reading A: `30 tokens; +10 durability, up to 45; it then loses 1 durability every 20 min, down to 15`
- M-0339 domain: durability integer, minutes
- M-0339 parameter `armor_enchant_cost_tokens`: 30
- M-0339 parameter `armor_enchant_bonus`: 10
- M-0339 parameter `armor_cap`: 45
- M-0339 parameter `armor_decay_interval_min`: 20
- M-0339 parameter `armor_decay_floor`: 15

**Consequences:** [T-0012](../theorems/T-0012.md)

**Open questions:**

- [U-0338](../unknowns.md#u-0338) (medium): Armor enchantment '+10 durability, up to 45': can it be bought repeatedly, is 45 a cap on durability after the enchant, and from what base?
- [U-0339](../unknowns.md#u-0339) (medium): Enchanted armor decay 'loses one durability every twenty minutes, down to 15': when does the clock start, does decay stop at 15 even if damage left less, and does a re-enchant restart it?

Notes (M-0339): Base armor durability is on the Body Armor page ('Absorbs up to 15 HP of damage' there), not on this page.

### M-0503: Piety chest and crate to random health potion

Label: `CONDITIONAL`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0503 `wiki-sigils-piety-010`: "Every item chest you claim and every crate you take gives you a random health potion instead of the item inside." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
- M-0503 `wiki-sigils-piety-012`: "Merchant care packages are not changed." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))

**Formal model:**

- M-0503 reading A: `claim(item chest) or take(crate) -> add one health potion of random tier to inventory; the inside item is not given; merchant care packages unchanged; other care packages unchanged`
- M-0503 reading B: `as A but non-merchant care packages (airdrop, viewer, admin) also convert`
- M-0503 domain: per claim of an item chest or take of a crate
- M-0503 parameter `potion_tier_weights`: UNKNOWN, see U-0504
- M-0503 parameter `scope`: UNKNOWN, see U-0505
- M-0503 parameter `overflow`: UNKNOWN, see U-0506

**Interactions:** M-0502, M-0504, M-0506

**Open questions:**

- [U-0504](../unknowns.md#u-0504) (high): What is the size distribution of the 'random health potion' a Piety contestant gets from a chest or crate?
- [U-0505](../unknowns.md#u-0505) (medium): Piety chest conversion scope: do only 'item chests' and crates convert, or do other care packages (airdrop, admin, viewer, Endurance) also turn into potions?
- [U-0506](../unknowns.md#u-0506) (low): Piety claiming a chest or crate when the potion stack is already at 6 (or the inventory cannot take a potion): what happens?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

Notes (M-0503): Everything about what chests are comes from the removed chests page, see U-0015. Fake chests are not item chests, see the next mechanic. Piety item loot never includes the item inside (no weapon, no armor from chests). Greed contestants roll their own bonuses on chests (separate sigil).

### M-0504: Fake chest still springs its trap on Piety

Label: `DOCUMENTED`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0504 `wiki-sigils-piety-011`: "A fake chest still springs its trap." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))

**Formal model:**

- M-0504 reading A: `claim(fake chest) by Piety contestant -> trap effect applies as to any other contestant; no health potion is given`
- M-0504 domain: claim of a fake chest by a Piety contestant

**Interactions:** M-0503, M-0533

Notes (M-0504): The trap effect itself is on the Trolling page (5 HP damage and chest lockout) and is modelled in M-0533. Whether a Piety contestant can tell a fake chest from a real one is not stated (only Ingenuity recognizes fakes).

### M-0506: Piety health potion stack of 6 in one slot

Label: `DOCUMENTED`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0506 `wiki-sigils-piety-014`: "All your health potions share one inventory slot, up to 6 potions." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
- M-0506 `wiki-items-003`: "Piety contestants stack up to 6 health potions in one slot." ([source](https://iceposeidon.com/safezone/wiki/items#inventory))

**Formal model:**

- M-0506 reading A: `all health potions of any tier occupy one inventory slot, stack cap 6; slot capacity 3 (M-0500)`
- M-0506 domain: potion count 0..6
- M-0506 parameter `stack_cap`: 6
- M-0506 parameter `slots_for_potions`: 1

**Interactions:** M-0500, M-0503

Notes (M-0506): Both pages agree: one slot, up to 6. Whether mixed tiers share the slot is read from 'All your health potions'. Zombies have a 10% chance to break one of your health potions (zombies page), which matters most for Piety.

### M-0513: Greed chest Shield roll

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- M-0513 `wiki-sigils-greed-010`: "Each real chest you claim has a 25% chance to give you a Shield for 20min." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- M-0513 `wiki-sigils-greed-011`: "No roll while you are vulnerable." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- M-0513 `wiki-items-007`: "a Greed chest shield" ([source](https://iceposeidon.com/safezone/wiki/items#effects))

**Formal model:**

- M-0513 reading A: `claim(real chest) while not vulnerable -> with probability 0.25 grant Shield for 1200 s; no roll while vulnerable; the Shield does not count toward the 3 active item effects limit`
- M-0513 reading B: `overlap rule with an existing Shield undefined`
- M-0513 domain: per real chest claim; 20 min = 1200 s
- M-0513 parameter `p`: 0.25
- M-0513 parameter `duration_s`: 1200
- M-0513 parameter `stack_rule`: UNKNOWN, see U-0511

**Interactions:** M-0512

**Open questions:**

- [U-0511](../unknowns.md#u-0511) (medium): Greed chest Shield: what happens when the contestant already has an active Shield (item or earlier chest Shield)?

Notes (M-0513): The items page says explicitly that a Greed chest shield is not an active item effect for the limit of 3, so it is not an item use. Fake chests do not roll ('real chest'). Whether the Vulnerability Dart (which removes a Shield) removes this one is not written; the Shield item text says a Vulnerability Dart removes it.

### M-0518: Ingenuity potion combining

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0518 `wiki-sigils-ingenuity-009`: "Combine two matching potions into the next size, up to gigantic." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

**Formal model:**

- M-0518 reading A: `combine(p1, p2) with tier(p1) = tier(p2) < gigantic -> one potion of the next tier`
- M-0518 reading B: `any two matching potions of one kind combine`
- M-0518 domain: tiers small < medium < large < gigantic; heal values 5, 10, 20, 40 (items page) so combining is lossless
- M-0518 parameter `results`: small+small=medium; medium+medium=large; large+large=gigantic

**Interactions:** M-0525, M-0526

**Open questions:**

- [U-0515](../unknowns.md#u-0515) (low): Ingenuity potion combining: what does 'two matching potions' mean, and are there costs or limits?

Notes (M-0518): No cost or cooldown stated. Used as the Campfire and Everything potion ingredients: a combined potion sets the pool or the heal.

### M-0519: Ingenuity trapped gift

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0519 `wiki-sigils-ingenuity-010`: "Attach a landmine or C4 to an item to make a trapped gift, once every 16h." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
- M-0519 `wiki-sigils-ingenuity-011`: "Only you can see it is trapped." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

**Formal model:**

- M-0519 reading A: `attach(trap in {landmine, C4}, item) -> trapped gift; one shared cooldown 16 h = 57600 s; only the owner can see that it is trapped`
- M-0519 reading B: `separate 16 h cooldowns for landmine and C4`
- M-0519 reading C: `other Ingenuity contestants also see it`
- M-0519 domain: time in seconds
- M-0519 parameter `cooldown_s`: 57600
- M-0519 parameter `trap_types`: landmine, C4

**Interactions:** M-0517

**Open questions:**

- [U-0516](../unknowns.md#u-0516) (medium): Trapped gift: is the 16 h limit shared between landmine and C4 attachments, and who can see the trap (the owner only, or also other Ingenuity contestants)?

Notes (M-0519): The C4 page says C4 attaches 'to another item you hold' and the Landmine page 'to an item you use on yourself'; each repeats once every 16h. Damages (23 HP C4, 11 HP landmine) are on the weapons page and are not recorded here. A trapped gift ignores Body armor and hurts the holder through a Safety bubble (items page).

### M-0520: Ingenuity unique craft restrictions and zombie destruction

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0520 `wiki-sigils-ingenuity-012`: "Unique crafts cannot be traded, stolen or looted, and have a 40% chance to be destroyed by Zombie hits." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
- M-0520 `wiki-zombies-004`: "a 40% chance to destroy crafted items" ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- M-0520 reading A: `craft c: not tradable, not stealable, not lootable; each zombie drain hit: for every craft, destroy with probability 0.40`
- M-0520 reading B: `each zombie hit rolls once and destroys one random craft with probability 0.40`
- M-0520 reading C: `one 0.40 roll per zombie encounter`
- M-0520 domain: probability 0.4 per roll; hit rate per zombie is 1 drain per 10 s (guard zombie 2 HP per 5 s)
- M-0520 parameter `p_destroy`: 0.4
- M-0520 parameter `roll_unit`: UNKNOWN, see U-0518

**Interactions:** M-0522, M-0527

**Open questions:**

- [U-0518](../unknowns.md#u-0518) (high): Unique crafts '40% chance to be destroyed by Zombie hits': is the roll per drain hit, per zombie, or per craft, and does a blocked hit roll?

Notes (M-0520): Ingenuity page and zombies page agree on 40% ('unique crafts' versus 'crafted items' is the same set). Greed cannot steal them; Black hole and Fortress are crafts too. 'looted' implies crafts do not enter the gravestone loot; their fate at death is not stated.

### M-0522: Ingenuity craft recipes

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0522 `wiki-sigils-ingenuity-014`: "Made from Landmine Drone" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
- M-0522 `wiki-sigils-ingenuity-018`: "Made from Guardian angel Health potion" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
- M-0522 `wiki-sigils-ingenuity-022`: "Made from Anti poison Health potion" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-everything_potion))
- M-0522 `wiki-sigils-ingenuity-024`: "Made from Safety bubble Zombie repellent" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-zombie_killer))
- M-0522 `wiki-sigils-ingenuity-027`: "Made from EMP Mirror forcefield" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-black_hole))
- M-0522 `wiki-sigils-ingenuity-029`: "Made from Shield Body armor" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-fortress))

**Formal model:**

- M-0522 reading A: `craft(Robot) = Landmine + Drone; craft(Campfire) = Guardian angel + Health potion; craft(Everything potion) = Anti poison + Health potion; craft(Zombie killer) = Safety bubble + Zombie repellent; craft(Black hole) = EMP + Mirror forcefield; craft(Fortress) = Shield + Body armor; both ingredients consumed`
- M-0522 reading B: `only one ingredient is consumed`
- M-0522 domain: recipes are unordered pairs of item names as read from the labels
- M-0522 parameter `robot`: Landmine,Drone
- M-0522 parameter `campfire`: Guardian angel,Health potion
- M-0522 parameter `everything_potion`: Anti poison,Health potion
- M-0522 parameter `zombie_killer`: Safety bubble,Zombie repellent
- M-0522 parameter `black_hole`: EMP,Mirror forcefield
- M-0522 parameter `fortress`: Shield,Body armor

**Interactions:** M-0515, M-0520, M-0521

**Open questions:**

- [U-0517](../unknowns.md#u-0517) (high): Ingenuity crafts: are both named ingredients consumed, does a craft occupy one of the five craft slots, and how do six recipes fit five slots?

Notes (M-0522): Labels list the two ingredient names back to back without a separator; splitting is by known item names (Guardian angel, Health potion, Anti poison, Safety bubble, Zombie repellent, Mirror forcefield, Body armor, Landmine, Drone, EMP, Shield). The combined potion sizes feed Campfire and Everything potion. Crafts are not counted in the 3-effect item limit (items page).

### M-0528: Black hole craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0528 `wiki-sigils-ingenuity-028`: "Destroys every chest and crate within 200m (656ft), including care packages, airdrops and fake chests." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-black_hole))

**Formal model:**

- M-0528 reading A: `use at position x -> destroy every chest and crate with dist(x, c) <= 200 m, including care packages, airdrops and fake chests, at the instant of use`
- M-0528 reading B: `persistent field for an unstated duration`
- M-0528 domain: dist in metres 0..200
- M-0528 parameter `radius_m`: 200
- M-0528 parameter `duration_s`: UNKNOWN, see U-0523

**Interactions:** M-0521, M-0531

**Open questions:**

- [U-0523](../unknowns.md#u-0523) (medium): Black hole: is it instant or does it persist, centered where, and who gets the benefit?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

Notes (M-0528): Destruction of crates by any means can also pay Trolling (one token per crate destroyed, whoever spawned it) and Ingenuity tokens for chests (M-0521).

### M-0532: Fake chest placement

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- M-0532 `wiki-sigils-trolling-007`: "Fake chest: place up to 2 per rolling hour." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- M-0532 `wiki-sigils-trolling-008`: "It looks like a care package." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- M-0532 `wiki-sigils-trolling-011`: "It vanishes after 1h." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))

**Formal model:**

- M-0532 reading A: `place(fake chest) allowed iff fewer than 2 placements in the previous 3600 s; it looks like a care package; it vanishes 3600 s after placement`
- M-0532 reading B: `two charges regained one per 1800 s`
- M-0532 reading C: `2 per clock hour`
- M-0532 domain: time in seconds
- M-0532 parameter `limit`: 2
- M-0532 parameter `window_s`: 3600
- M-0532 parameter `lifetime_s`: 3600
- M-0532 parameter `limit_semantics`: UNKNOWN, see U-0530

**Interactions:** M-0517, M-0533

**Open questions:**

- [U-0530](../unknowns.md#u-0530) (medium): Fake chest 'up to 2 per rolling hour': sliding window over placement times, or two charges that refill?

Notes (M-0532): Since it lasts 1 h, the active count under reading A is at most 2. Only Ingenuity recognizes fakes (M-0517). Location constraints and the item shown are not stated.

### M-0534: Fake gravestone

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- M-0534 `wiki-sigils-trolling-013`: "Fake gravestone: place one, then wait 2h before the next." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- M-0534 `wiki-sigils-trolling-014`: "It copies the gravestone of an eliminated contestant, or of a random living one while nobody is eliminated." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- M-0534 `wiki-sigils-trolling-015`: "Each contestant who tries to loot it is poisoned once." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))

**Formal model:**

- M-0534 reading A: `place at most one; next placement allowed 7200 s after placement; copy = gravestone of an eliminated contestant chosen by the troll, else a random living contestant's if nobody is eliminated; each contestant who tries to loot it is poisoned once (first attempt only)`
- M-0534 reading B: `2 h wait counted from the moment the previous fake disappears`
- M-0534 reading C: `copy chosen at random among eliminated contestants`
- M-0534 domain: time in seconds
- M-0534 parameter `cooldown_s`: 7200
- M-0534 parameter `lifetime_s`: UNKNOWN, see U-0533
- M-0534 parameter `copy_source`: UNKNOWN, see U-0534
- M-0534 parameter `poison`: once per contestant

**Interactions:** M-0517

**Open questions:**

- [U-0533](../unknowns.md#u-0533) (medium): Fake gravestone: how long does it last, and does the 2 h wait start at placement or when the previous one disappears?
- [U-0534](../unknowns.md#u-0534) (low): Fake gravestone copy source: when someone is eliminated, who chooses which eliminated contestant is copied?

Notes (M-0534): Poison details (1 HP every 1 min 30 s, resets, does not stack) are on the poison page; a fake gravestone is one of the two poisoning sources there. A Mirror forcefield turns it back on the attacker. Ingenuity recognizes fakes. Death-sigil robbing of a fake gravestone is not described.

### M-0537: Unsafe circle defense item loss

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- M-0537 `wiki-sigils-trolling-017`: "loses one defense item or unique craft every five seconds, equipped Body Armor included" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- M-0537 `wiki-sigils-trolling-024`: "After your first hit, you lose one random defense item or unique craft every five seconds while you stay inside and are not immune." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- M-0537 `wiki-sigils-trolling-025`: "Defense items are Shields, Safety Bubbles, Guardian Angels, Hazmat Suits, Body Armor, Mirror Forcefields, Flak Jackets, Gas Masks, Zombie Repellents, Anti Poisons and Sleeping Bags." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- M-0537 `wiki-sigils-trolling-026`: "Equipped Body Armor is not safe." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))

**Formal model:**

- M-0537 reading A: `from the first hit, every 5 s while inside and not immune: remove one random item from {Shield, Safety Bubble, Guardian Angel, Hazmat Suit, Body Armor, Mirror Forcefield, Flak Jacket, Gas Mask, Zombie Repellent, Anti Poison, Sleeping Bag} or a unique craft; first loss at t_hit + 5 s`
- M-0537 reading B: `first loss at the first hit`
- M-0537 reading C: `clock from entry`
- M-0537 domain: 5 s period; random uniform over the held qualifying items (distribution not stated)
- M-0537 parameter `period_s`: 5
- M-0537 parameter `defense_item_types`: 11
- M-0537 parameter `fate`: UNKNOWN, see U-0539
- M-0537 parameter `clock_start`: UNKNOWN, see U-0538

**Interactions:** M-0536

**Open questions:**

- [U-0538](../unknowns.md#u-0538) (high): Unsafe circle item loss: when does the first loss happen relative to entry and to the first hit?
- [U-0539](../unknowns.md#u-0539) (medium): Unsafe circle item loss: is the lost item destroyed or dropped, does 'not immune' pause the clock or just skip the loss, and are active effects (not inventory) affected?

**Contradictions:** [C-0503](../unknowns.md#c-0503)

Notes (M-0537): Equipped Body Armor is explicitly not safe. The defense list excludes the sigil abilities Reality Shield and Death Ward. Uniformity of the random choice is not stated.

### M-0620: Endurance inventory: 10 slots instead of 3

Label: `DOCUMENTED`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- M-0620 `wiki-sigils-endurance-008`: "You have 10 inventory slots instead of 3." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- M-0620 reading A: `slots = 10`
- M-0620 parameter `inventory_slots`: 10

Notes (M-0620): Same value as the Slots label (M-0603). Merchant page allows up to 20 for Endurance with purchases.

### M-0621: Endurance care package schedule

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- M-0621 `wiki-sigils-endurance-009`: "Every 2h 30min, a care package falls within 10m (33ft) of you." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
- M-0621 `wiki-sigils-endurance-013`: "Every 2h 30min, a care package falls within 10m (33ft) of each Endurance contestant." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
- M-0621 `wiki-sigils-endurance-014`: "It lands after 30s." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
- M-0621 `wiki-sigils-endurance-010`: "Anyone can claim it." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
- M-0621 `wiki-sigils-endurance-015`: "After it lands it is a normal care package: any contestant can claim it." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
- M-0621 `wiki-sigils-endurance-016`: "It never holds a health potion or drone." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))

**Formal model:**

- M-0621 reading A: `t_k = t0 + k*9000 s fixed clock; landing at t_k + 30 s; position within 10 m of the contestant`
- M-0621 reading B: `timer restarts when the previous package is claimed`
- M-0621 domain: seconds
- M-0621 parameter `period_s`: 9000
- M-0621 parameter `landing_delay_s`: 30
- M-0621 parameter `t0`: UNKNOWN, see U-0607

**Open questions:**

- [U-0607](../unknowns.md#u-0607) (high): Endurance care packages 'every 2h 30min': first drop 2h30 after the event start, after the sigil pick, or after the previous claim, and which packages are 'your own'?

Notes (M-0621): Position at time of drop vs landing is not specified (the 10m is from the contestant when it falls). Contents are random items except health potion and drone.

### M-0624: Endurance restrictions: no trade, no gravestone loot, no drop, no pickup

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- M-0624 `wiki-sigils-endurance-011`: "You cannot trade, loot gravestones, drop items or pick up dropped items." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
- M-0624 `wiki-sigils-endurance-012`: "You can still destroy items, claim chests and take crates." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- M-0624 reading A: `actions {trade, loot_gravestone, drop_item, pickup_dropped_item} disabled; {destroy_item, claim_chest, take_crate, claim_care_package} enabled`
- M-0624 reading B: `A, and incoming trade offers from others also refused`

**Open questions:**

- [U-0610](../unknowns.md#u-0610) (medium): Endurance 'cannot trade, loot gravestones, drop items or pick up dropped items': does trade ban cover receiving offers from others, giving gifts, and the items returned by a revive?

Notes (M-0624): Disables looting gravestones: an Endurance contestant cannot rob or collect items from graves. Claiming care packages is allowed by the earn-tokens rule.

## Simulation check

Theorems with tests in `sim/tests/`: [T-0008](../theorems/T-0008.md), [T-0012](../theorems/T-0012.md)

## Open questions

[U-0003](../unknowns.md#u-0003), [U-0005](../unknowns.md#u-0005), [U-0015](../unknowns.md#u-0015), [U-0120](../unknowns.md#u-0120), [U-0122](../unknowns.md#u-0122), [U-0200](../unknowns.md#u-0200), [U-0201](../unknowns.md#u-0201), [U-0202](../unknowns.md#u-0202), [U-0205](../unknowns.md#u-0205), [U-0206](../unknowns.md#u-0206), [U-0207](../unknowns.md#u-0207), [U-0208](../unknowns.md#u-0208), [U-0209](../unknowns.md#u-0209), [U-0210](../unknowns.md#u-0210), [U-0211](../unknowns.md#u-0211), [U-0212](../unknowns.md#u-0212), [U-0213](../unknowns.md#u-0213), [U-0215](../unknowns.md#u-0215), [U-0216](../unknowns.md#u-0216), [U-0217](../unknowns.md#u-0217), [U-0218](../unknowns.md#u-0218), [U-0300](../unknowns.md#u-0300), [U-0321](../unknowns.md#u-0321), [U-0324](../unknowns.md#u-0324), [U-0325](../unknowns.md#u-0325), [U-0326](../unknowns.md#u-0326), [U-0327](../unknowns.md#u-0327), [U-0328](../unknowns.md#u-0328), [U-0338](../unknowns.md#u-0338), [U-0339](../unknowns.md#u-0339), [U-0340](../unknowns.md#u-0340), [U-0504](../unknowns.md#u-0504), [U-0505](../unknowns.md#u-0505), [U-0506](../unknowns.md#u-0506), [U-0511](../unknowns.md#u-0511), [U-0515](../unknowns.md#u-0515), [U-0516](../unknowns.md#u-0516), [U-0517](../unknowns.md#u-0517), [U-0518](../unknowns.md#u-0518), [U-0523](../unknowns.md#u-0523), [U-0530](../unknowns.md#u-0530), [U-0533](../unknowns.md#u-0533), [U-0534](../unknowns.md#u-0534), [U-0538](../unknowns.md#u-0538), [U-0539](../unknowns.md#u-0539), [U-0607](../unknowns.md#u-0607), [U-0610](../unknowns.md#u-0610)

## Confidence

`CONTRADICTED`: the lowest label among the rules on this page.
