---
type: concept
tags: [agents, workflow, agent-design, judgment, architecture]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Single Call, Workflow, or Agent

From [[zero-to-hireable-ai-engineer]]: knowing when NOT to use an agent is one of the most overlooked skills in the field, and reaching for the simplest thing that works is a sign of judgment, not timidity.

## The decision framework

- **Single model call** - if the task fits in one prompt with the right context.
- **Fixed workflow** - a chain of steps you define, if the steps are predictable. The large, productive middle ground: chaining (one call's output feeds the next), routing (classify then send to a specialized handler), parallelization (run several, combine).
- **Agent** - only when the number of steps is genuinely unpredictable and needs the model to decide dynamically at runtime.

Rule of thumb: a chain of three fixed calls is always faster, cheaper, and easier to debug than an agent that *might* make three calls. Agents are slower, pricier, less predictable, and harder to debug - reserve them for open-ended tasks.

## Synthesis

This is the build-time twin of [[start-as-a-workflow]]: that concept says agent *products* should begin predictable and earn autonomy; this one says at the level of a single feature, pick the least-powerful architecture that solves it.
Both push the same way - constrain the decision space by default - and both connect to [[evals]] (the eval set is how you justify adding a step of autonomy) and [[model-selection]] / [[reasoning-effort-discipline]] (don't over-spend capability on a simple task).
For hcho it is a crisp interview-ready judgment heuristic and a design default for the Agentic RAG work: most "agent" asks are really workflows.
