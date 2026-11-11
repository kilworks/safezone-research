# Rules: economy

## Summary

Rules of the `economy` family, as the wiki states them on 2026-11-11.

This page gathers 23 rules (4 `DOCUMENTED`, 19 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0110: Final kill pays 25 blood tokens, 50 with the blood crown involved

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0110 `wiki-013`: "A final kill pays 25 blood tokens, or 50 if the killer or victim held the blood crown." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0110 reading A: `pay(kill) = 50 if crown(killer) or crown(victim) else 25, to the killer at the killing blow`
- M-0110 reading B: `same amount paid when the revival window ends`
- M-0110 reading C: `50 = 25 base + 25 crown bonus split between parties`
- M-0110 domain: pay in blood tokens
- M-0110 parameter `base_tokens`: 25
- M-0110 parameter `crown_tokens`: 50

**Open questions:**

- [U-0104](../unknowns.md#u-0104) (high): 'A final kill pays 25 blood tokens, or 50 if the killer or victim held the blood crown': who is paid, what makes a kill 'final', and when is the payment made?
- [U-0125](../unknowns.md#u-0125) (high): Blood crown: who 'held' it at the time of a kill (before the kill, or after transfer by that same kill), and how is it obtained/lost?

Notes (M-0110): The Death sigil page also earns one token whenever another contestant dies: different mechanic, not merged.

### M-0320: Merchant overview and currency

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0320 `wiki-merchant-001`: "The merchant sells items, upgrades and enchantments for blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant))
- M-0320 `wiki-merchant-002`: "Every sigil can buy from it." ([source](https://iceposeidon.com/safezone/wiki/merchant))
- M-0320 `wiki-merchant-009`: "You pay with blood tokens only." ([source](https://iceposeidon.com/safezone/wiki/merchant#paying))
- M-0320 `wiki-merchant-010`: "Each sigil earns them in its own way." ([source](https://iceposeidon.com/safezone/wiki/merchant#paying))

**Formal model:**

- M-0320 reading A: `the merchant sells items, upgrades and enchantments; every sigil can buy; payment is in blood tokens only; each sigil earns tokens in its own way`
- M-0320 domain: blood tokens (integers)

Notes (M-0320): Earning rules are on the sigil pages.

### M-0321: Merchant spawning and presence cycle

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0321 `wiki-merchant-003`: "There is at most one merchant on the map." ([source](https://iceposeidon.com/safezone/wiki/merchant#spawning))
- M-0321 `wiki-merchant-004`: "Admins place it, or let it appear at random inside the safe zones or inside an area they pick." ([source](https://iceposeidon.com/safezone/wiki/merchant#spawning))
- M-0321 `wiki-merchant-005`: "A random merchant stays for 15min." ([source](https://iceposeidon.com/safezone/wiki/merchant#spawning))
- M-0321 `wiki-merchant-006`: "Then it leaves and comes back at a new random spot after 30min to 1h." ([source](https://iceposeidon.com/safezone/wiki/merchant#spawning))

**Formal model:**

- M-0321 reading A: `at most one merchant on the map; admins place it, or let it appear at random in the safe zones or in an area they pick; a random merchant stays 15 min, then leaves and returns at a new random spot after a delay in [30, 60] min measured from its departure`
- M-0321 reading B: `the delay is measured from its arrival`
- M-0321 domain: minutes
- M-0321 parameter `merchant_stay_min`: 15
- M-0321 parameter `merchant_return_delay_min`: 30 to 60
- M-0321 parameter `merchant_first_spawn_min`: UNKNOWN, see U-0319

**Open questions:**

- [U-0319](../unknowns.md#u-0319) (medium): When does the first random merchant appear after the event starts?
- [U-0320](../unknowns.md#u-0320) (high): Merchant return delay: is 'after 30min to 1h' measured from the departure or from the arrival, and what is its distribution within the range?

Notes (M-0321): An admin-placed merchant has no stated stay time; only 'a random merchant' stays 15 min.

### M-0322: Merchant purchase range and slot requirement

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0322 `wiki-merchant-007`: "Buy from within 10m (33ft) of it." ([source](https://iceposeidon.com/safezone/wiki/merchant#spawning))
- M-0322 `wiki-merchant-008`: "Items need a free inventory slot." ([source](https://iceposeidon.com/safezone/wiki/merchant#spawning))

**Formal model:**

- M-0322 reading A: `buy only at distance <= 10 m from the merchant; an item purchase needs a free inventory slot`
- M-0322 domain: metres
- M-0322 parameter `merchant_range_m`: 10

**Open questions:**

- [U-0300](../unknowns.md#u-0300) (medium): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground?
- [U-0321](../unknowns.md#u-0321) (medium): Which merchant purchases need a free inventory slot ('Items need a free inventory slot')?

### M-0323: Ingenuity merchant surcharge

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0323 `wiki-merchant-011`: "Ingenuity contestants pay 10% more, rounded up." ([source](https://iceposeidon.com/safezone/wiki/merchant#paying))

**Formal model:**

- M-0323 reading A: `price p becomes ceil(11*p/10) (exact arithmetic)`
- M-0323 reading B: `price p becomes ceil(p*1.1) in binary64`
- M-0323 domain: integer p >= 1

**Open questions:**

- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?
- [U-0322](../unknowns.md#u-0322) (high): How does Ingenuity's 'pay 10% more, rounded up' apply to the 40 + 10k upgrade ladders?

Notes (M-0323): The same sentence is on the Ingenuity page ('Merchant prices are 10% higher, rounded up'), no contradiction. Readings A and B differ by 1 token at base 50, 90, 100, 110 (U-0006). How the surcharge applies to the ladders is U-0322.

### M-0324: Merchant base price list

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0324 `wiki-merchant-012`: "Care package: 10 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0324 `wiki-merchant-014`: "Anti poison: 12 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0324 `wiki-merchant-015`: "Vulnerability Dart: 25 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0324 `wiki-merchant-020`: "Sleeping Bag: 30 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0324 `wiki-merchant-030`: "Missile: 10 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- M-0324 `wiki-merchant-038`: "Dual Wield: 50 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0324 `wiki-merchant-042`: "Deep Cut: 20 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0324 `wiki-merchant-046`: "Weapon enchantment: 15 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))
- M-0324 `wiki-merchant-057`: "Armor enchantment: 30 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#enchantments))

**Formal model:**

- M-0324 reading A: `fixed base prices in blood tokens, before any Ingenuity surcharge`
- M-0324 domain: blood tokens
- M-0324 parameter `care_package`: 10
- M-0324 parameter `anti_poison`: 12
- M-0324 parameter `vulnerability_dart`: 25
- M-0324 parameter `sleeping_bag`: 30
- M-0324 parameter `missile`: 10
- M-0324 parameter `dual_wield`: 50
- M-0324 parameter `deep_cut`: 20
- M-0324 parameter `weapon_enchantment`: 15
- M-0324 parameter `armor_enchantment`: 30

Notes (M-0324): Ladder prices (slots, max HP) are M-0332 and M-0333. Ingenuity contestants pay more, see M-0323.

### M-0325: Merchant care package contents

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0325 `wiki-merchant-013`: "One random item, straight into your inventory." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

**Formal model:**

- M-0325 reading A: `one random item goes straight into the inventory`

**Open questions:**

- [U-0323](../unknowns.md#u-0323) (medium): Which item does a merchant care package give: the distribution of 'One random item'?
- [U-0321](../unknowns.md#u-0321) (medium): Which merchant purchases need a free inventory slot ('Items need a free inventory slot')?

Notes (M-0325): Piety: 'Merchant care packages are not changed' (Piety page). Endurance's own care packages never hold a potion or drone; nothing says that of the merchant's.

### M-0332: Inventory slot upgrade ladder

Label: `CONDITIONAL`. Sigils: all, endurance, ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0332 `wiki-merchant-033`: "Inventory slot: starts at 40 blood tokens and costs 10 more for each one you already bought." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0332 `wiki-merchant-034`: "Buy up to 10 slots, to at most 13 slots, or 20 for Endurance." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0332 `wiki-merchant-035`: "Ingenuity tops out at 12." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0332 reading A: `the k-th purchase (k = 0, 1, ...) costs 40 + 10*k tokens; at most 10 purchases; slots = base + purchases, so at most 13 (base 3), 20 for Endurance (base 10), 12 for Ingenuity (base 2)`
- M-0332 domain: k integer, 0 <= k <= 9
- M-0332 parameter `slot_ladder_start`: 40
- M-0332 parameter `slot_ladder_step`: 10
- M-0332 parameter `slot_purchase_max`: 10
- M-0332 parameter `slot_cap_default`: 13
- M-0332 parameter `slot_cap_endurance`: 20
- M-0332 parameter `slot_cap_ingenuity`: 12

**Open questions:**

- [U-0329](../unknowns.md#u-0329) (high): Are the 'for each one you already bought' counters of Inventory slot and +10 maximum HP separate, or shared?
- [U-0322](../unknowns.md#u-0322) (high): How does Ingenuity's 'pay 10% more, rounded up' apply to the 40 + 10k upgrade ladders?
- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?

Notes (M-0332): Cross-check with sigil pages: Ingenuity starts with 2 slots (2+10=12), Endurance 10 (10+10=20), others 3 (3+10=13): consistent, no contradiction.

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

### M-0334: Dual Wield

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0334 `wiki-merchant-038`: "Dual Wield: 50 blood tokens." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0334 `wiki-merchant-039`: "Unlocks a second weapon slot and a second enchanted weapon." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))
- M-0334 `wiki-merchant-040`: "Weapon and worn equipment slots do not use inventory space." ([source](https://iceposeidon.com/safezone/wiki/merchant#upgrades))

**Formal model:**

- M-0334 reading A: `50 tokens; unlocks a second weapon slot and a second enchanted weapon; weapon and worn equipment slots do not use inventory space`
- M-0334 parameter `dual_wield_cost_tokens`: 50

Notes (M-0334): The first weapon slot is implied by the text 'a second weapon slot'. Base 50 is a price hit by the binary64 question (U-0006, Ingenuity).

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

### M-0510: Greed steal reward and cooldown

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- M-0510 `wiki-sigils-greed-007`: "A successful steal earns five blood tokens, once per victim every 24 hours." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))
- M-0510 `wiki-sigils-greed-014`: "Cooldown 30min." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- M-0510 reading A: `reward 5 blood tokens per successful steal, at most once per victim per rolling 24 h; steals allowed every 30 min`
- M-0510 reading B: `a given victim can be successfully stolen from by the thief at most once per 24 h`
- M-0510 reading C: `cooldown 30 min starts on any use; or only after a success`
- M-0510 domain: time in seconds: cooldown 1800 s, window 86400 s
- M-0510 parameter `reward_tokens`: 5
- M-0510 parameter `per_victim_window_s`: 86400
- M-0510 parameter `cooldown_s`: 1800

**Interactions:** M-0509

**Open questions:**

- [U-0507](../unknowns.md#u-0507) (high): Greed 'A successful steal earns five blood tokens, once per victim every 24 hours': does the 24 h limit cap the token payout only, or the steals themselves?
- [U-0508](../unknowns.md#u-0508) (medium): Greed timers: does the 30 min cooldown start at any steal attempt or only at a successful steal, and is the 24 h per-victim window anchored at the last payout (rolling) or at a daily clock?

Notes (M-0510): 'Cooldown 30min' is cited as the steal cooldown because it sits directly after the Steal sentence in the same list. Different victims can be stolen from every 30 min.

### M-0514: Greed money bag income

Label: `CONDITIONAL`. Sigils: greed.

**Official text** (snapshot 2026-11-11):

- M-0514 `wiki-sigils-greed-012`: "Each real chest you claim and each crate you take adds a blood token to your money bag." ([source](https://iceposeidon.com/safezone/wiki/sigils/greed#rules))

**Formal model:**

- M-0514 reading A: `claim(real chest) or take(crate) -> money_bag += 1 blood token, money bag = ordinary balance`
- M-0514 reading B: `money bag is a separate store paid at an unstated moment`
- M-0514 domain: per claim of a real chest and per crate taken
- M-0514 parameter `tokens_per_claim`: 1
- M-0514 parameter `money_bag_semantics`: UNKNOWN, see U-0512

**Interactions:** M-0510

**Open questions:**

- [U-0512](../unknowns.md#u-0512) (high): Greed 'adds a blood token to your money bag': is the money bag the ordinary blood-token balance, or a separate store that is paid out later?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

Notes (M-0514): Other Greed income is the steal reward (M-0510). Fake chests give nothing.

### M-0516: Ingenuity merchant prices plus 10 percent rounded up

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0516 `wiki-sigils-ingenuity-007`: "Merchant prices are 10% higher, rounded up." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))
- M-0516 `wiki-merchant-011`: "Ingenuity contestants pay 10% more, rounded up." ([source](https://iceposeidon.com/safezone/wiki/merchant#paying))

**Formal model:**

- M-0516 reading A: `price_I(p) = ceil(11 * p / 10), exact integers`
- M-0516 reading B: `price_I(p) = ceil(p * 1.1) in IEEE 754 binary64: gives 56 for p=50, 100 for p=90, 111 for p=100, 122 for p=110 (one token more than A at those bases)`
- M-0516 domain: p positive integer base price in blood tokens, e.g. 10, 12, 15, 20, 25, 30, 40, 50 and escalating 40+10k upgrades
- M-0516 parameter `markup`: 10%
- M-0516 parameter `rounding`: up

**Open questions:**

- [U-0006](../unknowns.md#u-0006) (high): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)?

Notes (M-0516): This record is the Ingenuity-side statement; the merchant page repeats the same sentence (same meaning, no mismatch). Base prices: Care package 10, Anti poison 12, Vulnerability Dart 25, Sleeping Bag 30, Missile 10, Dual Wield 50, Deep Cut 20, weapon enchantment 15, armor enchantment 30, slots and HP upgrades from 40 (merchant page). Whether the markup applies to upgrades is stated by 'Merchant prices'.

### M-0521: Ingenuity blood token income

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0521 `wiki-sigils-ingenuity-013`: "Earn one blood token per craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

**Formal model:**

- M-0521 reading A: `+1 token per craft; +1 per hack; +1 per real item chest destroyed by Black Hole; +1 per HP healed on anyone by the contestant's Campfire; +1 per zombie killed by the Zombie killer`
- M-0521 reading B: `chests destroyed by Black Hole includes crates, care packages, airdrops and fake chests; zombie killed by any means`
- M-0521 domain: events counted per occurrence; no cap stated
- M-0521 parameter `per_craft`: 1
- M-0521 parameter `per_hack`: 1
- M-0521 parameter `per_chest_black_hole`: 1
- M-0521 parameter `per_campfire_hp`: 1
- M-0521 parameter `per_zombie_killed`: 1

**Interactions:** M-0517, M-0522, M-0525, M-0527, M-0528

**Open questions:**

- [U-0519](../unknowns.md#u-0519) (medium): Ingenuity income: what counts as 'craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed'?

Notes (M-0521): The Campfire term pays per HP (not per 5 HP), unlike Piety and Trolling.

### M-0531: Trolling blood token income

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- M-0531 `wiki-sigils-trolling-006`: "Earn one blood token per 5 HP dealt to other players and per crate destroyed, whoever spawned it." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))

**Formal model:**

- M-0531 reading A: `tokens += floor(D_total / 5) over cumulative HP lost by other players because of the contestant, plus 1 per crate destroyed whoever spawned it`
- M-0531 reading B: `tokens += floor(d / 5) per hit, remainder discarded`
- M-0531 reading C: `D counts the nominal hit before armor, fortress and Kick reduction`
- M-0531 reading D: `periodic damage from the contestant's traps counts or not, per U-0529`
- M-0531 domain: d integer HP per hit; crate count integer
- M-0531 parameter `hp_per_token`: 5
- M-0531 parameter `tokens_per_crate`: 1
- M-0531 parameter `hp_basis`: UNKNOWN, see U-0528
- M-0531 parameter `source_scope`: UNKNOWN, see U-0529

**Interactions:** M-0528, M-0533, M-0536

**Open questions:**

- [U-0528](../unknowns.md#u-0528) (high): Trolling 'one blood token per 5 HP dealt to other players': is the remainder carried, and is 'dealt' the nominal hit or the HP that actually got through (after armor, fortress, Kick reduction)?
- [U-0529](../unknowns.md#u-0529) (high): Trolling income scope: which damage counts as 'HP dealt to other players' (weapons, fake chest, unsafe circle ticks, poison from the fake gravestone, reflected hits), and which crates count as 'crate destroyed, whoever spawned it'?
- [U-0001](../unknowns.md#u-0001) (critical): Does the defender's Kick-live 10% reduction floor the result (A) or the removed 10% (B)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0531): 'other players' excludes the Trolling contestant and zombies. A fake chest claim deals 5 HP, a Kick-live defender takes 4 or 5 depending on U-0001, so one claim may pay 0 or 1 token depending on readings.

### M-0610: Death blood token income

Label: `CONDITIONAL`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- M-0610 `wiki-sigils-death-006`: "Earn ten blood tokens per gravestone robbed and one whenever another contestant dies." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))

**Formal model:**

- M-0610 reading A: `tokens += 10 per gravestone robbed; tokens += 1 per death of another contestant, anywhere`
- M-0610 reading B: `same, but the 1 token requires the death within 50m`
- M-0610 domain: integer token counts
- M-0610 parameter `death_token_range_m`: UNKNOWN, see U-0605

**Open questions:**

- [U-0605](../unknowns.md#u-0605) (medium): Death sigil '1 blood token whenever another contestant dies': is there a distance limit (heal uses 50m), and does a revive or second death pay again?
- [U-0606](../unknowns.md#u-0606) (high): Death 'rob': does first-looting an item or blood tokens give the same 5% heal and 10 tokens as the 'rob a gravestone' action, and can blood tokens be looted while locked for revival?

Notes (M-0610): The 10m rob range and the 50m heal range are stated on other lines; the token line gives no range.

### M-0622: Endurance tokens for claiming own care package

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- M-0622 `wiki-sigils-endurance-006`: "Claiming one of your own care packages, which fall every 2h 30min, earns six blood tokens." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- M-0622 reading A: `tokens += 6 when the claimer is the contestant it fell for`
- M-0622 reading B: `tokens += 6 for any claim of a package the claimer owns, even if first looted by another`
- M-0622 parameter `tokens_per_claim`: 6

**Interactions:** M-0621

**Open questions:**

- [U-0607](../unknowns.md#u-0607) (high): Endurance care packages 'every 2h 30min': first drop 2h30 after the event start, after the sigil pick, or after the previous claim, and which packages are 'your own'?

Notes (M-0622): Anyone can claim, so a rival can take the package first; whether the owner then earns tokens is not stated.

### M-0623: Endurance bonus token per five item uses

Label: `CONDITIONAL`. Sigils: endurance.

**Official text** (snapshot 2026-11-11):

- M-0623 `wiki-sigils-endurance-007`: "Earn one more for every five item uses." ([source](https://iceposeidon.com/safezone/wiki/sigils/endurance#rules))

**Formal model:**

- M-0623 reading A: `tokens += 1 each time the cumulative item-use counter reaches a multiple of 5`
- M-0623 reading B: `claim payout = 6 + floor(uses since last claim / 5)`
- M-0623 reading C: `claim payout = 6 + 1 once five uses happened`
- M-0623 domain: integer counters

**Open questions:**

- [U-0608](../unknowns.md#u-0608) (medium): Endurance 'Earn one more for every five item uses': when is the extra token paid?
- [U-0609](../unknowns.md#u-0609) (medium): Endurance item use bonus: which actions are an 'item use' (weapon shots, bandages, Safety bubbles, crafts, merchant upgrades, effects that stay active)?

Notes (M-0623): Compare the items page: some effects (Safety Bubbles, smoke bombs, bandages, crafts, merchant upgrades) are excluded from 'active item effects'; it is not stated that this applies here.

### M-0630: Necromancy blood token income

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0630 `wiki-sigils-necromancy-008`: "Earn one blood token for each zombie of yours that appears, guards and horde bonuses included, and one per HP your zombies drain." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))

**Formal model:**

- M-0630 reading A: `tokens += 1 per owned zombie appearing (summon, death, horde bonus, guard); tokens += 1 per HP drained by owned zombies`
- M-0630 reading B: `A, with HP drained = HP the victim actually lost after armor and caps`

**Open questions:**

- [U-0613](../unknowns.md#u-0613) (high): Necromancy 'The HP goes to you': is the gain the HP the victim actually lost, is it capped at the owner's max HP, and does a blocked or armor-absorbed drain give HP and tokens?
- [U-0614](../unknowns.md#u-0614) (medium): Do guard zombies and horde-bonus zombies drain HP to their Necromancy owner and count in 'one per HP your zombies drain'?

Notes (M-0630): A horde bonus gives 5 zombies and so 5 tokens.

### M-0642: Protection blood tokens from immunity blocks

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- M-0642 `wiki-sigils-protection-010`: "A drone, missile, C4 or landmine hit earns one blood token, and an airstrike or gunship hit earns 1, but only when your own immunity blocks it." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- M-0642 `wiki-sigils-protection-011`: "A nuke hit earns twenty when your damage cut applies." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- M-0642 `wiki-sigils-protection-012`: "A hit already blocked by something else earns nothing." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))

**Formal model:**

- M-0642 reading A: `tokens += 1 per blocked hit of {drone, missile, C4, landmine, airstrike, gunship}; += 20 per nuke hit that reaches the 50% reduction; += 0 if another blocker already stopped the hit`
- M-0642 reading B: `A plus airstrike fire ticks pay`
- M-0642 parameter `tokens_per_block`: 1
- M-0642 parameter `tokens_per_nuke`: 20

**Interactions:** M-0640, M-0643

**Open questions:**

- [U-0620](../unknowns.md#u-0620) (medium): Protection blood tokens from blocked hits: do airstrike fire ticks, a landmine of its own, and the unlisted immunities (trapped gift, poison, retribution) pay tokens?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0642): Poison, trapped gift and Protection retribution are in the immunity list but not in the token list. The nuke bonus is 20 tokens. Whether a sigil landmine of its own pays is not stated.

### M-0650: Healing blood tokens: 1 per heal, 20 per revive

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0650 `wiki-sigils-healing-006`: "Earn one blood token per heal and twenty per revive." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- M-0650 reading A: `tokens += 1 per use of the heal ability; += 20 per completed revive`
- M-0650 parameter `tokens_per_heal`: 1
- M-0650 parameter `tokens_per_revive`: 20

**Open questions:**

- [U-0623](../unknowns.md#u-0623) (medium): Healing ability: can it target the healer, an already full HP target, a non-poisoned target? Is the cooldown and token spent anyway?

Notes (M-0650): Does a heal on a full HP target pay: U-0623.

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0001](../unknowns.md#u-0001), [U-0002](../unknowns.md#u-0002), [U-0006](../unknowns.md#u-0006), [U-0015](../unknowns.md#u-0015), [U-0104](../unknowns.md#u-0104), [U-0125](../unknowns.md#u-0125), [U-0300](../unknowns.md#u-0300), [U-0319](../unknowns.md#u-0319), [U-0320](../unknowns.md#u-0320), [U-0321](../unknowns.md#u-0321), [U-0322](../unknowns.md#u-0322), [U-0323](../unknowns.md#u-0323), [U-0329](../unknowns.md#u-0329), [U-0330](../unknowns.md#u-0330), [U-0331](../unknowns.md#u-0331), [U-0500](../unknowns.md#u-0500), [U-0501](../unknowns.md#u-0501), [U-0502](../unknowns.md#u-0502), [U-0507](../unknowns.md#u-0507), [U-0508](../unknowns.md#u-0508), [U-0512](../unknowns.md#u-0512), [U-0519](../unknowns.md#u-0519), [U-0528](../unknowns.md#u-0528), [U-0529](../unknowns.md#u-0529), [U-0605](../unknowns.md#u-0605), [U-0606](../unknowns.md#u-0606), [U-0607](../unknowns.md#u-0607), [U-0608](../unknowns.md#u-0608), [U-0609](../unknowns.md#u-0609), [U-0613](../unknowns.md#u-0613), [U-0614](../unknowns.md#u-0614), [U-0620](../unknowns.md#u-0620), [U-0623](../unknowns.md#u-0623)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
