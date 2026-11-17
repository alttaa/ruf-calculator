# Session log
(Newest at the bottom. `/checkpoint` appends here.)

## 2026-11-11 — planning + first module (claude.ai chat)
- Did: chose Python backend architecture (engine → FastAPI → React → Vercel), roadmap PDF,
  wrote `cards.py` + 4 passing tests, set up Claude Code workflow (.claude/, docs/).
- Verified core example by brute force: 38/1081 ≈ 3.5%; 2 opponents ≈ 6.9%.
- Learned: no dataset needed (math, not ML); project = venv + package + tests;
  cards as ints (Ah = 12×4+2 = 50, divmod reverses it); negative indexing (`"AH"[-1]` = "H",
  `"10H"[:-1]` = "10"); classes vs ints tradeoff; copying paths (Option+Cmd+C, `pwd | pbcopy`);
  conda `(base)` vs venv.
- Next: evaluator.py v1.

## 2026-11-12 — src layout + evaluator start
- Did: moved engine to `python/src/ruf_engine/`, added `pyproject.toml` (editable install), PR #1 merged;
  wrote `rank_groups()` + 2 tests. Tests: 6 passed.
- Learned: src layout vs flat layout; pyproject/editable installs; `Counter` for counting ranks;
  `card // 4` = rank; sorting tuples `(count, rank)` descending puts pairs/trips first.
- Next: `is_flush`, `straight_high` (wheel!), then `score5` tuple and `best7` over 21 subsets.
