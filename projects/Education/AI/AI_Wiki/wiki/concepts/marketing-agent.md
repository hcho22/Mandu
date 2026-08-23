---
type: concept
tags: [agent-operations, marketing, agents, definition, data]
status: developing
source-count: 2
last-updated: 2026-08-21
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

## The definition tested against a second source (2026-08-21)

[[one-person-marketing-team]] calls its system a "marketing team."
Run against the three requirements above, it satisfies **none** of them:

| Requirement | Present in that source |
|---|---|
| Data clarity (unified cross-channel data) | No. One Excel file with an empty performance tab |
| Autonomous decision-making on a cadence | No. Every generation is human-triggered in a chat |
| Infrastructure (pipeline, warehouse, hosting) | No |

That is a useful result rather than a criticism, because it shows the definition **discriminates**.
A definition that admitted a chat-driven creative studio would not be worth having.

What that source actually built is a **context-rich creative studio**: a production tool with a human in the loop on every request, whose differentiator is the [[own-the-context-layer|context layer]] of business facts, skills, and brand rules sitting in front of a commodity generation tool.
It is genuinely good at the thing Cody's system barely addresses - staying on-brand and on-message - and completely absent the loop.

**The two sources are opposite halves of the same system.**
Cody has the data layer and the cadence, with the context layer left implicit.
Nate has the context layer, with no loop and no data.
Neither is complete, and the union - branded generation driven by a context layer, published on a cadence, judged against unified revenue data - is a system no source in this wiki has documented.
That gap is the most concrete build target the distribution material has produced.

The practical ordering hint, since the two halves cost very differently: **the context layer is the cheap half and the data layer is the expensive half.**
A weekend of context files and brand rules buys most of the output quality; Airbyte and ClickHouse buy the decision-making, and only matter once there is real spend to decide about.

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
