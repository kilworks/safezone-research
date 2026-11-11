# Rules: sigil

## Summary

Rules of the `sigil` family, as the wiki states them on 2026-11-11.

This page gathers 24 rules (12 `DOCUMENTED`, 12 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0500"></a>

### M-0500: Piety base max HP and inventory slots

Label: `DOCUMENTED`. Sigils: piety.

**Official text** (snapshot 2026-11-11):

- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-003`: "110 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/piety))
- [M-0500](../rules/sigil.md#m-0500) `wiki-sigils-piety-006`: "Your max HP is 10 HP higher." ([source](https://iceposeidon.com/safezone/wiki/sigils/piety#rules))

**Formal model:**

- [M-0500](../rules/sigil.md#m-0500) reading A: `maxHP_piety = 110; slots_piety = 3; maxHP = base + 10 where base = 100 (the Ingenuity and Trolling labels give 100)`
- [M-0500](../rules/sigil.md#m-0500) domain: integer HP and slot counts at event start
- [M-0500](../rules/sigil.md#m-0500) parameter `max_hp`: 110
- [M-0500](../rules/sigil.md#m-0500) parameter `slots`: 3
- [M-0500](../rules/sigil.md#m-0500) parameter `max_hp_delta_vs_base`: +10

**Interactions:** [M-0506](../rules/items.md#m-0506)

Notes ([M-0500](../rules/sigil.md#m-0500)): Stat labels are read as pairs (label 'Max HP' then '110 HP'; label 'Slots' then '3'). The sentence 'Your max HP is 10 HP higher' agrees with 110 against a base of 100. The merchant page raises the maximum HP cap to 220 for Piety; that is the merchant formalizer's record. Starting HP equal to max HP is not stated on this page.

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

**Interactions:** [M-0520](../rules/items.md#m-0520), [M-0522](../rules/items.md#m-0522)

**Open questions:**

- [U-0517](../unknowns.md#u-0517) (high): Ingenuity crafts: are both named ingredients consumed, does a craft occupy one of the five craft slots, and how do six recipes fit five slots?

Notes ([M-0515](../rules/sigil.md#m-0515)): Six recipes share five craft slots; how crafts occupy them is open. Items page: 'You can carry up to 3 items' is the ordinary default, replaced by the sigil value 2. The merchant page cap of 12 equals 2 + 10 purchases, consistent.

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

<a id="m-0600"></a>

### M-0600: Sigil choice is final

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0600](../rules/sigil.md#m-0600) `wiki-sigils-002`: "The choice is final." ([source](https://iceposeidon.com/safezone/wiki/sigils))

**Formal model:**

- [M-0600](../rules/sigil.md#m-0600) reading A: `sigil(c) is assigned once; sigil(c, t2) = sigil(c, t1) for all t2 >= t1 >= t_pick`
- [M-0600](../rules/sigil.md#m-0600) domain: each contestant c, one of nine sigils

Notes ([M-0600](../rules/sigil.md#m-0600)): No respec. Nothing in the wiki changes a sigil after the pick.

<a id="m-0601"></a>

### M-0601: Sigil pick happens after the event starts

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0601](../rules/sigil.md#m-0601) `wiki-sigils-001`: "Each contestant picks one sigil after the event starts." ([source](https://iceposeidon.com/safezone/wiki/sigils))

**Formal model:**

- [M-0601](../rules/sigil.md#m-0601) reading A: `pick time t_pick(c) > t_start, bounded by an unknown deadline`
- [M-0601](../rules/sigil.md#m-0601) domain: t_pick in seconds from event start
- [M-0601](../rules/sigil.md#m-0601) parameter `sigil_pick_deadline_s`: UNKNOWN, see [U-0627](../unknowns.md#u-0627)

**Open questions:**

- [U-0627](../unknowns.md#u-0627) (medium): Sigil pick: is there a deadline after the event start, and what applies to a contestant who has not picked (base stats, no ability)?

Notes ([M-0601](../rules/sigil.md#m-0601)): Between the event start and the pick the wiki gives no stats or abilities. Passive timers (Healing regeneration, care packages) may start at the pick or at the event start (see [U-0007](../unknowns.md#u-0007), [U-0607](../unknowns.md#u-0607)).

<a id="m-0602"></a>

### M-0602: Death base stats: 100 max HP, 3 inventory slots

Label: `DOCUMENTED`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0602](../rules/sigil.md#m-0602) `wiki-sigils-death-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/death))
- [M-0602](../rules/sigil.md#m-0602) `wiki-sigils-death-003`: "100 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/death))
- [M-0602](../rules/sigil.md#m-0602) `wiki-sigils-death-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/death))
- [M-0602](../rules/sigil.md#m-0602) `wiki-sigils-death-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/death))

**Formal model:**

- [M-0602](../rules/sigil.md#m-0602) reading A: `maxHP = 100; inventory_slots = 3`
- [M-0602](../rules/sigil.md#m-0602) domain: start of event
- [M-0602](../rules/sigil.md#m-0602) parameter `max_hp`: 100
- [M-0602](../rules/sigil.md#m-0602) parameter `inventory_slots`: 3

Notes ([M-0602](../rules/sigil.md#m-0602)): Merchant upgrades (+10 max HP, inventory slots) change these during play; this record is the base value only. The merchant page caps slots at 13, or 20 for Endurance.

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

<a id="m-0604"></a>

### M-0604: Necromancy base stats: 100 max HP, 3 inventory slots

Label: `DOCUMENTED`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0604](../rules/sigil.md#m-0604) `wiki-sigils-necromancy-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))
- [M-0604](../rules/sigil.md#m-0604) `wiki-sigils-necromancy-003`: "100 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))
- [M-0604](../rules/sigil.md#m-0604) `wiki-sigils-necromancy-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))
- [M-0604](../rules/sigil.md#m-0604) `wiki-sigils-necromancy-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))

**Formal model:**

- [M-0604](../rules/sigil.md#m-0604) reading A: `maxHP = 100; inventory_slots = 3`
- [M-0604](../rules/sigil.md#m-0604) domain: start of event
- [M-0604](../rules/sigil.md#m-0604) parameter `max_hp`: 100
- [M-0604](../rules/sigil.md#m-0604) parameter `inventory_slots`: 3

Notes ([M-0604](../rules/sigil.md#m-0604)): Merchant upgrades (+10 max HP, inventory slots) change these during play; this record is the base value only. The merchant page caps slots at 13, or 20 for Endurance.

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

<a id="m-0606"></a>

### M-0606: Healing base stats: 100 max HP, 3 inventory slots

Label: `DOCUMENTED`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-002`: "Max HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/healing))
- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-003`: "100 HP" ([source](https://iceposeidon.com/safezone/wiki/sigils/healing))
- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-004`: "Slots" ([source](https://iceposeidon.com/safezone/wiki/sigils/healing))
- [M-0606](../rules/sigil.md#m-0606) `wiki-sigils-healing-005`: "3" ([source](https://iceposeidon.com/safezone/wiki/sigils/healing))

**Formal model:**

- [M-0606](../rules/sigil.md#m-0606) reading A: `maxHP = 100; inventory_slots = 3`
- [M-0606](../rules/sigil.md#m-0606) domain: start of event
- [M-0606](../rules/sigil.md#m-0606) parameter `max_hp`: 100
- [M-0606](../rules/sigil.md#m-0606) parameter `inventory_slots`: 3

Notes ([M-0606](../rules/sigil.md#m-0606)): Merchant upgrades (+10 max HP, inventory slots) change these during play; this record is the base value only. The merchant page caps slots at 13, or 20 for Endurance.

<a id="m-0611"></a>

### M-0611: Death gravestone rob: heal 5% of max HP

Label: `CONDITIONAL`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0611](../rules/sigil.md#m-0611) `wiki-sigils-death-007`: "Rob a gravestone within 10m (33ft) to heal 5% of your max HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
- [M-0611](../rules/sigil.md#m-0611) `wiki-sigils-death-008`: "Empty gravestones can be robbed too." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
- [M-0611](../rules/sigil.md#m-0611) `wiki-sigils-death-009`: "If you are the first to loot an item or blood tokens from a gravestone, you also rob it." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))

**Formal model:**

- [M-0611](../rules/sigil.md#m-0611) reading A: `heal = floor(M*5/100)`
- [M-0611](../rules/sigil.md#m-0611) reading B: `heal = ceil(M*5/100)`
- [M-0611](../rules/sigil.md#m-0611) reading C: `heal = round half up of M*5/100`
- [M-0611](../rules/sigil.md#m-0611) reading D: `heal = M*5/100 exact fraction`
- [M-0611](../rules/sigil.md#m-0611) domain: M = max HP, integer, 100 at base; distance to the gravestone <= 10 m

**Open questions:**

- [U-0600](../unknowns.md#u-0600) (medium): Death gravestone rob heal: 5% of max HP, how is a fractional result rounded (max HP is 100 at base but the merchant sells +10 max HP steps, so 5% of 110 is 5.5)?
- [U-0606](../unknowns.md#u-0606) (high): Death 'rob': does first-looting an item or blood tokens give the same 5% heal and 10 tokens as the 'rob a gravestone' action, and can blood tokens be looted while locked for revival?

Notes ([M-0611](../rules/sigil.md#m-0611)): At M = 100 all readings give 5 HP. Cap at max HP is not stated. Empty gravestones can be robbed too; whether an empty rob still pays the heal and tokens is not stated.

<a id="m-0613"></a>

### M-0613: Death heal per elimination within 50m

Label: `CONDITIONAL`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0613](../rules/sigil.md#m-0613) `wiki-sigils-death-011`: "When a contestant dies within 50m (164ft) of you, you heal 1 HP for every contestant eliminated so far, them included." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))

**Formal model:**

- [M-0613](../rules/sigil.md#m-0613) reading A: `heal = D_events (death events so far including this one)`
- [M-0613](../rules/sigil.md#m-0613) reading B: `heal = D_dead_now (currently dead, victim included)`
- [M-0613](../rules/sigil.md#m-0613) reading C: `heal = D_distinct (distinct contestants who died at least once)`
- [M-0613](../rules/sigil.md#m-0613) domain: integer 1 <= heal <= N; victim within 50 m

**Open questions:**

- [U-0601](../unknowns.md#u-0601) (high): Death heal 'for every contestant eliminated so far, them included': what is counted, and does a revived contestant still count?
- [U-0009](../unknowns.md#u-0009) (critical): Number of contestants and event duration for Miami.

Notes ([M-0613](../rules/sigil.md#m-0613)): Needs the contestant total ([U-0009](../unknowns.md#u-0009)) for the upper bound. Heal repeated for each death near the Death contestant. Cap at max HP not stated here.

<a id="m-0614"></a>

### M-0614: Death heal cap at 60% max HP when 20% or fewer alive

Label: `CONDITIONAL`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0614](../rules/sigil.md#m-0614) `wiki-sigils-death-012`: "When 20% or fewer of the contestants are alive, that heal cannot take you above 60% of your max HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))

**Formal model:**

- [M-0614](../rules/sigil.md#m-0614) reading A: `if alive*5 <= N: HP' = min(HP + h, 0.6*M) else HP' = min(HP + h, M)`
- [M-0614](../rules/sigil.md#m-0614) reading B: `as A but HP' = max(HP, min(HP + h, 0.6*M)) (never lowers)`
- [M-0614](../rules/sigil.md#m-0614) reading C: `cap rounded: floor(0.6*M) or ceil(0.6*M)`
- [M-0614](../rules/sigil.md#m-0614) domain: alive, N integers; h from the per-elimination heal only; the rob heal is not named by 'that heal'
- [M-0614](../rules/sigil.md#m-0614) parameter `N`: UNKNOWN, see [U-0009](../unknowns.md#u-0009)

**Interactions:** [M-0613](../rules/sigil.md#m-0613)

**Open questions:**

- [U-0602](../unknowns.md#u-0602) (high): Death cap 'When 20% or fewer of the contestants are alive': 20% of which count, with what rounding, and is the alive count taken before or after the death that triggers the heal?
- [U-0603](../unknowns.md#u-0603) (high): Death 60% cap: if HP is already above 60% of max HP, does the heal lower HP to the cap, do nothing, or is the cap rounded?
- [U-0009](../unknowns.md#u-0009) (critical): Number of contestants and event duration for Miami.

Notes ([M-0614](../rules/sigil.md#m-0614)): N is the contestant total, see [U-0009](../unknowns.md#u-0009). Whether the cap applies to the rob heal is not stated: 'that heal' points to the per-elimination heal.

<a id="m-0615"></a>

### M-0615: Death ward: block the first outside-circle hit and 2min of immunity, 2h cooldown

Label: `CONDITIONAL`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0615](../rules/sigil.md#m-0615) `wiki-sigils-death-013`: "Death ward: the first hit from outside the circle or from an unsafe circle is blocked and you are immune to both for 2min." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
- [M-0615](../rules/sigil.md#m-0615) `wiki-sigils-death-014`: "Cooldown 2h." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
- [M-0615](../rules/sigil.md#m-0615) `wiki-damage-073`: "Death Ward: a Death contestant's first hit from outside the circle is blocked, and damage from outside the circle is blocked for 2min." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0615](../rules/sigil.md#m-0615) reading A: `on first hit from outside circle or unsafe circle: block it, then immune to both sources for 120 s; ability then unavailable for 7200 s`
- [M-0615](../rules/sigil.md#m-0615) reading B: `damage-page wording: only 'outside the circle' sources, 120 s window`
- [M-0615](../rules/sigil.md#m-0615) domain: seconds
- [M-0615](../rules/sigil.md#m-0615) parameter `window_s`: 120
- [M-0615](../rules/sigil.md#m-0615) parameter `cooldown_s`: 7200

**Open questions:**

- [U-0604](../unknowns.md#u-0604) (high): Death ward: when does the 2h cooldown start (at the blocked hit, at the end of the 2min immunity, or from the sigil pick), is the ward ready at the pick, and which damage ticks count as 'the first hit'?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

**Contradictions:** [C-0600](../unknowns.md#c-0600)

Notes ([M-0615](../rules/sigil.md#m-0615)): The damage table lists Death Ward as a blocker for both the outside-circle and unsafe-circle rows. See contradiction [C-0600](../unknowns.md#c-0600) about the prose on the damage page.

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

No theorem or simulation covers this page yet.

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0009](../unknowns.md#u-0009), [U-0015](../unknowns.md#u-0015), [U-0509](../unknowns.md#u-0509), [U-0510](../unknowns.md#u-0510), [U-0513](../unknowns.md#u-0513), [U-0514](../unknowns.md#u-0514), [U-0517](../unknowns.md#u-0517), [U-0526](../unknowns.md#u-0526), [U-0600](../unknowns.md#u-0600), [U-0601](../unknowns.md#u-0601), [U-0602](../unknowns.md#u-0602), [U-0603](../unknowns.md#u-0603), [U-0604](../unknowns.md#u-0604), [U-0606](../unknowns.md#u-0606), [U-0621](../unknowns.md#u-0621), [U-0627](../unknowns.md#u-0627)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
