---
type: concept
tags: [agents, agent-design, spec]
status: developing
source-count: 2
last-updated: 2026-10-14
---

# Seven-Part Agent Spec

The specification you capture by shadowing the human who does a job, before building anything, from [[agents-are-the-new-saas]].
Getting these seven parts right is what separates a real agent from "agent slop."

## The seven parts

1. **Trigger** - what wakes the agent up.
2. **Context** - what information it needs.
3. **Tools** - what it can use to act and read.
4. **Allowed actions** - what it may do itself.
5. **Approval** - where a human must sign off.
6. **Escalation** - when to bring a human into the loop.
7. **Success** - what a good outcome looks like.

## Why shadow first

Watch someone do the job across 10-20 cases, have them screen-record and narrate, and ask what makes a case easy, weird, or error-prone.
The surface request ("what time are you open?") usually hides a deeper workflow (kitchen hours, stroller-friendly tables, VIP routing). "The detail is the product."

## A marketing job spec (2026-10-14)

[[projects/Education/Marketing/wiki/sources/becoming-a-marketing-engineer|Becoming a Marketing Engineer]] (Marketing wiki) has the speaker write each agent's job "almost like I was hiring a person," and the fields line up closely:

| Seven-part spec | Marketing job spec |
|---|---|
| Trigger | When it runs |
| Context | The data source |
| Tools | (implied by the data source) |
| Allowed actions | What it filters out; where it writes results |
| Approval | What needs human approval |
| Escalation | (not named) |
| Success | Expected output, what good looks like, and **the metric that matters** |

Two differences are useful.
The marketing version splits success into an output check and a business metric (its competitor-engager agent is judged on positive replies from qualified accounts), and it adds **where results are written** so the system gets smarter next time.
It never names escalation, which this page treats as one of the two hardest questions.

## Synthesis

This is a design checklist that front-loads the two hardest agent-safety questions - approval and escalation - into the spec, before code.
It maps cleanly onto hcho's validation instinct: define success and failure boundaries first, then build to them. The trigger/context/tools/allowed/approval/escalate/success frame recurs across agent-engineering sources; treat it as a default template.
