---
type: concept
tags: [agents, agent-design, spec]
status: seed
source-count: 1
last-updated: 2026-07-08
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

## Synthesis

This is a design checklist that front-loads the two hardest agent-safety questions - approval and escalation - into the spec, before code.
It maps cleanly onto hcho's validation instinct: define success and failure boundaries first, then build to them. The trigger/context/tools/allowed/approval/escalate/success frame recurs across agent-engineering sources; treat it as a default template.
