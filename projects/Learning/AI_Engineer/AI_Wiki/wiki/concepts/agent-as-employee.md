---
type: concept
tags: [agents, agent-ops, agent-safety, permissions]
status: developing
source-count: 3
last-updated: 2026-07-28
---

# Agent as Employee

The principle from [[one-person-company-with-agents]] of treating an agent like a real (scoped) hire: give it its own identity and real permissions rather than running everything as you.

## Key points

- **Own identity:** its own email on your domain, its own GitHub account.
- **Scoped permissions:** read access where an EA would have it (email, calendar); write "as itself" (books meetings from the agent, adds you as attendee), never impersonating you.
- **Be overly specific and pedantic** in its instructions - spell out things you would never tell a human ("always check if you've emailed this person") - once, and then never again.
- The agent follows instructions literally, so audit the markdown: a stray "CC my other account" line caused a confusing bug.

## A caution on the metaphor ([[designing-loops-and-workflows]], 2026-07-28)

[[tharic]], from Anthropic's [[claude-code]] team, is deliberately guarded about the coworker framing:

> "I think these metaphors can sometimes be helpful but also limiting... it is kind of helpful to think of an agent that has persistence and memory, but I think they're also different from co-workers in some ways."

He adds that Claude's memory is "better and worse sometimes... it's spiky," which is the concrete way the analogy breaks.
A human colleague's recall degrades predictably, so you can model what they will and will not remember; an agent's does not, so the employee metaphor quietly imports an intuition about reliability that does not hold.

Where the metaphor still earns its keep is the part this page was built on: identity, scoped permissions, and auditability are real design decisions, and "what would I give a new hire" is a good prompt for making them.
Where it misleads is capability and continuity, where you should reason from the actual system (context windows, per-channel memory, [[context-rot]]) rather than from the analogy.
Notably, the source's own agent-ops practice is consistent with this: every agent and channel in Claude-in-Slack carries its own memory, which is an architectural fact, not a personality.

## Synthesis

This is the identity-and-permissions face of [[capabilities-not-instructions]]: scoping what the agent *is* and can touch, not just what you tell it.
Giving the agent its own identity also makes its actions auditable (its email, its PRs), which pairs with [[red-team-your-agent]] and the wiki's broader "make safety physical" stance.
For hcho this is concrete agent-ops design worth demonstrating in a portfolio piece.
The same employee model reappears in the [[agentic-web]] as an infrastructure spec ([[agent-building-blocks]]): identity -> tools -> wallet, with the spending limit raised as trust is earned ([[phased-autonomy]]) - so "agent as employee" is both an ops discipline and the design pattern for agent-facing products.
