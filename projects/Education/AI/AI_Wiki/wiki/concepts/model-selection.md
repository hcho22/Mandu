---
type: concept
tags: [models, workflow, claude, codex]
status: developing
source-count: 3
last-updated: 2026-07-08
---

# Model Selection (Opus vs Codex)

Practical guidance on which model to reach for, from [[inside-conductor-workflow]] and [[working-with-fable-5]].

## Rule of thumb

- **Codex / GPT-5.5 ([[openai]]) = the workhorse:** powers through a specific problem, unafraid to make many tool calls; good for long grindy debugging, bulk mechanical implementation, and (currently) computer use.
- **Claude / Opus / Fable ([[anthropic]]) = the partner/steerer:** more back-and-forth, more creative, better taste for user-facing work; the instinctive choice for new features and for orchestrating/reviewing.

## The glossary + ratings pattern ([[working-with-fable-5]])

Theo ([[theo-t3]]) encodes model choice directly in `CLAUDE.md` as a **glossary**: rate each model on the axes you care about and, crucially, *define what those axes mean to you* so the model applies your terms.
His three axes:

- **Intelligence** - the hardest problem it can handle unsupervised.
- **Taste** - UI/UX, code quality, API design, copy.
- **Cost** - to him, given his subscriptions.

Rough ratings he uses: Fable 5 best-in-class intelligence + taste but expensive; GPT-5.5 very high intelligence, low taste, effectively free; Opus 4.8 high intelligence, high taste, often cheap; "never use Haiku" for real work.
Two rules he attaches:

- **Ratings are defaults, not limits:** the model may override them and re-run with a smarter model without asking - "judge the output, not the price tag."
- **Do not let cost prevent using the right model** (he overrode the model's own auto-written "cost is a tiebreaker" line): use cheap models to gather info and try things, then move the real work to the better model.

## Synthesis

The reusable idea is that models have temperaments, so match the model to the task shape, not to a single default.
This underpins [[adversarial-code-review]]'s cross-model pattern (a different model reviews) and is the "which model" half of [[model-routing]]'s "how to orchestrate several at once" - selection picks, routing wires them together.
The glossary tactic generalizes beyond models: the highest-value part of a config is often defining your own vocabulary so the agent applies it consistently (a cousin of [[self-updating-config]]).
A related but separate decision is [[model-build-vs-buy]] ([[evaluate-ai-systems]]): temperament-based selection is *which model*; build-vs-buy is *which host* (self-hosted open-weight vs commercial API) along seven axes (privacy, lineage, performance, functionality, cost, control, on-device).
