---
type: concept
tags: [validation, code-review, context-engineering, evals]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# Fresh-Context Review

The principle from [[building-products-with-agents]] that AI-generated work should be reviewed in a **fresh context window**, because a reviewer that saw every step of the work is biased toward believing it is correct and misses edge cases.

## Key points

- The No Mistakes pipeline reviews each change in a clean context, with an "Intent" phase that hands the fresh reviewer just enough context - like a principal engineer reviewing with fresh eyes after a brief explanation.
- Same-session self-review underperforms because the model already "believes" its work.
- The reviewer is heavily prompt-engineered for high recall on bugs, logical errors, and edge cases, and presents test evidence (screenshots/video).

## Synthesis

This is the unifying principle beneath several earlier pages: it is why the [[skill-eval-loop]] runs its grader in a separate agent, why [[context-rot]] motivates fresh sessions, and what makes [[adversarial-code-review]] work (a different model, or a fresh context, does not share the original's blind spots).
It is the strongest single import for hcho: "review in fresh context" is a concrete, teachable validation technique, and productizing it (as No Mistakes does) is exactly the automated-reviewer artifact that [[get-out-of-the-loop]] requires.
