---
type: concept
tags: [agents, agent-design, scoping]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Minimal Useful Agent (MUA)

The principle from [[agents-are-the-new-saas]] that you should build the smallest agent that does real work, not a fully autonomous "employee."
Chasing the autonomous employee produces viral demos that do not hold up and become weak businesses.

## The four first versions (a ladder)

1. **Draft-and-approve** - reads context, drafts the reply/quote/summary; a human approves. Best when there is risk, creativity, or an approval process.
2. **Triage** - classifies inbound work and routes it.
3. **Coordinator** - moves between systems and people: checks availability, sends reminders, chases missing info.
4. **Bounded-action** - does a specific thing under clear rules (book an appointment, refund under $50).

The ladder is **draft to triage to coordinate to act** - autonomy increases as trust is earned.

## Ship one workflow and one promise

Day-one scope is a single workflow with a single promise ("we answer missed calls for roofers and book qualified jobs"). First-time agent buyers do not want everything at once.

## Synthesis

The MUA is the scoping discipline that makes agent products actually ship and actually work.
It is tightly paired with [[start-as-a-workflow]]: begin at the low, predictable end of the ladder and climb only when value and reliability justify it. The [[product-wrapper]] is what lets a customer trust each rung.
