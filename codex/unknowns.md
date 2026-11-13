# Open questions and contradictions

Everything the official wiki leaves undecided, as of the 2026-11-11 snapshot. Each question lists the competing readings and what would settle it. No model in this project picks a reading silently: every simulation is run under each reading that matters.

Open questions by priority: 5 critical, 72 high, 95 medium, 31 low (source: kb/unknowns/, 204 records).

## Priority: critical

### U-0000

[U-0000](unknowns.md#u-0000): What is the source and what are the exact conditions of the reported $5,000 viewer prize? Status: `open`.

Why it matters ([U-0000](unknowns.md#u-0000)): Sets the viewer's objective in the viewer-economics model (section 8.10); without it, viewer strategy can only maximize damage per Cx-Buck.

- [U-0000](unknowns.md#u-0000) reading A: No $5,000 prize exists; viewer prizes are the unquantified 'top 3 viewers' cash prizes.
- [U-0000](unknowns.md#u-0000) reading B: A $5,000 prize exists with conditions not yet found.
- [U-0000](unknowns.md#u-0000) resolution: Organizer post on X read directly (needs a logged-in browser session by kil).
- [U-0000](unknowns.md#u-0000) resolution: Organizer statement on stream (VOD timestamp).
- [U-0000](unknowns.md#u-0000) resolution: Pages /events or /safezone/recap, if kil adds them to SCOPE.md.

### U-0001

[U-0001](unknowns.md#u-0001): Does the defender's Kick-live 10% reduction floor the result (A) or the removed 10% (B)? Status: `open`.

Why it matters ([U-0001](unknowns.md#u-0001)): Changes every small hit by up to 1 HP: under A, hits of 2 to 10 lose 1 HP; under B, hits below 10 are unchanged.

- [U-0001](unknowns.md#u-0001) reading A: d -> floor(9d/10)
- [U-0001](unknowns.md#u-0001) reading B: d -> d - floor(d/10)
- [U-0001](unknowns.md#u-0001) resolution: VOD: a live contestant taking a 5 HP hit (bow, knife, fake chest) shows -4 (A) or -5 (B).
- [U-0001](unknowns.md#u-0001) resolution: REA: damage formula in shipped code (client code holds none, RE-0001).

### U-0002

[U-0002](unknowns.md#u-0002): For damage that is not a discrete attack (zone ticks, unsafe circle, robot, poison, tear gas, bleeding, zombie drain, Eddie's loss, Retribution), do pipeline steps 4b (the defender's Kick-live reduction), 5 (the 1 HP minimum) and 6 (fortress) apply? And are the guard zombie drain and the revive cost kinds of damage at all (neither has a row in the damage table)? Status: `open`.

Why it matters ([U-0002](unknowns.md#u-0002)): Blockers and Body armor no longer depend on this question (see the narrowing below). What is left changes the loss of a Kick-live contestant from Retribution (18 or 20 HP), from Eddie's potion (27 or 30 HP at 100 max HP) and from the 2 HP ticks of tear gas and guard zombies (1 or 2 HP, under [U-0001](unknowns.md#u-0001) reading A only), whether a fortress absorbs zone ticks, and whether the revive cost can be reduced or absorbed. A 1 HP tick stays 1 HP under readings A and B ([T-0002](theorems/T-0002.md), [T-0004](theorems/T-0004.md)).

- [U-0002](unknowns.md#u-0002) reading A: Every row of the damage table is a hit, so steps 4b, 5 and 6 apply to all of them.
- [U-0002](unknowns.md#u-0002) reading B: Steps 4b, 5 and 6 apply to discrete attacks only; periodic and self-inflicted damage gets steps 1 and 7 and nothing else.
- [U-0002](unknowns.md#u-0002) reading C: Mixed, source by source or step by step.
- [U-0002](unknowns.md#u-0002) resolution: VOD: a Protection contestant dies within 30m of a Kick-live contestant who has no armor and stands in no fortress: the victim loses 18 HP (step 4b applies) or 20 HP (it does not), under both readings of [U-0001](unknowns.md#u-0001).
- [U-0002](unknowns.md#u-0002) resolution: VOD: a Kick-live contestant with 100 max HP loses the gamble of Eddie's potion: 27 HP or 30 HP.
- [U-0002](unknowns.md#u-0002) resolution: VOD: a contestant stands in a fortress outside every safe zone: the durability of the fortress falls (step 6 applies) or the HP of the contestant does.
- [U-0002](unknowns.md#u-0002) resolution: VOD: a reviver who wears Body armor: the armor durability falls by 5 (the cost is damage) or the HP does.
- [U-0002](unknowns.md#u-0002) resolution: Not a test: a 1 HP tick (zone, poison, zombie drain) on a contestant without armor reads 1 HP under readings A and B ([T-0002](theorems/T-0002.md), [T-0004](theorems/T-0004.md)).
- [U-0002](unknowns.md#u-0002) narrowed: Narrowed on 2026-11-13 from the text of the 2026-11-11 snapshot, not resolved. Settled: (1) step 1 applies source by source: zone, unsafe circle, robot, poison, tear gas, zombie drain, bleeding, Eddie's backfire and Retribution each have a row of blockers in the damage table (wiki-damage-005 to wiki-damage-010, wiki-damage-017, wiki-damage-030, wiki-damage-031); (2) step 7 applies to all of them: each of those rows ends with "Body armor (absorbs)", which refutes the former reading B (periodic drains bypass the whole pipeline) for armor (wiki-damage-071 says "Body Armor works on every kind of damage", but that sentence is not general: "A trapped gift ignores it", wiki-items-027); (3) step 2 does not apply: the Kick bonus of the attacker is a closed list of weapons (wiki-damage-038) that holds none of these sources; (4) step 3 does not apply: a Mirror forcefield "only reflects" a closed list (wiki-damage-070) that holds none of them (Poison Darts are on that list, and the Poison row of the table has no Mirror forcefield, wiki-damage-008); (5) step 4a does not apply: the Protection cut is for a nuke only (wiki-damage-044). Still open: steps 4b, 5 and 6 for these sources, whether the guard zombie drain is a "Zombie drain", and the revive cost, which the text calls a cost.

### U-0009

[U-0009](unknowns.md#u-0009): Number of contestants and event duration for Miami. Status: `open`.

Why it matters ([U-0009](unknowns.md#u-0009)): Sets the horizon T, the Death sigil's '20% or fewer alive' threshold, and every last-survivor model.

- [U-0009](unknowns.md#u-0009) resolution: Organizer statement or live overview page during the event (SCOPE.md P2).

### U-0417

[U-0417](unknowns.md#u-0417): Bounty claim: 'The first other contestant to stay within 5m of them for 1min claims it'. Is the 60s continuous (reset when leaving range), cumulative, or does it tolerate short exits? Is the marked contestant's movement relevant, and are multiple hunters tracked separately? Status: `open`.

Why it matters ([U-0417](unknowns.md#u-0417)): Decides whether a bounty is claimable by chasing and the expected payout rate.

- [U-0417](unknowns.md#u-0417) reading A: a continuous 60s counter per hunter, reset on leaving range
- [U-0417](unknowns.md#u-0417) reading B: a cumulative 60s counter per hunter
- [U-0417](unknowns.md#u-0417) reading C: one shared counter reset when no other contestant is in range
- [U-0417](unknowns.md#u-0417) resolution: VOD of a bounty claim with a moving target.

## Priority: high

### U-0004

[U-0004](unknowns.md#u-0004): Can Eddie's potion 30% loss kill, and do armor, fortress or Kick status apply to it? Status: `open`.

Why it matters ([U-0004](unknowns.md#u-0004)): Decides whether the potion is a last resort or a suicide at low HP.

- [U-0004](unknowns.md#u-0004) reading A: Loss can kill, no protection applies.
- [U-0004](unknowns.md#u-0004) reading B: Loss can kill, pipeline applies (armor absorbs, Kick reduces).
- [U-0004](unknowns.md#u-0004) reading C: Loss cannot take HP below 1.
- [U-0004](unknowns.md#u-0004) resolution: VOD: a contestant at HP <= 30% of max drinking it.
- [U-0004](unknowns.md#u-0004) resolution: The damage table lists 'Eddie's Potion backfire' as stoppable by Shield, Safety bubble, Sleeping Bag and Body armor, which supports B for blocking (to be formalized).
- [U-0004](unknowns.md#u-0004) narrowed: Narrowed on 2026-11-13 from the text of the 2026-11-11 snapshot, not resolved. Reading A (no protection applies) is refuted: the damage table has a row "Eddie's Potion backfire" with Shield, Safety bubble and Sleeping Bag as blockers and "Body armor (absorbs)" (wiki-damage-030), and "Body Armor works on every kind of damage" (wiki-damage-071). Still open: whether the loss can kill or stops at 1 HP (readings B and C), and whether the Kick-live reduction and a fortress apply, which is the part of [U-0002](unknowns.md#u-0002) that is left.

### U-0005

[U-0005](unknowns.md#u-0005): Does a mirrored hit go through the attacker's own pipeline (immunity, reductions, armor)? Status: `open`.

Why it matters ([U-0005](unknowns.md#u-0005)): Changes the value of the Mirror forcefield against armored or live attackers.

- [U-0005](unknowns.md#u-0005) reading A: Reflected hit runs the attacker's full pipeline.
- [U-0005](unknowns.md#u-0005) reading B: Reflected hit lands raw.
- [U-0005](unknowns.md#u-0005) resolution: VOD: a reflected hit on an armored attacker.

### U-0006

[U-0006](unknowns.md#u-0006): Is server arithmetic exact or IEEE 754 binary64 (H-0001: Ingenuity prices at base 50, 90, 100, 110)? Status: `open`.

Why it matters ([U-0006](unknowns.md#u-0006)): binary64 ceil(p*1.1) charges 1 extra blood token at those base prices.

- [U-0006](unknowns.md#u-0006) reading A: exact integer arithmetic
- [U-0006](unknowns.md#u-0006) reading B: binary64 with ceil(p * 1.1)
- [U-0006](unknowns.md#u-0006) resolution: VOD: an Ingenuity contestant's merchant screen showing Dual Wield (base 50): 55 (A) or 56 (B).

### U-0008

[U-0008](unknowns.md#u-0008): Zombie 30 HP cap: per zombie lifetime, per encounter, or per day? What happens when a zombie dies? Status: `open`.

Why it matters ([U-0008](unknowns.md#u-0008)): Bounds total zombie damage; per-encounter would make zombies unbounded.

- [U-0008](unknowns.md#u-0008) reading A: per zombie lifetime, per contestant
- [U-0008](unknowns.md#u-0008) reading B: per encounter
- [U-0008](unknowns.md#u-0008) reading C: per time window
- [U-0008](unknowns.md#u-0008) resolution: VOD: one zombie re-engaging a contestant after leaving range.

### U-0014

[U-0014](unknowns.md#u-0014): What are the viewer attack prices in Cx-Bucks? Status: `open`.

Why it matters ([U-0014](unknowns.md#u-0014)): Without prices, section 8.10 can rank attacks by damage only, not by damage per Cx-Buck, and the crown-kill bonus (20% of the price) has no value.

- [U-0014](unknowns.md#u-0014) resolution: SCOPE.md P3 (api route 'purchasables', not called).
- [U-0014](unknowns.md#u-0014) resolution: VOD of the viewer shop.
- [U-0014](unknowns.md#u-0014) resolution: Shop page, out of scope today.

### U-0015

[U-0015](unknowns.md#u-0015): What are the chest rules (types, claim range, spawn rate, contents)? The chests page was removed (RE-0004). Status: `open`.

Why it matters ([U-0015](unknowns.md#u-0015)): Piety, Greed, Trolling and Ingenuity mechanics all act on chests; their value depends on chest frequency.

- [U-0015](unknowns.md#u-0015) resolution: Organizer statement; VOD observation of chest spawn rates.
- [U-0015](unknowns.md#u-0015) resolution: SCOPE.md P1 (search index may keep the removed text).

### U-0101

[U-0101](unknowns.md#u-0101): Body armor 'absorbs what is left, until it breaks': does a hit larger than the remaining durability pass the excess through (A), or is the whole hit absorbed and the armor simply breaks (B)? Does durability drop 1 per HP absorbed? Status: `open`.

Why it matters ([U-0101](unknowns.md#u-0101)): Decides whether armor durability is an HP pool (excess passes) or a number of hits; changes effective HP of every armored contestant.

- [U-0101](unknowns.md#u-0101) reading A: absorbed = min(h, dur); dur -= absorbed; excess h - absorbed reaches HP
- [U-0101](unknowns.md#u-0101) reading B: if h > 0 and dur > 0: absorbed = h (whole hit), dur -= h, floored at 0, armor breaks when dur reaches 0, excess lost
- [U-0101](unknowns.md#u-0101) reading C: armor loses 1 durability per hit regardless of size
- [U-0101](unknowns.md#u-0101) resolution: VOD: armored contestant (durability visible) taking a hit larger than the remaining durability.
- [U-0101](unknowns.md#u-0101) resolution: REA: shipped armor code.

### U-0103

[U-0103](unknowns.md#u-0103): 'A hit that gets through always does at least 1 HP' is step 5 of 7: can fortress (step 6) and armor (step 7) still reduce the final HP loss to 0? Status: `open`.

Why it matters ([U-0103](unknowns.md#u-0103)): If steps 6 and 7 may absorb everything, 'always at least 1 HP' only holds up to step 5; if the 1 HP floor is final, armor and fortress can never fully protect a contestant from a tiny hit.

- [U-0103](unknowns.md#u-0103) reading A: stated order: h5 = max(1, h4), then fortress and armor subtract, final HP loss can be 0
- [U-0103](unknowns.md#u-0103) reading B: final HP loss = max(1, h7): the floor is enforced at the end
- [U-0103](unknowns.md#u-0103) reading C: floor applies only to hits that arrive at step 5 non-zero and unabsorbed
- [U-0103](unknowns.md#u-0103) resolution: VOD: armored contestant taking a 1 HP source (zone tick, poison step, bow after reductions).
- [U-0103](unknowns.md#u-0103) resolution: REA: damage formula in shipped code.

### U-0104

[U-0104](unknowns.md#u-0104): 'A final kill pays 25 blood tokens, or 50 if the killer or victim held the blood crown': who is paid, what makes a kill 'final', and when is the payment made? Status: `open`.

Why it matters ([U-0104](unknowns.md#u-0104)): Blood-token income from kills is the main resource flow in combat; the recipient and timing decide whether revival undoes the payment.

- [U-0104](unknowns.md#u-0104) reading A: the killer is paid 25 (50 with crown) at the killing blow
- [U-0104](unknowns.md#u-0104) reading B: the killer is paid after the revival window ends without a revive (final = not revived)
- [U-0104](unknowns.md#u-0104) reading C: the killer is paid 25, and an additional 25 goes elsewhere if the crown is involved, so 50 is the total paid out
- [U-0104](unknowns.md#u-0104) resolution: VOD: blood token counter of a killer at the killing blow and 10 min later.
- [U-0104](unknowns.md#u-0104) resolution: Organizer statement.

### U-0107

[U-0107](unknowns.md#u-0107): Revival caps '2 times' (on a Healing contestant) and '10 times' (by a Healing contestant): what is the counter attached to? Status: `open`.

Why it matters ([U-0107](unknowns.md#u-0107)): Determines how many lives a Healing contestant has and how many revives a Healing reviver can perform over the whole event.

- [U-0107](unknowns.md#u-0107) reading A: 2 = total revives a given Healing contestant can ever receive (any reviver); 10 = total revives a given Healing contestant can ever perform
- [U-0107](unknowns.md#u-0107) reading B: 2 and 10 are per (reviver, target) pair
- [U-0107](unknowns.md#u-0107) reading C: 2 = per life of the target; 10 = per reviver per day or per hour
- [U-0107](unknowns.md#u-0107) reading D: when a Healing contestant revives another Healing contestant both limits apply and the lower (2) binds; or only 10 applies
- [U-0107](unknowns.md#u-0107) resolution: VOD: a Healing contestant revived a third time; a Healing reviver performing an eleventh revive.
- [U-0107](unknowns.md#u-0107) resolution: Organizer statement.

### U-0110

[U-0110](unknowns.md#u-0110): After the offline grace ends ('you start taking damage after 15min'), what damage applies: the outside-circle rule (5 s grace then 1 HP every 2 s), an immediate tick cadence, or something else? Status: `open`.

Why it matters ([U-0110](unknowns.md#u-0110)): Sets how fast a contestant with a dead phone loses HP and the time to death after the grace.

- [U-0110](unknowns.md#u-0110) reading A: same as outside the circle: 5 s grace, then 1 HP every 2 s
- [U-0110](unknowns.md#u-0110) reading B: 1 HP every 2 s starting at the grace end, no extra 5 s
- [U-0110](unknowns.md#u-0110) reading C: a different rate not given on this page
- [U-0110](unknowns.md#u-0110) free parameter `offline_damage_start_delay_s`, swept over 0 to 5 s: 0 if damage starts at the grace end, 5 if the outside-circle grace is re-applied
- [U-0110](unknowns.md#u-0110) resolution: VOD: a contestant with a dead phone after 15 min.
- [U-0110](unknowns.md#u-0110) resolution: REA: shipped GPS watchdog.

### U-0111

[U-0111](unknowns.md#u-0111): Offline grace timer semantics: is it measured from the last GPS update only, does a later GPS update reset it, and is 'live on Kick' evaluated at the moment the GPS stops (A), at the expiry (B), or continuously with fractional accrual (C)? Status: `open`.

Why it matters ([U-0111](unknowns.md#u-0111)): A stream drop or reconnect during an outage changes the grace between 15 and 30 min; ties to [U-0012](unknowns.md#u-0012) detection latency.

- [U-0111](unknowns.md#u-0111) reading A: grace = 30 min if live at the last GPS update, else 15 min, fixed at that moment
- [U-0111](unknowns.md#u-0111) reading B: live status is read at the end of 15 min: if live then, the deadline moves to 30 min
- [U-0111](unknowns.md#u-0111) reading C: elapsed offline time is accumulated at weight 1/15 or 1/30 per minute depending on live status at each instant
- [U-0111](unknowns.md#u-0111) resolution: VOD: phone off while live, stream ends at minute 10, damage start time.
- [U-0111](unknowns.md#u-0111) resolution: Organizer statement.

### U-0112

[U-0112](unknowns.md#u-0112): Speed rule averaging: is '20mph on average over 1min' a sliding window, a fixed window, or a ratio of distance to time; is '30mph over any 15s' the same average on a 15 s window or a peak speed; are comparisons strict; are 8.94 and 13.41 m/s the exact thresholds? Status: `open`.

Why it matters ([U-0112](unknowns.md#u-0112)): Decides who is classified as moving too fast on a vehicle ride or a GPS jump, and the exact trigger edge.

- [U-0112](unknowns.md#u-0112) reading A: sliding windows, mean speed = displacement path length / window length, strict >, thresholds 8.94 and 13.41 m/s as printed
- [U-0112](unknowns.md#u-0112) reading B: same but thresholds exact 8.9408 and 13.4112 m/s
- [U-0112](unknowns.md#u-0112) reading C: straight-line displacement endpoint to endpoint in the window, not path length
- [U-0112](unknowns.md#u-0112) reading D: the 15 s rule uses peak instantaneous speed
- [U-0112](unknowns.md#u-0112) resolution: VOD/GPS trace of a vehicle trip near the threshold.
- [U-0112](unknowns.md#u-0112) resolution: REA: shipped speed check.

### U-0114

[U-0114](unknowns.md#u-0114): The zone can 'split apart': with several safe zones, is 'leave a safezone' damage triggered when outside every zone (A) or when leaving the zone you were last in (B)? Status: `open`.

Why it matters ([U-0114](unknowns.md#u-0114)): Decides whether crossing between two zones is a loss, which is central when the zone splits.

- [U-0114](unknowns.md#u-0114) reading A: damage clock runs only when the position is inside no safe zone
- [U-0114](unknowns.md#u-0114) reading B: damage clock runs when leaving a zone, restarts if re-entering any zone
- [U-0114](unknowns.md#u-0114) reading C: damage clock is tied to one assigned zone per contestant
- [U-0114](unknowns.md#u-0114) resolution: VOD: a split event and a contestant crossing between the two.
- [U-0114](unknowns.md#u-0114) resolution: Organizer statement.
- [U-0114](unknowns.md#u-0114) narrowed: Narrowed on 2026-11-13 from the text of the 2026-11-11 snapshot, not resolved. Three clauses are consistent with reading A, without describing the clock: "Only the part inside a safe zone hurts: outside every safe zone you take normal zone damage only" (wiki-sigils-trolling-023), an unsafe circle hurts "Anyone inside it who is also inside a safe zone" (wiki-sigils-trolling-017), and of the giant cyclops, "Outside the safe zones it takes zone damage" (wiki-attacks-071). Against it, the base rule is written in the singular with the verb leave, which reads like B or C: "If you leave a safezone, after 5s you will start taking 1 HP damage every 2s" (wiki-005). The zone can "even split apart" (wiki-004), and no clause gives a rule for a split or assigns a contestant to one zone. Still open: a VOD of a split or an organizer statement.

### U-0116

[U-0116](unknowns.md#u-0116): Poison 'Getting poisoned again resets the timer, it doesn't stack': does the reset only restart the 90 s countdown, or also restore the total damage still to be dealt? What is the total? Status: `open`.

Why it matters ([U-0116](unknowns.md#u-0116)): Re-poisoning could be an indefinite extension (total restored) or a mere delay; and the page gives no total.

- [U-0116](unknowns.md#u-0116) reading A: countdown restarts, remaining damage unchanged
- [U-0116](unknowns.md#u-0116) reading B: countdown and remaining damage both restart to the full total
- [U-0116](unknowns.md#u-0116) reading C: countdown restarts and remaining damage is max(remaining, new total)
- [U-0116](unknowns.md#u-0116) free parameter `poison_total_hp`, swept over 1 to 40 HP: lower bound 1 tick, upper bound twice the largest total seen on any page (20 HP), sweep choice
- [U-0116](unknowns.md#u-0116) resolution: VOD: a contestant poisoned twice, HP lost versus time.
- [U-0116](unknowns.md#u-0116) resolution: Items/attacks pages give the total of one poison source; compare.

### U-0117

[U-0117](unknowns.md#u-0117): A Shield or Safety bubble 'blocks each poison step while it lasts': is a blocked step consumed (counts toward 'all its damage') or skipped (poison extended)? Does the countdown continue while protected? Status: `open`.

Why it matters ([U-0117](unknowns.md#u-0117)): Decides whether a temporary shield cancels poison or only pauses it.

- [U-0117](unknowns.md#u-0117) reading A: blocked step is consumed: remaining steps decrement, no HP lost
- [U-0117](unknowns.md#u-0117) reading B: blocked step is skipped: remaining steps unchanged, poison extends
- [U-0117](unknowns.md#u-0117) reading C: poison timer is paused while protected
- [U-0117](unknowns.md#u-0117) resolution: VOD: poisoned contestant entering and leaving a bubble.

### U-0120

[U-0120](unknowns.md#u-0120): When several blockers apply to one hit (Shield, Safety bubble, Flak jacket, Sleeping Bag, Reality Shield, Protection), which one is the 'blocker' and which items are consumed? The only stated rule is 'a hit already blocked by something else does not use [the Flak jacket] up'. Status: `open`.

Why it matters ([U-0120](unknowns.md#u-0120)): Decides whether stacking consumables wastes them and which defence to equip first.

- [U-0120](unknowns.md#u-0120) reading A: a fixed priority order exists; only the first applicable blocker is consumed
- [U-0120](unknowns.md#u-0120) reading B: all applicable blockers are consumed
- [U-0120](unknowns.md#u-0120) reading C: non-consumable blockers (immunities) take priority over consumables, consumables are consumed only if nothing else blocks
- [U-0120](unknowns.md#u-0120) resolution: VOD: a hit on a contestant holding a Flak jacket and a Shield.
- [U-0120](unknowns.md#u-0120) resolution: REA: shipped hit resolver.

### U-0125

[U-0125](unknowns.md#u-0125): Blood crown: who 'held' it at the time of a kill (before the kill, or after transfer by that same kill), and how is it obtained/lost? Status: `open`.

Why it matters ([U-0125](unknowns.md#u-0125)): The 25 versus 50 token payout depends on it, and the crown rules are not on the pages in this clause set.

- [U-0125](unknowns.md#u-0125) reading A: holder status read before the kill resolves
- [U-0125](unknowns.md#u-0125) reading B: holder status read after crown transfer resolves
- [U-0125](unknowns.md#u-0125) resolution: Organizer statement; page that documents the crown (cross-family).

### U-0205

[U-0205](unknowns.md#u-0205): Hazmat suit '+2s per interval': which damage sources and which timings (first tick, grace) does it lengthen? Status: `open`.

Why it matters ([U-0205](unknowns.md#u-0205)): Changes time to death outside the zone and the value of the suit against unsafe circle and robots.

- [U-0205](unknowns.md#u-0205) reading A: only outside-zone interval, 2s -> 4s, first tick unchanged
- [U-0205](unknowns.md#u-0205) reading B: interval 4s and first tick delayed by 2s
- [U-0205](unknowns.md#u-0205) reading C: also unsafe circle and robot intervals, which the damage page marks 'slows'
- [U-0205](unknowns.md#u-0205) free parameter `hazmat_added_interval_s`, swept over 0..4 s (page says 2; bound 4 covers a doubling reading)
- [U-0205](unknowns.md#u-0205) resolution: VOD: a Hazmat carrier leaving the zone with an on-screen timer.
- [U-0205](unknowns.md#u-0205) resolution: Robot interval is not on the Items page.
- [U-0205](unknowns.md#u-0205) narrowed: Narrowed on 2026-11-13 from the text of the 2026-11-11 snapshot, not resolved. Sources settled: the damage table marks "Hazmat suit (slows)" on exactly three rows, Outside the circle, Unsafe circle and Robot (wiki-damage-005, wiki-damage-006, wiki-damage-007), so reading A (outside-zone damage only) is refuted for the list of sources. The amount is written for zone damage only: "While you carry it, each zone damage interval is 2s longer" (wiki-items-013); an unsafe circle deals zone damage (wiki-sigils-trolling-017), the robot interval is on no page. Still open: the first tick and the 5 s delay (with [U-0003](unknowns.md#u-0003)), and how much a robot is slowed.

### U-0207

[U-0207](unknowns.md#u-0207): What counts as 'attacks you' for ending a Guardian angel? Status: `open`.

Why it matters ([U-0207](unknowns.md#u-0207)): Decides whether traps, poison, area effects, drones or thefts end the immunity.

- [U-0207](unknowns.md#u-0207) reading A: any attack action by another contestant targeting you, blocked or not
- [U-0207](unknowns.md#u-0207) reading B: also non-damage hostile actions and traps
- [U-0207](unknowns.md#u-0207) reading C: only attacks that would damage you
- [U-0207](unknowns.md#u-0207) resolution: VOD: a Guardian angel holder hit by a trap, a thrown dart or a steal.

### U-0209

[U-0209](unknowns.md#u-0209): Is the 15 HP of Body armor a depleting pool or a per-hit cap, and how is a partly absorbed hit handled? Status: `open`.

Why it matters ([U-0209](unknowns.md#u-0209)): Changes survivability against repeated small hits (zone ticks, poison).

- [U-0209](unknowns.md#u-0209) reading A: depleting pool of 15 HP, partial absorption of the last hit
- [U-0209](unknowns.md#u-0209) reading B: per-hit cap 15 HP, never depleted
- [U-0209](unknowns.md#u-0209) resolution: VOD: armor durability after repeated hits.
- [U-0209](unknowns.md#u-0209) resolution: Damage page: 'absorbs what is left, until it breaks' favors A.
- [U-0209](unknowns.md#u-0209) narrowed: Narrowed on 2026-11-13 from the text of the 2026-11-11 snapshot, not resolved. Reading B is refuted: the armor "absorbs what is left, until it breaks" (wiki-damage-055), and it has a durability that changes: "+10 durability, up to 45" (wiki-merchant-057), then it "loses one durability every twenty minutes, down to 15" (wiki-merchant-058). An armor that is never used up cannot break. Still open, and the same question as [U-0101](unknowns.md#u-0101): what one hit takes from the durability (the HP absorbed, the whole hit, or 1 per hit), so whether "Absorbs up to 15 HP of damage" (wiki-items-026) is a pool counted in HP.

### U-0305

[U-0305](unknowns.md#u-0305): Drone: after use, is the target fixed at launch and hit 30s later regardless of what happens, or does the drone need the target to stay visible or alive? Status: `open`.

Why it matters ([U-0305](unknowns.md#u-0305)): Decides whether a drone can be dodged (shield, bubble, sleep, distance, Greed theft of the drone) during the 30s delay.

- [U-0305](unknowns.md#u-0305) reading A: target fixed at launch, hit applied 30s later whatever happens to visibility
- [U-0305](unknowns.md#u-0305) reading B: hit applied only if the target is still visible at t+30s
- [U-0305](unknowns.md#u-0305) reading C: hit follows the target and is checked against defenses at t+30s only
- [U-0305](unknowns.md#u-0305) resolution: VOD: drone launch, then target hides or gets a Shield during the 30s.

### U-0307

[U-0307](unknowns.md#u-0307): Cooldown semantics (bow 5s, knife 5s, machete 5s, long sword 10s, staff 20min): does it start at the attempt or at the hit, and is it per weapon item or per contestant (Dual Wield)? Status: `open`.

Why it matters ([U-0307](unknowns.md#u-0307)): With Dual Wield and a second weapon, per-contestant cooldown halves throughput relative to per-weapon cooldown; it also matters for blocked or missed attacks.

- [U-0307](unknowns.md#u-0307) reading A: per weapon item, starts at the attack
- [U-0307](unknowns.md#u-0307) reading B: per contestant (shared by all weapons), starts at the attack
- [U-0307](unknowns.md#u-0307) reading C: per weapon item, starts when the hit resolves
- [U-0307](unknowns.md#u-0307) resolution: VOD: Dual Wield contestant alternating two weapons within the cooldown.

### U-0308

[U-0308](unknowns.md#u-0308): Is a use (weapon use, arrow, Deep Cut charge, enchanted use) consumed by an attack that is blocked, reflected, out of range or missing? Status: `open`.

Why it matters ([U-0308](unknowns.md#u-0308)): Decides whether Shields, Safety Bubbles, Mirror and Sleeping Bags waste an attacker's limited uses (knife 2, long sword 3) and charges.

- [U-0308](unknowns.md#u-0308) reading A: consumed on every attempt
- [U-0308](unknowns.md#u-0308) reading B: consumed only when the hit lands
- [U-0308](unknowns.md#u-0308) reading C: consumed unless the hit is blocked by a defense item
- [U-0308](unknowns.md#u-0308) resolution: VOD: knife stab at a Shielded contestant, then count the knife uses left.

### U-0309

[U-0309](unknowns.md#u-0309): What is the range of 'nearby' for the Poison Dart, Zarok's axe and Huge machete? Status: `open`.

Why it matters ([U-0309](unknowns.md#u-0309)): Other melee weapons state 10m (knife, long sword); these three give no number, so reach and positioning cannot be modelled.

- [U-0309](unknowns.md#u-0309) free parameter `nearby_range_m`, swept over 5 to 50 m: the knife and long sword reach 10m, the bow 20m and the staff placement 50m, so a melee 'nearby' is bounded by 5 and 50
- [U-0309](unknowns.md#u-0309) resolution: Organizer statement.
- [U-0309](unknowns.md#u-0309) resolution: VOD: measured distance of a successful axe or machete hit.

### U-0310

[U-0310](unknowns.md#u-0310): Zarok's axe: how does damage go from 5 HP at full health to 25 HP as the wielder's health drops (linear, stepwise, relative to max HP, where is 25 reached)? Status: `open`.

Why it matters ([U-0310](unknowns.md#u-0310)): The axe's whole value depends on the curve: it fixes the damage at every HP level and whether 25 HP is reachable at all.

- [U-0310](unknowns.md#u-0310) reading A: linear in the wielder's missing fraction of max HP: 5 + 20*(1 - h/H), H = current max HP, 25 reached at h = 0
- [U-0310](unknowns.md#u-0310) reading B: linear in missing fraction with 25 reached at h = 1 (lowest living HP)
- [U-0310](unknowns.md#u-0310) reading C: linear in absolute HP against a fixed 100 HP scale: 5 + 20*(100 - h)/100, clamped to [5, 25]
- [U-0310](unknowns.md#u-0310) reading D: stepwise in tiers of the wielder's HP (tier boundaries not stated)
- [U-0310](unknowns.md#u-0310) resolution: VOD: axe hits at several wielder HP values (full, half, low).
- [U-0310](unknowns.md#u-0310) resolution: REA: weapon damage formula if shipped.

### U-0320

[U-0320](unknowns.md#u-0320): Merchant return delay: is 'after 30min to 1h' measured from the departure or from the arrival, and what is its distribution within the range? Status: `open`.

Why it matters ([U-0320](unknowns.md#u-0320)): Sets how long contestants must save blood tokens between visits (away 30 to 60 min versus 15 to 45 min) and the long-run share of time the merchant is present.

- [U-0320](unknowns.md#u-0320) reading A: uniform over [30, 60] min from the departure
- [U-0320](unknowns.md#u-0320) reading B: uniform over [30, 60] min from the arrival (away 15 to 45 min)
- [U-0320](unknowns.md#u-0320) reading C: fixed or non-uniform inside [30, 60] min from the departure
- [U-0320](unknowns.md#u-0320) free parameter `merchant_return_delay_min`, swept over 30 to 60 min as stated, reading A or B; sweep distribution shape (uniform, endpoints only)
- [U-0320](unknowns.md#u-0320) resolution: VOD: timestamps of merchant departure and next arrival over several cycles.

### U-0322

[U-0322](unknowns.md#u-0322): How does Ingenuity's 'pay 10% more, rounded up' apply to the 40 + 10k upgrade ladders? Status: `open`.

Why it matters ([U-0322](unknowns.md#u-0322)): Applying it to each current price, to the start price only, or to the step changes the whole ladder and the total cost to buy N upgrades.

- [U-0322](unknowns.md#u-0322) reading A: each price p becomes ceil(1.1*p): 44, 55, 66, ...
- [U-0322](unknowns.md#u-0322) reading B: only the start price is raised: 44, 54, 64, ...
- [U-0322](unknowns.md#u-0322) resolution: VOD: Ingenuity contestant's merchant screen for the first three slot upgrades.

### U-0325

[U-0325](unknowns.md#u-0325): Sleeping Bag: what are the 'sleep from 18:00 to 06:00 ... for eight hours of sleep in total' rules? Status: `open`.

Why it matters ([U-0325](unknowns.md#u-0325)): Twelve hours of window against eight hours of sleep: the wiki does not say whether the 8h is a continuous block, a total budget or a cap on one night.

- [U-0325](unknowns.md#u-0325) reading A: sleeping is allowed only between 18:00 and 06:00; total sleep time is capped at 8h and may be split
- [U-0325](unknowns.md#u-0325) reading B: one continuous 8h block that must lie inside the window
- [U-0325](unknowns.md#u-0325) reading C: the bag holds a total of 8h of sleep across the whole event
- [U-0325](unknowns.md#u-0325) free parameter `sleep_total_h`, swept over 8 as stated; test splits of the budget
- [U-0325](unknowns.md#u-0325) resolution: VOD: a contestant sleeping through the window.
- [U-0325](unknowns.md#u-0325) resolution: Organizer statement.

### U-0327

[U-0327](unknowns.md#u-0327): Sleeping Bag: is the 65 s of sleep continuous, what happens when the sleeper leaves the 15m radius, wakes up or is hit, and does waking end the immunity at once? Status: `open`.

Why it matters ([U-0327](unknowns.md#u-0327)): The first 65 s are the exposed window; leaving range or waking decides whether the counter resets, and the flashbang and damage immunity depend on it.

- [U-0327](unknowns.md#u-0327) reading A: 65 s must be continuous; leaving 15m or waking resets it and ends the immunity
- [U-0327](unknowns.md#u-0327) reading B: 65 s are cumulative over the night
- [U-0327](unknowns.md#u-0327) reading C: once reached, immunity lasts until the sleeper wakes, even outside 15m
- [U-0327](unknowns.md#u-0327) resolution: VOD: sleeper leaving the bag's range; a hit at second 30 of sleep.

### U-0328

[U-0328](unknowns.md#u-0328): Sleeping Bag: when does the 20-minute 'cannot sleep again' lockout start (the moment the bag first protects, when you wake, or at the last blocked damage)? Status: `open`.

Why it matters ([U-0328](unknowns.md#u-0328)): Changes how long a contestant can sleep: if the lockout starts when protection begins at the 65 s mark, an 8h sleeper is locked out long before they wake.

- [U-0328](unknowns.md#u-0328) reading A: starts when the bag starts protecting (after 65 s of sleep)
- [U-0328](unknowns.md#u-0328) reading B: starts when the sleeper wakes
- [U-0328](unknowns.md#u-0328) reading C: starts at the last damage the bag blocked
- [U-0328](unknowns.md#u-0328) resolution: VOD: a sleeper waking and trying to sleep again.

### U-0329

[U-0329](unknowns.md#u-0329): Are the 'for each one you already bought' counters of Inventory slot and +10 maximum HP separate, or shared? Status: `open`.

Why it matters ([U-0329](unknowns.md#u-0329)): Buying 10 slots and 10 HP upgrades costs very different amounts under a shared count (the second type would start where the first stopped).

- [U-0329](unknowns.md#u-0329) reading A: separate counters: each ladder is 40 + 10k with k its own purchases
- [U-0329](unknowns.md#u-0329) reading B: one shared counter over both upgrades
- [U-0329](unknowns.md#u-0329) resolution: VOD: merchant screen after one slot upgrade (HP price 40 or 50?).

### U-0333

[U-0333](unknowns.md#u-0333): Weapon enchantment 'Twice the uses ... keeps the uses it had before or the uses it has left, whichever is lower': twice what, and what is 'the uses it had before'? Status: `open`.

Why it matters ([U-0333](unknowns.md#u-0333)): Fixes the use count after the enchant and what a weapon with few uses left keeps after two hours.

- [U-0333](unknowns.md#u-0333) reading A: uses become 2 * (uses left when enchanted); 'before' = uses left when enchanted
- [U-0333](unknowns.md#u-0333) reading B: uses become 2 * (maximum uses of the weapon); 'before' = uses left when enchanted
- [U-0333](unknowns.md#u-0333) reading C: uses become uses left + maximum uses; 'before' = maximum uses
- [U-0333](unknowns.md#u-0333) resolution: VOD: enchanting a half-used knife and checking uses.

### U-0340

[U-0340](unknowns.md#u-0340): What damage and radius does the merchant 'standard missile' have, given it lands at an exact location after 30 s? Status: `open`.

Why it matters ([U-0340](unknowns.md#u-0340)): The attacks page describes a viewer missile with a 3min random landing; the merchant text names a 'standard missile' but gives no damage or radius.

- [U-0340](unknowns.md#u-0340) reading A: same damage and blast radius as the viewer missile (10 HP within 25 m per the attacks page)
- [U-0340](unknowns.md#u-0340) reading B: a different, unstated damage
- [U-0340](unknowns.md#u-0340) free parameter `merchant_missile_damage_hp`, swept over 10 to 20 HP: the viewer missile does 10 and the nuke does 20 on the attacks page
- [U-0340](unknowns.md#u-0340) resolution: VOD: merchant missile impact HP loss and radius.

### U-0400

[U-0400](unknowns.md#u-0400): Missile landing spread: 'a random spot near that point' with the whole blast within 100m. Is the landing offset at most 75m (blast edge within 100m) or at most 100m, and what is the distribution? Status: `open`.

Why it matters ([U-0400](unknowns.md#u-0400)): Decides hit probability on a contestant standing at the aim point, and whether a viewer can reliably target one contestant.

- [U-0400](unknowns.md#u-0400) reading A: landing offset r <= 100 - 25 = 75m, so the 25m blast stays within 100m
- [U-0400](unknowns.md#u-0400) reading B: landing offset r <= 100m (blast centre), the sentence meaning 'near'
- [U-0400](unknowns.md#u-0400) reading C: uniform over the disc of that radius
- [U-0400](unknowns.md#u-0400) reading D: uniform in distance r, random angle (centre-weighted)
- [U-0400](unknowns.md#u-0400) free parameter `missile_max_offset_m`, swept over 0 to 100 m; the wiki bounds the blast at 100m of the aim point, so the centre offset lies between 0 and 100
- [U-0400](unknowns.md#u-0400) resolution: VOD: record aim point versus crater for several missiles.
- [U-0400](unknowns.md#u-0400) resolution: Admin or organizer statement.

### U-0403

[U-0403](unknowns.md#u-0403): Zombie lifetime: the Horde lasts 20min and guard zombies 1h (Necromancy page), but what is the lifetime of Summon, Death and Horde-bonus zombies, and of horde zombies counted from release? Status: `open`.

Why it matters ([U-0403](unknowns.md#u-0403)): 'A zombie disappears when its time runs out' with no stated time makes total zombie pressure and Necromancy income unbounded or bounded.

- [U-0403](unknowns.md#u-0403) reading A: each zombie lives 20min from its own spawn, whatever its source
- [U-0403](unknowns.md#u-0403) reading B: only horde zombies expire at 20min; Summon, Death and bonus zombies live to the end of the event
- [U-0403](unknowns.md#u-0403) reading C: each source has its own undisclosed time
- [U-0403](unknowns.md#u-0403) free parameter `zombie_lifetime_s`, swept over 60 to 86400 s; 20min is the only stated zombie timer, the day bound is the event scale
- [U-0403](unknowns.md#u-0403) resolution: VOD: follow a Summon zombie until it vanishes.

### U-0404

[U-0404](unknowns.md#u-0404): Tear gas geometry: '25m cloud' is a radius or a diameter, and the cloud edge must be at least 20m from every contestant: at purchase time only, or also at placement? Must the whole cloud be inside the safe zone? Status: `open`.

Why it matters ([U-0404](unknowns.md#u-0404)): Sets the minimum aim distance to the nearest contestant (45m or 32.5m from the centre) and whether viewers can gas a contestant at all.

- [U-0404](unknowns.md#u-0404) reading A: radius 25m, so the centre is at least 45m from every contestant
- [U-0404](unknowns.md#u-0404) reading B: diameter 25m (radius 12.5m), so the centre is at least 32.5m from every contestant
- [U-0404](unknowns.md#u-0404) reading C: the 20m rule is only a placement check; later movement into the cloud is free
- [U-0404](unknowns.md#u-0404) free parameter `tear_gas_radius_m`, swept over 12.5 to 25 m; the wiki gives '25m' as the only size
- [U-0404](unknowns.md#u-0404) resolution: VOD: place tear gas near contestants and note the refusal threshold.

### U-0406

[U-0406](unknowns.md#u-0406): Airstrike strip width (the wiki gives centre and direction only). Status: `open`.

Why it matters ([U-0406](unknowns.md#u-0406)): Hit probability of the 5 HP strike and of the 5min fire.

- [U-0406](unknowns.md#u-0406) free parameter `airstrike_strip_width_m`, swept over 5 to 100 m; narrower than the 25m blasts yet within the 100m scale of other attacks
- [U-0406](unknowns.md#u-0406) resolution: VOD: measure the burn strip on the map.

### U-0407

[U-0407](unknowns.md#u-0407): Airstrike strip length and whether the strip is centred on the chosen point and may leave the safe zone. Status: `open`.

Why it matters ([U-0407](unknowns.md#u-0407)): Together with the width fixes the burned area, and whether fire can reach the unsafe zone.

- [U-0407](unknowns.md#u-0407) free parameter `airstrike_strip_length_m`, swept over 50 to 1000 m; the wiki gives no size, bounded by the map scale
- [U-0407](unknowns.md#u-0407) resolution: VOD: measure the burn strip on the map.

### U-0409

[U-0409](unknowns.md#u-0409): Gunship bomb count and timing: 'a gunship for 5min', 'one every 10s', 'each bomb lands 5s later'. How many bombs can be dropped, does the first drop come at t=0 or t=10s, and do bombs landing after 5min still land? Status: `open`.

Why it matters ([U-0409](unknowns.md#u-0409)): Bomb count is 30, 29 or 31 (or fewer if the buyer must click), which sets total damage and Flak jacket value.

- [U-0409](unknowns.md#u-0409) reading A: drops at t=10,20,...,300s: 30 bombs, the last lands at 305s
- [U-0409](unknowns.md#u-0409) reading B: drops at t=0,10,...,290s: 30 bombs
- [U-0409](unknowns.md#u-0409) reading C: drops at t=0,...,300s: 31 bombs
- [U-0409](unknowns.md#u-0409) reading D: drops at t=10,...,290s: 29 bombs (last drop before expiry)
- [U-0409](unknowns.md#u-0409) reading E: bomb launch is manual with a 10s cooldown, count is player dependent
- [U-0409](unknowns.md#u-0409) free parameter `gunship_bombs_max`, swept over 29 to 31 bombs; derived from the 5min window and the 10s cadence, plus the 'manual' reading as a cap
- [U-0409](unknowns.md#u-0409) resolution: VOD: count bombs of one full gunship with a timer.

### U-0418

[U-0418](unknowns.md#u-0418): Bounty consequences: does the bounty end when claimed (the wiki ends it at 1h or on death) so that repeated claims are possible, and is the marked contestant's 10 HP taken once at claim? Who counts as eligible when no living contestant lacks a bounty? Status: `open`.

Why it matters ([U-0418](unknowns.md#u-0418)): A bounty that persists after a claim would pay and hurt repeatedly.

- [U-0418](unknowns.md#u-0418) reading A: claim ends the bounty and the 10 HP hit happens once
- [U-0418](unknowns.md#u-0418) reading B: bounty persists and can be claimed again after each 1min
- [U-0418](unknowns.md#u-0418) reading C: bounty persists for the claim by another hunter only
- [U-0418](unknowns.md#u-0418) resolution: VOD: bounty marker after a claim.

### U-0425

[U-0425](unknowns.md#u-0425): Zombie drain timing: 'drain 1 HP from any contestants within 5m every 10s'. Is the 10s timer per zombie (global phase) or per contestant from entry, when does the first drain occur, is each drain a 'hit' ([U-0002](unknowns.md#u-0002)), and does it reach the 1 HP floor/Kick-live reduction? Status: `open`.

Why it matters ([U-0425](unknowns.md#u-0425)): Drain per second by many zombies; a crowd of 50 zombies is 5 HP/s if all are in range.

- [U-0425](unknowns.md#u-0425) reading A: per zombie: all contestants within 5m at the tick lose 1 HP
- [U-0425](unknowns.md#u-0425) reading B: per zombie-contestant pair, timer starts at entry
- [U-0425](unknowns.md#u-0425) reading C: per zombie, first tick 10s after spawn
- [U-0425](unknowns.md#u-0425) resolution: VOD: a contestant approached by one zombie, timed.

### U-0500

[U-0500](unknowns.md#u-0500): Piety 'one blood token per 5 HP healed': is the remainder carried between heal events (cumulative counter) or floored per event? Status: `open`.

Why it matters ([U-0500](unknowns.md#u-0500)): Decides whether small heals (campfire 1 HP per second, bandage ticks, Healing sigil 1 HP heals, potions of 5/11/23/46 HP) earn tokens at all; per-event flooring can make a 1 HP trickle worth 0.

- [U-0500](unknowns.md#u-0500) reading A: tokens = floor(H_total / 5) with H_total the cumulative qualifying HP healed since the start (remainder carried)
- [U-0500](unknowns.md#u-0500) reading B: tokens per event = floor(h / 5), remainder discarded at each heal event
- [U-0500](unknowns.md#u-0500) reading C: like B but a continuous heal (bandage 10 HP over 2min, Campfire 1 HP/s) is one event per tick, so ticks of 1 HP earn nothing
- [U-0500](unknowns.md#u-0500) resolution: VOD: observe the blood-token counter of a Piety contestant across several heals. Two consecutive 3 HP heals pay 1 token total (A) or 0 (B, C).
- [U-0500](unknowns.md#u-0500) resolution: REA: token-award code in shipped server logic (client code holds none, RE-0001).

### U-0501

[U-0501](unknowns.md#u-0501): Piety token counter: does 'HP healed' mean the nominal potion amount or the HP actually restored, and is the +15% bonus included? Status: `open`.

Why it matters ([U-0501](unknowns.md#u-0501)): A Piety contestant near full HP can drink a potion for almost no HP; the token yield per potion changes by up to 9 tokens (gigantic potion).

- [U-0501](unknowns.md#u-0501) reading A: effective HP restored (clamped by max HP), after the +15% bonus
- [U-0501](unknowns.md#u-0501) reading B: nominal heal after the +15% bonus (overheal counts)
- [U-0501](unknowns.md#u-0501) reading C: nominal heal before the bonus (raw tier value 5/10/20/40, overheal counts)
- [U-0501](unknowns.md#u-0501) reading D: effective HP restored, bonus not counted
- [U-0501](unknowns.md#u-0501) resolution: VOD: observe the blood-token counter of a Piety contestant across several heals. Drink a potion at full HP and at 1 HP below max, compare token gain.
- [U-0501](unknowns.md#u-0501) resolution: REA: heal handler.

### U-0502

[U-0502](unknowns.md#u-0502): Piety 'from any source except revives, Campfires and healing circles included': are Campfires and healing circles counted (only revives excluded) or excluded together with revives? Status: `open`.

Why it matters ([U-0502](unknowns.md#u-0502)): The trailing phrase 'included' attaches either to the exception list or to the counted sources; the term 'healing circle' appears nowhere else in the corpus. Changes whether standing at an Ingenuity Campfire pays Piety tokens.

- [U-0502](unknowns.md#u-0502) reading A: all healing except revives counts; Campfire healing and healing circles are explicitly included
- [U-0502](unknowns.md#u-0502) reading B: revives, Campfires and healing circles are all excluded; everything else counts
- [U-0502](unknowns.md#u-0502) resolution: VOD: Piety contestant healed by a Campfire, token counter before and after.
- [U-0502](unknowns.md#u-0502) resolution: Organizer statement.

### U-0504

[U-0504](unknowns.md#u-0504): What is the size distribution of the 'random health potion' a Piety contestant gets from a chest or crate? Status: `open`.

Why it matters ([U-0504](unknowns.md#u-0504)): Expected healing per chest and the blood-token value of converted potions (1, 2, 3 or 4 tokens) depend on the tier weights; the wiki gives none.

- [U-0504](unknowns.md#u-0504) reading A: uniform over the four tiers (1/4 each)
- [U-0504](unknowns.md#u-0504) reading B: weighted toward small tiers (as an ordinary health-potion drop table)
- [U-0504](unknowns.md#u-0504) reading C: tier depends on the replaced item or chest type
- [U-0504](unknowns.md#u-0504) free parameter `piety_potion_tier_weights`, swept over each of 4 weights in [0,1] summing to 1; the uniform vector (0.25 each) is the baseline and the two extremes (all small, all gigantic) bound the value of a chest
- [U-0504](unknowns.md#u-0504) resolution: VOD: tally potion tiers from many Piety claims.
- [U-0504](unknowns.md#u-0504) resolution: Organizer statement.

### U-0507

[U-0507](unknowns.md#u-0507): Greed 'A successful steal earns five blood tokens, once per victim every 24 hours': does the 24 h limit cap the token payout only, or the steals themselves? Status: `open`.

Why it matters ([U-0507](unknowns.md#u-0507)): If only the payout is capped, a Greed contestant can keep stealing from one victim every 30 min for items; otherwise each victim loses at most one item a day to a given thief.

- [U-0507](unknowns.md#u-0507) reading A: steals from the same victim are allowed every cooldown; the 5 tokens are paid at most once per victim per 24 h
- [U-0507](unknowns.md#u-0507) reading B: a given victim can be successfully stolen from at most once per 24 h by that thief
- [U-0507](unknowns.md#u-0507) resolution: VOD: a Greed contestant stealing twice from the same victim within 24 h (cooldown 30 min).
- [U-0507](unknowns.md#u-0507) resolution: Organizer statement.

### U-0510

[U-0510](unknowns.md#u-0510): What is the base claim range for chests and crates that Greed doubles ('2x as far away')? Status: `open`.

Why it matters ([U-0510](unknowns.md#u-0510)): No page in the corpus gives the ordinary claim or take range (the chests page was removed), so the Greed reach is not a number yet.

- [U-0510](unknowns.md#u-0510) free parameter `chest_claim_range_base_m`, swept over 2 to 20 m: other contact actions on the wiki use 10 m (steal, merchant, gravestone robbing, heal range), so 10 m is the central value and 2 m / 20 m bound close contact and a wide reach
- [U-0510](unknowns.md#u-0510) resolution: VOD: distance at which a non-Greed contestant can claim a chest versus a Greed one.
- [U-0510](unknowns.md#u-0510) resolution: SCOPE.md P1 (removed chests page).

### U-0512

[U-0512](unknowns.md#u-0512): Greed 'adds a blood token to your money bag': is the money bag the ordinary blood-token balance, or a separate store that is paid out later? Status: `open`.

Why it matters ([U-0512](unknowns.md#u-0512)): The term appears once in the corpus. A separate bag changes when tokens are spendable at the merchant and whether they drop into the gravestone.

- [U-0512](unknowns.md#u-0512) reading A: the money bag is the ordinary balance; +1 token is immediate and spendable
- [U-0512](unknowns.md#u-0512) reading B: a separate store, released at some trigger (time, merchant visit, death)
- [U-0512](unknowns.md#u-0512) reading C: a separate store that is lost or locked in the gravestone on death
- [U-0512](unknowns.md#u-0512) resolution: VOD: a Greed contestant's token counter right after claiming a chest.
- [U-0512](unknowns.md#u-0512) resolution: Organizer statement.

### U-0514

[U-0514](unknowns.md#u-0514): What does 'hack' do to a landmine or C4, and is there a limit? Status: `open`.

Why it matters ([U-0514](unknowns.md#u-0514)): Ingenuity earns a blood token per hack; the effect (disarm, take over, steal) decides whether it counters enemy explosives or turns them.

- [U-0514](unknowns.md#u-0514) reading A: hack disarms or destroys the explosive
- [U-0514](unknowns.md#u-0514) reading B: hack transfers control to the Ingenuity contestant (the sigil text says 'take control of traps')
- [U-0514](unknowns.md#u-0514) reading C: hack reveals and lets the Ingenuity contestant pick it up
- [U-0514](unknowns.md#u-0514) resolution: VOD: an Ingenuity contestant hacking an enemy landmine.

### U-0517

[U-0517](unknowns.md#u-0517): Ingenuity crafts: are both named ingredients consumed, does a craft occupy one of the five craft slots, and how do six recipes fit five slots? Status: `open`.

Why it matters ([U-0517](unknowns.md#u-0517)): Six recipes exist and five craft slots; whether crafts of one type stack and whether ingredients return decide how many crafts can be held.

- [U-0517](unknowns.md#u-0517) reading A: both ingredients are consumed; each craft occupies one of the 5 craft slots; the same recipe can be crafted repeatedly until slots are full
- [U-0517](unknowns.md#u-0517) reading B: crafts stack by type inside a slot
- [U-0517](unknowns.md#u-0517) reading C: only one ingredient is consumed
- [U-0517](unknowns.md#u-0517) resolution: VOD: an Ingenuity contestant crafting with a full craft inventory.
- [U-0517](unknowns.md#u-0517) resolution: Organizer statement.

### U-0518

[U-0518](unknowns.md#u-0518): Unique crafts '40% chance to be destroyed by Zombie hits': is the roll per drain hit, per zombie, or per craft, and does a blocked hit roll? Status: `open`.

Why it matters ([U-0518](unknowns.md#u-0518)): Sets the expected lifetime of crafts near zombies; zombies drain every 10 s (guard zombies every 5 s), so per-hit rolling destroys nearly every craft quickly.

- [U-0518](unknowns.md#u-0518) reading A: each drain hit rolls once per craft held, 40% each
- [U-0518](unknowns.md#u-0518) reading B: each drain hit rolls once and destroys one random craft
- [U-0518](unknowns.md#u-0518) reading C: one roll per zombie encounter
- [U-0518](unknowns.md#u-0518) reading D: as A or B but a hit blocked by Shield, repellent or bubble does not roll
- [U-0518](unknowns.md#u-0518) resolution: VOD: Ingenuity contestant holding several crafts near a zombie.

### U-0520

[U-0520](unknowns.md#u-0520): Campfire shared pool: how does the pool drain with several people, and are full-HP bystanders healed? Status: `open`.

Why it matters ([U-0520](unknowns.md#u-0520)): 'Heals everyone within 10m 1 HP per second from one shared pool' gives pool drain N HP/s for N targets or 1 HP/s total; the pool equals the potion's heal (5, 10, 20, 40 HP) but also the 10 min cap, so a gigantic potion gives 40 HP only.

- [U-0520](unknowns.md#u-0520) reading A: each person in range with missing HP takes 1 HP per second from the pool (pool drains N HP/s)
- [U-0520](unknowns.md#u-0520) reading B: the pool pays 1 HP per second in total, split among those in range
- [U-0520](unknowns.md#u-0520) reading C: every person in range counts, including those at full HP, and drains 1 HP/s each
- [U-0520](unknowns.md#u-0520) resolution: VOD: a Campfire with 1, then 2 contestants in range.

### U-0524

[U-0524](unknowns.md#u-0524): Fortress 'up to 30 HP': one pool shared by everyone inside 20 m, or 30 HP for each person? Status: `open`.

Why it matters ([U-0524](unknowns.md#u-0524)): A shared pool of 30 HP is gone after 2 missiles; per person it protects a group much longer. The damage page says it 'absorbs up to its remaining durability', which suggests one shared durability.

- [U-0524](unknowns.md#u-0524) reading A: one shared durability of 30 HP, consumed by any hit on anyone inside
- [U-0524](unknowns.md#u-0524) reading B: 30 HP of absorption per protected contestant
- [U-0524](unknowns.md#u-0524) resolution: VOD: two contestants inside a fortress, hits on both.

### U-0525

[U-0525](unknowns.md#u-0525): Fortress and zone damage: is zone damage absorbed from the 30 HP durability or ignored entirely? Status: `open`.

Why it matters ([U-0525](unknowns.md#u-0525)): The page lists zone damage next to the 30 HP absorption but also says it protects 'from Sigil of Greed stealing, and zone damage', a separate kind of protection.

- [U-0525](unknowns.md#u-0525) reading A: zone damage inside a fortress is fully immunized and does not use durability
- [U-0525](unknowns.md#u-0525) reading B: zone damage is absorbed 1 HP per tick from the 30 HP durability
- [U-0525](unknowns.md#u-0525) resolution: VOD: a contestant standing in a fortress outside the safe zone.

### U-0526

[U-0526](unknowns.md#u-0526): Fortress lifetime and position: how long does it stay, and is it fixed where it is placed? Status: `open`.

Why it matters ([U-0526](unknowns.md#u-0526)): Without a duration the 30 HP could be a permanent camp; the page gives none.

- [U-0526](unknowns.md#u-0526) free parameter `fortress_duration_s`, swept over from 600 s (the Campfire and Robot cap) to the event length: 10 min is the lower bound set by sibling crafts, the whole event the upper bound
- [U-0526](unknowns.md#u-0526) resolution: VOD: a fortress after several minutes.
- [U-0526](unknowns.md#u-0526) resolution: Organizer statement.

### U-0528

[U-0528](unknowns.md#u-0528): Trolling 'one blood token per 5 HP dealt to other players': is the remainder carried, and is 'dealt' the nominal hit or the HP that actually got through (after armor, fortress, Kick reduction)? Status: `open`.

Why it matters ([U-0528](unknowns.md#u-0528)): A 5 HP fake chest pays 1 token only if the full 5 HP counts: a Kick-live victim takes 4 HP under reading A of [U-0001](unknowns.md#u-0001), and armor or a Shield can absorb all of it.

- [U-0528](unknowns.md#u-0528) reading A: cumulative counter over HP actually lost by the victim, floor(total / 5) tokens, remainder carried
- [U-0528](unknowns.md#u-0528) reading B: per hit floor(d / 5) over the hit after reductions, remainder discarded
- [U-0528](unknowns.md#u-0528) reading C: cumulative or per hit, but over the nominal hit before armor, fortress and Kick reduction
- [U-0528](unknowns.md#u-0528) reading D: damage absorbed by Body Armor or a fortress counts as dealt
- [U-0528](unknowns.md#u-0528) resolution: VOD: Trolling contestant token counter after fake chest claims on armored, shielded and Kick-live victims.

### U-0529

[U-0529](unknowns.md#u-0529): Trolling income scope: which damage counts as 'HP dealt to other players' (weapons, fake chest, unsafe circle ticks, poison from the fake gravestone, reflected hits), and which crates count as 'crate destroyed, whoever spawned it'? Status: `open`.

Why it matters ([U-0529](unknowns.md#u-0529)): Unsafe circle ticks are 1 HP each and a periodic source; whether they pay depends on whether periodic damage is a hit ([U-0002](unknowns.md#u-0002)). Crates destroyed by an Ingenuity Black hole or by another contestant may or may not pay the Trolling contestant.

- [U-0529](unknowns.md#u-0529) reading A: damage by the contestant's own weapons and traps only; crates destroyed by the contestant's own action
- [U-0529](unknowns.md#u-0529) reading B: also unsafe circle ticks and poison steps caused by the contestant's traps; crates destroyed by anyone near them
- [U-0529](unknowns.md#u-0529) reading C: damage counts only when it reduces the target's HP; crates destroyed by the contestant only, including viewer-bought crates
- [U-0529](unknowns.md#u-0529) resolution: VOD: Trolling token counter after an unsafe circle with a victim inside.
- [U-0529](unknowns.md#u-0529) resolution: Organizer statement.

### U-0535

[U-0535](unknowns.md#u-0535): Unsafe circle '50m (164ft) circle': is 50 m the radius or the diameter? Status: `open`.

Why it matters ([U-0535](unknowns.md#u-0535)): Area differs by a factor of 4 (about 7854 m2 versus 1963 m2).

- [U-0535](unknowns.md#u-0535) reading A: radius 50 m
- [U-0535](unknowns.md#u-0535) reading B: diameter 50 m (radius 25 m)
- [U-0535](unknowns.md#u-0535) free parameter `unsafe_circle_radius_m`, swept over 25 to 50 m (diameter versus radius reading)
- [U-0535](unknowns.md#u-0535) resolution: VOD: placing a circle and measuring on the map.
- [U-0535](unknowns.md#u-0535) resolution: Organizer statement.

### U-0537

[U-0537](unknowns.md#u-0537): Unsafe circle damage clock: is the first hit 2 s after each entry (timer resets on exit) or does a global 2 s phase continue? Does moving between the part of the circle inside a safe zone and the outside part reset it? Status: `open`.

Why it matters ([U-0537](unknowns.md#u-0537)): Changes the damage for contestants who skirt the edge; also interacts with the 5 s grace of ordinary zone damage ([U-0003](unknowns.md#u-0003)).

- [U-0537](unknowns.md#u-0537) reading A: per-contestant timer: first hit 2 s after entering the damaging part, reset on leaving
- [U-0537](unknowns.md#u-0537) reading B: timer persists while the contestant is inside the circle, even when crossing between inside-zone and outside-zone parts
- [U-0537](unknowns.md#u-0537) reading C: global 2 s ticks while inside
- [U-0537](unknowns.md#u-0537) resolution: VOD: contestant entering and leaving an unsafe circle.

### U-0538

[U-0538](unknowns.md#u-0538): Unsafe circle item loss: when does the first loss happen relative to entry and to the first hit? Status: `open`.

Why it matters ([U-0538](unknowns.md#u-0538)): Two clauses word it differently ('every five seconds' while inside versus 'after your first hit ... every five seconds'); first loss time differs by 0 to 5 s.

- [U-0538](unknowns.md#u-0538) reading A: first loss at t_hit + 5 s, then every 5 s
- [U-0538](unknowns.md#u-0538) reading B: first loss at the first hit, then every 5 s
- [U-0538](unknowns.md#u-0538) reading C: first loss 5 s after entry, then every 5 s, independent of the first hit
- [U-0538](unknowns.md#u-0538) resolution: VOD: a contestant with several defense items entering the circle.

### U-0601

[U-0601](unknowns.md#u-0601): Death heal 'for every contestant eliminated so far, them included': what is counted, and does a revived contestant still count? Status: `open`.

Why it matters ([U-0601](unknowns.md#u-0601)): Sets the heal size N per nearby death; N grows during the event so the choice shifts total Death healing.

- [U-0601](unknowns.md#u-0601) reading A: N = number of death events since the event start, the new victim included (a revive never lowers it)
- [U-0601](unknowns.md#u-0601) reading B: N = number of contestants currently dead, the new victim included (a revive lowers it)
- [U-0601](unknowns.md#u-0601) reading C: N = number of distinct contestants who have died at least once
- [U-0601](unknowns.md#u-0601) resolution: VOD: heal amount shown on a Death contestant after a death that follows a revive.

### U-0602

[U-0602](unknowns.md#u-0602): Death cap 'When 20% or fewer of the contestants are alive': 20% of which count, with what rounding, and is the alive count taken before or after the death that triggers the heal? Status: `open`.

Why it matters ([U-0602](unknowns.md#u-0602)): Decides the exact elimination at which the 60% cap switches on; with N total contestants the threshold shifts by one contestant.

- [U-0602](unknowns.md#u-0602) reading A: alive * 5 <= N exactly (equals alive <= floor(N/5))
- [U-0602](unknowns.md#u-0602) reading B: alive <= ceil(N/5)
- [U-0602](unknowns.md#u-0602) reading C: alive counted after the triggering death; D: alive counted before it (combine with A or B)
- [U-0602](unknowns.md#u-0602) resolution: Organizer statement of N ([U-0009](unknowns.md#u-0009)), then VOD of the first Death heal that stops at 60%.

### U-0603

[U-0603](unknowns.md#u-0603): Death 60% cap: if HP is already above 60% of max HP, does the heal lower HP to the cap, do nothing, or is the cap rounded? Status: `open`.

Why it matters ([U-0603](unknowns.md#u-0603)): A literal cap can remove HP from a healthy Death contestant; also the cap value 0.6*M is fractional when M is not a multiple of 5.

- [U-0603](unknowns.md#u-0603) reading A: HP' = min(HP + h, 0.6*M), can lower HP
- [U-0603](unknowns.md#u-0603) reading B: HP' = max(HP, min(HP + h, 0.6*M)), never lowers
- [U-0603](unknowns.md#u-0603) reading C: as B with cap = floor(0.6*M)
- [U-0603](unknowns.md#u-0603) reading D: as B with cap = ceil(0.6*M)
- [U-0603](unknowns.md#u-0603) resolution: VOD: Death contestant above 60% HP near a death while 20% or fewer are alive.

### U-0604

[U-0604](unknowns.md#u-0604): Death ward: when does the 2h cooldown start (at the blocked hit, at the end of the 2min immunity, or from the sigil pick), is the ward ready at the pick, and which damage ticks count as 'the first hit'? Status: `open`.

Why it matters ([U-0604](unknowns.md#u-0604)): Fixes how many times the ward can protect over the event (a 2 min window per 2h) and whether zone ticks consume it.

- [U-0604](unknowns.md#u-0604) reading A: cooldown starts at the first blocked hit; ready from the sigil pick
- [U-0604](unknowns.md#u-0604) reading B: cooldown starts when the 2min immunity ends
- [U-0604](unknowns.md#u-0604) reading C: ready only 2h after the pick
- [U-0604](unknowns.md#u-0604) reading D: periodic zone ticks count as hits (see [U-0002](unknowns.md#u-0002)), E: only discrete attacks count
- [U-0604](unknowns.md#u-0604) resolution: VOD: Death contestant leaving the zone twice in under 2h.

### U-0606

[U-0606](unknowns.md#u-0606): Death 'rob': does first-looting an item or blood tokens give the same 5% heal and 10 tokens as the 'rob a gravestone' action, and can blood tokens be looted while locked for revival? Status: `open`.

Why it matters ([U-0606](unknowns.md#u-0606)): The intro page says tokens in a grave stay locked while revival is possible, yet the Death page says the first loot of tokens robs the grave.

- [U-0606](unknowns.md#u-0606) reading A: first loot of an item or tokens is a full rob (heal, 10 tokens, grave becomes unrevivable); tokens lootable immediately
- [U-0606](unknowns.md#u-0606) reading B: first loot is a rob, but tokens cannot be looted until the revive window is over, so only an item loot robs early
- [U-0606](unknowns.md#u-0606) reading C: first loot only seals the grave; the heal and 10 tokens need the explicit rob action
- [U-0606](unknowns.md#u-0606) resolution: VOD: Death contestant looting a grave less than 10 min after a death.

### U-0607

[U-0607](unknowns.md#u-0607): Endurance care packages 'every 2h 30min': first drop 2h30 after the event start, after the sigil pick, or after the previous claim, and which packages are 'your own'? Status: `open`.

Why it matters ([U-0607](unknowns.md#u-0607)): Fixes how many six-token claims an Endurance contestant can make during an event and when supply arrives.

- [U-0607](unknowns.md#u-0607) reading A: fixed clock from event start
- [U-0607](unknowns.md#u-0607) reading B: fixed clock from the sigil pick
- [U-0607](unknowns.md#u-0607) reading C: timer restarts when the previous package is claimed or lands
- [U-0607](unknowns.md#u-0607) reading D: 'your own' = the package that fell near you, whoever stands there; E: also requires you to be the claimer
- [U-0607](unknowns.md#u-0607) resolution: VOD: first Endurance drop timestamp against the event start and the sigil pick.

### U-0612

[U-0612](unknowns.md#u-0612): How long do summoned, death and horde-bonus zombies live ('A zombie disappears when its time runs out')? Status: `open`.

Why it matters ([U-0612](unknowns.md#u-0612)): Lifetime caps zombie drain and Necromancy blood-token income. Only the guard zombie has a stated duration (1h).

- [U-0612](unknowns.md#u-0612) free parameter `zombie_lifetime_s`, swept over 60 to 86400 s: 1 min as a floor for a zombie to matter, one full day as a ceiling above any event length; anchor is the 3600 s guard zombie.
- [U-0612](unknowns.md#u-0612) resolution: VOD: time between a summon and the zombie vanishing.

### U-0613

[U-0613](unknowns.md#u-0613): Necromancy 'The HP goes to you': is the gain the HP the victim actually lost, is it capped at the owner's max HP, and does a blocked or armor-absorbed drain give HP and tokens? Status: `open`.

Why it matters ([U-0613](unknowns.md#u-0613)): Sets Necromancy sustain and blood-token income per drain tick.

- [U-0613](unknowns.md#u-0613) reading A: owner gains HP actually removed from the victim, capped at max HP
- [U-0613](unknowns.md#u-0613) reading B: owner gains the nominal 1 HP (or 2 HP) per tick even when armor absorbs it, capped at max HP
- [U-0613](unknowns.md#u-0613) reading C: owner gains nominal HP and may exceed max HP
- [U-0613](unknowns.md#u-0613) reading D: blood tokens ('one per HP your zombies drain') follow the same measure as the HP
- [U-0613](unknowns.md#u-0613) resolution: VOD: drain on an armored victim, owner HP and token counter.

### U-0617

[U-0617](unknowns.md#u-0617): Protection 'Potions heal you 50% less': which heals are 'potions' (health potions, Eddie's potion, God's Fruit, bandages, healing circle)? Status: `open`.

Why it matters ([U-0617](unknowns.md#u-0617)): Decides how much healing a Protection contestant can still use.

- [U-0617](unknowns.md#u-0617) reading A: health potions of every tier only
- [U-0617](unknowns.md#u-0617) reading B: health potions and Eddie's potion (a gamble that heals 50% of max HP)
- [U-0617](unknowns.md#u-0617) reading C: every item heal
- [U-0617](unknowns.md#u-0617) resolution: VOD: Protection contestant using each heal item.
- [U-0617](unknowns.md#u-0617) narrowed: Narrowed on 2026-11-13 from the text of the 2026-11-11 snapshot, not resolved. A Campfire is out of the rule: "Piety and Protection potion changes do not apply" (wiki-sigils-ingenuity-021). Bandages have their own line on the Protection page, next to the potion line: "Bandages last 1.1x as long" (wiki-sigils-protection-017); that suggests they are not counted as potions, without saying so. The wording does not choose between readings A and B: Protection says "Potions heal you 50% less" (wiki-sigils-protection-016) where Piety says "Health potions heal you 15% more" (wiki-sigils-piety-013), and two other things are named potions, Eddie's potion and the Everything potion, which "heals by potion tier" (wiki-sigils-ingenuity-023). Still open: Eddie's potion, the Everything potion, God's Fruit and the healing circle.

### U-0624

[U-0624](unknowns.md#u-0624): Healing revive counters: '2 times' (a Healing contestant being revived) and '10 times' (a Healing contestant reviving): per event, per pair, and do cancelled or failed revives count? Status: `open`.

Why it matters ([U-0624](unknowns.md#u-0624)): Bounds the Healing contestant's number of lives and total revives.

- [U-0624](unknowns.md#u-0624) reading A: total per event for each Healing contestant, successful revives only
- [U-0624](unknowns.md#u-0624) reading B: per reviver for the 2-times rule
- [U-0624](unknowns.md#u-0624) reading C: attempts count, even when the revive is cancelled
- [U-0624](unknowns.md#u-0624) resolution: VOD: third revive of a Healing contestant.

### U-0625

[U-0625](unknowns.md#u-0625): Revive cost 'costs the reviver 5 HP': can it kill a reviver with 5 HP or fewer, and does it run through the hit pipeline (armor, fortress, Kick live)? Status: `open`.

Why it matters ([U-0625](unknowns.md#u-0625)): A reviver at 5 HP or less could die for the revive, and the revived contestant gets 5 HP.

- [U-0625](unknowns.md#u-0625) reading A: revive needs HP > 5; refused otherwise
- [U-0625](unknowns.md#u-0625) reading B: revive needs HP >= 5 and may leave 0 (reviver dies)
- [U-0625](unknowns.md#u-0625) reading C: cost is min(5, HP - 1)
- [U-0625](unknowns.md#u-0625) reading D: cost goes through the hit pipeline (see [U-0002](unknowns.md#u-0002))
- [U-0625](unknowns.md#u-0625) resolution: VOD: reviver with 5 HP attempting a revive.

## Priority: medium

### U-0003

[U-0003](unknowns.md#u-0003): Zone damage: is the first tick at 5 s or at 7 s after leaving the safe zone? Status: `open`.

Why it matters ([U-0003](unknowns.md#u-0003)): Shifts time to death outside the zone by 2 s (T(100) = 203 s or 205 s).

- [U-0003](unknowns.md#u-0003) reading A: first tick at 5 s, then every 2 s
- [U-0003](unknowns.md#u-0003) reading B: first tick at 7 s (5 s grace, then one 2 s interval)
- [U-0003](unknowns.md#u-0003) resolution: VOD with on-screen timer of a contestant leaving the zone.

### U-0007

[U-0007](unknowns.md#u-0007): Healing regeneration: does damage reset the 30 min timer? Status: `open`.

Why it matters ([U-0007](unknowns.md#u-0007)): Sets the sustained regeneration rate under periodic damage.

- [U-0007](unknowns.md#u-0007) reading A: fixed 30 min clock, damage does not reset it
- [U-0007](unknowns.md#u-0007) reading B: damage resets the timer
- [U-0007](unknowns.md#u-0007) resolution: VOD: Healing contestant HP over an hour with hits.

### U-0010

[U-0010](unknowns.md#u-0010): Wizard staff '10 HP in total over 5 s': one hit or several ticks? Status: `open`.

Why it matters ([U-0010](unknowns.md#u-0010)): Decides whether the Kick bonus, the Kick reduction and the 1 HP minimum apply once or per tick.

- [U-0010](unknowns.md#u-0010) reading A: one 10 HP hit
- [U-0010](unknowns.md#u-0010) reading B: five 2 HP ticks
- [U-0010](unknowns.md#u-0010) reading C: ten 1 HP ticks
- [U-0010](unknowns.md#u-0010) resolution: VOD: HP readout during a staff area.

### U-0011

[U-0011](unknowns.md#u-0011): Revive window: 'within 10min of their death' on the intro page versus 'within 10min of the death' on the Healing page: whose death starts the window? Status: `open`.

Why it matters ([U-0011](unknowns.md#u-0011)): Read literally, 'their' could refer to the reviving contestants.

- [U-0011](unknowns.md#u-0011) reading A: the dead contestant's death (only coherent reading)
- [U-0011](unknowns.md#u-0011) reading B: the reviver's death
- [U-0011](unknowns.md#u-0011) resolution: Healing page wording supports A.

### U-0012

[U-0012](unknowns.md#u-0012): How is Kick-live status detected, and with what latency? Status: `open`.

Why it matters ([U-0012](unknowns.md#u-0012)): A stream drop could flip the 10% modifiers mid-fight.

- [U-0012](unknowns.md#u-0012) resolution: Organizer statement; VOD of a stream reconnect during combat.

### U-0102

[U-0102](unknowns.md#u-0102): Fortress step: how many fortresses can absorb one hit when the contestant stands within several, in which order, and is durability lost 1 per HP absorbed? Status: `open`.

Why it matters ([U-0102](unknowns.md#u-0102)): Decides whether stacked fortresses add durability and whether fortress durability is a pool of HP.

- [U-0102](unknowns.md#u-0102) reading A: one fortress (nearest or first built) absorbs min(h, dur) and dur -= absorbed
- [U-0102](unknowns.md#u-0102) reading B: all fortresses in range absorb in turn until h = 0
- [U-0102](unknowns.md#u-0102) reading C: absorption is per hit, not per HP
- [U-0102](unknowns.md#u-0102) resolution: VOD: contestant inside two overlapping fortresses taking a hit.
- [U-0102](unknowns.md#u-0102) resolution: Items page fortress rules read against this step (cross-family).

### U-0105

[U-0105](unknowns.md#u-0105): 'Blood tokens in the grave stay locked while revival is possible': whose tokens, for how long, and what happens at the end of the lock? Status: `open`.

Why it matters ([U-0105](unknowns.md#u-0105)): Decides when looters (including Death sigil) can take tokens from a gravestone and what a revived contestant gets back.

- [U-0105](unknowns.md#u-0105) reading A: the dead contestant's tokens are locked for the 10 min window, then lootable; a revive returns them
- [U-0105](unknowns.md#u-0105) reading B: locked until a revive happens or revival is impossible for another reason (revive cap, robbery)
- [U-0105](unknowns.md#u-0105) reading C: tokens paid to the killer are also locked in the grave until the window ends
- [U-0105](unknowns.md#u-0105) resolution: VOD: gravestone looted before and after 10 min.
- [U-0105](unknowns.md#u-0105) resolution: Cross-check Death sigil page 'first to loot items or blood tokens' rule.

### U-0106

[U-0106](unknowns.md#u-0106): Viewer crown-kill bonus 'equal to 20% of the attack's purchase price': rounding rule, whether 'kills' means the final kill, and which attack counts when several viewers hit the holder. Status: `open`.

Why it matters ([U-0106](unknowns.md#u-0106)): Without the rule the value of a crown kill for viewers is not computable even once prices ([U-0014](unknowns.md#u-0014)) are known.

- [U-0106](unknowns.md#u-0106) reading A: bonus = floor(0.2*p)
- [U-0106](unknowns.md#u-0106) reading B: bonus = ceil(0.2*p)
- [U-0106](unknowns.md#u-0106) reading C: bonus = 0.2*p exactly (fractional Cx-Bucks allowed)
- [U-0106](unknowns.md#u-0106) resolution: VOD/screen: a viewer's Cx-Bucks balance after a crown kill with a known attack price.
- [U-0106](unknowns.md#u-0106) resolution: Organizer statement.

### U-0108

[U-0108](unknowns.md#u-0108): Who can revive a non-Healing contestant: only Healing contestants (implied by the two rules), or anyone with some other rule? Status: `open`.

Why it matters ([U-0108](unknowns.md#u-0108)): Decides whether a dead non-Healing contestant is revivable at all without a Healing contestant alive nearby.

- [U-0108](unknowns.md#u-0108) reading A: only a Healing contestant can revive a non-Healing contestant; others can revive only Healing contestants
- [U-0108](unknowns.md#u-0108) reading B: any contestant can revive any contestant; the 2-times rule is only a cap specific to Healing targets
- [U-0108](unknowns.md#u-0108) resolution: VOD: a non-Healing contestant reviving a non-Healing one.
- [U-0108](unknowns.md#u-0108) resolution: Organizer statement.

### U-0113

[U-0113](unknowns.md#u-0113): 'Moving too fast counts as being outside': when the speed rule trips, does the 5 s grace and 1 HP per 2 s apply as outside, starting when, and does it end the instant speed drops back? Status: `open`.

Why it matters ([U-0113](unknowns.md#u-0113)): Sets the cost of a fast trip: immediate ticks versus 5 s lag and hysteresis.

- [U-0113](unknowns.md#u-0113) reading A: violation = outside; the normal 5 s grace then ticks, ending when the windows are clean again
- [U-0113](unknowns.md#u-0113) reading B: ticks start at once, no grace
- [U-0113](unknowns.md#u-0113) reading C: outside status persists until the window is clean again, which lags the speed drop by up to the window length
- [U-0113](unknowns.md#u-0113) free parameter `speed_violation_grace_s`, swept over 0 to 5 s: 0 if no grace, 5 matches the outside-circle grace
- [U-0113](unknowns.md#u-0113) resolution: VOD: a contestant on a fast ride, HP timeline against speed.

### U-0115

[U-0115](unknowns.md#u-0115): Poison: does the first 1 HP land at once, after 1min 30s, or on a fixed global 90 s phase? Status: `open`.

Why it matters ([U-0115](unknowns.md#u-0115)): Moves total damage by 1 HP at any cut-off time and changes the value of cures.

- [U-0115](unknowns.md#u-0115) reading A: first tick at t = 90 s after poisoning, then every 90 s
- [U-0115](unknowns.md#u-0115) reading B: first tick at t = 0, then every 90 s
- [U-0115](unknowns.md#u-0115) reading C: ticks on a global 90 s grid independent of the poison start
- [U-0115](unknowns.md#u-0115) resolution: VOD: HP of a poisoned contestant with a clock after a poison dart hit.

### U-0119

[U-0119](unknowns.md#u-0119): Death Ward: does the 2 min of immunity start at the first blocked hit or when the sigil is selected; does 'Cooldown 2h' start at activation or at the end of the 2 min, and is the ward available once per cooldown? Status: `open`.

Why it matters ([U-0119](unknowns.md#u-0119)): Sets how often a Death contestant can ignore the outside-circle damage.

- [U-0119](unknowns.md#u-0119) reading A: 2 min window starts at the first blocked hit; cooldown 2 h from that moment
- [U-0119](unknowns.md#u-0119) reading B: 2 min window starts at activation by the contestant; cooldown 2 h from activation
- [U-0119](unknowns.md#u-0119) reading C: cooldown starts when the 2 min window ends
- [U-0119](unknowns.md#u-0119) resolution: VOD: Death contestant after the first outside-circle hit.
- [U-0119](unknowns.md#u-0119) resolution: Sigil page for Death read against this record (cross-family).

### U-0122

[U-0122](unknowns.md#u-0122): Wiki-damage-002 reads 'Reality Shield block every kind of damage. absorbs every kind of damage.' (scrambled): which sentence belongs to which item (Reality Shield blocks every kind, Body armor absorbs every kind)? Status: `open`.

Why it matters ([U-0122](unknowns.md#u-0122)): The only statement that Reality Shield blocks all damage; the table never lists it.

- [U-0122](unknowns.md#u-0122) reading A: Reality Shield blocks every kind of damage; Body armor absorbs every kind of damage (caption of the table)
- [U-0122](unknowns.md#u-0122) reading B: Reality Shield blocks every kind of damage except those the Shield note excludes
- [U-0122](unknowns.md#u-0122) resolution: Re-fetch the rendered page for the header text.
- [U-0122](unknowns.md#u-0122) resolution: Items page Reality Shield section.

### U-0123

[U-0123](unknowns.md#u-0123): Hazmat suit '(slows)' in the damage table: what does slowing do to zone, unsafe-circle and robot damage (tick interval multiplier, damage fraction)? Status: `open`.

Why it matters ([U-0123](unknowns.md#u-0123)): Without the factor the Hazmat suit cannot be priced against Body armor for zone survival.

- [U-0123](unknowns.md#u-0123) reading A: multiplies the tick interval (fewer ticks)
- [U-0123](unknowns.md#u-0123) reading B: reduces each tick below 1 HP over time (fractional accumulation)
- [U-0123](unknowns.md#u-0123) reading C: slows only movement, not damage
- [U-0123](unknowns.md#u-0123) free parameter `hazmat_slow_factor`, swept over 1.0 to 4.0 times the tick interval: 1.0 is no effect, 4.0 is an upper guess for 'slows', sweep choice
- [U-0123](unknowns.md#u-0123) resolution: Items page Hazmat suit section (cross-family).

### U-0200

[U-0200](unknowns.md#u-0200): Which items stack in one slot beyond C4, landmines and arrows (non-Piety health potions, mirror forcefields, others)? Status: `open`.

Why it matters ([U-0200](unknowns.md#u-0200)): Inventory space is 3 slots, so stack rules decide how many defenses and potions fit.

- [U-0200](unknowns.md#u-0200) reading A: only the named C4, landmines and arrows stack
- [U-0200](unknowns.md#u-0200) reading B: other kinds stack as well (list open: 'such as')
- [U-0200](unknowns.md#u-0200) resolution: VOD: a contestant picking up a second mirror forcefield or health potion with a full inventory.
- [U-0200](unknowns.md#u-0200) resolution: Weapons page stack sizes are 5 and 10 per stack.

### U-0201

[U-0201](unknowns.md#u-0201): Do several mirror forcefields count as one effect or each as one toward the 3-effect cap? Status: `open`.

Why it matters ([U-0201](unknowns.md#u-0201)): Decides how many mirrors fit under the cap of 3 and the room left for Shield and Flak jacket.

- [U-0201](unknowns.md#u-0201) reading A: each mirror counts separately
- [U-0201](unknowns.md#u-0201) reading B: all mirrors count as one effect
- [U-0201](unknowns.md#u-0201) reading C: mirrors held but never 'used' do not count until active
- [U-0201](unknowns.md#u-0201) resolution: VOD: a contestant holding two mirrors using a third effect item at the cap.

### U-0202

[U-0202](unknowns.md#u-0202): How do effects not named in the cap lists behave: EMP (10min), Thermal goggles (carried), Body armor, Sleeping Bag, health potions? And what happens when a Hazmat suit is picked up at the cap? Status: `open`.

Why it matters ([U-0202](unknowns.md#u-0202)): The cap lists 'count' and 'do not count' do not cover every item; loadout planning depends on it.

- [U-0202](unknowns.md#u-0202) reading A: only the named items count, EMP and goggles do not
- [U-0202](unknowns.md#u-0202) reading B: EMP counts as a timed item effect, goggles count while carried like the Hazmat suit
- [U-0202](unknowns.md#u-0202) reading C: Hazmat pickup refused at the cap
- [U-0202](unknowns.md#u-0202) resolution: VOD: a contestant with 3 effects using an EMP or picking up goggles or Hazmat.

### U-0203

[U-0203](unknowns.md#u-0203): Do health potions, bandage ticks and Eddie's heal cap at max HP? Status: `open`.

Why it matters ([U-0203](unknowns.md#u-0203)): The heal-over-max question decides whether potions are wasted at high HP and whether Eddie's heal is partly lost.

- [U-0203](unknowns.md#u-0203) reading A: hp = min(maxHP, hp + h)
- [U-0203](unknowns.md#u-0203) reading B: hp can exceed max HP
- [U-0203](unknowns.md#u-0203) resolution: VOD: drinking a potion at full or near full HP.
- [U-0203](unknowns.md#u-0203) resolution: Healing page says regeneration is 'up to your max HP' (explicit only there).

### U-0206

[U-0206](unknowns.md#u-0206): Does Guardian angel 'zone damage' include unsafe circle damage? Status: `open`.

Why it matters ([U-0206](unknowns.md#u-0206)): The damage page table lists Guardian angel for both; the Items page for Shield names the two separately.

- [U-0206](unknowns.md#u-0206) reading A: zone damage only
- [U-0206](unknowns.md#u-0206) reading B: outside-the-circle and unsafe circle damage
- [U-0206](unknowns.md#u-0206) resolution: VOD: a Guardian angel holder inside a Trolling unsafe circle.

### U-0208

[U-0208](unknowns.md#u-0208): Is the Safety bubble '10m' a radius or a diameter? Status: `open`.

Why it matters ([U-0208](unknowns.md#u-0208)): Doubles or quarters the covered area.

- [U-0208](unknowns.md#u-0208) reading A: radius 10 m
- [U-0208](unknowns.md#u-0208) reading B: diameter 10 m, radius 5 m
- [U-0208](unknowns.md#u-0208) free parameter `bubble_radius_m`, swept over 5..10 m (diameter 10 reading to radius 10 reading)
- [U-0208](unknowns.md#u-0208) resolution: VOD: contestants at measured distances from the bubble creator.

### U-0211

[U-0211](unknowns.md#u-0211): Is the smoke bomb cloud fixed where it was set off or does it follow the user? Status: `open`.

Why it matters ([U-0211](unknowns.md#u-0211)): The Items page says 'within 50m of you' and 'inside it'.

- [U-0211](unknowns.md#u-0211) reading A: fixed centre
- [U-0211](unknowns.md#u-0211) reading B: centred on the user
- [U-0211](unknowns.md#u-0211) resolution: VOD: user walking out of their own cloud.

### U-0212

[U-0212](unknowns.md#u-0212): Can the contestant who set off the smoke bomb be targeted from outside the cloud? Status: `open`.

Why it matters ([U-0212](unknowns.md#u-0212)): Sentence 'Nobody outside can target anyone inside' and the setter exemption disagree on the setter.

- [U-0212](unknowns.md#u-0212) reading A: no, the setter is inside and protected
- [U-0212](unknowns.md#u-0212) reading B: yes, the setter is unaffected so can be targeted
- [U-0212](unknowns.md#u-0212) resolution: VOD: attack on a smoke setter from outside.

### U-0213

[U-0213](unknowns.md#u-0213): Does Thermal goggles' exemption cover only smoke attack blocks and blackout, or also the inside-cloud restrictions on healing, stealing and trading? Status: `open`.

Why it matters ([U-0213](unknowns.md#u-0213)): Items 067 says 'block your attacks'; the heal/steal/trade restrictions (043) are not attacks.

- [U-0213](unknowns.md#u-0213) reading A: attack block and blackout only
- [U-0213](unknowns.md#u-0213) reading B: all smoke restrictions
- [U-0213](unknowns.md#u-0213) resolution: VOD: goggles holder inside a cloud attempting to steal or trade.

### U-0214

[U-0214](unknowns.md#u-0214): What is the tick schedule of the Bandage: 10 HP over 2min? Status: `open`.

Why it matters ([U-0214](unknowns.md#u-0214)): Interaction with damage, max HP cap and cure timing.

- [U-0214](unknowns.md#u-0214) reading A: 10 ticks of 1 HP at +12 s..+120 s
- [U-0214](unknowns.md#u-0214) reading B: 10 ticks of 1 HP at +0 s..+108 s
- [U-0214](unknowns.md#u-0214) reading C: 5 ticks of 2 HP every 24 s
- [U-0214](unknowns.md#u-0214) reading D: fractional continuous
- [U-0214](unknowns.md#u-0214) free parameter `bandage_tick_count`, swept over 1..120 ticks over 120 s (1 HP per tick up to fractional)
- [U-0214](unknowns.md#u-0214) resolution: VOD: HP bar after using a bandage.

### U-0215

[U-0215](unknowns.md#u-0215): When several mirror forcefields are held, does one reflection consume one, all, or reflect several times? Status: `open`.

Why it matters ([U-0215](unknowns.md#u-0215)): Pages say 'Several stack' and 'Ends when it reflects an attack' without count.

- [U-0215](unknowns.md#u-0215) reading A: one per reflection
- [U-0215](unknowns.md#u-0215) reading B: all are consumed
- [U-0215](unknowns.md#u-0215) reading C: several reflections in sequence
- [U-0215](unknowns.md#u-0215) resolution: VOD: contestant with two mirrors hit twice.

### U-0216

[U-0216](unknowns.md#u-0216): Does a Flak jacket get used up by a hit already blocked by another defense (Shield, Safety bubble, Sleeping Bag)? Status: `open`.

Why it matters ([U-0216](unknowns.md#u-0216)): Guardian angel is explicit about blocked hits; Flak jacket is not.

- [U-0216](unknowns.md#u-0216) reading A: any hit on you uses it
- [U-0216](unknowns.md#u-0216) reading B: only a hit that reaches it
- [U-0216](unknowns.md#u-0216) resolution: VOD: holder with Shield and Flak jacket hit by a missile.

### U-0300

[U-0300](unknowns.md#u-0300): Are the range bounds of weapons, traps, the merchant and the sleeping bag (10m, 20m, 50m, 15m) inclusive or exclusive, and is distance Euclidean on the ground? Status: `open`.

Why it matters ([U-0300](unknowns.md#u-0300)): Every 'within Xm' and 'comes within Xm' sentence changes at the boundary; a contestant at exactly X metres is hit under one reading and safe under the other.

- [U-0300](unknowns.md#u-0300) reading A: inside iff d <= R (inclusive)
- [U-0300](unknowns.md#u-0300) reading B: inside iff d < R (exclusive)
- [U-0300](unknowns.md#u-0300) resolution: VOD: a contestant at a measured distance equal to the stated radius from a C4 or landmine.
- [U-0300](unknowns.md#u-0300) resolution: REA: shipped distance comparison (client code holds no server logic, RE-0001).

### U-0301

[U-0301](unknowns.md#u-0301): Is the 'once every 16h' Ingenuity trap attachment limit one shared timer for C4 and landmine, or one timer per kind, and does it start at attachment or at detonation? Status: `open`.

Why it matters ([U-0301](unknowns.md#u-0301)): Decides how many trapped gifts an Ingenuity contestant can have in any 48h and whether a stale trap blocks the next one.

- [U-0301](unknowns.md#u-0301) reading A: one shared timer, starts at attachment
- [U-0301](unknowns.md#u-0301) reading B: one timer per kind (C4, landmine), starts at attachment
- [U-0301](unknowns.md#u-0301) reading C: shared timer, starts when the trapped gift fires or is removed
- [U-0301](unknowns.md#u-0301) resolution: VOD: an Ingenuity contestant attaching a C4 then a landmine within 16h.

### U-0303

[U-0303](unknowns.md#u-0303): How do the 'up to 5 of each share one slot / carry at most 5 of each' caps interact with 'An enchanted one uses its own slot'? Status: `open`.

Why it matters ([U-0303](unknowns.md#u-0303)): Fixes the maximum number of C4 and landmines a contestant can hold and the slots they take.

- [U-0303](unknowns.md#u-0303) reading A: enchanted ones count toward the 5 cap and take a separate slot
- [U-0303](unknowns.md#u-0303) reading B: enchanted ones are outside the 5 cap (5 plain + own slot)
- [U-0303](unknowns.md#u-0303) reading C: one enchanted one at a time, outside the cap
- [U-0303](unknowns.md#u-0303) resolution: VOD: inventory screen with 5 plain C4 and an enchanted one.

### U-0304

[U-0304](unknowns.md#u-0304): How many uses do the drone, C4, landmine and Poison Dart have when not enchanted? Status: `open`.

Why it matters ([U-0304](unknowns.md#u-0304)): The wiki gives uses for knife, machete, sword, axe and bow but not for these four, and the enchantment text says they are 'used up' after the bonus uses.

- [U-0304](unknowns.md#u-0304) reading A: single use each (consumed on use)
- [U-0304](unknowns.md#u-0304) reading B: some have several uses (not stated)
- [U-0304](unknowns.md#u-0304) free parameter `uses_unstated_items`, swept over 1 to 3 uses; the enchantment text says 1 use for enchanted C4, landmine and drone and 2 for the dart, so 1 is the natural lower bound and 3 covers the knife/long sword scale
- [U-0304](unknowns.md#u-0304) resolution: VOD: use of each item.
- [U-0304](unknowns.md#u-0304) resolution: Organizer statement.

### U-0306

[U-0306](unknowns.md#u-0306): Which items count for the Ingenuity landmine attachment 'an item you use on yourself'? Status: `open`.

Why it matters ([U-0306](unknowns.md#u-0306)): The C4 text says 'another item you hold'; the landmine text restricts to items used on oneself. The set of valid items decides what a landmine trap can hide in.

- [U-0306](unknowns.md#u-0306) reading A: consumables with a self effect (potions, bandage, shields)
- [U-0306](unknowns.md#u-0306) reading B: any usable item
- [U-0306](unknowns.md#u-0306) reading C: only items that heal
- [U-0306](unknowns.md#u-0306) resolution: VOD: Ingenuity contestant attaching a landmine to several item types.

### U-0311

[U-0311](unknowns.md#u-0311): Zarok's axe: how is a non-integer damage value rounded? Status: `open`.

Why it matters ([U-0311](unknowns.md#u-0311)): Changes the damage by up to 1 HP at most HP levels (and the Kick bonus and the 1 HP minimum then apply on top).

- [U-0311](unknowns.md#u-0311) reading A: floor
- [U-0311](unknowns.md#u-0311) reading B: ceil
- [U-0311](unknowns.md#u-0311) reading C: round half up
- [U-0311](unknowns.md#u-0311) resolution: VOD: axe hit at an HP where the curve gives a fraction.

### U-0312

[U-0312](unknowns.md#u-0312): Wizard staff: is '10m damage area' a radius or a diameter? Status: `open`.

Why it matters ([U-0312](unknowns.md#u-0312)): Doubles or quarters the covered ground; the enchantment text speaks of '+10m area radius', which only suggests radius.

- [U-0312](unknowns.md#u-0312) reading A: radius 10m
- [U-0312](unknowns.md#u-0312) reading B: diameter 10m (radius 5m)
- [U-0312](unknowns.md#u-0312) resolution: VOD: HP loss of contestants at measured distances from the centre.

### U-0313

[U-0313](unknowns.md#u-0313): Wizard staff: does a contestant who is inside the area for only part of the 5s take the full 10 HP or only a share, and do contestants who enter after placement take damage? Status: `open`.

Why it matters ([U-0313](unknowns.md#u-0313)): Decides whether stepping out of the area fast avoids the damage and whether placing it ahead of a path works.

- [U-0313](unknowns.md#u-0313) reading A: everyone inside at placement time takes the full 10 HP
- [U-0313](unknowns.md#u-0313) reading B: damage accrues only while inside (pro rata by time inside)
- [U-0313](unknowns.md#u-0313) reading C: everyone inside at any moment of the 5s takes the full 10 HP once
- [U-0313](unknowns.md#u-0313) resolution: VOD: contestant leaving or entering an active staff area.

### U-0315

[U-0315](unknowns.md#u-0315): Poison Dart: if a poisoned contestant is darted again (or hit by a Fake gravestone), does the new poison restart a full 20 HP schedule, replace what remains, or add? Status: `open`.

Why it matters ([U-0315](unknowns.md#u-0315)): The poison page says re-poisoning resets the timer and does not stack, but the amount reset (full 20 HP or the remainder) is not stated.

- [U-0315](unknowns.md#u-0315) reading A: restarts a fresh 20 HP schedule from the new dart
- [U-0315](unknowns.md#u-0315) reading B: keeps the remaining HP of the older poison and only restarts the interval timer
- [U-0315](unknowns.md#u-0315) reading C: second dart ignored while poisoned
- [U-0315](unknowns.md#u-0315) resolution: VOD: HP and timer of a contestant darted twice.

### U-0317

[U-0317](unknowns.md#u-0317): What does 'Poison Dart ... +10 damage for two uses' mean for a damage-over-time item? Status: `open`.

Why it matters ([U-0317](unknowns.md#u-0317)): Enchanted dart poison could add 10 HP in total, 10 HP per use, or an instant hit.

- [U-0317](unknowns.md#u-0317) reading A: each enchanted dart poisons for 30 HP total over the same 30min
- [U-0317](unknowns.md#u-0317) reading B: each enchanted dart poisons for 20 HP over 30min plus an immediate 10 HP
- [U-0317](unknowns.md#u-0317) reading C: each enchanted dart poisons for 30 HP with the interval kept at 1min 30s (so 45min)
- [U-0317](unknowns.md#u-0317) resolution: VOD: enchanted dart on a contestant.

### U-0318

[U-0318](unknowns.md#u-0318): What do the labels Equippable and Usable mean for the Poison Dart and Zarok's axe, which carry both? Status: `open`.

Why it matters ([U-0318](unknowns.md#u-0318)): Decides whether the dart/axe sit in the weapon slot, are thrown or consumed from the inventory, and whether both modes exist.

- [U-0318](unknowns.md#u-0318) reading A: Equippable = held in a weapon slot, Usable = consumed on use; both labels mean the item can be used either way
- [U-0318](unknowns.md#u-0318) reading B: the two labels are sequential: equip to wield, then use once
- [U-0318](unknowns.md#u-0318) resolution: VOD: inventory and weapon slot of a contestant holding an axe or dart.

### U-0319

[U-0319](unknowns.md#u-0319): When does the first random merchant appear after the event starts? Status: `open`.

Why it matters ([U-0319](unknowns.md#u-0319)): The merchant cycle (15min stay, 30min to 1h away) has no stated phase; early purchasing power and token hoarding depend on it.

- [U-0319](unknowns.md#u-0319) free parameter `merchant_first_spawn_min`, swept over 0 to 75 min after event start: 75 min is the longest full cycle (15 min stay + 1h away), so any phase within one cycle is covered
- [U-0319](unknowns.md#u-0319) resolution: VOD: event start to first merchant appearance.
- [U-0319](unknowns.md#u-0319) resolution: Organizer statement.

### U-0321

[U-0321](unknowns.md#u-0321): Which merchant purchases need a free inventory slot ('Items need a free inventory slot')? Status: `open`.

Why it matters ([U-0321](unknowns.md#u-0321)): Only items are named; the missile, Deep Cut, Dual Wield, enchantments and upgrades may not need a slot. A care package with a full inventory is not covered.

- [U-0321](unknowns.md#u-0321) reading A: care package, anti poison, Vulnerability Dart, Sleeping Bag need a slot; missile and upgrades do not
- [U-0321](unknowns.md#u-0321) reading B: the missile also needs a slot
- [U-0321](unknowns.md#u-0321) reading C: the care package item may go to a weapon slot for a weapon and needs none then
- [U-0321](unknowns.md#u-0321) resolution: VOD: purchase with a full inventory.

### U-0323

[U-0323](unknowns.md#u-0323): Which item does a merchant care package give: the distribution of 'One random item'? Status: `open`.

Why it matters ([U-0323](unknowns.md#u-0323)): Decides the expected value of 10 blood tokens, including whether weapons, C4 and drones come out and whether the result lands in a weapon slot.

- [U-0323](unknowns.md#u-0323) free parameter `merchant_care_package_item_distribution`, swept over uniform over the item catalogue of the items and weapons pages versus weighted toward cheap items; sample at least 30 openings to tell them apart
- [U-0323](unknowns.md#u-0323) resolution: VOD: a sample of merchant care package results.
- [U-0323](unknowns.md#u-0323) resolution: Organizer statement.

### U-0324

[U-0324](unknowns.md#u-0324): Vulnerability Dart: does a second dart on an already vulnerable contestant reset, extend or do nothing, and is the 10 minutes counted from the throw or the impact? Status: `open`.

Why it matters ([U-0324](unknowns.md#u-0324)): Fixes the length of the unprotected window; repeated darts could keep a target vulnerable for good.

- [U-0324](unknowns.md#u-0324) reading A: a new dart resets the 10 min timer to a fresh 10 min from now
- [U-0324](unknowns.md#u-0324) reading B: a new dart adds 10 min
- [U-0324](unknowns.md#u-0324) reading C: no effect while already vulnerable
- [U-0324](unknowns.md#u-0324) resolution: VOD: a contestant hit by two darts 5 min apart.

### U-0330

[U-0330](unknowns.md#u-0330): Max HP upgrade: is there a purchase limit in addition to the HP cap (200, or 220 for Piety), and how many purchases reach each cap per sigil? Status: `open`.

Why it matters ([U-0330](unknowns.md#u-0330)): With 100 base HP the cap 200 is 10 purchases; Piety (110 base) reaches 220 only with 11, and Greed (90 base) needs 11 for 200; the wiki states a purchase limit only for slots.

- [U-0330](unknowns.md#u-0330) reading A: no purchase limit, only the HP cap (Greed 11, Piety 11, others 10 purchases)
- [U-0330](unknowns.md#u-0330) reading B: 10 purchases for everyone (Piety stops at 210, which contradicts the 220 cap)
- [U-0330](unknowns.md#u-0330) free parameter `hp_upgrade_purchase_limit`, swept over 10 to 12 purchases: the caps imply 10 for base 100, 11 for base 90 or 110
- [U-0330](unknowns.md#u-0330) resolution: VOD: Piety contestant after 10 and 11 HP upgrades.

### U-0331

[U-0331](unknowns.md#u-0331): Does '+10 maximum HP' also raise current HP by 10? Status: `open`.

Why it matters ([U-0331](unknowns.md#u-0331)): Decides whether the upgrade is a heal as well as a cap raise.

- [U-0331](unknowns.md#u-0331) reading A: max HP +10, current HP unchanged
- [U-0331](unknowns.md#u-0331) reading B: max HP +10 and current HP +10
- [U-0331](unknowns.md#u-0331) resolution: VOD: HP readout before and after an upgrade at less than full health.

### U-0332

[U-0332](unknowns.md#u-0332): Deep Cut: when is the first bleeding tick, does a new hit while bleeding reset the timer, how long does the charge last unused, and does a bleeding tick count as a hit? Status: `open`.

Why it matters ([U-0332](unknowns.md#u-0332)): Bleeding is the only unbounded damage over time on this page; it ends only on a bandage or a Healing contestant.

- [U-0332](unknowns.md#u-0332) reading A: first tick 5 min after the hit; a new bleeding hit is ignored; the charge never expires; ticks are plain damage events
- [U-0332](unknowns.md#u-0332) reading B: first tick at once, then every 5 min; a new hit restarts the 5 min timer; charge never expires
- [U-0332](unknowns.md#u-0332) reading C: charge expires after an unstated period
- [U-0332](unknowns.md#u-0332) resolution: VOD: bleeding timeline of a contestant hit with a Deep Cut weapon.

### U-0334

[U-0334](unknowns.md#u-0334): Enchantment clocks: does the 2 hours start at purchase or at applying it to a weapon, and does 'For every other weapon, if two hours pass first' also bound the Zarok's axe, Poison Dart, C4, landmine and drone? Status: `open`.

Why it matters ([U-0334](unknowns.md#u-0334)): Without a time limit those items could stay enchanted indefinitely (they only end by use).

- [U-0334](unknowns.md#u-0334) reading A: 2 h from purchase; limit applies only to knife, machete, long sword (the 'every other weapon' group) and to the bow
- [U-0334](unknowns.md#u-0334) reading B: 2 h from purchase; limit applies to every enchanted weapon except the staff
- [U-0334](unknowns.md#u-0334) reading C: 2 h from applying the enchantment to a weapon
- [U-0334](unknowns.md#u-0334) resolution: VOD: enchanted axe or landmine kept for more than 2 h.

### U-0336

[U-0336](unknowns.md#u-0336): Enchanted C4 or landmine: is the '+10m radius' applied to the trigger distance too, and does the enchantment carry onto a trapped gift made with an enchanted trap? Status: `open`.

Why it matters ([U-0336](unknowns.md#u-0336)): The +20 damage on a trapped gift (23 HP and 11 HP base) and the trigger range both change what an enchanted trap does.

- [U-0336](unknowns.md#u-0336) reading A: radius +10 m for both trigger and blast; trapped gift made from an enchanted trap keeps +20
- [U-0336](unknowns.md#u-0336) reading B: radius +10 m for the blast only; trapped gift uses its base 23 or 11 HP
- [U-0336](unknowns.md#u-0336) reading C: an enchanted trap cannot be attached
- [U-0336](unknowns.md#u-0336) resolution: VOD: enchanted landmine triggered at 15 m.

### U-0337

[U-0337](unknowns.md#u-0337): Enchantment limit 'one enchanted weapon, or two with Dual Wield': does it count C4, landmine, drone and Poison Dart, which are not weapon slot items? Status: `open`.

Why it matters ([U-0337](unknowns.md#u-0337)): Decides whether a contestant can hold an enchanted C4 and an enchanted bow together at one slot.

- [U-0337](unknowns.md#u-0337) reading A: limit counts every enchanted item including C4, landmine and drone
- [U-0337](unknowns.md#u-0337) reading B: limit counts only weapon slot items (melee, bows, staffs, Poison Darts)
- [U-0337](unknowns.md#u-0337) resolution: VOD: buying a second weapon enchantment with an enchanted C4 held.

### U-0338

[U-0338](unknowns.md#u-0338): Armor enchantment '+10 durability, up to 45': can it be bought repeatedly, is 45 a cap on durability after the enchant, and from what base? Status: `open`.

Why it matters ([U-0338](unknowns.md#u-0338)): The armor base durability is on another page (Body Armor 15 HP absorb); a repeat purchase path could reach 45.

- [U-0338](unknowns.md#u-0338) reading A: each purchase adds 10, capped at 45 total durability
- [U-0338](unknowns.md#u-0338) reading B: one enchantment per armor; the cap only constrains the starting durability
- [U-0338](unknowns.md#u-0338) reading C: enchantment sets durability to min(current + 10, 45)
- [U-0338](unknowns.md#u-0338) resolution: VOD: armor durability readout before and after buying twice.

### U-0339

[U-0339](unknowns.md#u-0339): Enchanted armor decay 'loses one durability every twenty minutes, down to 15': when does the clock start, does decay stop at 15 even if damage left less, and does a re-enchant restart it? Status: `open`.

Why it matters ([U-0339](unknowns.md#u-0339)): Sets the lifetime of the 45 durability and the floor of the enchanted armor.

- [U-0339](unknowns.md#u-0339) reading A: clock starts at enchant, first loss after 20 min, no loss when durability <= 15
- [U-0339](unknowns.md#u-0339) reading B: clock keeps running from the first enchant and a re-enchant does not restart it
- [U-0339](unknowns.md#u-0339) reading C: decay applies to all armor above 15, enchanted or not
- [U-0339](unknowns.md#u-0339) resolution: VOD: armor durability over an hour after the enchant.

### U-0401

[U-0401](unknowns.md#u-0401): Scope of the EMP block: the wiki lists missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes and bounties. Are emergency airdrops, healing circles, illusions and viewer crates blocked? Does the block test the moment of purchase or the moment of landing? Status: `open`.

Why it matters ([U-0401](unknowns.md#u-0401)): Decides which viewer actions an EMP holder can stop and whether an in-flight healing circle or airdrop survives.

- [U-0401](unknowns.md#u-0401) reading A: only the eight listed attacks are refused; airdrop, healing circle, illusion and crates always go through
- [U-0401](unknowns.md#u-0401) reading B: all viewer actions are refused while an EMP is active, the list being illustrative
- [U-0401](unknowns.md#u-0401) reading C: the block tests the purchase moment only, and in-flight destruction applies to missiles, nukes, airstrikes, gunships only
- [U-0401](unknowns.md#u-0401) resolution: Items page EMP text (10 min) plus VOD of a viewer airdrop or healing circle sent during an EMP.

### U-0405

[U-0405](unknowns.md#u-0405): Tear gas and zombie-kill timing: does the 2 HP every 10s tick start 10s after entry, on entry, or on a cloud-global 10s phase, and are zombies killed instantly on entry or on a tick? Is a tick a 'hit' ([U-0002](unknowns.md#u-0002))? Status: `open`.

Why it matters ([U-0405](unknowns.md#u-0405)): Changes damage for a short crossing (a 9s pass costs 0 HP under entry-timers, 2 HP under global phase) and gas deaths of zombies.

- [U-0405](unknowns.md#u-0405) reading A: per-contestant timer: first loss 10s after entering, then every 10s
- [U-0405](unknowns.md#u-0405) reading B: first loss on entry, then every 10s
- [U-0405](unknowns.md#u-0405) reading C: cloud-global phase, any contestant inside at a tick loses 2 HP
- [U-0405](unknowns.md#u-0405) resolution: VOD: observe the event live with an on-screen timer.

### U-0408

[U-0408](unknowns.md#u-0408): Airstrike timeline: impact at 20s, then 'the strip then burns for 5min'. Does the fire last 5min from impact, is the first 1 HP tick at impact or 2s later, and does stepping into the strip during the fire cost HP? Is a fire tick a hit ([U-0002](unknowns.md#u-0002))? Status: `open`.

Why it matters ([U-0408](unknowns.md#u-0408)): Total fire damage inside the strip: up to 150 or 149 HP over 5min if standing in it, and whether entering late is punished.

- [U-0408](unknowns.md#u-0408) reading A: fire from t=20s to t=320s, first tick at 22s, entry anywhere in that window counts
- [U-0408](unknowns.md#u-0408) reading B: fire from t=20s to t=320s, first tick at 20s
- [U-0408](unknowns.md#u-0408) reading C: fire timer starts at purchase, so it ends at t=300s
- [U-0408](unknowns.md#u-0408) resolution: VOD: observe the event live with an on-screen timer.

### U-0410

[U-0410](unknowns.md#u-0410): Gunship bomb position and target circle: the circle 'sweeps around a random safe zone at 75m/s' (circle radius and path unstated). Does a bomb land where the circle was at the drop or where it is 5s later (75m/s x 5s = 375m away)? Status: `open`.

Why it matters ([U-0410](unknowns.md#u-0410)): Decides whether bombs are aimable and where contestants should stand.

- [U-0410](unknowns.md#u-0410) reading A: bomb lands at the circle position at the drop instant
- [U-0410](unknowns.md#u-0410) reading B: bomb lands at the circle position 5s later
- [U-0410](unknowns.md#u-0410) reading C: circle radius equals bomb blast radius 25m
- [U-0410](unknowns.md#u-0410) free parameter `gunship_circle_radius_m`, swept over 10 to 50 m; the wiki gives only the 25m bomb radius, the circle is not sized
- [U-0410](unknowns.md#u-0410) resolution: VOD of a gunship with the circle visible.

### U-0411

[U-0411](unknowns.md#u-0411): Care package Trolling rule: does the 3% roll apply to each package separately (including the 5 of an emergency airdrop, Endurance packages and merchant packages), is 'within 5m' the same as 'next to', and which Trolling contestant is chosen when several exist? Status: `open`.

Why it matters ([U-0411](unknowns.md#u-0411)): Sets expected Trolling income and defensive value of crates across all supply sources.

- [U-0411](unknowns.md#u-0411) reading A: independent 3% roll per viewer-sent package or crate, nearest or random Trolling contestant
- [U-0411](unknowns.md#u-0411) reading B: 3% roll for every care package, Endurance and merchant packages included
- [U-0411](unknowns.md#u-0411) reading C: roll only for single care packages, not for the 5 of the airdrop
- [U-0411](unknowns.md#u-0411) resolution: VOD: log where 100+ viewer packages land.
- [U-0411](unknowns.md#u-0411) resolution: Trolling page text (viewer crates).

### U-0413

[U-0413](unknowns.md#u-0413): Healing circle: is the 50m circle a radius or a diameter, is membership tested at +60s only or continuously, and does 25 HP heal above max HP? Does the heal count for Healing and Piety tokens? Status: `open`.

Why it matters ([U-0413](unknowns.md#u-0413)): Decides who benefits (a mover can leave before 60s) and the heal amount at full HP.

- [U-0413](unknowns.md#u-0413) reading A: radius 50m, members tested at t+60s, heal min(25, max-hp)
- [U-0413](unknowns.md#u-0413) reading B: diameter 50m (radius 25m), tested at t+60s
- [U-0413](unknowns.md#u-0413) reading C: membership tested continuously, heal on entry after 60s
- [U-0413](unknowns.md#u-0413) free parameter `healing_circle_radius_m`, swept over 25 to 50 m; the wiki gives '50m' as the only size
- [U-0413](unknowns.md#u-0413) resolution: VOD: observe the event live with an on-screen timer.

### U-0414

[U-0414](unknowns.md#u-0414): Illusion copies count: 'a copy of every living contestant' and, under 10 alive, 'several copies, up to 30 in total'. How many copies each, how are 30 shared, and at 10 or more is the total capped at 30? Status: `open`.

Why it matters ([U-0414](unknowns.md#u-0414)): Sets copy density and the odds that an attack hits a real contestant.

- [U-0414](unknowns.md#u-0414) reading A: copies each = floor(30/n) for n < 10, total 30 at most
- [U-0414](unknowns.md#u-0414) reading B: copies each = ceil(30/n), total capped to 30
- [U-0414](unknowns.md#u-0414) reading C: random split of exactly 30
- [U-0414](unknowns.md#u-0414) reading D: n >= 10: n copies uncapped; n >= 30 gives more than 30
- [U-0414](unknowns.md#u-0414) free parameter `illusion_total_cap`, swept over 10 to 40 copies; 30 is stated for fewer than 10 contestants, the n>=10 case is not capped by the wiki
- [U-0414](unknowns.md#u-0414) resolution: VOD: observe the event live with an on-screen timer.

### U-0419

[U-0419](unknowns.md#u-0419): Cyclops blood tokens: '1 blood token per damage dealt' when it dies. Is damage counted with overkill capped at its 200 HP, are merchant missiles 'viewer items', and does a zone kill still pay nothing if contestants dealt damage earlier? Status: `open`.

Why it matters ([U-0419](unknowns.md#u-0419)): Cyclops is a major token source; the total is bounded by 200 or unbounded by overkill.

- [U-0419](unknowns.md#u-0419) reading A: payout = actual HP removed (<= 200 total); merchant missiles count
- [U-0419](unknowns.md#u-0419) reading B: payout counts raw damage including overkill
- [U-0419](unknowns.md#u-0419) reading C: merchant missiles count as viewer items and earn nothing
- [U-0419](unknowns.md#u-0419) resolution: VOD of a cyclops kill with the token log.

### U-0420

[U-0420](unknowns.md#u-0420): Cyclops attack timing and target: 'Every 5s it hits the nearest contestant within 30m for 10 HP'. First hit at spawn+5s or when a target first enters range; tie breaks; does it pass the damage pipeline ([U-0002](unknowns.md#u-0002))? Status: `open`.

Why it matters ([U-0420](unknowns.md#u-0420)): Damage to a contestant standing near the cyclops: 10 HP / 5s = 2 HP/s.

- [U-0420](unknowns.md#u-0420) reading A: global 5s timer from spawn, hit if a contestant is in range
- [U-0420](unknowns.md#u-0420) reading B: timer starts when a contestant enters range
- [U-0420](unknowns.md#u-0420) reading C: hit goes through the 7-step pipeline
- [U-0420](unknowns.md#u-0420) resolution: VOD: observe the event live with an on-screen timer.

### U-0424

[U-0424](unknowns.md#u-0424): Zombie targeting: 'nearest valid contestant, at any distance'. What makes a contestant valid (alive, not immune, not repellent, not Necromancy), how often is the nearest re-evaluated, and do zombies path through terrain? Status: `open`.

Why it matters ([U-0424](unknowns.md#u-0424)): Determines whether zombies are a hard pursuer.

- [U-0424](unknowns.md#u-0424) reading A: valid = alive and not currently immune to zombies, nearest re-evaluated each tick
- [U-0424](unknowns.md#u-0424) reading B: valid = alive only; immunity applies at drain time
- [U-0424](unknowns.md#u-0424) resolution: VOD: observe the event live with an on-screen timer.

### U-0426

[U-0426](unknowns.md#u-0426): Potion break roll: '10% chance to break one of your health potions'. Per drain tick, per encounter or per zombie? Which potion is broken, and is a roll made when no potion is held or when drain is blocked? Status: `open`.

Why it matters ([U-0426](unknowns.md#u-0426)): A per-tick roll would break about one potion per 100s next to a zombie; per encounter far fewer.

- [U-0426](unknowns.md#u-0426) reading A: one roll per drain tick per zombie
- [U-0426](unknowns.md#u-0426) reading B: one roll per zombie per contestant (first contact)
- [U-0426](unknowns.md#u-0426) reading C: one roll per drain event only when HP is actually lost
- [U-0426](unknowns.md#u-0426) resolution: VOD: observe the event live with an on-screen timer.

### U-0427

[U-0427](unknowns.md#u-0427): Craft destruction roll: '40% chance to destroy crafted items' (the Ingenuity page says 'unique crafts' and 'Zombie hits'). Per drain tick or encounter, one item or all crafts, and are non-unique crafts included? Status: `open`.

Why it matters ([U-0427](unknowns.md#u-0427)): Decides whether Ingenuity crafts survive zombie contact.

- [U-0427](unknowns.md#u-0427) reading A: per drain tick, one random craft
- [U-0427](unknowns.md#u-0427) reading B: per encounter, one random craft
- [U-0427](unknowns.md#u-0427) reading C: per tick, every craft rolls independently
- [U-0427](unknowns.md#u-0427) resolution: VOD: observe the event live with an on-screen timer.

### U-0429

[U-0429](unknowns.md#u-0429): Guard zombie: does a guard zombie stay at its spawn point or chase, is one appearing per Necromancy contestant or per death, does it also drain its owner and the dead, and does it live 1h (Necromancy page) as stated only there? Status: `open`.

Why it matters ([U-0429](unknowns.md#u-0429)): Guard zombies drain 2 HP/5s (0.4 HP/s) up to 30 HP: 75s for a full cap.

- [U-0429](unknowns.md#u-0429) reading A: stationary for 1h, drains non-Necromancy contestants within 10m
- [U-0429](unknowns.md#u-0429) reading B: chases like a normal zombie
- [U-0429](unknowns.md#u-0429) reading C: one per death regardless of Necromancy count
- [U-0429](unknowns.md#u-0429) resolution: VOD: observe the event live with an on-screen timer.

### U-0432

[U-0432](unknowns.md#u-0432): Viewer attack concurrency: no limit is stated for missiles, nukes, hordes, tear gas, airstrikes, gunships, bounties and healing circles (only cyclops and illusion are limited to one). Are they stackable at will? Status: `open`.

Why it matters ([U-0432](unknowns.md#u-0432)): Unbounded stacking would make total damage price-limited only ([U-0014](unknowns.md#u-0014)).

- [U-0432](unknowns.md#u-0432) reading A: stackable without limit, bounded by Cx-Bucks
- [U-0432](unknowns.md#u-0432) reading B: undisclosed per-type limits
- [U-0432](unknowns.md#u-0432) resolution: Shop page and VOD.

### U-0503

[U-0503](unknowns.md#u-0503): Piety 'heal you 15% more, rounded down': what is rounded, and at which step relative to the max-HP clamp? Status: `open`.

Why it matters ([U-0503](unknowns.md#u-0503)): The four potion tiers give the same totals under exact arithmetic and under binary64 (5, 11, 23, 46), so the open part is the order of operations at the HP cap and the base value used.

- [U-0503](unknowns.md#u-0503) reading A: heal = floor(1.15 * h) with h the tier value, then clamped by missing HP
- [U-0503](unknowns.md#u-0503) reading B: heal = h + floor(0.15 * h), then clamped (equal to A for every integer h)
- [U-0503](unknowns.md#u-0503) reading C: heal = floor(1.15 * min(h, missing HP)): bonus applied to the effective heal
- [U-0503](unknowns.md#u-0503) resolution: VOD: Piety contestant 1 to 10 HP below max drinking a medium potion.
- [U-0503](unknowns.md#u-0503) resolution: VOD: HP readout after drinking each tier from low HP (expect +5, +11, +23, +46).

### U-0505

[U-0505](unknowns.md#u-0505): Piety chest conversion scope: do only 'item chests' and crates convert, or do other care packages (airdrop, admin, viewer, Endurance) also turn into potions? Status: `open`.

Why it matters ([U-0505](unknowns.md#u-0505)): Only merchant care packages are named as unchanged; the text is silent on every other care package, which are a large share of loot.

- [U-0505](unknowns.md#u-0505) reading A: only item chests and crates convert; every care package is unchanged (the merchant sentence is a clarification)
- [U-0505](unknowns.md#u-0505) reading B: item chests, crates and all care packages convert except merchant ones
- [U-0505](unknowns.md#u-0505) resolution: VOD: Piety contestant claiming a viewer or airdrop care package.
- [U-0505](unknowns.md#u-0505) resolution: Organizer statement.

### U-0508

[U-0508](unknowns.md#u-0508): Greed timers: does the 30 min cooldown start at any steal attempt or only at a successful steal, and is the 24 h per-victim window anchored at the last payout (rolling) or at a daily clock? Status: `open`.

Why it matters ([U-0508](unknowns.md#u-0508)): A failed steal (fortress, Piety victim, empty inventory) either costs 30 min or nothing; a daily clock allows two payouts in a short span around the reset.

- [U-0508](unknowns.md#u-0508) reading A: cooldown starts on any use of Steal; the 24 h window is rolling from the last payout for that victim
- [U-0508](unknowns.md#u-0508) reading B: cooldown starts only on a successful steal; rolling 24 h window
- [U-0508](unknowns.md#u-0508) reading C: as A or B but the 24 h window resets at a fixed daily time
- [U-0508](unknowns.md#u-0508) resolution: VOD: a Greed contestant using Steal on a fortress-protected or Piety target, then retrying.

### U-0511

[U-0511](unknowns.md#u-0511): Greed chest Shield: what happens when the contestant already has an active Shield (item or earlier chest Shield)? Status: `open`.

Why it matters ([U-0511](unknowns.md#u-0511)): Decides whether repeated chest claims extend protection and how long a Greed contestant can stay immune; the wiki also says the chest Shield is not counted toward the 3-effect limit.

- [U-0511](unknowns.md#u-0511) reading A: new Shield refreshes the timer to 20 min
- [U-0511](unknowns.md#u-0511) reading B: new Shield adds 20 min to the remaining time
- [U-0511](unknowns.md#u-0511) reading C: new roll ignored while a Shield is active
- [U-0511](unknowns.md#u-0511) reading D: independent Shields coexist
- [U-0511](unknowns.md#u-0511) resolution: VOD: a Greed contestant claiming a second chest while shielded.

### U-0513

[U-0513](unknowns.md#u-0513): Ingenuity 'Recognize fake chests and gravestones, see traps, and hack landmines or C4 within 50m (164ft)': does the 50 m limit apply to all three abilities or only to hacking? Status: `open`.

Why it matters ([U-0513](unknowns.md#u-0513)): Scope of fake detection decides how much of the map an Ingenuity contestant sees through Trolling traps.

- [U-0513](unknowns.md#u-0513) reading A: all three abilities work only within 50 m
- [U-0513](unknowns.md#u-0513) reading B: only hacking is limited to 50 m; recognizing fakes and seeing traps has no stated range
- [U-0513](unknowns.md#u-0513) reading C: recognizing and seeing are map-wide for the owner, hacking within 50 m
- [U-0513](unknowns.md#u-0513) free parameter `ingenuity_detect_radius_m`, swept over 50 m (as written) up to map-wide; the lower bound is the literal 50 m
- [U-0513](unknowns.md#u-0513) resolution: VOD: an Ingenuity contestant's map at various distances from a fake chest.

### U-0516

[U-0516](unknowns.md#u-0516): Trapped gift: is the 16 h limit shared between landmine and C4 attachments, and who can see the trap (the owner only, or also other Ingenuity contestants)? Status: `open`.

Why it matters ([U-0516](unknowns.md#u-0516)): The Ingenuity page says 'once every 16h' for the pair; the C4 and Landmine pages repeat it for each, and one line says 'Only you and Sigil of Ingenuity contestants can see it'.

- [U-0516](unknowns.md#u-0516) reading A: one shared cooldown of 16 h for any attachment
- [U-0516](unknowns.md#u-0516) reading B: separate 16 h cooldowns for C4 and for landmine attachments
- [U-0516](unknowns.md#u-0516) reading C: visibility: only the owner sees the trap
- [U-0516](unknowns.md#u-0516) reading D: visibility: the owner and every Ingenuity contestant see it
- [U-0516](unknowns.md#u-0516) resolution: VOD: an Ingenuity contestant attaching a landmine then a C4 within 16 h.
- [U-0516](unknowns.md#u-0516) resolution: VOD: a second Ingenuity contestant inspecting a trapped gift.

### U-0519

[U-0519](unknowns.md#u-0519): Ingenuity income: what counts as 'craft, hack, chest destroyed by Black Hole, HP your Campfire heals on anyone, or zombie killed'? Status: `open`.

Why it matters ([U-0519](unknowns.md#u-0519)): Crates, care packages, airdrops and fake chests are also destroyed by the Black Hole but only 'chest' is written; 'zombie killed' does not say whose kill; Campfire HP could be nominal or effective.

- [U-0519](unknowns.md#u-0519) reading A: zombie killed = any zombie killed by the contestant's Zombie killer; chests = real item chests only; Campfire HP = effective HP restored (full-HP bystanders pay nothing)
- [U-0519](unknowns.md#u-0519) reading B: zombie killed = any zombie the contestant kills by any means; chests = every chest, crate, care package and fake chest the Black Hole destroys; Campfire HP = pool consumed
- [U-0519](unknowns.md#u-0519) reading C: mixed per item
- [U-0519](unknowns.md#u-0519) resolution: VOD: token counter of an Ingenuity contestant after a Black Hole near several containers.

### U-0522

[U-0522](unknowns.md#u-0522): Zombie killer 'Kills the next ten zombies that come within 10m': does it kill zombies already inside 10 m when used, which zombie types count, and are more than ten in range handled? Status: `open`.

Why it matters ([U-0522](unknowns.md#u-0522)): Decides whether the craft protects against a horde (50 zombies) or only ten arrivals; also whether guard zombies and hordes count.

- [U-0522](unknowns.md#u-0522) reading A: kills the first ten zombies (any type) that enter or are inside 10 m, one per instant of arrival
- [U-0522](unknowns.md#u-0522) reading B: only zombies that enter 10 m after use; those already inside are not counted
- [U-0522](unknowns.md#u-0522) reading C: guard zombies and horde zombies are excluded
- [U-0522](unknowns.md#u-0522) resolution: VOD: using the craft inside a horde.

### U-0523

[U-0523](unknowns.md#u-0523): Black hole: is it instant or does it persist, centered where, and who gets the benefit? Status: `open`.

Why it matters ([U-0523](unknowns.md#u-0523)): 'Destroys every chest and crate within 200m' reads as a one-shot at activation; a lingering field would also destroy chests spawning later.

- [U-0523](unknowns.md#u-0523) reading A: one-shot at the place where it is used, radius 200 m
- [U-0523](unknowns.md#u-0523) reading B: persistent field for an unstated duration
- [U-0523](unknowns.md#u-0523) reading C: centered on the contestant at use
- [U-0523](unknowns.md#u-0523) free parameter `black_hole_duration_s`, swept over 0 (instant, as written) to 600 s: ten minutes matches the longest stated timers of the other crafts (Robot, Campfire)
- [U-0523](unknowns.md#u-0523) resolution: VOD: Black hole use followed by new chest spawns.

### U-0527

[U-0527](unknowns.md#u-0527): Robot 'deals 1 HP every 2s to other players within 10m': is the 2 s clock global or per target, and does the first hit come immediately or after one interval? Status: `open`.

Why it matters ([U-0527](unknowns.md#u-0527)): Changes total damage for fast passers-by and whether a target that stays only 1 s is hit at all.

- [U-0527](unknowns.md#u-0527) reading A: global 2 s clock: each tick hits everyone in range at that instant
- [U-0527](unknowns.md#u-0527) reading B: per-target timer, first hit one interval (2 s) after the target enters range (like the unsafe circle)
- [U-0527](unknowns.md#u-0527) reading C: per-target, first hit immediately at entry and then every 2 s
- [U-0527](unknowns.md#u-0527) resolution: VOD: a contestant walking past a robot.

### U-0530

[U-0530](unknowns.md#u-0530): Fake chest 'up to 2 per rolling hour': sliding window over placement times, or two charges that refill? Status: `open`.

Why it matters ([U-0530](unknowns.md#u-0530)): Changes the maximum fake chest placement rate: a sliding window never allows a third within 60 min; a token bucket allows 2 immediately then 1 per 30 min.

- [U-0530](unknowns.md#u-0530) reading A: at most 2 placements in any 60 min window (sliding)
- [U-0530](unknowns.md#u-0530) reading B: 2 charges, one regained every 30 min
- [U-0530](unknowns.md#u-0530) reading C: 2 per clock hour (fixed window), contrary to the word rolling
- [U-0530](unknowns.md#u-0530) resolution: VOD: Trolling contestant placing fake chests at 0, 10 and 40 min.

### U-0531

[U-0531](unknowns.md#u-0531): Fake chest lockout 'cannot claim chests for 1h': does it block care packages and crates too, does a second claim extend it, and do blockers other than a Shield (Safety bubble, Sleeping Bag, Body armor) also leave it standing? Status: `open`.

Why it matters ([U-0531](unknowns.md#u-0531)): The fake chest looks like a care package; the lockout protects the troll's items only if it covers what the victim would claim next.

- [U-0531](unknowns.md#u-0531) reading A: lockout covers item chests only; a second claim of a fake chest during lockout is not possible
- [U-0531](unknowns.md#u-0531) reading B: lockout covers chests, care packages and crates
- [U-0531](unknowns.md#u-0531) reading C: every blocker that stops the 5 HP leaves the lockout (damage and lockout are separate effects)
- [U-0531](unknowns.md#u-0531) reading D: only a Shield is stated to leave it; other blockers are unspecified
- [U-0531](unknowns.md#u-0531) resolution: VOD: a victim claiming a fake chest, then a care package within 1 h.

### U-0532

[U-0532](unknowns.md#u-0532): Trolling fake chest 'You heal 5 HP': fixed 5 HP at claim time, or the damage that actually landed, and does it happen when the victim is protected or the chest is reflected? Status: `open`.

Why it matters ([U-0532](unknowns.md#u-0532)): Decides whether a Shield, Safety bubble or Mirror denies the troll the heal, and whether a Kick-reduced hit heals 4 or 5.

- [U-0532](unknowns.md#u-0532) reading A: heal 5 HP whenever the chest is claimed, regardless of protection
- [U-0532](unknowns.md#u-0532) reading B: heal equals the damage the victim lost
- [U-0532](unknowns.md#u-0532) reading C: heal only when the damage was not blocked; a reflected chest heals nobody
- [U-0532](unknowns.md#u-0532) resolution: VOD: troll HP before and after a claim by a shielded victim.

### U-0533

[U-0533](unknowns.md#u-0533): Fake gravestone: how long does it last, and does the 2 h wait start at placement or when the previous one disappears? Status: `open`.

Why it matters ([U-0533](unknowns.md#u-0533)): The page gives no lifetime for the fake gravestone; the 2 h cooldown or 'wait' could run from placement or from the removal.

- [U-0533](unknowns.md#u-0533) reading A: 2 h from placement; lifetime unlimited until looted
- [U-0533](unknowns.md#u-0533) reading B: 2 h from the moment the previous fake gravestone is gone
- [U-0533](unknowns.md#u-0533) reading C: 2 h from placement; lifetime shorter than 2 h
- [U-0533](unknowns.md#u-0533) free parameter `fake_gravestone_lifetime_s`, swept over 600 s to the event length: below 600 s it would vanish before anyone loots it, the upper bound is permanent
- [U-0533](unknowns.md#u-0533) resolution: VOD: a fake gravestone observed for hours.

### U-0539

[U-0539](unknowns.md#u-0539): Unsafe circle item loss: is the lost item destroyed or dropped, does 'not immune' pause the clock or just skip the loss, and are active effects (not inventory) affected? Status: `open`.

Why it matters ([U-0539](unknowns.md#u-0539)): Dropped items can be looted by the troll; destroyed items are gone. Immunity by Guardian angel, Safety bubble, Reality Shield or Death Ward stops both damage and loss.

- [U-0539](unknowns.md#u-0539) reading A: destroyed, inventory items and unique crafts only
- [U-0539](unknowns.md#u-0539) reading B: dropped at the contestant's feet
- [U-0539](unknowns.md#u-0539) reading C: destroyed, and active effects (a running Shield, a worn Hazmat suit) are removed too
- [U-0539](unknowns.md#u-0539) reading D: clock keeps running while immune, the loss is skipped; or clock pauses while immune
- [U-0539](unknowns.md#u-0539) resolution: VOD: contestant losing items in an unsafe circle.

### U-0540

[U-0540](unknowns.md#u-0540): Trolling care package diversion '3% chance to land next to a Trolling contestant': which packages roll, how is the contestant chosen with several Trolling contestants, and is the draw once per package? Status: `open`.

Why it matters ([U-0540](unknowns.md#u-0540)): The Trolling page says crates and care packages from viewers; the attacks page says only care packages (any care package), landing within 5 m. With N Trolling contestants the chance of a diversion may be 3% total or 3% each.

- [U-0540](unknowns.md#u-0540) reading A: every care package rolls once (3%); on success a Trolling contestant is chosen uniformly; crates are not affected
- [U-0540](unknowns.md#u-0540) reading B: crates and care packages bought by viewers roll once each (3%)
- [U-0540](unknowns.md#u-0540) reading C: each Trolling contestant rolls independently, 3% each, per package
- [U-0540](unknowns.md#u-0540) resolution: VOD: tally of care package landing points over many drops.
- [U-0540](unknowns.md#u-0540) resolution: Organizer statement.

### U-0600

[U-0600](unknowns.md#u-0600): Death gravestone rob heal: 5% of max HP, how is a fractional result rounded (max HP is 100 at base but the merchant sells +10 max HP steps, so 5% of 110 is 5.5)? Status: `open`.

Why it matters ([U-0600](unknowns.md#u-0600)): Changes every rob heal by up to 1 HP once max HP is not a multiple of 20; matters for Death sustain.

- [U-0600](unknowns.md#u-0600) reading A: heal = floor(M*5/100)
- [U-0600](unknowns.md#u-0600) reading B: heal = ceil(M*5/100)
- [U-0600](unknowns.md#u-0600) reading C: heal = round half up of M*5/100
- [U-0600](unknowns.md#u-0600) reading D: fractional HP kept exactly
- [U-0600](unknowns.md#u-0600) resolution: VOD: Death contestant with 110 max HP robbing a gravestone shows +5 (A), +6 (B or C) or +5.5 (D).

### U-0605

[U-0605](unknowns.md#u-0605): Death sigil '1 blood token whenever another contestant dies': is there a distance limit (heal uses 50m), and does a revive or second death pay again? Status: `open`.

Why it matters ([U-0605](unknowns.md#u-0605)): Sets Death blood-token income, which funds merchant purchases.

- [U-0605](unknowns.md#u-0605) reading A: any death anywhere in the arena
- [U-0605](unknowns.md#u-0605) reading B: only deaths within 50m of the Death contestant
- [U-0605](unknowns.md#u-0605) reading C: A or B, and a contestant who dies again after a revive pays again
- [U-0605](unknowns.md#u-0605) resolution: VOD: Death contestant's blood token counter after a distant death.

### U-0608

[U-0608](unknowns.md#u-0608): Endurance 'Earn one more for every five item uses': when is the extra token paid? Status: `open`.

Why it matters ([U-0608](unknowns.md#u-0608)): Changes the Endurance token rate (up to one token per five uses versus one token per claimed package).

- [U-0608](unknowns.md#u-0608) reading A: +1 token immediately on every 5th item use (cumulative counter)
- [U-0608](unknowns.md#u-0608) reading B: floor(uses since last claim / 5) added to the next care package claim
- [U-0608](unknowns.md#u-0608) reading C: +1 token on each care package claim at most, when five uses occurred since the last claim
- [U-0608](unknowns.md#u-0608) resolution: VOD: Endurance token counter on the fifth item use.

### U-0609

[U-0609](unknowns.md#u-0609): Endurance item use bonus: which actions are an 'item use' (weapon shots, bandages, Safety bubbles, crafts, merchant upgrades, effects that stay active)? Status: `open`.

Why it matters ([U-0609](unknowns.md#u-0609)): Determines how fast the counter of [U-0608](unknowns.md#u-0608) advances.

- [U-0609](unknowns.md#u-0609) reading A: every consumed or activated inventory item, as in the active-item-effects rule
- [U-0609](unknowns.md#u-0609) reading B: A minus the exclusions listed in the items page (Safety Bubbles, smoke bombs, bandages, crafts, merchant upgrades)
- [U-0609](unknowns.md#u-0609) reading C: also weapon attacks such as bow shots
- [U-0609](unknowns.md#u-0609) resolution: VOD: counter movement after each action type.

### U-0610

[U-0610](unknowns.md#u-0610): Endurance 'cannot trade, loot gravestones, drop items or pick up dropped items': does trade ban cover receiving offers from others, giving gifts, and the items returned by a revive? Status: `open`.

Why it matters ([U-0610](unknowns.md#u-0610)): Shows how isolated an Endurance contestant really is, and whether a teammate can pass items to them.

- [U-0610](unknowns.md#u-0610) reading A: only actions the Endurance contestant starts are blocked
- [U-0610](unknowns.md#u-0610) reading B: any trade involving them is blocked, including offers from others
- [U-0610](unknowns.md#u-0610) reading C: as B, and items restored from their own gravestone on a revive are also refused
- [U-0610](unknowns.md#u-0610) resolution: VOD: another contestant sending a trade request to an Endurance contestant.

### U-0611

[U-0611](unknowns.md#u-0611): Necromancy summon 'up to 3 times every 6h': rolling window, fixed 6h blocks, or three charges refilled on a timer? Status: `open`.

Why it matters ([U-0611](unknowns.md#u-0611)): Bounds zombies per hour and blood tokens from summons.

- [U-0611](unknowns.md#u-0611) reading A: rolling: at most 3 summons in any 6h interval
- [U-0611](unknowns.md#u-0611) reading B: fixed blocks: counter resets at multiples of 6h from event start
- [U-0611](unknowns.md#u-0611) reading C: counter resets 6h after the first summon of each batch
- [U-0611](unknowns.md#u-0611) reading D: one charge refills every 2h
- [U-0611](unknowns.md#u-0611) resolution: VOD: summon attempts at a 4th use inside and just outside 6h from the first.

### U-0614

[U-0614](unknowns.md#u-0614): Do guard zombies and horde-bonus zombies drain HP to their Necromancy owner and count in 'one per HP your zombies drain'? Status: `open`.

Why it matters ([U-0614](unknowns.md#u-0614)): Guard zombies could be a large part of the drain, or only a zone-control tool.

- [U-0614](unknowns.md#u-0614) reading A: all zombies of the owner (summoned, death, horde bonus, guard) feed HP and tokens
- [U-0614](unknowns.md#u-0614) reading B: only summoned, death and horde-bonus zombies feed; guard zombies drain without feeding
- [U-0614](unknowns.md#u-0614) resolution: VOD: owner HP and tokens while a victim stands near a guard zombie.

### U-0615

[U-0615](unknowns.md#u-0615): Guard zombie 'up to 30 HP per contestant': per guard zombie, or shared across all guard zombies on the same contestant? Does it stand still all hour? Status: `open`.

Why it matters ([U-0615](unknowns.md#u-0615)): Several deaths near one gravestone could stack guards; the cap decides whether guards multiply the total.

- [U-0615](unknowns.md#u-0615) reading A: 30 HP cap per guard zombie per contestant (like the ordinary zombie rule)
- [U-0615](unknowns.md#u-0615) reading B: 30 HP cap per contestant over all guard zombies
- [U-0615](unknowns.md#u-0615) reading C: A, and a guard that has hit its cap on a contestant stops draining them only
- [U-0615](unknowns.md#u-0615) resolution: VOD: contestant standing between two guard zombies.

### U-0616

[U-0616](unknowns.md#u-0616): Necromancy 'Fully immune from zombies': does it cover horde and guard zombies of other Necromancy contestants, and also the 10% potion break and 40% craft destruction? Status: `open`.

Why it matters ([U-0616](unknowns.md#u-0616)): Decides whether a Necromancy contestant can cross a horde safely.

- [U-0616](unknowns.md#u-0616) reading A: immune to all zombie effects (drain, potion breaking, craft destruction) from every zombie
- [U-0616](unknowns.md#u-0616) reading B: immune to drain only; other zombie effects can still hit
- [U-0616](unknowns.md#u-0616) reading C: immune to drain from every zombie, but not to a zombie landmine trigger
- [U-0616](unknowns.md#u-0616) resolution: VOD: Necromancy contestant inside a horde with a health potion.

### U-0619

[U-0619](unknowns.md#u-0619): Protection 'Bandages last 1.1x as long': same total heal over a longer time, or same rate over a longer time? Status: `open`.

Why it matters ([U-0619](unknowns.md#u-0619)): Either 10 HP over 132 s, or 11 HP over 132 s.

- [U-0619](unknowns.md#u-0619) reading A: duration = 132 s, total stays 10 HP (rate drops)
- [U-0619](unknowns.md#u-0619) reading B: duration = 132 s at the same HP per second, total 11 HP
- [U-0619](unknowns.md#u-0619) reading C: duration rounds to a tick grid of the bandage
- [U-0619](unknowns.md#u-0619) resolution: VOD: Protection contestant bandage HP gain total.

### U-0620

[U-0620](unknowns.md#u-0620): Protection blood tokens from blocked hits: do airstrike fire ticks, a landmine of its own, and the unlisted immunities (trapped gift, poison, retribution) pay tokens? Status: `open`.

Why it matters ([U-0620](unknowns.md#u-0620)): Sets Protection blood-token income and whether viewers farm tokens for it.

- [U-0620](unknowns.md#u-0620) reading A: one token per airstrike impact or gunship bomb only; poison, trapped gift, retribution and the sigil's own landmine pay nothing
- [U-0620](unknowns.md#u-0620) reading B: A plus one token per fire tick
- [U-0620](unknowns.md#u-0620) reading C: every immunity pays one token except where 'already blocked' applies
- [U-0620](unknowns.md#u-0620) resolution: VOD: Protection contestant under an airstrike fire.

### U-0621

[U-0621](unknowns.md#u-0621): Protection landmine ability: ready at the sigil pick or after 2h, does the 2h start at placement, and is it the item Landmine (stack of 5, Kick live bonus, enchant, visibility)? Status: `open`.

Why it matters ([U-0621](unknowns.md#u-0621)): Sets how many free landmines Protection can lay and how they interact with item rules.

- [U-0621](unknowns.md#u-0621) reading A: ready at pick; cooldown starts at placement; ordinary landmine item rules apply otherwise
- [U-0621](unknowns.md#u-0621) reading B: first landmine 2h after the pick
- [U-0621](unknowns.md#u-0621) reading C: ability landmine has its own rules and gets no Kick live bonus
- [U-0621](unknowns.md#u-0621) resolution: VOD: Protection contestant placing landmines.

### U-0622

[U-0622](unknowns.md#u-0622): Healing ability 'Heal a nearby contestant': what is the range? Status: `open`.

Why it matters ([U-0622](unknowns.md#u-0622)): Range sets how close a healer must stand.

- [U-0622](unknowns.md#u-0622) free parameter `healing_ability_range_m`, swept over 1 to 50 m: 1 m as the closest meaningful contact, 50 m matching the largest sigil range stated (Death heal, Necromancy guard trigger); 5 m and 10 m are the other stated ranges.
- [U-0622](unknowns.md#u-0622) resolution: VOD: healer and target at measured distances.

### U-0623

[U-0623](unknowns.md#u-0623): Healing ability: can it target the healer, an already full HP target, a non-poisoned target? Is the cooldown and token spent anyway? Status: `open`.

Why it matters ([U-0623](unknowns.md#u-0623)): Decides whether the blood token per heal can be farmed and how the 10min cooldown behaves.

- [U-0623](unknowns.md#u-0623) reading A: targets must be others; any target; token and cooldown spent whatever the effect
- [U-0623](unknowns.md#u-0623) reading B: target must benefit (HP below max or poisoned or bleeding); cooldown and token spent only then
- [U-0623](unknowns.md#u-0623) reading C: A but self allowed
- [U-0623](unknowns.md#u-0623) resolution: VOD: healer using the ability on a full HP target.

### U-0626

[U-0626](unknowns.md#u-0626): Range for a Healing contestant to revive a non-Healing contestant: the Healing page gives 10m of the gravestone only when a Healing contestant is the one revived. Status: `open`.

Why it matters ([U-0626](unknowns.md#u-0626)): Needed for any revive-race model.

- [U-0626](unknowns.md#u-0626) free parameter `revive_range_other_m`, swept over 1 to 30 m: 1 m minimum contact, 30 m above the longest comparable range stated (10m).
- [U-0626](unknowns.md#u-0626) resolution: VOD: revive at measured distances.

### U-0627

[U-0627](unknowns.md#u-0627): Sigil pick: is there a deadline after the event start, and what applies to a contestant who has not picked (base stats, no ability)? Status: `open`.

Why it matters ([U-0627](unknowns.md#u-0627)): Delay costs the sigil's passive timers and abilities; no pick may leave a contestant without sigil effects.

- [U-0627](unknowns.md#u-0627) free parameter `sigil_pick_deadline_s`, swept over 0 to the event duration ([U-0009](unknowns.md#u-0009)): 0 means the pick is already done at the event start, the upper bound is the longest possible delay.
- [U-0627](unknowns.md#u-0627) resolution: Organizer statement; VOD of the pick screen.

## Priority: low

### U-0013

[U-0013](unknowns.md#u-0013): Do events/safe-zone/ assets belong to a previous edition with different rules? Status: `resolved`.

Why it matters ([U-0013](unknowns.md#u-0013)): Would identify reused versus new content.

- [U-0013](unknowns.md#u-0013) resolution: RE-0002, corpus/diffs/
- [U-0013](unknowns.md#u-0013) resolved: Yes, the October 2026 Austin edition (RE-0002, RE-0005). Irrelevant to the rule model: only the 2026-11-11 snapshot is a rule source (project owner decision, 2026-11-11).

### U-0100

[U-0100](unknowns.md#u-0100): Where does 'The damage left is rounded down' apply in step 4: to the Protection 50% result only, or as one final floor after all reductions, with the Kick 10% computed on the unrounded value? Status: `open`.

Why it matters ([U-0100](unknowns.md#u-0100)): Changes odd damages when a Protection contestant who is live on Kick takes a nuke: intermediate floor then Kick, versus Kick on the exact half.

- [U-0100](unknowns.md#u-0100) reading A: x -> floor(x/2), then the Kick reduction ([U-0001](unknowns.md#u-0001) reading) applied to that integer
- [U-0100](unknowns.md#u-0100) reading B: x -> floor(0.9*(x/2)) with one final floor (Kick percentage applied to the exact half)
- [U-0100](unknowns.md#u-0100) resolution: VOD: a live Protection contestant taking a nuke of odd base damage, read the HP drop.
- [U-0100](unknowns.md#u-0100) resolution: REA: damage formula in shipped code.

### U-0109

[U-0109](unknowns.md#u-0109): 'Items that do not fit stay in the gravestone': what is the capacity rule at revival, and what happens later to items left in the grave? Status: `open`.

Why it matters ([U-0109](unknowns.md#u-0109)): Decides how much of an inventory survives death and whether leftover items remain lootable.

- [U-0109](unknowns.md#u-0109) reading A: capacity is the normal carry limits per category; leftovers stay lootable by anyone
- [U-0109](unknowns.md#u-0109) reading B: leftovers stay in the grave but are locked like blood tokens for the window only
- [U-0109](unknowns.md#u-0109) free parameter `inventory_capacity`, swept over 0 to 12 slots across all categories; the upper bound is a sweep choice above any carry set seen on the items page, not a wiki value
- [U-0109](unknowns.md#u-0109) resolution: VOD: a revival of a contestant who picked up new items between death and revival.
- [U-0109](unknowns.md#u-0109) resolution: Items page carry limits read against this rule (cross-family).

### U-0118

[U-0118](unknowns.md#u-0118): 'Sleeping in your own Sleeping Bag' appears as a label in the Poison immunity list with no verb: does it prevent new poison, block each step, or both? Status: `open`.

Why it matters ([U-0118](unknowns.md#u-0118)): The label's meaning changes whether a sleeper can be poisoned at all (a dart still poisons, steps blocked), see the damage table row listing Sleeping Bag against Poison.

- [U-0118](unknowns.md#u-0118) reading A: no new poison while sleeping in own bag (like Anti poison)
- [U-0118](unknowns.md#u-0118) reading B: existing and new poison steps are blocked while sleeping (like Shield)
- [U-0118](unknowns.md#u-0118) reading C: both
- [U-0118](unknowns.md#u-0118) resolution: VOD: Poison Dart on a sleeping contestant.

### U-0121

[U-0121](unknowns.md#u-0121): Self-inflicted hits ('hit by your own C4 and landmine'): does the full pipeline run with attacker = defender, including Kick bonus (step 2) and Kick reduction (step 4), and do own-held blockers (Protection, Shield) apply? Status: `open`.

Why it matters ([U-0121](unknowns.md#u-0121)): Decides the real cost of detonating near yourself.

- [U-0121](unknowns.md#u-0121) reading A: full pipeline, attacker bonus and defender reduction both apply, Mirror skipped (never your own explosives)
- [U-0121](unknowns.md#u-0121) reading B: no Kick bonus on self hits
- [U-0121](unknowns.md#u-0121) reading C: own-held Protection or Shield makes it harmless
- [U-0121](unknowns.md#u-0121) resolution: VOD: self-detonation by a live contestant.

### U-0124

[U-0124](unknowns.md#u-0124): Gravestone location 'where you were last seen': position at the moment of death or the last received GPS fix? Status: `open`.

Why it matters ([U-0124](unknowns.md#u-0124)): Matters for deaths with no GPS (offline) and for the 10 m style ranges of looters.

- [U-0124](unknowns.md#u-0124) reading A: position at death
- [U-0124](unknowns.md#u-0124) reading B: last GPS fix received before death
- [U-0124](unknowns.md#u-0124) resolution: VOD: death of an offline contestant.

### U-0204

[U-0204](unknowns.md#u-0204): How are Eddie's potion 50% heal and 30% loss rounded when max HP is not a multiple of 10? Status: `open`.

Why it matters ([U-0204](unknowns.md#u-0204)): Off-by-one on a gamble that can kill; also tie to which base max HP exists.

- [U-0204](unknowns.md#u-0204) reading A: floor for both
- [U-0204](unknowns.md#u-0204) reading B: ceil for both
- [U-0204](unknowns.md#u-0204) reading C: round half up for both
- [U-0204](unknowns.md#u-0204) reading D: heal and loss use different roundings
- [U-0204](unknowns.md#u-0204) free parameter `eddie_rounding`, swept over floor, ceil, round half up applied to heal and loss separately (4 to 9 combos); max HP 90..110 in steps of 1 because sigils change max HP by 10 from an unknown base
- [U-0204](unknowns.md#u-0204) resolution: VOD: a contestant at max HP 95 or 105 (if any) drinking it.
- [U-0204](unknowns.md#u-0204) resolution: Seed [U-0004](unknowns.md#u-0004) asks whether it can kill; independent of rounding.

### U-0210

[U-0210](unknowns.md#u-0210): What happens when you get a second Body armor while one is equipped or carried? Status: `open`.

Why it matters ([U-0210](unknowns.md#u-0210)): Decides whether the new armor is refused, replaced, or dropped.

- [U-0210](unknowns.md#u-0210) reading A: refused
- [U-0210](unknowns.md#u-0210) reading B: replaces the equipped one
- [U-0210](unknowns.md#u-0210) resolution: VOD: pickup of a second armor.

### U-0217

[U-0217](unknowns.md#u-0217): Mirror versus mirror and flashbang: if the thrower also holds a mirror, is the thrower blinded? Status: `open`.

Why it matters ([U-0217](unknowns.md#u-0217)): Mirror rule says both are used up and nothing happens; flashbang rule says the thrower is blinded instead.

- [U-0217](unknowns.md#u-0217) reading A: mirror-mirror rule wins, no blind
- [U-0217](unknowns.md#u-0217) reading B: flashbang rule wins, thrower blinded
- [U-0217](unknowns.md#u-0217) resolution: VOD: flashbang thrown by a mirror holder into a mirror holder.

### U-0218

[U-0218](unknowns.md#u-0218): If a contestant is blinded and hit by another flashbang, is the blind extended, reset or ignored? Status: `open`.

Why it matters ([U-0218](unknowns.md#u-0218)): Affects stacking of flashbang pressure.

- [U-0218](unknowns.md#u-0218) reading A: ignored
- [U-0218](unknowns.md#u-0218) reading B: reset to 30 s
- [U-0218](unknowns.md#u-0218) reading C: added
- [U-0218](unknowns.md#u-0218) free parameter `flashbang_reapply_rule`, swept over ignored, reset, additive up to 2 stacks
- [U-0218](unknowns.md#u-0218) resolution: VOD: double flashbang.

### U-0302

[U-0302](unknowns.md#u-0302): Does 'Only you can see the trap.' (C4 section) describe the trapped gift (item with attached C4) or the placed C4? Status: `open`.

Why it matters ([U-0302](unknowns.md#u-0302)): The next sentences say a placed C4 is seen only by you and Ingenuity contestants; the referent decides who sees a trapped gift and whether Ingenuity contestants see it.

- [U-0302](unknowns.md#u-0302) reading A: describes the trapped gift only
- [U-0302](unknowns.md#u-0302) reading B: describes the placed C4 only (then the last C4 sentence repeats it with Ingenuity added)
- [U-0302](unknowns.md#u-0302) reading C: describes both
- [U-0302](unknowns.md#u-0302) resolution: VOD: a non-Ingenuity contestant's map with a placed C4 nearby and holding a trapped item.

### U-0314

[U-0314](unknowns.md#u-0314): Wizard staff 'Each use costs 2 blood tokens': does Ingenuity's 10% surcharge apply to it, and what happens with fewer than 2 tokens? Status: `open`.

Why it matters ([U-0314](unknowns.md#u-0314)): ceil(2*1.1) = 3 would make the staff a third dearer for Ingenuity contestants; it is not a merchant price.

- [U-0314](unknowns.md#u-0314) reading A: 2 tokens for every sigil (not a merchant price)
- [U-0314](unknowns.md#u-0314) reading B: Ingenuity pays ceil(2*1.1) = 3
- [U-0314](unknowns.md#u-0314) reading C: cannot be used with fewer than the cost
- [U-0314](unknowns.md#u-0314) resolution: VOD: Ingenuity contestant's token count before and after a staff use.

### U-0316

[U-0316](unknowns.md#u-0316): Poison Dart: with '20 HP over 30min' and the poison page's 1 HP every 1min 30s, is the first tick at 1min 30s or immediately? Status: `open`.

Why it matters ([U-0316](unknowns.md#u-0316)): Shifts every dart tick by 1min 30s and the time of the last HP.

- [U-0316](unknowns.md#u-0316) reading A: ticks at 90, 180, ..., 1800 s (20 ticks, last at 30min)
- [U-0316](unknowns.md#u-0316) reading B: ticks at 0, 90, ..., 1710 s (20 ticks, first immediately)
- [U-0316](unknowns.md#u-0316) resolution: VOD: poisoned contestant HP timeline.

### U-0326

[U-0326](unknowns.md#u-0326): 'Local solar time': local to what (the contestant's position, the event location, one reference city)? Status: `open`.

Why it matters ([U-0326](unknowns.md#u-0326)): The wake and sleep window depends on it; it differs by about 4 minutes per degree of longitude, more across time zones if a reference clock is used.

- [U-0326](unknowns.md#u-0326) reading A: solar time at the contestant's own position
- [U-0326](unknowns.md#u-0326) reading B: solar time at one reference location of the event
- [U-0326](unknowns.md#u-0326) reading C: local clock time of the contestant's phone
- [U-0326](unknowns.md#u-0326) resolution: Organizer statement.

### U-0335

[U-0335](unknowns.md#u-0335): Enchanted bow 'five shots or two hours': whichever first, or whichever last? Status: `open`.

Why it matters ([U-0335](unknowns.md#u-0335)): Decides whether the bonus survives long idle periods or ends after five shots.

- [U-0335](unknowns.md#u-0335) reading A: ends at the first of 5 shots or 2 h
- [U-0335](unknowns.md#u-0335) reading B: ends only when both are reached
- [U-0335](unknowns.md#u-0335) resolution: VOD: enchanted bow after 5 shots within 2 h.

### U-0402

[U-0402](unknowns.md#u-0402): Nuke damage cut for the Protection sigil: '50% less' of 20 HP is 10 HP, but how are odd admin-set damages rounded, and is the cut applied before or after other reductions? Status: `open`.

Why it matters ([U-0402](unknowns.md#u-0402)): Admin nukes may set any damage; an odd value makes floor, ceil and exact fractions differ, and order changes totals with Kick-live and armor.

- [U-0402](unknowns.md#u-0402) reading A: d -> floor(d/2)
- [U-0402](unknowns.md#u-0402) reading B: d -> ceil(d/2)
- [U-0402](unknowns.md#u-0402) reading C: d -> d/2 exact (no rounding)
- [U-0402](unknowns.md#u-0402) free parameter `admin_nuke_damage`, swept over 1 to 100 HP; the wiki gives only the 20 HP default and no admin range
- [U-0402](unknowns.md#u-0402) resolution: VOD of an admin nuke with odd damage on a Protection contestant.
- [U-0402](unknowns.md#u-0402) resolution: Damage page order of operations ([U-0001](unknowns.md#u-0001), [U-0006](unknowns.md#u-0006)).

### U-0412

[U-0412](unknowns.md#u-0412): Random items: what is the distribution of 'a random item' in care packages and airdrops, and what is the distribution of 'within 10m of a random point' for the airdrop? Status: `open`.

Why it matters ([U-0412](unknowns.md#u-0412)): Needed for expected supply value; the item pool is stated nowhere in the corpus.

- [U-0412](unknowns.md#u-0412) resolution: VOD: log item contents of airdrops.
- [U-0412](unknowns.md#u-0412) resolution: Chests page was removed ([U-0015](unknowns.md#u-0015)).

### U-0415

[U-0415](unknowns.md#u-0415): What does 'attacking a copy uses up your attack' consume: the weapon durability, the attack slot, the item, a cooldown? Does it apply to staffs, drones, C4 and landmines and to Thermal goggle holders who identify copies? Status: `open`.

Why it matters ([U-0415](unknowns.md#u-0415)): Cost of a misidentified target for an attacker.

- [U-0415](unknowns.md#u-0415) reading A: the charge or use of the item as for a normal hit
- [U-0415](unknowns.md#u-0415) reading B: only a cooldown
- [U-0415](unknowns.md#u-0415) reading C: one durability point and a cooldown
- [U-0415](unknowns.md#u-0415) resolution: VOD of a weapon hit on an illusion copy.

### U-0416

[U-0416](unknowns.md#u-0416): Illusion cooldown: 'The next one can start 30min after it ends'. Does 'it ends' mean the 10min expiry or a destroyed illusion, and what happens to a purchase made while the illusion is running (queued, refused, refunded)? Status: `open`.

Why it matters ([U-0416](unknowns.md#u-0416)): Bounds how often illusions occur (about one per 40min).

- [U-0416](unknowns.md#u-0416) reading A: 30min after the 10min expiry; purchases during the wait are refused
- [U-0416](unknowns.md#u-0416) reading B: 30min after the previous start
- [U-0416](unknowns.md#u-0416) reading C: purchases queue and start at the earliest time
- [U-0416](unknowns.md#u-0416) resolution: VOD: observe the event live with an on-screen timer.

### U-0421

[U-0421](unknowns.md#u-0421): Cyclops steering vote: what is the direction set, does the winner persist when nobody votes, and are votes per viewer per 5s window? Status: `open`.

Why it matters ([U-0421](unknowns.md#u-0421)): Decides how directable the cyclops is toward a contestant.

- [U-0421](unknowns.md#u-0421) reading A: continuous bearing, mean of votes
- [U-0421](unknowns.md#u-0421) reading B: discrete directions, plurality per 5s window
- [U-0421](unknowns.md#u-0421) reading C: no votes keep the previous direction
- [U-0421](unknowns.md#u-0421) resolution: VOD of the cyclops vote UI.

### U-0422

[U-0422](unknowns.md#u-0422): Cyclops zone damage: 'Outside the safe zones it takes zone damage'. Same rate as contestants ([U-0003](unknowns.md#u-0003)), same escalation, or flat? Status: `open`.

Why it matters ([U-0422](unknowns.md#u-0422)): Whether an unsafe cyclops dies to the zone alone, paying nothing.

- [U-0422](unknowns.md#u-0422) reading A: same 2s tick and rule as for contestants
- [U-0422](unknowns.md#u-0422) reading B: different rule
- [U-0422](unknowns.md#u-0422) resolution: VOD of a cyclops outside the zone.

### U-0423

[U-0423](unknowns.md#u-0423): Reality Shield: duration is not given, 'Everyone within 30m' is radius or diameter, and 'immune to all damage, zombies and new poison' leaves existing poison running? Status: `open`.

Why it matters ([U-0423](unknowns.md#u-0423)): Admin tool, but decides nuke counters and poison cure.

- [U-0423](unknowns.md#u-0423) reading A: permanent until removed
- [U-0423](unknowns.md#u-0423) reading B: timed (undisclosed)
- [U-0423](unknowns.md#u-0423) reading C: radius 30m
- [U-0423](unknowns.md#u-0423) reading D: diameter 30m
- [U-0423](unknowns.md#u-0423) free parameter `reality_shield_duration_s`, swept over 60 to 86400 s; no time stated, event scale bound
- [U-0423](unknowns.md#u-0423) resolution: Admin statement.

### U-0428

[U-0428](unknowns.md#u-0428): Summon rate: 'up to 3 times every 6h'. Fixed 6h blocks, a rolling 6h window, or a cooldown after the third use? Status: `open`.

Why it matters ([U-0428](unknowns.md#u-0428)): Bounds Necromancy income from Summon.

- [U-0428](unknowns.md#u-0428) reading A: rolling window: at most 3 uses in any 6h
- [U-0428](unknowns.md#u-0428) reading B: fixed 6h blocks from the event start
- [U-0428](unknowns.md#u-0428) reading C: 6h lockout after the third use
- [U-0428](unknowns.md#u-0428) resolution: VOD of a Necromancy contestant summoning four times.

### U-0430

[U-0430](unknowns.md#u-0430): Ingenuity Zombie Killer: 'kills the next ten zombies that come within 10m of its owner' and 'stops zombies draining you until it has killed ten'. Do ten zombies arriving together count, is the drain stop limited to the ten, and is the order by approach? Status: `open`.

Why it matters ([U-0430](unknowns.md#u-0430)): Defensive value against hordes of 50.

- [U-0430](unknowns.md#u-0430) reading A: ten kills then ends, simultaneous arrivals killed in distance order
- [U-0430](unknowns.md#u-0430) reading B: ten distinct zombies within 10m at any moment
- [U-0430](unknowns.md#u-0430) resolution: VOD.

### U-0431

[U-0431](unknowns.md#u-0431): Zombie repellent: 'zombies ignore you for 20min' (Zombies page) versus 'stop zombies hurting you' (Items). Does ignoring remove you from targeting (zombies chase other contestants) or only block drain? Status: `open`.

Why it matters ([U-0431](unknowns.md#u-0431)): Affects how zombies redistribute among unprotected contestants.

- [U-0431](unknowns.md#u-0431) reading A: immune to drain only, still chased
- [U-0431](unknowns.md#u-0431) reading B: removed from the target set
- [U-0431](unknowns.md#u-0431) resolution: VOD.

### U-0506

[U-0506](unknowns.md#u-0506): Piety claiming a chest or crate when the potion stack is already at 6 (or the inventory cannot take a potion): what happens? Status: `open`.

Why it matters ([U-0506](unknowns.md#u-0506)): Decides whether chest claims are free actions at the cap and whether potions are lost or dropped.

- [U-0506](unknowns.md#u-0506) reading A: claim refused, chest stays
- [U-0506](unknowns.md#u-0506) reading B: chest consumed, potion lost
- [U-0506](unknowns.md#u-0506) reading C: potion drops at the contestant's feet (as the hunter potion does in the attacks page)
- [U-0506](unknowns.md#u-0506) resolution: VOD: Piety contestant with a full stack of 6 claiming a chest.

### U-0509

[U-0509](unknowns.md#u-0509): Greed Steal when the thief has no room: what happens if the inventory is full, or Body Armor is stolen while the thief already carries armor? Status: `open`.

Why it matters ([U-0509](unknowns.md#u-0509)): Body Armor allows 'at most one, including equipped armor'; stealing it from an armored Greed contestant is either impossible or discards one armor.

- [U-0509](unknowns.md#u-0509) reading A: steal refused when the thief cannot hold the item
- [U-0509](unknowns.md#u-0509) reading B: item drops at the thief's feet
- [U-0509](unknowns.md#u-0509) reading C: the stolen item replaces or discards an existing one
- [U-0509](unknowns.md#u-0509) resolution: VOD: a Greed contestant with a full inventory using Steal.

### U-0515

[U-0515](unknowns.md#u-0515): Ingenuity potion combining: what does 'two matching potions' mean, and are there costs or limits? Status: `open`.

Why it matters ([U-0515](unknowns.md#u-0515)): Heal values add up exactly (5+5=10, 10+10=20, 20+20=40), so combining is lossless for healing but saves slots for a 2-slot sigil; the limits are unstated.

- [U-0515](unknowns.md#u-0515) reading A: two health potions of the same size give one of the next size (small to medium to large to gigantic); gigantic cannot combine
- [U-0515](unknowns.md#u-0515) reading B: any two potions of the same kind (including Eddie's potion or Anti poison) combine
- [U-0515](unknowns.md#u-0515) reading C: as A with a cooldown or a cost not stated
- [U-0515](unknowns.md#u-0515) resolution: VOD: an Ingenuity contestant combining potions.

### U-0521

[U-0521](unknowns.md#u-0521): Everything potion 'Cures poison and heals by potion tier': does it also grant the 10 min poison immunity of an Anti poison? Status: `open`.

Why it matters ([U-0521](unknowns.md#u-0521)): The recipe uses an Anti poison and a Health potion; the Anti poison item gives immunity for 10 min.

- [U-0521](unknowns.md#u-0521) reading A: cures poison and heals tier HP only
- [U-0521](unknowns.md#u-0521) reading B: also grants 10 min of poison immunity
- [U-0521](unknowns.md#u-0521) resolution: VOD: an Ingenuity contestant using the potion, then being poisoned.

### U-0534

[U-0534](unknowns.md#u-0534): Fake gravestone copy source: when someone is eliminated, who chooses which eliminated contestant is copied? Status: `open`.

Why it matters ([U-0534](unknowns.md#u-0534)): 'copies the gravestone of an eliminated contestant, or of a random living one while nobody is eliminated': the contrast suggests randomness only in the fallback case.

- [U-0534](unknowns.md#u-0534) reading A: the troll picks one eliminated contestant; random living contestant only if there is none
- [U-0534](unknowns.md#u-0534) reading B: random among eliminated contestants; random among living ones if none
- [U-0534](unknowns.md#u-0534) reading C: the most recent eliminated contestant
- [U-0534](unknowns.md#u-0534) resolution: VOD: fake gravestones placed after one and after several eliminations.

### U-0536

[U-0536](unknowns.md#u-0536): Unsafe circle 'Cooldown 2h' with a 20 min duration: does the cooldown start at placement or when the circle ends? Status: `open`.

Why it matters ([U-0536](unknowns.md#u-0536)): Placement-anchored allows a new circle 100 min after the previous one expired; end-anchored 120 min.

- [U-0536](unknowns.md#u-0536) reading A: 2 h from placement
- [U-0536](unknowns.md#u-0536) reading B: 2 h from the end of the circle (2 h 20 min from placement)
- [U-0536](unknowns.md#u-0536) resolution: VOD: second circle placed at 2 h versus 2 h 20 min.

### U-0618

[U-0618](unknowns.md#u-0618): Protection potion heal 'less 50%': rounding when the tier is odd (Small potion 5 HP)? Status: `open`.

Why it matters ([U-0618](unknowns.md#u-0618)): Small potion gives 2, 3 or 2.5 HP.

- [U-0618](unknowns.md#u-0618) reading A: floor(h/2)
- [U-0618](unknowns.md#u-0618) reading B: ceil(h/2)
- [U-0618](unknowns.md#u-0618) reading C: h/2 exact fraction
- [U-0618](unknowns.md#u-0618) resolution: VOD: Protection contestant drinking a Small potion.

## Contradictions between pages

### C-0100

[C-0100](unknowns.md#c-0100): Intro says a live Kick contestant does 10% more damage (all damage); the hit pipeline restricts the bonus to a closed list of the attacker's own weapon hits. Status: `open`.

- [C-0100](unknowns.md#c-0100) `wiki-006`: "you take 10% less damage and do 10% more damage" ([source](https://iceposeidon.com/safezone/wiki#damage))
- [C-0100](unknowns.md#c-0100) `wiki-damage-038`: "If the attacker is live on Kick, their own bow, staff, knife, long sword, axe, machete, drone, C4, landmine, fake chest and trapped gift hits deal 10% more, rounded down." ([source](https://iceposeidon.com/safezone/wiki/damage#order))

### C-0101

[C-0101](unknowns.md#c-0101): Mirror reflect list omits trapped gifts, but the damage table lists Mirror forcefield (reflects) on the Trapped gift row. Status: `open`.

- [C-0101](unknowns.md#c-0101) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [C-0101](unknowns.md#c-0101) `wiki-damage-070`: "It only reflects Poison Darts, fake gravestones, bows, wizard staffs, knives, long swords, Zarok's axes, machetes, drones, C4, landmines, flashbangs and fake chests, and never your own explosives." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

### C-0102

[C-0102](unknowns.md#c-0102): Body Armor 'works on every kind of damage' versus the Trapped gift row (no Body armor) and the items page ('A trapped gift ignores it'). Status: `open`.

- [C-0102](unknowns.md#c-0102) `wiki-damage-071`: "Body Armor works on every kind of damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [C-0102](unknowns.md#c-0102) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [C-0102](unknowns.md#c-0102) `wiki-items-027`: "A trapped gift ignores it." ([source](https://iceposeidon.com/safezone/wiki/items#body_armor))

### C-0103

[C-0103](unknowns.md#c-0103): Death Ward scope: damage page blocks outside-the-circle damage only; Death sigil page adds hits from an unsafe circle and immunity to both for 2min (the damage table row for Unsafe circle also lists Death Ward). Status: `open`.

- [C-0103](unknowns.md#c-0103) `wiki-damage-073`: "Death Ward: a Death contestant's first hit from outside the circle is blocked, and damage from outside the circle is blocked for 2min." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [C-0103](unknowns.md#c-0103) `wiki-damage-006`: "| Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [C-0103](unknowns.md#c-0103) `wiki-sigils-death-013`: "Death ward: the first hit from outside the circle or from an unsafe circle is blocked and you are immune to both for 2min." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))

### C-0104

[C-0104](unknowns.md#c-0104): Sleeping Bag immunity: damage page has no delay and excludes zone, unsafe circle and robot; merchant page needs 65 seconds of sleep, covers flashbangs and excludes only zone and unsafe circle. Status: `open`.

- [C-0104](unknowns.md#c-0104) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [C-0104](unknowns.md#c-0104) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

### C-0105

[C-0105](unknowns.md#c-0105): Revival of a Healing contestant: intro lets any contestant do it up to 2 times; Healing page requires a living contestant within 10m of the gravestone. Status: `open`.

- [C-0105](unknowns.md#c-0105) `wiki-015`: "Any contestant can revive a Healing contestant, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki#death))
- [C-0105](unknowns.md#c-0105) `wiki-sigils-healing-011`: "Any living contestant within 10m (33ft) of your gravestone can revive you, up to 2 times." ([source](https://iceposeidon.com/safezone/wiki/sigils/healing#rules))

### C-0200

[C-0200](unknowns.md#c-0200): Items page lists 13 reflectable attacks without trapped gift, but the damage page table lists Mirror forcefield (reflects) on the Trapped gift row. Status: `open`.

- [C-0200](unknowns.md#c-0200) `wiki-items-055`: "Only reflects Poison Darts, fake gravestones, knives, Zarok's axes, long swords, machetes, bows, staffs, drones, C4, landmines, flashbangs and fake chests." ([source](https://iceposeidon.com/safezone/wiki/items#mirror_forcefield))
- [C-0200](unknowns.md#c-0200) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([source](https://iceposeidon.com/safezone/wiki/damage))

### C-0201

[C-0201](unknowns.md#c-0201): Items page: a trapped gift ignores Body armor. Damage page: Body Armor works on every kind of damage. Status: `open`.

- [C-0201](unknowns.md#c-0201) `wiki-items-027`: "A trapped gift ignores it." ([source](https://iceposeidon.com/safezone/wiki/items#body_armor))
- [C-0201](unknowns.md#c-0201) `wiki-damage-071`: "Body Armor works on every kind of damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

### C-0202

[C-0202](unknowns.md#c-0202): Items page Shield exceptions omit robot damage; damage page adds robot to the unblocked list. Status: `open`.

- [C-0202](unknowns.md#c-0202) `wiki-items-023`: "Immune to damage for 20min, except zone damage and unsafe circle damage." ([source](https://iceposeidon.com/safezone/wiki/items#shield))
- [C-0202](unknowns.md#c-0202) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

### C-0203

[C-0203](unknowns.md#c-0203): Items page: sleeping contestants are immune to flashbangs. Merchant page: immune only after 65 seconds of sleep. Status: `open`.

- [C-0203](unknowns.md#c-0203) `wiki-items-075`: "Sleeping contestants are immune." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))
- [C-0203](unknowns.md#c-0203) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

### C-0204

[C-0204](unknowns.md#c-0204): Items page: a vulnerable contestant is unprotected by a Safety bubble. Merchant page: the Vulnerability Dart pops every Safety Bubble they own or stand in. Status: `open`.

- [C-0204](unknowns.md#c-0204) `wiki-items-021`: "It does not protect a vulnerable contestant, and you cannot use it while vulnerable." ([source](https://iceposeidon.com/safezone/wiki/items#safety_bubble))
- [C-0204](unknowns.md#c-0204) `wiki-merchant-017`: "It removes their Shield and pops every Safety Bubble they own or stand in, and stops Shields and Safety Bubbles protecting them for 10 minutes." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))

### C-0205

[C-0205](unknowns.md#c-0205): Items page: Zombie repellent stops zombies hurting you. Zombies page: zombies ignore you. Status: `open`.

- [C-0205](unknowns.md#c-0205) `wiki-items-031`: "Use it to stop zombies hurting you for 20min." ([source](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))
- [C-0205](unknowns.md#c-0205) `wiki-zombies-019`: "Zombie repellent: use it and zombies ignore you for 20min." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))

### C-0300

[C-0300](unknowns.md#c-0300): Sleeping Bag immunity exceptions: the merchant page lists zone and unsafe circle damage only; the damage page also lists robot damage as not blocked. Status: `open`.

- [C-0300](unknowns.md#c-0300) `wiki-merchant-023`: "After 65 seconds of sleep you are immune to flashbangs and to all damage except zone and unsafe circle damage." ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- [C-0300](unknowns.md#c-0300) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

### C-0301

[C-0301](unknowns.md#c-0301): Sleeping Bag immunity timing: the merchant page grants immunity only after 65 seconds of sleep; the damage page grants it to any sleeping contestant within 15m of their bag with no delay; the items page says sleeping contestants are immune to a flashbang with no delay. Status: `open`.

- [C-0301](unknowns.md#c-0301) `wiki-merchant-023`: "After 65 seconds of sleep you are immune" ([source](https://iceposeidon.com/safezone/wiki/merchant#items))
- [C-0301](unknowns.md#c-0301) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [C-0301](unknowns.md#c-0301) `wiki-items-075`: "Sleeping contestants are immune." ([source](https://iceposeidon.com/safezone/wiki/items#flashbang))

### C-0400

[C-0400](unknowns.md#c-0400): Blocker lists differ: the attacks page names Gas mask for tear gas, Flak jacket for gunship bombs, while the damage page also lists Shield, Safety bubble, Sleeping Bag and Body armor for the same sources. Status: `open`.

- [C-0400](unknowns.md#c-0400) `wiki-attacks-025`: "A Gas mask blocks it." ([source](https://iceposeidon.com/safezone/wiki/attacks#tear-gas))
- [C-0400](unknowns.md#c-0400) `wiki-damage-009`: "| Tear gas | Shield, Safety bubble, Sleeping Bag, Gas mask, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [C-0400](unknowns.md#c-0400) `wiki-attacks-041`: "A Flak jacket blocks one bomb." ([source](https://iceposeidon.com/safezone/wiki/attacks#gunship))
- [C-0400](unknowns.md#c-0400) `wiki-damage-027`: "| Gunship bomb | Shield, Safety bubble, Sleeping Bag, Protection, Flak jacket, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

### C-0401

[C-0401](unknowns.md#c-0401): Zombie immunity list omits Necromancy, which the Necromancy page calls fully immune from zombies (the Damage page lists it). Status: `open`.

- [C-0401](unknowns.md#c-0401) `wiki-zombies-018`: "A Shield, a Safety bubble, a Reality Shield or sleeping in your own Sleeping Bag makes you immune." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))
- [C-0401](unknowns.md#c-0401) `wiki-sigils-necromancy-016`: "Fully immune from zombies." ([source](https://iceposeidon.com/safezone/wiki/sigils/necromancy#rules))
- [C-0401](unknowns.md#c-0401) `wiki-damage-010`: "| Zombie drain | Shield, Safety bubble, Sleeping Bag, Necromancy / Repellent, Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

### C-0402

[C-0402](unknowns.md#c-0402): Repellent effect: zombies 'ignore you' (targeting) versus 'stop zombies hurting you' (damage only). Status: `open`.

- [C-0402](unknowns.md#c-0402) `wiki-zombies-019`: "Zombie repellent: use it and zombies ignore you for 20min." ([source](https://iceposeidon.com/safezone/wiki/zombies#defence))
- [C-0402](unknowns.md#c-0402) `wiki-items-031`: "Use it to stop zombies hurting you for 20min." ([source](https://iceposeidon.com/safezone/wiki/items#zombie_repellent))

### C-0403

[C-0403](unknowns.md#c-0403): Care package Trolling diversion: 'within 5m of a Trolling contestant' for any care package versus 'next to' and only 'from viewers' on the Trolling page. Status: `open`.

- [C-0403](unknowns.md#c-0403) `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))
- [C-0403](unknowns.md#c-0403) `wiki-sigils-trolling-020`: "Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))

### C-0404

[C-0404](unknowns.md#c-0404): Craft destruction: 'crafted items' on the Zombies page versus only 'unique crafts' destroyed by 'Zombie hits' on the Ingenuity page. Status: `open`.

- [C-0404](unknowns.md#c-0404) `wiki-zombies-004`: "a 40% chance to destroy crafted items" ([source](https://iceposeidon.com/safezone/wiki/zombies))
- [C-0404](unknowns.md#c-0404) `wiki-sigils-ingenuity-012`: "Unique crafts cannot be traded, stolen or looted, and have a 40% chance to be destroyed by Zombie hits." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#rules))

### C-0500

[C-0500](unknowns.md#c-0500): Ingenuity page: Shields and Sleeping Bags stop the Robot. Damage page: Shield does not block robot damage and a sleeping contestant is not immune to robot damage. Status: `open`.

- [C-0500](unknowns.md#c-0500) `wiki-sigils-ingenuity-016`: "Shields and Sleeping Bags stop it." ([source](https://iceposeidon.com/safezone/wiki/sigils/ingenuity#recipe-robot))
- [C-0500](unknowns.md#c-0500) `wiki-damage-058`: "A Shield does not block zone, unsafe circle or robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [C-0500](unknowns.md#c-0500) `wiki-damage-067`: "A sleeping contestant within 15m (49ft) of their own Sleeping Bag is immune to all damage except zone, unsafe circle and robot damage." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

### C-0501

[C-0501](unknowns.md#c-0501): Trolling page: crates and care packages from viewers roll the 3% diversion. Attacks page: only care packages roll (with a 5 m landing distance); a crate is a separate item. Status: `open`.

- [C-0501](unknowns.md#c-0501) `wiki-sigils-trolling-020`: "Each crate or care package from viewers has a 3% chance to land next to a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [C-0501](unknowns.md#c-0501) `wiki-attacks-080`: "It has a 3% chance to land within 5m (16ft) of a Trolling contestant instead." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))
- [C-0501](unknowns.md#c-0501) `wiki-attacks-081`: "A crate holds an item bought by a viewer." ([source](https://iceposeidon.com/safezone/wiki/attacks#care-package))

### C-0502

[C-0502](unknowns.md#c-0502): Trolling page: a Reality Shield blocks unsafe circle damage. Damage table row for unsafe circle omits the Reality Shield (the notes on the same page include it). Status: `open`.

- [C-0502](unknowns.md#c-0502) `wiki-sigils-trolling-027`: "A Guardian angel, a Safety bubble, a Reality Shield or a Death Ward blocks it." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))
- [C-0502](unknowns.md#c-0502) `wiki-damage-006`: "Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))
- [C-0502](unknowns.md#c-0502) `wiki-damage-059`: "A Safety bubble and a Reality Shield do." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))

### C-0503

[C-0503](unknowns.md#c-0503): Trolling page: one clause says defense item loss every five seconds with no first-hit condition, another says it starts after the first hit and requires being not immune. Status: `open`.

- [C-0503](unknowns.md#c-0503) `wiki-sigils-trolling-017`: "loses one defense item or unique craft every five seconds, equipped Body Armor included" ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#rules))
- [C-0503](unknowns.md#c-0503) `wiki-sigils-trolling-024`: "After your first hit, you lose one random defense item or unique craft every five seconds while you stay inside and are not immune." ([source](https://iceposeidon.com/safezone/wiki/sigils/trolling#unsafe))

### C-0600

[C-0600](unknowns.md#c-0600): Death ward: the sigil page blocks the first hit from outside the circle or from an unsafe circle with immunity to both for 2min; the damage page prose names only outside-the-circle damage (the damage table lists Death Ward for both rows). Status: `open`.

- [C-0600](unknowns.md#c-0600) `wiki-sigils-death-013`: "Death ward: the first hit from outside the circle or from an unsafe circle is blocked and you are immune to both for 2min." ([source](https://iceposeidon.com/safezone/wiki/sigils/death#rules))
- [C-0600](unknowns.md#c-0600) `wiki-damage-073`: "Death Ward: a Death contestant's first hit from outside the circle is blocked, and damage from outside the circle is blocked for 2min." ([source](https://iceposeidon.com/safezone/wiki/damage#notes))
- [C-0600](unknowns.md#c-0600) `wiki-damage-006`: "| Unsafe circle | Safety bubble, Guardian angel, Death Ward, Hazmat suit (slows), Body armor (absorbs)" ([source](https://iceposeidon.com/safezone/wiki/damage))

### C-0601

[C-0601](unknowns.md#c-0601): Protection immunity: the stat card lists poison, drones, missiles, C4, landmines, airstrikes, gunships; the rules sentence and the damage table add trapped gifts, airstrike fire and Protection retribution. Status: `open`.

- [C-0601](unknowns.md#c-0601) `wiki-sigils-protection-007`: "Poison, drones, missiles, C4, landmines, airstrikes, gunships" ([source](https://iceposeidon.com/safezone/wiki/sigils/protection))
- [C-0601](unknowns.md#c-0601) `wiki-sigils-protection-008`: "Immune to poison, drones, missiles, C4, landmines, trapped gifts, airstrikes and their fire, gunship bombs and Protection retribution." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [C-0601](unknowns.md#c-0601) `wiki-damage-021`: "| Trapped gift | Shield, Sleeping Bag, Protection, Mirror forcefield (reflects)" ([source](https://iceposeidon.com/safezone/wiki/damage))

### C-0602

[C-0602](unknowns.md#c-0602): Protection strategy advice says immune from 'most viewer attacks'; the sigil and attack pages make Protection immune to missiles, airstrikes and gunships only, out of eight viewer attack types (nukes halved). Status: `open`.

- [C-0602](unknowns.md#c-0602) `wiki-strategy-006`: "If you are unpopular with viewers, consider picking the Protection sigil, so you are immune from most viewer attacks." ([source](https://iceposeidon.com/safezone/wiki/strategy#sigils))
- [C-0602](unknowns.md#c-0602) `wiki-sigils-protection-008`: "Immune to poison, drones, missiles, C4, landmines, trapped gifts, airstrikes and their fire, gunship bombs and Protection retribution." ([source](https://iceposeidon.com/safezone/wiki/sigils/protection#rules))
- [C-0602](unknowns.md#c-0602) `wiki-attacks-001`: "While a contestant's EMP is active, viewers cannot send missiles, nukes, hordes, tear gas, airstrikes, gunships, cyclopes or bounties." ([source](https://iceposeidon.com/safezone/wiki/attacks#emp))
