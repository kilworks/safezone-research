# Rules: healing

## Summary

Rules of the `healing` family, as the wiki states them on 2026-11-11.

This page gathers 11 rules (1 `DOCUMENTED`, 10 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0207: Health potion heal by tier

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0207 `wiki-items-008`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#health_potion))
- M-0207 `wiki-items-009`: "Heals by tier: Small 5 HP, Medium 10 HP, Large 20 HP, Gigantic 40 HP." ([source](https://iceposeidon.com/safezone/wiki/items#health_potion))

**Formal model:**

- M-0207 reading A: `hp' = min(maxHP, hp + h)`
- M-0207 reading B: `hp' = hp + h with no cap at max HP (cap enforced elsewhere or not at all)`
- M-0207 domain: tier in {Small, Medium, Large, Gigantic}; 0 < hp <= maxHP
- M-0207 parameter `Small`: 5 HP
- M-0207 parameter `Medium`: 10 HP
- M-0207 parameter `Large`: 20 HP
- M-0207 parameter `Gigantic`: 40 HP

**Interactions:** M-0202, M-0208

**Open questions:**

- [U-0203](../unknowns.md#u-0203) (medium): Do health potions, bandage ticks and Eddie's heal cap at max HP?

Notes (M-0207): Piety adds 15% rounded down on its own page: 5->5, 10->11, 20->23, 40->46 under exact integer arithmetic (U-0006 for binary64). Bounty reward gives a random health potion (attacks page).

### M-0208: Eddie's potion gamble

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0208 `wiki-items-010`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#eddies_potion))
- M-0208 `wiki-items-011`: "A gamble: 10% chance to heal 50% of your max HP." ([source](https://iceposeidon.com/safezone/wiki/items#eddies_potion))
- M-0208 `wiki-items-012`: "Otherwise you lose 30% of your max HP." ([source](https://iceposeidon.com/safezone/wiki/items#eddies_potion))

**Formal model:**

- M-0208 reading A: `p=0.1: hp += floor(M/2); else hp -= floor(3*M/10)`
- M-0208 reading B: `p=0.1: hp += ceil(M/2); else hp -= ceil(3*M/10)`
- M-0208 reading C: `p=0.1: hp += round(M/2); else hp -= round(3*M/10) (round half up)`
- M-0208 reading D: `mixed: heal rounded one way, loss the other way`
- M-0208 domain: M = max HP integer; hp 1..M; outcomes disjoint, P(heal)=1/10, P(loss)=9/10
- M-0208 parameter `heal_chance`: 10%
- M-0208 parameter `heal_fraction`: 50% of max HP
- M-0208 parameter `loss_fraction`: 30% of max HP
- M-0208 parameter `rounding`: UNKNOWN, see U-0204

**Interactions:** M-0207

**Open questions:**

- [U-0004](../unknowns.md#u-0004) (high): Can Eddie's potion 30% loss kill, and do armor, fortress or Kick status apply to it?
- [U-0204](../unknowns.md#u-0204) (low): How are Eddie's potion 50% heal and 30% loss rounded when max HP is not a multiple of 10?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?
- [U-0203](../unknowns.md#u-0203) (medium): Do health potions, bandage ticks and Eddie's heal cap at max HP?

Notes (M-0208): All readings agree when M is a multiple of 10 (heal M/2, loss 3M/10). Sigils shift max HP by 10 (Piety +10, Greed -10), so only a base HP that is not a multiple of 10 makes rounding matter. The damage page lists Eddie's Potion backfire as stopped by Shield, Safety bubble, Sleeping Bag and Body armor (absorbs), see U-0004. The heal amount is 'of your max HP', not of missing HP.

### M-0233: Bandage heal over time

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0233 `wiki-items-048`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#bandage))
- M-0233 `wiki-items-049`: "Heals 10 HP over 2min." ([source](https://iceposeidon.com/safezone/wiki/items#bandage))
- M-0233 `wiki-items-050`: "Taking damage does not stop it." ([source](https://iceposeidon.com/safezone/wiki/items#bandage))

**Formal model:**

- M-0233 reading A: `10 ticks of 1 HP, first at +12 s, last at +120 s`
- M-0233 reading B: `10 ticks of 1 HP, first at +0 s, last at +108 s`
- M-0233 reading C: `5 ticks of 2 HP every 24 s`
- M-0233 reading D: `continuous 1 HP per 12 s accumulated fractionally (120 s total)`
- M-0233 domain: t in [0,120] seconds; total 10 HP; damage does not interrupt
- M-0233 parameter `total`: 10 HP
- M-0233 parameter `duration`: 2min
- M-0233 parameter `tick_schedule`: UNKNOWN, see U-0214

**Interactions:** M-0206, M-0234

**Open questions:**

- [U-0214](../unknowns.md#u-0214) (medium): What is the tick schedule of the Bandage: 10 HP over 2min?
- [U-0203](../unknowns.md#u-0203) (medium): Do health potions, bandage ticks and Eddie's heal cap at max HP?

Notes (M-0233): Protection sigil: bandages last 1.1x as long (132 s), whether total HP also changes is on that page. Each tick may or may not cap at max HP.

### M-0234: Bandage stops Deep Cut bleeding

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0234 `wiki-items-051`: "It also stops Deep Cut bleeding." ([source](https://iceposeidon.com/safezone/wiki/items#bandage))
- M-0234 `wiki-merchant-043`: "Your next bow, knife, long sword, axe, machete or drone hit, or Poison Dart, causes bleeding: 1 HP every five minutes until a bandage or a Healing contestant cures it." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0234 reading A: `using a bandage ends Deep Cut bleeding`
- M-0234 domain: bleeding boolean

**Interactions:** M-0233

Notes (M-0234): Merchant page: bleeding is 1 HP every five minutes until a bandage or a Healing contestant cures it. Not stated whether at use or at the end of the heal.

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

### M-0525: Campfire craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0525 `wiki-sigils-ingenuity-019`: "Heals everyone within 10m (33ft) 1 HP per second from one shared pool equal to the potion's heal." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
- M-0525 `wiki-sigils-ingenuity-020`: "It burns out when the pool is empty or after 10min." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))
- M-0525 `wiki-sigils-ingenuity-021`: "Piety and Protection potion changes do not apply." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-campfire))

**Formal model:**

- M-0525 reading A: `campfire pool = heal of the potion used (small 5, medium 10, large 20, gigantic 40 HP, base values); each second every contestant within 10 m with missing HP gets +1 HP and the pool -1; it ends at pool 0 or after 600 s`
- M-0525 reading B: `pool pays 1 HP per second in total, shared`
- M-0525 reading C: `every contestant in range drains 1 HP per second from the pool regardless of missing HP`
- M-0525 domain: pool integer 0..40; duration 600 s
- M-0525 parameter `rate_hp_per_s`: 1
- M-0525 parameter `radius_m`: 10
- M-0525 parameter `max_duration_s`: 600
- M-0525 parameter `pool`: tier heal of the potion, no Piety +15%, no Protection -50%
- M-0525 parameter `pool_drain`: UNKNOWN, see U-0520

**Interactions:** M-0501, M-0505, M-0518, M-0521

**Open questions:**

- [U-0520](../unknowns.md#u-0520) (high): Campfire shared pool: how does the pool drain with several people, and are full-HP bystanders healed?
- [U-0502](../unknowns.md#u-0502) (high): Piety 'from any source except revives, Campfires and healing circles included': are Campfires and healing circles counted (only revives excluded) or excluded together with revives?

Notes (M-0525): Piety and Protection potion changes are stated not to apply, so the pool is the raw tier value. A heal from a Campfire counts as HP for the Ingenuity income (1 token per HP) and is in the Piety exclusion/inclusion question U-0502. 'Everyone' includes the owner and other sigils; enemies are not excluded.

### M-0526: Everything potion craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0526 `wiki-sigils-ingenuity-023`: "Cures poison and heals by potion tier." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-everything_potion))

**Formal model:**

- M-0526 reading A: `use -> cure poison; heal tier HP of the Health potion ingredient`
- M-0526 reading B: `as A and also grant 600 s of poison immunity as the Anti poison item does`
- M-0526 domain: tier in 5, 10, 20, 40 HP
- M-0526 parameter `heal`: tier of the ingredient potion
- M-0526 parameter `immunity`: UNKNOWN, see U-0521

**Interactions:** M-0518, M-0522

**Open questions:**

- [U-0521](../unknowns.md#u-0521) (low): Everything potion 'Cures poison and heals by potion tier': does it also grant the 10 min poison immunity of an Anti poison?

Notes (M-0526): The poison page lists Anti poison, Healing healing and God's Fruit as cures; the Everything potion cure is stated here only. Poison immunity from Anti poison lasts 10 min (items page).

### M-0645: Protection potions heal 50% less

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- M-0645 `wiki-sigils-protection-016`: "Potions heal you 50% less." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))

**Formal model:**

- M-0645 reading A: `heal -> floor(h/2)`
- M-0645 reading B: `heal -> ceil(h/2)`
- M-0645 reading C: `heal -> h/2 exact`
- M-0645 domain: h integer: health potion tiers 5, 10, 20, 40; Eddie's potion 50% of max HP

**Open questions:**

- [U-0617](../unknowns.md#u-0617) (high): Protection 'Potions heal you 50% less': which heals are 'potions' (health potions, Eddie's potion, God's Fruit, bandages, healing circle)?
- [U-0618](../unknowns.md#u-0618) (low): Protection potion heal 'less 50%': rounding when the tier is odd (Small potion 5 HP)?

Notes (M-0645): Scope (which items count as potions) is U-0617.

### M-0646: Protection bandages last 1.1x as long

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- M-0646 `wiki-sigils-protection-017`: "Bandages last 1.1x as long." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- M-0646 `wiki-items-049`: "Heals 10 HP over 2min." ([source](https://iceposeidon.com/safezone/wiki/items#bandage))

**Formal model:**

- M-0646 reading A: `bandage: 10 HP total over 132 s`
- M-0646 reading B: `bandage: 11 HP total over 132 s at the old rate`
- M-0646 domain: seconds, HP
- M-0646 parameter `duration_factor`: 1.1
- M-0646 parameter `base_duration_s`: 120

**Open questions:**

- [U-0619](../unknowns.md#u-0619) (medium): Protection 'Bandages last 1.1x as long': same total heal over a longer time, or same rate over a longer time?

Notes (M-0646): Cross reference: the bandage item page (heals 10 HP over 2 min).

### M-0651: Healing ability: heal 1 HP, cure poison, stop bleeding, 10min cooldown

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0651 `wiki-sigils-healing-008`: "Heal a nearby contestant for 1 HP and cure their poison." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- M-0651 `wiki-sigils-healing-007`: "Healing also stops Deep Cut bleeding." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- M-0651 `wiki-sigils-healing-009`: "Cooldown 10min." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- M-0651 reading A: `target within range r: HP += 1 (capped at max HP), poison cured, Deep Cut bleeding stopped; next use after 600 s`
- M-0651 domain: seconds, HP
- M-0651 parameter `heal_hp`: 1
- M-0651 parameter `cooldown_s`: 600
- M-0651 parameter `range_m`: UNKNOWN, see U-0622

**Open questions:**

- [U-0622](../unknowns.md#u-0622) (medium): Healing ability 'Heal a nearby contestant': what is the range?
- [U-0623](../unknowns.md#u-0623) (medium): Healing ability: can it target the healer, an already full HP target, a non-poisoned target? Is the cooldown and token spent anyway?

Notes (M-0651): Matches the poison page ('Healing healing' cures poison) and the merchant Deep Cut text (cured by a bandage or a Healing contestant).

### M-0652: Healing passive regeneration: 1 HP every 30min

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0652 `wiki-sigils-healing-010`: "You regenerate 1 HP every 30min, up to your max HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- M-0652 reading A: `every 1800 s on a fixed clock, damage does not reset it`
- M-0652 reading B: `damage resets the 1800 s timer`
- M-0652 domain: seconds
- M-0652 parameter `regen_hp`: 1
- M-0652 parameter `period_s`: 1800

**Consequences:** [T-0011](../theorems/T-0011.md)

**Open questions:**

- [U-0007](../unknowns.md#u-0007) (medium): Healing regeneration: does damage reset the 30 min timer?

Notes (M-0652): Belongs to Healing, not Necromancy. Start of the clock: event start or sigil pick is also open.

## Simulation check

Theorems with tests in `sim/tests/`: [T-0011](../theorems/T-0011.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0004](../unknowns.md#u-0004), [U-0006](../unknowns.md#u-0006), [U-0007](../unknowns.md#u-0007), [U-0203](../unknowns.md#u-0203), [U-0204](../unknowns.md#u-0204), [U-0214](../unknowns.md#u-0214), [U-0502](../unknowns.md#u-0502), [U-0503](../unknowns.md#u-0503), [U-0520](../unknowns.md#u-0520), [U-0521](../unknowns.md#u-0521), [U-0617](../unknowns.md#u-0617), [U-0618](../unknowns.md#u-0618), [U-0619](../unknowns.md#u-0619), [U-0622](../unknowns.md#u-0622), [U-0623](../unknowns.md#u-0623)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
