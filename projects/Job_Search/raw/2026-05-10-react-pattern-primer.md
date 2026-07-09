# The ReAct Pattern: A Primer

*Published 2026-05-10 by Mira Sato on The Agent Engineer*

LLM agents have converged on a small number of control-flow patterns over the last two years. The most durable of these is **ReAct** — short for "Reasoning and Acting" — introduced by Yao et al. in 2022. Despite being one of the oldest agent patterns, it remains the default loop in frameworks like LangGraph, AutoGen, and CrewAI in 2026.

## The pattern

ReAct interleaves three steps in a loop:

1. **Thought** — the LLM writes a short natural-language reasoning step.
2. **Action** — the LLM picks a tool to call and emits its arguments.
3. **Observation** — the result of the tool call is fed back into the context.

The loop continues until the model emits a `Finish` action with the final answer. The key trick is that **the thought is visible in the trajectory**, so the model can refer back to its own prior reasoning on the next step.

## Why it's stuck around

Three reasons.

First, ReAct works with any tool-calling LLM, including small ones. Unlike planner-executor architectures, you don't need a dedicated planning model.

Second, ReAct trajectories are **legible**. A human reviewer reading a ReAct trace can usually understand why the agent did what it did. This matters enormously for debugging — and increasingly for compliance.

Third, ReAct degrades gracefully. When a tool call fails, the model sees the error in the next Observation and can recover. Planner-executor agents tend to commit to a plan and then flail when it goes off the rails.

## When ReAct breaks down

The ceiling is roughly 10-15 tool calls in a single trajectory. Beyond that, context window pressure and reasoning drift become real problems. For long-horizon tasks (think: "research this topic over 50 sources"), you need either subagents (decompose the task) or explicit memory (offload prior thoughts to a store).

The other common failure mode is **tool over-selection**: when the agent has 30+ tools available, ReAct's per-step selection accuracy drops sharply. The fix is either tool retrieval (only show the agent the top-K relevant tools per step) or hierarchical tools (group related tools behind a router tool).

## Variants in the wild

- **ReAct + Reflection** — after a Finish, run a critique pass that can re-open the loop. Used heavily in coding agents.
- **ReAct + Replanning** — periodically inject a "stop and plan" step. Bridges ReAct and planner-executor.
- **Parallel ReAct** — fan out multiple ReAct trajectories, then merge. Used in deep-research agents.

For a 2026 agent, ReAct is still the right default. Reach for fancier architectures only when you've measured ReAct hitting one of its known walls.

---

*Mira Sato writes The Agent Engineer, a weekly newsletter on agent infrastructure.*
