# Sigil of Healing

## Summary

Rules that name the Sigil of Healing, as the wiki states them on 2026-11-11.

### In plain words

Healing is the "medic" class. Its stats are the plain ones, 100 maximum HP and 3 inventory slots ([M-0606](../rules/sigil.md#m-0606)), and its job is to keep people alive, including by bringing them back.

The everyday tool is the heal ability: you heal a nearby contestant for 1 HP and cure their poison, it also stops Deep Cut bleeding, and the cooldown is 10 minutes ([M-0651](../rules/healing.md#m-0651)). Poison can be cured by Anti poison, Healing healing, or God's Fruit, so a Healing player is one of three answers to poison ([M-0174](../rules/poison.md#m-0174)). You also regenerate 1 HP every 30 minutes, up to your max HP ([M-0652](../rules/healing.md#m-0652)). Note that this slow regeneration is Healing's own, not a power of any other sigil ([M-0652](../rules/healing.md#m-0652)).

The big tool is revival. A Healing contestant can revive a contestant of any sigil, up to 10 times ([M-0654](../rules/revival.md#m-0654)). A revive must happen within 10 minutes of the death ([M-0655](../rules/revival.md#m-0655)), it costs the reviver 5 HP, and it brings the contestant back with 5 HP ([M-0656](../rules/revival.md#m-0656)). Healing players are also easier to bring back themselves: any living contestant within 10 m (33 ft) of your gravestone can revive you, up to 2 times ([M-0653](../rules/revival.md#m-0653)).

Income is small and steady: one blood token per heal and twenty per revive ([M-0650](../rules/economy.md#m-0650)). So a Healing player earns most from revives ([M-0650](../rules/economy.md#m-0650)).

What a player would feel: a patient role. The heal is tiny and slow ([M-0651](../rules/healing.md#m-0651)), so the weight of the sigil sits in the revives ([M-0654](../rules/revival.md#m-0654)) and the poison cure ([M-0174](../rules/poison.md#m-0174)). Strongest as written: revival of any sigil ([M-0654](../rules/revival.md#m-0654)) and the poison and bleeding cure ([M-0651](../rules/healing.md#m-0651)). Weakest: the heal is 1 HP with a 10 minute cooldown ([M-0651](../rules/healing.md#m-0651)), and the revive costs you HP ([M-0656](../rules/revival.md#m-0656)).

What is unknown: the range of the heal ([U-0622](../unknowns.md#u-0622)), and whether it can target yourself or a full-HP target and still spend the cooldown ([U-0623](../unknowns.md#u-0623)). It is open what the revive counters attach to, the event, the pair or the target ([U-0107](../unknowns.md#u-0107), [U-0624](../unknowns.md#u-0624)), and who can revive a non-Healing contestant ([U-0108](../unknowns.md#u-0108)). It is open whose death starts the 10 minute window ([U-0011](../unknowns.md#u-0011)), and whether the 5 HP cost can kill you ([U-0625](../unknowns.md#u-0625)). Whether damage resets the regeneration timer is open too ([U-0007](../unknowns.md#u-0007)).

This page gathers 11 rules (2 `DOCUMENTED`, 9 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0112"></a>

### M-0112: Any contestant can revive a Healing contestant, up to 2 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0112](../rules/revival.md#m-0112) `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- [M-0112](../rules/revival.md#m-0112) reading A: `revives_received(h) <= 2 for each Healing contestant h`
- [M-0112](../rules/revival.md#m-0112) reading B: `limit counts per reviver-target pair`
- [M-0112](../rules/revival.md#m-0112) domain: Healing contestant h
- [M-0112](../rules/revival.md#m-0112) parameter `max_revives_received`: 2

**Open questions:**

- [U-0107](../unknowns.md#u-0107) (high): Revival caps '2 times' (on a Healing contestant) and '10 times' (by a Healing contestant): what is the counter attached to?
- [U-0108](../unknowns.md#u-0108) (medium): Who can revive a non-Healing contestant: only Healing contestants (implied by the two rules), or anyone with some other rule?

**Contradictions:** [C-0105](../unknowns.md#c-0105)

Notes ([M-0112](../rules/revival.md#m-0112)): Healing page adds 'living contestant within 10m of your gravestone' and says 'You can revive ... up to 10 times': see [C-0104](../unknowns.md#c-0104). Sigil-specific details are compared, not duplicated.

<a id="m-0113"></a>

### M-0113: A Healing contestant can revive any sigil, up to 10 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0113](../rules/revival.md#m-0113) `wiki-016`: "A Healing contestant can revive a contestant of any sigil, up to 10 times." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- [M-0113](../rules/revival.md#m-0113) reading A: `revives_performed(h) <= 10 for each Healing contestant h`
- [M-0113](../rules/revival.md#m-0113) reading B: `limit counts per target`
- [M-0113](../rules/revival.md#m-0113) reading C: `when the target is Healing the 2-times cap ([M-0112](../rules/revival.md#m-0112)) binds`
- [M-0113](../rules/revival.md#m-0113) parameter `max_revives_performed`: 10

**Interactions:** [M-0112](../rules/revival.md#m-0112)

**Open questions:**

- [U-0107](../unknowns.md#u-0107) (high): Revival caps '2 times' (on a Healing contestant) and '10 times' (by a Healing contestant): what is the counter attached to?
- [U-0108](../unknowns.md#u-0108) (medium): Who can revive a non-Healing contestant: only Healing contestants (implied by the two rules), or anyone with some other rule?

<a id="m-0174"></a>

### M-0174: Poison cures: Anti poison, Healing healing, God's Fruit

Label: `DOCUMENTED`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0174](../rules/poison.md#m-0174) `wiki-poison-005`: "Poison can be cured by: Anti poison, Healing healing, or God's Fruit" ([source](https://iceposeidon.com/safezone/wiki/poison))

**Formal model:**

- [M-0174](../rules/poison.md#m-0174) reading A: `cure events: Anti poison, a heal by a Healing contestant, God's Fruit`

Notes ([M-0174](../rules/poison.md#m-0174)): Attribution kept as written: 'Healing healing' = healing by the Healing sigil.

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

**Consequences:** [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

Notes ([M-0606](../rules/sigil.md#m-0606)): Merchant upgrades (+10 max HP, inventory slots) change these during play; this record is the base value only. The merchant page caps slots at 13, or 20 for Endurance.

<a id="m-0650"></a>

### M-0650: Healing blood tokens: 1 per heal, 20 per revive

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0650](../rules/economy.md#m-0650) `wiki-sigils-healing-006`: "Earn one blood token per heal and twenty per revive." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- [M-0650](../rules/economy.md#m-0650) reading A: `tokens += 1 per use of the heal ability; += 20 per completed revive`
- [M-0650](../rules/economy.md#m-0650) parameter `tokens_per_heal`: 1
- [M-0650](../rules/economy.md#m-0650) parameter `tokens_per_revive`: 20

**Open questions:**

- [U-0623](../unknowns.md#u-0623) (medium): Healing ability: can it target the healer, an already full HP target, a non-poisoned target? Is the cooldown and token spent anyway?

Notes ([M-0650](../rules/economy.md#m-0650)): Does a heal on a full HP target pay: [U-0623](../unknowns.md#u-0623).

<a id="m-0651"></a>

### M-0651: Healing ability: heal 1 HP, cure poison, stop bleeding, 10min cooldown

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0651](../rules/healing.md#m-0651) `wiki-sigils-healing-008`: "Heal a nearby contestant for 1 HP and cure their poison." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- [M-0651](../rules/healing.md#m-0651) `wiki-sigils-healing-007`: "Healing also stops Deep Cut bleeding." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- [M-0651](../rules/healing.md#m-0651) `wiki-sigils-healing-009`: "Cooldown 10min." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- [M-0651](../rules/healing.md#m-0651) reading A: `target within range r: HP += 1 (capped at max HP), poison cured, Deep Cut bleeding stopped; next use after 600 s`
- [M-0651](../rules/healing.md#m-0651) domain: seconds, HP
- [M-0651](../rules/healing.md#m-0651) parameter `heal_hp`: 1
- [M-0651](../rules/healing.md#m-0651) parameter `cooldown_s`: 600
- [M-0651](../rules/healing.md#m-0651) parameter `range_m`: UNKNOWN, see [U-0622](../unknowns.md#u-0622)

**Consequences:** [T-0305](../theorems/T-0305.md)

**Open questions:**

- [U-0622](../unknowns.md#u-0622) (medium): Healing ability 'Heal a nearby contestant': what is the range?
- [U-0623](../unknowns.md#u-0623) (medium): Healing ability: can it target the healer, an already full HP target, a non-poisoned target? Is the cooldown and token spent anyway?

Notes ([M-0651](../rules/healing.md#m-0651)): Matches the poison page ('Healing healing' cures poison) and the merchant Deep Cut text (cured by a bandage or a Healing contestant).

<a id="m-0652"></a>

### M-0652: Healing passive regeneration: 1 HP every 30min

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0652](../rules/healing.md#m-0652) `wiki-sigils-healing-010`: "You regenerate 1 HP every 30min, up to your max HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- [M-0652](../rules/healing.md#m-0652) reading A: `every 1800 s on a fixed clock, damage does not reset it`
- [M-0652](../rules/healing.md#m-0652) reading B: `damage resets the 1800 s timer`
- [M-0652](../rules/healing.md#m-0652) domain: seconds
- [M-0652](../rules/healing.md#m-0652) parameter `regen_hp`: 1
- [M-0652](../rules/healing.md#m-0652) parameter `period_s`: 1800

**Consequences:** [T-0011](../theorems/T-0011.md), [T-0305](../theorems/T-0305.md)

**Open questions:**

- [U-0007](../unknowns.md#u-0007) (medium): Healing regeneration: does damage reset the 30 min timer?

Notes ([M-0652](../rules/healing.md#m-0652)): Belongs to Healing, not Necromancy. Start of the clock: event start or sigil pick is also open.

<a id="m-0653"></a>

### M-0653: Healing contestant revived by any contestant, up to 2 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0653](../rules/revival.md#m-0653) `wiki-sigils-healing-011`: "Any living contestant within 10m (33ft) of your gravestone can revive you, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- [M-0653](../rules/revival.md#m-0653) `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki#death))
- [M-0653](../rules/revival.md#m-0653) `wiki-strategy-014`: "Death is not always the end, a Healing contestant could revive you." ([source](https://iceposeidon.com/safezone/wiki/strategy#death))

**Formal model:**

- [M-0653](../rules/revival.md#m-0653) reading A: `revive(g) allowed if reviver is living, within 10 m of g, and revives_of(target) < 2`
- [M-0653](../rules/revival.md#m-0653) reading B: `limit counted per reviver`
- [M-0653](../rules/revival.md#m-0653) parameter `max_revives_of_healing`: 2
- [M-0653](../rules/revival.md#m-0653) parameter `range_m`: 10

**Open questions:**

- [U-0624](../unknowns.md#u-0624) (high): Healing revive counters: '2 times' (a Healing contestant being revived) and '10 times' (a Healing contestant reviving): per event, per pair, and do cancelled or failed revives count?
- [U-0011](../unknowns.md#u-0011) (medium): Revive window: 'within 10min of their death' on the intro page versus 'within 10min of the death' on the Healing page: whose death starts the window?

Notes ([M-0653](../rules/revival.md#m-0653)): The strategy sentence only names the Healing contestant as a reviver; it does not mention the other path.

<a id="m-0654"></a>

### M-0654: Healing contestant revives any sigil, up to 10 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0654](../rules/revival.md#m-0654) `wiki-sigils-healing-012`: "You can revive a contestant of any sigil, up to 10 times." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- [M-0654](../rules/revival.md#m-0654) `wiki-016`: "A Healing contestant can revive a contestant of any sigil, up to 10 times." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- [M-0654](../rules/revival.md#m-0654) reading A: `revives_by(h) < 10 per Healing contestant h, successful revives`
- [M-0654](../rules/revival.md#m-0654) parameter `max_revives_by`: 10
- [M-0654](../rules/revival.md#m-0654) parameter `range_m`: UNKNOWN, see [U-0626](../unknowns.md#u-0626)

**Open questions:**

- [U-0624](../unknowns.md#u-0624) (high): Healing revive counters: '2 times' (a Healing contestant being revived) and '10 times' (a Healing contestant reviving): per event, per pair, and do cancelled or failed revives count?
- [U-0626](../unknowns.md#u-0626) (medium): Range for a Healing contestant to revive a non-Healing contestant: the Healing page gives 10m of the gravestone only when a Healing contestant is the one revived.

<a id="m-0655"></a>

### M-0655: Revive window: 10min from the death

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0655](../rules/revival.md#m-0655) `wiki-sigils-healing-013`: "A revive must happen within 10min of the death." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- [M-0655](../rules/revival.md#m-0655) `wiki-008`: "revive you within 10min of their death." ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- [M-0655](../rules/revival.md#m-0655) reading A: `revive allowed iff t_now - t_death <= 600 s, t_death of the dead contestant`
- [M-0655](../rules/revival.md#m-0655) reading B: `t_death of the reviver`
- [M-0655](../rules/revival.md#m-0655) domain: seconds
- [M-0655](../rules/revival.md#m-0655) parameter `window_s`: 600

**Open questions:**

- [U-0011](../unknowns.md#u-0011) (medium): Revive window: 'within 10min of their death' on the intro page versus 'within 10min of the death' on the Healing page: whose death starts the window?

Notes ([M-0655](../rules/revival.md#m-0655)): Boundary (<= or <) is not stated. Compare wiki-012: blood tokens in the grave stay locked while revival is possible.

<a id="m-0656"></a>

### M-0656: Revive cost 5 HP and return with 5 HP

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- [M-0656](../rules/revival.md#m-0656) `wiki-sigils-healing-014`: "It costs the reviver 5 HP and brings the contestant back with 5 HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- [M-0656](../rules/revival.md#m-0656) reading A: `reviver HP -= 5 (requires HP > 5); target HP := 5`
- [M-0656](../rules/revival.md#m-0656) reading B: `reviver may drop to 0 and die`
- [M-0656](../rules/revival.md#m-0656) reading C: `reviver HP -= min(5, HP-1)`
- [M-0656](../rules/revival.md#m-0656) domain: integer HP
- [M-0656](../rules/revival.md#m-0656) parameter `cost_hp`: 5
- [M-0656](../rules/revival.md#m-0656) parameter `revived_hp`: 5

**Open questions:**

- [U-0625](../unknowns.md#u-0625) (high): Revive cost 'costs the reviver 5 HP': can it kill a reviver with 5 HP or fewer, and does it run through the hit pipeline (armor, fortress, Kick live)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0656](../rules/revival.md#m-0656)): Revived contestant also gets back items from the gravestone (intro page). Whether the cost goes through the damage pipeline is [U-0002](../unknowns.md#u-0002).

## Simulation check

Theorems with tests in `sim/tests/`: [T-0011](../theorems/T-0011.md), [T-0305](../theorems/T-0305.md), [T-0400](../theorems/T-0400.md), [T-0703](../theorems/T-0703.md)

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0007](../unknowns.md#u-0007), [U-0011](../unknowns.md#u-0011), [U-0107](../unknowns.md#u-0107), [U-0108](../unknowns.md#u-0108), [U-0622](../unknowns.md#u-0622), [U-0623](../unknowns.md#u-0623), [U-0624](../unknowns.md#u-0624), [U-0625](../unknowns.md#u-0625), [U-0626](../unknowns.md#u-0626)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
