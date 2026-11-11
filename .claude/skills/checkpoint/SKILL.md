---
name: checkpoint
description: Save RUF progress at the end of a session so the next session can pick up exactly here.
disable-model-invocation: true
---

Checkpoint the RUF session:

1. Run the tests from `python/` and note the result.
2. Update `docs/PROGRESS.md`:
   - tick off finished items, add new sub-items if the work split up
   - rewrite the "Next step" section so a fresh session knows exactly what to do first
   - update "Open questions"
3. Append an entry to the END of `docs/SESSION_LOG.md` with today's date:
   what we did, what Alex learned (concepts, in a few words each), what's next.
   Keep it under 10 lines.
4. If any fork-point decision was made, add it to `docs/DECISIONS.md`.
5. Show Alex the git commands to commit, with a suggested message, e.g.
   `git add -A && git commit -m "engine: add naive evaluator + tests"`.
   Don't commit for him unless he asks.
6. Tip: suggest `/rename <short-topic>` so this session is easy to find with `claude --resume`.

$ARGUMENTS
