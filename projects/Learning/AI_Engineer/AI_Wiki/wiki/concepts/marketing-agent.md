---
type: concept
tags: [agent-operations, marketing, agents, definition, data]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# Marketing Agent

Cody Schneider's definition in [[building-marketing-agents]], offered against what he says is loose usage - many people "talk a huge game" but the reality doesn't match the term when you dig in.

**A marketing agent has to satisfy three things:**

1. **Data clarity** - unified visibility across the entire pipeline, not siloed data.
2. **Autonomous decision-making** - the agent acts on some cadence with a "thinking loop," not a one-off script.
3. **Infrastructure** - a data pipeline, a data warehouse, and cloud hosting for the agent itself.

**Under the hood, "an agent is just code"** - a decision tree fed a live data stream, with an LLM-driven decision loop optimizing toward a defined outcome, most commonly more revenue.

## What it is not

He explicitly does **not** want a fully autonomous agent that thinks entirely on its own.
He wants something that **executes a defined process, looks at the resulting data, and improves based on that feedback** - a narrower, more controllable definition than the "totally autonomous agent running your whole marketing stack" hype.

## The worked instance

An agent that fully runs a Facebook ads account: research the target customer's pain points and desired outcomes, generate on-brand static and AI-avatar video creative, publish it, turn off underperformers, promote winners, and feed results back into a loop that generates more content like the top performers.

Its actual cadence with a client: **2 new ad sets per day, 5 ads per ad set**, each batch running a **2-3 day window** to gather signal, worst performers auto-killed, winners moved into a **"winners pool"** to compete for budget.

## Synthesis

The useful contribution is requirement #1, because it is the one that actually separates an agent from a Zapier chain and it is the one everyone omits.
An LLM on a schedule is a script.
An LLM on a schedule **with unified cross-channel data** can make a decision no single-source automation can make - which is why [[unified-data-warehouse-for-agents]] is the load-bearing piece rather than the model choice.

Note how closely this definition tracks [[seven-part-agent-spec]] from [[agents-are-the-new-saas]] (trigger, context, tools, allowed, approval, escalation, success) and [[minimal-useful-agent]]'s draft-to-act ladder.
Both sources independently reject full autonomy in favor of a defined process with a feedback loop, which is the same posture as [[start-as-a-workflow]].
Three unrelated sources landing on "begin predictable, earn autonomy" is about as close to consensus as this wiki has.

The tension worth noting is with [[agents-as-cron-plus-markdown]], which holds that an agent is a deterministic cron plus a good skill file.
This source would say that is necessary and not sufficient - without the warehouse, the cron has nothing to reason over.
Both are describing real working systems, and the difference is probably whether the agent's decision needs **cross-channel** context or just task context.
