# Sigil of Ingenuity

## Summary

Rules that name the Sigil of Ingenuity, as the wiki states them on 2026-11-11.

### In plain words

Ingenuity is the "inventor" class. It starts a bit cramped, with 100 maximum HP, 2 inventory slots and 5 separate slots for unique crafts ([M-0515](../rules/sigil.md#m-0515)), and pays 10% more at the merchant, rounded up ([M-0516](../rules/economy.md#m-0516)). In return it gets tools nobody else has: crafting, trapped gifts and good eyes.

Crafting combines two items into something new: Landmine plus Drone gives a Robot, Guardian angel plus Health potion gives a Campfire, Anti poison plus Health potion gives an Everything potion, Safety bubble plus Zombie repellent gives a Zombie killer, EMP plus Mirror forcefield gives a Black hole, and Shield plus Body armor gives a Fortress ([M-0522](../rules/items.md#m-0522)). Whether both ingredients are used up is open, [U-0517](../unknowns.md#u-0517). Crafts cannot be traded, stolen or looted, and zombie hits can destroy them with a 40% chance ([M-0520](../rules/items.md#m-0520)); how that roll works is open, [U-0518](../unknowns.md#u-0518).

What you get: the Robot hits other players within 10 m for 1 HP every 2 seconds for ten minutes ([M-0523](../rules/weapons.md#m-0523)). The Campfire heals everyone within 10 m from one shared pool ([M-0525](../rules/healing.md#m-0525)). The Everything potion cures poison and heals by tier ([M-0526](../rules/healing.md#m-0526)). The Zombie killer kills the next ten zombies near you and stops their drain meanwhile ([M-0527](../rules/zombies.md#m-0527)). The Black hole destroys every chest and crate within 200 m ([M-0528](../rules/items.md#m-0528)). The Fortress protects people within 20 m for up to 30 HP and blocks Greed stealing ([M-0529](../rules/damage.md#m-0529)).

Other tricks: attach a landmine or C4 to an item as a trapped gift, once every 16 hours ([M-0519](../rules/items.md#m-0519)); recognize fake chests and gravestones, see traps, and hack landmines or C4 within 50 m ([M-0517](../rules/sigil.md#m-0517)); combine two matching potions into the next size ([M-0518](../rules/items.md#m-0518)).

Strongest as written: the range of tools, and knowing about traps and fakes ([M-0517](../rules/sigil.md#m-0517)). Zombie drain is one thing it handles well, through the Zombie killer ([M-0527](../rules/zombies.md#m-0527)).

Weakest: the cramped start ([M-0515](../rules/sigil.md#m-0515)), the surcharge ([M-0516](../rules/economy.md#m-0516)), and fragile crafts ([M-0520](../rules/items.md#m-0520)).

What is unknown is a lot. Whether the surcharge hits the upgrade ladders is open, [U-0322](../unknowns.md#u-0322). Whether prices use exact or floating arithmetic changes some prices by one token, and this is open, [U-0006](../unknowns.md#u-0006). The wiki disagrees with itself about whether Shield and Sleeping Bag stop Robot damage ([M-0524](../rules/damage.md#m-0524), [C-0500](../unknowns.md#c-0500)). The Fortress pool may be shared or per person ([U-0524](../unknowns.md#u-0524)), and its lifetime is open ([U-0526](../unknowns.md#u-0526)). The Black hole may be instant or persistent ([U-0523](../unknowns.md#u-0523)). Hacking has no stated effect ([U-0514](../unknowns.md#u-0514)).

This page gathers 24 rules (23 `CONDITIONAL`, 1 `UNKNOWN`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0303"></a>

### M-0303: C4 trapped gift (Ingenuity attach)

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-007`: "With the Ingenuity sigil you can attach one C4 to another item you hold, once every 16h." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-009`: "Detonate it while another contestant holds that item." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-010`: "Only that contestant takes 23 HP." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- [M-0303](../rules/weapons.md#m-0303) `wiki-weapons-011`: "It does not hurt you while you hold the item." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))

**Formal model:**

- [M-0303](../rules/weapons.md#m-0303) reading A: `attach one C4 to another item held, at most once per 16h; detonate while another contestant holds it: only that contestant takes 23 HP; the owner is not hurt while holding it`
- [M-0303](../rules/weapons.md#m-0303) domain: HP, hours
- [M-0303](../rules/weapons.md#m-0303) parameter `trapped_gift_c4_damage_hp`: 23
- [M-0303](../rules/weapons.md#m-0303) parameter `attach_cooldown_h`: 16

**Open questions:**

- [U-0301](../unknowns.md#u-0301) (medium): Is the 'once every 16h' Ingenuity trap attachment limit one shared timer for C4 and landmine, or one timer per kind, and does it start at attachment or at detonation?

Notes ([M-0303](../rules/weapons.md#m-0303)): 23 HP is recorded as stated, no derivation. Trapped gifts appear in other pages' blocker tables (Shield, Sleeping Bag, Protection, Mirror) and in the Kick bonus list.

<a id="m-0304"></a>

### M-0304: C4 visibility

Label: `CONDITIONAL`. Sigils: all, ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0304](../rules/weapons.md#m-0304) `wiki-weapons-008`: "Only you can see the trap." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))
- [M-0304](../rules/weapons.md#m-0304) `wiki-weapons-014`: "Only you and Sigil of Ingenuity contestants can see it." ([source](https://iceposeidon.com/safezone/wiki/weapons#c4))

**Formal model:**

- [M-0304](../rules/weapons.md#m-0304) reading A: `a placed C4 is visible only to its owner and Sigil of Ingenuity contestants; the trapped gift is visible only to the owner`
- [M-0304](../rules/weapons.md#m-0304) reading B: `'Only you can see the trap' describes the placed C4 (the later sentence repeating it with Ingenuity added)`

**Open questions:**

- [U-0302](../unknowns.md#u-0302) (low): Does 'Only you can see the trap.' (C4 section) describe the trapped gift (item with attached C4) or the placed C4?

Notes ([M-0304](../rules/weapons.md#m-0304)): Unlike the landmine, no proximity visibility for other contestants and no viewer visibility is stated for C4.

<a id="m-0308"></a>

### M-0308: Landmine trapped gift (Ingenuity attach)

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0308](../rules/weapons.md#m-0308) `wiki-weapons-022`: "With the Ingenuity sigil you can attach one landmine to an item you use on yourself, once every 16h." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- [M-0308](../rules/weapons.md#m-0308) `wiki-weapons-024`: "It fires when another contestant uses that item, the item is used up and its effect does not apply." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- [M-0308](../rules/weapons.md#m-0308) `wiki-weapons-025`: "Only that contestant takes 11 HP." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))

**Formal model:**

- [M-0308](../rules/weapons.md#m-0308) reading A: `attach one landmine to an item used on yourself, at most once per 16h; it fires when another contestant uses that item: the item is used up, its effect does not apply, only that contestant takes 11 HP`
- [M-0308](../rules/weapons.md#m-0308) domain: HP, hours
- [M-0308](../rules/weapons.md#m-0308) parameter `trapped_gift_landmine_damage_hp`: 11
- [M-0308](../rules/weapons.md#m-0308) parameter `attach_cooldown_h`: 16

**Open questions:**

- [U-0301](../unknowns.md#u-0301) (medium): Is the 'once every 16h' Ingenuity trap attachment limit one shared timer for C4 and landmine, or one timer per kind, and does it start at attachment or at detonation?
- [U-0306](../unknowns.md#u-0306) (medium): Which items count for the Ingenuity landmine attachment 'an item you use on yourself'?

Notes ([M-0308](../rules/weapons.md#m-0308)): 11 HP is recorded as stated, no derivation.

<a id="m-0309"></a>

### M-0309: Landmine visibility

Label: `CONDITIONAL`. Sigils: all, ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-023`: "Only you can see the trap." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-026`: "Other contestants see it only within 20m (66ft) of it." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-027`: "A Sigil of Ingenuity always sees it." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))
- [M-0309](../rules/weapons.md#m-0309) `wiki-weapons-028`: "Viewers always see it." ([source](https://iceposeidon.com/safezone/wiki/weapons#landmine))

**Formal model:**

- [M-0309](../rules/weapons.md#m-0309) reading A: `the owner sees it; other contestants see it only within 20 m of it; Sigil of Ingenuity contestants always see it; viewers always see it`
- [M-0309](../rules/weapons.md#m-0309) domain: distance in metres
- [M-0309](../rules/weapons.md#m-0309) parameter `other_see_radius_m`: 20

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?

Notes ([M-0309](../rules/weapons.md#m-0309)): 'Only you can see the trap' follows the attach sentence and is the trapped gift (item), by position; the placed landmine rule is the next sentences.

<a id="m-0323"></a>

### M-0323: Ingenuity merchant surcharge

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0323](../rules/economy.md#m-0323) `wiki-merchant-011`: "Ingenuity contestants pay 10% more, rounded up." ([source](https://iceposeidon.com/safezone/wiki/merchant#paying))

**Formal model:**

- [M-0323](../rules/economy.md#m-0323) reading A: `price p becomes ceil(11*p/10) (exact arithmetic)`
- [M-0323](../rules/economy.md#m-0323) reading B: `price p becomes ceil(p*1.1) in binary64`
- [M-0323](../rules/economy.md#m-0323) domain: integer p >= 1

**Open questions:**

- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?
- [U-0322](../unknowns.md#u-0322) (high): How does Ingenuity's 'pay 10% more, rounded up' apply to the 40 + 10k upgrade ladders?

Notes ([M-0323](../rules/economy.md#m-0323)): The same sentence is on the Ingenuity page ('Merchant prices are 10% higher, rounded up'), no contradiction. Readings A and B differ by 1 token at base 50, 90, 100, 110 ([U-0006](../unknowns.md#u-0006)). How the surcharge applies to the ladders is [U-0322](../unknowns.md#u-0322).

<a id="m-0332"></a>

### M-0332: Inventory slot upgrade ladder

Label: `CONDITIONAL`. Sigils: all, endurance, ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0332](../rules/economy.md#m-0332) `wiki-merchant-033`: "Inventory slot: starts at 40 blood tokens and costs 10 more for each one you already bought." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- [M-0332](../rules/economy.md#m-0332) `wiki-merchant-034`: "Buy up to 10 slots, to at most 13 slots, or 20 for Endurance." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- [M-0332](../rules/economy.md#m-0332) `wiki-merchant-035`: "Ingenuity tops out at 12." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- [M-0332](../rules/economy.md#m-0332) reading A: `the k-th purchase (k = 0, 1, ...) costs 40 + 10*k tokens; at most 10 purchases; slots = base + purchases, so at most 13 (base 3), 20 for Endurance (base 10), 12 for Ingenuity (base 2)`
- [M-0332](../rules/economy.md#m-0332) domain: k integer, 0 <= k <= 9
- [M-0332](../rules/economy.md#m-0332) parameter `slot_ladder_start`: 40
- [M-0332](../rules/economy.md#m-0332) parameter `slot_ladder_step`: 10
- [M-0332](../rules/economy.md#m-0332) parameter `slot_purchase_max`: 10
- [M-0332](../rules/economy.md#m-0332) parameter `slot_cap_default`: 13
- [M-0332](../rules/economy.md#m-0332) parameter `slot_cap_endurance`: 20
- [M-0332](../rules/economy.md#m-0332) parameter `slot_cap_ingenuity`: 12

**Open questions:**

- [U-0329](../unknowns.md#u-0329) (high): Are the 'for each one you already bought' counters of Inventory slot and +10 maximum HP separate, or shared?
- [U-0322](../unknowns.md#u-0322) (high): How does Ingenuity's 'pay 10% more, rounded up' apply to the 40 + 10k upgrade ladders?
- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?

Notes ([M-0332](../rules/economy.md#m-0332)): Cross-check with sigil pages: Ingenuity starts with 2 slots (2+10=12), Endurance 10 (10+10=20), others 3 (3+10=13): consistent, no contradiction.

<a id="m-0444"></a>

### M-0444: Zombies destroy crafted items

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0444](../rules/zombies.md#m-0444) `wiki-zombies-004`: "a 40% chance to destroy crafted items" ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- [M-0444](../rules/zombies.md#m-0444) reading A: `p = 0.4 per drain tick, one random craft`
- [M-0444](../rules/zombies.md#m-0444) reading B: `per encounter`
- [M-0444](../rules/zombies.md#m-0444) reading C: `each craft independently`
- [M-0444](../rules/zombies.md#m-0444) domain: p in {0.4}
- [M-0444](../rules/zombies.md#m-0444) parameter `p`: 0.4

**Interactions:** [M-0441](../rules/zombies.md#m-0441)

**Open questions:**

- [U-0427](../unknowns.md#u-0427) (medium): Craft destruction roll: '40% chance to destroy crafted items' (the Ingenuity page says 'unique crafts' and 'Zombie hits'). Per drain tick or encounter, one item or all crafts, and are non-unique crafts included?

**Contradictions:** [C-0404](../unknowns.md#c-0404)

Notes ([M-0444](../rules/zombies.md#m-0444)): Ingenuity page says 'unique crafts' and 'Zombie hits' ([C-0404](../unknowns.md#c-0404)).

<a id="m-0453"></a>

### M-0453: Ingenuity Zombie Killer

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0453](../rules/zombies.md#m-0453) `wiki-zombies-016`: "An Ingenuity Zombie Killer kills the next ten zombies that come within 10m (33ft) of its owner." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))
- [M-0453](../rules/zombies.md#m-0453) `wiki-zombies-017`: "It has no time limit." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))
- [M-0453](../rules/zombies.md#m-0453) `wiki-zombies-020`: "An Ingenuity Zombie Killer also stops zombies draining you until it has killed ten." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

**Formal model:**

- [M-0453](../rules/zombies.md#m-0453) reading A: `kills the next 10 zombies that come within 10m of its owner; no time limit; stops zombie drain until ten are killed`
- [M-0453](../rules/zombies.md#m-0453) domain: count 0..10
- [M-0453](../rules/zombies.md#m-0453) parameter `kills`: 10
- [M-0453](../rules/zombies.md#m-0453) parameter `radius`: 10 m

**Consequences:** [T-0707](../theorems/T-0707.md)

**Open questions:**

- [U-0430](../unknowns.md#u-0430) (low): Ingenuity Zombie Killer: 'kills the next ten zombies that come within 10m of its owner' and 'stops zombies draining you until it has killed ten'. Do ten zombies arriving together count, is the drain stop limited to the ten, and is the order by approach?

<a id="m-0511"></a>

### M-0511: Fortress prevents stealing

Label: `CONDITIONAL`. Sigils: greed, ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0511](../rules/sigil.md#m-0511) `wiki-sigils-greed-008`: "Fortress protection prevents stealing." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- [M-0511](../rules/sigil.md#m-0511) `wiki-sigils-ingenuity-030`: "from Sigil of Greed stealing" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-fortress))

**Formal model:**

- [M-0511](../rules/sigil.md#m-0511) reading A: `steal(thief, victim) fails when victim stands within 20 m of an active fortress`
- [M-0511](../rules/sigil.md#m-0511) domain: victim position relative to fortress, 20 m radius
- [M-0511](../rules/sigil.md#m-0511) parameter `fortress_radius_m`: 20

**Interactions:** [M-0509](../rules/sigil.md#m-0509), [M-0529](../rules/damage.md#m-0529)

**Open questions:**

- [U-0526](../unknowns.md#u-0526) (high): Fortress lifetime and position: how long does it stay, and is it fixed where it is placed?

Notes ([M-0511](../rules/sigil.md#m-0511)): Depends on fortress presence over time (lifetime, [U-0526](../unknowns.md#u-0526)). Whether the thief inside a fortress can steal outside it is not stated.

<a id="m-0515"></a>

### M-0515: Ingenuity base max HP and slots

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0515](../rules/sigil.md#m-0515) `wiki-sigils-ingenuity-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity))
- [M-0515](../rules/sigil.md#m-0515) `wiki-sigils-ingenuity-003`: "100 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity))
- [M-0515](../rules/sigil.md#m-0515) `wiki-sigils-ingenuity-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity))
- [M-0515](../rules/sigil.md#m-0515) `wiki-sigils-ingenuity-005`: "2" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity))
- [M-0515](../rules/sigil.md#m-0515) `wiki-sigils-ingenuity-006`: "Start with 2 inventory slots and five separate slots for unique crafts." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
- [M-0515](../rules/sigil.md#m-0515) `wiki-merchant-035`: "Ingenuity tops out at 12." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- [M-0515](../rules/sigil.md#m-0515) reading A: `maxHP = 100; inventory slots = 2; plus 5 separate slots for unique crafts that do not use inventory slots; merchant slot upgrades cap at 12 total`
- [M-0515](../rules/sigil.md#m-0515) reading B: `the 5 craft slots hold crafts of any recipe, one each (6 recipes exist)`
- [M-0515](../rules/sigil.md#m-0515) reading C: `the 5 craft slots hold one craft per recipe type and crafts of one type stack`
- [M-0515](../rules/sigil.md#m-0515) domain: integer counts at event start
- [M-0515](../rules/sigil.md#m-0515) parameter `max_hp`: 100
- [M-0515](../rules/sigil.md#m-0515) parameter `inventory_slots`: 2
- [M-0515](../rules/sigil.md#m-0515) parameter `craft_slots`: 5
- [M-0515](../rules/sigil.md#m-0515) parameter `slot_cap_with_upgrades`: 12

**Consequences:** [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

**Interactions:** [M-0520](../rules/items.md#m-0520), [M-0522](../rules/items.md#m-0522)

**Open questions:**

- [U-0517](../unknowns.md#u-0517) (high): Ingenuity crafts: are both named ingredients consumed, does a craft occupy one of the five craft slots, and how do six recipes fit five slots?

Notes ([M-0515](../rules/sigil.md#m-0515)): Six recipes share five craft slots; how crafts occupy them is open. Items page: 'You can carry up to 3 items' is the ordinary default, replaced by the sigil value 2. The merchant page cap of 12 equals 2 + 10 purchases, consistent.

<a id="m-0516"></a>

### M-0516: Ingenuity merchant prices plus 10 percent rounded up

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0516](../rules/economy.md#m-0516) `wiki-sigils-ingenuity-007`: "Merchant prices are 10% higher, rounded up." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
- [M-0516](../rules/economy.md#m-0516) `wiki-merchant-011`: "Ingenuity contestants pay 10% more, rounded up." ([source](https://iceposeidon.com/safezone/wiki/merchant#paying))

**Formal model:**

- [M-0516](../rules/economy.md#m-0516) reading A: `price_I(p) = ceil(11 * p / 10), exact integers`
- [M-0516](../rules/economy.md#m-0516) reading B: `price_I(p) = ceil(p * 1.1) in IEEE 754 binary64: gives 56 for p=50, 100 for p=90, 111 for p=100, 122 for p=110 (one token more than A at those bases)`
- [M-0516](../rules/economy.md#m-0516) domain: p positive integer base price in blood tokens, e.g. 10, 12, 15, 20, 25, 30, 40, 50 and escalating 40+10k upgrades
- [M-0516](../rules/economy.md#m-0516) parameter `markup`: 10%
- [M-0516](../rules/economy.md#m-0516) parameter `rounding`: up

**Open questions:**

- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?

Notes ([M-0516](../rules/economy.md#m-0516)): This record is the Ingenuity-side statement; the merchant page repeats the same sentence (same meaning, no mismatch). Base prices: Care package 10, Anti poison 12, Vulnerability Dart 25, Sleeping Bag 30, Missile 10, Dual Wield 50, Deep Cut 20, weapon enchantment 15, armor enchantment 30, slots and HP upgrades from 40 (merchant page). Whether the markup applies to upgrades is stated by 'Merchant prices'.

<a id="m-0517"></a>

### M-0517: Ingenuity detection of fakes and traps, hacking of landmines and C4

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0517](../rules/sigil.md#m-0517) `wiki-sigils-ingenuity-008`: "Recognize fake chests and gravestones, see traps, and hack landmines or C4 within 50m (164ft)." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

**Formal model:**

- [M-0517](../rules/sigil.md#m-0517) reading A: `for entity e in {fake chest, fake gravestone, trap, landmine, C4}: Ingenuity sees e correctly iff dist <= 50; hack(e) allowed iff dist <= 50`
- [M-0517](../rules/sigil.md#m-0517) reading B: `only hack is limited to 50 m; recognition and trap sight have no range`
- [M-0517](../rules/sigil.md#m-0517) reading C: `recognition and sight map-wide; hack within 50 m`
- [M-0517](../rules/sigil.md#m-0517) domain: dist in metres 0..50
- [M-0517](../rules/sigil.md#m-0517) parameter `radius_m`: 50
- [M-0517](../rules/sigil.md#m-0517) parameter `hack_effect`: UNKNOWN, see [U-0514](../unknowns.md#u-0514)

**Interactions:** [M-0519](../rules/items.md#m-0519), [M-0521](../rules/economy.md#m-0521)

**Open questions:**

- [U-0513](../unknowns.md#u-0513) (medium): Ingenuity 'Recognize fake chests and gravestones, see traps, and hack landmines or C4 within 50m (164ft)': does the 50 m limit apply to all three abilities or only to hacking?
- [U-0514](../unknowns.md#u-0514) (high): What does 'hack' do to a landmine or C4, and is there a limit?

Notes ([M-0517](../rules/sigil.md#m-0517)): Other pages: Landmine page says a Sigil of Ingenuity always sees a placed landmine; Black hole destroys fake chests too. Ingenuity earns a blood token per hack.

<a id="m-0518"></a>

### M-0518: Ingenuity potion combining

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0518](../rules/items.md#m-0518) `wiki-sigils-ingenuity-009`: "Combine two matching potions into the next size, up to gigantic." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

**Formal model:**

- [M-0518](../rules/items.md#m-0518) reading A: `combine(p1, p2) with tier(p1) = tier(p2) < gigantic -> one potion of the next tier`
- [M-0518](../rules/items.md#m-0518) reading B: `any two matching potions of one kind combine`
- [M-0518](../rules/items.md#m-0518) domain: tiers small < medium < large < gigantic; heal values 5, 10, 20, 40 (items page) so combining is lossless
- [M-0518](../rules/items.md#m-0518) parameter `results`: small+small=medium; medium+medium=large; large+large=gigantic

**Interactions:** [M-0525](../rules/healing.md#m-0525), [M-0526](../rules/healing.md#m-0526)

**Open questions:**

- [U-0515](../unknowns.md#u-0515) (low): Ingenuity potion combining: what does 'two matching potions' mean, and are there costs or limits?

Notes ([M-0518](../rules/items.md#m-0518)): No cost or cooldown stated. Used as the Campfire and Everything potion ingredients: a combined potion sets the pool or the heal.

<a id="m-0519"></a>

### M-0519: Ingenuity trapped gift

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0519](../rules/items.md#m-0519) `wiki-sigils-ingenuity-010`: "Attach a landmine or C4 to an item to make a trapped gift, once every 16h." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
- [M-0519](../rules/items.md#m-0519) `wiki-sigils-ingenuity-011`: "Only you can see it is trapped." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

**Formal model:**

- [M-0519](../rules/items.md#m-0519) reading A: `attach(trap in {landmine, C4}, item) -> trapped gift; one shared cooldown 16 h = 57600 s; only the owner can see that it is trapped`
- [M-0519](../rules/items.md#m-0519) reading B: `separate 16 h cooldowns for landmine and C4`
- [M-0519](../rules/items.md#m-0519) reading C: `other Ingenuity contestants also see it`
- [M-0519](../rules/items.md#m-0519) domain: time in seconds
- [M-0519](../rules/items.md#m-0519) parameter `cooldown_s`: 57600
- [M-0519](../rules/items.md#m-0519) parameter `trap_types`: landmine, C4

**Interactions:** [M-0517](../rules/sigil.md#m-0517)

**Open questions:**

- [U-0516](../unknowns.md#u-0516) (medium): Trapped gift: is the 16 h limit shared between landmine and C4 attachments, and who can see the trap (the owner only, or also other Ingenuity contestants)?

Notes ([M-0519](../rules/items.md#m-0519)): The C4 page says C4 attaches 'to another item you hold' and the Landmine page 'to an item you use on yourself'; each repeats once every 16h. Damages (23 HP C4, 11 HP landmine) are on the weapons page and are not recorded here. A trapped gift ignores Body armor and hurts the holder through a Safety bubble (items page).

<a id="m-0520"></a>

### M-0520: Ingenuity unique craft restrictions and zombie destruction

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0520](../rules/items.md#m-0520) `wiki-sigils-ingenuity-012`: "Unique crafts cannot be traded, stolen or looted, and have a 40% chance to be destroyed by Zombie hits." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
- [M-0520](../rules/items.md#m-0520) `wiki-zombies-004`: "a 40% chance to destroy crafted items" ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- [M-0520](../rules/items.md#m-0520) reading A: `craft c: not tradable, not stealable, not lootable; each zombie drain hit: for every craft, destroy with probability 0.40`
- [M-0520](../rules/items.md#m-0520) reading B: `each zombie hit rolls once and destroys one random craft with probability 0.40`
- [M-0520](../rules/items.md#m-0520) reading C: `one 0.40 roll per zombie encounter`
- [M-0520](../rules/items.md#m-0520) domain: probability 0.4 per roll; hit rate per zombie is 1 drain per 10 s (guard zombie 2 HP per 5 s)
- [M-0520](../rules/items.md#m-0520) parameter `p_destroy`: 0.4
- [M-0520](../rules/items.md#m-0520) parameter `roll_unit`: UNKNOWN, see [U-0518](../unknowns.md#u-0518)

**Interactions:** [M-0522](../rules/items.md#m-0522), [M-0527](../rules/zombies.md#m-0527)

**Open questions:**

- [U-0518](../unknowns.md#u-0518) (high): Unique crafts '40% chance to be destroyed by Zombie hits': is the roll per drain hit, per zombie, or per craft, and does a blocked hit roll?

Notes ([M-0520](../rules/items.md#m-0520)): Ingenuity page and zombies page agree on 40% ('unique crafts' versus 'crafted items' is the same set). Greed cannot steal them; Black hole and Fortress are crafts too. 'looted' implies crafts do not enter the gravestone loot; their fate at death is not stated.

<a id="m-0521"></a>

### M-0521: Ingenuity blood token income

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0521](../rules/economy.md#m-0521) `wiki-sigils-ingenuity-013`: "Earn one blood token per craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

**Formal model:**

- [M-0521](../rules/economy.md#m-0521) reading A: `+1 token per craft; +1 per hack; +1 per real item chest destroyed by Black Hole; +1 per HP healed on anyone by the contestant's Campfire; +1 per zombie killed by the Zombie killer`
- [M-0521](../rules/economy.md#m-0521) reading B: `chests destroyed by Black Hole includes crates, care packages, airdrops and fake chests; zombie killed by any means`
- [M-0521](../rules/economy.md#m-0521) domain: events counted per occurrence; no cap stated
- [M-0521](../rules/economy.md#m-0521) parameter `per_craft`: 1
- [M-0521](../rules/economy.md#m-0521) parameter `per_hack`: 1
- [M-0521](../rules/economy.md#m-0521) parameter `per_chest_black_hole`: 1
- [M-0521](../rules/economy.md#m-0521) parameter `per_campfire_hp`: 1
- [M-0521](../rules/economy.md#m-0521) parameter `per_zombie_killed`: 1

**Consequences:** [T-0304](../theorems/T-0304.md), [T-0706](../theorems/T-0706.md)

**Interactions:** [M-0517](../rules/sigil.md#m-0517), [M-0522](../rules/items.md#m-0522), [M-0525](../rules/healing.md#m-0525), [M-0527](../rules/zombies.md#m-0527), [M-0528](../rules/items.md#m-0528)

**Open questions:**

- [U-0519](../unknowns.md#u-0519) (medium): Ingenuity income: what counts as 'craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed'?

Notes ([M-0521](../rules/economy.md#m-0521)): The Campfire term pays per HP (not per 5 HP), unlike Piety and Trolling.

<a id="m-0522"></a>

### M-0522: Ingenuity craft recipes

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-014`: "Made from Landmine Drone" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-018`: "Made from Guardian angel Health potion" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-022`: "Made from Anti poison Health potion" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-everything_potion))
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-024`: "Made from Safety bubble Zombie repellent" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-zombie_killer))
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-027`: "Made from EMP Mirror forcefield" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-black_hole))
- [M-0522](../rules/items.md#m-0522) `wiki-sigils-ingenuity-029`: "Made from Shield Body armor" ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-fortress))

**Formal model:**

- [M-0522](../rules/items.md#m-0522) reading A: `craft(Robot) = Landmine + Drone; craft(Campfire) = Guardian angel + Health potion; craft(Everything potion) = Anti poison + Health potion; craft(Zombie killer) = Safety bubble + Zombie repellent; craft(Black hole) = EMP + Mirror forcefield; craft(Fortress) = Shield + Body armor; both ingredients consumed`
- [M-0522](../rules/items.md#m-0522) reading B: `only one ingredient is consumed`
- [M-0522](../rules/items.md#m-0522) domain: recipes are unordered pairs of item names as read from the labels
- [M-0522](../rules/items.md#m-0522) parameter `robot`: Landmine,Drone
- [M-0522](../rules/items.md#m-0522) parameter `campfire`: Guardian angel,Health potion
- [M-0522](../rules/items.md#m-0522) parameter `everything_potion`: Anti poison,Health potion
- [M-0522](../rules/items.md#m-0522) parameter `zombie_killer`: Safety bubble,Zombie repellent
- [M-0522](../rules/items.md#m-0522) parameter `black_hole`: EMP,Mirror forcefield
- [M-0522](../rules/items.md#m-0522) parameter `fortress`: Shield,Body armor

**Interactions:** [M-0515](../rules/sigil.md#m-0515), [M-0520](../rules/items.md#m-0520), [M-0521](../rules/economy.md#m-0521)

**Open questions:**

- [U-0517](../unknowns.md#u-0517) (high): Ingenuity crafts: are both named ingredients consumed, does a craft occupy one of the five craft slots, and how do six recipes fit five slots?

Notes ([M-0522](../rules/items.md#m-0522)): Labels list the two ingredient names back to back without a separator; splitting is by known item names (Guardian angel, Health potion, Anti poison, Safety bubble, Zombie repellent, Mirror forcefield, Body armor, Landmine, Drone, EMP, Shield). The combined potion sizes feed Campfire and Everything potion. Crafts are not counted in the 3-effect item limit (items page).

<a id="m-0523"></a>

### M-0523: Robot craft damage and movement

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0523](../rules/weapons.md#m-0523) `wiki-sigils-ingenuity-015`: "For ten minutes it deals 1 HP every 2s to other players within 10m (33ft)." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
- [M-0523](../rules/weapons.md#m-0523) `wiki-sigils-ingenuity-017`: "Leave it still or pick a player to follow at 1.4m/s (3.13mph)." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))

**Formal model:**

- [M-0523](../rules/weapons.md#m-0523) reading A: `robot active for 600 s; global 2 s clock; each tick: every other player within 10 m takes 1 HP; robot stays still or follows a chosen player at 1.4 m/s`
- [M-0523](../rules/weapons.md#m-0523) reading B: `per-target timer, first hit 2 s after entry`
- [M-0523](../rules/weapons.md#m-0523) reading C: `per-target, first hit at entry then every 2 s`
- [M-0523](../rules/weapons.md#m-0523) domain: t in 0..600 s; distance in metres; speed 1.4 m/s (3.13 mph)
- [M-0523](../rules/weapons.md#m-0523) parameter `duration_s`: 600
- [M-0523](../rules/weapons.md#m-0523) parameter `interval_s`: 2
- [M-0523](../rules/weapons.md#m-0523) parameter `damage_hp`: 1
- [M-0523](../rules/weapons.md#m-0523) parameter `radius_m`: 10
- [M-0523](../rules/weapons.md#m-0523) parameter `speed_mps`: 1.4
- [M-0523](../rules/weapons.md#m-0523) parameter `clock`: UNKNOWN, see [U-0527](../unknowns.md#u-0527)

**Consequences:** [T-0305](../theorems/T-0305.md)

**Interactions:** [M-0522](../rules/items.md#m-0522), [M-0524](../rules/damage.md#m-0524)

**Open questions:**

- [U-0527](../unknowns.md#u-0527) (medium): Robot 'deals 1 HP every 2s to other players within 10m': is the 2 s clock global or per target, and does the first hit come immediately or after one interval?
- [U-0002](../unknowns.md#u-0002) (critical): For damage that is not a discrete attack (zone ticks, unsafe circle, robot, poison, tear gas, bleeding, zombie drain, Eddie's loss, Retribution), do pipeline steps 4b (the defender's Kick-live reduction), 5 (the 1 HP minimum) and 6 (fortress) apply? And are the guard zombie drain and the revive cost kinds of damage at all (neither has a row in the damage table)?

**Contradictions:** [C-0500](../unknowns.md#c-0500)

Notes ([M-0523](../rules/weapons.md#m-0523)): 'other players' excludes the owner. The robot is a damage-table source (another page); whether its damage passes the 7-step hit pipeline is [U-0002](../unknowns.md#u-0002). A merchant item lets a contestant give a robot a target (items page). Blockers are in [M-0524](../rules/damage.md#m-0524).

<a id="m-0524"></a>

### M-0524: Robot damage blockers

Label: `UNKNOWN`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0524](../rules/damage.md#m-0524) `wiki-sigils-ingenuity-016`: "Shields and Sleeping Bags stop it." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
- [M-0524](../rules/damage.md#m-0524) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [M-0524](../rules/damage.md#m-0524) `wiki-damage-007`: "Robot | Safety bubble, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0524](../rules/damage.md#m-0524) reading A: `robot damage is stopped by Shield and Sleeping Bag (Ingenuity page)`
- [M-0524](../rules/damage.md#m-0524) reading B: `robot damage is not stopped by Shield or by a Sleeping Bag (damage page); stopped by Safety bubble, slowed by Hazmat suit, absorbed by Body armor`
- [M-0524](../rules/damage.md#m-0524) domain: boolean block per defender state
- [M-0524](../rules/damage.md#m-0524) parameter `shield_blocks`: contradicted, see [C-0500](../unknowns.md#c-0500)
- [M-0524](../rules/damage.md#m-0524) parameter `sleeping_bag_blocks`: contradicted, see [C-0500](../unknowns.md#c-0500)

**Interactions:** [M-0523](../rules/weapons.md#m-0523)

**Contradictions:** [C-0500](../unknowns.md#c-0500)

Notes ([M-0524](../rules/damage.md#m-0524)): Contradiction [C-0500](../unknowns.md#c-0500). The damage page also lists robot damage as an exception to the sleeping-bag immunity.

<a id="m-0525"></a>

### M-0525: Campfire craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0525](../rules/healing.md#m-0525) `wiki-sigils-ingenuity-019`: "Heals everyone within 10m (33ft) 1 HP per second from one shared pool equal to the potion's heal." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
- [M-0525](../rules/healing.md#m-0525) `wiki-sigils-ingenuity-020`: "It burns out when the pool is empty or after 10min." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
- [M-0525](../rules/healing.md#m-0525) `wiki-sigils-ingenuity-021`: "Piety and Protection potion changes do not apply." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))

**Formal model:**

- [M-0525](../rules/healing.md#m-0525) reading A: `campfire pool = heal of the potion used (small 5, medium 10, large 20, gigantic 40 HP, base values); each second every contestant within 10 m with missing HP gets +1 HP and the pool -1; it ends at pool 0 or after 600 s`
- [M-0525](../rules/healing.md#m-0525) reading B: `pool pays 1 HP per second in total, shared`
- [M-0525](../rules/healing.md#m-0525) reading C: `every contestant in range drains 1 HP per second from the pool regardless of missing HP`
- [M-0525](../rules/healing.md#m-0525) domain: pool integer 0..40; duration 600 s
- [M-0525](../rules/healing.md#m-0525) parameter `rate_hp_per_s`: 1
- [M-0525](../rules/healing.md#m-0525) parameter `radius_m`: 10
- [M-0525](../rules/healing.md#m-0525) parameter `max_duration_s`: 600
- [M-0525](../rules/healing.md#m-0525) parameter `pool`: tier heal of the potion, no Piety +15%, no Protection -50%
- [M-0525](../rules/healing.md#m-0525) parameter `pool_drain`: UNKNOWN, see [U-0520](../unknowns.md#u-0520)

**Interactions:** [M-0501](../rules/economy.md#m-0501), [M-0505](../rules/healing.md#m-0505), [M-0518](../rules/items.md#m-0518), [M-0521](../rules/economy.md#m-0521)

**Open questions:**

- [U-0520](../unknowns.md#u-0520) (high): Campfire shared pool: how does the pool drain with several people, and are full-HP bystanders healed?
- [U-0502](../unknowns.md#u-0502) (high): Piety 'from any source except revives, Campfires and healing circles included': are Campfires and healing circles counted (only revives excluded) or excluded together with revives?

Notes ([M-0525](../rules/healing.md#m-0525)): Piety and Protection potion changes are stated not to apply, so the pool is the raw tier value. A heal from a Campfire counts as HP for the Ingenuity income (1 token per HP) and is in the Piety exclusion/inclusion question [U-0502](../unknowns.md#u-0502). 'Everyone' includes the owner and other sigils; enemies are not excluded.

<a id="m-0526"></a>

### M-0526: Everything potion craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0526](../rules/healing.md#m-0526) `wiki-sigils-ingenuity-023`: "Cures poison and heals by potion tier." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-everything_potion))

**Formal model:**

- [M-0526](../rules/healing.md#m-0526) reading A: `use -> cure poison; heal tier HP of the Health potion ingredient`
- [M-0526](../rules/healing.md#m-0526) reading B: `as A and also grant 600 s of poison immunity as the Anti poison item does`
- [M-0526](../rules/healing.md#m-0526) domain: tier in 5, 10, 20, 40 HP
- [M-0526](../rules/healing.md#m-0526) parameter `heal`: tier of the ingredient potion
- [M-0526](../rules/healing.md#m-0526) parameter `immunity`: UNKNOWN, see [U-0521](../unknowns.md#u-0521)

**Interactions:** [M-0518](../rules/items.md#m-0518), [M-0522](../rules/items.md#m-0522)

**Open questions:**

- [U-0521](../unknowns.md#u-0521) (low): Everything potion 'Cures poison and heals by potion tier': does it also grant the 10 min poison immunity of an Anti poison?

Notes ([M-0526](../rules/healing.md#m-0526)): The poison page lists Anti poison, Healing healing and God's Fruit as cures; the Everything potion cure is stated here only. Poison immunity from Anti poison lasts 10 min (items page).

<a id="m-0527"></a>

### M-0527: Zombie killer craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0527](../rules/zombies.md#m-0527) `wiki-sigils-ingenuity-025`: "Kills the next ten zombies that come within 10m (33ft) of you." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-zombie_killer))
- [M-0527](../rules/zombies.md#m-0527) `wiki-sigils-ingenuity-026`: "No time limit." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-zombie_killer))
- [M-0527](../rules/zombies.md#m-0527) `wiki-zombies-020`: "An Ingenuity Zombie Killer also stops zombies draining you until it has killed ten." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

**Formal model:**

- [M-0527](../rules/zombies.md#m-0527) reading A: `for the next 10 zombies that come within 10 m of the owner: kill the zombie; zombies do not drain the owner until 10 have been killed; no expiry`
- [M-0527](../rules/zombies.md#m-0527) reading B: `zombies already inside 10 m at use are not counted`
- [M-0527](../rules/zombies.md#m-0527) reading C: `guard zombies and horde zombies are excluded from the count`
- [M-0527](../rules/zombies.md#m-0527) domain: kills counter 0..10; radius 10 m; no time limit
- [M-0527](../rules/zombies.md#m-0527) parameter `kills`: 10
- [M-0527](../rules/zombies.md#m-0527) parameter `radius_m`: 10
- [M-0527](../rules/zombies.md#m-0527) parameter `expiry`: none

**Consequences:** [T-0707](../theorems/T-0707.md)

**Interactions:** [M-0520](../rules/items.md#m-0520), [M-0521](../rules/economy.md#m-0521)

**Open questions:**

- [U-0522](../unknowns.md#u-0522) (medium): Zombie killer 'Kills the next ten zombies that come within 10m': does it kill zombies already inside 10 m when used, which zombie types count, and are more than ten in range handled?

Notes ([M-0527](../rules/zombies.md#m-0527)): Zombies page repeats the same ten zombies and the same 10 m. Zombie drain range is 5 m and zombies chase at 1.4 m/s, so a zombie reaches 10 m before it can drain. Pays 1 token per zombie killed for Ingenuity ([M-0521](../rules/economy.md#m-0521)).

<a id="m-0528"></a>

### M-0528: Black hole craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0528](../rules/items.md#m-0528) `wiki-sigils-ingenuity-028`: "Destroys every chest and crate within 200m (656ft), including care packages, airdrops and fake chests." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-black_hole))

**Formal model:**

- [M-0528](../rules/items.md#m-0528) reading A: `use at position x -> destroy every chest and crate with dist(x, c) <= 200 m, including care packages, airdrops and fake chests, at the instant of use`
- [M-0528](../rules/items.md#m-0528) reading B: `persistent field for an unstated duration`
- [M-0528](../rules/items.md#m-0528) domain: dist in metres 0..200
- [M-0528](../rules/items.md#m-0528) parameter `radius_m`: 200
- [M-0528](../rules/items.md#m-0528) parameter `duration_s`: UNKNOWN, see [U-0523](../unknowns.md#u-0523)

**Interactions:** [M-0521](../rules/economy.md#m-0521), [M-0531](../rules/economy.md#m-0531)

**Open questions:**

- [U-0523](../unknowns.md#u-0523) (medium): Black hole: is it instant or does it persist, centered where, and who gets the benefit?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

Notes ([M-0528](../rules/items.md#m-0528)): Destruction of crates by any means can also pay Trolling (one token per crate destroyed, whoever spawned it) and Ingenuity tokens for chests ([M-0521](../rules/economy.md#m-0521)).

<a id="m-0529"></a>

### M-0529: Fortress craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0529](../rules/damage.md#m-0529) `wiki-sigils-ingenuity-030`: "Protects everyone within 20m (66ft) of it for up to 30 HP, and from Sigil of Greed stealing, and zone damage." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-fortress))
- [M-0529](../rules/damage.md#m-0529) `wiki-damage-052`: "A fortress you stand within absorbs up to its remaining durability, whoever built it." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0529](../rules/damage.md#m-0529) reading A: `fortress at x: every contestant within 20 m of x is protected; durability D = 30 shared; hit step 6 absorbs min(d, D) and D -= absorbed; also blocks Greed stealing; zone damage fully immunized`
- [M-0529](../rules/damage.md#m-0529) reading B: `30 HP of absorption for each protected contestant`
- [M-0529](../rules/damage.md#m-0529) reading C: `zone damage is absorbed from the durability`
- [M-0529](../rules/damage.md#m-0529) domain: dist in metres 0..20; D integer 0..30
- [M-0529](../rules/damage.md#m-0529) parameter `radius_m`: 20
- [M-0529](../rules/damage.md#m-0529) parameter `durability_hp`: 30
- [M-0529](../rules/damage.md#m-0529) parameter `duration_s`: UNKNOWN, see [U-0526](../unknowns.md#u-0526)

**Consequences:** [T-0007](../theorems/T-0007.md), [T-0008](../theorems/T-0008.md), [T-0305](../theorems/T-0305.md)

**Interactions:** [M-0511](../rules/sigil.md#m-0511), [M-0522](../rules/items.md#m-0522)

**Open questions:**

- [U-0524](../unknowns.md#u-0524) (high): Fortress 'up to 30 HP': one pool shared by everyone inside 20 m, or 30 HP for each person?
- [U-0525](../unknowns.md#u-0525) (high): Fortress and zone damage: is zone damage absorbed from the 30 HP durability or ignored entirely?
- [U-0526](../unknowns.md#u-0526) (high): Fortress lifetime and position: how long does it stay, and is it fixed where it is placed?

Notes ([M-0529](../rules/damage.md#m-0529)): Damage page: 'A fortress you stand within absorbs up to its remaining durability, whoever built it' (step 6, before Armor). The Ingenuity text lists three protections: HP absorption, Greed stealing and zone damage.

## Simulation check

Theorems with tests in `sim/tests/`: [T-0007](../theorems/T-0007.md), [T-0008](../theorems/T-0008.md), [T-0304](../theorems/T-0304.md), [T-0305](../theorems/T-0305.md), [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md), [T-0706](../theorems/T-0706.md), [T-0707](../theorems/T-0707.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0006](../unknowns.md#u-0006), [U-0015](../unknowns.md#u-0015), [U-0300](../unknowns.md#u-0300), [U-0301](../unknowns.md#u-0301), [U-0302](../unknowns.md#u-0302), [U-0306](../unknowns.md#u-0306), [U-0322](../unknowns.md#u-0322), [U-0329](../unknowns.md#u-0329), [U-0427](../unknowns.md#u-0427), [U-0430](../unknowns.md#u-0430), [U-0502](../unknowns.md#u-0502), [U-0513](../unknowns.md#u-0513), [U-0514](../unknowns.md#u-0514), [U-0515](../unknowns.md#u-0515), [U-0516](../unknowns.md#u-0516), [U-0517](../unknowns.md#u-0517), [U-0518](../unknowns.md#u-0518), [U-0519](../unknowns.md#u-0519), [U-0520](../unknowns.md#u-0520), [U-0521](../unknowns.md#u-0521), [U-0522](../unknowns.md#u-0522), [U-0523](../unknowns.md#u-0523), [U-0524](../unknowns.md#u-0524), [U-0525](../unknowns.md#u-0525), [U-0526](../unknowns.md#u-0526), [U-0527](../unknowns.md#u-0527)

## Confidence

`UNKNOWN`: the lowest label among the rules on this page.
