# CLAUDE.md — "R U F***ed" Poker Calculator

## What this project is
A public website that answers: **"Given my hand and the board, how likely is it that an opponent already has me beat?"**

Purely probability-based: no opponent actions, betting, or reads. Just card counting over every possible opponent hand.
Nickname: "R U F***ed" (RUF), i.e. "are your opponents beating you?"
No sign-in, no database.

## The owner
Alex, learning **Python** and **React** through this project, so treat it as a learning project.
RUF is a side project; Alex's end goal (EBMs + MLIPs) is in `~/.claude/rules/end-goal.md`.
How to teach Alex: `.claude/rules/teaching.md` (always loaded).

## Goals and scope (respect the cap: don't build anything listed as OUT)
@docs/GOALS.md
@docs/SCOPE.md

## Where we are (always read first)
@docs/PROGRESS.md

## Core example (the first test case)
- Hero holds **J♠ J♥**. Flop: **K♥ Q♣ J♦** (rainbow: all different suits).
- Unseen cards: 52 − 5 = **47**. Possible opponent hands: C(47,2) = **1081**.
- Hands that beat hero right now:

| Hand | Combos | Why |
|---|---|---|
| AT | 16 | Broadway straight |
| T9 | 16 | Straight |
| KK | 3 | Higher set |
| QQ | 3 | Higher set |
| **Total** | **38** | 38/1081 ≈ **3.5%** per opponent |

- Two opponents: P(at least one beats hero) ≈ **6.9%** (exact enumeration: 1,070,190 deals).
  Not exactly 1 − (1 − 0.035)², because opponents draw from the same deck.
- Terminology: call these **"beating hands"**, not "outs" (outs = cards that improve *your* hand).

## Math approach
- Brute-force enumeration: for each possible opponent hand, compare against hero's hand and count winners.
- At most 1081 hands per opponent, so it's instant.
- "Bayesian" conditioning = **filtering** the list of possible hands, then recounting. No closed-form formulas needed.
- Multiple opponents: deal hands without replacement (opponents can't share cards). Exact enumeration or Monte Carlo.
- Later: equity (win/tie/lose % over turn + river runouts) as an add-on feature.

## Features (build order)
1. **Beat-list engine** (Python): beating hands grouped by type, with combos and %.
2. **Multiple opponents** (2–9): P(at least one has hero beat).
3. **Dead cards**: cards believed folded (e.g. "a queen was folded"), removed from the deck.
4. **Range constraints**: e.g. "opponent holds exactly one queen", which filters opponent hands before counting.
5. **Card picker UI**: hero's 2 cards + board (flop/turn/river).
6. *(Optional, after shipping)* Turn/river projections and equity.

## Tech plan (decided 2026-11-11: Python backend)
- **Engine** (`python/ruf_engine/`): pure Python math. Never imports web code. Single source of truth.
  - Hand evaluator: write our own (learning), with `treys` as a cross-check.
- **API** (`api/`, later): FastAPI `POST /api/beat-list`, Pydantic schemas, stateless.
- **Web** (`web/`, later): Vite + React + TypeScript; calls the API.
- **Hosting**: GitHub → one Vercel project (static frontend + Python function).
- Fork point kept open: port the engine to the browser later (see docs/DECISIONS.md).
- Full roadmap: `docs/RUF_roadmap.pdf`.

## Repo layout
```
/
├── CLAUDE.md
├── README.md
├── .claude/          # rules + /start /checkpoint /quiz
├── docs/             # PROGRESS, SESSION_LOG, DECISIONS, roadmap
├── python/
│   ├── ruf_engine/   # the engine package
│   ├── tests/        # pytest tests
│   └── requirements.txt
├── notebooks/        # scratch Jupyter notebooks (not tests)
├── resources/        # papers
├── api/              # FastAPI (added at Phase 2)
└── web/              # React site (added at Phase 3)
```

## Commands
- Activate env (from `python/`): `conda deactivate` (if `(base)` shows), then `source .venv/bin/activate`
- Run tests (from `python/`): `python -m pytest -q`

## Session workflow
- Start of session: Alex runs `/start`.
- End of session: Alex runs `/checkpoint`. Never end a session with docs/PROGRESS.md out of date.
- `/quiz <topic>` for review questions.
