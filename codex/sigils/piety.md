# Sigil of Piety

## Summary

Rules that name the Sigil of Piety, as the wiki states them on 2026-11-11.

This page gathers 10 rules (6 `DOCUMENTED`, 4 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0202: Piety health potion stack of 6

Label: `DOCUMENTED`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0202 `wiki-items-003`: "Piety contestants stack up to 6 health potions in one slot." ([source](https://iceposeidon.com/safezone/wiki/items#inventory))

**Formal model:**

- M-0202 reading A: `all health potions of a Piety contestant share one slot, count <= 6`
- M-0202 domain: potion count 0..6

**Interactions:** M-0207

Notes (M-0202): Equal to the Piety page (all your health potions share one inventory slot, up to 6). For other contestants the Items page says nothing about potion stacking (see U-0200).

### M-0333: Maximum HP upgrade ladder

Label: `CONDITIONAL`. Sigils: all, piety.

**Official text** (snapshot 2026-11-11):

- M-0333 `wiki-merchant-036`: "+10 maximum HP: starts at 40 blood tokens and costs 10 more for each one you already bought." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0333 `wiki-merchant-037`: "Maximum HP goes up to 200, or 220 for Piety." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0333 reading A: `the k-th purchase costs 40 + 10*k tokens and adds 10 to maximum HP; maximum HP is capped at 200, or 220 for Piety`
- M-0333 domain: k integer >= 0
- M-0333 parameter `hp_ladder_start`: 40
- M-0333 parameter `hp_ladder_step`: 10
- M-0333 parameter `hp_per_purchase`: 10
- M-0333 parameter `hp_cap_default`: 200
- M-0333 parameter `hp_cap_piety`: 220
- M-0333 parameter `hp_purchase_limit`: UNKNOWN, see U-0330

**Open questions:**

- [U-0329](../unknowns.md#u-0329) (high): Are the 'for each one you already bought' counters of Inventory slot and +10 maximum HP separate, or shared?
- [U-0330](../unknowns.md#u-0330) (medium): Max HP upgrade: is there a purchase limit in addition to the HP cap (200, or 220 for Piety), and how many purchases reach each cap per sigil?
- [U-0331](../unknowns.md#u-0331) (medium): Does '+10 maximum HP' also raise current HP by 10?
- [U-0322](../unknowns.md#u-0322) (high): How does Ingenuity's 'pay 10% more, rounded up' apply to the 40 + 10k upgrade ladders?
- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?

Notes (M-0333): Base max HP: Greed 90, Piety 110, others 100 (sigil pages). The cap is the only stated limit.

### M-0500: Piety base max HP and inventory slots

Label: `DOCUMENTED`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0500 `wiki-sigils-piety-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- M-0500 `wiki-sigils-piety-003`: "110 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- M-0500 `wiki-sigils-piety-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- M-0500 `wiki-sigils-piety-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- M-0500 `wiki-sigils-piety-006`: "Your max HP is 10 HP higher." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))

**Formal model:**

- M-0500 reading A: `maxHP_piety = 110; slots_piety = 3; maxHP = base + 10 where base = 100 (the Ingenuity and Trolling labels give 100)`
- M-0500 domain: integer HP and slot counts at event start
- M-0500 parameter `max_hp`: 110
- M-0500 parameter `slots`: 3
- M-0500 parameter `max_hp_delta_vs_base`: +10

**Interactions:** M-0506

Notes (M-0500): Stat labels are read as pairs (label 'Max HP' then '110 HP'; label 'Slots' then '3'). The sentence 'Your max HP is 10 HP higher' agrees with 110 against a base of 100. The merchant page raises the maximum HP cap to 220 for Piety; that is the merchant formalizer's record. Starting HP equal to max HP is not stated on this page.

### M-0501: Piety blood tokens from healing

Label: `CONDITIONAL`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0501 `wiki-sigils-piety-007`: "Earn one blood token per 5 HP healed from any source except revives, Campfires and healing circles included." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))

**Formal model:**

- M-0501 reading A: `tokens += floor(H_total / 5) over cumulative qualifying HP; all healing except revives counts, Campfire and healing circles included`
- M-0501 reading B: `tokens += floor(h / 5) per event, remainder dropped, same exclusion list`
- M-0501 reading C: `Campfires, healing circles and revives are all excluded from the count`
- M-0501 domain: h integer >= 0 per heal event; H_total cumulative
- M-0501 parameter `hp_per_token`: 5
- M-0501 parameter `tokens_per_step`: 1
- M-0501 parameter `hp_basis`: UNKNOWN, see U-0501

**Interactions:** M-0502, M-0505

**Open questions:**

- [U-0500](../unknowns.md#u-0500) (high): Piety 'one blood token per 5 HP healed': is the remainder carried between heal events (cumulative counter) or floored per event?
- [U-0501](../unknowns.md#u-0501) (high): Piety token counter: does 'HP healed' mean the nominal potion amount or the HP actually restored, and is the +15% bonus included?
- [U-0502](../unknowns.md#u-0502) (high): Piety 'from any source except revives, Campfires and healing circles included': are Campfires and healing circles counted (only revives excluded) or excluded together with revives?

Notes (M-0501): Sources named: any healing except revives. Potions, bandages, Healing sigil heals and Campfires are candidate sources. Converted potions never heal, see the conversion mechanic. The +15% potion bonus changes the HP that a potion heals, so which of the nominal or boosted value counts is in U-0501.

### M-0502: Piety potion to blood token conversion

Label: `DOCUMENTED`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0502 `wiki-sigils-piety-008`: "Convert small, medium, large or gigantic potions into 1, 2, 3 or 4 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
- M-0502 `wiki-sigils-piety-009`: "Converted potions do not count as healing." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))

**Formal model:**

- M-0502 reading A: `tokens(small)=1, tokens(medium)=2, tokens(large)=3, tokens(gigantic)=4 per potion converted; a converted potion heals nothing and produces no healing-token credit`
- M-0502 domain: potion tier in {small, medium, large, gigantic}; count 0..6 in the stack
- M-0502 parameter `small`: 1
- M-0502 parameter `medium`: 2
- M-0502 parameter `large`: 3
- M-0502 parameter `gigantic`: 4

**Interactions:** M-0501, M-0503

Notes (M-0502): The page gives no cooldown or location for the conversion action. Piety tokens from healing (M-0501) are not earned for converted potions because they are not healing. Potion heal values are on the items page: Small 5, Medium 10, Large 20, Gigantic 40 HP (not cited here: those are another family's clauses).

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

### M-0505: Piety health potion bonus of 15%

Label: `CONDITIONAL`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- M-0505 `wiki-sigils-piety-013`: "Health potions heal you 15% more, rounded down." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))

**Formal model:**

- M-0505 reading A: `heal(h) = floor(1.15 * h): tiers 5, 10, 20, 40 give 5, 11, 23, 46`
- M-0505 reading B: `heal(h) = h + floor(0.15 * h): same values as A on every integer h`
- M-0505 reading C: `heal = floor(1.15 * min(h, missing HP)): bonus applied to the effective heal`
- M-0505 domain: h in {5, 10, 20, 40}; binary64 1.15*h gives 5.75, 11.5, 23.0, 46.0 so floor equals the exact values
- M-0505 parameter `bonus`: 15%

**Interactions:** M-0501, M-0525

**Open questions:**

- [U-0503](../unknowns.md#u-0503) (medium): Piety 'heal you 15% more, rounded down': what is rounded, and at which step relative to the max-HP clamp?
- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?

Notes (M-0505): Only 'Health potions' are named. The Campfire pool and Everything potion are separate effects: the Ingenuity page says Piety and Protection potion changes do not apply to the Campfire. The Protection sigil heals 50% less from potions (another page).

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

### M-0507: Piety immunity to theft by Greed

Label: `DOCUMENTED`. Sigils: piety, greed.

**Official text** (snapshot 2026-11-11):

- M-0507 `wiki-sigils-piety-015`: "You are immune to having your items stolen by Greed players." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
- M-0507 `wiki-sigils-greed-017`: "You cannot steal from Piety players." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- M-0507 reading A: `steal(thief, victim) is refused when victim has sigil Piety`
- M-0507 domain: any thief with sigil Greed, any victim with sigil Piety

**Interactions:** M-0509

Notes (M-0507): The two pages say the same thing from each side. Does not protect Piety contestants from other sources of item loss (zombie breakage, unsafe circle loss for defense items).

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0006](../unknowns.md#u-0006), [U-0015](../unknowns.md#u-0015), [U-0322](../unknowns.md#u-0322), [U-0329](../unknowns.md#u-0329), [U-0330](../unknowns.md#u-0330), [U-0331](../unknowns.md#u-0331), [U-0500](../unknowns.md#u-0500), [U-0501](../unknowns.md#u-0501), [U-0502](../unknowns.md#u-0502), [U-0503](../unknowns.md#u-0503), [U-0504](../unknowns.md#u-0504), [U-0505](../unknowns.md#u-0505), [U-0506](../unknowns.md#u-0506)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
