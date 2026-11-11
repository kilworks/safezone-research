# Rules: revival

## Summary

Rules of the `revival` family, as the wiki states them on 2026-11-11.

This page gathers 13 rules (2 `DOCUMENTED`, 11 `CONDITIONAL`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

### M-0107: Gravestone creation at death

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0107 `wiki-007`: "When you die, a gravestone with your items appears where you were last seen." ([source](https://iceposeidon.com/safezone/wiki#damage))
- M-0107 `wiki-011`: "When you die, you leave behind a gravestone containing any items you had." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0107 reading A: `on death: gravestone(pos = position at death, items = all items carried)`
- M-0107 reading B: `gravestone(pos = last GPS fix before death)`
- M-0107 domain: all contestants

**Open questions:**

- [U-0124](../unknowns.md#u-0124) (low): Gravestone location 'where you were last seen': position at the moment of death or the last received GPS fix?

Notes (M-0107): The two sentences are the same rule (intro and Death/Revival section). Blood tokens in the grave are covered by M-0109.

### M-0108: Loot or revive a gravestone within 10 min

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0108 `wiki-008`: "Other contestants can loot it, or revive you within 10min of their death." ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- M-0108 reading A: `revive allowed while t - t_death <= 600 s (death of the dead contestant)`
- M-0108 reading B: `window counted from the reviver's death (literal pronoun)`
- M-0108 domain: t, t_death seconds
- M-0108 parameter `revive_window_s`: 600

**Open questions:**

- [U-0011](../unknowns.md#u-0011) (medium): Revive window: 'within 10min of their death' on the intro page versus 'within 10min of the death' on the Healing page: whose death starts the window?
- [U-0108](../unknowns.md#u-0108) (medium): Who can revive a non-Healing contestant: only Healing contestants (implied by the two rules), or anyone with some other rule?

Notes (M-0108): Healing page says 'within 10min of the death', same 600 s. The sigil-specific revival mechanics (5 HP cost, 10 m range) live on the Healing page and are not duplicated here.

### M-0109: Blood tokens in a grave are locked while revival is possible

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0109 `wiki-012`: "Blood tokens in the grave stay locked while revival is possible." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0109 reading A: `locked(tokens) = revival_possible(grave); unlocked afterwards`
- M-0109 reading B: `locked until revived, even past 600 s if a revive remains possible by the caps`

**Open questions:**

- [U-0105](../unknowns.md#u-0105) (medium): 'Blood tokens in the grave stay locked while revival is possible': whose tokens, for how long, and what happens at the end of the lock?
- [U-0011](../unknowns.md#u-0011) (medium): Revive window: 'within 10min of their death' on the intro page versus 'within 10min of the death' on the Healing page: whose death starts the window?
- [U-0107](../unknowns.md#u-0107) (high): Revival caps '2 times' (on a Healing contestant) and '10 times' (by a Healing contestant): what is the counter attached to?

Notes (M-0109): 'Revival possible' depends on the window, the revive caps and the Death-sigil robbery rule (M-0116).

### M-0112: Any contestant can revive a Healing contestant, up to 2 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0112 `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0112 reading A: `revives_received(h) <= 2 for each Healing contestant h`
- M-0112 reading B: `limit counts per reviver-target pair`
- M-0112 domain: Healing contestant h
- M-0112 parameter `max_revives_received`: 2

**Open questions:**

- [U-0107](../unknowns.md#u-0107) (high): Revival caps '2 times' (on a Healing contestant) and '10 times' (by a Healing contestant): what is the counter attached to?
- [U-0108](../unknowns.md#u-0108) (medium): Who can revive a non-Healing contestant: only Healing contestants (implied by the two rules), or anyone with some other rule?

**Contradictions:** [C-0105](../unknowns.md#c-0105)

Notes (M-0112): Healing page adds 'living contestant within 10m of your gravestone' and says 'You can revive ... up to 10 times': see C-0104. Sigil-specific details are compared, not duplicated.

### M-0113: A Healing contestant can revive any sigil, up to 10 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0113 `wiki-016`: "A Healing contestant can revive a contestant of any sigil, up to 10 times." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0113 reading A: `revives_performed(h) <= 10 for each Healing contestant h`
- M-0113 reading B: `limit counts per target`
- M-0113 reading C: `when the target is Healing the 2-times cap (M-0112) binds`
- M-0113 parameter `max_revives_performed`: 10

**Interactions:** M-0112

**Open questions:**

- [U-0107](../unknowns.md#u-0107) (high): Revival caps '2 times' (on a Healing contestant) and '10 times' (by a Healing contestant): what is the counter attached to?
- [U-0108](../unknowns.md#u-0108) (medium): Who can revive a non-Healing contestant: only Healing contestants (implied by the two rules), or anyone with some other rule?

### M-0114: Revived contestant gets back the items still in the gravestone

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0114 `wiki-017`: "The revived contestant gets back the items still in their gravestone." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0114 reading A: `on revive: inventory := items(grave) subject to capacity (M-0115); grave items removed`

**Interactions:** M-0107

**Open questions:**

- [U-0109](../unknowns.md#u-0109) (low): 'Items that do not fit stay in the gravestone': what is the capacity rule at revival, and what happens later to items left in the grave?
- [U-0105](../unknowns.md#u-0105) (medium): 'Blood tokens in the grave stay locked while revival is possible': whose tokens, for how long, and what happens at the end of the lock?

Notes (M-0114): Only items that remain are returned: items taken by looters before the revive are gone.

### M-0115: Items that do not fit stay in the gravestone

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- M-0115 `wiki-018`: "Items that do not fit stay in the gravestone." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0115 reading A: `leftover = items(grave) minus the fitting subset; leftover remains in the grave`
- M-0115 reading B: `leftover is dropped on the ground`
- M-0115 parameter `inventory_capacity`: UNKNOWN, see U-0109

**Interactions:** M-0114

**Open questions:**

- [U-0109](../unknowns.md#u-0109) (low): 'Items that do not fit stay in the gravestone': what is the capacity rule at revival, and what happens later to items left in the grave?

### M-0116: Death sigil robbing or first looting a gravestone ends revivability

Label: `DOCUMENTED`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- M-0116 `wiki-019`: "If a Sigil of death player robs your gravestone, or is the first to loot it, you can never be revived." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0116 reading A: `revivable(grave) = false permanently once a Death contestant robs it, or is the first looter of it`

Notes (M-0116): Compared with the Death sigil page ('Each gravestone can be robbed once, and a robbed gravestone can never be revived', 'If you are the first to loot an item or blood tokens from a gravestone, you also rob it'): same rule, no mismatch found. Sigil-specific details not duplicated.

### M-0612: Robbed gravestone: once only, never revivable

Label: `DOCUMENTED`. Sigils: death.

**Official text** (snapshot 2026-11-11):

- M-0612 `wiki-sigils-death-010`: "Each gravestone can be robbed once, and a robbed gravestone can never be revived." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
- M-0612 `wiki-019`: "If a Sigil of death player robs your gravestone, or is the first to loot it, you can never be revived." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0612 reading A: `robbed(g) is a one-way flag; robbed(g) implies not revivable(g) forever`
- M-0612 domain: gravestone g

**Interactions:** M-0611

Notes (M-0612): The overview page and the Death page agree. The intro page speaks of 'robs ... or is the first to loot'; the Death page says looting an item or tokens first counts as a rob.

### M-0653: Healing contestant revived by any contestant, up to 2 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0653 `wiki-sigils-healing-011`: "Any living contestant within 10m (33ft) of your gravestone can revive you, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- M-0653 `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki#death))
- M-0653 `wiki-strategy-014`: "Death is not always the end, a Healing contestant could revive you." ([source](https://iceposeidon.com/safezone/wiki/strategy#death))

**Formal model:**

- M-0653 reading A: `revive(g) allowed if reviver is living, within 10 m of g, and revives_of(target) < 2`
- M-0653 reading B: `limit counted per reviver`
- M-0653 parameter `max_revives_of_healing`: 2
- M-0653 parameter `range_m`: 10

**Open questions:**

- [U-0624](../unknowns.md#u-0624) (high): Healing revive counters: '2 times' (a Healing contestant being revived) and '10 times' (a Healing contestant reviving): per event, per pair, and do cancelled or failed revives count?
- [U-0011](../unknowns.md#u-0011) (medium): Revive window: 'within 10min of their death' on the intro page versus 'within 10min of the death' on the Healing page: whose death starts the window?

Notes (M-0653): The strategy sentence only names the Healing contestant as a reviver; it does not mention the other path.

### M-0654: Healing contestant revives any sigil, up to 10 times

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0654 `wiki-sigils-healing-012`: "You can revive a contestant of any sigil, up to 10 times." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- M-0654 `wiki-016`: "A Healing contestant can revive a contestant of any sigil, up to 10 times." ([source](https://iceposeidon.com/safezone/wiki#death))

**Formal model:**

- M-0654 reading A: `revives_by(h) < 10 per Healing contestant h, successful revives`
- M-0654 parameter `max_revives_by`: 10
- M-0654 parameter `range_m`: UNKNOWN, see U-0626

**Open questions:**

- [U-0624](../unknowns.md#u-0624) (high): Healing revive counters: '2 times' (a Healing contestant being revived) and '10 times' (a Healing contestant reviving): per event, per pair, and do cancelled or failed revives count?
- [U-0626](../unknowns.md#u-0626) (medium): Range for a Healing contestant to revive a non-Healing contestant: the Healing page gives 10m of the gravestone only when a Healing contestant is the one revived.

### M-0655: Revive window: 10min from the death

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0655 `wiki-sigils-healing-013`: "A revive must happen within 10min of the death." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))
- M-0655 `wiki-008`: "revive you within 10min of their death." ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- M-0655 reading A: `revive allowed iff t_now - t_death <= 600 s, t_death of the dead contestant`
- M-0655 reading B: `t_death of the reviver`
- M-0655 domain: seconds
- M-0655 parameter `window_s`: 600

**Open questions:**

- [U-0011](../unknowns.md#u-0011) (medium): Revive window: 'within 10min of their death' on the intro page versus 'within 10min of the death' on the Healing page: whose death starts the window?

Notes (M-0655): Boundary (<= or <) is not stated. Compare wiki-012: blood tokens in the grave stay locked while revival is possible.

### M-0656: Revive cost 5 HP and return with 5 HP

Label: `CONDITIONAL`. Sigils: healing.

**Official text** (snapshot 2026-11-11):

- M-0656 `wiki-sigils-healing-014`: "It costs the reviver 5 HP and brings the contestant back with 5 HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

**Formal model:**

- M-0656 reading A: `reviver HP -= 5 (requires HP > 5); target HP := 5`
- M-0656 reading B: `reviver may drop to 0 and die`
- M-0656 reading C: `reviver HP -= min(5, HP-1)`
- M-0656 domain: integer HP
- M-0656 parameter `cost_hp`: 5
- M-0656 parameter `revived_hp`: 5

**Open questions:**

- [U-0625](../unknowns.md#u-0625) (high): Revive cost 'costs the reviver 5 HP': can it kill a reviver with 5 HP or fewer, and does it run through the hit pipeline (armor, fortress, Kick live)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes (M-0656): Revived contestant also gets back items from the gravestone (intro page). Whether the cost goes through the damage pipeline is U-0002.

## Simulation check

No theorem or simulation covers this page yet.

## Open questions

[U-0002](../unknowns.md#u-0002), [U-0011](../unknowns.md#u-0011), [U-0105](../unknowns.md#u-0105), [U-0107](../unknowns.md#u-0107), [U-0108](../unknowns.md#u-0108), [U-0109](../unknowns.md#u-0109), [U-0124](../unknowns.md#u-0124), [U-0624](../unknowns.md#u-0624), [U-0625](../unknowns.md#u-0625), [U-0626](../unknowns.md#u-0626)

## Confidence

`CONDITIONAL`: the lowest label among the rules on this page.
