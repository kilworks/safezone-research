# Sigil of Necromancy

## Summary

Rules that name the Sigil of Necromancy, as the wiki states them on 2026-11-11.

### In plain words

Necromancy is the "zombie master" class. Its stats are the plain ones, 100 maximum HP and 3 inventory slots ([M-0604](../rules/sigil.md#m-0604)), but it is the only sigil that makes zombies work for it. Zombies are normally a threat to everyone; for a Necromancer they are a power source, and the sigil makes you fully immune to zombies ([M-0636](../rules/zombies.md#m-0636)).

Zombies come to you in four ways. You can summon one where you stand, up to 3 times every 6 hours ([M-0631](../rules/zombies.md#m-0631)). When any contestant dies, a zombie of yours appears within 10 m (33 ft) of you ([M-0632](../rules/zombies.md#m-0632)). When viewers send a horde, you also get 5 zombies of your own ([M-0634](../rules/zombies.md#m-0634)). And when a contestant dies within 50 m (164 ft) of you, a guard zombie stands 10 m from their gravestone for 1 hour, draining 2 HP every 5 seconds from anyone within 10 m, up to 30 HP per contestant ([M-0633](../rules/zombies.md#m-0633)).

The zombies you own drain 1 HP every 10 seconds from contestants within 5 m (16 ft), up to 30 HP per contestant for each zombie, and the HP goes to you ([M-0635](../rules/zombies.md#m-0635)). You also earn one blood token for each zombie of yours that appears and one per HP your zombies drain ([M-0630](../rules/economy.md#m-0630)).

In play you would feel like a slow, spreading menace: the more people die, the more zombies you collect, and the more HP you steal from anyone who walks near them. Your bodyguards are the zombies themselves, because nobody else is immune ([M-0636](../rules/zombies.md#m-0636)).

Strongest as written: the immunity ([M-0636](../rules/zombies.md#m-0636)) and the way the sigil scales with deaths ([M-0632](../rules/zombies.md#m-0632), [M-0633](../rules/zombies.md#m-0633)). Weakest: it depends on events, deaths, hordes and a limited summon ([M-0631](../rules/zombies.md#m-0631)), and it has no stat bonus ([M-0604](../rules/sigil.md#m-0604)).

What is unknown: how long summoned, death and horde-bonus zombies live ([U-0612](../unknowns.md#u-0612)), and whether the summon limit is a rolling window, fixed blocks or charges ([U-0428](../unknowns.md#u-0428), [U-0611](../unknowns.md#u-0611)). It is open whether guard zombies and horde-bonus zombies send drained HP to you and count for tokens ([U-0614](../unknowns.md#u-0614)), and whether the HP gained is what the victim really lost ([U-0613](../unknowns.md#u-0613)). It is open whether the 30 HP cap is per zombie lifetime, per encounter or per day ([U-0008](../unknowns.md#u-0008)), and whether the immunity covers other Necromancers' zombies ([U-0616](../unknowns.md#u-0616)). Whether guard zombies chase or stay put is open ([U-0429](../unknowns.md#u-0429)).

This page gathers 12 rules (1 `DOCUMENTED`, 11 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0446"></a>

### M-0446: Zombie Summon

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0446](../rules/zombies.md#m-0446) `wiki-zombies-007`: "Summon: a Necromancy contestant summons a zombie where they stand, up to 3 times every 6h." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- [M-0446](../rules/zombies.md#m-0446) reading A: `at most 3 summons in any 6h; a zombie appears where the contestant stands`
- [M-0446](../rules/zombies.md#m-0446) reading B: `fixed blocks`
- [M-0446](../rules/zombies.md#m-0446) reading C: `6h lockout`
- [M-0446](../rules/zombies.md#m-0446) domain: uses <= 3 per 6h
- [M-0446](../rules/zombies.md#m-0446) parameter `uses`: 3
- [M-0446](../rules/zombies.md#m-0446) parameter `window`: 6 h

**Open questions:**

- [U-0428](../unknowns.md#u-0428) (low): Summon rate: 'up to 3 times every 6h'. Fixed 6h blocks, a rolling 6h window, or a cooldown after the third use?
- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

<a id="m-0447"></a>

### M-0447: Zombie on any death

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0447](../rules/zombies.md#m-0447) `wiki-zombies-008`: "Death: when any contestant dies, every living Necromancy contestant gets a zombie within 10m (33ft) of themselves." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- [M-0447](../rules/zombies.md#m-0447) reading A: `on any contestant death, each living Necromancy contestant gets a zombie within 10m`
- [M-0447](../rules/zombies.md#m-0447) domain: radius 10 m
- [M-0447](../rules/zombies.md#m-0447) parameter `radius`: 10 m

**Open questions:**

- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

Notes ([M-0447](../rules/zombies.md#m-0447)): Necromancy page: same rule, and blood token per zombie appearing.

<a id="m-0448"></a>

### M-0448: Horde bonus

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0448](../rules/zombies.md#m-0448) `wiki-zombies-009`: "Horde bonus: when a horde is released, every living Necromancy contestant also gets 5 zombies where they stand." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- [M-0448](../rules/zombies.md#m-0448) reading A: `on horde release, each living Necromancy contestant gets 5 zombies where they stand`
- [M-0448](../rules/zombies.md#m-0448) domain: count 5
- [M-0448](../rules/zombies.md#m-0448) parameter `count`: 5

**Interactions:** [M-0445](../rules/zombies.md#m-0445)

**Open questions:**

- [U-0403](../unknowns.md#u-0403) (high): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release?

<a id="m-0449"></a>

### M-0449: Guard zombies

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0449](../rules/zombies.md#m-0449) `wiki-zombies-010`: "When a contestant dies within 50m (164ft) of a Necromancy contestant, a guard zombie appears 10m (33ft) from the gravestone." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))
- [M-0449](../rules/zombies.md#m-0449) `wiki-zombies-011`: "Guard zombies drain 2 HP every 5s from everyone within 10m (33ft), up to 30 HP per contestant." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))

**Formal model:**

- [M-0449](../rules/zombies.md#m-0449) reading A: `death within 50m of a Necromancy contestant: a guard zombie 10m from the gravestone drains 2 HP every 5s from contestants within 10m, up to 30 HP per contestant`
- [M-0449](../rules/zombies.md#m-0449) domain: d(death, necromancer) <= 50 m; drain range 10 m
- [M-0449](../rules/zombies.md#m-0449) parameter `hp`: 2
- [M-0449](../rules/zombies.md#m-0449) parameter `period`: 5 s
- [M-0449](../rules/zombies.md#m-0449) parameter `range`: 10 m
- [M-0449](../rules/zombies.md#m-0449) parameter `cap`: 30 HP
- [M-0449](../rules/zombies.md#m-0449) parameter `lifetime`: 1 h (Necromancy page)

**Consequences:** [T-0010](../theorems/T-0010.md)

**Open questions:**

- [U-0429](../unknowns.md#u-0429) (medium): Guard zombie: does a guard zombie stay at its spawn point or chase, is one appearing per Necromancy contestant or per death, does it also drain its owner and the dead, and does it live 1h (Necromancy page) as stated only there?
- [U-0008](../unknowns.md#u-0008) (high): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies?

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

<a id="m-0630"></a>

### M-0630: Necromancy blood token income

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0630](../rules/economy.md#m-0630) `wiki-sigils-necromancy-008`: "Earn one blood token for each zombie of yours that appears, guards and horde bonuses included, and one per HP your zombies drain." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))

**Formal model:**

- [M-0630](../rules/economy.md#m-0630) reading A: `tokens += 1 per owned zombie appearing (summon, death, horde bonus, guard); tokens += 1 per HP drained by owned zombies`
- [M-0630](../rules/economy.md#m-0630) reading B: `A, with HP drained = HP the victim actually lost after armor and caps`

**Open questions:**

- [U-0613](../unknowns.md#u-0613) (high): Necromancy 'The HP goes to you': is the gain the HP the victim actually lost, is it capped at the owner's max HP, and does a blocked or armor-absorbed drain give HP and tokens?
- [U-0614](../unknowns.md#u-0614) (medium): Do guard zombies and horde-bonus zombies drain HP to their Necromancy owner and count in 'one per HP your zombies drain'?

Notes ([M-0630](../rules/economy.md#m-0630)): A horde bonus gives 5 zombies and so 5 tokens.

<a id="m-0631"></a>

### M-0631: Necromancy summon: up to 3 times every 6h

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0631](../rules/zombies.md#m-0631) `wiki-sigils-necromancy-009`: "Summon a zombie where you stand, up to 3 times every 6h." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0631](../rules/zombies.md#m-0631) `wiki-zombies-007`: "a Necromancy contestant summons a zombie where they stand, up to 3 times every 6h." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- [M-0631](../rules/zombies.md#m-0631) reading A: `at most 3 summons in any rolling 21600 s`
- [M-0631](../rules/zombies.md#m-0631) reading B: `counter resets at fixed 21600 s boundaries`
- [M-0631](../rules/zombies.md#m-0631) reading C: `3 charges, refill 6 h after the first of the batch`
- [M-0631](../rules/zombies.md#m-0631) domain: seconds
- [M-0631](../rules/zombies.md#m-0631) parameter `summon_cap`: 3
- [M-0631](../rules/zombies.md#m-0631) parameter `window_s`: 21600
- [M-0631](../rules/zombies.md#m-0631) parameter `zombie_lifetime_s`: UNKNOWN, see [U-0612](../unknowns.md#u-0612)

**Open questions:**

- [U-0611](../unknowns.md#u-0611) (medium): Necromancy summon 'up to 3 times every 6h': rolling window, fixed 6h blocks, or three charges refilled on a timer?
- [U-0612](../unknowns.md#u-0612) (high): How long do summoned, death and horde-bonus zombies live ('A zombie disappears when its time runs out')?

Notes ([M-0631](../rules/zombies.md#m-0631)): The two pages agree.

<a id="m-0632"></a>

### M-0632: Necromancy death zombie within 10m

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0632](../rules/zombies.md#m-0632) `wiki-sigils-necromancy-010`: "When any contestant dies, a zombie of yours appears within 10m (33ft) of you." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0632](../rules/zombies.md#m-0632) `wiki-zombies-008`: "when any contestant dies, every living Necromancy contestant gets a zombie within 10m (33ft) of themselves." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- [M-0632](../rules/zombies.md#m-0632) reading A: `for each death of any contestant, each living Necromancy contestant gets one owned zombie within 10 m`
- [M-0632](../rules/zombies.md#m-0632) parameter `zombie_lifetime_s`: UNKNOWN, see [U-0612](../unknowns.md#u-0612)

**Open questions:**

- [U-0612](../unknowns.md#u-0612) (high): How long do summoned, death and horde-bonus zombies live ('A zombie disappears when its time runs out')?

Notes ([M-0632](../rules/zombies.md#m-0632)): The zombies page adds 'living'. No distance limit on the death. A Necromancy contestant dying themselves is not covered.

<a id="m-0633"></a>

### M-0633: Necromancy guard zombie at a gravestone

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0633](../rules/zombies.md#m-0633) `wiki-sigils-necromancy-011`: "When a contestant dies within 50m (164ft) of you, a guard zombie stands 10m (33ft) from their gravestone for 1h." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0633](../rules/zombies.md#m-0633) `wiki-sigils-necromancy-012`: "It drains 2 HP every 5s from anyone within 10m (33ft), up to 30 HP per contestant." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0633](../rules/zombies.md#m-0633) `wiki-zombies-010`: "a guard zombie appears 10m (33ft) from the gravestone." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))
- [M-0633](../rules/zombies.md#m-0633) `wiki-zombies-011`: "Guard zombies drain 2 HP every 5s from everyone within 10m (33ft), up to 30 HP per contestant." ([source](https://iceposeidon.com/safezone/wiki/zombies#guard-zombies))

**Formal model:**

- [M-0633](../rules/zombies.md#m-0633) reading A: `per death within 50 m of a Necromancy contestant: guard zombie at 10 m from the grave for 3600 s, drains 2 HP per 5 s within 10 m, at most 30 HP per contestant per guard zombie`
- [M-0633](../rules/zombies.md#m-0633) reading B: `A, with the 30 HP cap shared by all guard zombies`
- [M-0633](../rules/zombies.md#m-0633) domain: seconds, HP
- [M-0633](../rules/zombies.md#m-0633) parameter `duration_s`: 3600
- [M-0633](../rules/zombies.md#m-0633) parameter `drain_hp`: 2
- [M-0633](../rules/zombies.md#m-0633) parameter `interval_s`: 5
- [M-0633](../rules/zombies.md#m-0633) parameter `radius_m`: 10
- [M-0633](../rules/zombies.md#m-0633) parameter `cap_hp`: 30

**Open questions:**

- [U-0615](../unknowns.md#u-0615) (medium): Guard zombie 'up to 30 HP per contestant': per guard zombie, or shared across all guard zombies on the same contestant? Does it stand still all hour?
- [U-0008](../unknowns.md#u-0008) (high): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0633](../rules/zombies.md#m-0633)): The zombies page gives no duration for the guard zombie; the sigil page gives 1h. First drain tick timing is not stated. Owner immunity: see [M-0636](../rules/zombies.md#m-0636).

<a id="m-0634"></a>

### M-0634: Necromancy horde bonus: 5 zombies

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0634](../rules/zombies.md#m-0634) `wiki-sigils-necromancy-013`: "When viewers send a horde, you also get 5 zombies of your own." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0634](../rules/zombies.md#m-0634) `wiki-zombies-009`: "when a horde is released, every living Necromancy contestant also gets 5 zombies where they stand." ([source](https://iceposeidon.com/safezone/wiki/zombies#sources))

**Formal model:**

- [M-0634](../rules/zombies.md#m-0634) reading A: `on horde release, each living Necromancy contestant gains 5 owned zombies at their position`
- [M-0634](../rules/zombies.md#m-0634) parameter `bonus_zombies`: 5
- [M-0634](../rules/zombies.md#m-0634) parameter `zombie_lifetime_s`: UNKNOWN, see [U-0612](../unknowns.md#u-0612)

**Open questions:**

- [U-0612](../unknowns.md#u-0612) (high): How long do summoned, death and horde-bonus zombies live ('A zombie disappears when its time runs out')?

Notes ([M-0634](../rules/zombies.md#m-0634)): The zombies page adds 'living' and 'where they stand'. Horde zombies (50 of them, at random points) have no owner: they are not part of this mechanic.

<a id="m-0635"></a>

### M-0635: Necromancy owned zombie drain and HP transfer

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0635](../rules/zombies.md#m-0635) `wiki-sigils-necromancy-014`: "Your zombies drain 1 HP every 10s from contestants within 5m (16ft), up to 30 HP per contestant for each zombie." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0635](../rules/zombies.md#m-0635) `wiki-sigils-necromancy-015`: "The HP goes to you." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0635](../rules/zombies.md#m-0635) `wiki-zombies-002`: "drain 1 HP from any contestants within 5m (16ft) every 10s." ([source](https://iceposeidon.com/safezone/wiki/zombies))
- [M-0635](../rules/zombies.md#m-0635) `wiki-zombies-003`: "Each zombie can drain at most 30 HP from each contestant." ([source](https://iceposeidon.com/safezone/wiki/zombies))

**Formal model:**

- [M-0635](../rules/zombies.md#m-0635) reading A: `each owned zombie: every 10 s, for each contestant within 5 m: victim -1 HP (until 30 total per zombie per victim), owner += actual HP removed, capped at maxHP`
- [M-0635](../rules/zombies.md#m-0635) reading B: `owner += nominal 1 HP per tick regardless of armor, capped at maxHP`
- [M-0635](../rules/zombies.md#m-0635) domain: integer HP
- [M-0635](../rules/zombies.md#m-0635) parameter `drain_hp`: 1
- [M-0635](../rules/zombies.md#m-0635) parameter `interval_s`: 10
- [M-0635](../rules/zombies.md#m-0635) parameter `radius_m`: 5
- [M-0635](../rules/zombies.md#m-0635) parameter `cap_hp`: 30

**Open questions:**

- [U-0613](../unknowns.md#u-0613) (high): Necromancy 'The HP goes to you': is the gain the HP the victim actually lost, is it capped at the owner's max HP, and does a blocked or armor-absorbed drain give HP and tokens?
- [U-0008](../unknowns.md#u-0008) (high): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0635](../rules/zombies.md#m-0635)): Cap semantics (lifetime or per encounter) is [U-0008](../unknowns.md#u-0008). Nearest-contestant chase at 1.4 m/s is in the zombies page (other family).

<a id="m-0636"></a>

### M-0636: Necromancy immunity to zombies

Label: `CONDITIONAL`. Sigils: necromancy.

**Official text** (snapshot 2026-11-11):

- [M-0636](../rules/zombies.md#m-0636) `wiki-sigils-necromancy-006`: "Immune to" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))
- [M-0636](../rules/zombies.md#m-0636) `wiki-sigils-necromancy-007`: "Zombies" ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy))
- [M-0636](../rules/zombies.md#m-0636) `wiki-sigils-necromancy-016`: "Fully immune from zombies." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [M-0636](../rules/zombies.md#m-0636) `wiki-damage-010`: "| Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0636](../rules/zombies.md#m-0636) reading A: `damage from zombies to a Necromancy contestant = 0 (every zombie, every owner)`
- [M-0636](../rules/zombies.md#m-0636) reading B: `A for drain only`

**Open questions:**

- [U-0616](../unknowns.md#u-0616) (medium): Necromancy 'Fully immune from zombies': does it cover horde and guard zombies of other Necromancy contestants, and also the 10% potion break and 40% craft destruction?

Notes ([M-0636](../rules/zombies.md#m-0636)): The damage table lists Necromancy as a blocker of the zombie drain row, consistent.

## Simulation check

Theorems with tests in `sim/tests/`: [T-0010](../theorems/T-0010.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0008](../unknowns.md#u-0008), [U-0403](../unknowns.md#u-0403), [U-0428](../unknowns.md#u-0428), [U-0429](../unknowns.md#u-0429), [U-0611](../unknowns.md#u-0611), [U-0612](../unknowns.md#u-0612), [U-0613](../unknowns.md#u-0613), [U-0614](../unknowns.md#u-0614), [U-0615](../unknowns.md#u-0615), [U-0616](../unknowns.md#u-0616)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
