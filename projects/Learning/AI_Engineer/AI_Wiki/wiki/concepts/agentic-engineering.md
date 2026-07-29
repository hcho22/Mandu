---
type: concept
tags: [agentic-engineering, agents, craft, tooling]
status: developing
source-count: 2
last-updated: 2026-07-28
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

## Primary-source confirmation ([[designing-loops-and-workflows]])

The first insider account in the wiki ([[tharic]], Anthropic [[claude-code]] team) fills in three of the four pillars with specifics:

- **Context engineering** - [[principles-over-constraints]]: as models get smarter they need less direction, fewer constraints, and fewer examples, and Anthropic cut the Claude Code system prompt by 80% on that basis. Most `CLAUDE.md` files and skills are judged too long.
- **Agentic validations** - [[self-referential-bias]] makes a separate verifying agent a structural requirement, not a nicety, and [[verification-signal-picks-the-mechanism]] decides which orchestration primitive you can even use.
- **Compound engineering** - the concrete primitives are `/loop`, `/goal`, and workflows; workflows are a JS file that can be packaged into a skill, joining [[building-skills]] to [[sub-agents]] in one artifact.

The pillar it complicates is the implied "more agents is more leverage" reading: Tharic runs one active session rather than five (see [[get-out-of-the-loop]]).

## Synthesis

This is the umbrella skill that ties the wiki's craft hubs together: [[evals]] (as agentic validation), [[agent-saas]] (as the productization of agents), and the [[react-loop]] (as the mechanism).
For hcho it reframes "learn Claude Code deeply" from a productivity tip into a hireable core competency, and its "agentic validations" pillar is his validation background restated in the newest vocabulary.

The insider source strengthens that reframe in a specific way.
Its central rule is that the verification signal decides the orchestration mechanism, which makes the "agentic validations" pillar upstream of the others rather than a downstream quality step: what you can measure determines what you can automate, so the eval skill gates the agentic-engineering skill.

As dedicated Claude Code / agent sources are ingested, this concept may graduate into its own area hub.
It is now the leading candidate, with four more agent-workflow sources queued in `raw/` as of 2026-07-28; the plan is to graduate it once that batch is ingested rather than reshaping the hub after each one.
