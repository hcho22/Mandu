---
type: concept
tags: [reviewing-agent-work, mental-model, code-quality, validation]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Time-to-Fix as a Codebase Health Signal

From [[working-with-fable-5]]: read how long an agent takes to fix something (and how many files it touches) as a diagnostic of codebase health and problem difficulty, not just as latency.

## Key points

- Rough heuristic ([[theo-t3]]'s, personal but broadly useful):
  - **under ~3 min** - probably a simple, well-isolated fix; comfortable to file.
  - **~15 min** - "a little scary"; worth closer attention.
  - **an hour or more** - the architecture may be fragile; go deeper before trusting the diff.
- **Too fast is also a smell:** a 2-min fix that referenced a behavior he wasn't sure still existed turned out partly wrong. Both extremes warrant scrutiny.
- When the signal is off, reason about the **architecture and the request**, not just whether the diff reads correctly - and ask the model questions rather than guessing.

## Synthesis

This is a lightweight, agent-native quality signal that complements the wiki's verification family: [[adversarial-code-review]] and [[fresh-context-review]] check *whether* the code is right; time-to-fix tells you *where to look* and *how hard to look*.
It is a validation instinct rebadged for agentic work - the same "unusually long/short test time means investigate" reflex hcho would apply on a hardware bench, now pointed at agent runs.
Pairs with [[get-out-of-the-loop]]: as you review less line-by-line, cheap meta-signals like this help you allocate the scrutiny you keep.
