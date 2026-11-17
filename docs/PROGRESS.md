# RUF progress

## Next step
Continue `python/src/ruf_engine/evaluator.py` (it has `rank_groups()` + 2 tests so far).
1. Add small helpers, each with a test: `is_flush(cards)` and `straight_high(cards)`
   (returns the top rank of a straight or None; remember the wheel A-2-3-4-5 → high = 3, i.e. the 5).
2. Combine them into `score5(cards)` → a tuple `(category, tiebreak ranks...)` so Python's
   tuple comparison ranks hands. One test per category (high card … straight flush).
3. Then `best7(cards)`: best `score5` over all C(7,5) = 21 subsets (`itertools.combinations`).

## Open questions
- Unanswered check questions from the first chat: parse_card("2c"), parse_card("Ks"), card_to_str(13).
- Stray file `.gitignire` (typo) in repo root: delete it with `git rm .gitignire` (`.gitignore` already has `*.egg-info/`).
- Empty `#demo block` comment at the end of evaluator.py: fill in or remove.

## Checklist
### Phase 0 — Setup
- [x] GitHub repo, README, .gitignore, CLAUDE.md
- [x] `python/.venv` created
- [x] `pytest` installed in the venv and listed in `python/requirements.txt`
- [x] Claude Code workflow files committed (.claude/, docs/)
- [x] src layout + `pyproject.toml` (editable install: `pip install -e .`)

### Phase 1 — Engine (Python)
- [x] `cards.py` + `tests/test_cards.py` (4 tests)
- [ ] `evaluator.py` v1: naive 5-card scorer → best-of-subsets for 6–7 cards  ← NEXT
  - [x] `rank_groups()` + 2 tests (one pair, full house)
  - [ ] `is_flush()`, `straight_high()` (incl. wheel)
  - [ ] `score5()` → (category, tiebreaks) tuple, test per category
  - [ ] `best7()` over 21 subsets
- [ ] evaluator cross-checked against `treys` on 10,000 random hands
- [ ] `beat_list.py`: core example → 38/1081 (AT 16, T9 16, KK 3, QQ 3)
- [ ] multiple opponents: 2 opponents → ≈ 6.9% (exact: 1,070,190 deals)
- [ ] Monte Carlo multi-opponent with error bar (bridge to MCMC ideas)
- [ ] dead cards + range constraints (filtering)
- [ ] CLI: `python -m ruf_engine JsJh "Kh Qc Jd"`

### Phase 2 — API
- [ ] FastAPI `POST /api/beat-list` + Pydantic schemas + input validation

### Phase 3 — React prototype
- [ ] Vite + React + TS in `web/`; card picker; beat-list table

### Phase 4 — Deploy
- [ ] Vercel project live, rate limiting

### After shipping (see docs/SCOPE.md)
- [ ] OPTIONAL: turn/river equity · ranges with blockers
- OUT: CFR / Pluribus, glasses/mobile, browser port
- [ ] Next project: EBM Stage 2 toy double-well (end-goal track)
