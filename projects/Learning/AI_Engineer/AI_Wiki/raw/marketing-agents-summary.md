# Building Marketing Agents That Actually Get You Customers
### Summary of a conversation between Greg (host) and Cody Schneider

---

## Overview

Cody Schneider joins the podcast to explain, end-to-end, what a real "marketing agent" is (as opposed to a linear Zapier-style automation) and how founders can deploy them to autonomously grow a company. The episode has two threads that are woven together throughout:

1. **A startup idea Cody loves**: an AI-first bundle of WordPress plugins (a "Lovable for WordPress").
2. **A full technical walkthrough** of how to build a marketing agent — using the WordPress idea as the working example — covering data pipelines, creative generation, the Facebook Marketing API, and the feedback loop that lets an agent improve itself over time.

Cody frames a marketing agent as needing three things: unified data clarity across the whole pipeline, autonomous decision-making on a thinking loop/cadence, and infrastructure (data pipeline + data warehouse + cloud hosting) to support it.

---

## Table of Contents

1. [What Is a Marketing Agent?](#1-what-is-a-marketing-agent)
2. [Business Idea: AI-First WordPress Plugin Bundle](#2-business-idea-ai-first-wordpress-plugin-bundle)
3. [Facebook Ads in the Age of Andromeda](#3-facebook-ads-in-the-age-of-andromeda)
4. [Building the Agent, Step by Step](#4-building-the-agent-step-by-step)
   - [4.1 Research Pain Points](#41-research-pain-points)
   - [4.2 Generate Ad Creative](#42-generate-ad-creative)
   - [4.3 Publish via the Facebook Marketing API](#43-publish-via-the-facebook-marketing-api)
   - [4.4 Build the Data Pipeline & Warehouse](#44-build-the-data-pipeline--warehouse)
   - [4.5 Host the Agent in the Cloud](#45-host-the-agent-in-the-cloud)
   - [4.6 The Learning/Feedback Loop](#46-the-learningfeedback-loop)
5. [Solving for Entropy](#5-solving-for-entropy)
6. [The Rise of the "Agent Jockey"](#6-the-rise-of-the-agent-jockey)
7. [Why Paid Ads Beat "Organic Only"](#7-why-paid-ads-beat-organic-only)
8. [More Marketing Agent Ideas (Grab Bag)](#8-more-marketing-agent-ideas-grab-bag)
9. [Corrections & Transcription Notes](#9-corrections--transcription-notes)

---

## 1. What Is a Marketing Agent?

> 💬 **Speaker Opinion (Cody):** Cody says he gets frustrated by how loosely "marketing agent" is used online — many people "talk a huge game" but the reality doesn't match the term when you dig in.

**📏 General Rule — Cody's definition, a marketing agent has to satisfy three things:**
1. **Data clarity** — unified visibility across the entire pipeline (not siloed data).
2. **Autonomous decision-making** — the agent acts on some cadence with a "thinking loop," not just a one-off script.
3. **Infrastructure** — a data pipeline, a data warehouse, and cloud hosting for the agent itself.

> 💬 **Speaker Opinion:** Cody explicitly does **not** want a fully autonomous "AGI" agent that thinks entirely on its own. He wants something that executes a defined process, looks at the resulting data, and improves based on that feedback — a narrower, more controllable definition than the "totally autonomous agent running your whole marketing stack" hype.

**Example given:** An agent can fully run a Facebook ads account — researching pain points/outcomes of the target customer, generating on-brand static and AI-avatar UGC video creative, publishing it to the ad account, turning off underperformers, promoting winners, and feeding results back into a loop that generates more content like the top performers.

---

## 2. Business Idea: AI-First WordPress Plugin Bundle

**Context:** Cody has pitched this idea to three YC-backed founders looking for a pivot; all declined, so he's sharing it publicly.

**📏 Key stat:** WordPress powers roughly **43% of the internet** (Cody notes he'd previously cited "50%+" from memory but confirmed 43% when he checked live).

> 💬 **Speaker Opinion:** Cody believes this is a "blue ocean" — a huge, underserved category that almost nobody is building AI-first products for.

### The Pitch
- Essentially **"Lovable (or anything.com) but for WordPress"** — let users vibe-code their website on top of WordPress.
- Bundle together the plugins people normally buy separately (forms, CRM, SEO, storefront, security, etc.) into a single subscription.
- Monetize via **token-based pricing** — e.g., a base tier around **$29/month** that includes a set number of tokens usable to build/design the site with pre-built features.
- Sell it at roughly **a fifth to a tenth of the cost** of buying all the individual plugins separately.

### Cody's Background Context
Cody was a partner in a WordPress migration agency around 2011, officially partnered with WordPress to migrate large sites (including **Time.com** and **TechCrunch.com**) off custom CMSs — giving him first-hand insight into how much money flows through the WordPress/Automattic plugin ecosystem.

### 🔧 Tool/Plugin Examples to "AI-ify"
| Existing Plugin | Category | AI-First Reimagining |
|---|---|---|
| **Yoast SEO** | SEO | Instead of red/green dot indicators the user must fix manually, have the agent auto-write meta descriptions, restructure content, and add internal links |
| **WPForms** | Forms | Replace static forms with a conversational agent that qualifies leads and answers questions |
| **WooCommerce** | E-commerce | An "AI storekeeper" that auto-writes product descriptions and builds abandoned-cart flows |
| **Akismet** | Spam/security | AI-driven spam and security protection |

> 💡 **Tip:** The core strategy is to find plugins with **already-validated demand** that lack an AI-first version, then rebuild them "10x better" with agents — you skip demand-validation risk because the market already proven to pay for the underlying function.

---

## 3. Facebook Ads in the Age of Andromeda

**🔧 Tool — Andromeda:** Meta's newer ad-serving algorithm. Rather than relying on interest-based targeting, Andromeda's AI reads the ad creative itself (image, video, on-screen text, video script) *and* the landing page content, then uses that combined understanding to decide which ad is shown to which person.

**📏 General Rule (per Cody):** Interest-based targeting (e.g., targeting people with a "WordPress" interest) is largely obsolete post-Andromeda. Instead, **the creative itself must speak directly to the pain point or outcome** of the target customer, paired with a landing page that clearly explains the product — Andromeda's AI does the audience-matching for you.

> 💬 **Speaker Opinion:** Cody says, "Facebook has turned into the best B2B ads channel that exists right now" — because sufficiently niche/obscure ad creative can find the small pool of people (he gives an example of maybe ~10 people in the US) who have that exact problem, generating qualified B2B leads.

**Example ad script structure Cody sketches for the WordPress idea:**
> "I used to be paying my agency $1,000/month to maintain my WordPress site and they were not responsive... but I found this plugin that lets me chat with AI to change my website, and it includes all the plugins I used to pay extra for. Click the link to learn more."

**📏 General Rule:** Set up **conversion events** for both the signup action and the payment action deeper in the funnel so Andromeda can optimize toward real revenue outcomes, not just clicks.

---

## 4. Building the Agent, Step by Step

Cody walks through the actual architecture for a Facebook ads marketing agent, using the WordPress example throughout.

### 4.1 Research Pain Points

- **🔧 Tool: Perplexity** — used live to scrape Reddit for pain points and desired outcomes among WordPress site owners (e.g., "why would they buy an AI WordPress tool that solves plugin problems and lets them vibe-code the site design?").
- **Why Reddit specifically:** it captures real people complaining in their own words — genuine unfiltered dialogue.

> ⚠️ **Caution (Cody's own admission):** Reddit is increasingly being "eroded" by people manipulating threads so LLMs will rank/cite them — part of what Cody wryly calls "the dead internet." He admits, "I am the problem," acknowledging his own role in that manipulation.

**Process:**
1. Pull raw pain points from Reddit via Perplexity.
2. Rank/stack them by **most referenced** to identify the top 3.
3. Use the top pain points to seed ad creative concepts.

**Example pain points surfaced:**
- Content workflows / customization requiring development skills → biggest referenced pain point → becomes the primary ad angle.
- Performance and speed → consider lightweight frameworks like **Astro** to serve content fast.
- Security and maintenance → messaging around never worrying about plugin security, site hacks, or Google de-indexing.

### 4.2 Generate Ad Creative

- **🔧 Tool: Kie AI** (referred to in the transcript as "Kai AI") — an aggregator that provides access to multiple image and video generation models in one place, used for bulk static ad creative generation.
- **🔧 Tool: Google Nano Banana** — image generation model used for static ad creative, seeded with an example ad from a competitor or a tangentially related industry.
- **🔧 Tool: HeyGen** — still used for AI avatar UGC-style video ads and, per Cody, still getting great results despite not being the newest option.
- **🔧 Tool: Seedance** — an emerging video generation tool Cody is experimenting with more; current limitation is clip length (roughly under 9 seconds per generation — *unconfirmed exact number, Cody says "don't quote me"*), requiring frame-stitching for longer videos.

> 💡 **Tip:** Define explicit **brand style guides** (fonts, colors, brand specifics) and run outputs through a vision model that checks generated creative against those guides — verifying text readability and on-brand font usage before anything goes live.

### 4.3 Publish via the Facebook Marketing API

- **🔧 Tool: Facebook Marketing API** — used to publish, pause, and promote ads programmatically.

> ⚠️ **Caution / Common Misconception:** Cody directly addresses the common claim that "my Facebook ads account got banned because I used an agent." **The agent isn't the cause of bans** — accounts get banned for violating Facebook's Terms of Service, typically by spamming the API (e.g., trying to pull hundreds of millions of rows of account data). 

**📏 General Rule:** Use the Facebook Marketing API primarily for **write actions** — publishing content, turning ads off, promoting/boosting ads — not for bulk-pulling excessive data, which is what triggers ToS violations.

### 4.4 Build the Data Pipeline & Warehouse

**🔧 Tool: Airbyte** — an open-source, self-hostable data pipeline tool with pre-built connectors that pipe data from multiple sources into a data warehouse.

**🔧 Tool: ClickHouse** — an open-source, self-hostable data warehouse used to unify all data sources into a single queryable location.

**What "data warehouse" means in this context (Cody's explanation):** A single location that unifies all your data sources so the agent has context across *all* channels simultaneously — not just one data source in isolation.

**Example data sources unified for a Facebook ads use case:**
- Facebook Ads data
- Google Analytics data
- PostHog data
- CRM data (e.g., HubSpot)
- Stripe data (to trace ad spend all the way through to actual revenue)

> 💡 **Tip:** With this unified data warehouse connected to your coding agent (Claude Code, Codex, etc.), you gain **conversational analytics** — you can literally ask business questions like "we're having trouble hitting payroll this month, what's going wrong?" and get an answer sourced from live data (e.g., "your accounts receivables are off").

### 4.5 Host the Agent in the Cloud

> 💬 **Speaker Opinion:** Cody jokes about people running these setups locally on repurposed hardware (e.g., "a Mac Mini I bought for OpenClaw that's now working as a server") — his position is that this isn't necessary; cloud hosting is simpler and more scalable.

**🔧 Tool options mentioned for hosting:** Heroku, Railway, or "any" cloud provider — Cody presents these as interchangeable examples, not a strict recommendation.

**📏 General Rule:** Under the hood, "an agent is just code" — a decision tree fed a live data stream, with an LLM-driven decision loop optimizing toward a defined outcome (most commonly: more revenue).

### 4.6 The Learning/Feedback Loop

Example cadence Cody describes running for an actual client:
- **2 new ad sets per day, 5 ads per ad set**, auto-uploaded to Facebook Ads based on prior research and warehouse data.
- Each new batch runs for a **2–3 day window** to gather initial performance signal.
- Worst-performing ads are automatically turned off.
- Winning ads move into a **"winners pool"** where they compete against each other for available ad budget.
- A vision model (or, increasingly, a structured database of the JSON prompts/scripts used to generate each ad) analyzes what's actually working so future creative generation improves.

---

## 5. Solving for Entropy

**Problem:** An agent left alone tends to "get stuck thinking in the same way" — creative ideation stagnates over time.

**Two solutions Cody uses:**

1. **🔧 Facebook Ads Library** — pull ads from competitors' public ad libraries to inject "new DNA" into the creative system, using them as fresh source material for research.
2. **YouTube & podcast transcripts** — pull insights from niche-specific YouTube channels (e.g., channels dedicated to WordPress) and podcast transcripts, extracting insights to seed new ad angles.

**🔧 Tool: Viral Loop [?]** *(name as heard in transcript — could not be fully confirmed; possibly "Viralo" or similar)* — described as an API that scrapes TikTok (and reportedly Instagram Reels) to surface the most viral posts within a given category, which can then inform creative trend direction (e.g., "show me the most viral posts in the beauty category from the last week").

> ⚠️ **Caution:** Cody stresses this entropy problem is rarely discussed publicly — most people describe these systems as "set it up once and it's just good," which he directly disputes (see Section 7).

---

## 6. The Rise of the "Agent Jockey"

> 💬 **Speaker Opinion:** Cody frequently talks with marketers asking "is my job secure?" His candid answer: it depends on whether they can adapt. He describes the emerging role as an **"agent jockey"** — someone who takes their existing domain knowledge and encodes it into agent-driven systems rather than executing tasks manually.

**📏 General Rule (per Cody):** You don't need to be deeply technical to do this. A semi-technical person with access to a coding agent (e.g., Claude Code) can feed it a transcript like this one and be walked through building the actual system described.

---

## 7. Why Paid Ads Beat "Organic Only"

> 💬 **Speaker Opinion:** Both Cody and Greg push back on founders who only want to do organic/word-of-mouth growth, calling it a "rookie way to look at the market." Cody's framing: paid ads are the only system where "I put a dollar in and $5 can potentially come out the other side," and you can keep feeding that multiplier at scale.

**📏 General Rule — common mistake to avoid:** Founders often run a handful of ads, see no results, and give up — without realizing the same core ad often needs **10–20 variations in positioning** before finding what resonates. Cody notes he's regularly surprised by which positioning angles end up working.

**Example given:** For a hypothetical WordPress plugin competing with Yoast, an unconventional angle like an explicitly "anti-Yoast" positioning might be the one that performs.

> 💬 **Speaker Opinion:** "We're not Don Draper" — Cody rejects the idea of imposing a predetermined message on the market. Instead, the approach is to test broadly (he references testing "a thousand different ad creatives") and let market response — visible within about 48 hours — reveal what's actually resonating.

**Context — why this is newly accessible:** Historically, this level of ad testing required hiring an agency for tens of thousands of dollars per month. Cody's position is that founders can now build the described agent system themselves (with fine-tuning still required) at a fraction of that cost.

**📏 General Rule:** Marketing should be treated as **continuous, not campaign-based** — Cody argues that because feedback loops are now much faster (he compares it to how fashion trends now cycle roughly 10x faster than 20 years ago), businesses need constant observability into shifting trends rather than a "start and stop" campaign mentality.

---

## 8. More Marketing Agent Ideas (Grab Bag)

Cody rattled off additional agent concepts he plans to cover in a future follow-up, time permitting:

- **Google Ads agents** — entirely running a Google Ads account.
- **Influencer outreach agents** — researching influencers in-category, cold-emailing them, negotiating pricing, and hand-raising promising responses to a human.
- **Cold email agents** — finding target customers, sourcing email addresses, sending cold emails, and managing the inbox/booking responses.
- **TikTok "reel farms"** — running multiple TikTok accounts in the cloud, generating product-related slideshows at scale, scheduling/posting, and aggregating view data.
- **SEO agents** — keyword research, article research and writing, tuning for on-brand voice/perspective to both rank well and read well.
- **AI search / citation agents** — building citations and doing outreach to get a brand listed in AI search results for its category.
- **Social media management agents** — running LinkedIn and Twitter/X accounts.
- **Podcast-to-newsletter agents** — researching a podcast topic, writing the script, using **ElevenLabs** ("11 Labs") voices to read it, and building lead magnets/email lists off the resulting content (example industry given: e-commerce).

> 💬 **Speaker Opinion:** Cody says he'd return to cover these in depth if there's audience interest, noting this space is currently an all-consuming focus for him personally ("this is all I think about... from when I wake up to when I go to bed").

**Where to follow up:** Cody is active on **Twitter/X** and **LinkedIn**, and the company doing this work is **companiesgraph.com**.

---

## 9. Corrections & Transcription Notes

| As captioned | Likely correct | Confidence |
|---|---|---|
| "Kai AI" | Kie AI | Moderate — matches a known multi-model image/video generation aggregator; flagged `[?]` where referenced |
| "Viral Low" | Possibly "Viralo" or similar TikTok/Reels trend-scraping API | Low — kept as heard, flagged `[?]`; exact product name unconfirmed |
| "seed dance" | Seedance (video generation model) | High |
| "hey Jen" | HeyGen (AI avatar video tool) | High |
| "air bite" | Airbyte (data pipeline tool) | High |
| "click house" | ClickHouse (data warehouse) | High |
| "a kismmet" | Akismet (WordPress spam plugin) | High |
| "companiesgraph.com" | companiesgraph.com (kept as stated) | High |

**Note:** Filler words, false starts, and repeated words characteristic of spoken conversation were removed for readability; all tool names, numbers, and proper nouns were preserved as spoken except where corrected above.
