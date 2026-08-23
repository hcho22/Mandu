---
type: source
title: "Building Marketing Agents That Actually Get You Customers"
source-type: podcast
author: "Cody Schneider (companiesgraph.com), interviewed by Greg"
url: "local"
date-ingested: 2026-08-01
date-created: unknown
tags: [agent-operations, marketing, ads, data-warehouse, agents, growth, entropy, distribution]
concepts: [marketing-agent, unified-data-warehouse-for-agents, creative-entropy, test-breadth-over-conviction, creative-is-the-targeting, manager-of-agents, business-loops, agents-as-cron-plus-markdown]
---

# Building Marketing Agents That Actually Get You Customers

A podcast interview with **Cody Schneider** on what a real "marketing agent" is, as opposed to a linear Zapier-style automation, and how to build one end to end.

This is the wiki's first source on **agents pointed at distribution rather than at code**, and it is the deepest technical account of a non-engineering agent so far.
It matters here for two reasons beyond marketing.
First, its **entropy problem** - an agent left alone stagnates and needs external DNA injected - is a general agent-operations finding that no other source in the wiki has named.
Second, its **unified data warehouse** requirement is the concrete answer to why most "agents" are really just automations.

Cody opens by saying he's frustrated by how loosely "marketing agent" is used, and he explicitly does **not** want a fully autonomous agent that thinks entirely on its own.
He wants something that executes a defined process, looks at the resulting data, and improves from that feedback.

## Key claims

### What makes it an agent, not an automation

**Cody's definition requires three things:**

1. **Data clarity** - unified visibility across the entire pipeline, not siloed data.
2. **Autonomous decision-making** - the agent acts on some cadence with a "thinking loop," not a one-off script.
3. **Infrastructure** - a data pipeline, a data warehouse, and cloud hosting for the agent itself.

- Under the hood, **"an agent is just code"** - a decision tree fed a live data stream, with an LLM-driven decision loop optimizing toward a defined outcome, most commonly more revenue.
- Worked example: an agent that fully runs a Facebook ads account - researching pain points and outcomes of the target customer, generating on-brand static and AI-avatar UGC video creative, publishing it, turning off underperformers, promoting winners, and feeding results back into a loop that generates more content like the top performers.

### The data pipeline and warehouse

- **Airbyte** (open-source, self-hostable) pipes data from multiple sources into a warehouse; **ClickHouse** (open-source, self-hostable) is the warehouse.
- **What a data warehouse means here:** a single location that unifies all your data sources so the agent has context across *all* channels simultaneously, not one data source in isolation.
- Sources unified for a Facebook ads use case: Facebook Ads, Google Analytics, PostHog, CRM (e.g. HubSpot), and **Stripe - to trace ad spend all the way through to actual revenue**.
- **The sleeper benefit is conversational analytics.**
With the unified warehouse connected to your coding agent, you can ask business questions like "we're having trouble hitting payroll this month, what's going wrong?" and get an answer sourced from live data ("your accounts receivable are off").
- On hosting: he's dismissive of running these setups locally on repurposed hardware; cloud hosting (Heroku, Railway, any provider) is simpler and more scalable.

### The build, step by step

**Research pain points.**
**Perplexity** used to scrape Reddit for pain points and desired outcomes, because Reddit captures real people complaining in their own words.
Rank them by **most referenced** to identify the top 3, then use those to seed ad creative concepts.
His own caution: Reddit is increasingly "eroded" by people manipulating threads so LLMs will rank and cite them - part of what he calls "the dead internet."
He admits, "I am the problem."

**Generate creative.**
**Kie AI** as a multi-model aggregator for bulk static generation, **Google Nano Banana** for static ads seeded with a competitor example, **HeyGen** for AI-avatar UGC video, and **Seedance** as an emerging video tool whose current limitation is clip length, requiring frame-stitching.
**Define explicit brand style guides** (fonts, colors, brand specifics) and **run outputs through a vision model that checks generated creative against those guides**, verifying text readability and on-brand fonts before anything goes live.

**Publish.**
The **Facebook Marketing API** for publishing, pausing, and promoting.
On the common claim that "my ads account got banned because I used an agent": **the agent isn't the cause.**
Accounts get banned for ToS violations, typically spamming the API by trying to pull hundreds of millions of rows.
**Use the API primarily for write actions**, not bulk data pulls.

**The learning loop.**
His actual client cadence: **2 new ad sets per day, 5 ads per ad set**, auto-uploaded based on prior research and warehouse data.
Each batch runs a **2-3 day window** to gather signal.
Worst performers are automatically turned off; winners move into a **"winners pool"** where they compete against each other for budget.
A vision model - or increasingly a structured database of the JSON prompts and scripts used to generate each ad - analyzes what's actually working so future generation improves.

### Solving for entropy

- **The problem: an agent left alone tends to "get stuck thinking in the same way."**
Creative ideation stagnates over time.
- **Two solutions:** pull ads from competitors' public **Facebook Ads Library** to inject "new DNA" into the creative system, and pull insights from **niche YouTube channels and podcast transcripts** to seed new ad angles.
He also mentions a TikTok/Reels trend-scraping API for surfacing the most viral posts in a category.
- **He stresses this problem is rarely discussed publicly.**
Most people describe these systems as "set it up once and it's just good," which he directly disputes.

### Creative is the targeting now

- **Andromeda** is Meta's newer ad-serving algorithm.
Rather than relying on interest-based targeting, it reads the ad creative itself (image, video, on-screen text, script) *and* the landing page content, then uses that combined understanding to decide who sees which ad.
- **Interest-based targeting is largely obsolete post-Andromeda.**
Instead, the creative itself must speak directly to the pain point or outcome of the target customer, paired with a landing page that clearly explains the product; the algorithm does the audience-matching.
- "Facebook has turned into the best B2B ads channel that exists right now" - because sufficiently niche creative can find the small pool of people (he gives an example of maybe ~10 people in the US) who have that exact problem.
- **Set up conversion events for both signup and payment** deeper in the funnel so the algorithm optimizes toward real revenue, not just clicks.

### Test breadth, not conviction

- **The common founder mistake:** run a handful of ads, see no results, give up - without realizing the same core ad often needs **10-20 variations in positioning** before finding what resonates.
He's regularly surprised by which angle wins.
- "We're not Don Draper" - he rejects imposing a predetermined message on the market.
Test broadly (he references testing "a thousand different ad creatives") and let market response, visible within about **48 hours**, reveal what's resonating.
- Both speakers push back on founders who only want organic/word-of-mouth growth, calling it a "rookie way to look at the market."
Paid ads are the only system where "I put a dollar in and $5 can potentially come out the other side," and you can keep feeding that multiplier at scale.
- **Marketing should be treated as continuous, not campaign-based**, because feedback loops are now much faster; businesses need constant observability into shifting trends rather than a start-and-stop campaign mentality.
- Historically this level of testing required an agency at tens of thousands per month; his position is founders can now build the system themselves, with fine-tuning still required.

### The agent jockey

- Cody frequently talks with marketers asking "is my job secure?"
His answer depends on whether they can adapt, and he describes the emerging role as an **"agent jockey"**: someone who takes their existing domain knowledge and encodes it into agent-driven systems rather than executing tasks manually.
- **You don't need to be deeply technical.**
A semi-technical person with a coding agent can feed it a transcript like this one and be walked through building the actual system described.

### Other agent concepts named

Google Ads agents, influencer outreach agents (research, cold email, negotiate pricing, hand-raise promising responses to a human), cold email agents, TikTok "reel farms," SEO agents, AI search/citation agents, social media management agents, and podcast-to-newsletter agents.

## Connections

- [[marketing-agent]] - the three-requirement definition that separates an agent from an automation.
- [[unified-data-warehouse-for-agents]] - the infrastructure precondition; also the source of conversational analytics.
- [[creative-entropy]] - **the source's most generalizable finding**: agents converge and stagnate, and need external DNA injected on purpose.
- [[test-breadth-over-conviction]] - 10-20 positioning variants; let response reveal the message.
- [[creative-is-the-targeting]] - Andromeda reads the creative and the landing page; the ad *is* the audience selection.
- [[manager-of-agents]] - the "agent jockey" framing is the same role reframe [[running-teams-of-ai-agents]] states for engineering, restated for marketing.
- [[business-loops]] - this is the ads loop of [[loops-to-run-your-business]] built out in full, with the data layer that source leaves implicit.
- [[agents-as-cron-plus-markdown]] - a cadence-driven agent, but this source argues cron plus markdown is not sufficient without the warehouse.
- [[agent-saas-sells-work]] - selling the ad-agency job rather than an ad tool.
- [[llm-as-judge]] - the vision model checking creative against a brand style guide is a judge with a rubric, applied to images.
- [[agent-operations]] - the area this source populates.
- [[agent-observability]] - "constant observability into shifting trends" as a business-side restatement.

## Source

- **Author:** Cody Schneider (companiesgraph.com), interviewed by a host addressed as "Greg"
- **Title:** Building Marketing Agents That Actually Get You Customers
- **Format:** Podcast interview, ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/marketing-agents-summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-01

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix.
Tool names flagged as uncertain there: **Kie AI** (moderate confidence, captioned "Kai AI") and the TikTok/Reels trend-scraping API rendered as "Viral Loop" (low confidence; possibly "Viralo" - the exact product name is unconfirmed and it is referred to descriptively above rather than by name).
The Seedance clip-length limit is explicitly unconfirmed in the source ("don't quote me").

The **43% of the internet runs WordPress** figure is Cody's live-checked correction of his own earlier "50%+" claim and is reported, not independently verified.
Roughly a third of the raw source is a startup pitch for an AI-first WordPress plugin bundle, used as the worked example throughout.
That business idea is **not** filed as wiki knowledge - it is a specific opportunity pitch, not durable AI-engineering understanding - but it is preserved in the raw file if hcho wants it.
