---
type: concept
tags: [agentic-engineering, agents, craft, tooling]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# Agentic Engineering

The emerging expertise of getting agents to do more work on your behalf, named in [[ai-era-50-career-tips]] as one of the most important new skills.
As models improve, the leverage is in the "meta work" around them, not in hand-writing code.

## The pillars

- **Context engineering** - loading the right information into the model's working context (memory, retrieval, context-window management).
- **Agentic validations** - checking agent output automatically; this is the [[evals]] discipline applied to agents.
- **Agentic tooling** - building the tools the agent uses to act (the [[react-loop]] is the underlying pattern).
- **Compound engineering** - stacking agents, sub-agents, and loops so work compounds.

## Key points

- Mastering the agent harness (Claude Code / Codex): how it loads memory, manages context, plus slash commands, skills, sub-agents, agent teams, and scheduled loops. The talk claims tool mastery alone can get you hired.
- Andrej Karpathy ([[andrej-karpathy]]) frames tool-use skill as a genuine skill gap.
- Agents are only this capable because the modern stack is [[everything-as-code-abstractions|everything-as-code]] ([[building-robust-apps-with-ai]]): agentic engineering on production infra depends on platforms an agent can operate in code, so it is inseparable from [[system-design]].

## Synthesis

This is the umbrella skill that ties the wiki's craft hubs together: [[evals]] (as agentic validation), [[agent-saas]] (as the productization of agents), and the [[react-loop]] (as the mechanism).
For hcho it reframes "learn Claude Code deeply" from a productivity tip into a hireable core competency, and its "agentic validations" pillar is his validation background restated in the newest vocabulary.
As dedicated Claude Code / agent sources are ingested, this concept may graduate into its own area hub.
