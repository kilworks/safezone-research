# Rules: zombies

## Summary

Rules of the `zombies` family, as the wiki states them on 2026-11-11.

This page gathers 23 rules (2 `DOCUMENTED`, 21 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0440: Zombie pursuit

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0440 `wiki-zombies-001`: "Zombies roam the map, chase contestants and drain their HP." ([source](https://iceposeidon.com/safezone/wiki/zombies))
- M-0440 `wiki-zombies-002`: "They chase the nearest valid contestant, at any distance, at 1.4m/s (3.13mph)" ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- M-0440 reading A: `each zombie moves toward the nearest valid contestant at 1.4 m/s at any distance`
- M-0440 domain: valid set undefined
- M-0440 parameter `speed`: 1.4 m/s
- M-0440 parameter `valid`: UNKNOWN, see U-0424

**Open questions:**

- [U-0424](../unknowns.md#u-0424) (medium): Zombie targeting: 'nearest valid contestant, at any distance'. What makes a contestant valid (alive, not immune, not repellent, not Necromancy), how often is the nearest re-evaluated, and do zombies path through terrain?

### M-0441: Zombie drain

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0441 `wiki-zombies-002`: "drain 1 HP from any contestants within 5m (16ft) every 10s" ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- M-0441 reading A: `per zombie every 10s: each contestant within 5m loses 1 HP`
- M-0441 reading B: `per zombie-contestant timer from entry`
- M-0441 domain: d <= 5 m, period 10 s
- M-0441 parameter `damage`: 1 HP
- M-0441 parameter `period`: 10 s
- M-0441 parameter `range`: 5 m

**Consequences:** [T-0010](../theorems/T-0010.md)

**Interactions:** M-0440

**Open questions:**

- [U-0425](../unknowns.md#u-0425) (high): Zombie drain timing: 'drain 1 HP from any contestants within 5m every 10s'. Is the 10s timer per zombie (global phase) or per contestant from entry, when does the first drain occur, is each drain a 'hit' (U-0002), and does it reach the 1 HP floor/Kick-live reduction?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

### M-0442: Zombie drain cap

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0442 `wiki-zombies-003`: "Each zombie can drain at most 30 HP from each contestant." ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- M-0442 reading A: `total drain per (zombie, contestant) <= 30 HP over the zombie's lifetime`
- M-0442 reading B: `per encounter`
- M-0442 reading C: `per time window`
- M-0442 domain: integer 0..30 per pair
- M-0442 parameter `cap`: 30 HP

**Consequences:** [T-0010](../theorems/T-0010.md)

**Interactions:** M-0441

**Open questions:**

- [U-0008](../unknowns.md#u-0008) (high): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies?

### M-0443: Zombie breaks health potions

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0443 `wiki-zombies-004`: "Zombies have a 10% chance to break one of your health potions" ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- M-0443 reading A: `p = 0.1 per drain tick`
- M-0443 reading B: `p = 0.1 per encounter`
- M-0443 reading C: `p = 0.1 per HP lost`
- M-0443 domain: p in {0.1}
- M-0443 parameter `p`: 0.1

**Interactions:** M-0441

**Open questions:**

- [U-0426](../unknowns.md#u-0426) (medium): Potion break roll: '10% chance to break one of your health potions'. Per drain tick, per encounter or per zombie? Which potion is broken, and is a roll made when no potion is held or when drain is blocked?

### M-0444: Zombies destroy crafted items

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0444 `wiki-zombies-004`: "a 40% chance to destroy crafted items" ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- M-0444 reading A: `p = 0.4 per drain tick, one random craft`
- M-0444 reading B: `per encounter`
- M-0444 reading C: `each craft independently`
- M-0444 domain: p in {0.4}
- M-0444 parameter `p`: 0.4

**Interactions:** M-0441

**Open questions:**

- [U-0427](../unknowns.md#u-0427) (medium): Craft destruction roll: '40% chance to destroy crafted items' (the Ingenuity page says 'unique crafts' and 'Zombie hits'). Per drain tick or encounter, one item or all crafts, and are non-unique crafts included?

**Contradictions:** [C-0404](../unknowns.md#c-0404)

Notes (M-0444): Ingenuity page says 'unique crafts' and 'Zombie hits' (C-0404).

### M-0445: Horde zombies

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0445 `wiki-zombies-005`: "Horde: viewers release 50 zombies at random points in the safe zones." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))
- M-0445 `wiki-zombies-006`: "Horde zombies have no owner." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- M-0445 reading A: `viewers release 50 ownerless zombies at random points in the safe zones`
- M-0445 domain: count 50
- M-0445 parameter `count`: 50
- M-0445 parameter `lifetime`: 20 min (attacks page)

**Interactions:** M-0408

**Open questions:**

- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

Notes (M-0445): Ownerless: no Necromancy owner earns tokens for them.

### M-0446: Zombie Summon

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0446 `wiki-zombies-007`: "Summon: a Necromancy contestant summons a zombie where they stand, up to 3 times every 6h." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- M-0446 reading A: `at most 3 summons in any 6h; a zombie appears where the contestant stands`
- M-0446 reading B: `fixed blocks`
- M-0446 reading C: `6h lockout`
- M-0446 domain: uses <= 3 per 6h
- M-0446 parameter `uses`: 3
- M-0446 parameter `window`: 6 h

**Open questions:**

- [U-0428](../unknowns.md#u-0428) (low): Summon rate: 'up to 3 times every 6h'. Fixed 6h blocks, a rolling 6h window, or a cooldown after the third use?
- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

### M-0447: Zombie on any death

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0447 `wiki-zombies-008`: "Death: when any contestant dies, every living Necromancy contestant gets a zombie within 10m (33ft) of themselves." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- M-0447 reading A: `on any contestant death, each living Necromancy contestant gets a zombie within 10m`
- M-0447 domain: radius 10 m
- M-0447 parameter `radius`: 10 m

**Open questions:**

- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

Notes (M-0447): Necromancy page: same rule, and blood token per zombie appearing.

### M-0448: Horde bonus

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0448 `wiki-zombies-009`: "Horde bonus: when a horde is released, every living Necromancy contestant also gets 5 zombies where they stand." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- M-0448 reading A: `on horde release, each living Necromancy contestant gets 5 zombies where they stand`
- M-0448 domain: count 5
- M-0448 parameter `count`: 5

**Interactions:** M-0445

**Open questions:**

- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

### M-0449: Guard zombies

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0449 `wiki-zombies-010`: "When a contestant dies within 50m (164ft) of a Necromancy contestant, a guard zombie appears 10m (33ft) from the gravestone." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))
- M-0449 `wiki-zombies-011`: "Guard zombies drain 2 HP every 5s from everyone within 10m (33ft), up to 30 HP per contestant." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))

**Formal model:**

- M-0449 reading A: `death within 50m of a Necromancy contestant: a guard zombie 10m from the gravestone drains 2 HP every 5s from contestants within 10m, up to 30 HP per contestant`
- M-0449 domain: d(death, necromancer) <= 50 m; drain range 10 m
- M-0449 parameter `hp`: 2
- M-0449 parameter `period`: 5 s
- M-0449 parameter `range`: 10 m
- M-0449 parameter `cap`: 30 HP
- M-0449 parameter `lifetime`: 1 h (Necromancy page)

**Consequences:** [T-0010](../theorems/T-0010.md)

**Open questions:**

- [U-0429](../unknowns.md#u-0429) (medium): Guard zombie: does a guard zombie stay at its spawn point or chase, is one appearing per Necromancy contestant or per death, does it also drain its owner and the dead, and does it live 1h (Necromancy page) as stated only there?
- [U-0008](../unknowns.md#u-0008) (high): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies?

### M-0450: Zombie expiry

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0450 `wiki-zombies-012`: "A zombie disappears when its time runs out." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))

**Formal model:**

- M-0450 reading A: `a zombie is removed when its lifetime elapses`
- M-0450 domain: per zombie
- M-0450 parameter `lifetime`: UNKNOWN, see U-0403

**Open questions:**

- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

### M-0451: Blasts kill zombies

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0451 `wiki-zombies-013`: "Blasts kill every zombie inside them: C4, landmines, missiles, nukes, airstrikes, gunship bombs and tear gas." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))

**Formal model:**

- M-0451 reading A: `any zombie inside a blast of C4, landmine, missile, nuke, airstrike, gunship bomb or tear gas dies`
- M-0451 domain: zombie position within blast

**Interactions:** M-0404, M-0405, M-0410

Notes (M-0451): Airstrike fire is not listed as a kill source (only airstrike blasts).

### M-0452: Landmine and C4 versus zombies

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0452 `wiki-zombies-014`: "A zombie that walks within range of a Landmine sets it off." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))
- M-0452 `wiki-zombies-015`: "Zombies do not set off C4." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))

**Formal model:**

- M-0452 reading A: `a zombie walking within a landmine's range triggers it; a zombie never triggers C4`
- M-0452 domain: boolean

### M-0453: Ingenuity Zombie Killer

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0453 `wiki-zombies-016`: "An Ingenuity Zombie Killer kills the next ten zombies that come within 10m (33ft) of its owner." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))
- M-0453 `wiki-zombies-017`: "It has no time limit." ([source](https://iceposeidon.com/safezone/wiki/zombies#deaths))
- M-0453 `wiki-zombies-020`: "An Ingenuity Zombie Killer also stops zombies draining you until it has killed ten." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

**Formal model:**

- M-0453 reading A: `kills the next 10 zombies that come within 10m of its owner; no time limit; stops zombie drain until ten are killed`
- M-0453 domain: count 0..10
- M-0453 parameter `kills`: 10
- M-0453 parameter `radius`: 10 m

**Open questions:**

- [U-0430](../unknowns.md#u-0430) (low): Ingenuity Zombie Killer: 'kills the next ten zombies that come within 10m of its owner' and 'stops zombies draining you until it has killed ten'. Do ten zombies arriving together count, is the drain stop limited to the ten, and is the order by approach?

### M-0454: Zombie immunity items

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0454 `wiki-zombies-018`: "A Shield, a Safety bubble, a Reality Shield or sleeping in your own Sleeping Bag makes you immune." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

**Formal model:**

- M-0454 reading A: `Shield, Safety bubble, Reality Shield or sleeping in your own Sleeping Bag => immune to zombies`
- M-0454 domain: boolean per contestant

**Open questions:**

- [U-0424](../unknowns.md#u-0424) (medium): Zombie targeting: 'nearest valid contestant, at any distance'. What makes a contestant valid (alive, not immune, not repellent, not Necromancy), how often is the nearest re-evaluated, and do zombies path through terrain?

**Contradictions:** [C-0401](../unknowns.md#c-0401)

Notes (M-0454): Necromancy is listed as fully immune on the Necromancy page and the Damage page, absent here (C-0401).

### M-0455: Zombie repellent

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0455 `wiki-zombies-019`: "Zombie repellent: use it and zombies ignore you for 20min." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

**Formal model:**

- M-0455 reading A: `for 1200 s zombies ignore the user (drain only)`
- M-0455 reading B: `removed from the target set`
- M-0455 domain: t in [0, 1200] s
- M-0455 parameter `duration`: 1200 s

**Open questions:**

- [U-0431](../unknowns.md#u-0431) (low): Zombie repellent: 'zombies ignore you for 20min' (Zombies page) versus 'stop zombies hurting you' (Items). Does ignoring remove you from targeting (zombies chase other contestants) or only block drain?

**Contradictions:** [C-0402](../unknowns.md#c-0402)

Notes (M-0455): Items page: 'stop zombies hurting you for 20min' (C-0402).

### M-0527: Zombie killer craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- M-0527 `wiki-sigils-ingenuity-025`: "Kills the next ten zombies that come within 10m (33ft) of you." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-zombie_killer))
- M-0527 `wiki-sigils-ingenuity-026`: "No time limit." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-zombie_killer))
- M-0527 `wiki-zombies-020`: "An Ingenuity Zombie Killer also stops zombies draining you until it has killed ten." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

**Formal model:**

- M-0527 reading A: `for the next 10 zombies that come within 10 m of the owner: kill the zombie; zombies do not drain the owner until 10 have been killed; no expiry`
- M-0527 reading B: `zombies already inside 10 m at use are not counted`
- M-0527 reading C: `guard zombies and horde zombies are excluded from the count`
- M-0527 domain: kills counter 0..10; radius 10 m; no time limit
- M-0527 parameter `kills`: 10
- M-0527 parameter `radius_m`: 10
- M-0527 parameter `expiry`: none

**Interactions:** M-0520, M-0521

**Open questions:**

- [U-0522](../unknowns.md#u-0522) (medium): Zombie killer 'Kills the next ten zombies that come within 10m': does it kill zombies already inside 10 m when used, which zombie types count, and are more than ten in range handled?

Notes (M-0527): Zombies page repeats the same ten zombies and the same 10 m. Zombie drain range is 5 m and zombies chase at 1.4 m/s, so a zombie reaches 10 m before it can drain. Pays 1 token per zombie killed for Ingenuity (M-0521).

### M-0631: Necromancy summon: up to 3 times every 6h

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0631 `wiki-sigils-necromancy-009`: "Summon a zombie where you stand, up to 3 times every 6h." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0631 `wiki-zombies-007`: "a Necromancy contestant summons a zombie where they stand, up to 3 times every 6h." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- M-0631 reading A: `at most 3 summons in any rolling 21600 s`
- M-0631 reading B: `counter resets at fixed 21600 s boundaries`
- M-0631 reading C: `3 charges, refill 6 h after the first of the batch`
- M-0631 domain: seconds
- M-0631 parameter `summon_cap`: 3
- M-0631 parameter `window_s`: 21600
- M-0631 parameter `zombie_lifetime_s`: UNKNOWN, see U-0612

**Open questions:**

- [U-0611](../unknowns.md#u-0611) (medium): Necromancy summon 'up to 3 times every 6h': rolling window, fixed 6h blocks, or three charges refilled on a timer?
- [U-0612](../unknowns.md#u-0612) (high): How long do summoned, death and horde-bonus zombies live ('A zombie disappears when its time runs out')?

Notes (M-0631): The two pages agree.

### M-0632: Necromancy death zombie within 10m

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0632 `wiki-sigils-necromancy-010`: "When any contestant dies, a zombie of yours appears within 10m (33ft) of you." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0632 `wiki-zombies-008`: "when any contestant dies, every living Necromancy contestant gets a zombie within 10m (33ft) of themselves." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- M-0632 reading A: `for each death of any contestant, each living Necromancy contestant gets one owned zombie within 10 m`
- M-0632 parameter `zombie_lifetime_s`: UNKNOWN, see U-0612

**Open questions:**

- [U-0612](../unknowns.md#u-0612) (high): How long do summoned, death and horde-bonus zombies live ('A zombie disappears when its time runs out')?

Notes (M-0632): The zombies page adds 'living'. No distance limit on the death. A Necromancy contestant dying themselves is not covered.

### M-0633: Necromancy guard zombie at a gravestone

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0633 `wiki-sigils-necromancy-011`: "When a contestant dies within 50m (164ft) of you, a guard zombie stands 10m (33ft) from their gravestone for 1h." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0633 `wiki-sigils-necromancy-012`: "It drains 2 HP every 5s from anyone within 10m (33ft), up to 30 HP per contestant." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0633 `wiki-zombies-010`: "a guard zombie appears 10m (33ft) from the gravestone." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))
- M-0633 `wiki-zombies-011`: "Guard zombies drain 2 HP every 5s from everyone within 10m (33ft), up to 30 HP per contestant." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))

**Formal model:**

- M-0633 reading A: `per death within 50 m of a Necromancy contestant: guard zombie at 10 m from the grave for 3600 s, drains 2 HP per 5 s within 10 m, at most 30 HP per contestant per guard zombie`
- M-0633 reading B: `A, with the 30 HP cap shared by all guard zombies`
- M-0633 domain: seconds, HP
- M-0633 parameter `duration_s`: 3600
- M-0633 parameter `drain_hp`: 2
- M-0633 parameter `interval_s`: 5
- M-0633 parameter `radius_m`: 10
- M-0633 parameter `cap_hp`: 30

**Open questions:**

- [U-0615](../unknowns.md#u-0615) (medium): Guard zombie 'up to 30 HP per contestant': per guard zombie, or shared across all guard zombies on the same contestant? Does it stand still all hour?
- [U-0008](../unknowns.md#u-0008) (high): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0633): The zombies page gives no duration for the guard zombie; the sigil page gives 1h. First drain tick timing is not stated. Owner immunity: see M-0636.

### M-0634: Necromancy horde bonus: 5 zombies

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0634 `wiki-sigils-necromancy-013`: "When viewers send a horde, you also get 5 zombies of your own." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0634 `wiki-zombies-009`: "when a horde is released, every living Necromancy contestant also gets 5 zombies where they stand." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- M-0634 reading A: `on horde release, each living Necromancy contestant gains 5 owned zombies at their position`
- M-0634 parameter `bonus_zombies`: 5
- M-0634 parameter `zombie_lifetime_s`: UNKNOWN, see U-0612

**Open questions:**

- [U-0612](../unknowns.md#u-0612) (high): How long do summoned, death and horde-bonus zombies live ('A zombie disappears when its time runs out')?

Notes (M-0634): The zombies page adds 'living' and 'where they stand'. Horde zombies (50 of them, at random points) have no owner: they are not part of this mechanic.

### M-0635: Necromancy owned zombie drain and HP transfer

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0635 `wiki-sigils-necromancy-014`: "Your zombies drain 1 HP every 10s from contestants within 5m (16ft), up to 30 HP per contestant for each zombie." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0635 `wiki-sigils-necromancy-015`: "The HP goes to you." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0635 `wiki-zombies-002`: "drain 1 HP from any contestants within 5m (16ft) every 10s." ([source](https://iceposeidon.com/safezone/wiki/zombies))
- M-0635 `wiki-zombies-003`: "Each zombie can drain at most 30 HP from each contestant." ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- M-0635 reading A: `each owned zombie: every 10 s, for each contestant within 5 m: victim -1 HP (until 30 total per zombie per victim), owner += actual HP removed, capped at maxHP`
- M-0635 reading B: `owner += nominal 1 HP per tick regardless of armor, capped at maxHP`
- M-0635 domain: integer HP
- M-0635 parameter `drain_hp`: 1
- M-0635 parameter `interval_s`: 10
- M-0635 parameter `radius_m`: 5
- M-0635 parameter `cap_hp`: 30

**Open questions:**

- [U-0613](../unknowns.md#u-0613) (high): Necromancy 'The HP goes to you': is the gain the HP the victim actually lost, is it capped at the owner's max HP, and does a blocked or armor-absorbed drain give HP and tokens?
- [U-0008](../unknowns.md#u-0008) (high): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0635): Cap semantics (lifetime or per encounter) is U-0008. Nearest-contestant chase at 1.4 m/s is in the zombies page (other family).

### M-0636: Necromancy immunity to zombies

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- M-0636 `wiki-sigils-necromancy-006`: "Immune to" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))
- M-0636 `wiki-sigils-necromancy-007`: "Zombies" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))
- M-0636 `wiki-sigils-necromancy-016`: "Fully immune from zombies." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- M-0636 `wiki-damage-010`: "| Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- M-0636 reading A: `damage from zombies to a Necromancy contestant = 0 (every zombie, every owner)`
- M-0636 reading B: `A for drain only`

**Open questions:**

- [U-0616](../unknowns.md#u-0616) (medium): Necromancy 'Fully immune from zombies': does it cover horde and guard zombies of other Necromancy contestants, and also the 10% potion break and 40% craft destruction?

Notes (M-0636): The damage table lists Necromancy as a blocker of the zombie drain row, consistent.

## Simulation check

Theorems with tests in `sim/tests/`: [T-0010](../theorems/T-0010.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0008](../unknowns.md#u-0008), [U-0403](../unknowns.md#u-0403), [U-0424](../unknowns.md#u-0424), [U-0425](../unknowns.md#u-0425), [U-0426](../unknowns.md#u-0426), [U-0427](../unknowns.md#u-0427), [U-0428](../unknowns.md#u-0428), [U-0429](../unknowns.md#u-0429), [U-0430](../unknowns.md#u-0430), [U-0431](../unknowns.md#u-0431), [U-0522](../unknowns.md#u-0522), [U-0611](../unknowns.md#u-0611), [U-0612](../unknowns.md#u-0612), [U-0613](../unknowns.md#u-0613), [U-0615](../unknowns.md#u-0615), [U-0616](../unknowns.md#u-0616)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
