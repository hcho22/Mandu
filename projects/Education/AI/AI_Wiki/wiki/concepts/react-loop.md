---
type: concept
tags: [agents, agent-architecture, craft]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# ReAct Loop

The core control loop of an agent: reason, decide on a tool use, act, observe the result, and repeat until done.
Introduced in the wiki via [[ai-era-50-career-tips]], which recommends learning it by reading real open-source agents rather than reinventing it.

## Key points

- Structurally it is a while-loop: the model reasons about the goal, chooses a tool (or decides it is finished), the tool runs, the result is fed back, and the loop continues.
- It is the mechanism beneath [[agentic-engineering]] and the [[minimal-useful-agent]] ladder: "act" agents are ReAct loops with tightly bounded tools.
- Recommended study path: read open-source agent implementations to see how the loop, tool schemas, and stopping conditions are actually built.

## Synthesis

The ReAct loop is the "hard pattern worth reading" that the career talk singles out, and it is the concrete bridge between the agent-business framing ([[agent-saas]], [[seven-part-agent-spec]]) and how an agent actually runs.
Pair it with [[evals]]: the loop's tool calls and stopping conditions are exactly what an agent eval set probes.
Deepen this page when a primary agent-architecture source (e.g. Anthropic's building-agents guidance) is ingested.
