---
type: concept
tags: [agents, agent-design, workflows, anthropic]
status: developing
source-count: 2
last-updated: 2026-08-05
---

# Start as a Workflow, Earn Autonomy

The design principle, attributed in [[agents-are-the-new-saas]] to [[anthropic]]'s agent guidance, that many "agent" problems should start as workflows and add dynamic judgment only when it creates value.

## Key points

- A **workflow** follows a predictable, pre-defined path; an **agent** decides more dynamically at runtime.
- Most problems are better served by starting predictable, then adding autonomy incrementally - you "earn" autonomy rather than assuming it.
- This is the same instinct as the [[minimal-useful-agent]] ladder (draft to act): begin at the constrained end.
- [[graph-engineering-isenberg]] restates it as a build discipline from the operator side: **"draw the graph before you automate the graph,"** and run the workflow manually and successfully three times before reaching for LangGraph or a framework - "if you automate a workflow you do not understand, you get a mess." Same principle, one level more concrete: earn the automation, not just the autonomy.

## Synthesis

This is the counterweight to demo-driven over-scoping: reliability comes from constraining the decision space, and you widen it only where the data shows judgment pays off.
It connects the agent-business playbook to the broader craft, and it is worth pairing with [[evals]] - the eval set is how you decide whether an added degree of autonomy actually improved outcomes.
The build-time counterpart is now its own page, [[single-call-workflow-or-agent]] (pick the least-powerful architecture per feature: single call, fixed workflow, or agent); Anthropic's "Building Effective Agents" is the primary reference behind both ([[zero-to-hireable-ai-engineer]] names it the must-read before writing agent code).
