---
type: concept
tags: [ai-career, job-search, portfolio, positioning, fde]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Do the Job Before You Have the Title

The organizing principle of the 30-day roadmap in [[fde-in-30-days]]:
build a complete case study **before** you have the job title, so that by day 30 you don't just understand the role conceptually - you have **tangible proof you can do it**.

## The 30-day spec

**Week 1 - build a working agent.**
One **real enterprise workflow** end to end (finance, HR, procurement, logistics, IT, sales).
Learn roughly one building block per day: agent looping, tool usage, guardrails, context and memory, and an **audit trail** logging every prompt, response, tool call, and error.
*"If you can't show the client what the agent is doing, they will never trust you."*
**Checkpoint:** a working agent with tools, guardrails, deliberate memory, and a full audit trail.

**Week 2 - make it recoverable.**
Defined JSON schema with every response validated, explicit failure handling, and checkpointing so it resumes rather than restarts ([[solve-for-the-exceptions]]).
**Checkpoint:** a resumable agent with structured outputs, state recovery, and explicit failure behavior.

**Week 3 - measure and optimize.**
A **golden dataset of 20+ real queries** with evals for correctness, format, tool selection, and escalation behavior.
Route simpler subtasks to cheaper models.
Add multi-agent coordination only when decomposition genuinely helps.
Measure impact in exactly **three buckets: revenue uplift, risk mitigation, cost savings** - the only categories that matter to a business.
**Checkpoint:** an evaluated agent with known failure modes, measured cost, and a golden dataset.

**Week 4 - communicate and defend.**
Document the pain point, why AI belongs there, the architecture, and the **iteration history** ("accuracy went from 70% to 95%").
**Rehearse the pitch two ways: as an engineer** (architecture, decisions, tradeoffs) **and as a VP** (problem, outcome, evidence, risk).
Actually pitch it to real businesses; they'll tell you whether your economics and framing are right.
**Checkpoint:** a case study defensible to both engineers and executives.

## The entry tactic

**Do the first audit for free.**
Get your foot in the door, prove value, and only get paid once you've demonstrated measurable value.
Early customers "are genuinely worth more to you than you are to them"; after 2-3 proven engagements you can start charging.

## Synthesis

The wiki already holds the general version of this - [[t-shaped-portfolio]], [[build-in-public]], [[zero-to-hireable-ai-engineer]]'s build-first path, and [[career-switch-mistakes]]'s skill-first antidote.
What this adds is a **specification with checkpoints**, which is a different kind of object from advice.

The Week 4 requirement is the genuinely differentiated part, and the one most portfolios skip.
Documenting the **iteration history** - not the final architecture but the path from 70% to 95% - is what demonstrates method rather than outcome, and it is exactly what an evals-quality interviewer is trying to find out.
So is the two-audience rehearsal, which maps onto [[two-kinds-of-judgment]]: the engineer pitch and the VP pitch are the two columns, and being unable to give one of them is the diagnostic.

For hcho the practical observation is that **much of this is already built**.
The Agentic RAG work covers Week 1 (agentic system with tools and guardrails) and substantial parts of Week 3 (eval harness, leak suite, escalation golden set, CI gate).
The gaps are narrower than the plan implies: an explicit **audit trail** framed as a trust artifact rather than as debugging, Week 2's failure-handling and resumability stated as a deliberate feature, the **three-bucket business framing**, and the Week 4 packaging - iteration history plus a rehearsed VP-level pitch.

That reframes the flagship from "a product I am validating" to "a product I am validating **that is also an FDE case study**," at close to zero extra cost.
Given the job search runs as a parallel hedge, extracting the case study from work already done is the highest-leverage move this batch suggests.
