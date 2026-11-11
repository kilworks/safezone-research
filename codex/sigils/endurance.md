# Sigil of Endurance

## Summary

Rules that name the Sigil of Endurance, as the wiki states them on 2026-11-11.

### In plain words

Endurance is the "pack mule on a schedule" class. Its big difference is space: 10 inventory slots instead of 3 ([M-0620](../rules/items.md#m-0620), [M-0603](../rules/sigil.md#m-0603)), with the usual 100 maximum HP ([M-0603](../rules/sigil.md#m-0603)). The slot upgrade ladder lets Endurance reach 20 slots, against 13 for the ordinary case ([M-0332](../rules/economy.md#m-0332)).

The second feature is a delivery that comes to you. Every 2h 30min, a care package falls within 10 m (33 ft) of each Endurance contestant, and it lands after 30 seconds ([M-0621](../rules/items.md#m-0621)). It never holds a health potion or drone ([M-0621](../rules/items.md#m-0621)). Anyone can claim it, but if you claim one of your own you earn six blood tokens ([M-0622](../rules/economy.md#m-0622)), plus one more for every five item uses ([M-0623](../rules/economy.md#m-0623)).

The price of all this is a set of limits. You cannot trade, loot gravestones, drop items or pick up dropped items; you can still destroy items, claim chests and take crates ([M-0624](../rules/items.md#m-0624)). So Endurance cannot join the item economy between players, and cannot loot the dead.

What a player would feel: a roomy bag, a steady drip of income on a fixed rhythm, and a sense of being slightly outside the social part of the game. The exposed moment is the landing, because a package is open to anyone once it lands ([M-0621](../rules/items.md#m-0621)), so the package marks a spot where other people may come.

Strongest as written: the slot count ([M-0603](../rules/sigil.md#m-0603)) and the predictable income ([M-0622](../rules/economy.md#m-0622)). Weakest: the lack of trading and looting ([M-0624](../rules/items.md#m-0624)), and the fact that your package can be claimed by others ([M-0621](../rules/items.md#m-0621)).

What is unknown: when the clock for the 2h 30min starts, and which packages count as yours ([U-0607](../unknowns.md#u-0607)). It is open whether it is a fixed clock or restarts after a claim ([M-0621](../rules/items.md#m-0621), [U-0607](../unknowns.md#u-0607)). It is open when the extra token for item uses is paid ([U-0608](../unknowns.md#u-0608)) and what counts as an item use ([U-0609](../unknowns.md#u-0609)). It is open whether the trade ban also stops you receiving offers or gifts ([U-0610](../unknowns.md#u-0610)). The slot ladder prices and counters are open too ([U-0329](../unknowns.md#u-0329)).

This page gathers 7 rules (2 `DOCUMENTED`, 5 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

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

<a id="m-0603"></a>

### M-0603: Endurance base stats: 100 max HP, 10 inventory slots

Label: `DOCUMENTED`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- [M-0603](../rules/sigil.md#m-0603) `wiki-sigils-endurance-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance))
- [M-0603](../rules/sigil.md#m-0603) `wiki-sigils-endurance-003`: "100 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance))
- [M-0603](../rules/sigil.md#m-0603) `wiki-sigils-endurance-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance))
- [M-0603](../rules/sigil.md#m-0603) `wiki-sigils-endurance-005`: "10" ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance))

**Formal model:**

- [M-0603](../rules/sigil.md#m-0603) reading A: `maxHP = 100; inventory_slots = 10`
- [M-0603](../rules/sigil.md#m-0603) domain: start of event
- [M-0603](../rules/sigil.md#m-0603) parameter `max_hp`: 100
- [M-0603](../rules/sigil.md#m-0603) parameter `inventory_slots`: 10

Notes ([M-0603](../rules/sigil.md#m-0603)): Merchant upgrades (+10 max HP, inventory slots) change these during play; this record is the base value only. The merchant page caps slots at 13, or 20 for Endurance.

<a id="m-0620"></a>

### M-0620: Endurance inventory: 10 slots instead of 3

Label: `DOCUMENTED`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- [M-0620](../rules/items.md#m-0620) `wiki-sigils-endurance-008`: "You have 10 inventory slots instead of 3." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- [M-0620](../rules/items.md#m-0620) reading A: `slots = 10`
- [M-0620](../rules/items.md#m-0620) parameter `inventory_slots`: 10

Notes ([M-0620](../rules/items.md#m-0620)): Same value as the Slots label ([M-0603](../rules/sigil.md#m-0603)). Merchant page allows up to 20 for Endurance with purchases.

<a id="m-0621"></a>

### M-0621: Endurance care package schedule

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-009`: "Every 2h 30min, a care package falls within 10m (33ft) of you." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-013`: "Every 2h 30min, a care package falls within 10m (33ft) of each Endurance contestant." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-014`: "It lands after 30s." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-010`: "Anyone can claim it." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-015`: "After it lands it is a normal care package: any contestant can claim it." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))
- [M-0621](../rules/items.md#m-0621) `wiki-sigils-endurance-016`: "It never holds a health potion or drone." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#endurance-drops))

**Formal model:**

- [M-0621](../rules/items.md#m-0621) reading A: `t_k = t0 + k*9000 s fixed clock; landing at t_k + 30 s; position within 10 m of the contestant`
- [M-0621](../rules/items.md#m-0621) reading B: `timer restarts when the previous package is claimed`
- [M-0621](../rules/items.md#m-0621) domain: seconds
- [M-0621](../rules/items.md#m-0621) parameter `period_s`: 9000
- [M-0621](../rules/items.md#m-0621) parameter `landing_delay_s`: 30
- [M-0621](../rules/items.md#m-0621) parameter `t0`: UNKNOWN, see [U-0607](../unknowns.md#u-0607)

**Open questions:**

- [U-0607](../unknowns.md#u-0607) (high): Endurance care packages 'every 2h 30min': first drop 2h30 after the event start, after the sigil pick, or after the previous claim, and which packages are 'your own'?

Notes ([M-0621](../rules/items.md#m-0621)): Position at time of drop vs landing is not specified (the 10m is from the contestant when it falls). Contents are random items except health potion and drone.

<a id="m-0622"></a>

### M-0622: Endurance tokens for claiming own care package

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- [M-0622](../rules/economy.md#m-0622) `wiki-sigils-endurance-006`: "Claiming one of your own care packages, which fall every 2h 30min, earns six blood tokens." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- [M-0622](../rules/economy.md#m-0622) reading A: `tokens += 6 when the claimer is the contestant it fell for`
- [M-0622](../rules/economy.md#m-0622) reading B: `tokens += 6 for any claim of a package the claimer owns, even if first looted by another`
- [M-0622](../rules/economy.md#m-0622) parameter `tokens_per_claim`: 6

**Interactions:** [M-0621](../rules/items.md#m-0621)

**Open questions:**

- [U-0607](../unknowns.md#u-0607) (high): Endurance care packages 'every 2h 30min': first drop 2h30 after the event start, after the sigil pick, or after the previous claim, and which packages are 'your own'?

Notes ([M-0622](../rules/economy.md#m-0622)): Anyone can claim, so a rival can take the package first; whether the owner then earns tokens is not stated.

<a id="m-0623"></a>

### M-0623: Endurance bonus token per five item uses

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- [M-0623](../rules/economy.md#m-0623) `wiki-sigils-endurance-007`: "Earn one more for every five item uses." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- [M-0623](../rules/economy.md#m-0623) reading A: `tokens += 1 each time the cumulative item-use counter reaches a multiple of 5`
- [M-0623](../rules/economy.md#m-0623) reading B: `claim payout = 6 + floor(uses since last claim / 5)`
- [M-0623](../rules/economy.md#m-0623) reading C: `claim payout = 6 + 1 once five uses happened`
- [M-0623](../rules/economy.md#m-0623) domain: integer counters

**Open questions:**

- [U-0608](../unknowns.md#u-0608) (medium): Endurance 'Earn one more for every five item uses': when is the extra token paid?
- [U-0609](../unknowns.md#u-0609) (medium): Endurance item use bonus: which actions are an 'item use' (weapon shots, bandages, Safety bubbles, crafts, merchant upgrades, effects that stay active)?

Notes ([M-0623](../rules/economy.md#m-0623)): Compare the items page: some effects (Safety Bubbles, smoke bombs, bandages, crafts, merchant upgrades) are excluded from 'active item effects'; it is not stated that this applies here.

<a id="m-0624"></a>

### M-0624: Endurance restrictions: no trade, no gravestone loot, no drop, no pickup

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- [M-0624](../rules/items.md#m-0624) `wiki-sigils-endurance-011`: "You cannot trade, loot gravestones, drop items or pick up dropped items." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))
- [M-0624](../rules/items.md#m-0624) `wiki-sigils-endurance-012`: "You can still destroy items, claim chests and take crates." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- [M-0624](../rules/items.md#m-0624) reading A: `actions {trade, loot_gravestone, drop_item, pickup_dropped_item} disabled; {destroy_item, claim_chest, take_crate, claim_care_package} enabled`
- [M-0624](../rules/items.md#m-0624) reading B: `A, and incoming trade offers from others also refused`

**Open questions:**

- [U-0610](../unknowns.md#u-0610) (medium): Endurance 'cannot trade, loot gravestones, drop items or pick up dropped items': does trade ban cover receiving offers from others, giving gifts, and the items returned by a revive?

Notes ([M-0624](../rules/items.md#m-0624)): Disables looting gravestones: an Endurance contestant cannot rob or collect items from graves. Claiming care packages is allowed by the earn-tokens rule.

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0006](../unknowns.md#u-0006), [U-0322](../unknowns.md#u-0322), [U-0329](../unknowns.md#u-0329), [U-0607](../unknowns.md#u-0607), [U-0608](../unknowns.md#u-0608), [U-0609](../unknowns.md#u-0609), [U-0610](../unknowns.md#u-0610)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
