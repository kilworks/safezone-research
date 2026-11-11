# CONTINUE: the recursive session prompt

Paste this file (or "read prompts/CONTINUE.md and execute") to start any new session. Each session does a bounded amount of work, leaves the repository green, and rewrites the handoff so the next session can start cold. Repeat until the stop condition below holds.

## 0. Load the state (no work before this)

1. Read `prompts/HANDOFF.md` in full. It wins over memory and over anything else in this file about "what is done".
2. Read `SCOPE.md`. It wins over `prompts/MASTER_PROMPT.md` whenever they disagree.
3. Read only the sections of `prompts/MASTER_PROMPT.md` that the next task needs (section numbers are in the handoff).
4. Run the four commands of the handoff. If any fails, fixing it is the first task of the session, before anything new.

## 1. Pick the work

Take the first unfinished item of "Next, in order" in the handoff. If it is blocked (on kil's decision or a missing input), skip it, say why in the handoff, and take the next one. Never start a second item before the first one is committed and pushed.

Set a budget for the session before starting (in turns or a share of the quota), and state it to kil in one line with the item chosen.

## 2. Do it

- Same epistemic rules as the master prompt, section 1: one label per statement, verbatim quotes, no invented number, every ambiguity kept as readings, a test checks the model and not the game.
- Prefer a script (an engine) to tokens. Delegate mechanical work to sonnet subagents with an explicit model, a disjoint ID range, the files they may write, and the instruction to write file by file.
- Every new theorem: statement, hypotheses, proof, label, a test in `sim/tests/` that has been seen to fail once on a deliberately wrong version.

## 3. Verify

- The four commands of the handoff are green, read from their own exit codes.
- Every new theorem or Codex page is attacked by a fresh sonnet Adversarial Verifier (master prompt section 6.1). A `BROKEN` verdict is either fixed now or written as a visible notice in the file and as an item in the handoff. Nothing is called verified without that pass.

## 4. Ship

1. `git add` by explicit file names, commit with the attribution lines, push.
2. Append one line to `ledger/iterations.jsonl`: `{date, item, outputs, tests, review, budget_used}`.
3. Rewrite `prompts/HANDOFF.md`: the state table, the "Next, in order" list (remove the done item, add any new question or follow-up the work revealed), the commit hash, and any new trap. Commit and push it.
4. Report to kil in French: 2 to 3 bullets, the files with absolute paths, the counts done over total, what needs his decision.

## 5. Recurse or stop

- At 80% of the session budget: stop starting new work, finish steps 3 and 4, and end the session. The next session starts again at step 0.
- Stop condition for the whole project (master prompt section 6.3 and section 11): all gates pass (`pytest`, `check_kb.py --coverage`, `check_codex.py`, `lint_text.py`), every theorem is `UPHELD` by a fresh verifier, theory 00 to 10 exist, the simulator reproduces every closed form, the strategy pages state scenario, seed, sample size, intervals and dependencies, and two consecutive sessions added no mechanic, theorem, promotion or demotion (fixed point). Then write the final README and tell kil.
