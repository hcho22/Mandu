---
type: concept
tags: [system-design, architecture, decision-making]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Engineering Trade-Offs

From [[building-robust-apps-with-ai]]: the foundational principle of [[system-design]] is that engineering is all about trade-offs.
No system, stack, tool, or infra provider is perfect ("nothing is perfect except Jesus," per Ross); every choice carries downsides, so you design by consciously choosing which downsides you accept.

## The four axes

- **Scalability** - can it absorb growing traffic/data by adding resources (a dashboard change vs true autoscaling)?
- **Reliability** - what is the chance of going down; is the provider outage-prone?
- **Performance** - does the tool/architecture keep the app fast?
- **Cost** - can you afford it, now and at scale?

## Key points

- You cannot maximize all four; picking a stack is picking a trade-off profile.
- Cost is often the trade-off to defer deliberately (Ross prioritized "never breaks, always fast" and left cost optimization "for later").
- On solid, "tried and true" infra, scaling to 1,000 users is mostly upgrading plans - the app fails from bad code, not the platform.

## Synthesis

This is the lens the whole [[system-design]] area is read through, and it is a validation mindset in disguise: naming the axes and their failure conditions is exactly the risk-weighting a QA/validation engineer does.
It reframes tool choice away from "what's best" (a non-developer's question) toward "what fails, when, and can I live with it" - hcho's native register.
Pairs with [[cost-of-being-wrong]] (the cost axis is really the cost of each failure mode) and [[dont-let-ai-be-your-architect]] (trade-off calls are human-owned judgment, not something to delegate).
