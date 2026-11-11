# Design decisions (fork points taken)

| Date | Decision | Alternatives considered | Why |
|---|---|---|---|
| 2026-11-11 | Main feature = beat-list ("who beats me right now") | Equity-first | Original project question; equity becomes an add-on |
| 2026-11-11 | Python backend (FastAPI on Vercel) | Static site with engine ported to JS | One engine to maintain (no Python→JS port to keep in sync); more Python practice. Browser port stays open as R&D Level 3 |
| 2026-11-11 | Cards stored as ints 0–51 | Card class (OOP), bitmasks | Speed (up to ~1M comparisons for 2 opponents); a class can wrap ints at the edges |
| 2026-11-11 | Ten written as "T" | "10" | Every card string is exactly 2 chars |
| 2026-11-11 | Vite + React + TS | Next.js | Fewer concepts while learning React |
| 2026-11-11 | Write own evaluator first, `treys` as cross-check | Library only | Learning; treys catches bugs |
| 2026-11-11 | Cap RUF scope at Phase 4 (ship); game theory shelved | Full R&D Levels 1–5 | RUF is a learn-to-ship side project; end goal is EBMs/MLIPs (docs/SCOPE.md) |
