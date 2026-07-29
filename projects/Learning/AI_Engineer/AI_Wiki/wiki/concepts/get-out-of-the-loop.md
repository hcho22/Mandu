---
type: concept
tags: [agentic-engineering, workflow, scale, validation]
status: developing
source-count: 3
last-updated: 2026-07-28
---

# Get Out of the Loop

The central philosophy of [[building-products-with-agents]] (and lived out in [[working-with-fable-5]]): a human who inspects every line an agent produces becomes the rate limiter for the whole system, so move yourself out of the agent's loop wherever possible.

## Key points

- As agents write ~10x more PRs than a human used to, human-in-the-loop review of everything does not scale.
- The guest stopped reading first-pass agent code and reached a point where his review "never catches anything the agents don't."
- The human is needed mainly at the start (planning) and end (judgment) of a task; parallelism ([[sub-agents]], many sessions) is a forcing function to move yourself out of the loop.
- **At scale ([[working-with-fable-5]]):** Theo set a long-running "goal" that ran ~5 hours and merged a month of work while he checked GitHub from his phone; he then burned *more tokens verifying* (spinning up agents to test features and diff prod vs main) than producing. Leaving the loop was only safe behind a staging-only merge boundary and automated reviewers ([[adversarial-code-review]]) - the checking that replaces his review.

## Counterweight: the operator's attention is also a limit (2026-07-28)

[[designing-loops-and-workflows]] pushes back on the parallelism half of the third bullet above, and it is worth recording rather than smoothing over, because it comes from inside Anthropic's [[claude-code]] team.

- [[tharic]] previously ran about **five parallel Claude Code sessions** and has **cut back to one active session** plus multiple background Claude-in-Slack sessions.
- The host describes running five simultaneous threads as exhausting and "worse than back-to-back meetings."
- Tharic's stated aim is "to be more productive, but work less," and his practice is one primary project at a time with background work running alongside.
- He names his own biggest time-waster as being "a little bit lazy," giving a weak prompt, and having to redo the work, which is a cost that rises with the number of threads you are splitting attention across.

Dating the two claims: [[building-products-with-agents]] (filed 2026-07-08) frames parallelism as a forcing function that pushes you out of the loop; this source (2026-07-28) finds a ceiling where added parallelism degrades the human's prompt quality and judgment faster than it adds throughput.
These are compatible if you separate the two exits: parallelism forces you out of *line-by-line review*, which is the point, but it does not scale your capacity for *direction and judgment*, which is what [[read-what-the-agent-writes]] says you must not exit.

## Synthesis

Getting out of the loop is only safe if something replaces your review, which is why this concept is the demand that creates the wiki's entire verification family: [[adversarial-code-review]], [[fresh-context-review]], the [[skill-eval-loop]], [[self-referential-bias]], and [[agent-testing-instructions]] are all mechanisms for removing the human without removing the checking.
It reframes hcho's validation edge from "review the output" to "build the automated reviewer" - a higher-leverage, more hireable framing.
The counter-note in the source (some teams stopped reviewing entirely and ship less stable products) is exactly why the automated-reviewer half matters.

The third source sharpens the concept's boundary.
"Get out of the loop" is a claim about *verification*, not about *attention*, and the two get conflated because both look like stepping back.
The strongest current reading is that the loop you exit is the review loop, the loop you cannot exit is the judgment loop, and the number of parallel agents you can usefully run is capped by the second, not the first.
An insider running one active session while advocating longer autonomous runs is the clearest available evidence that these are separate dials.
