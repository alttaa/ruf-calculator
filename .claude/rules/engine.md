---
paths:
  - "python/**/*.py"
---

# Engine conventions

- Cards are ints 0–51: `card = rank * 4 + suit`.
  Ranks "23456789TJQKA" -> 0..12, suits "cdhs" -> 0..3. Ten is "T"; every card string is 2 chars.
- Integers inside the engine (speed). A readable Card class only at the edges, if ever.
- The engine never imports FastAPI, React, or anything web-related.
- Gotchas every evaluator/equity change must be tested against:
  - split pots count as ties (partial wins), not losses
  - A-2-3-4-5 is a straight (ace low)
  - kickers decide ties between equal pairs
  - dead/known cards are removed from every deal
- Core test: JsJh on Kh Qc Jd -> 38 of 1081 opponent hands beat hero (AT 16, T9 16, KK 3, QQ 3).
- Later equity sanity check: AA vs KK all-in preflop ≈ 82% / 18%.
