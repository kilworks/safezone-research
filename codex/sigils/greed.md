# Sigil of Greed

## Summary

Rules that name the Sigil of Greed, as the wiki states them on 2026-11-11.

### In plain words

Greed is the "thief and collector" class. It trades toughness for income: 90 maximum HP, 10 lower than the base, with 3 inventory slots ([M-0508](../rules/sigil.md#m-0508)). The idea is to be the person who takes what others have and grabs more than the usual share from chests.

The signature move is Steal. You take one item of your choice from a contestant within 10 m (33 ft); equipped weapons and worn Body Armor can be taken, Sleeping Bags cannot, but you can steal from someone who is asleep ([M-0509](../rules/sigil.md#m-0509)). A successful steal earns five blood tokens, once per victim every 24 hours, and the cooldown is 30 minutes ([M-0510](../rules/economy.md#m-0510)). So the play is to move through a crowd, taking from different people.

The second half is chests. You can claim chests and open or take crates from twice as far away ([M-0512](../rules/sigil.md#m-0512)). Each real chest you claim or crate you take adds a blood token to your money bag ([M-0514](../rules/economy.md#m-0514)). Each real chest you claim also has a 25% chance to give you a Shield for 20 minutes, with no roll while you are vulnerable ([M-0513](../rules/items.md#m-0513)).

In practice you would feel like a pickpocket with a small steady paycheck, and a slightly fragile body ([M-0508](../rules/sigil.md#m-0508)).

Limits that the rules state clearly: you cannot steal from Piety players ([M-0507](../rules/sigil.md#m-0507)), and Fortress protection prevents stealing ([M-0511](../rules/sigil.md#m-0511)). Those are the things Greed is weak against, and the 90 HP ([M-0508](../rules/sigil.md#m-0508)) is a plain cost.

Where it is uncertain: all the chest and crate numbers depend on chest rules that the wiki no longer has ([U-0015](../unknowns.md#u-0015)), including the base range that is doubled ([U-0510](../unknowns.md#u-0510)). It is open whether the 24 hour limit caps only the payout or the steals themselves ([U-0507](../unknowns.md#u-0507)). It is open when the 30 minute cooldown starts ([U-0508](../unknowns.md#u-0508)). It is open what happens if you steal with a full inventory or take armor while already wearing some ([U-0509](../unknowns.md#u-0509)). It is open whether the money bag is the ordinary balance or a separate store ([U-0512](../unknowns.md#u-0512)), and what happens if a chest Shield rolls while you already have one ([U-0511](../unknowns.md#u-0511)). For Fortress, how long it lasts and whether it can move is open ([U-0526](../unknowns.md#u-0526)).

This page gathers 8 rules (2 `DOCUMENTED`, 6 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0507"></a>

### M-0507: Piety immunity to theft by Greed

Label: `DOCUMENTED`. Sigils: piety, greed.

**Official text** (snapshot 2026-11-11):

- [M-0507](../rules/sigil.md#m-0507) `wiki-sigils-piety-015`: "You are immune to having your items stolen by Greed players." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))
- [M-0507](../rules/sigil.md#m-0507) `wiki-sigils-greed-017`: "You cannot steal from Piety players." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- [M-0507](../rules/sigil.md#m-0507) reading A: `steal(thief, victim) is refused when victim has sigil Piety`
- [M-0507](../rules/sigil.md#m-0507) domain: any thief with sigil Greed, any victim with sigil Piety

**Interactions:** [M-0509](../rules/sigil.md#m-0509)

Notes ([M-0507](../rules/sigil.md#m-0507)): The two pages say the same thing from each side. Does not protect Piety contestants from other sources of item loss (zombie breakage, unsafe circle loss for defense items).

<a id="m-0508"></a>

### M-0508: Greed base max HP and inventory slots

Label: `DOCUMENTED`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- [M-0508](../rules/sigil.md#m-0508) `wiki-sigils-greed-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/greed))
- [M-0508](../rules/sigil.md#m-0508) `wiki-sigils-greed-003`: "90 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/greed))
- [M-0508](../rules/sigil.md#m-0508) `wiki-sigils-greed-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/greed))
- [M-0508](../rules/sigil.md#m-0508) `wiki-sigils-greed-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/greed))
- [M-0508](../rules/sigil.md#m-0508) `wiki-sigils-greed-006`: "Your max HP is 10 HP lower." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- [M-0508](../rules/sigil.md#m-0508) reading A: `maxHP_greed = 90; slots_greed = 3; maxHP = base - 10 where base = 100`
- [M-0508](../rules/sigil.md#m-0508) domain: integer HP and slot counts at event start
- [M-0508](../rules/sigil.md#m-0508) parameter `max_hp`: 90
- [M-0508](../rules/sigil.md#m-0508) parameter `slots`: 3
- [M-0508](../rules/sigil.md#m-0508) parameter `max_hp_delta_vs_base`: -10

**Consequences:** [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

Notes ([M-0508](../rules/sigil.md#m-0508)): Merchant HP upgrades are +10 each with a cap of 200 (220 for Piety); how many Greed purchases reach the cap is a merchant-page question (90 + 10k = 200 needs k = 11).

<a id="m-0509"></a>

### M-0509: Greed steal action

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- [M-0509](../rules/sigil.md#m-0509) `wiki-sigils-greed-013`: "Steal: take one item of your choice from a contestant within 10m (33ft)." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- [M-0509](../rules/sigil.md#m-0509) `wiki-sigils-greed-015`: "Equipped weapons and worn Body Armor can be stolen." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- [M-0509](../rules/sigil.md#m-0509) `wiki-sigils-greed-016`: "Sleeping Bags cannot be stolen, but you can steal from a sleeping contestant." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- [M-0509](../rules/sigil.md#m-0509) `wiki-sigils-greed-017`: "You cannot steal from Piety players." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- [M-0509](../rules/sigil.md#m-0509) reading A: `steal(thief, victim, item): requires dist <= 10 m, thief has Greed, victim not Piety, victim not fortress-protected, item in victim inventory or equipped weapon or worn Body Armor, item is not a Sleeping Bag; victim may be asleep; moves item to thief`
- [M-0509](../rules/sigil.md#m-0509) domain: dist in metres 0..10 inclusive (the text says 'within 10m')
- [M-0509](../rules/sigil.md#m-0509) parameter `range_m`: 10
- [M-0509](../rules/sigil.md#m-0509) parameter `items_per_use`: 1

**Interactions:** [M-0507](../rules/sigil.md#m-0507), [M-0510](../rules/economy.md#m-0510), [M-0511](../rules/sigil.md#m-0511)

**Open questions:**

- [U-0509](../unknowns.md#u-0509) (low): Greed Steal when the thief has no room: what happens if the inventory is full, or Body Armor is stolen while the thief already carries armor?

Notes ([M-0509](../rules/sigil.md#m-0509)): Cannot be used from inside a smoke bomb and not while blinded (items page, another family); the merchant page confirms Greed can steal other items while the victim sleeps. Inclusive versus exclusive 10 m is not stated; the model uses <=.

<a id="m-0510"></a>

### M-0510: Greed steal reward and cooldown

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- [M-0510](../rules/economy.md#m-0510) `wiki-sigils-greed-007`: "A successful steal earns five blood tokens, once per victim every 24 hours." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- [M-0510](../rules/economy.md#m-0510) `wiki-sigils-greed-014`: "Cooldown 30min." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- [M-0510](../rules/economy.md#m-0510) reading A: `reward 5 blood tokens per successful steal, at most once per victim per rolling 24 h; steals allowed every 30 min`
- [M-0510](../rules/economy.md#m-0510) reading B: `a given victim can be successfully stolen from by the thief at most once per 24 h`
- [M-0510](../rules/economy.md#m-0510) reading C: `cooldown 30 min starts on any use; or only after a success`
- [M-0510](../rules/economy.md#m-0510) domain: time in seconds: cooldown 1800 s, window 86400 s
- [M-0510](../rules/economy.md#m-0510) parameter `reward_tokens`: 5
- [M-0510](../rules/economy.md#m-0510) parameter `per_victim_window_s`: 86400
- [M-0510](../rules/economy.md#m-0510) parameter `cooldown_s`: 1800

**Interactions:** [M-0509](../rules/sigil.md#m-0509)

**Open questions:**

- [U-0507](../unknowns.md#u-0507) (high): Greed 'A successful steal earns five blood tokens, once per victim every 24 hours': does the 24 h limit cap the token payout only, or the steals themselves?
- [U-0508](../unknowns.md#u-0508) (medium): Greed timers: does the 30 min cooldown start at any steal attempt or only at a successful steal, and is the 24 h per-victim window anchored at the last payout (rolling) or at a daily clock?

Notes ([M-0510](../rules/economy.md#m-0510)): 'Cooldown 30min' is cited as the steal cooldown because it sits directly after the Steal sentence in the same list. Different victims can be stolen from every 30 min.

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

<a id="m-0512"></a>

### M-0512: Greed chest and crate reach

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- [M-0512](../rules/sigil.md#m-0512) `wiki-sigils-greed-009`: "You can claim chests and open or take crates from 2x as far away." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- [M-0512](../rules/sigil.md#m-0512) reading A: `claim_range_greed = 2 * claim_range_base for chests, open/take range for crates`
- [M-0512](../rules/sigil.md#m-0512) domain: metres
- [M-0512](../rules/sigil.md#m-0512) parameter `claim_range_base_m`: UNKNOWN, see [U-0510](../unknowns.md#u-0510)
- [M-0512](../rules/sigil.md#m-0512) parameter `multiplier`: 2

**Open questions:**

- [U-0510](../unknowns.md#u-0510) (high): What is the base claim range for chests and crates that Greed doubles ('2x as far away')?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

Notes ([M-0512](../rules/sigil.md#m-0512)): Care packages are not named in this sentence; only chests and crates.

<a id="m-0513"></a>

### M-0513: Greed chest Shield roll

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- [M-0513](../rules/items.md#m-0513) `wiki-sigils-greed-010`: "Each real chest you claim has a 25% chance to give you a Shield for 20min." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- [M-0513](../rules/items.md#m-0513) `wiki-sigils-greed-011`: "No roll while you are vulnerable." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- [M-0513](../rules/items.md#m-0513) `wiki-items-007`: "a Greed chest shield" ([source](https://iceposeidon.com/safezone/wiki/items#effects))

**Formal model:**

- [M-0513](../rules/items.md#m-0513) reading A: `claim(real chest) while not vulnerable -> with probability 0.25 grant Shield for 1200 s; no roll while vulnerable; the Shield does not count toward the 3 active item effects limit`
- [M-0513](../rules/items.md#m-0513) reading B: `overlap rule with an existing Shield undefined`
- [M-0513](../rules/items.md#m-0513) domain: per real chest claim; 20 min = 1200 s
- [M-0513](../rules/items.md#m-0513) parameter `p`: 0.25
- [M-0513](../rules/items.md#m-0513) parameter `duration_s`: 1200
- [M-0513](../rules/items.md#m-0513) parameter `stack_rule`: UNKNOWN, see [U-0511](../unknowns.md#u-0511)

**Interactions:** [M-0512](../rules/sigil.md#m-0512)

**Open questions:**

- [U-0511](../unknowns.md#u-0511) (medium): Greed chest Shield: what happens when the contestant already has an active Shield (item or earlier chest Shield)?

Notes ([M-0513](../rules/items.md#m-0513)): The items page says explicitly that a Greed chest shield is not an active item effect for the limit of 3, so it is not an item use. Fake chests do not roll ('real chest'). Whether the Vulnerability Dart (which removes a Shield) removes this one is not written; the Shield item text says a Vulnerability Dart removes it.

<a id="m-0514"></a>

### M-0514: Greed money bag income

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- [M-0514](../rules/economy.md#m-0514) `wiki-sigils-greed-012`: "Each real chest you claim and each crate you take adds a blood token to your money bag." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- [M-0514](../rules/economy.md#m-0514) reading A: `claim(real chest) or take(crate) -> money_bag += 1 blood token, money bag = ordinary balance`
- [M-0514](../rules/economy.md#m-0514) reading B: `money bag is a separate store paid at an unstated moment`
- [M-0514](../rules/economy.md#m-0514) domain: per claim of a real chest and per crate taken
- [M-0514](../rules/economy.md#m-0514) parameter `tokens_per_claim`: 1
- [M-0514](../rules/economy.md#m-0514) parameter `money_bag_semantics`: UNKNOWN, see [U-0512](../unknowns.md#u-0512)

**Interactions:** [M-0510](../rules/economy.md#m-0510)

**Open questions:**

- [U-0512](../unknowns.md#u-0512) (high): Greed 'adds a blood token to your money bag': is the money bag the ordinary blood-token balance, or a separate store that is paid out later?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

Notes ([M-0514](../rules/economy.md#m-0514)): Other Greed income is the steal reward ([M-0510](../rules/economy.md#m-0510)). Fake chests give nothing.

## Simulation check

Theorems with tests in `sim/tests/`: [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

## Open questions

[U-0015](../unknowns.md#u-0015), [U-0507](../unknowns.md#u-0507), [U-0508](../unknowns.md#u-0508), [U-0509](../unknowns.md#u-0509), [U-0510](../unknowns.md#u-0510), [U-0511](../unknowns.md#u-0511), [U-0512](../unknowns.md#u-0512), [U-0526](../unknowns.md#u-0526)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
