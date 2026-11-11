# Sigil of Death

## Summary

Rules that name the Sigil of Death, as the wiki states them on 2026-11-11.

### In plain words

Death is the "grave robber" class. Its stats are the plain ones, 100 maximum HP and 3 inventory slots ([M-0602](../rules/sigil.md#m-0602)), and it gets stronger as other people die. The player who picks it is basically betting that the event will produce many bodies.

The central action is robbing gravestones. Within 10 m (33 ft) you can rob a gravestone to heal 5% of your max HP, and even empty gravestones can be robbed; being the first to loot an item or blood tokens from one also counts as robbing it ([M-0611](../rules/sigil.md#m-0611)). Each gravestone can be robbed once, and a robbed gravestone can never be revived ([M-0612](../rules/revival.md#m-0612)). This is the part other players will feel: if a Death player robs your gravestone, or is the first to loot it, you can never be revived ([M-0116](../rules/revival.md#m-0116)).

Death also feeds on eliminations. You earn ten blood tokens per gravestone robbed and one whenever another contestant dies ([M-0610](../rules/economy.md#m-0610)). When a contestant dies within 50 m (164 ft) of you, you heal 1 HP for every contestant eliminated so far, them included ([M-0613](../rules/sigil.md#m-0613)). Later in the event this is capped: when 20% or fewer of the contestants are alive, that heal cannot take you above 60% of your max HP ([M-0614](../rules/sigil.md#m-0614)).

For defense there is the Death Ward: the first hit from outside the circle is blocked, and you are protected for 2 minutes, with a 2 hour cooldown ([M-0615](../rules/sigil.md#m-0615)). The same ability is worded more narrowly on the damage page ([M-0137](../rules/damage.md#m-0137)).

Strongest as written: the permanent harm done to a victim's revival chances ([M-0116](../rules/revival.md#m-0116)), and healing that grows with the death count ([M-0613](../rules/sigil.md#m-0613)). Weakest: the healing is capped late in the event ([M-0614](../rules/sigil.md#m-0614)), and it needs bodies nearby ([M-0613](../rules/sigil.md#m-0613)).

What is unknown: the rounding of the 5% heal when max HP is not 100 ([U-0600](../unknowns.md#u-0600)). It is open what counts as "eliminated so far" and whether a revived contestant still counts ([U-0601](../unknowns.md#u-0601)), how the 20% threshold is computed ([U-0602](../unknowns.md#u-0602)), and what the cap does if you are already above 60% ([U-0603](../unknowns.md#u-0603)). It is open whether the token for another death has a distance limit ([U-0605](../unknowns.md#u-0605)). For the Ward, it is open when the cooldown starts ([U-0604](../unknowns.md#u-0604), [U-0119](../unknowns.md#u-0119)) and whether it covers unsafe circles as well as the outside of the circle ([U-0604](../unknowns.md#u-0604)).

This page gathers 9 rules (3 `DOCUMENTED`, 6 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0116"></a>

### M-0116: Death sigil robbing or first looting a gravestone ends revivability

Label: `DOCUMENTED`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0116](../rules/revival.md#m-0116) `wiki-019`: "If a Sigil of death player robs your gravestone, or is the first to loot it, you can never be revived." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- [M-0116](../rules/revival.md#m-0116) reading A: `revivable(grave) = false permanently once a Death contestant robs it, or is the first looter of it`

Notes ([M-0116](../rules/revival.md#m-0116)): Compared with the Death sigil page ('Each gravestone can be robbed once, and a robbed gravestone can never be revived', 'If you are the first to loot an item or blood tokens from a gravestone, you also rob it'): same rule, no mismatch found. Sigil-specific details not duplicated.

<a id="m-0137"></a>

### M-0137: Death Ward: first outside-circle hit blocked, then 2 min of outside-circle immunity, cooldown 2 h

Label: `CONDITIONAL`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0137](../rules/damage.md#m-0137) `wiki-damage-073`: "Death Ward: a Death contestant's first hit from outside the circle is blocked, and damage from outside the circle is blocked for 2min." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [M-0137](../rules/damage.md#m-0137) `wiki-damage-074`: "Cooldown 2h." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0137](../rules/damage.md#m-0137) reading A: `Death contestant: first outside-circle hit blocked; outside-circle damage blocked for 120 s; then cooldown 7200 s`
- [M-0137](../rules/damage.md#m-0137) reading B: `window and cooldown start at activation`
- [M-0137](../rules/damage.md#m-0137) parameter `window_s`: 120
- [M-0137](../rules/damage.md#m-0137) parameter `cooldown_s`: 7200

**Open questions:**

- [U-0119](../unknowns.md#u-0119) (medium): Death Ward: does the 2 min of immunity start at the first blocked hit or when the sigil is selected; does 'Cooldown 2h' start at activation or at the end of the 2 min, and is the ward available once per cooldown?

**Contradictions:** [C-0103](../unknowns.md#c-0103)

Notes ([M-0137](../rules/damage.md#m-0137)): The Death sigil page words the ward differently (adds unsafe circle): [C-0103](../unknowns.md#c-0103). Sigil-specific mechanics not duplicated.

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

<a id="m-0610"></a>

### M-0610: Death blood token income

Label: `CONDITIONAL`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0610](../rules/economy.md#m-0610) `wiki-sigils-death-006`: "Earn ten blood tokens per gravestone robbed and one whenever another contestant dies." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))

**Formal model:**

- [M-0610](../rules/economy.md#m-0610) reading A: `tokens += 10 per gravestone robbed; tokens += 1 per death of another contestant, anywhere`
- [M-0610](../rules/economy.md#m-0610) reading B: `same, but the 1 token requires the death within 50m`
- [M-0610](../rules/economy.md#m-0610) domain: integer token counts
- [M-0610](../rules/economy.md#m-0610) parameter `death_token_range_m`: UNKNOWN, see [U-0605](../unknowns.md#u-0605)

**Open questions:**

- [U-0605](../unknowns.md#u-0605) (medium): Death sigil '1 blood token whenever another contestant dies': is there a distance limit (heal uses 50m), and does a revive or second death pay again?
- [U-0606](../unknowns.md#u-0606) (high): Death 'rob': does first-looting an item or blood tokens give the same 5% heal and 10 tokens as the 'rob a gravestone' action, and can blood tokens be looted while locked for revival?

Notes ([M-0610](../rules/economy.md#m-0610)): The 10m rob range and the 50m heal range are stated on other lines; the token line gives no range.

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

<a id="m-0612"></a>

### M-0612: Robbed gravestone: once only, never revivable

Label: `DOCUMENTED`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- [M-0612](../rules/revival.md#m-0612) `wiki-sigils-death-010`: "Each gravestone can be robbed once, and a robbed gravestone can never be revived." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
- [M-0612](../rules/revival.md#m-0612) `wiki-019`: "If a Sigil of death player robs your gravestone, or is the first to loot it, you can never be revived." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- [M-0612](../rules/revival.md#m-0612) reading A: `robbed(g) is a one-way flag; robbed(g) implies not revivable(g) forever`
- [M-0612](../rules/revival.md#m-0612) domain: gravestone g

**Interactions:** [M-0611](../rules/sigil.md#m-0611)

Notes ([M-0612](../rules/revival.md#m-0612)): The overview page and the Death page agree. The intro page speaks of 'robs ... or is the first to loot'; the Death page says looting an item or tokens first counts as a rob.

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

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0009](../unknowns.md#u-0009), [U-0119](../unknowns.md#u-0119), [U-0600](../unknowns.md#u-0600), [U-0601](../unknowns.md#u-0601), [U-0602](../unknowns.md#u-0602), [U-0603](../unknowns.md#u-0603), [U-0604](../unknowns.md#u-0604), [U-0605](../unknowns.md#u-0605), [U-0606](../unknowns.md#u-0606)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
