---
type: concept
tags: [agentic-engineering, workflow, scale, validation]
status: established
source-count: 7
last-updated: 2026-09-23
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

## Where the exits stop (2026-08-01)

Three more sources sharpen the boundary further, and all three exit *further* on implementation while explicitly refusing to exit somewhere else.

- **Out of the tool calls, but not the plan** ([[agentic-full-stack-build]]).
Kun runs a "calm mode" that hides all tool calls, script runs, and skill invocations, and never reads source code across an entire full-stack build - while reviewing every plan as an interactive artifact ([[review-plans-as-artifacts]]).
His justification is dated: watching tool calls was useful with weaker models and the noise is no longer worth reading.
But the two interventions that mattered were both **scope and cost judgments** ([[agent-over-engineering]], [[anchor-cost-in-real-pricing]]) - so what he could not delegate was deciding how much system the situation deserved.
- **Out of the code, but not out of the product** ([[running-teams-of-ai-agents]]).
[[ryan-carson]] automates browser QA, production digests, and rubric-graded self-improvement, and still says: "There's no substitute, and we probably won't have a substitute for a while, for you using your own app."
Even the smartest models still lack the sense of *obvious*.
He also names the real cost of the exit: **observability is the hard part, not the automation.**
- **Out of the scaffolding entirely** ([[building-at-the-frontier]]).
[[boris-cherny]]'s prescription is the furthest exit recorded here - describe the **task, the guardrails, and the exit criteria**, then let the model cook and check back later, for days or weeks ([[long-horizon-agent-runs]]).
The condition is unchanged and absolute: a verification loop the model can run on itself.

The pattern across six sources is now stable enough to state as a rule.
**You can exit any loop you can replace with a check, and no loop you cannot.**
Line-by-line review is replaceable ([[adversarial-code-review]]). Scope judgment, product feel, and direction are not - because no one has built the oracle for them.

## Explicit counter-position: keep reading consequential code (2026-09-23)

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] recommends evidence review and a skim for genuinely isolated leaf changes, but deep human review for shared infrastructure and consequential behavior.
That directly qualifies the blanket statement above that line-by-line review is replaceable.
The provisional reconciliation is risk-dependent review, captured by [[risk-based-agent-governance]], not a universal exit from reading code.
Executable checks cover known requirements; passing them does not demonstrate that every consequential failure mode was specified.
The new source is an undated secondary guide, so this records a substantive disagreement rather than an empirical verdict.

## Synthesis

Getting out of the loop is only safe if something replaces your review, which is why this concept is the demand that creates the wiki's entire verification family: [[adversarial-code-review]], [[fresh-context-review]], the [[skill-eval-loop]], [[self-referential-bias]], and [[agent-testing-instructions]] are all mechanisms for removing the human without removing the checking.
It reframes hcho's validation edge from "review the output" to "build the automated reviewer" - a higher-leverage, more hireable framing.
The counter-note in the source (some teams stopped reviewing entirely and ship less stable products) is exactly why the automated-reviewer half matters.

The third source sharpens the concept's boundary.
"Get out of the loop" is a claim about *verification*, not about *attention*, and the two get conflated because both look like stepping back.
The strongest current reading is that the loop you exit is the review loop, the loop you cannot exit is the judgment loop, and the number of parallel agents you can usefully run is capped by the second, not the first.
An insider running one active session while advocating longer autonomous runs is the clearest available evidence that these are separate dials.
