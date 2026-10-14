---
type: concept
tags: [marketing, customer-research, evidence, positioning, agents]
status: seed
source-count: 1
last-updated: 2026-10-14
---

# Customer Truth File

One regularly updated file that shows what the market is telling the company and what changed, with every claim tied to a quote, a link, or a count.
From [[projects/Education/Marketing/wiki/sources/becoming-a-marketing-engineer|Becoming a Marketing Engineer]], where the output of the customer truth system is a markdown file called "what the market is telling us," and its goal is to make the business "harder to lie to."

## How it works

- **Inputs:** sales calls, support tickets, churn notes, payment movement, CRM notes, and social data, especially for consumer products.
- **Cadence:** every morning or every week, depending on how much signal there is.
- **Job:** show what changed, such as buyers using a new phrase or trial users getting stuck before inviting a teammate.
- **Evidence:** ask the agent for quote snippets, ticket links, and event counts, and reject vague summaries.

| Bad | Good (the source's HVAC example) |
|---|---|
| "Customers want better collaboration." | "Five sales calls this week mentioned emergency dispatch, but the calls that actually converted all talked about missed follow-up quotes after the tech left." |

The minimal first job in the source asks for the same thing: "tell me what's changed, show me the receipts, suggest one marketing test that could create pipeline this week."

## Synthesis

The file applies an evidence rule the wikis already hold elsewhere.
It is [[approved-language-repurposing]]'s refusal to invent claims, applied to market research, and the same move as AI_Wiki's [[projects/Education/AI/AI_Wiki/wiki/concepts/proof-in-the-pr|Proof in the PR]]: a claim arrives with the record that supports it, so the reader audits instead of trusts.
Its "what changed" framing makes it a change log of market language rather than a static persona, which is what lets it drive weekly decisions.

Mandu's caution: receipts make a claim checkable, not representative.
The source's good example compares calls that mentioned one pain with calls that converted, but small weekly counts can flip by chance; a count needs its denominator and enough cases before it moves positioning ([[projects/Education/AI/AI_Wiki/wiki/concepts/leading-metric-over-vanity-metric|Leading metric over vanity metric]]).
For hcho this is research run like a test log: observation, source, count, and the question of whether the sample can carry the conclusion.

## Source

- [[projects/Education/Marketing/wiki/sources/becoming-a-marketing-engineer|Becoming a Marketing Engineer]] - the "what the market is telling us" file, its inputs, and the receipts rule.
