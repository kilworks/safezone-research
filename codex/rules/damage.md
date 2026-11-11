# Rules: damage

## Summary

Rules of the `damage` family, as the wiki states them on 2026-11-11.

This page gathers 48 rules (11 `DOCUMENTED`, 35 `CONDITIONAL`, 2 `UNKNOWN`). Every rule below quotes the official wiki word for word and gives its formal reading; where the wording allows several readings, all are listed and the question stays open.

## Rules

<a id="m-0102"></a>

### M-0102: Kick-live status: 10% less damage taken, 10% more damage dealt (general statement)

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0102](../rules/damage.md#m-0102) `wiki-006`: "If you're live on Kick, you take 10% less damage and do 10% more damage" ([source](https://iceposeidon.com/safezone/wiki#damage))

**Formal model:**

- [M-0102](../rules/damage.md#m-0102) reading A: `defender live: d -> floor(9*d/10); attacker live: d -> floor(11*d/10)`
- [M-0102](../rules/damage.md#m-0102) reading B: `defender live: d -> d - floor(d/10); attacker live: d -> floor(11*d/10)`
- [M-0102](../rules/damage.md#m-0102) reading C: `attacker bonus applies to every damage source (general wording), not only the pipeline list`
- [M-0102](../rules/damage.md#m-0102) domain: d integer, d >= 0

**Open questions:**

- [U-0001](../unknowns.md#u-0001) (critical): Does the defender's Kick-live 10% reduction floor the result (A) or the removed 10% (B)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

**Contradictions:** [C-0100](../unknowns.md#c-0100)

Notes ([M-0102](../rules/damage.md#m-0102)): The pipeline page restricts the attacker bonus to a named weapon list and states the defender reduction as a separate rounded step, see [C-0100](../unknowns.md#c-0100). Rounding of the reduction is [U-0001](../unknowns.md#u-0001).

<a id="m-0117"></a>

### M-0117: Hit pipeline: seven steps in order

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0117](../rules/damage.md#m-0117) `wiki-damage-032`: "Every hit goes through these steps in order." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0117](../rules/damage.md#m-0117) reading A: `result = armor(fortress(minimum(reductions(mirror(kick_bonus(immunity(h)))))))`
- [M-0117](../rules/damage.md#m-0117) domain: h integer, h >= 0, one hit

**Consequences:** [T-0003](../theorems/T-0003.md)

**Interactions:** [M-0118](../rules/damage.md#m-0118), [M-0119](../rules/damage.md#m-0119), [M-0120](../rules/damage.md#m-0120), [M-0121](../rules/damage.md#m-0121), [M-0122](../rules/damage.md#m-0122), [M-0123](../rules/damage.md#m-0123), [M-0124](../rules/damage.md#m-0124), [M-0125](../rules/damage.md#m-0125)

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?
- [U-0103](../unknowns.md#u-0103) (high): 'A hit that gets through always does at least 1 HP' is step 5 of 7: can fortress (step 6) and armor (step 7) still reduce the final HP loss to 0?

Notes ([M-0117](../rules/damage.md#m-0117)): Which damage sources count as a hit is [U-0002](../unknowns.md#u-0002). Steps are modeled one record each: 118 immunity, 119 Kick bonus, 120 mirror, 121 and 122 reductions, 123 minimum, 124 fortress, 125 armor.

<a id="m-0118"></a>

### M-0118: Pipeline step 1: immunity

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0118](../rules/damage.md#m-0118) `wiki-damage-034`: "Immunity" ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0118](../rules/damage.md#m-0118) `wiki-damage-035`: "If anything blocks the hit, you take nothing." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0118](../rules/damage.md#m-0118) reading A: `if any blocker of the source (damage table) applies: d := 0 and stop`

**Interactions:** [M-0117](../rules/damage.md#m-0117)

**Open questions:**

- [U-0120](../unknowns.md#u-0120) (high): When several blockers apply to one hit (Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection), which one is the 'blocker' and which items are consumed? The only stated rule is 'a hit already blocked by something else does not use [the Flak jacket] up'.

Notes ([M-0118](../rules/damage.md#m-0118)): Blocker sets come from the damage table rows ([M-0140](../rules/damage.md#m-0140)..[M-0166](../rules/damage.md#m-0166)). Which blocker is consumed when several apply is [U-0120](../unknowns.md#u-0120).

<a id="m-0119"></a>

### M-0119: Pipeline step 2: attacker Kick bonus, listed weapons only

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0119](../rules/damage.md#m-0119) `wiki-damage-038`: "If the attacker is live on Kick, their own bow, staff, knife, long sword, axe, machete, drone, C4, landmine, fake chest and trapped gift hits deal 10% more, rounded down." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0119](../rules/damage.md#m-0119) reading A: `if attacker live and source in {bow, staff, knife, long sword, axe, machete, drone, C4, landmine, fake chest, trapped gift}: d := floor(11*d/10) = d + floor(d/10)`
- [M-0119](../rules/damage.md#m-0119) domain: d integer >= 0; weapon list closed (Poison Dart, missile, nuke etc. not listed)
- [M-0119](../rules/damage.md#m-0119) parameter `bonus`: 10 percent
- [M-0119](../rules/damage.md#m-0119) parameter `list`: bow, staff, knife, long sword, axe, machete, drone, C4, landmine, fake chest, trapped gift

**Consequences:** [T-0001](../theorems/T-0001.md)

**Interactions:** [M-0117](../rules/damage.md#m-0117)

**Open questions:**

- [U-0010](../unknowns.md#u-0010) (medium): Wizard staff '10 HP in total over 5 s': one hit or several ticks?
- [U-0121](../unknowns.md#u-0121) (low): Self-inflicted hits ('hit by your own C4 and landmine'): does the full pipeline run with attacker = defender, including Kick bonus (step 2) and Kick reduction (step 4), and do own-held blockers (Protection, Shield) apply?

**Contradictions:** [C-0100](../unknowns.md#c-0100)

Notes ([M-0119](../rules/damage.md#m-0119)): Single rounding reading (floor of 1.1*d is exact in binary64). 'staff' is the Wizard staff area (ticks, [U-0010](../unknowns.md#u-0010)). General wording on the intro page ('do 10% more damage') is wider: [C-0100](../unknowns.md#c-0100). Bonus precedes the mirror, so a reflected hit carries it.

<a id="m-0120"></a>

### M-0120: Pipeline step 3: Mirror forcefield sends the whole hit back

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0120](../rules/damage.md#m-0120) `wiki-damage-041`: "A Mirror forcefield sends the whole hit back to the attacker instead, before any reduction." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0120](../rules/damage.md#m-0120) reading A: `if defender mirror active and source reflectable: attacker receives d (after step 2) through the attacker's full pipeline, defender takes 0`
- [M-0120](../rules/damage.md#m-0120) reading B: `attacker receives d raw, no pipeline`

**Interactions:** [M-0117](../rules/damage.md#m-0117), [M-0119](../rules/damage.md#m-0119), [M-0134](../rules/items.md#m-0134), [M-0135](../rules/damage.md#m-0135)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0120](../rules/damage.md#m-0120)): 'Before any reduction' fixes the mirror before steps 4 to 7 of the defender. The reflected amount includes the Kick bonus (step 2 earlier). Attacker's pipeline is [U-0005](../unknowns.md#u-0005).

<a id="m-0121"></a>

### M-0121: Pipeline step 4a: Protection sigil halves nuke damage

Label: `CONDITIONAL`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0121](../rules/damage.md#m-0121) `wiki-damage-044`: "A Protection contestant takes 50% less from a nuke." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0121](../rules/damage.md#m-0121) `wiki-damage-045`: "The damage left is rounded down." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0121](../rules/damage.md#m-0121) `wiki-damage-062`: "The Protection sigil is not immune to nukes, but takes 50% less from them." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0121](../rules/damage.md#m-0121) reading A: `if defender sigil is Protection and source is nuke: d := floor(d/2); other sources unchanged`
- [M-0121](../rules/damage.md#m-0121) domain: d integer >= 0
- [M-0121](../rules/damage.md#m-0121) parameter `nuke_reduction`: 50 percent

**Interactions:** [M-0117](../rules/damage.md#m-0117)

**Open questions:**

- [U-0100](../unknowns.md#u-0100) (low): Where does 'The damage left is rounded down' apply in step 4: to the Protection 50% result only, or as one final floor after all reductions, with the Kick 10% computed on the unrounded value?

Notes ([M-0121](../rules/damage.md#m-0121)): 'Not immune to nukes, but takes 50% less'. The Protection page treats the same rule (50% less); no mismatch found. Where the floor applies is [U-0100](../unknowns.md#u-0100). The Flak jacket ([M-0130](../rules/items.md#m-0130)) blocks the nuke before this step.

<a id="m-0122"></a>

### M-0122: Pipeline step 4b: defender Kick reduction

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0122](../rules/damage.md#m-0122) `wiki-damage-046`: "Being live on Kick then takes off 10%, rounded down." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0122](../rules/damage.md#m-0122) reading A: `defender live: d := floor(9*d/10)`
- [M-0122](../rules/damage.md#m-0122) reading B: `defender live: d := d - floor(d/10)`
- [M-0122](../rules/damage.md#m-0122) domain: d integer >= 0
- [M-0122](../rules/damage.md#m-0122) parameter `reduction`: 10 percent

**Consequences:** [T-0002](../theorems/T-0002.md)

**Interactions:** [M-0117](../rules/damage.md#m-0117), [M-0121](../rules/damage.md#m-0121)

**Open questions:**

- [U-0001](../unknowns.md#u-0001) (critical): Does the defender's Kick-live 10% reduction floor the result (A) or the removed 10% (B)?
- [U-0100](../unknowns.md#u-0100) (low): Where does 'The damage left is rounded down' apply in step 4: to the Protection 50% result only, or as one final floor after all reductions, with the Kick 10% computed on the unrounded value?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0122](../rules/damage.md#m-0122)): Applied after the Protection step (stated order). A and B differ by 1 HP whenever d is not a multiple of 10 and d >= 2.

<a id="m-0123"></a>

### M-0123: Pipeline step 5: minimum 1 HP for a hit that gets through

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0123](../rules/damage.md#m-0123) `wiki-damage-048`: "Minimum" ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0123](../rules/damage.md#m-0123) `wiki-damage-049`: "A hit that gets through always does at least 1 HP." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0123](../rules/damage.md#m-0123) reading A: `d := max(1, d) if the hit was not blocked in step 1 and was not mirrored`
- [M-0123](../rules/damage.md#m-0123) reading B: `final HP loss >= 1 after steps 6 and 7`
- [M-0123](../rules/damage.md#m-0123) domain: d integer >= 0
- [M-0123](../rules/damage.md#m-0123) parameter `minimum_hp`: 1

**Consequences:** [T-0004](../theorems/T-0004.md)

**Interactions:** [M-0117](../rules/damage.md#m-0117), [M-0122](../rules/damage.md#m-0122)

**Open questions:**

- [U-0103](../unknowns.md#u-0103) (high): 'A hit that gets through always does at least 1 HP' is step 5 of 7: can fortress (step 6) and armor (step 7) still reduce the final HP loss to 0?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0123](../rules/damage.md#m-0123)): 'Always' conflicts in spirit with steps 6 and 7 that follow ([U-0103](../unknowns.md#u-0103)).

<a id="m-0124"></a>

### M-0124: Pipeline step 6: fortress absorbs up to its remaining durability

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0124](../rules/damage.md#m-0124) `wiki-damage-051`: "Fortress" ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0124](../rules/damage.md#m-0124) `wiki-damage-052`: "A fortress you stand within absorbs up to its remaining durability, whoever built it." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0124](../rules/damage.md#m-0124) reading A: `if defender stands within a fortress (any owner): a := min(d, dur); d := d - a; dur := dur - a`
- [M-0124](../rules/damage.md#m-0124) reading B: `multiple fortresses absorb in turn`
- [M-0124](../rules/damage.md#m-0124) domain: d, dur integers >= 0
- [M-0124](../rules/damage.md#m-0124) parameter `fortress_durability`: UNKNOWN on this page, see items page

**Interactions:** [M-0117](../rules/damage.md#m-0117), [M-0123](../rules/damage.md#m-0123)

**Open questions:**

- [U-0102](../unknowns.md#u-0102) (medium): Fortress step: how many fortresses can absorb one hit when the contestant stands within several, in which order, and is durability lost 1 per HP absorbed?
- [U-0103](../unknowns.md#u-0103) (high): 'A hit that gets through always does at least 1 HP' is step 5 of 7: can fortress (step 6) and armor (step 7) still reduce the final HP loss to 0?

Notes ([M-0124](../rules/damage.md#m-0124)): 'Whoever built it': the owner is irrelevant, enemy fortresses protect too. Durability values are on another page family.

<a id="m-0125"></a>

### M-0125: Pipeline step 7: Body armor absorbs what is left until it breaks

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0125](../rules/damage.md#m-0125) `wiki-damage-054`: "Armor" ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0125](../rules/damage.md#m-0125) `wiki-damage-055`: "Body armor absorbs what is left, until it breaks." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0125](../rules/damage.md#m-0125) reading A: `a := min(d, dur); d := d - a; dur := dur - a; broken when dur = 0`
- [M-0125](../rules/damage.md#m-0125) reading B: `whole remaining d absorbed, excess lost, breaks when dur reaches 0`
- [M-0125](../rules/damage.md#m-0125) domain: d, dur integers >= 0
- [M-0125](../rules/damage.md#m-0125) parameter `armor_durability`: UNKNOWN on this page, see items page

**Interactions:** [M-0117](../rules/damage.md#m-0117), [M-0124](../rules/damage.md#m-0124), [M-0126](../rules/items.md#m-0126)

**Open questions:**

- [U-0101](../unknowns.md#u-0101) (high): Body armor 'absorbs what is left, until it breaks': does a hit larger than the remaining durability pass the excess through (A), or is the whole hit absorbed and the armor simply breaks (B)? Does durability drop 1 per HP absorbed?
- [U-0103](../unknowns.md#u-0103) (high): 'A hit that gets through always does at least 1 HP' is step 5 of 7: can fortress (step 6) and armor (step 7) still reduce the final HP loss to 0?

<a id="m-0128"></a>

### M-0128: Shield does not block zone, unsafe circle or robot; Safety bubble and Reality Shield do

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0128](../rules/damage.md#m-0128) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [M-0128](../rules/damage.md#m-0128) `wiki-damage-059`: "A Safety bubble and a Reality Shield do." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0128](../rules/damage.md#m-0128) reading A: `blocks(Shield) excludes {outside circle, unsafe circle, robot}; blocks(Safety bubble) and blocks(Reality Shield) include them`

**Consequences:** [T-0008](../theorems/T-0008.md)

Notes ([M-0128](../rules/damage.md#m-0128)): Consistent with the table: the three rows list Safety bubble and no Shield. Reality Shield on those rows relies on [M-0127](../rules/items.md#m-0127).

<a id="m-0129"></a>

### M-0129: Vulnerable contestant: no protection from Shield or Safety bubble

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0129](../rules/damage.md#m-0129) `wiki-damage-060`: "A vulnerable contestant gets no protection from a Shield or a Safety Bubble." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0129](../rules/damage.md#m-0129) reading A: `if vulnerable: Shield and Safety bubble are removed from the blocker set`

Notes ([M-0129](../rules/damage.md#m-0129)): The Vulnerability Dart itself is another page.

<a id="m-0133"></a>

### M-0133: Own C4 and landmine hit you if you stand in the blast

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0133](../rules/damage.md#m-0133) `wiki-damage-068`: "You are hit by your own C4 and landmine if you stand in the blast." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0133](../rules/damage.md#m-0133) reading A: `attacker = defender is allowed for C4 and landmine; the hit goes through the pipeline`

**Open questions:**

- [U-0121](../unknowns.md#u-0121) (low): Self-inflicted hits ('hit by your own C4 and landmine'): does the full pipeline run with attacker = defender, including Kick bonus (step 2) and Kick reduction (step 4), and do own-held blockers (Protection, Shield) apply?

Notes ([M-0133](../rules/damage.md#m-0133)): Mirror never reflects your own explosives ([M-0135](../rules/damage.md#m-0135)).

<a id="m-0135"></a>

### M-0135: Mirror forcefield reflectable source list

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0135](../rules/damage.md#m-0135) `wiki-damage-070`: "It only reflects Poison Darts, fake gravestones, bows, wizard staffs, knives, long swords, Zarok's axes, machetes, drones, C4, landmines, flashbangs and fake chests, and never your own explosives." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

**Formal model:**

- [M-0135](../rules/damage.md#m-0135) reading A: `reflect iff source in {Poison Dart, fake gravestone, bow, wizard staff, knife, long sword, Zarok's axe, machete, drone, C4, landmine, flashbang, fake chest} and not own explosive`

**Interactions:** [M-0120](../rules/damage.md#m-0120)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

**Contradictions:** [C-0101](../unknowns.md#c-0101)

Notes ([M-0135](../rules/damage.md#m-0135)): The table lists Mirror forcefield (reflects) also on the Trapped gift row, which this list omits: [C-0101](../unknowns.md#c-0101).

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

<a id="m-0140"></a>

### M-0140: Damage source 'Outside the circle' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0140](../rules/damage.md#m-0140) `wiki-damage-005`: "| Outside the circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0140](../rules/damage.md#m-0140) reading A: `blockers(Outside the circle) = {Safety bubble: blocks; Guardian angel: blocks; Death Ward: blocks; Hazmat suit: slows; Body armor: absorbs}`
- [M-0140](../rules/damage.md#m-0140) domain: one hit of source 'Outside the circle'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?
- [U-0003](../unknowns.md#u-0003) (medium): Zone damage: is the first tick at 5 s or at 7 s after leaving the safe zone?

Notes ([M-0140](../rules/damage.md#m-0140)): Periodic zone damage: whether Body armor and Kick apply is [U-0002](../unknowns.md#u-0002).

<a id="m-0141"></a>

### M-0141: Damage source 'Unsafe circle' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0141](../rules/damage.md#m-0141) `wiki-damage-006`: "| Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0141](../rules/damage.md#m-0141) reading A: `blockers(Unsafe circle) = {Safety bubble: blocks; Guardian angel: blocks; Death Ward: blocks; Hazmat suit: slows; Body armor: absorbs}`
- [M-0141](../rules/damage.md#m-0141) domain: one hit of source 'Unsafe circle'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?
- [U-0123](../unknowns.md#u-0123) (medium): Hazmat suit '(slows)' in the damage table: what does slowing do to zone, unsafe-circle and robot damage (tick interval multiplier, damage fraction)?

**Contradictions:** [C-0103](../unknowns.md#c-0103)

Notes ([M-0141](../rules/damage.md#m-0141)): Unsafe circle (Trolling). The Trolling page lists Guardian angel, Safety bubble, Reality Shield, Death Ward as blockers: same set, [C-0103](../unknowns.md#c-0103) concerns Death Ward scope.

<a id="m-0142"></a>

### M-0142: Damage source 'Robot' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0142](../rules/damage.md#m-0142) `wiki-damage-007`: "| Robot | Safety bubble, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0142](../rules/damage.md#m-0142) reading A: `blockers(Robot) = {Safety bubble: blocks; Hazmat suit: slows; Body armor: absorbs}`
- [M-0142](../rules/damage.md#m-0142) domain: one hit of source 'Robot'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?
- [U-0123](../unknowns.md#u-0123) (medium): Hazmat suit '(slows)' in the damage table: what does slowing do to zone, unsafe-circle and robot damage (tick interval multiplier, damage fraction)?

Notes ([M-0142](../rules/damage.md#m-0142)): Robot damage is not blocked by Shield ([M-0128](../rules/damage.md#m-0128)) nor by Sleeping Bag ([M-0132](../rules/items.md#m-0132)).

<a id="m-0143"></a>

### M-0143: Damage source 'Poison' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0143](../rules/damage.md#m-0143) `wiki-damage-008`: "| Poison | Shield, Safety bubble, Sleeping Bag, Protection, Anti poison, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0143](../rules/damage.md#m-0143) reading A: `blockers(Poison) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Anti poison: blocks; Body armor: absorbs}`
- [M-0143](../rules/damage.md#m-0143) domain: one hit of source 'Poison'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0117](../unknowns.md#u-0117) (high): A Shield or Safety bubble 'blocks each poison step while it lasts': is a blocked step consumed (counts toward 'all its damage') or skipped (poison extended)? Does the countdown continue while protected?
- [U-0118](../unknowns.md#u-0118) (low): 'Sleeping in your own Sleeping Bag' appears as a label in the Poison immunity list with no verb: does it prevent new poison, block each step, or both?

Notes ([M-0143](../rules/damage.md#m-0143)): Poison page: Protection immune, Anti poison no new poison, Reality Shield no new poison; blocks here mean poison ticks. Mirror is absent because the Poison Dart is the reflected attack ([M-0180](../rules/poison.md#m-0180)).

<a id="m-0144"></a>

### M-0144: Damage source 'Tear gas' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0144](../rules/damage.md#m-0144) `wiki-damage-009`: "| Tear gas | Shield, Safety bubble, Sleeping Bag, Gas mask, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0144](../rules/damage.md#m-0144) reading A: `blockers(Tear gas) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Gas mask: blocks; Body armor: absorbs}`
- [M-0144](../rules/damage.md#m-0144) domain: one hit of source 'Tear gas'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0144](../rules/damage.md#m-0144)): Tear gas: Gas mask listed, matches [M-0131](../rules/items.md#m-0131).

<a id="m-0145"></a>

### M-0145: Damage source 'Zombie drain' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0145](../rules/damage.md#m-0145) `wiki-damage-010`: "| Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0145](../rules/damage.md#m-0145) reading A: `blockers(Zombie drain) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Necromancy / Repellent: blocks; Body armor: absorbs}`
- [M-0145](../rules/damage.md#m-0145) domain: one hit of source 'Zombie drain'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0145](../rules/damage.md#m-0145)): Zombie drain (periodic). 'Necromancy / Repellent' read as Necromancy sigil or Zombie repellent.

<a id="m-0146"></a>

### M-0146: Damage source 'Bow' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0146](../rules/damage.md#m-0146) `wiki-damage-011`: "| Bow | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0146](../rules/damage.md#m-0146) reading A: `blockers(Bow) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0146](../rules/damage.md#m-0146) domain: one hit of source 'Bow'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0146](../rules/damage.md#m-0146)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0147"></a>

### M-0147: Damage source 'Wizard Staff area' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0147](../rules/damage.md#m-0147) `wiki-damage-012`: "| Wizard Staff area | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0147](../rules/damage.md#m-0147) reading A: `blockers(Wizard Staff area) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0147](../rules/damage.md#m-0147) domain: one hit of source 'Wizard Staff area'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0010](../unknowns.md#u-0010) (medium): Wizard staff '10 HP in total over 5 s': one hit or several ticks?
- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0147](../rules/damage.md#m-0147)): Wizard staff area damage (5 s of area ticks, [U-0010](../unknowns.md#u-0010)). Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0148"></a>

### M-0148: Damage source 'Assassin's Knife' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0148](../rules/damage.md#m-0148) `wiki-damage-013`: "| Assassin's Knife | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0148](../rules/damage.md#m-0148) reading A: `blockers(Assassin's Knife) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0148](../rules/damage.md#m-0148) domain: one hit of source 'Assassin's Knife'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0148](../rules/damage.md#m-0148)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0149"></a>

### M-0149: Damage source 'Long Sword' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0149](../rules/damage.md#m-0149) `wiki-damage-014`: "| Long Sword | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0149](../rules/damage.md#m-0149) reading A: `blockers(Long Sword) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0149](../rules/damage.md#m-0149) domain: one hit of source 'Long Sword'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0149](../rules/damage.md#m-0149)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0150"></a>

### M-0150: Damage source 'Zarok's Axe' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0150](../rules/damage.md#m-0150) `wiki-damage-015`: "| Zarok's Axe | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0150](../rules/damage.md#m-0150) reading A: `blockers(Zarok's Axe) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0150](../rules/damage.md#m-0150) domain: one hit of source 'Zarok's Axe'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0150](../rules/damage.md#m-0150)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0151"></a>

### M-0151: Damage source 'Huge Machete' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0151](../rules/damage.md#m-0151) `wiki-damage-016`: "| Huge Machete | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0151](../rules/damage.md#m-0151) reading A: `blockers(Huge Machete) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0151](../rules/damage.md#m-0151) domain: one hit of source 'Huge Machete'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0151](../rules/damage.md#m-0151)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0152"></a>

### M-0152: Damage source 'Deep Cut bleeding' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0152](../rules/damage.md#m-0152) `wiki-damage-017`: "| Deep Cut bleeding | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0152](../rules/damage.md#m-0152) reading A: `blockers(Deep Cut bleeding) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Body armor: absorbs}`
- [M-0152](../rules/damage.md#m-0152) domain: one hit of source 'Deep Cut bleeding'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0152](../rules/damage.md#m-0152)): Deep Cut bleeding (periodic).

<a id="m-0153"></a>

### M-0153: Damage source 'Drone' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0153](../rules/damage.md#m-0153) `wiki-damage-018`: "| Drone | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0153](../rules/damage.md#m-0153) reading A: `blockers(Drone) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0153](../rules/damage.md#m-0153) domain: one hit of source 'Drone'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0153](../rules/damage.md#m-0153)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0154"></a>

### M-0154: Damage source 'C4' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0154](../rules/damage.md#m-0154) `wiki-damage-019`: "| C4 | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0154](../rules/damage.md#m-0154) reading A: `blockers(C4) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0154](../rules/damage.md#m-0154) domain: one hit of source 'C4'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0154](../rules/damage.md#m-0154)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0155"></a>

### M-0155: Damage source 'Landmine' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0155](../rules/damage.md#m-0155) `wiki-damage-020`: "| Landmine | Shield, Safety bubble, Sleeping Bag, Protection, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0155](../rules/damage.md#m-0155) reading A: `blockers(Landmine) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0155](../rules/damage.md#m-0155) domain: one hit of source 'Landmine'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0155](../rules/damage.md#m-0155)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0156"></a>

### M-0156: Damage source 'Trapped gift' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0156](../rules/damage.md#m-0156) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0156](../rules/damage.md#m-0156) reading A: `blockers(Trapped gift) = {Shield: blocks; Sleeping Bag: blocks; Protection: blocks; Mirror forcefield: reflects}`
- [M-0156](../rules/damage.md#m-0156) domain: one hit of source 'Trapped gift'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

**Contradictions:** [C-0101](../unknowns.md#c-0101), [C-0102](../unknowns.md#c-0102)

Notes ([M-0156](../rules/damage.md#m-0156)): No Safety bubble and no Body armor listed: the items page says 'A trapped gift ignores it' (armor) and 'A trapped gift still hurts the holder' (bubble). See [C-0101](../unknowns.md#c-0101) and [C-0102](../unknowns.md#c-0102). Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0157"></a>

### M-0157: Damage source 'Fake chest' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0157](../rules/damage.md#m-0157) `wiki-damage-022`: "| Fake chest | Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0157](../rules/damage.md#m-0157) reading A: `blockers(Fake chest) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Mirror forcefield: reflects; Body armor: absorbs}`
- [M-0157](../rules/damage.md#m-0157) domain: one hit of source 'Fake chest'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0005](../unknowns.md#u-0005) (high): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)?

Notes ([M-0157](../rules/damage.md#m-0157)): Attacker Kick bonus applies to this source (step 2 list).

<a id="m-0158"></a>

### M-0158: Damage source 'Missile' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0158](../rules/damage.md#m-0158) `wiki-damage-023`: "| Missile | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0158](../rules/damage.md#m-0158) reading A: `blockers(Missile) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Flak jacket: blocks; Body armor: absorbs}`
- [M-0158](../rules/damage.md#m-0158) domain: one hit of source 'Missile'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0159"></a>

### M-0159: Damage source 'Nuke' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0159](../rules/damage.md#m-0159) `wiki-damage-024`: "| Nuke | Shield, Safety bubble, Sleeping Bag, Flak jacket, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0159](../rules/damage.md#m-0159) reading A: `blockers(Nuke) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Flak jacket: blocks; Body armor: absorbs}`
- [M-0159](../rules/damage.md#m-0159) domain: one hit of source 'Nuke'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0160"></a>

### M-0160: Damage source 'Airstrike impact' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0160](../rules/damage.md#m-0160) `wiki-damage-025`: "| Airstrike impact | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0160](../rules/damage.md#m-0160) reading A: `blockers(Airstrike impact) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Flak jacket: blocks; Body armor: absorbs}`
- [M-0160](../rules/damage.md#m-0160) domain: one hit of source 'Airstrike impact'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0161"></a>

### M-0161: Damage source 'Airstrike fire' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0161](../rules/damage.md#m-0161) `wiki-damage-026`: "| Airstrike fire | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0161](../rules/damage.md#m-0161) reading A: `blockers(Airstrike fire) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Body armor: absorbs}`
- [M-0161](../rules/damage.md#m-0161) domain: one hit of source 'Airstrike fire'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0162"></a>

### M-0162: Damage source 'Gunship bomb' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0162](../rules/damage.md#m-0162) `wiki-damage-027`: "| Gunship bomb | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0162](../rules/damage.md#m-0162) reading A: `blockers(Gunship bomb) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Flak jacket: blocks; Body armor: absorbs}`
- [M-0162](../rules/damage.md#m-0162) domain: one hit of source 'Gunship bomb'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0163"></a>

### M-0163: Damage source 'Giant cyclops attack' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0163](../rules/damage.md#m-0163) `wiki-damage-028`: "| Giant cyclops attack | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0163](../rules/damage.md#m-0163) reading A: `blockers(Giant cyclops attack) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Body armor: absorbs}`
- [M-0163](../rules/damage.md#m-0163) domain: one hit of source 'Giant cyclops attack'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0164"></a>

### M-0164: Damage source 'Bounty mark' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0164](../rules/damage.md#m-0164) `wiki-damage-029`: "| Bounty mark | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0164](../rules/damage.md#m-0164) reading A: `blockers(Bounty mark) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Body armor: absorbs}`
- [M-0164](../rules/damage.md#m-0164) domain: one hit of source 'Bounty mark'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0165"></a>

### M-0165: Damage source 'Eddie's Potion backfire' and what stops it

Label: `CONDITIONAL`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0165](../rules/damage.md#m-0165) `wiki-damage-030`: "| Eddie's Potion backfire | Shield, Safety bubble, Sleeping Bag, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0165](../rules/damage.md#m-0165) reading A: `blockers(Eddie's Potion backfire) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Body armor: absorbs}`
- [M-0165](../rules/damage.md#m-0165) domain: one hit of source 'Eddie's Potion backfire'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

**Open questions:**

- [U-0004](../unknowns.md#u-0004) (high): Can Eddie's potion 30% loss kill, and do armor, fortress or Kick status apply to it?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0165](../rules/damage.md#m-0165)): Matches seed [U-0004](../unknowns.md#u-0004) note: Shield, Safety bubble, Sleeping Bag and Body armor stop it, which supports reading B for blocking.

<a id="m-0166"></a>

### M-0166: Damage source 'Protection retribution' and what stops it

Label: `DOCUMENTED`. Sigils: all.

**Official text** (snapshot 2026-11-11):

- [M-0166](../rules/damage.md#m-0166) `wiki-damage-031`: "| Protection retribution | Shield, Safety bubble, Sleeping Bag, Protection, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0166](../rules/damage.md#m-0166) reading A: `blockers(Protection retribution) = {Shield: blocks; Safety bubble: blocks; Sleeping Bag: blocks; Protection: blocks; Body armor: absorbs}`
- [M-0166](../rules/damage.md#m-0166) domain: one hit of source 'Protection retribution'

**Interactions:** [M-0118](../rules/damage.md#m-0118)

<a id="m-0524"></a>

### M-0524: Robot damage blockers

Label: `UNKNOWN`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0524](../rules/damage.md#m-0524) `wiki-sigils-ingenuity-016`: "Shields and Sleeping Bags stop it." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
- [M-0524](../rules/damage.md#m-0524) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [M-0524](../rules/damage.md#m-0524) `wiki-damage-007`: "Robot | Safety bubble, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0524](../rules/damage.md#m-0524) reading A: `robot damage is stopped by Shield and Sleeping Bag (Ingenuity page)`
- [M-0524](../rules/damage.md#m-0524) reading B: `robot damage is not stopped by Shield or by a Sleeping Bag (damage page); stopped by Safety bubble, slowed by Hazmat suit, absorbed by Body armor`
- [M-0524](../rules/damage.md#m-0524) domain: boolean block per defender state
- [M-0524](../rules/damage.md#m-0524) parameter `shield_blocks`: contradicted, see [C-0500](../unknowns.md#c-0500)
- [M-0524](../rules/damage.md#m-0524) parameter `sleeping_bag_blocks`: contradicted, see [C-0500](../unknowns.md#c-0500)

**Interactions:** [M-0523](../rules/weapons.md#m-0523)

**Contradictions:** [C-0500](../unknowns.md#c-0500)

Notes ([M-0524](../rules/damage.md#m-0524)): Contradiction [C-0500](../unknowns.md#c-0500). The damage page also lists robot damage as an exception to the sleeping-bag immunity.

<a id="m-0529"></a>

### M-0529: Fortress craft

Label: `CONDITIONAL`. Sigils: ingenuity.

**Official text** (snapshot 2026-11-11):

- [M-0529](../rules/damage.md#m-0529) `wiki-sigils-ingenuity-030`: "Protects everyone within 20m (66ft) of it for up to 30 HP, and from Sigil of Greed stealing, and zone damage." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-fortress))
- [M-0529](../rules/damage.md#m-0529) `wiki-damage-052`: "A fortress you stand within absorbs up to its remaining durability, whoever built it." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

**Formal model:**

- [M-0529](../rules/damage.md#m-0529) reading A: `fortress at x: every contestant within 20 m of x is protected; durability D = 30 shared; hit step 6 absorbs min(d, D) and D -= absorbed; also blocks Greed stealing; zone damage fully immunized`
- [M-0529](../rules/damage.md#m-0529) reading B: `30 HP of absorption for each protected contestant`
- [M-0529](../rules/damage.md#m-0529) reading C: `zone damage is absorbed from the durability`
- [M-0529](../rules/damage.md#m-0529) domain: dist in metres 0..20; D integer 0..30
- [M-0529](../rules/damage.md#m-0529) parameter `radius_m`: 20
- [M-0529](../rules/damage.md#m-0529) parameter `durability_hp`: 30
- [M-0529](../rules/damage.md#m-0529) parameter `duration_s`: UNKNOWN, see [U-0526](../unknowns.md#u-0526)

**Interactions:** [M-0511](../rules/sigil.md#m-0511), [M-0522](../rules/items.md#m-0522)

**Open questions:**

- [U-0524](../unknowns.md#u-0524) (high): Fortress 'up to 30 HP': one pool shared by everyone inside 20 m, or 30 HP for each person?
- [U-0525](../unknowns.md#u-0525) (high): Fortress and zone damage: is zone damage absorbed from the 30 HP durability or ignored entirely?
- [U-0526](../unknowns.md#u-0526) (high): Fortress lifetime and position: how long does it stay, and is it fixed where it is placed?

Notes ([M-0529](../rules/damage.md#m-0529)): Damage page: 'A fortress you stand within absorbs up to its remaining durability, whoever built it' (step 6, before Armor). The Ingenuity text lists three protections: HP absorption, Greed stealing and zone damage.

<a id="m-0533"></a>

### M-0533: Fake chest claim effect

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-009`: "A contestant who claims it takes 5 HP damage and cannot claim chests for 1h." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-010`: "You heal 5 HP." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0533](../rules/damage.md#m-0533) `wiki-sigils-trolling-012`: "A Shield blocks the damage but not the lockout." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0533](../rules/damage.md#m-0533) `wiki-items-056`: "A reflected fake chest also locks the troll out of chests instead of you." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))

**Formal model:**

- [M-0533](../rules/damage.md#m-0533) reading A: `claim(fake chest by contestant v): v takes 5 HP through the hit pipeline (Kick bonus applies to the troll's hit, reductions apply to v); v cannot claim chests for 3600 s; the troll heals 5 HP; a Shield blocks the damage but not the lockout`
- [M-0533](../rules/damage.md#m-0533) reading B: `troll heals only when damage is not blocked`
- [M-0533](../rules/damage.md#m-0533) reading C: `lockout covers care packages and crates too`
- [M-0533](../rules/damage.md#m-0533) domain: damage integer 5 before modifiers; lockout 3600 s
- [M-0533](../rules/damage.md#m-0533) parameter `damage_hp`: 5
- [M-0533](../rules/damage.md#m-0533) parameter `lockout_s`: 3600
- [M-0533](../rules/damage.md#m-0533) parameter `troll_heal_hp`: 5
- [M-0533](../rules/damage.md#m-0533) parameter `lockout_scope`: UNKNOWN, see [U-0531](../unknowns.md#u-0531)
- [M-0533](../rules/damage.md#m-0533) parameter `heal_condition`: UNKNOWN, see [U-0532](../unknowns.md#u-0532)

**Interactions:** [M-0504](../rules/items.md#m-0504), [M-0531](../rules/economy.md#m-0531), [M-0532](../rules/items.md#m-0532)

**Open questions:**

- [U-0531](../unknowns.md#u-0531) (medium): Fake chest lockout 'cannot claim chests for 1h': does it block care packages and crates too, does a second claim extend it, and do blockers other than a Shield (Safety bubble, Sleeping Bag, Body armor) also leave it standing?
- [U-0532](../unknowns.md#u-0532) (medium): Trolling fake chest 'You heal 5 HP': fixed 5 HP at claim time, or the damage that actually landed, and does it happen when the victim is protected or the chest is reflected?
- [U-0001](../unknowns.md#u-0001) (critical): Does the defender's Kick-live 10% reduction floor the result (A) or the removed 10% (B)?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0533](../rules/damage.md#m-0533)): Damage page row: fake chest is stopped by Shield, Safety bubble, Sleeping Bag, Mirror forcefield (reflects) and Body armor (absorbs); the Kick bonus list includes the fake chest. Protection contestants still take fake chest damage. With a Mirror forcefield the whole effect returns to the troll including the lockout (items page).

<a id="m-0536"></a>

### M-0536: Unsafe circle damage

Label: `CONDITIONAL`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-017`: "Anyone inside it who is also inside a safe zone takes zone damage with no grace period" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-022`: "It hurts like the outside of the safe zone: 1 HP every 2s, first hit one interval after you enter, with no grace period." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0536](../rules/damage.md#m-0536) `wiki-sigils-trolling-023`: "Only the part inside a safe zone hurts: outside every safe zone you take normal zone damage only." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))

**Formal model:**

- [M-0536](../rules/damage.md#m-0536) reading A: `for contestant v in circle and in a safe zone: after 2 s inside, 1 HP every 2 s; no 5 s grace; outside every safe zone only normal zone damage (first tick after the ordinary grace)`
- [M-0536](../rules/damage.md#m-0536) reading B: `timer persists across moving between the inside-zone and outside-zone parts`
- [M-0536](../rules/damage.md#m-0536) reading C: `global 2 s ticks`
- [M-0536](../rules/damage.md#m-0536) domain: t >= 0 s since entry; 1 HP per tick
- [M-0536](../rules/damage.md#m-0536) parameter `interval_s`: 2
- [M-0536](../rules/damage.md#m-0536) parameter `damage_hp`: 1
- [M-0536](../rules/damage.md#m-0536) parameter `grace_s`: 0
- [M-0536](../rules/damage.md#m-0536) parameter `first_hit`: one interval after entry

**Interactions:** [M-0537](../rules/items.md#m-0537), [M-0538](../rules/damage.md#m-0538)

**Open questions:**

- [U-0537](../unknowns.md#u-0537) (high): Unsafe circle damage clock: is the first hit 2 s after each entry (timer resets on exit) or does a global 2 s phase continue? Does moving between the part of the circle inside a safe zone and the outside part reset it?
- [U-0003](../unknowns.md#u-0003) (medium): Zone damage: is the first tick at 5 s or at 7 s after leaving the safe zone?
- [U-0002](../unknowns.md#u-0002) (critical): Which damage sources go through the 7-step hit pipeline (zone ticks, poison, bleeding, zombie drain, guard zombies, robot, unsafe circle, Eddie's loss, the revive cost, Retribution)?

Notes ([M-0536](../rules/damage.md#m-0536)): Hazmat suit lengthens each zone damage interval by 2 s (items page) and the damage page lists it as slowing unsafe circle damage; Body armor absorbs. The ordinary zone damage first tick is [U-0003](../unknowns.md#u-0003).

<a id="m-0538"></a>

### M-0538: Unsafe circle blockers

Label: `UNKNOWN`. Sigils: trolling.

**Official text** (snapshot 2026-11-11):

- [M-0538](../rules/damage.md#m-0538) `wiki-sigils-trolling-027`: "A Guardian angel, a Safety bubble, a Reality Shield or a Death Ward blocks it." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0538](../rules/damage.md#m-0538) `wiki-sigils-trolling-028`: "A Shield does not." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [M-0538](../rules/damage.md#m-0538) `wiki-damage-006`: "Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

**Formal model:**

- [M-0538](../rules/damage.md#m-0538) reading A: `unsafe circle damage and item loss are blocked by Guardian angel, Safety bubble, Reality Shield or Death Ward (Trolling page); a Shield does not`
- [M-0538](../rules/damage.md#m-0538) reading B: `damage table row: blocked by Safety bubble, Guardian angel, Death Ward; Hazmat suit slows; Body armor absorbs; Reality Shield not in the row`
- [M-0538](../rules/damage.md#m-0538) domain: boolean block per defender state
- [M-0538](../rules/damage.md#m-0538) parameter `shield_blocks`: false
- [M-0538](../rules/damage.md#m-0538) parameter `reality_shield_blocks`: contradicted, see [C-0502](../unknowns.md#c-0502)

**Interactions:** [M-0536](../rules/damage.md#m-0536), [M-0537](../rules/items.md#m-0537)

**Contradictions:** [C-0502](../unknowns.md#c-0502)

Notes ([M-0538](../rules/damage.md#m-0538)): The Reality Shield is the only mismatch. The damage page notes (a different clause) also say a Safety bubble and a Reality Shield block zone, unsafe circle and robot damage, which supports reading A.

<a id="m-0643"></a>

### M-0643: Protection takes 50% less from nukes

Label: `DOCUMENTED`. Sigils: protection.

**Official text** (snapshot 2026-11-11):

- [M-0643](../rules/damage.md#m-0643) `wiki-sigils-protection-013`: "Nukes deal 50% less damage to you." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [M-0643](../rules/damage.md#m-0643) `wiki-damage-044`: "A Protection contestant takes 50% less from a nuke." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0643](../rules/damage.md#m-0643) `wiki-damage-045`: "The damage left is rounded down." ([source](https://iceposeidon.com/safezone/wiki/damage#order))
- [M-0643](../rules/damage.md#m-0643) `wiki-attacks-016`: "The Protection sigil is not immune, but takes 50% less." ([source](https://iceposeidon.com/safezone/wiki/attacks#nuke))

**Formal model:**

- [M-0643](../rules/damage.md#m-0643) reading A: `d -> floor(d/2) (reduction step 4, before the Kick live reduction)`
- [M-0643](../rules/damage.md#m-0643) domain: d integer

**Contradictions:** [C-0602](../unknowns.md#c-0602)

Notes ([M-0643](../rules/damage.md#m-0643)): Order against the Kick live reduction and the 1 HP minimum is given by the damage page (steps 4 and 5). Where the Kick 10% applies, see [U-0001](../unknowns.md#u-0001).

## Simulation check

Theorems with tests in `sim/tests/`: [T-0001](../theorems/T-0001.md), [T-0002](../theorems/T-0002.md), [T-0003](../theorems/T-0003.md), [T-0004](../theorems/T-0004.md), [T-0008](../theorems/T-0008.md)

## Open questions

[U-0001](../unknowns.md#u-0001), [U-0002](../unknowns.md#u-0002), [U-0003](../unknowns.md#u-0003), [U-0004](../unknowns.md#u-0004), [U-0005](../unknowns.md#u-0005), [U-0010](../unknowns.md#u-0010), [U-0100](../unknowns.md#u-0100), [U-0101](../unknowns.md#u-0101), [U-0102](../unknowns.md#u-0102), [U-0103](../unknowns.md#u-0103), [U-0117](../unknowns.md#u-0117), [U-0118](../unknowns.md#u-0118), [U-0119](../unknowns.md#u-0119), [U-0120](../unknowns.md#u-0120), [U-0121](../unknowns.md#u-0121), [U-0123](../unknowns.md#u-0123), [U-0524](../unknowns.md#u-0524), [U-0525](../unknowns.md#u-0525), [U-0526](../unknowns.md#u-0526), [U-0531](../unknowns.md#u-0531), [U-0532](../unknowns.md#u-0532), [U-0537](../unknowns.md#u-0537)

## Confidence

`UNKNOWN`: the lowest label among the rules on this page.
