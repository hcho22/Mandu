---
type: source
title: "Using Loops to Run Your Business"
source-type: video
author: "Unnamed host with guest 'Ellie' (builder of Inbox Zero and draftfantasy.com)"
url: "local"
date-ingested: 2026-08-01
date-created: unknown
tags: [loops, agent-operations, seo, ads, product-feedback, cost, lean-startup, claude-code]
concepts: [business-loops, minimal-viable-loop, loop-cost-discipline, leading-metric-over-vanity-metric, verification-signal-picks-the-mechanism, agents-as-cron-plus-markdown, eval-driven-development]
---

# Using Loops to Run Your Business

A YouTube tutorial in interview format arguing that "loop engineering" went viral for *building products* but that the more valuable use is *running a whole business*.

This is the wiki's first source to take the loop primitive outside the codebase.
Where [[designing-loops-and-workflows]] described `/loop` and `/goal` as software-development mechanisms, this source points the same build-measure-learn cycle at SEO rankings, ad ROAS, and product KPIs, over horizons of **weeks to years** rather than a half-hour run.

The lineage is stated explicitly: **Lean Startup** (Eric Ries) and before it **Toyota / lean manufacturing**.
Both speakers agree the surrounding hype and terminology are overblown even though the underlying idea is genuinely useful.

## Key claims

### What a loop is, and the non-negotiable parts

- Any process running on a schedule is already a form of loop.
"Loop engineering" is just getting an **agent** to run that same build/measure/learn cycle for you.
- The agent version mirrors Lean Startup: **build** (tell the AI to go do the thing), **verify** (an objective check - tests pass, a browser agent clicks through, an eval scores high enough, or a separate checker agent confirms), **learn** (feed the result back and iterate).
- In [[claude-code]], `/goal` runs this pattern: a checker agent verifies whether the goal is met and, if not, tells the main builder agent to keep looping.
- **A loop needs two things or it runs forever:** a defined **stop condition** and an **objective metric** fed back into the system.
Without a clear metric there is nothing to converge on.
- Example stop conditions: "the feature works in the browser" (`/goal make signup work`), or an **eval threshold** - for the guest's product **Inbox Zero**, evals test how well a model categorizes emails, targeting **≥ 90%**; at 88% the agent adjusts the prompt or swaps the model and retries until it clears.
- **The verify step does not have to be product or engineering related.**
Any objective metric can close the loop - Google ranking, ad ROAS, retention.
Pick the number first, then build the loop around it.
- The long-horizon framing is deliberate: these loops may run **once every few weeks for months or years**, not continuously for half an hour.

### The SEO loop (the anchor example)

- SEO is the anchor because the metric is unambiguous and "black or white": you moved up, moved down, or stayed the same.
- Concrete numbers: **Inbox Zero ranks #1** for "inbox zero"; for the higher-value term "AI email assistant" it ranked around **position 30**, and the loop's job is to push it onto page one.
Inbox Zero's domain rating is ~**63-64**, which matters, since a brand-new site with a very low domain rating may behave differently.
- **Live demo on draftfantasy.com** (a business the guest started ~12 years ago): **10 million impressions** over three months; for the term "380", ~**120,000 clicks**, ~**1 million impressions**, average position ~**4.4**.
The claim is that pushing that term from ~4 to 2-3 could turn 120K clicks into perhaps half a million.
Two days before recording he pointed Claude Code at the same SEO loop for Draft Fantasy "because why not"; it runs in the background, remembers what it did, and keeps improving.
- **The single easiest win, loops or not: connect your AI to your real tools and real data.**
That alone lets it make far smarter decisions than working blind.
- **Quick SEO wins to grab first**, independent of any loop: run a site audit, improve **meta tags**, add **JSON-LD** structured data, add a missing **sitemap**, and check for **keyword/link cannibalization** (two of your own pages splitting link power for the same term).
- Tools: **Google Search Console** (has an API - queries, impressions, clicks, average position, and which pages outrank you) and **DataForSEO** (comparable to Ahrefs and SEMrush).
- **The loop structure:** make improvements, check the objective metric, record what was tried in a **memory file**, then weeks or months later review whether the experiment moved the term up or down and iterate.
This is exactly what an SEO agency does for you.
- **SEO takes months, not days.** Results compound and can suddenly "bear fruit" around month four.
- **Remember and revert:** have the agent keep a markdown file logging every change so the next run can check its own past experiments.
Because each change is just an experiment, if a change drops you from position 20 to 30 you simply undo it.
- Everything done for Google SEO also benefits **LEO / GEO** (ranking inside LLMs and generative search).

### Setting one up

- The "lazy" recipe: screenshot your Google Search Console chart, paste it into Claude Code or Codex, say you want to create an SEO loop, give it access to Search Console / DataForSEO, and tell it it is judged on Google ranking.
- A ready-made reference prompt exists at **atomieve.dev** - essentially an `instructions.md` for the job ("you are the SEO improver; you're judged on these three metrics").
One instruction shown: *when applying changes, select the subset of this week's recommendations that map cleanly to files in the blog repo.*
- **The one extra step that makes it a true loop is scheduling:** Claude "routines", Cursor "automation", or Codex "automations".
- **Stay in the loop:** have the agent ping you on Slack when each run finishes so you can approve or reject its changes.
A Todoist-style "remind me in 3 days" habit is the manual version of the same idea.
- The guest advises **not** forcing the tooling; frameworks can complicate things.
For most people, talk to the agent directly, use plan mode, and let it guide you through connecting Search Console.

### Cost

- The skeptic's case raised by the host: the people who get rich from loops are the **token providers**, because people just burn tokens.
As a data point, **Peter Steinberger** reportedly spends ~**$1.3 million/month** on AI credits.
- **The guest's counter, specific to SEO:** a single run costs likely **under $5 in tokens** and only runs about once a month.
Compared to hiring an SEO agency, cost should not be a worry here.
- **These "infinite" loops are infinite over time**, not an agent trapped in a real-time infinite loop.
One shallow run every month for years; each individual run is small.
- **The proposed guardrail:** attach real economic values so a loop can stop itself - a click is worth 3 cents, a customer is worth $100 - and cap spend, since loops may run $50 / $100 / $200 a month depending on scope.
- Plan-based strategy: on a **Max plan ($100-200/month)** you effectively get thousands of dollars of tokens; on a tight $20 plan be much more careful and consider cheaper open-source models.

### The ads loop and the product-feedback loop

- **Ads loop:** the AI generates variants, reads performance data, kills losers, and doubles down on winners - what an ads agency does.
Facebook ads are fundamentally a **volume game**.
Give each variant **enough budget** to produce a statistically meaningful read before deciding.
- Where AI is weak versus strong: AI-generated **creative** probably still underperforms good human-made ads, but AI is clearly strong at **text changes** - swapping a line of copy and measuring - and at Google search ads where there is no imagery.
- The host's **human + AI thesis**: the best ads come from the best humans, but only if you have millions to spend.
For everyone else the winning approach is a mix - humans record raw material (a 30-second talking clip dropped into a folder daily), AI edits and optimizes around it.
- **The product-feedback loop is called the "holy grail":** an AI that both builds the product and learns from users.
It would read customer feedback, pull analytics (**PostHog**) and logs/errors (**Sentry**), prioritize the biggest pain points, prototype features, fix bugs, and judge itself on a chosen KPI (DAU, revenue, NPS, retention, virality).
- **Split the loops:** run a **bug loop** with an objective metric around **uptime** separately from a **feature loop** judged on **DAU/MAU**, retention, or virality.
- The guest expects real businesses built this way within a year, but a fully autonomous self-building business loop is **risky to run on a real business** today; treat it as experimental.

### Start small: the minimal viable loop

- Almost any part of a business can be set on a loop - social media, video content, cold outreach, support.
You (the founder) are the original agent, waking up and running your daily "how can I improve the business?" loop.
- **Do not hand the AI a giant goal** like "get 100,000 X followers."
Start with the **Minimal Viable Loop** - first just optimize for great posts, with a small verifiable outcome like **10 likes** or average impressions per post.
- **Pick a leading, achievable objective metric** (impressions or views per post per week) rather than a lagging vanity number (total follower count).
Follower growth is a downstream result, hard to move directly.
- Be realistic about which parts of the business a loop can genuinely move - the guest is skeptical you could get an AI to 100,000 followers - but note you lose little by trying.

## Connections

- [[business-loops]] - the source's core contribution: the loop primitive pointed at business metrics over months, not at a codebase over minutes.
- [[minimal-viable-loop]] - start with the smallest verifiable outcome, not the ambitious goal.
- [[loop-cost-discipline]] - attach real economic values so a loop can stop itself; the answer to the token-burn objection.
- [[leading-metric-over-vanity-metric]] - pick a metric the loop can actually move.
- [[verification-signal-picks-the-mechanism]] - **strong agreement from outside Anthropic**: "pick the number first, then build the loop around it" is the same rule stated from the business side.
- [[eval-driven-development]] - the Inbox Zero ≥90% eval threshold used directly as a loop stop condition; evals as control mechanism, not just measurement.
- [[agents-as-cron-plus-markdown]] - the memory-file-plus-schedule pattern, here applied to SEO experiments.
- [[agent-operations]] - the area this source anchors alongside [[running-teams-of-ai-agents]].
- [[building-marketing-agents]] - the ads loop here is the shallow version of what that source builds in full.
- [[get-out-of-the-loop]] - **tempered**: the recommended pattern keeps a human Slack approval on every run.
- [[claude-code]], [[openai]], [[boris-cherny]] - entities (Boris is credited by name as one of the people who popularized loop engineering).

## Source

- **Author:** An unnamed host interviewing a guest rendered in the captions as "Ellie", builder of **Inbox Zero** and **draftfantasy.com**
- **Title:** Using Loops to Run Your Business
- **Format:** YouTube tutorial, interview format; ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/Loops_to_run_your_business.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-01

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix.
Attribution is weak on this source: the **guest's name is only as-heard**, and several referenced people are flagged unverified in the appendix, including "Ditro"/"Demetro" (spelled two ways) and "Ross Mike."
Product and URL names flagged `[?]`: **atomieve.dev**, **Eve** (a Vercel project), **flow** (an Astro-team framework), and **GLM 5.2**.
The exact `/goal` syntax is not spelled out on screen.

The **$1.3 million/month** Peter Steinberger figure is reported second-hand by the host and should not be repeated as established fact.
