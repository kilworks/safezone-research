# Rules: viewer

## Summary

Rules of the `viewer` family, as the wiki states them on 2026-11-11.

This page gathers 43 rules (14 `DOCUMENTED`, 29 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0111: Viewer who kills the crown holder gets Cx-Bucks bonus

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0111 `wiki-014`: "A viewer who kills the crown holder receives a Cx-Bucks bonus equal to 20% of the attack's purchase price." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0111 reading A: `bonus = floor(0.2*p)`
- M-0111 reading B: `bonus = ceil(0.2*p)`
- M-0111 reading C: `bonus = 0.2*p`
- M-0111 domain: p = attack price in Cx-Bucks
- M-0111 parameter `attack_price`: UNKNOWN, see U-0014
- M-0111 parameter `bonus_rate`: 0.2

**Open questions:**

- [U-0106](../unknowns.md#u-0106) (medium): Viewer crown-kill bonus 'equal to 20% of the attack's purchase price': rounding rule, whether 'kills' means the final kill, and which attack counts when several viewers hit the holder.
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

### M-0222: EMP blocks viewer sends

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0222 `wiki-items-035`: "Usable" ([source](https://iceposeidon.com/safezone/wiki/items#emp))
- M-0222 `wiki-items-036`: "Stops viewers sending missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes and bounties for 10min." ([source](https://iceposeidon.com/safezone/wiki/items#emp))
- M-0222 `wiki-attacks-001`: "While a contestant's EMP is active, viewers cannot send missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes or bounties." ([source](https://iceposeidon.com/safezone/wiki/attacks#emp))

**Formal model:**

- M-0222 reading A: `for 10min viewers cannot send: missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes, bounties`
- M-0222 domain: t in [0, 600) seconds
- M-0222 parameter `duration`: 10min

Notes (M-0222): Compared with the attacks page: same eight items. Other viewer items are not on the list. Whether the EMP is global or only for the user's own safe-zone targeting is not stated on either page (viewer attacks are aimed at points inside a safe zone).

### M-0223: EMP destroys viewer items in flight

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0223 `wiki-items-037`: "It destroys every viewer missile and nuke already in the air, and every airstrike and gunship already in play, burning fire included." ([source](https://iceposeidon.com/safezone/wiki/items#emp))
- M-0223 `wiki-attacks-002`: "It destroys viewer missiles and nukes in the air, and airstrikes and gunships already in play, fire and falling bombs included." ([source](https://iceposeidon.com/safezone/wiki/attacks#emp))

**Formal model:**

- M-0223 reading A: `at use: every viewer missile and nuke in the air and every airstrike and gunship in play is destroyed, with fire and falling bombs`
- M-0223 domain: instant effect

Notes (M-0223): The attacks page adds that a cyclops, a bounty, tear gas and zombies already on the map are not removed.

### M-0224: EMP refuses viewer items without refund

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0224 `wiki-items-038`: "No refunds: a viewer item refused because of an EMP is lost." ([source](https://iceposeidon.com/safezone/wiki/items#emp))

**Formal model:**

- M-0224 reading A: `a viewer item refused due to EMP is lost; price is not returned`
- M-0224 domain: viewer send event

**Interactions:** M-0222

Notes (M-0224): Prices are U-0014.

### M-0225: EMP does not black out any map

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0225 `wiki-items-039`: "Does not black out any map." ([source](https://iceposeidon.com/safezone/wiki/items#emp))

**Formal model:**

- M-0225 reading A: `EMP does not alter map visibility for anyone`
- M-0225 domain: map state

### M-0230: Smoke bomb and viewer maps

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0230 `wiki-items-047`: "Viewers still see everyone on their map." ([source](https://iceposeidon.com/safezone/wiki/items#smoke_bomb))

**Formal model:**

- M-0230 reading A: `viewers see every contestant on their map regardless of smoke`
- M-0230 domain: viewer view

**Interactions:** M-0226

### M-0400: EMP blocks viewer attack purchases

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0400 `wiki-attacks-001`: "While a contestant's EMP is active, viewers cannot send missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes or bounties." ([source](https://iceposeidon.com/safezone/wiki/attacks#emp))

**Formal model:**

- M-0400 reading A: `EMP active at time t => viewer sends of {missile, nuke, horde, tear_gas, airstrike, gunship, cyclops, bounty} are refused`
- M-0400 domain: t in seconds during an active EMP; set of 8 attack types
- M-0400 parameter `emp_duration`: 10 min (Items page, not this page)

**Open questions:**

- [U-0401](../unknowns.md#u-0401) (medium): Scope of the EMP block: the wiki lists missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes and bounties. Are emergency airdrops, healing circles, illusions and viewer crates blocked? Does the block test the moment of purchase or the moment of landing?

Notes (M-0400): Emergency airdrop, healing circle, illusion and crates are not in the list; whether they are blocked is U-0401. The Items page also gives 10min and 'No refunds'. Cross-family: EMP item (items).

### M-0401: EMP destroys airborne viewer weapons

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0401 `wiki-attacks-002`: "It destroys viewer missiles and nukes in the air, and airstrikes and gunships already in play, fire and falling bombs included." ([source](https://iceposeidon.com/safezone/wiki/attacks#emp))

**Formal model:**

- M-0401 reading A: `at EMP activation: delete all viewer missiles and nukes in the air, and all airstrikes and gunships in play, with fire and falling bombs`
- M-0401 domain: objects in flight at activation time

**Interactions:** M-0400

Notes (M-0401): Admin nukes are not covered by 'viewer nukes' (attacks-018). 'Already in play' for a gunship includes its remaining time.

### M-0402: EMP does not remove standing effects

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0402 `wiki-attacks-003`: "It does not remove a cyclops, a bounty, tear gas or zombies already on the map." ([source](https://iceposeidon.com/safezone/wiki/attacks#emp))

**Formal model:**

- M-0402 reading A: `EMP activation leaves cyclops, bounties, tear gas clouds and zombies unchanged`
- M-0402 domain: objects on the map at activation

**Interactions:** M-0400, M-0401

### M-0403: Viewer missile aim and landing

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0403 `wiki-attacks-004`: "Viewers aim it at a point inside a safe zone." ([source](https://iceposeidon.com/safezone/wiki/attacks#missile))
- M-0403 `wiki-attacks-005`: "It lands 3min later at a random spot near that point." ([source](https://iceposeidon.com/safezone/wiki/attacks#missile))
- M-0403 `wiki-attacks-006`: "The whole blast stays within 100m (328ft) of the aim point." ([source](https://iceposeidon.com/safezone/wiki/attacks#missile))

**Formal model:**

- M-0403 reading A: `aim point p inside a safe zone; landing at t+180s at p+o, |o| <= 75 (blast within 100m)`
- M-0403 reading B: `same with |o| <= 100`
- M-0403 domain: p inside a safe zone; o random offset; t = fire time in seconds
- M-0403 parameter `flight_time`: 180 s
- M-0403 parameter `max_blast_extent`: 100 m
- M-0403 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0400](../unknowns.md#u-0400) (high): Missile landing spread: 'a random spot near that point' with the whole blast within 100m. Is the landing offset at most 75m (blast edge within 100m) or at most 100m, and what is the distribution?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

### M-0404: Viewer missile damage and counters

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0404 `wiki-attacks-007`: "Everyone within 25m (82ft) of where it lands takes 10 HP." ([source](https://iceposeidon.com/safezone/wiki/attacks#missile))
- M-0404 `wiki-attacks-008`: "The Protection sigil is immune." ([source](https://iceposeidon.com/safezone/wiki/attacks#missile))
- M-0404 `wiki-attacks-009`: "A Flak jacket blocks it." ([source](https://iceposeidon.com/safezone/wiki/attacks#missile))
- M-0404 `wiki-attacks-010`: "An EMP destroys it in the air." ([source](https://iceposeidon.com/safezone/wiki/attacks#missile))

**Formal model:**

- M-0404 reading A: `each contestant within 25m of the landing point takes 10 HP unless Protection sigil (immune) or a Flak jacket (blocks) applies; EMP destroys it in flight`
- M-0404 domain: distance d in metres, d <= 25; damage 10 HP
- M-0404 parameter `damage`: 10 HP
- M-0404 parameter `radius`: 25 m
- M-0404 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Interactions:** M-0400, M-0401, M-0403

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

**Contradictions:** [C-0400](../unknowns.md#c-0400)

Notes (M-0404): Damage page lists more blockers (Shield, Safety bubble, Sleeping Bag, Body armor absorbs) than this page; see C-0400. Merchant missile (blood tokens) is a different item, not modeled here.

### M-0405: Viewer nuke

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0405 `wiki-attacks-011`: "Viewers aim it at a point inside a safe zone." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))
- M-0405 `wiki-attacks-012`: "It lands exactly there after 1min." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))
- M-0405 `wiki-attacks-015`: "Everyone within 100m (328ft) takes 20 HP, unless an admin set other numbers." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))
- M-0405 `wiki-attacks-017`: "A Flak jacket, a Shield, a Safety bubble, a Reality Shield or sleeping in your own Sleeping Bag blocks it." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))
- M-0405 `wiki-attacks-018`: "An EMP destroys a viewer nuke in the air." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))

**Formal model:**

- M-0405 reading A: `aim p inside a safe zone; lands exactly at p after 60s; everyone within 100m takes 20 HP; blocked by Flak jacket, Shield, Safety bubble, Reality Shield or own Sleeping Bag; EMP destroys it in the air`
- M-0405 domain: d <= 100 m, damage 20 HP, flight 60 s
- M-0405 parameter `flight_time`: 60 s
- M-0405 parameter `damage`: 20 HP
- M-0405 parameter `radius`: 100 m
- M-0405 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Interactions:** M-0400, M-0401

**Open questions:**

- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

Notes (M-0405): Damage page also lists Body armor (absorbs); the attacks page does not (not a conflict, armor is partial).

### M-0406: Admin nuke

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0406 `wiki-attacks-013`: "Admins can also launch it." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))
- M-0406 `wiki-attacks-014`: "An admin nuke flies for 5min unless the admin sets its flight time, damage and radius." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))
- M-0406 `wiki-attacks-015`: "Everyone within 100m (328ft) takes 20 HP, unless an admin set other numbers." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))

**Formal model:**

- M-0406 reading A: `admin launch: flight 300 s, damage 20 HP, radius 100 m unless the admin sets flight, damage and radius`
- M-0406 domain: admin chosen values positive
- M-0406 parameter `default_flight_time`: 300 s
- M-0406 parameter `default_damage`: 20 HP
- M-0406 parameter `default_radius`: 100 m

Notes (M-0406): EMP wording names viewer nukes only, so admin nukes are not destroyed by EMP by the text.

### M-0407: Nuke damage cut for the Protection sigil

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- M-0407 `wiki-attacks-016`: "The Protection sigil is not immune, but takes 50% less." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))

**Formal model:**

- M-0407 reading A: `d -> floor(d/2)`
- M-0407 reading B: `d -> ceil(d/2)`
- M-0407 reading C: `d -> d/2`
- M-0407 domain: d integer HP of the nuke, default 20 gives 10 under all readings

**Interactions:** M-0405, M-0406

**Open questions:**

- [U-0402](../unknowns.md#u-0402) (low): Nuke damage cut for the Protection sigil: '50% less' of 20 HP is 10 HP, but how are odd admin-set damages rounded, and is the cut applied before or after other reductions?

Notes (M-0407): Protection is not immune to nukes (unlike missiles). Cross-family: Protection sigil page, damage pipeline order.

### M-0408: Horde

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0408 `wiki-attacks-019`: "50 zombies appear in the safe zones for 20min." ([source](https://iceposeidon.com/safezone/wiki/attacks#horde))

**Formal model:**

- M-0408 reading A: `on purchase, 50 zombies appear in the safe zones; each exists for 20 min`
- M-0408 domain: count 50, lifetime 20 min
- M-0408 parameter `zombies`: 50
- M-0408 parameter `duration`: 20 min
- M-0408 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Interactions:** M-0400, M-0445

**Open questions:**

- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?
- [U-0432](../unknowns.md#u-0432) (medium): Viewer attack concurrency: no limit is stated for missiles, nukes, hordes, tear gas, airstrikes, gunships, bounties and healing circles (only cyclops and illusion are limited to one). Are they stackable at will?

Notes (M-0408): Placement is 'in the safe zones' here and 'at random points in the safe zones' on the Zombies page. Bonus zombies for Necromancy are in the zombie family.

### M-0409: Tear gas placement

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0409 `wiki-attacks-020`: "The buyer picks where a 25m (82ft) cloud appears in a safe zone." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))
- M-0409 `wiki-attacks-022`: "The edge of the cloud must be at least 20m (66ft) from every contestant." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))

**Formal model:**

- M-0409 reading A: `centre c in a safe zone; for every contestant q, |c-q| - 25 >= 20 (radius reading)`
- M-0409 reading B: `|c-q| - 12.5 >= 20 (diameter reading)`
- M-0409 domain: c inside a safe zone, metres
- M-0409 parameter `cloud_size`: 25 m
- M-0409 parameter `min_edge_gap`: 20 m
- M-0409 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0404](../unknowns.md#u-0404) (high): Tear gas geometry: '25m cloud' is a radius or a diameter, and the cloud edge must be at least 20m from every contestant: at purchase time only, or also at placement? Must the whole cloud be inside the safe zone?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

### M-0410: Tear gas drain and zombie kill

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0410 `wiki-attacks-021`: "It stays for 10min." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))
- M-0410 `wiki-attacks-023`: "Anyone inside loses 2 HP every 10s." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))
- M-0410 `wiki-attacks-024`: "It kills zombies inside it." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))

**Formal model:**

- M-0410 reading A: `for 600 s, contestants inside lose 2 HP every 10s, first tick per entry timer`
- M-0410 reading B: `first tick on entry`
- M-0410 reading C: `cloud-global 10s phase; zombies inside die`
- M-0410 domain: t in [0, 600] s
- M-0410 parameter `duration`: 600 s
- M-0410 parameter `damage`: 2 HP
- M-0410 parameter `period`: 10 s

**Interactions:** M-0409

**Open questions:**

- [U-0405](../unknowns.md#u-0405) (medium): Tear gas and zombie-kill timing: does the 2 HP every 10s tick start 10s after entry, on entry, or on a cloud-global 10s phase, and are zombies killed instantly on entry or on a tick? Is a tick a 'hit' (U-0002)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0410): The zombie page lists tear gas among blasts that kill zombies. Protection sigil is not immune to tear gas (Protection page).

### M-0411: Tear gas counters

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0411 `wiki-attacks-025`: "A Gas mask blocks it." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))
- M-0411 `wiki-attacks-026`: "Viewers cannot send tear gas while an EMP is active." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))

**Formal model:**

- M-0411 reading A: `Gas mask blocks tear gas; no tear gas can be sent while an EMP is active`
- M-0411 domain: boolean per contestant

**Interactions:** M-0400

**Open questions:**

- [U-0401](../unknowns.md#u-0401) (medium): Scope of the EMP block: the wiki lists missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes and bounties. Are emergency airdrops, healing circles, illusions and viewer crates blocked? Does the block test the moment of purchase or the moment of landing?

**Contradictions:** [C-0400](../unknowns.md#c-0400)

Notes (M-0411): Damage page lists Shield, Safety bubble, Sleeping Bag and Body armor as well; see C-0400.

### M-0412: Airstrike strike

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0412 `wiki-attacks-027`: "The viewer picks the centre inside a safe zone and the direction." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
- M-0412 `wiki-attacks-028`: "20s later, everyone in the strip takes 5 HP." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))

**Formal model:**

- M-0412 reading A: `centre p inside a safe zone and a direction; 20s later every contestant in the strip takes 5 HP`
- M-0412 domain: strip is a rectangle around the centre along the direction; dimensions unknown
- M-0412 parameter `width`: UNKNOWN, see U-0406
- M-0412 parameter `length`: UNKNOWN, see U-0407
- M-0412 parameter `damage`: 5 HP
- M-0412 parameter `delay`: 20 s
- M-0412 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0406](../unknowns.md#u-0406) (high): Airstrike strip width (the wiki gives centre and direction only).
- [U-0407](../unknowns.md#u-0407) (high): Airstrike strip length and whether the strip is centred on the chosen point and may leave the safe zone.
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

### M-0413: Airstrike fire

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0413 `wiki-attacks-029`: "The strip then burns for 5min." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
- M-0413 `wiki-attacks-030`: "Anyone inside loses 1 HP every 2s." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))

**Formal model:**

- M-0413 reading A: `from impact for 300 s, a contestant inside the strip loses 1 HP every 2s, first tick at +2s`
- M-0413 reading B: `first tick at impact`
- M-0413 reading C: `fire from purchase, ends at 300 s`
- M-0413 domain: t in seconds from purchase; impact at t=20
- M-0413 parameter `duration`: 300 s
- M-0413 parameter `damage`: 1 HP
- M-0413 parameter `period`: 2 s

**Interactions:** M-0412

**Open questions:**

- [U-0408](../unknowns.md#u-0408) (medium): Airstrike timeline: impact at 20s, then 'the strip then burns for 5min'. Does the fire last 5min from impact, is the first 1 HP tick at impact or 2s later, and does stepping into the strip during the fire cost HP? Is a fire tick a hit (U-0002)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

### M-0414: Airstrike counters

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0414 `wiki-attacks-031`: "A Shield blocks the fire." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
- M-0414 `wiki-attacks-032`: "A Guardian angel and a Hazmat suit do not help." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
- M-0414 `wiki-attacks-033`: "The Protection sigil is immune to the strike and its fire." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
- M-0414 `wiki-attacks-034`: "A Flak jacket blocks the strike, but not the fire." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))
- M-0414 `wiki-attacks-035`: "An EMP removes the strike and its fire." ([source](https://iceposeidon.com/safezone/wiki/attacks#airstrike))

**Formal model:**

- M-0414 reading A: `fire: blocked by Shield; Guardian angel and Hazmat suit do not help; Protection immune to strike and fire; Flak jacket blocks the strike but not the fire; EMP removes strike and fire`
- M-0414 domain: per contestant, per phase (strike, fire)

**Interactions:** M-0401, M-0412, M-0413

Notes (M-0414): Damage page: airstrike fire blocked by Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs): consistent with the attacks page, which names fewer.

### M-0415: Gunship duration and bomb cadence

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0415 `wiki-attacks-036`: "The buyer gets a gunship for 5min." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))
- M-0415 `wiki-attacks-037`: "Its target circle sweeps around a random safe zone at 75m/s (167.77mph)." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))
- M-0415 `wiki-attacks-038`: "The buyer drops bombs on the target circle, one every 10s." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))

**Formal model:**

- M-0415 reading A: `gunship exists for 300 s; drops one bomb every 10s (30 bombs)`
- M-0415 reading B: `29 bombs`
- M-0415 reading C: `31 bombs`
- M-0415 reading D: `bomb drop is manual with 10s cooldown`
- M-0415 domain: t in [0, 300] s
- M-0415 parameter `duration`: 300 s
- M-0415 parameter `drop_period`: 10 s
- M-0415 parameter `target_circle_speed`: 75 m/s
- M-0415 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0409](../unknowns.md#u-0409) (high): Gunship bomb count and timing: 'a gunship for 5min', 'one every 10s', 'each bomb lands 5s later'. How many bombs can be dropped, does the first drop come at t=0 or t=10s, and do bombs landing after 5min still land?
- [U-0410](../unknowns.md#u-0410) (medium): Gunship bomb position and target circle: the circle 'sweeps around a random safe zone at 75m/s' (circle radius and path unstated). Does a bomb land where the circle was at the drop or where it is 5s later (75m/s x 5s = 375m away)?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

### M-0416: Gunship bomb effect

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0416 `wiki-attacks-039`: "Each bomb lands 5s later and deals 10 HP to everyone within 25m (82ft)." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))

**Formal model:**

- M-0416 reading A: `a bomb lands 5s after its drop; everyone within 25m takes 10 HP`
- M-0416 domain: d <= 25 m
- M-0416 parameter `delay`: 5 s
- M-0416 parameter `damage`: 10 HP
- M-0416 parameter `radius`: 25 m

**Interactions:** M-0415

**Open questions:**

- [U-0410](../unknowns.md#u-0410) (medium): Gunship bomb position and target circle: the circle 'sweeps around a random safe zone at 75m/s' (circle radius and path unstated). Does a bomb land where the circle was at the drop or where it is 5s later (75m/s x 5s = 375m away)?

### M-0417: Gunship counters

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0417 `wiki-attacks-040`: "The Protection sigil is immune." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))
- M-0417 `wiki-attacks-041`: "A Flak jacket blocks one bomb." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))
- M-0417 `wiki-attacks-042`: "An EMP removes the gunship and its falling bombs." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))

**Formal model:**

- M-0417 reading A: `Protection immune; a Flak jacket blocks one bomb; an EMP removes the gunship and its falling bombs`
- M-0417 domain: per contestant

**Interactions:** M-0401, M-0416

**Contradictions:** [C-0400](../unknowns.md#c-0400)

Notes (M-0417): Damage page lists Shield, Safety bubble, Sleeping Bag, Body armor as further blockers of a gunship bomb; see C-0400.

### M-0418: Emergency airdrop

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0418 `wiki-attacks-043`: "5 care packages fall within 10m (33ft) of a random point in the safe zones." ([source](https://iceposeidon.com/safezone/wiki/attacks#emergency-airdrop))
- M-0418 `wiki-attacks-044`: "They land after 5min." ([source](https://iceposeidon.com/safezone/wiki/attacks#emergency-airdrop))
- M-0418 `wiki-attacks-045`: "Each one holds a random item and is claimed like any other care package." ([source](https://iceposeidon.com/safezone/wiki/attacks#emergency-airdrop))

**Formal model:**

- M-0418 reading A: `5 care packages fall at landing time t+300s within 10m of one random point of the safe zones; each holds a random item; claimed like any care package`
- M-0418 domain: 5 packages, spread 10 m
- M-0418 parameter `packages`: 5
- M-0418 parameter `flight_time`: 300 s
- M-0418 parameter `spread`: 10 m
- M-0418 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0412](../unknowns.md#u-0412) (low): Random items: what is the distribution of 'a random item' in care packages and airdrops, and what is the distribution of 'within 10m of a random point' for the airdrop?
- [U-0411](../unknowns.md#u-0411) (medium): Care package Trolling rule: does the 3% roll apply to each package separately (including the 5 of an emergency airdrop, Endurance packages and merchant packages), is 'within 5m' the same as 'next to', and which Trolling contestant is chosen when several exist?
- [U-0401](../unknowns.md#u-0401) (medium): Scope of the EMP block: the wiki lists missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes and bounties. Are emergency airdrops, healing circles, illusions and viewer crates blocked? Does the block test the moment of purchase or the moment of landing?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

### M-0419: Healing circle

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0419 `wiki-attacks-046`: "A 50m (164ft) circle appears at a random point in the safe zones." ([source](https://iceposeidon.com/safezone/wiki/attacks#healing-circle))
- M-0419 `wiki-attacks-047`: "1min later, every living contestant inside heals 25 HP." ([source](https://iceposeidon.com/safezone/wiki/attacks#healing-circle))

**Formal model:**

- M-0419 reading A: `circle radius 50m at a random point; at +60s each living contestant inside gains min(25, maxhp - hp)`
- M-0419 reading B: `diameter 50m`
- M-0419 domain: t=60 s
- M-0419 parameter `delay`: 60 s
- M-0419 parameter `heal`: 25 HP
- M-0419 parameter `size`: 50 m
- M-0419 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0413](../unknowns.md#u-0413) (medium): Healing circle: is the 50m circle a radius or a diameter, is membership tested at +60s only or continuously, and does 25 HP heal above max HP? Does the heal count for Healing and Piety tokens?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

Notes (M-0419): Piety tokens count healing circles (Piety page).

### M-0420: Illusion copies

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0420 `wiki-attacks-048`: "For 10min, a copy of every living contestant walks around the safe zones at 1.4m/s (3.13mph)." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))
- M-0420 `wiki-attacks-049`: "With fewer than 10 contestants alive, each one gets several copies, up to 30 in total." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))
- M-0420 `wiki-attacks-051`: "You never see copies of yourself." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))

**Formal model:**

- M-0420 reading A: `for 600 s each living contestant has a copy; if n < 10, floor(30/n) copies each`
- M-0420 reading B: `ceil(30/n), capped at 30`
- M-0420 reading C: `n >= 10 uncapped`
- M-0420 domain: n living contestants, copies walk at 1.4 m/s; viewers never see their own copies
- M-0420 parameter `duration`: 600 s
- M-0420 parameter `speed`: 1.4 m/s
- M-0420 parameter `max_total`: 30
- M-0420 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0414](../unknowns.md#u-0414) (medium): Illusion copies count: 'a copy of every living contestant' and, under 10 alive, 'several copies, up to 30 in total'. How many copies each, how are 30 shared, and at 10 or more is the total capped at 30?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

Notes (M-0420): 'Copies look like real contestants' is cosmetic but links to Thermal goggles.

### M-0421: Illusion copy interactions

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0421 `wiki-attacks-052`: "Thermal goggles show them as copies." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))
- M-0421 `wiki-attacks-053`: "Attacking a copy uses up your attack and pops the copy." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))
- M-0421 `wiki-attacks-054`: "Nobody is hurt." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))
- M-0421 `wiki-attacks-055`: "Any blast or staff area pops every copy inside it." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))

**Formal model:**

- M-0421 reading A: `Thermal goggles distinguish copies; attacking a copy consumes the attack and removes the copy; no HP is lost; any blast or staff area removes every copy inside`
- M-0421 domain: per attack, per area

**Interactions:** M-0420

**Open questions:**

- [U-0415](../unknowns.md#u-0415) (low): What does 'attacking a copy uses up your attack' consume: the weapon durability, the attack slot, the item, a cooldown? Does it apply to staffs, drones, C4 and landmines and to Thermal goggle holders who identify copies?

Notes (M-0421): Thermal goggles are on the Items page.

### M-0422: Illusion exclusivity and cooldown

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0422 `wiki-attacks-056`: "Only one illusion can run at a time." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))
- M-0422 `wiki-attacks-057`: "The next one can start 30min after it ends." ([source](https://iceposeidon.com/safezone/wiki/attacks#illusion))

**Formal model:**

- M-0422 reading A: `one illusion at a time; a new one may start 30 min after the previous ends`
- M-0422 reading B: `30 min after its start`
- M-0422 domain: t in seconds
- M-0422 parameter `cooldown`: 1800 s
- M-0422 parameter `duration`: 600 s

**Interactions:** M-0420

**Open questions:**

- [U-0416](../unknowns.md#u-0416) (low): Illusion cooldown: 'The next one can start 30min after it ends'. Does 'it ends' mean the 10min expiry or a destroyed illusion, and what happens to a purchase made while the illusion is running (queued, refused, refunded)?

### M-0423: Bounty marking

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0423 `wiki-attacks-058`: "A random living contestant who has no bounty is marked." ([source](https://iceposeidon.com/safezone/wiki/attacks#bounty))
- M-0423 `wiki-attacks-059`: "The marker follows them on the map." ([source](https://iceposeidon.com/safezone/wiki/attacks#bounty))

**Formal model:**

- M-0423 reading A: `a uniformly random living contestant without a bounty is marked; the marker follows them`
- M-0423 domain: set of living contestants without a bounty
- M-0423 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0418](../unknowns.md#u-0418) (high): Bounty consequences: does the bounty end when claimed (the wiki ends it at 1h or on death) so that repeated claims are possible, and is the marked contestant's 10 HP taken once at claim? Who counts as eligible when no living contestant lacks a bounty?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

Notes (M-0423): Eligibility when everybody already has a bounty is undefined.

### M-0424: Bounty claim

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0424 `wiki-attacks-060`: "The first other contestant to stay within 5m (16ft) of them for 1min claims it." ([source](https://iceposeidon.com/safezone/wiki/attacks#bounty))
- M-0424 `wiki-attacks-061`: "The hunter heals 10 HP and gets a random health potion." ([source](https://iceposeidon.com/safezone/wiki/attacks#bounty))
- M-0424 `wiki-attacks-062`: "If their inventory is full, the potion drops at their feet." ([source](https://iceposeidon.com/safezone/wiki/attacks#bounty))

**Formal model:**

- M-0424 reading A: `continuous: 60s consecutively within 5m of the marked contestant by one hunter`
- M-0424 reading B: `cumulative 60s`
- M-0424 reading C: `shared counter`
- M-0424 domain: d <= 5 m, 60 s; hunter != marked
- M-0424 parameter `range`: 5 m
- M-0424 parameter `hold`: 60 s
- M-0424 parameter `heal`: 10 HP
- M-0424 parameter `reward`: one random health potion

**Interactions:** M-0423

**Open questions:**

- [U-0417](../unknowns.md#u-0417) (critical): Bounty claim: 'The first other contestant to stay within 5m of them for 1min claims it'. Is the 60s continuous (reset when leaving range), cumulative, or does it tolerate short exits? Is the marked contestant's movement relevant, and are multiple hunters tracked separately?
- [U-0418](../unknowns.md#u-0418) (high): Bounty consequences: does the bounty end when claimed (the wiki ends it at 1h or on death) so that repeated claims are possible, and is the marked contestant's 10 HP taken once at claim? Who counts as eligible when no living contestant lacks a bounty?

Notes (M-0424): The potion drops at the hunter's feet if inventory is full.

### M-0425: Bounty damage and expiry

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0425 `wiki-attacks-063`: "The marked contestant takes 10 HP." ([source](https://iceposeidon.com/safezone/wiki/attacks#bounty))
- M-0425 `wiki-attacks-064`: "The bounty ends after 1h, or when the marked contestant dies." ([source](https://iceposeidon.com/safezone/wiki/attacks#bounty))

**Formal model:**

- M-0425 reading A: `marked contestant takes 10 HP; bounty ends after 3600 s or on the marked contestant's death`
- M-0425 domain: t in [0, 3600] s
- M-0425 parameter `damage`: 10 HP
- M-0425 parameter `duration`: 3600 s

**Interactions:** M-0423, M-0424

**Open questions:**

- [U-0418](../unknowns.md#u-0418) (high): Bounty consequences: does the bounty end when claimed (the wiki ends it at 1h or on death) so that repeated claims are possible, and is the marked contestant's 10 HP taken once at claim? Who counts as eligible when no living contestant lacks a bounty?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0425): Damage page lists Shield, Safety bubble, Sleeping Bag, Body armor for the bounty mark. Protection still takes bounty damage (Protection page).

### M-0426: Cyclops stats and attack

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0426 `wiki-attacks-065`: "It has 200 HP and walks at 0.8m/s (1.79mph)." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0426 `wiki-attacks-066`: "Every 5s it hits the nearest contestant within 30m (98ft) for 10 HP." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))

**Formal model:**

- M-0426 reading A: `200 HP, speed 0.8 m/s; every 5s hits the nearest contestant within 30m for 10 HP`
- M-0426 domain: d <= 30 m
- M-0426 parameter `hp`: 200
- M-0426 parameter `speed`: 0.8 m/s
- M-0426 parameter `period`: 5 s
- M-0426 parameter `damage`: 10 HP
- M-0426 parameter `price_cx_bucks`: UNKNOWN, see U-0014

**Open questions:**

- [U-0420](../unknowns.md#u-0420) (medium): Cyclops attack timing and target: 'Every 5s it hits the nearest contestant within 30m for 10 HP'. First hit at spawn+5s or when a target first enters range; tie breaks; does it pass the damage pipeline (U-0002)?
- [U-0014](../unknowns.md#u-0014) (high): What are the viewer attack prices in Cx-Bucks?

### M-0427: Cyclops steering vote

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0427 `wiki-attacks-067`: "Every viewer can vote its direction while it is on the map, not only the buyer." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0427 `wiki-attacks-068`: "The most voted direction wins every 5s." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))

**Formal model:**

- M-0427 reading A: `every viewer votes; every 5s the most voted direction is selected`
- M-0427 domain: t in 5 s windows
- M-0427 parameter `window`: 5 s

**Interactions:** M-0426

**Open questions:**

- [U-0421](../unknowns.md#u-0421) (low): Cyclops steering vote: what is the direction set, does the winner persist when nobody votes, and are votes per viewer per 5s window?

### M-0428: Cyclops damage taken

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0428 `wiki-attacks-069`: "Contestants attack it with a bow, knife, long sword, Zarok's axe or machete within the weapon's range, or with a drone from anywhere." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0428 `wiki-attacks-070`: "All damage hurts it: weapons, drones, C4, landmines, staffs, nukes, missiles, airstrikes, tear gas and gunship bombs." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0428 `wiki-attacks-071`: "Outside the safe zones it takes zone damage." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0428 `wiki-attacks-075`: "It cannot attack into or out of a smoke bomb cloud." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0428 `wiki-attacks-076`: "Weapons and drones cannot hit it inside one unless you hold Thermal goggles, but blasts and damage areas still hurt it." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))

**Formal model:**

- M-0428 reading A: `bow, knife, long sword, Zarok's axe, machete within range, or drone at any range; all damage types hurt it; zone damage outside safe zones; smoke bomb prevents attacks in both directions, weapons and drones hit only with Thermal goggles, blasts and areas still hurt`
- M-0428 domain: cyclops hp 0..200

**Interactions:** M-0426

**Open questions:**

- [U-0422](../unknowns.md#u-0422) (low): Cyclops zone damage: 'Outside the safe zones it takes zone damage'. Same rate as contestants (U-0003), same escalation, or flat?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0428): Compare weapon list with the weapons page: only 5 melee/ranged listed here.

### M-0429: Cyclops blood tokens

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0429 `wiki-attacks-072`: "When it dies, each contestant earns 1 blood token per damage they dealt to it." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0429 `wiki-attacks-073`: "Damage from viewer items earns nothing." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0429 `wiki-attacks-074`: "If the zone kills it, nobody earns anything." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))

**Formal model:**

- M-0429 reading A: `on death by contestants each earns 1 token per HP dealt, viewer-item damage earns nothing, a zone kill pays nobody`
- M-0429 domain: d integer per contestant, sum over contestants
- M-0429 parameter `rate`: 1 token per damage

**Interactions:** M-0428

**Open questions:**

- [U-0419](../unknowns.md#u-0419) (medium): Cyclops blood tokens: '1 blood token per damage dealt' when it dies. Is damage counted with overkill capped at its 200 HP, are merchant missiles 'viewer items', and does a zone kill still pay nothing if contestants dealt damage earlier?

### M-0430: Cyclops concurrency and respawn

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0430 `wiki-attacks-077`: "Only one cyclops can be on the map at a time." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))
- M-0430 `wiki-attacks-078`: "The next one can come 3h after it dies." ([source](https://iceposeidon.com/safezone/wiki/attacks#cyclops))

**Formal model:**

- M-0430 reading A: `at most one on the map; next can come 10800 s after the previous dies`
- M-0430 domain: t seconds
- M-0430 parameter `cooldown`: 10800 s

**Interactions:** M-0426

### M-0431: Care package drop

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0431 `wiki-attacks-079`: "A care package drops a random item at a random point in the safe zones." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))

**Formal model:**

- M-0431 reading A: `one care package with a random item lands at a random point in the safe zones`
- M-0431 domain: uniform point in the safe zones

**Open questions:**

- [U-0412](../unknowns.md#u-0412) (low): Random items: what is the distribution of 'a random item' in care packages and airdrops, and what is the distribution of 'within 10m of a random point' for the airdrop?

### M-0432: Care package Trolling diversion

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- M-0432 `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))

**Formal model:**

- M-0432 reading A: `each care package: with probability 0.03 it lands within 5m of a Trolling contestant instead`
- M-0432 domain: p = 3%, distance <= 5 m
- M-0432 parameter `p`: 0.03
- M-0432 parameter `radius`: 5 m

**Interactions:** M-0431

**Open questions:**

- [U-0411](../unknowns.md#u-0411) (medium): Care package Trolling rule: does the 3% roll apply to each package separately (including the 5 of an emergency airdrop, Endurance packages and merchant packages), is 'within 5m' the same as 'next to', and which Trolling contestant is chosen when several exist?

**Contradictions:** [C-0403](../unknowns.md#c-0403)

Notes (M-0432): Trolling page wording: 'Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead' (C-0403).

### M-0433: Viewer crate

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0433 `wiki-attacks-081`: "A crate holds an item bought by a viewer." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))
- M-0433 `wiki-attacks-082`: "It looks like every other crate until someone opens it." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))

**Formal model:**

- M-0433 reading A: `a crate holds an item bought by a viewer and is visually identical to other crates until opened`
- M-0433 domain: per crate

Notes (M-0433): Fake chests are described on other pages. Visual sameness is the Trolling lure.

### M-0434: God's fruit (admin)

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0434 `wiki-attacks-083`: "Only admins launch it." ([source](https://iceposeidon.com/safezone/wiki/attacks#gods-fruit))
- M-0434 `wiki-attacks-084`: "It lands after 5min, exactly where it is aimed." ([source](https://iceposeidon.com/safezone/wiki/attacks#gods-fruit))
- M-0434 `wiki-attacks-085`: "Everyone within 100m (328ft) heals 20 HP and is cured of poison, even at full HP." ([source](https://iceposeidon.com/safezone/wiki/attacks#gods-fruit))

**Formal model:**

- M-0434 reading A: `admin launch; lands at the aim point after 300 s; everyone within 100m heals 20 HP and is cured of poison even at full HP`
- M-0434 domain: d <= 100 m, hp += 20 (cap at max HP unspecified)
- M-0434 parameter `flight_time`: 300 s
- M-0434 parameter `heal`: 20 HP
- M-0434 parameter `radius`: 100 m

Notes (M-0434): Overheal beyond max HP is unspecified; the effect on revive-state contestants is not stated.

### M-0435: Reality Shield (admin)

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0435 `wiki-attacks-086`: "Placed by admins." ([source](https://iceposeidon.com/safezone/wiki/attacks#reality-shield))
- M-0435 `wiki-attacks-087`: "Everyone within 30m (98ft) is immune to all damage, zombies and new poison." ([source](https://iceposeidon.com/safezone/wiki/attacks#reality-shield))

**Formal model:**

- M-0435 reading A: `placed by admins; everyone within 30m is immune to all damage, zombies and new poison`
- M-0435 domain: d <= 30 m
- M-0435 parameter `radius`: 30 m
- M-0435 parameter `duration`: UNKNOWN, see U-0423

**Open questions:**

- [U-0423](../unknowns.md#u-0423) (low): Reality Shield: duration is not given, 'Everyone within 30m' is radius or diameter, and 'immune to all damage, zombies and new poison' leaves existing poison running?

Notes (M-0435): Items page lists Safety bubble as 'immune to damage and zombies, zone damage included'. Attacks list the Reality Shield among nuke blockers.

### M-0539: Trolling care package diversion

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- M-0539 `wiki-sigils-trolling-020`: "Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- M-0539 `wiki-attacks-079`: "A care package drops a random item at a random point in the safe zones." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))
- M-0539 `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))

**Formal model:**

- M-0539 reading A: `each viewer care package: with probability 0.03 it lands within 5 m of a Trolling contestant instead of a random point in the safe zones`
- M-0539 reading B: `crates also roll`
- M-0539 reading C: `each Trolling contestant rolls separately`
- M-0539 domain: per package; probability 0.03
- M-0539 parameter `p`: 0.03
- M-0539 parameter `landing_radius_m`: 5
- M-0539 parameter `scope`: UNKNOWN, see U-0540

**Open questions:**

- [U-0540](../unknowns.md#u-0540) (medium): Trolling care package diversion '3% chance to land next to a Trolling contestant': which packages roll, how is the contestant chosen with several Trolling contestants, and is the draw once per package?
- [U-0015](../unknowns.md#u-0015) (high): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004).

**Contradictions:** [C-0501](../unknowns.md#c-0501)

Notes (M-0539): The attacks page gives the 5 m distance; the Trolling page does not. Scope mismatch is contradiction C-0501.

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0014](../unknowns.md#u-0014), [U-0015](../unknowns.md#u-0015), [U-0106](../unknowns.md#u-0106), [U-0400](../unknowns.md#u-0400), [U-0401](../unknowns.md#u-0401), [U-0402](../unknowns.md#u-0402), [U-0403](../unknowns.md#u-0403), [U-0404](../unknowns.md#u-0404), [U-0405](../unknowns.md#u-0405), [U-0406](../unknowns.md#u-0406), [U-0407](../unknowns.md#u-0407), [U-0408](../unknowns.md#u-0408), [U-0409](../unknowns.md#u-0409), [U-0410](../unknowns.md#u-0410), [U-0411](../unknowns.md#u-0411), [U-0412](../unknowns.md#u-0412), [U-0413](../unknowns.md#u-0413), [U-0414](../unknowns.md#u-0414), [U-0415](../unknowns.md#u-0415), [U-0416](../unknowns.md#u-0416), [U-0417](../unknowns.md#u-0417), [U-0418](../unknowns.md#u-0418), [U-0419](../unknowns.md#u-0419), [U-0420](../unknowns.md#u-0420), [U-0421](../unknowns.md#u-0421), [U-0422](../unknowns.md#u-0422), [U-0423](../unknowns.md#u-0423), [U-0432](../unknowns.md#u-0432), [U-0540](../unknowns.md#u-0540)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
