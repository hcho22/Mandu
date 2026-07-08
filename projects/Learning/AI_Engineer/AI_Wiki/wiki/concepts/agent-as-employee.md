---
type: concept
tags: [agents, agent-ops, agent-safety, permissions]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Agent as Employee

The principle from [[one-person-company-with-agents]] of treating an agent like a real (scoped) hire: give it its own identity and real permissions rather than running everything as you.

## Key points

- **Own identity:** its own email on your domain, its own GitHub account.
- **Scoped permissions:** read access where an EA would have it (email, calendar); write "as itself" (books meetings from the agent, adds you as attendee), never impersonating you.
- **Be overly specific and pedantic** in its instructions - spell out things you would never tell a human ("always check if you've emailed this person") - once, and then never again.
- The agent follows instructions literally, so audit the markdown: a stray "CC my other account" line caused a confusing bug.

## Synthesis

This is the identity-and-permissions face of [[capabilities-not-instructions]]: scoping what the agent *is* and can touch, not just what you tell it.
Giving the agent its own identity also makes its actions auditable (its email, its PRs), which pairs with [[red-team-your-agent]] and the wiki's broader "make safety physical" stance.
For hcho this is concrete agent-ops design worth demonstrating in a portfolio piece.
The same employee model reappears in the [[agentic-web]] as an infrastructure spec ([[agent-building-blocks]]): identity -> tools -> wallet, with the spending limit raised as trust is earned ([[phased-autonomy]]) - so "agent as employee" is both an ops discipline and the design pattern for agent-facing products.
