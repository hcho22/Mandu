# Using Loops to Run Your Business

**A practical guide to "loop engineering" for SEO, ads, and product — with Ellie**

*Detailed summary of a YouTube tutorial (interview format: host + guest "Ellie"). Section order follows the flow of the conversation. Speaker opinions are flagged separately from general rules.*

> **Overview.** "Loop engineering" went viral for *building products*, but this tutorial argues the more valuable use is *running a whole business* on loops. A loop is a simple, old idea — **build → measure → learn** (Lean Startup / Toyota) — pointed at an AI agent that iterates against an **objective metric** over long time horizons (weeks, months, even years) rather than a single half-hour run. The tutorial walks through concrete, copyable loops: an **SEO loop** (the anchor example), a **Facebook/ads loop**, and a **product-feedback loop** (the "holy grail"), plus cost analysis and how to actually set one up in Claude Code or Codex.

**Callout legend:** 💡 TIP · 🛠️ TOOLS · 📏 RULE · 💬 OPINION · ⚠️ CAUTION

---

## Table of Contents

1. [What "Loop Engineering" Is (and Why It's Not New)](#1--what-loop-engineering-is-and-why-its-not-new)
2. [How Loops Work with AI Agents: Build → Verify → Learn](#2--how-loops-work-with-ai-agents-build--verify--learn)
3. [The SEO Loop — The Core Example](#3--the-seo-loop--the-core-example)
4. [Setting Up an SEO Loop, Step by Step](#4--setting-up-an-seo-loop-step-by-step)
5. [Cost–Benefit of Loops](#5--costbenefit-of-loops)
6. [The Facebook / Ads Loop](#6--the-facebook--ads-loop)
7. [The Product-Feedback Loop (the "Holy Grail")](#7--the-product-feedback-loop-the-holy-grail)
8. [Other Loops & the "Minimal Viable Loop"](#8--other-loops--the-minimal-viable-loop)
9. [Appendix: Caption Corrections & Uncertain Items](#appendix--caption-corrections--uncertain-items)

---

## 1 · What "Loop Engineering" Is (and Why It's Not New)

Loop engineering became popular roughly a month before recording, after **Boris** (from **Claude Code**) and **Peter Steinberger** began tweeting about it. The term is new; the concept is not. A friend of the guest ("Ditro"/"Demetro") posted a semi-joking tweet along the lines of: *you don't prompt anymore — your software should build itself and reach product-market fit on its own; your only job is to find money to pay for tokens and take care of yourself.* The joke prompted a serious question: **what would it actually look like to run an entire business as a loop?**

The lineage is explicit:

- **Lean Startup** (Eric Ries, ~10–15 years ago): the **build → measure → learn** loop.
- **Toyota / lean manufacturing**: the highly efficient, constantly-iterating assembly line that inspired Lean Startup. Reliable, consistent cars at good prices came from the loop mechanism.
- You already run loops today — improving SEO (where do I rank → what can I fix → did I move up?) is itself a loop with accurate feedback from Google.

> 📏 **GENERAL RULE**
> Any process running on a schedule is already a form of loop. The point of "loop engineering" is just getting an **agent** to run that same build/measure/learn cycle for you.

> 💬 **SPEAKER OPINION**
> The host's favorite loop is the **last one covered** (the product-feedback loop). Both speakers agree the surrounding hype/terminology is overblown even though the underlying idea is genuinely useful — a point credited to their guest "Mike," who is skeptical of the loop hype (see §5).

> ⚠️ **CAUTION**
> The really long-horizon framing is deliberate: these loops may run **once every few weeks for months or years**, not continuously for half an hour. Don't picture a chatbot spinning in real time.

---

## 2 · How Loops Work with AI Agents: Build → Verify → Learn

The agent loop mirrors Lean Startup's build/measure/learn:

- **Build** — tell the AI to go do the thing ("build my new SaaS," write the SEO change, draft the ad).
- **Verify** — an objective check that it worked (tests pass, a browser agent clicks through, an eval scores high enough, or a separate checker agent confirms).
- **Learn** — feed the result back in and iterate.

In Claude Code, the `/goal` command runs this pattern: a checker agent verifies whether the goal is met and, if not, tells the main builder agent to keep looping until it works.

### Stop conditions (the non-negotiable part)

Every loop must converge on a result, or it loops forever. Example stop conditions given:

- **"The feature works in the browser."** e.g. `/goal make signup work` → loop ends once sign-up works.
- **Eval threshold.** For the guest's product **Inbox Zero** (an AI that manages your inbox), evals test how well a model categorizes emails (does an incoming newsletter get tagged "newsletter"?). Target: **evals ≥ 90%**. If it's only passing **88%**, the agent adjusts the prompt or swaps the model and retries until it clears 90%.

> 📏 **GENERAL RULE**
> A loop needs (1) a defined **stop condition** and (2) an **objective metric / input fed back into the system**. Without a clear metric, there's nothing to converge on.

> 🛠️ **TOOLS**
> - **Claude Code** and **Codex** — the agents used to run loops.
> - `/goal` — Claude Code command that runs the build/verify loop with a checker agent.
> - **Evals** — automated tests scoring AI quality; here used as the loop's objective metric.
> - **Browser agents** — used in the verify step to click through a real UI.

> 💡 **TIP**
> The verify step doesn't have to be product/engineering-related. *Any* objective metric can close the loop — Google ranking, ad ROAS, retention. Pick the number first, then build the loop around it.

---

## 3 · The SEO Loop — The Core Example

SEO is the anchor example because it generalizes to almost everything else. The objective metric is unambiguous: **where you rank in Google search**. It's "black or white" — you moved up, moved down, or stayed the same.

Concrete numbers cited:

- Search **"inbox zero"** on Google → **Inbox Zero ranks #1**.
- For **"AI email assistant"** (a high-value term) → ranked ~**position 30**; the loop's job is to push it onto page one.
- **Inbox Zero domain rating ≈ 63–64** (matters — a brand-new site with a very low domain rating may behave differently).

### Live demo: draftfantasy.com

The guest shows Google Search Console for **draftfantasy.com** (a business he started ~12 years ago, still running, boosted lately by the World Cup):

- **10 million impressions** over the last 3 months.
- For the search term **"380"**: **~120,000 clicks**, ~**1 million impressions**, average position **~4.4** (ranked ~4th).
- Claim: pushing that term from ~4 to 2–3 could turn 120K clicks into perhaps half a million.
- ~2 days before recording he told Claude Code to run the same SEO loop on Draft Fantasy "because why not" — it runs in the background, remembers what it did, and keeps improving.

> 💡 **TIP (works loops or not)**
> The single easiest win across any business: **connect your AI to your real tools and real data.** That alone lets it make far smarter decisions than working blind.

> 💡 **TIP — quick SEO wins to grab first**
> Have AI run a **site audit** regardless of loops. Common fast fixes: improve **meta tags**, add **JSON-LD** structured data for a small boost, add a missing **sitemap**, and check for **keyword/link cannibalization** (two of your own pages splitting link power for the same term).

> 🛠️ **TOOLS for the SEO loop**
> - **Google Search Console** (has an **API**) — your ranking data: queries, impressions, clicks, average position; also shows which pages outrank you.
> - **DataForSEO** — an SEO API (comparable to **Ahrefs** and **SEMrush**) that shows how you rank against competitors.

> 📏 **GENERAL RULE**
> The loop structure: make improvements → check the objective metric (Google ranking) → record what was tried in a memory file → weeks/months later, review whether the experiment moved the term up or down, then iterate. This is exactly what an SEO agency does for you.

> 📏 **GENERAL RULE**
> **SEO takes months, not days.** Don't expect results in 24 hours. This is a background loop; results compound and can suddenly "bear fruit" around month four.

> 💡 **TIP — remember & revert**
> Have the agent keep a **markdown file** logging every change so the next run can check its own past experiments. Because each change is just an experiment, if a change drops you (e.g. position 20 → 30) you can simply **undo it** — nothing is set in stone.

> 💡 **TIP — LEO / GEO comes free**
> Everything you do for Google SEO also benefits **LEO / GEO** (ranking inside LLMs / generative search). Still valuable even if your audience has moved off Google search.

> 💬 **SPEAKER OPINION**
> The guest is happy to run this loop on an established site *or* a brand-new one. The host's framing: worst case you revert the change, and most people weren't going to hire an SEO expert anyway — so there's little downside to trying.

---

## 4 · Setting Up an SEO Loop, Step by Step

The "lazy" starting recipe the host proposes and the guest endorses:

1. Screenshot your Google Search Console chart.
2. Paste it into **Claude Code** or **Codex** and say you want to create an SEO loop.
3. Give it access to **Google Search Console** / **DataForSEO**.
4. Tell it to be judged on the objective metric: **Google ranking**.

### A ready-made reference prompt

The guest points to **atomieve.dev**, a site with a real, expanded version of this SEO-improver prompt — essentially an `instructions.md` for the job ("you are the SEO improver; you're judged on these three metrics…"). One instruction shown: *when applying changes, select the subset of this week's recommendations that map cleanly to files in the blog repo.* You can copy that URL/prompt straight into Claude Code or Codex.

> 🛠️ **TOOLS & references mentioned**
> - **atomieve.dev** — reference site hosting the full SEO-improver prompt + `instructions.md`.
> - **Eve** — a Vercel project (one way to build agents; optional).
> - **flow** — a framework by the **Astro** team (optional; another agent-building path).
> - **plan mode** — use it to let the agent map out the setup before executing.
> - Blog hosting the agent connects to: **WordPress**, **GitHub**, or wherever your blog lives.

### Scheduling / automation (the one extra step that matters)

To make it a true long-running loop, add automation so it picks up where it left off every few weeks:

> 🛠️ **AUTOMATION options**
> - **Claude** — "routines."
> - **Cursor** — "automation."
> - **Codex** — "automations."

> 💡 **TIP — stay in the loop (human approval)**
> Have the agent **ping you on Slack** when each run finishes so you can quickly approve or reject its changes. A Todoist-style "remind me in 3 days" habit is the manual version of the same idea.

> 💬 **SPEAKER OPINION**
> The guest suggests **not** forcing the tooling: Eve/flow can actually *complicate* things for some people. For most, just talk to the agent directly, ideally use plan mode, and let it guide you through connecting Google Search Console (a CLI or the Google API). Running it on your own computer is the easiest path.

---

## 5 · Cost–Benefit of Loops

The host raises the skeptic's case (from friend "Ross Mike," a front-end engineer): the people who get rich from loops are the **token providers**, because people just burn tokens. As a concrete data point, **Peter Steinberger** — now at OpenAI — reportedly spends **~$1.3 million/month** on AI credits.

The host's proposed guardrail: attach real economic values so a loop can stop itself — e.g. *a click is worth 3 cents*, *a customer is worth $100* — and cap spend, since loops may run **$50 / $100 / $200 a month** depending on scope.

> 💬 **SPEAKER OPINION — the SEO loop is cheap**
> The guest agrees the general hype/cost concern is fair, but argues the **SEO loop specifically is very cheap** and worth doing. His estimate: a single run costs likely **under $5 in tokens**, and it only runs ~once a month. Compared to hiring an SEO agency, cost shouldn't be a worry here.

> 📏 **GENERAL RULE**
> These "infinite" loops are infinite *over time* (one shallow run every month for years), not an agent trapped in a real-time infinite loop. Each individual run is small.

> 💡 **TIP — plan-based cost strategy**
> - On a **Max plan ($100–$200/month)**, you effectively get thousands of dollars of tokens — don't sweat cost for something like this.
> - On a tight **$20 plan**, be much more careful; consider cheaper open-source models (e.g. **GLM 5.2** [?]) for this kind of task.

> ⚠️ **CAUTION**
> Loops *do* cost money and it accumulates. Set a budget and, ideally, tie stop conditions to real value (cost per click / cost per customer) so a loop can't quietly run up spend.

---

## 6 · The Facebook / Ads Loop

Run ads (Facebook, or Google search ads) where the AI generates variants, reads the performance data, kills losers, and doubles down on winners — the same thing an ads agency does. Facebook ads are fundamentally a **volume game**: many narratives, hooks, and audiences (male/female, older/younger) tested against how the algorithm reacts.

> 📏 **GENERAL RULE**
> Give each variant **enough budget** to produce a statistically meaningful read before deciding whether it worked or not.

> 💬 **SPEAKER OPINION — where AI is weak vs strong**
> Guest: AI-generated **creative** (video/graphics) probably still underperforms good human-made ads today, though some AI ads run well. AI is clearly strong at **text changes** — swapping a line of copy, then measuring — and at Google search ads where there's no imagery, just copy.

> 💬 **SPEAKER OPINION — the host's "human + AI" thesis**
> The best ads come from hiring the best humans — but only if you have millions to spend ("we're not making Super Bowl ads here"). For everyone else, the winning approach is a **mix of humans + AI**: humans record raw material (e.g. a 30-second talking clip dropped into a folder daily), AI edits and optimizes around it. You keep the human feel with AI optimization on top.

> 💡 **TIP**
> You're running this loop anyway — the human version is a Todoist reminder ("look at Facebook ads in 3 days"). You don't need to watch it hourly; you need to periodically review results and try new angles. AI's edge is testing **far more variants** than a human could.

---

## 7 · The Product-Feedback Loop (the "Holy Grail")

The most ambitious loop: an AI that both **builds the product** and **learns from users**, then builds more — the Lean Startup loop applied to the whole company. It would:

- Read **customer feedback**.
- Pull **analytics** (**PostHog**) and **logs / errors** (**Sentry**).
- Prioritize the biggest pain points, prototype features, and fix bugs.
- Judge itself on a chosen KPI — **DAU**, revenue, **NPS**, retention, or virality (you pick, or let the agent propose a KPI per feature for your approval).

> 💬 **SPEAKER OPINION — split the loops (host)**
> Run a **bug loop separate from a feature loop**:
> - **Bug loop** → objective metric around **uptime** and reliability.
> - **Feature loop** → core product metrics like **DAU/MAU**, retention, or virality.
>
> The guest agrees this is a good way to structure it.

> 💬 **SPEAKER OPINION — this is the future, but…**
> The guest calls this the "ultimate" / "holy grail" loop and expects real businesses built this way within a year (early experiments already exist, though none are doing incredibly well yet). "Anything that can be done at a computer, AI can do."

> ⚠️ **CAUTION**
> A fully autonomous, self-building business loop is **risky to run on a real business** today. Treat it as experimental rather than something to hand your live product to.

---

## 8 · Other Loops & the "Minimal Viable Loop"

Almost any part of a business can be set on a loop: social media, video content, cold outreach, support. You (the founder) are the original agent — you wake up, the alarm goes off, and you start your daily "how can I improve the business?" loop. The goal is to put the AI in that same mode, each cycle checked against an objective metric (likes, impressions, conversions, views).

> 💬 **SPEAKER OPINION — start small (the "MVL")**
> Host: don't hand the AI a giant goal like "get 100,000 X followers." Start with the **Minimal Viable Loop (MVL)** — first just optimize for **great posts**, with a small verifiable outcome like **10 likes** (or average impressions/views per post). The guest agrees 100% — 100K followers should *not* be the outcome.

> 📏 **GENERAL RULE**
> Pick a **leading, achievable** objective metric (impressions or views per post/week) rather than a lagging vanity number (total follower count). Follower growth is a downstream result, hard to move directly.

> ⚠️ **CAUTION**
> AI won't do everything well. The guest is skeptical you could get an AI to **100,000 Twitter/X followers**. Be realistic about which parts of the business a loop can genuinely move — but note you lose little by trying.

> 💡 **TIP — the founder's own workflow**
> Mirror what good creators already do manually: "I posted 10 tweets this week, 9 flopped, 1 did well — why did that one work, and how do I do it better next time?" That review-and-iterate habit *is* the loop; the question is whether an agent can run it for you.

---

## Appendix · Caption Corrections & Uncertain Items

Auto-caption fixes applied in this summary. Items marked **[?]** could not be verified from the transcript alone and are flagged rather than silently asserted.

| As heard in captions | Corrected / used here | Note |
|---|---|---|
| "cloud code" | Claude Code | Clear mishearing; product name. |
| "codeex" / "codecs" | Codex | OpenAI's coding agent. |
| "/ash goal" / "slash goal" | `/goal` | "slash goal" = the `/goal` command. [?] exact syntax not spelled out on screen. |
| "Eric Reese" | Eric Ries | Author of *The Lean Startup*. |
| "Boris from Op, well, Boris from Claude Code" | Boris (Claude Code) | Self-corrected by the speaker mid-sentence. |
| "Peter Steinberger from OpenClaw" / "works for OpenAI" | Peter Steinberger [?] | "OpenClaw" is likely a caption error; speaker later says he now works at OpenAI. Employer stated as OpenAI. |
| "Ditro" … "Demetro's question" | Ditro / Demetro [?] | Same person, spelled two ways in captions; true spelling uncertain. |
| "in 2026 Six, you don't prompt anymore" | "in 2026 …" [?] | "Six" appears to be a caption artifact; tweet is paraphrased, not quoted verbatim. |
| "HFS" | Ahrefs | SEO tool named alongside SEMrush. |
| "data for SEO" | DataForSEO | SEO data API. |
| "JSON LDS" | JSON-LD | Structured-data markup. |
| "atomieve.dev" | atomieve.dev [?] | URL transcribed as heard; exact spelling unverified. |
| "Eve … a versel project" | Eve (Vercel project) [?] | "versel" = Vercel. Project name "Eve" as heard. |
| "flu framework by the Astro team" | flow (Astro team) [?] | Framework name transcribed as "flow"; spelling unverified. |
| "post hog" / "sentry" | PostHog / Sentry | Analytics / error-monitoring tools. |
| "to-doist" | Todoist | Task app. |
| "GLM 5.2" | GLM 5.2 [?] | Open-source model named as a cheaper option; version as heard. |
| "Ross Mike" | Ross Mike [?] | Guest referenced from a prior episode; name as heard. |
| "a true pulsia … company builder" | [?] unclear word | "pulsia" could not be resolved; meaning ≈ a genuine autonomous company-builder. |
| "LEO / GEO" | LEO / GEO | LLM / Generative Engine Optimization (ranking inside LLMs). |
| "380" (Draft Fantasy term) | "380" | Preserved verbatim as the search term shown in the demo. |

---

> **Obsidian note:** if you use Obsidian and prefer its native callout syntax, the blockquotes above can be swapped to `> [!tip]`, `> [!info]` (tools), `> [!note]` (rules), `> [!quote]` (opinions), and `> [!warning]` (cautions). The emoji-blockquote form used here renders cleanly in both GitHub and Obsidian without any plugins.
