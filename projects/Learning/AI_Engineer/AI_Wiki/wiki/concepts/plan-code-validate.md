---
type: concept
tags: [workflow, agentic-engineering, planning]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Plan, Code, Validate

The standard three-phase build loop, but with an unusual effort distribution, from [[building-products-with-agents]]: spend most time planning, hand coding almost entirely to agents, and automate validation.

## Key points

- **Plan depth buys autonomy.** The more comprehensive the plan, the longer agents run unattended: a short prompt bounces back constantly; a written **spec** runs longer; a **measurable goal** lets agents experiment on their own.
- **Write an objective definition of done.** [[every-claude-feature-ranked]]'s `/goal` runs until a condition is met with verification built in; subjective criteria ("very hard") weaken the loop, so use a metric where one exists. This is the same rubric idea as [[outcome-rubric-iteration]].
- **Code + validation form a loop the agent runs by itself,** which is what lets one delegation run a long time without the human.
- **Visual planning:** render the plan as an interactive HTML artifact so you click and annotate options rather than copy-pasting text feedback (HTML over Markdown when human-agent collaboration matters).
- Bake best practices ("push back on me," surface risks) into the planning tool itself, not a user-level config.

## Synthesis

This is the operating model behind [[get-out-of-the-loop]]: the human's leverage moves to the front (planning) and the end (judgment), while the middle runs autonomously.
Plan depth as the control knob for autonomy is the same "constrain first" instinct as [[phased-implementation]] and [[phased-autonomy]], applied to the plan.
For hcho, the takeaway is that up-front spec quality - a validation-adjacent skill - is what makes agent delegation actually work.
