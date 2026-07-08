---
type: concept
tags: [agentic-engineering, workflow, scale, validation]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Get Out of the Loop

The central philosophy of [[building-products-with-agents]] (and lived out in [[working-with-fable-5]]): a human who inspects every line an agent produces becomes the rate limiter for the whole system, so move yourself out of the agent's loop wherever possible.

## Key points

- As agents write ~10x more PRs than a human used to, human-in-the-loop review of everything does not scale.
- The guest stopped reading first-pass agent code and reached a point where his review "never catches anything the agents don't."
- The human is needed mainly at the start (planning) and end (judgment) of a task; parallelism ([[sub-agents]], many sessions) is a forcing function to move yourself out of the loop.
- **At scale ([[working-with-fable-5]]):** Theo set a long-running "goal" that ran ~5 hours and merged a month of work while he checked GitHub from his phone; he then burned *more tokens verifying* (spinning up agents to test features and diff prod vs main) than producing. Leaving the loop was only safe behind a staging-only merge boundary and automated reviewers ([[adversarial-code-review]]) - the checking that replaces his review.

## Synthesis

Getting out of the loop is only safe if something replaces your review, which is why this concept is the demand that creates the wiki's entire verification family: [[adversarial-code-review]], [[fresh-context-review]], the [[skill-eval-loop]], and [[agent-testing-instructions]] are all mechanisms for removing the human without removing the checking.
It reframes hcho's validation edge from "review the output" to "build the automated reviewer" - a higher-leverage, more hireable framing.
The counter-note in the source (some teams stopped reviewing entirely and ship less stable products) is exactly why the automated-reviewer half matters.
