---
type: concept
tags: [workflow, agentic-engineering, planning]
status: developing
source-count: 2
last-updated: 2026-07-28
---

# Plan, Code, Validate

The standard three-phase build loop, but with an unusual effort distribution, from [[building-products-with-agents]]: spend most time planning, hand coding almost entirely to agents, and automate validation.

## Key points

- **Plan depth buys autonomy.** The more comprehensive the plan, the longer agents run unattended: a short prompt bounces back constantly; a written **spec** runs longer; a **measurable goal** lets agents experiment on their own.
- **Write an objective definition of done.** [[every-claude-feature-ranked]]'s `/goal` runs until a condition is met with verification built in; subjective criteria ("very hard") weaken the loop, so use a metric where one exists. This is the same rubric idea as [[outcome-rubric-iteration]].
- **Code + validation form a loop the agent runs by itself,** which is what lets one delegation run a long time without the human.
- **Visual planning:** render the plan as an interactive HTML artifact so you click and annotate options rather than copy-pasting text feedback (HTML over Markdown when human-agent collaboration matters).
- Bake best practices ("push back on me," surface risks) into the planning tool itself, not a user-level config.

## Refinement: planning is not a phase (2026-07-28)

[[designing-loops-and-workflows]] agrees that the plan is the control knob but disputes its shape.
[[tharic]] argues there is no clean one-time handoff from spec to implementation now that agents read specs too, so "plan" is better understood as continuous exploration whose job is [[planning-is-removing-unknowns|getting rid of your unknowns]].
The cycle he describes is request, exploration, mockups and explainers, refine the spec, implement while keeping **implementation notes**, then re-spec from what those notes surfaced.

Reconciling the two datings: the original source (2026-07-08) says plan *depth* buys autonomy; the newer one (2026-07-28) says that depth is reached by iterating the plan against what the build discovers rather than by writing more of it before starting.
Both agree that a vague prompt bounces back constantly and that an objective definition of done is what lets an agent run long.

That same source also supplies the missing selection rule for the "objective definition of done" bullet.
Whether you can express the check deterministically decides your mechanism: deterministic signal takes `/goal`, subjective signal takes a workflow with a rubric and a separate verifier ([[verification-signal-picks-the-mechanism]]).
It independently confirms the visual-planning bullet as well, since HTML artifacts are used at Anthropic for plans, PRs, status reports, and incident reports.

## Synthesis

This is the operating model behind [[get-out-of-the-loop]]: the human's leverage moves to the front (planning) and the end (judgment), while the middle runs autonomously.
Plan depth as the control knob for autonomy is the same "constrain first" instinct as [[phased-implementation]] and [[phased-autonomy]], applied to the plan.
For hcho, the takeaway is that up-front spec quality - a validation-adjacent skill - is what makes agent delegation actually work.
The second source keeps that conclusion but changes the practice behind it: plan quality is not measured by how much you wrote before starting, it is measured by how few unknowns remain, and the cheapest way to retire unknowns is to make the agent explore and report rather than to specify harder in advance.
