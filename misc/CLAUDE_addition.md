# RUF ("R U F***ed") — poker probability calculator

## What this project is
A public website that shows the probability that opponents' hands beat yours,
computed purely from card probability, with adjustable assumptions
(dead/folded cards, "opponent holds X"). No sign-in, no database.

## Who I am and how to teach me
- I'm Alex, a novice at Python projects (beyond simple scripts) and new to React. I'm on macOS.
- This is a learning project: explain, don't just write code for me.
- Short chunks, one idea at a time, concrete numbers before abstract symbols.
- Quiz me with small check questions before moving on.
- Flag "fork points" where another method/design is worth knowing.

## Architecture (build inside out)
1. `engine/ruf_engine/` — pure Python math. Never imports web code.
2. `api/` — FastAPI wrapper (POST /api/equity), Pydantic schemas, stateless.
3. `web/` — Vite + React + TypeScript frontend.
4. Deploy: one Vercel project (static frontend + Python function).

## Conventions
- Cards are ints 0–51: `card = rank * 4 + suit`.
  Ranks "23456789TJQKA" -> 0..12, suits "cdhs" -> 0..3. Ten is "T", so every card string is 2 chars.
- Integers inside the engine (speed); any readable Card class only at the edges.
- Every module gets pytest tests. Run from `engine/`: `python -m pytest -q`
- Virtual env: `engine/.venv` (`source .venv/bin/activate`).

## Progress
- [x] Phase 0: folder layout, venv, pytest
- [x] `cards.py` + `tests/test_cards.py` (4 tests passing)
- [ ] `evaluator.py` v1: naive 7-card ranker (try all 21 five-card subsets) — NEXT
- [ ] evaluator v2: phevaluator/treys, cross-checked against v1 on 10,000 random hands
- [ ] `equity.py`: exact enumeration (flop: 1,081 × 990 ≈ 1.07M matchups) + Monte Carlo
- [ ] assumptions (dead cards, conditioning), CLI: `python -m ruf_engine AhKh "Qh Jh 2c"`
- [ ] Phases 2–4: API, React prototype, Vercel deploy
- [ ] Phase 5: R&D levels (ranges/blockers, speed, CFR on Kuhn poker, Pluribus-style)

## Gotchas to test for
Split pots count as ties; A-2-3-4-5 is a straight (ace low); kickers; dead cards removed from every deal.
Sanity check: AA vs KK all-in preflop ≈ 82% / 18%.
