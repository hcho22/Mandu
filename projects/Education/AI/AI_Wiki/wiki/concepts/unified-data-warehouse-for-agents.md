---
type: concept
tags: [agent-operations, data, infrastructure, analytics, marketing]
status: developing
source-count: 2
last-updated: 2026-08-21
---

# The Unified Data Warehouse for Agents

**A single location that unifies all your data sources so the agent has context across *all* channels simultaneously - not one data source in isolation.**

From [[building-marketing-agents]], where it is requirement #1 of a real [[marketing-agent]] and the piece Cody says most people skip.

## The stack

| Layer | Tool |
|---|---|
| Pipeline | **Airbyte** - open-source, self-hostable, pre-built connectors |
| Warehouse | **ClickHouse** - open-source, self-hostable |
| Hosting | Heroku, Railway, or any cloud provider |

**Sources unified for a Facebook ads use case:** Facebook Ads, Google Analytics, PostHog, CRM (e.g. HubSpot), and **Stripe - so ad spend can be traced all the way through to actual revenue.**

That last one is the point of the exercise. Without it the agent optimizes clicks; with it, it can optimize revenue.

## The sleeper benefit: conversational analytics

With the warehouse connected to a coding agent, you can ask business questions in plain language:

> "We're having trouble hitting payroll this month, what's going wrong?"
> → "Your accounts receivable are off."

The agent queries live data across every source rather than answering from one dashboard.

## The spreadsheet version, and where it stops (2026-08-21)

[[one-person-marketing-team]] builds the smallest possible instance of this, and it is instructive precisely because it is inadequate.

After four generation runs, an 8-minute prompt produced an Excel **creative tracker** with tabs for a generation log (ID, date, type, campaign, channel, primary angle, deliverables, tool and model, credits, dollar cost, status), the creative assets and their copy, a **copy bank**, a cost summary, and an **angle performance** tab.

Two things worth taking from it.

**A spreadsheet is a legitimate starting point.**
Airbyte and ClickHouse are the right answer at real spend and enormously premature before it.
One file that records what was made, why, at what cost, and under which angle is a real analytics substrate, and it costs eight minutes.
The unglamorous precondition is that every run reported its own cost ([[make-the-agent-report-its-cost]]) - without that, the log cannot be reconstructed afterwards at any price.

**The angle performance tab was empty, and stayed empty.**
That single detail is this page's original thesis restated as a demonstration.
The tracker records everything the *generation side* knows and nothing the *market* knows, because no ad was ever served and nothing was connected to a performance source.
It is a production log, not a decision substrate.
An agent reading it can tell you what you made and what it cost; it cannot tell you what to make next, which is the entire point of the warehouse.

**The generalization:** the hard and valuable half of a data layer is never the storage, it is the connection to outcomes you do not control.
Cost data is free because you generate it.
Revenue data is expensive because someone else does.

## Synthesis

The reframe is that **the data layer, not the model, is what makes an agent an agent.**
Two systems can run the same model on the same schedule and only one of them can make a real decision, because only one can see the whole funnel.

This is the operations-side restatement of [[context-is-king]] - the model is the engine, your context is the fuel - with a concrete answer to *where the fuel is stored* for a business rather than for an individual.
[[ai-operating-system]] and [[four-cs-framework]] describe assembling personal context; this is the same architecture at company scale, where the context is transactional data rather than notes.

It also quietly resolves why so many "AI agents" underperform.
[[agents-as-cron-plus-markdown]] is sufficient when the agent's decision is local to one task.
It is insufficient the moment the decision requires comparing across channels, which is most interesting business decisions, and the missing ingredient is plumbing rather than intelligence.

The conversational-analytics payoff is the part with the widest applicability and the lowest current uptake.
For hcho at present scale it is over-engineering - there is no revenue to unify - but the pattern is worth holding for the moment Rep Today has App Store, RevenueCat, and analytics data that would otherwise live in three dashboards nobody correlates.
See also [[agent-observability]] and [[production-watchdog]], which solve an adjacent problem (what happened) with much less infrastructure.
