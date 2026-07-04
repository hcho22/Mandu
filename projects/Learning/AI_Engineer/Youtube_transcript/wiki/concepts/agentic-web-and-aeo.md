---
type: concept
tags: [agentic-web, agent-as-customer, aeo, mcp, machine-to-machine]
date: 2026-07-03
source-count: 1
status: seeded
---

# Agentic Web and AEO

The shift from an internet whose customers are humans to one whose customers are AI agents - the machine-to-machine economy - and the product and discovery changes it forces, including the move from SEO to AEO (optimizing for which agents cite, trust, and recommend you).

## From the sources

[[startups-for-agents-agentic-web]] is the anchor source:

- The end users of the internet are shifting from humans to agents; the forecast is billions of agent "customers" with millions of wallets over 10 years, with almost every SaaS category rebuilt agent-native.
- The human customer wants persuasion; the agent customer wants structured capability, permission, and trust. The agent buying journey has six stages: finding, evaluating, trust, transacting, using tools, and recommending (including agents recommending tools to other agents).
- Agents need six building blocks - identity, tools, inbox, memory, wallet, receipts - with trust granted incrementally like a new hire.
- An agent-readable homepage exposes structured docs, schemas, policies, examples, and endpoints - in practice MCP tools, SDKs, OAuth, checkout, a sandbox, receipts, and dedicated entry points like /agents. If an agent cannot understand you or safely act, you are invisible to it.
- What changes for startups: SEO -> AEO, forms -> tool calls, support docs -> executable support, landing pages -> capability manifests, sales calls -> agent procurement, analytics -> agent analytics. The idea generator: "what is the agent version of this tool?"

## Synthesis

Where [[agents-as-labor]] is about *selling* agents, this concept is the mirror image: agents as the *buyers*, and the infrastructure a product needs to be usable by them. The load-bearing distinction is that a human customer is won by persuasion (brand, copy, social proof) while an agent customer is won by structured capability, permission, and trust - so a marketing page becomes a capability manifest and a form becomes a tool call. Concretely, "agent-readable" resolves to primitives this wiki already tracks: exposing MCP tools and SDKs is the same tool surface described in [[production-agent-infrastructure]], and the trust building blocks (identity, permissioned tools, wallet with spend caps, receipts/audit trail) are [[agent-permissions-and-safety]] and [[agent-memory]] viewed from the product side. AEO is the discovery consequence - if agents decide what to cite and recommend, you optimize for agent selection rather than human search - and the honest open question the source keeps returning to is agent analytics: what does conversion-rate optimization look like when your visitors are agents? This is a single-source, forward-looking page; it is included because it reframes every other concept from the supply side (how you *build* agents) to the demand side (how you *serve* them), and it is where future talks on MCP, agent commerce, and AEO will accrue.
