# Running Teams of AI Agents — Ryan Carson

**Format:** Podcast interview (host: Greg) · **Guest:** Ryan Carson, founder/CEO of Untangle

---

## Overview

Ryan Carson argues that the highest-leverage skill of this era is being an *operator of agent fleets*. His background: ~25 years as a founder/CEO, now on his fourth company. His previous company, **Treehouse**, reached ~110 full-time employees and taught a million people to code, and was acquired. His current company, **Untangle**, is an AI divorce agent for family-law firms — and he is currently its **only employee**, with a seed round raised, revenue projected to **4x this month**, and first hires imminent.

The episode is organized around three things he wants you to be able to do: **run cloud agents**, **build automations**, and **ship faster**. A fourth, softer theme runs underneath: build a public reputation so the network compounds.

His central reframe: *no matter what you used to be — IC, people manager, founder, VC, parent, student — you are now a manager of agents, and you should aim to be world-class at it.*

> ⚠️ **Caution — shelf life**
> The speaker explicitly notes this entire landscape changes every **3–6 months**. Treat specific tools and prices as a snapshot, not a permanent map.

---

## Table of Contents

1. [The reframe: you are a manager of agents](#1-the-reframe-you-are-a-manager-of-agents)
2. [The setup: desk and phone](#2-the-setup-desk-and-phone)
3. [Pillar 1 — Work in the cloud, not locally](#3-pillar-1--work-in-the-cloud-not-locally)
4. [Managing yourself: high-stakes decisions all day](#4-managing-yourself-high-stakes-decisions-all-day)
5. [Pillar 2 — Automations](#5-pillar-2--automations)
6. [Cost, model routing, and choosing your stack](#6-cost-model-routing-and-choosing-your-stack)
7. [Pillar 3 — The software factory, and building in public](#7-pillar-3--the-software-factory-and-building-in-public)
8. [Quick reference: tools and numbers](#8-quick-reference-tools-and-numbers)
9. [Appendix: caption corrections and editorial notes](#appendix-caption-corrections-and-editorial-notes)

**Callout key:** 💡 Tip · 🛠️ Tool · 📏 General rule · 💬 Speaker opinion · ⚠️ Caution

---

## 1. The reframe: you are a manager of agents

**Key points**

- The promise of the episode: by the end you should be able to (a) run cloud agents, (b) build automations, (c) ship faster.
- The role change is universal. Whatever your previous job title, your new job is managing agents — and the target isn't competence, it's being the best at it.
- Counterintuitively, managing agents makes you **more** technical, not less. To direct agents well you end up having to understand Postgres, production vs. dev environments, migrations, and so on — and you learn all of it *by using the agents*.
- Ryan says he is more technical now than at any point in his life.
- The right mental model is **engineering manager**, not "prompt user."

> 💬 **Speaker opinion**
> "It is a farce that engineering is going away." Anyone claiming engineers are disappearing or becoming less technical, he says, is not doing the work.

> 📏 **General rule — the carpenter analogy**
> If robot carpenters existed, a *real* carpenter would manage them far better than a non-carpenter, because they know where the cut goes and where the nail goes. Domain skill makes you a better manager of agents, not a redundant one.

> 💡 **Tip**
> The best way to learn this is to do it. Get your hands dirty, try it a few times, get your reps in — don't try to learn agent operations by reading about it.

---

## 2. The setup: desk and phone

### The desk

Ryan works from a home office in Connecticut.

**Key points**

- One **52-inch Dell monitor**, replacing a previous multi-monitor rig. He deliberately chose a single huge display over several.
- He tiles **eight panes at once**, because he has to supervise many agents simultaneously. Typical layout:
  - **Slack** (top left) — the notification surface for what agents are doing. That's essentially all he uses Slack for.
  - **1Password** — always open, for keys.
  - **Devin** — where most of the work happens.
  - **Two panes for testing the app** — "it's just a lot of testing."
  - **X** — top left and top right.
  - **Codex** (bottom right) — used for local/desktop work.

> 🛠️ **Tools on the desk**
> **Devin** (Cognition) · **Codex** (OpenAI) · **Slack** · **1Password** · **Ugmonk Analog** paper to-do system · **Razer** vertical mouse · **Wispr Flow** (voice dictation, bound to a physical button) · one **52-inch Dell** monitor.

> ⚠️ **Caution — never give agents production write keys**
> Production writes are dangerous and agents *will* do something bad. Keep keys secure, separate, and in 1Password. Build the workflow so the agent **asks you** for the key when it needs to write to prod; you then paste it into that session, and both of you are explicit about what's happening.

> 💡 **Tip — ergonomics and voice**
> He switched to a **vertical mouse** (Razer) after significant wrist pain. He also runs almost all input through **Wispr Flow** on a dedicated button rather than typing.

> 💡 **Tip — analog for priorities**
> Alongside all of this he keeps a handwritten daily to-do list on the **Ugmonk** system. He calls it "a little bit weird" and "hilarious," but it's the mechanism that keeps the day's real priorities from being drowned out.

### The phone

**Key points**

- He does roughly **50% or more of his work from his iPhone**.
- The mechanism is simple: Devin runs in a mobile browser, so he can check a PR, give feedback, or land a PR from anywhere — including from the shower.
- He frames this as non-optional if you're chasing product-market fit or 4x-ing revenue in a month: agents are blocked waiting on your decisions, so waiting until you're back at your Mac makes no sense.

> 💬 **Speaker opinion — the homework**
> He challenges the host directly: next time we talk, be doing **more than 50% of your work on your phone**. "If you ran a big team and you were out to lunch on your boat all the time, you'd have to get in the office — and the office is your phone."

---

## 3. Pillar 1 — Work in the cloud, not locally

### Why local development breaks down

**Key points**

- Local development means running your own database, authentication, dev server — the whole environment on your Mac.
- To do **two** things at once you need **git worktrees** (technical and hard to reason about) or literally a second copy of the repo in another directory.
- Three, four, five, ten parallel efforts? It simply doesn't work.
- The overhead isn't just mechanical — it's mental: *which worktree am I on? has this been synced? does this change collide with that one?* That overhead is what stops you shipping.

### What cloud agents do instead

**Key points**

- A cloud harness spins up a **VM** — a small server that *is* your dev environment — per session, on a button click.
- You can create effectively **infinite** numbers of them, with **zero risk of code collision**.
- Ryan typically runs **at least 5 cloud agents at once, often 10**.
- His workflow reduces to: open browser → new session → new VM → work. He never thinks about environment coordination.

### Why Devin specifically

**Key points**

- **Devin** launched roughly **2 to 2.5 years ago**, pitched as an AI software engineer. It didn't work well then — no matter how good the harness was, the **models weren't good enough**.
- By **2026**, the models are good enough, and a well-built cloud harness on top of them is genuinely good.
- Devin is described as "one of the best software factories in the industry" — expensive, but good.
- Ryan is explicit that **the lessons in the episode are not Devin-specific**; they just happen to work well in Devin.

**The landscape as he frames it**

| Category | Examples |
|---|---|
| Frontier-lab harnesses | **Codex** (OpenAI), **Claude Code** (Anthropic) |
| Independent agent labs | **Amp**, **Cursor** (he notes it's no longer independent), **Cognition** (Devin), **Factory** |

> 💬 **Speaker opinion — strongly stated**
> "If you are working locally, I honestly think you are a caveman." He argues you're shipping **10x less** than you could be, and that the belief that serious people work locally is out of date. On the "local maxis" who mock cloud VMs as amateurish: "They are not doing real work."

> 📏 **General rule — the one legitimate exception**
> Heavy new front-end work. If you're shipping a feature with a lot of new UI, spin up a **local** agent for light front-end and wireframing. But move it into the cloud **as quickly as you can** and let a cloud agent take over.

> 💡 **Tip — the forcing function**
> The trigger for his own switch was reaching product-market fit at Untangle: once real customers needed real fixes and real features, he had to roughly **50x his output**, which is not achievable locally.

---

## 4. Managing yourself: high-stakes decisions all day

This section answers the obvious follow-up: if you 50x your output, how do you not go insane?

**Key points**

- **Redefine what your work is.** Your job is now making high-stakes decisions almost all day.
- The old cadence: maybe **2–3 high-stakes decisions per day**, communicated in a meeting, executed over two weeks.
- The new cadence: **10–20 high-stakes decisions before lunch**.
- Agents are an infinitely scalable team that works very fast — and they will be **blocked by you**. You can't delegate the decisions yet.
- Be honest about the cost: in this world you will work **more**, not less, and it is tiring.
- The muscle analogy: it's a back muscle you never had to exercise before, and it turns out to be the most important one.

**His concrete system**

- **Triage into two buckets.** Big important things shipping *today* vs. everything else. **Pin** the important threads; let the rest rip and come back when you can.
- **Write the day's priorities down** on paper. On a normal day ~10 of the PRs are firefighting, which is exactly what pulls you off the things that matter.
- **Set a cadence.** He checks his high-stakes threads roughly **every 25 minutes** — enough to be responsive, spaced enough that he can mentally rest instead of clicking through threads all day and getting wiped out.

> 💡 **Tip — the mantra**
> "Slow is smooth, and smooth is fast."

**Throughput, in his own numbers**

- Average of roughly **22–25 PRs per day**, sometimes **40 in a day**.
- Most get merged; a few get closed.
- On the **18th** he climbed **Mount Washington** with his son and couldn't access his phone — but shipped about **8 PRs** that morning before the hike, while his son was still asleep.

> 🛠️ **Tool pattern — parent/child sessions**
> Use a premium model thread as the **manager**, and have it spin up children. His example: open a **Fable** thread, tell it "we want to accomplish these five things — spin up five child Devin sessions." The children run on a **cheaper model** (he names **Fusion**, described as a cheaper sidekick model to Fable's parent). Running a super-premium model for everything is not economically viable.

> 💬 **Speaker opinion — the meta-observation (from the host)**
> The host points out that Ryan's task system isn't very different from what a well-organized person did *before* AI — pinning priorities, writing things down. Obvious in hindsight, but overwhelming if nobody tells you the system. Ryan agrees: "It's back to the basics, just in an agent age."

---

## 5. Pillar 2 — Automations

**The general move:** take anything you'd normally handle in a recurring meeting or a daily manual check, and turn it into an automation. The starting prompt is literally that simple — open a session and say *"I want you to automate this task every X days."*

> 📏 **General rule — the big unlock**
> Set your agents up so that **they can make themselves better**, rather than you hand-building all the systems.

> 🛠️ **Devin playbooks**
> In Devin, a recurring automation is called a **playbook**. Ryan distinguishes it from a *skill*: a playbook is more a list of things to do and how to do them correctly.

### Automation A — End-to-end signup test (QA)

**Key points**

- The playbook is named **"end-to-end signup test."** It drives a browser through the real Untangle user experience: sign up → create a case → onboard a client → run the client through discovery.
- Runs **three times a week** (Monday / Wednesday / Friday) — the cadence is set by cost: roughly **$60 in tokens** per run, because browser testing is expensive.
- The purpose is **finding bugs that reached production** and slipped past the automated test suite. It is explicitly *not* a UX review.
- On failure, it **triggers a child triage session** to fix the problem.

**Why browser testing matters**

- It's now vital that your agent can properly drive a browser, and it should work out of the box.
- Part of why he chose Devin: Cognition has been running browser-capable cloud agents for **2 years**.
- The loop is genuinely agentic: it **records a video**, **annotates the video**, **watches its own video**, and **fixes bugs it sees**.

> ⚠️ **Caution — observability is the hard part**
> The automation is the easy half. The real questions are: how do you *know* it failed? Did the agent silently fail and self-fix? What happened to the PR it opened? Ryan's advice is to work this out *with* the agent — ask it "I understand it runs Mon/Wed/Fri and triggers a triage session on failure; how do I find out about it?" The answer chain (post to Slack → connect the **MCP** → which channel do I watch?) is the machinery you have to build.

### Automation B — Production watchdog

**Key points**

- Runs **daily at 9:00 a.m.**
- It walks every event in the database for **paid customers**, summarizes them into a **JSON file**, and surfaces that file in the admin panel.
- Each morning he opens the production watchdog and reads the summary of what customers actually did.
- The framing: it's a chief of staff showing up and saying "here's the important stuff that happened for our customers yesterday — what went well, and a couple of bugs we saw."
- Motivation: with lots of real law firms and real clients on Untangle, there's no way to track activity mentally by reading logs.

> 💡 **Tip — link out to the real UI**
> Pick your most important customers, and make sure each line of the report reads *"the customer did X — here's a link to view it,"* pointing at a production instance where you can see exactly what they did. Humans are extraordinarily good at spotting "that's weird" at a glance. Several times this has led him to click in and discover the UX an agent built wasn't what he assumed. He calls the linked version "a game changer."

### Automation C — The self-improvement loop

**Key points**

- Untangle has an agent named **Grace**, essentially a paralegal, who chats with attorney customers, paralegal customers, and those customers' own clients going through divorce.
- A **daily automation** reads those conversations and **grades them against a rubric** you define.
- Anything scoring below your threshold **kicks off a child session to fix it**, which produces a PR.
- Result: roughly **three of these fixes ship per day**.
- The value is in the paper cuts — small UX details he either didn't know about or wouldn't have bothered to prioritize. Because the agent already found it, opened the PR, and made it ready, he just ships it.

**How to build your own:** pick the most important part of your app that you want to self-improve, then tell the agent how to judge whether a given interaction was good or bad. That rubric is the whole design.

> ⚠️ **Caution — you still have to use your own product**
> "There's no substitute, and we probably won't have a substitute for a while, for you using your own app." Ryan still clicks through the entire app himself periodically, then spins up sessions to fix what he finds. Even the smartest models still lack the sense of *obvious* — the "why did you think that was okay?" judgment.

---

## 6. Cost, model routing, and choosing your stack

**Key points — the numbers**

- Last month he spent roughly **$20,000 in tokens**, which he calls "just too much — not viable."
- His estimate of where things will settle for real engineering work: about **$5,000 per month per employee**.
- Above that number, you need to figure out **model routing**.
- The cheap reinforcement loops run on **SWE-1.7** [?], a coding model fine-tuned by Cognition — far cheaper than frontier models like Opus 4.8 [?] or GPT-5.6 [?]. That puts those loop sessions around **$5 per session**.

> 💬 **Speaker opinion — spend the money**
> "If you're not willing to pay **$15 a day** to improve one of the core feature sets of your product — what are you doing? Either it's not a real company or you don't care." Spend it first; *then* engineer the token cost down.

**Key points — frontier lab vs. independent agent lab**

- Ryan's sharpest strategic claim: **don't build your engineering motion inside a frontier lab's stack.** If your whole workflow lives inside Claude Code or Codex, those vendors aren't incentivized to keep it economical for you long term — they're incentivized to lock you into their models and their process.
- Independent agent labs (**Amp**, **Devin**/Cognition, **Factory**, and Cursor with caveats) are incentivized to give you the best result at the lowest price, so they'll do the hard routing work: high-effort frontier model for one task, **SWE-1.7** for another, a check with **Fable** at the end.
- His analogy: an independent lab is like a **mortgage broker or a travel agent**, making a lot of calls to get you the best price.
- Frontier labs are currently **subsidizing tokens** heavily — at ~**$200/month** you get near-infinite tokens. He thinks that's unsustainable.
- **"Yes, and":** you're not abandoning frontier models by using an independent harness. You can still run their models inside these products.

> 💡 **Tip — where the subsidized plans are genuinely great**
> He still uses **Codex** and praises the Mac app. For a local helper agent that opens browser tabs, creates Google Docs, checks email, and does general information work, a subsidized $200/month plan is excellent value. Just don't build your company's software factory on it.

> 📏 **General rule — don't build your own software factory (yet)**
> If you're a one-person shop, a frontier-lab plan is fine. Once you have product-market fit, a real product, and you're starting to hire, you need a software factory — and at that point you want an independent agent lab. Building one yourself is what companies do when they get large enough (his example: **Ramp** launching **Inspect** [?], their in-house agent). Doing it early is "stupid"; the alternative is being locked in a walled garden.

---

## 7. Pillar 3 — The software factory, and building in public

### The software factory

> 📏 **General rule — the direction of travel**
> "The agents are going to be writing 100% of your code, reviewing 100% of your code, shipping 100% of your code. That's where we're going." The more you can get there, the better.

### Build a credible public reputation

**Key points**

- Ryan credits ~**20 years** of work on **X** with paying real dividends — including this podcast appearance, which came out of a relationship built there.
- Share what you're learning publicly. It doesn't have to be polished.
- The payoff isn't paid posting — it's the **network and relationships**. Doors open, and more of them than you'd expect. Not immediately, but eventually.
- Saying **"I don't know"** is a perfectly good posture — and then ask an agent to help you figure it out.

> 💡 **Tip — format matters**
> Write **articles** on X specifically; he notes the algorithm still rewards long-form articles. And: be on X regardless of how you feel about Elon.

> 💬 **Speaker opinion / worked example (from the host)**
> The host's original co-host **Sahil Bloom** worked in private equity and started writing about topics that interested him during COVID — finance topics, interesting individuals — in a Wikipedia-ish style optimized for Twitter. He wasn't claiming expertise; he was documenting what he was learning. Outcome: **1M+ followers**, a **New York Times bestselling book**, companies started on top of it, and a fund raised.

**Closing line:** "There is no try, there is only do," as Yoda says. *(Ryan's paraphrase of the original "Do, or do not. There is no try.")*

---

## 8. Quick reference: tools and numbers

### Tools mentioned

| Tool | Maker | What it's for here |
|---|---|---|
| **Devin** | Cognition | Primary cloud agent / software factory; playbooks; browser testing |
| **Codex** | OpenAI | Local/desktop agent work; praised Mac app |
| **Claude Code** | Anthropic | Named as the other frontier-lab harness |
| **Amp** | — | Independent agent lab |
| **Factory** | — | Independent agent lab |
| **Cursor** | — | Named as no longer independent (see appendix note) |
| **Fable** | — | Premium "parent" model used to orchestrate child sessions |
| **Fusion** [?] | — | Cheaper "sidekick" model used for the child sessions |
| **SWE-1.7** [?] | Cognition | Fine-tuned coding model powering cheap loops |
| **Slack** (+ **MCP**) | — | Notification surface for agent activity and automation alerts |
| **1Password** | — | Key custody; agents never hold prod write keys |
| **Wispr Flow** | — | Voice dictation, bound to a physical button |
| **Ugmonk Analog** | Ugmonk | Paper daily priority system |
| **Razer** vertical mouse | Razer | Wrist pain |
| **git worktrees** | — | The painful local alternative he's arguing against |
| **Inspect** [?] | Ramp | Example of an in-house software factory built at scale |

### Numbers cited

| Figure | Context |
|---|---|
| ~25 years | Ryan as founder/CEO; on his fourth company |
| ~110 | Full-time employees at Treehouse; taught 1M people to code |
| 1 | Current employees at Untangle |
| 4x | Projected Untangle revenue growth this month |
| 50%+ | Share of his work done on his phone |
| 52-inch | The Dell monitor |
| 8 | Panes tiled on screen at once |
| 5–10 | Cloud agents running simultaneously |
| 50x | Output increase required after hitting PMF |
| 2–3 → 10–20 | High-stakes decisions per day, before AI → before lunch now |
| 25 min | Interval for checking pinned high-stakes threads |
| 22–25 (up to 40) | PRs per day |
| 8 | PRs shipped the morning of the Mount Washington hike |
| 3x/week | End-to-end signup test cadence (Mon/Wed/Fri) |
| ~$60 | Token cost per end-to-end signup test run |
| 9:00 a.m. | Daily production watchdog run time |
| ~3/day | Fixes shipped from the self-improvement loop |
| ~$20,000 | Last month's total token spend |
| ~$5,000/mo | His estimate of sustainable token cost per engineer |
| ~$5 | Cost per cheap-model loop session |
| ~$15/day | The spend he argues is obviously worth it |
| $200/mo | Subsidized frontier-lab plan pricing |
| 3–6 months | How often this whole landscape changes |
| 2–2.5 years | Since Devin launched |

---

## Appendix: caption corrections and editorial notes

Corrections applied to the auto-generated captions. Entries marked **[?]** are uncertain and should be verified against the source before you rely on them.

| As heard in captions | Rendered as | Note |
|---|---|---|
| "Devon" / "Devon AI" | **Devin** | Cognition's agent |
| "codeex" / "codecs" | **Codex** | OpenAI's agent |
| "cloud code" | **Claude Code** | Where referring to Anthropic's tool. Note: "cloud agents" and "work in the cloud" are *not* corrections — those are genuinely about cloud VMs |
| "get work trees" | **git worktrees** | |
| "Razor" | **Razer** | Mouse brand |
| "Whisper Flow" | **Wispr Flow** | Voice dictation app |
| "UG Monk" | **Ugmonk** | Maker of the Analog paper to-do system |
| "one password" | **1Password** | |
| "parallegal" | **paralegal** | |
| "soloreneur" | **solopreneur** | |
| "52-in" | **52-inch** | |
| "AMP" | **Amp** | |
| "Sahel Bloom" | **Sahil Bloom** | Corrected on first mention; the host says it both ways |
| "the phrasing smooth is uh slow is smooth and smooth is fast" | **"Slow is smooth, and smooth is fast"** | Garbled delivery; reconstructed to the standard phrasing |
| "SUI 1.7" / "SWE 1.7" | **SWE-1.7** [?] | Spoken two ways. Normalized to the SWE-# naming Cognition uses for its coding models; the exact version number is uncertain |
| "Opus 48" | **Opus 4.8** [?] | Version number uncertain |
| "GPT56" | **GPT-5.6** [?] | Version number uncertain |
| "GPT56 soul on extra high" | **GPT-5.6 [?] on extra-high effort** | The word rendered as "soul" is unclear — possibly a model variant name. Left out rather than guessed |
| "Fusion" | **Fusion** [?] | Named as a cheaper sidekick model paired with Fable; name not verified |
| "Ramp launch, Inspect" | **Ramp launched Inspect** [?] | Product name not verified |
| "Untangle" | **Untangle** | Company name kept as spoken |
| "Grace" | **Grace** | Untangle's paralegal agent |

**Editorial notes (not corrections):**

- **"Cursor… sort of owned by Elon."** Preserved as spoken. This is the speaker's characterization of Cursor no longer being independent; it is not corroborated here and should be checked before being repeated.
- **Yoda quote.** Ryan says "there's no try, there's only do." The original line is "Do, or do not. There is no try." His paraphrase is preserved with a note rather than silently rewritten.
- **Host name.** The host is addressed only as "Greg" in the transcript; no surname is given, so none has been supplied.
- **"Fable" as a model name** is used repeatedly and consistently and has been left as spoken.
