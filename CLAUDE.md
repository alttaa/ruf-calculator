# CLAUDE.md — "R U F***ed" Poker Calculator

## What this project is
A public website that answers: **"Given my hand and the board, how likely is it that an opponent already has me beat?"**

Purely probability-based: no opponent actions, betting, or reads. Just card counting over every possible opponent hand.

Nickname: "R U F***ed" (RUF), i.e. "are your opponents beating you?"

## The owner
- Goes by Alex. Learning **Python** and **React** through this project, so treat it as a learning project.
- Explain things in **short chunks, one idea at a time, concrete numbers before abstract symbols**.
- Prefer letting Alex write code with guidance over dumping large finished files, unless asked.

## Core example (use as the first test case)
- Hero holds **J♠ J♥**. Flop: **K Q J rainbow** (all different suits).
- Unseen cards: 52 − 5 = **47**. Possible opponent hands: C(47,2) = **1081**.
- Hands that beat hero right now:

| Hand | Combos | Why |
|---|---|---|
| AT | 16 | Broadway straight |
| T9 | 16 | Straight |
| KK | 3 | Higher set |
| QQ | 3 | Higher set |
| **Total** | **38** | 38/1081 ≈ **3.5%** per opponent |

- Two opponents: P(at least one beats hero) ≈ **7%**.
- Terminology: call these **"beating hands"**, not "outs" (outs = cards that improve *your* hand).

## Math approach
- Brute-force enumeration: for each possible opponent hand, compare against hero's hand and count winners.
- At most 1081 hands per opponent, which is instant in a browser.
- "Bayesian" conditioning = **filtering** the list of possible hands, then recounting. No closed-form formulas needed.
- For multiple opponents, deal hands without replacement (opponents can't share cards). Exact enumeration or Monte Carlo are both fine.

## Features (build order)
1. **Card picker**: select hero's 2 cards + board (flop/turn/river).
2. **Beat-list engine**: list beating hands grouped by type, with combos and %.
3. **Multiple opponents** (2–9): P(at least one has hero beat).
4. **Dead cards**: mark cards believed folded (e.g. "a queen was folded"), removed from the deck.
5. **Range constraints**: e.g. "opponent holds exactly one queen", which filters opponent hands before counting.
6. *(Optional)* Turn/river projections.

## Tech plan
- **Python** (`/python`): prototype + verify the math first. Must reproduce 38/1081 for the core example.
  - Hand evaluator: write our own (learning), with `treys` as a fallback/cross-check.
- **React + JavaScript** (`/web`): the actual site. Port verified logic from Python.
  - Hand evaluator fallback: `pokersolver`.
- **Static site only**: no backend, no database, no sign-in. All computation runs in the browser.
- **Hosting**: GitHub → Vercel / Netlify / GitHub Pages.

## Milestones
1. Repo set up + first commit (README, .gitignore, this file)
2. Python hand evaluator: compares two hands correctly
3. Python beat-list for the core example → 38/1081
4. React app scaffold + card picker
5. JS engine ported, beat-list shown in UI
6. Multi-opponent + dead cards
7. Range constraints + polish + publish

## Suggested repo layout
```
/
├── CLAUDE.md
├── README.md
├── .gitignore
├── python/        # math prototype + tests
└── web/           # React site (added at milestone 4)
```

## Current status
Planning done. Next step: create the GitHub repo and make the first commit.
