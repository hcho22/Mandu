---
type: concept
tags: [sub-agents, multi-agent, delegation, agent-teams, coordination]
date: 2026-07-03
source-count: 5
status: seeded
---

# Sub-Agents and Multi-Agent

Delegating work to other agents from within a task: sub-agents that run in isolation and return only a conclusion, and multi-agent setups where several agents coordinate or debate - distinct from running independent sessions in parallel.

## From the sources

[[building-products-with-coding-agents]] gives the primary reason to delegate:

- The main reason to use a sub-agent is to keep the main session's context window from blowing up: carve heavy, exploratory investigation out to a sub-agent that returns only its conclusion; also good for many isolated tasks ("spin up 10 sub-agents").
- Today's models rarely self-delegate (a built-in "explore" agent is the exception), so you must prompt for sub-agents explicitly.

[[every-claude-feature-ranked]] draws the sharp contrast:

- Sub-agents work in parallel and only report back to the main session that invoked them; agent teams are groups of agents that talk to each other and debate through rounds via personas (e.g., a beginner and a CEO) until they agree. Agents are defined as markdown files in .claude/agents declaring their tools and embedded skills - token-intensive but useful for genuinely different perspectives.

[[claude-managed-agents]] shows multi-agent as a managed capability:

- Agent events include multi-agent coordination when Claude spawns other agents; in the live run Claude spawned four sub-agents, each with its own context window, coordinating and passing updates, each visible as a line in the console with drill-down.

[[inside-conductor-agent-orchestration]] raises the open design questions:

- Should you be able to talk to sub-agents directly? Should there be multiplayer chats where several people work with the AIs on the same thing?

[[working-with-fable-5-in-claude-code]] shows the archetypes becoming emergent:

- A capable-enough model now *invents* the sub-agent archetypes a task needs (reviewer, adversarial reviewer, exploratory), so hand-defining a fixed roster is no longer worth it - decomposition itself is delegated.
- Both patterns appear in one run: sub-agents that report up (Codex-backed review/implementation/computer-use helpers) and a debate-style panel (16 PR investigators, each verdict stress-tested by a Fable+Opus judge pair) - the panel is the multi-agent "diversity" pattern applied to raise confidence in a decision.

## Synthesis

Two different patterns hide under "more than one agent," and the sources are careful to separate them. **Sub-agents are a context tool**: their defining property is that they run in isolation and return only a conclusion, so the value is keeping exploratory or bulky work out of the caller's window - which makes this concept a direct instrument of [[context-engineering]]. Because models rarely spawn sub-agents on their own, using them is a deliberate prompt, not an emergent behavior. **Agent teams / multi-agent are a diversity tool**: several agents with distinct personas debate or divide a problem so you get genuinely different perspectives or coordinated specialization (CMA's four coordinating agents, the panel/debate boards), at a real token cost. The clean rule from [[every-claude-feature-ranked]] is directional: sub-agents *report up* to a single caller, agent teams *talk across* to each other. Distinguish this from [[parallel-agent-orchestration]], which runs whole independent tasks as separate sessions/worktrees rather than delegating subtasks within one. The Agentic RAG flagship uses the sub-agent pattern in production: [[agentic-tools-and-subagents]] delegates document-level work to isolated agents that return conclusions, which is the same context-isolation motive described here - a concrete bridge between the video diet and a shipped system.
