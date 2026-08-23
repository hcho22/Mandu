---
type: concept
tags: [agent-operations, loops, lean-startup, seo, ads, metrics]
status: developing
source-count: 2
last-updated: 2026-08-01
---

# Business Loops

The loop primitive pointed at **business metrics over months**, not at a codebase over minutes.

From [[loops-to-run-your-business]], with the ads case built out in full by [[building-marketing-agents]].

## It is not a new idea

The lineage is stated explicitly:

- **Lean Startup** (Eric Ries): the **build → measure → learn** loop.
- **Toyota / lean manufacturing**: the constantly-iterating assembly line that inspired it.
- **You already run loops.** Improving SEO - where do I rank, what can I fix, did I move up - is itself a loop with accurate feedback from Google.

**Any process running on a schedule is already a loop.**
"Loop engineering" is just getting an **agent** to run that build/measure/learn cycle for you.
Both speakers agree the surrounding hype and terminology are overblown even though the underlying idea is genuinely useful.

## The agent version

| Lean Startup | Agent loop |
|---|---|
| Build | Tell the AI to go do the thing |
| Measure | **Verify** - tests pass, a browser agent clicks through, an eval scores high enough, or a checker agent confirms |
| Learn | Feed the result back and iterate |

**A loop needs two things or it runs forever:** a defined **stop condition** and an **objective metric** fed back into the system.

**The key generalization:** the verify step does **not** have to be product or engineering related.
Any objective metric can close the loop - Google ranking, ad ROAS, retention.
**Pick the number first, then build the loop around it.**

## The three worked loops

- **SEO loop** (the anchor, because the metric is unambiguous): make improvements, check ranking, record what was tried in a **memory file**, and weeks or months later review whether the experiment moved the term up or down.
Because each change is just an experiment, a change that drops you can simply be undone.
SEO takes **months, not days** - results compound and can suddenly bear fruit around month four.
- **Ads loop:** generate variants, read performance, kill losers, double down on winners.
AI is weak at creative and strong at **text changes** - swapping a line of copy and measuring.
Give each variant **enough budget** for a statistically meaningful read.
- **Product-feedback loop** (called the "holy grail"): read customer feedback, pull analytics and error logs, prioritize pain points, prototype features, and judge against a KPI.
**Split it** - a **bug loop** on uptime, a **feature loop** on DAU/retention.
Still experimental and risky to run on a live business.

## Key points

- **These loops are long-horizon.** They may run once every few weeks for months or years, not continuously for half an hour.
"Infinite" means infinite over time, not an agent trapped in a real-time infinite loop.
- **The single easiest win, loops or not: connect your AI to your real tools and real data.**
- **Keep a memory file** logging every change so the next run can check its own past experiments.
- **Keep a human approval step** - have the agent ping you on Slack when a run finishes.
- Scheduling is what turns a prompt into a loop: Claude routines, Cursor automation, Codex automations.

## Synthesis

The important move is decoupling the loop from the codebase.
The wiki's earlier loop material ([[verification-signal-picks-the-mechanism]], [[designing-loops-and-workflows]]) is all software-development framing, and it quietly assumes the verifier is a test or a rendered UI.
Stating the rule as "pick the number first" makes the same machinery apply to anything with a metric, which is most of a business.

It also arrives at [[verification-signal-picks-the-mechanism]] from completely outside Anthropic, which is worth something: two sources with no shared context both conclude that **the available feedback signal is the design constraint.**

The tension to note is horizon.
[[building-at-the-frontier]] describes runs where the agent works continuously for days on one task; these run for ten minutes once a month for years.
Both are called loops, and they are structurally different animals - the distinction [[dynamic-workflows-as-test-time-compute]] draws between a workflow (one task, shared context) and a loop or routine (one repetitive task, no shared context) is the clean way to keep them apart.

For hcho the immediately actionable instance is SEO on the Agentic RAG landing page and waitlist, where the metric is objective, the cost is under $5 a run, and the current alternative is doing nothing.
See [[minimal-viable-loop]] for how to scope the first one and [[loop-cost-discipline]] for the spending guardrail.
