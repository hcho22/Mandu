---
type: concept
tags: [agentic-web, agents, infrastructure, identity, wallet]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Agent Building Blocks (the six an agent needs)

From [[startups-for-agents]]: the six things any agent operating in the world needs, each a piece of missing infrastructure and thus a startup opening.

## The six

- **Identity** - who is this agent acting for?
- **Tools** - what actions can it safely invoke?
- **Inbox** - where do OTPs, docs, and threads land, and where can it reply? (e.g. AgentMail)
- **Memory** - what does it know about my preferences and rules?
- **Wallet** - what can it spend, and who approves it? (e.g. the Stripe agent wallet: spend caps, approval rules, audit trail)
- **Receipts** - what did it see, decide, change, and buy?

## The employee mental model

Trust is granted the way it is to a new hire: start with identity, add tools, then hand over a wallet and raise the spending limit as trust grows.
This is [[agent-as-employee]] and [[phased-autonomy]] restated as an infrastructure checklist.

## Synthesis

These six are the concrete substrate of the [[agentic-web]]: identity, wallet, and receipts are the trust-and-accountability layer, and they map directly onto the safety spine that runs through the wiki - [[capabilities-not-instructions]] (scoped tools), [[credential-vaults]] (wallet/secret hygiene), and [[red-team-your-agent]] (can identity or permissions be abused?).
For hcho, "receipts" (what did the agent see, decide, and buy) is essentially an audit/observability trail - [[agent-observability]] pointed at accountability rather than debugging, and squarely his kind of problem.
