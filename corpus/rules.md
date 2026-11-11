# Official contest rules (Phase 0)

Snapshot: 2026-11-11. Searched by the orchestrator on 2026-11-11.

## Where we looked

| Place | Method | Result |
|---|---|---|
| The 19 wiki pages listed in `SCOPE.md` | Full text read of the 2026-11-11 snapshot (`corpus/manifest.json`) | Game rules only. No terms, eligibility, prize conditions or usage policy. |
| `https://iceposeidon.com/robots.txt` | Plain GET, 2026-11-11 03:46 UTC | HTTP 404: the site publishes no crawler policy. Under RFC 9309 a missing robots.txt allows all paths. We still keep the 1 request per second limit of `SCOPE.md`. |
| `https://iceposeidon.com/sitemap-0.xml` (referenced by every wiki page) | Plain GET | 71 URLs. No URL named rules, terms, legal or privacy. Pages outside the wiki that may hold rules: `/events`, `/safezone-austin`, `/safezone/download`, `/safezone/recap` (found by web search). Not fetched: outside `SCOPE.md` (see "Pending" below). |
| Web search (organizer posts on X, press) | Three searches, 2026-11-11 | No official rules document found. See the organizer statements below. |
| Kick channel panels, Discord announcements | Not reachable without login or a browser session | Not checked. |

Bounded negative: we found no official contest rules in the places above. That is not proof that none exist.

## What the official wiki says about the contest

All quotes from the 2026-11-11 snapshot.

- https://iceposeidon.com/safezone : "Stay in the Safe Zone at all costs, for a chance to win $50,000."
- https://iceposeidon.com/safezone/wiki : "Safe Zone is an event hosted by Ice Poseidon. Any Kick streamer is welcome to join and compete to win $50,000."
- https://iceposeidon.com/safezone/wiki : "The objective is simple: don't die, stay in the safezone, and endure. The Safe Zone will move in whatever unpredictable way Ice Poseidon chooses, it can change in size or speed, or even split apart."
- https://iceposeidon.com/safezone/wiki/sigils : "Each contestant picks one sigil after the event starts. The choice is final."

## Organizer statements (secondary, not verbatim-checked)

Found through web search on 2026-11-11. The search engine returned paraphrases of posts on the organizer's X account (https://x.com/REALIcePoseidon); we could not load the posts themselves without logging in, so none of this is a verbatim quote and all of it is labeled `HYPOTHESIS` until a post is read directly.

- The Miami edition ("Safezone 2") is announced for November 13, open to anyone who shows up with the app and streams on Kick, for a $50,000 prize; described elsewhere as a week-long event with no cars.
- "The top 3 viewers who spend their Cx bucks the best in the game (points from watching) will win cash prizes", with viewer points for actions such as damaging or healing players. No amount was given in what we could read.
- An earlier edition took place in Austin in October (consistent with the `events/safe-zone/` asset folder, see U-0013).

## The $5,000 viewer prize

Not found. The closest source describes cash prizes for the top 3 viewers with no amount. Recorded as `kb/unknowns/U-0000.yaml`, status `open`.

## Verdict for this project

No rule we found forbids reading the public wiki, analyzing its rules, or publishing derived mathematics. The work proceeds under `SCOPE.md`.

## Pending, for kil

1. Pages outside the wiki that may hold contest rules or the viewer prize: `/events`, `/safezone/recap` (`SCOPE.md` P2). Reading them is a plain visitor read but is not in `SCOPE.md` "Allowed". Add them in writing if wanted.
2. `/safezone/download` suggests a public contestant app exists (Phase 2b, `SCOPE.md` item 7).
3. Not to be read in any case: `/safezone/map` and `/safezone/leaderboards` may show contestant positions (`SCOPE.md` "Forbidden").
