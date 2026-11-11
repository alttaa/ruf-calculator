# RUF — goals (defined 2026-11-11)

## Why this project exists
RUF is a **curiosity / learn-and-grow project**, not Alex's career end goal
(that lives in `~/.claude/rules/end-goal.md`: energy-based models + ML interatomic potentials).
Success = Alex can build, test, and ship a real Python + React project end to end,
and understands every line of it.

## The product question
"Given my hand and the board, how likely is it that an opponent **already has me beat**?"
Core test: J♠J♥ on K♥ Q♣ J♦ → 38 of 1,081 opponent hands beat hero (≈ 3.5%);
2 opponents ≈ 6.9%.

## Goals
1. **Ship it.** A public URL on Vercel that a friend can use on their phone.
2. **Learn Python project skills:** packages, venv, pytest, git, CLI entry points, reading tracebacks.
3. **Learn React basics:** components, state, props, fetch, loading/error states.
4. **Learn web basics:** what an API is, JSON, request/response, deploys, environment differences.
5. **Build probability intuition that transfers to the end goal:**
   - probability = weight / sum over all states (1,081 here; Z in a Boltzmann distribution)
   - exact enumeration vs Monte Carlo, and error bars that shrink like 1/√n
   - conditioning = filter the sample space, then re-normalize
6. **Build working habits:** small steps, a test for every function, `/start` and `/checkpoint` every session.

## Not goals
- Competing with commercial poker tools.
- Poker strategy / game theory (CFR, Pluribus). Interesting, but a different branch from the end goal.
- Perfect performance or polish beyond "works, correct, readable".
