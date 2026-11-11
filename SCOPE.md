# Scope

Written before any analysis. Anything not listed under "Allowed" is out of scope until the owner (kil) adds it here in writing.

## Target

Ice Poseidon's Safe Zone event (Miami edition), as described by its public wiki:

- https://iceposeidon.com/safezone
- https://iceposeidon.com/safezone/wiki and its 18 sub-pages (snapshot of 2026-11-11 lists them in `prompts/MASTER_PROMPT.md`, section 3)

The object of study is the rule system. The deliverable is an encyclopedia (the "Codex") that reconstructs, formalizes and proves the consequences of those rules.

## Allowed

1. Reading every public wiki page, as any visitor's browser would, at most 1 request per second, honoring `robots.txt`.
2. Downloading, once per dated snapshot, the static assets those pages reference (`/_astro/*.js`, `/_astro/*.css`, images referenced by `<img>` tags). They are hashed (SHA-256) and analyzed offline with REA.
3. Public archives of those same pages (Internet Archive Wayback Machine) to reconstruct rule changes over time.
4. Public stream VODs and public posts by the organizer, used only to read rule statements and game-event outcomes (HP changes, item effects, prices shown on screen).
5. A HAR file that kil records himself while browsing the public wiki, analyzed with REA `inspect_web_network_capture`.
6. Mathematics, simulation and statistics on all of the above.

## Allowed only after kil writes "yes" in this file

7. Static, offline analysis of an official contestant app, if one is publicly distributed (store APK or similar), downloaded by kil. No execution against the live server.
8. Reading a public, unauthenticated endpoint discovered in the site's own JavaScript (for example a leaderboard). Location data is never stored, whatever the endpoint returns.

## Pending approval (found during the work, not yet allowed)

Each line needs kil to write "yes" next to it. Until then, nothing here is requested.

- P1. `https://iceposeidon.com/safezone/wiki/search-index.json`: static JSON loaded by the wiki's own search box (RE-0003). One GET.
- P2. `https://iceposeidon.com/events`, `/safezone/recap`: public pages that may hold contest rules or the viewer prize (`corpus/rules.md`). One GET each. (`/safezone-austin` dropped: October rules are obsolete.)
- P3. `api.iceposeidon.com` route `purchasables` (and any public, unauthenticated route that lists viewer attack prices), `event-public.iceposeidon.com`, `robot-api.iceposeidon.com` (RE-0003). Allowed item 8 applies: no location data stored.
- P4. Phase 2b: the contestant app behind `/safezone/download` (Allowed item 7).
- Never, whatever the answer: `/safezone/map`, `/safezone/leaderboards` or any feed of contestant positions.

## Forbidden

- Any request that is not a plain visitor read: no fuzzing, no parameter tampering, no endpoint guessing, no enumeration of CDN paths that pages do not reference.
- Authentication bypass, use of anyone else's session, automation of gameplay or of viewer purchases.
- Collecting, storing or deriving the real-world position or movement of any contestant.
- Publishing the site's or app's code. The public repository contains hashes, extraction scripts, short attributed quotations and derived facts only.
- Uploading any downloaded artifact to a third-party service.

## Amendments by kil

- 2026-11-11: the repository is public "as is", including `corpus/clauses/` (the full wiki text, split into attributed clauses with source URL and snapshot date). This overrides the "short attributed quotations only" limit above for the clause corpus. Site code and downloaded assets stay out of the repository.
- 2026-11-11: only the 2026-11-11 snapshot is a rule source; October 2026 captures are history only (`corpus/diffs/`).

## Contest rules gate

Phase 0 locates the official contest rules (wiki, Kick, Discord, X posts by the organizer) and quotes them in `corpus/rules.md`. If any rule forbids this kind of analysis, work stops and kil is told before anything else happens.

## Stop conditions

Stop immediately and report to kil if: an action would leave this scope, a response contains personal data, a tool behaves unexpectedly (sandbox escape, unexpected network access), or the contest rules forbid the work.
