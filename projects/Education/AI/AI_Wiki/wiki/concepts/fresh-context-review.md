---
type: concept
tags: [validation, code-review, context-engineering, evals]
status: developing
source-count: 2
last-updated: 2026-07-28
---

# Fresh-Context Review

The principle from [[building-products-with-agents]] that AI-generated work should be reviewed in a **fresh context window**, because a reviewer that saw every step of the work is biased toward believing it is correct and misses edge cases.

## Key points

- The No Mistakes pipeline reviews each change in a clean context, with an "Intent" phase that hands the fresh reviewer just enough context - like a principal engineer reviewing with fresh eyes after a brief explanation.
- Same-session self-review underperforms because the model already "believes" its work.
- The reviewer is heavily prompt-engineered for high recall on bugs, logical errors, and edge cases, and presents test evidence (screenshots/video).

## Fresh context is half the fix ([[designing-loops-and-workflows]])

An Anthropic [[claude-code]] team member names the same effect as [[self-referential-bias]] and prescribes varying **two** things, not one: the verifying agent should have different context *and* a different model from the producing agent.

That distinction matters for this page.
Clearing the context window removes the reviewer's *belief* that the work is correct, which is what this page's original source identified.
It does not remove the model's *preference* for its own style of output, which the eval literature measures directly ([[llm-as-judge]]: GPT-4 about +10%, Claude-v1 about +25% self-win rate).
Fresh context is therefore necessary but not sufficient, and the fuller prescription is three roles with different context and different models: one coordinating, one doing, one verifying.

## Synthesis

This is the unifying principle beneath several earlier pages: it is why the [[skill-eval-loop]] runs its grader in a separate agent, why [[context-rot]] motivates fresh sessions, and what makes [[adversarial-code-review]] work (a different model, or a fresh context, does not share the original's blind spots).
It is the strongest single import for hcho: "review in fresh context" is a concrete, teachable validation technique, and productizing it (as No Mistakes does) is exactly the automated-reviewer artifact that [[get-out-of-the-loop]] requires.
With the second source, the technique's mechanism is now named and generalized in [[self-referential-bias]]: this page is the context-variable case of that broader constraint, and the practical upgrade is to vary the model too wherever the check actually matters.
