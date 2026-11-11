# RUF — roadmap and scope (capped 2026-11-11)

Scope is capped so RUF ships and then hands time back to the end goal (EBMs / MLIPs).
If a new idea isn't listed under IN, it goes to "Parking lot" — don't build it.

## IN — build these, in order
| Phase | Deliverable | Done when |
|---|---|---|
| 1 Engine | `python/ruf_engine/`: cards, evaluator (own, cross-checked with treys), beat-list, multi-opponent, dead cards, range filters, CLI | Core test 38/1081; 2 opponents ≈ 6.9%; evaluator agrees with treys on 10,000 random hands |
| 1b Bridge | Monte Carlo version of multi-opponent with an error bar | Monte Carlo lands within its ±error of the exact answer |
| 2 API | FastAPI `POST /api/beat-list`, Pydantic schemas, input validation | Interactive docs page returns correct answers |
| 3 Web | Vite + React + TS: card picker, beat-list table, opponent count, dead cards | Any valid input works; invalid input can't reach the API |
| 4 Ship | One Vercel project, basic rate limiting, README with a screenshot | Public URL works on a phone |

## OPTIONAL — only after Phase 4 ships
- Turn/river equity (win/tie/lose %).
- Opponent ranges with blockers (a "prior over hands").

## OUT — shelved
- R&D Level 4–5: CFR, Kuhn poker solver, Pluribus-style bots.
- Meta glasses / mobile app / computer vision.
- Porting the engine to the browser (only revisit if hosting becomes a problem).

## Parking lot
(Ideas that came up mid-build. Review after shipping.)
-

## After RUF ships
Next project: EBM roadmap Stage 2 — toy 2D double-well potential with denoising score matching
(see `~/.claude/rules/end-goal.md`). Reuse this repo's `.claude/` workflow.
