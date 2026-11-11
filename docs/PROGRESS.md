# RUF progress

## Next step
Start `python/ruf_engine/evaluator.py` v1: a naive hand ranker.
First sub-step: score a 5-card hand (category: high card … straight flush, plus tiebreak ranks),
with a test for each category. Then extend to 6–7 cards by trying every 5-card subset
(C(7,5) = 21) and keeping the best. Goal after that: `beat_list()` reproduces 38/1081.

## Open questions
- Unanswered check questions from the first chat: parse_card("2c"), parse_card("Ks"), card_to_str(13).

## Checklist
### Phase 0 — Setup
- [x] GitHub repo, README, .gitignore, CLAUDE.md
- [x] `python/.venv` created
- [ ] `pytest` installed in the venv and listed in `python/requirements.txt`
- [ ] Claude Code workflow files committed (.claude/, docs/)

### Phase 1 — Engine (Python)
- [x] `cards.py` + `tests/test_cards.py` (4 tests)
- [ ] `evaluator.py` v1: naive 5-card scorer → best-of-subsets for 6–7 cards  ← NEXT
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
