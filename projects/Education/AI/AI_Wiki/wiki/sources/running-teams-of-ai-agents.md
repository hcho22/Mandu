---
type: source
title: "Running Teams of AI Agents - Ryan Carson"
source-type: podcast
author: "Ryan Carson (founder/CEO, Untangle), interviewed by Greg"
url: "local"
date-ingested: 2026-08-01
date-created: unknown
tags: [agents, agent-operations, cloud-agents, automations, devin, cost, model-routing, solo-building, build-in-public]
concepts: [cloud-agents-over-local, manager-of-agents, independent-agent-lab-vs-frontier-lab, self-improving-agent-loop, production-watchdog, agents-as-cron-plus-markdown, credential-vaults, model-routing, build-in-public, agent-testing-instructions]
---

# Running Teams of AI Agents

A podcast interview with [[ryan-carson]], now founder/CEO of **Untangle**, an AI divorce agent for family-law firms.

This is the wiki's **second source on Ryan Carson**, after [[one-person-company-with-agents]], and it is a substantial update rather than a restatement.
The earlier source caught him running a one-person company on cron plus markdown files.
Here the same operator has hit product-market fit, is projecting **4x revenue this month**, is still the **only employee**, and has rebuilt his entire motion around **cloud agent fleets** - a position that directly contradicts the local-worktree workflows the wiki recorded from other builders.

He is explicit that the landscape changes every **3-6 months**, so the specific tools and prices are a snapshot, not a map.

## Key claims

### The reframe: you are a manager of agents

- Whatever your previous title (IC, people manager, founder, VC, parent, student), your new job is managing agents, and the target is not competence but being world-class at it.
- **Counterintuitively, managing agents makes you more technical, not less.**
To direct agents well you end up having to understand Postgres, production versus dev environments, migrations, and so on, and you learn all of it *by using the agents*.
Ryan says he is more technical now than at any point in his life.
- The right mental model is **engineering manager**, not "prompt user."
- "It is a farce that engineering is going away."
Anyone claiming engineers are disappearing or becoming less technical, he says, is not doing the work.
- **The carpenter analogy:** if robot carpenters existed, a real carpenter would manage them far better than a non-carpenter, because they know where the cut goes and where the nail goes.
Domain skill makes you a better manager of agents, not a redundant one.
- The way to learn it is to do it and get your reps in, not to read about it.

### Pillar 1: work in the cloud, not locally

- **Why local breaks down:** local development means running your own database, auth, and dev server on your Mac.
To do **two** things at once you need **git worktrees** (technical and hard to reason about) or a second copy of the repo.
Three, four, five, ten parallel efforts simply does not work.
The overhead is not just mechanical but mental - which worktree am I on, has this been synced, does this change collide with that one - and that overhead is what stops you shipping.
- **What cloud agents do instead:** a cloud harness spins up a **VM** per session on a button click, and you can create effectively **infinite** numbers of them with **zero risk of code collision**.
Ryan typically runs **at least 5 cloud agents at once, often 10**.
- **Why [[devin]] specifically:** it launched 2 to 2.5 years ago and did not work well then, because no matter how good the harness was, **the models were not good enough**.
By 2026 the models are good enough and a well-built cloud harness on top is genuinely good.
He is explicit that **the lessons are not Devin-specific**.
- **His strongly-stated opinion:** "If you are working locally, I honestly think you are a caveman."
He argues you are shipping **10x less** than you could be, and of the "local maxis" who mock cloud VMs: "They are not doing real work."
- **The one legitimate exception:** heavy new front-end work.
Spin up a local agent for light front-end and wireframing, then move it into the cloud as quickly as you can.
- **His forcing function** was reaching product-market fit: once real customers needed real fixes, he had to roughly **50x his output**, which is not achievable locally.

### The setup, and working from a phone

- One **52-inch Dell monitor**, replacing a multi-monitor rig, with **eight panes tiled at once**: Slack (the notification surface for what agents are doing, and essentially all he uses Slack for), 1Password, Devin, two panes for testing the app, X, and Codex for local work.
- **Never give agents production write keys.**
Production writes are dangerous and agents *will* do something bad.
Keep keys in 1Password and build the workflow so the agent **asks you** for the key when it needs to write to prod; you paste it into that session and both of you are explicit about what is happening.
- He does roughly **50% or more of his work from his iPhone**, because Devin runs in a mobile browser so he can check, review, or land a PR from anywhere.
His framing: agents are blocked waiting on your decisions, so waiting until you are back at your Mac makes no sense.
"The office is your phone."
- Ergonomics and input: a **Razer vertical mouse** after significant wrist pain, and almost all input through **Wispr Flow** voice dictation bound to a physical button.
- Alongside all of it he keeps a handwritten daily to-do list on the **Ugmonk Analog** system, which he calls "a little bit weird" but which is the mechanism that keeps the day's real priorities from being drowned out.

### Managing yourself: decision throughput is the bottleneck

- **Redefine what your work is.** Your job is now making high-stakes decisions almost all day.
- The old cadence was **2-3 high-stakes decisions per day**, communicated in a meeting, executed over two weeks.
The new cadence is **10-20 high-stakes decisions before lunch**.
- Agents are an infinitely scalable team that works very fast, and they will be **blocked by you**.
You cannot delegate the decisions yet.
- Be honest about the cost: in this world you will work **more**, not less, and it is tiring.
The muscle analogy - it is a back muscle you never had to exercise before, and it turns out to be the most important one.
- **His concrete system:** triage into two buckets (big things shipping *today* versus everything else) and **pin** the important threads; write the day's priorities on paper, because on a normal day ~10 of the PRs are firefighting and that is exactly what pulls you off what matters; check pinned high-stakes threads roughly **every 25 minutes**, spaced enough that he can mentally rest rather than clicking through threads all day.
- Mantra: "Slow is smooth, and smooth is fast."
- **Throughput:** roughly **22-25 PRs per day**, sometimes **40**.
On the day he climbed Mount Washington with his son he shipped about **8 PRs** that morning before the hike.
- **Parent/child sessions:** use a premium model thread as the **manager** and have it spin up children on a cheaper model.
His example is opening a **Fable** thread, saying "we want to accomplish these five things, spin up five child Devin sessions," with the children running on **Fusion**.
Running a super-premium model for everything is not economically viable.
- The host's meta-observation, which Ryan accepts: this task system is not very different from what a well-organized person did *before* AI - pin priorities, write things down.
"It's back to the basics, just in an agent age."

### Pillar 2: automations

- The general move is to take anything you would normally handle in a recurring meeting or a daily manual check and turn it into an automation.
The starting prompt is literally *"I want you to automate this task every X days."*
- **The big unlock:** set your agents up so that **they can make themselves better**, rather than you hand-building all the systems.
- In Devin a recurring automation is a **playbook**, which he distinguishes from a skill: a playbook is more a list of things to do and how to do them correctly.

**Automation A - end-to-end signup test.**
Drives a browser through the real Untangle experience (sign up, create a case, onboard a client, run the client through discovery), **three times a week**, with the cadence set by cost at roughly **$60 in tokens per run** because browser testing is expensive.
Its purpose is finding bugs that reached production and slipped past the automated suite; it is explicitly *not* a UX review.
On failure it **triggers a child triage session**.
The loop is genuinely agentic: it **records a video, annotates the video, watches its own video, and fixes bugs it sees**.

**Automation B - production watchdog.**
Runs **daily at 9:00 a.m.**, walks every event in the database for **paid customers**, summarizes them into a **JSON file**, and surfaces it in the admin panel.
The framing is a chief of staff saying "here's the important stuff that happened for our customers yesterday."
**Link out to the real UI:** make each line read "the customer did X, here's a link to view it," pointing at production.
Humans are extraordinarily good at spotting "that's weird" at a glance, and several times this has led him to click in and find the UX an agent built was not what he assumed.
He calls the linked version "a game changer."

**Automation C - the self-improvement loop.**
Untangle has an agent named **Grace**, essentially a paralegal, who chats with attorney and paralegal customers and their clients.
A **daily automation** reads those conversations and **grades them against a rubric** you define; anything below threshold **kicks off a child session to fix it**, producing a PR.
Roughly **three fixes ship per day**.
The value is in the paper cuts he either did not know about or would not have prioritized.
**How to build your own:** pick the most important part of your app, then tell the agent how to judge whether a given interaction was good or bad.
That rubric is the whole design.

- **Observability is the hard part, not the automation.**
How do you *know* it failed? Did the agent silently fail and self-fix? What happened to the PR it opened?
His advice is to work this out *with* the agent - ask it "how do I find out about it?" - and the answer chain (post to Slack, connect the MCP, which channel do I watch) is the machinery you have to build.
- **You still have to use your own product.**
"There's no substitute, and we probably won't have a substitute for a while, for you using your own app."
Even the smartest models still lack the sense of *obvious* - the "why did you think that was okay?" judgment.

### Cost, model routing, and choosing your stack

- Last month he spent roughly **$20,000 in tokens**, which he calls "just too much - not viable."
His estimate of where it settles for real engineering work is about **$5,000 per month per employee**; above that you need **model routing**.
- Cheap reinforcement loops run on **SWE-1.7**, a coding model fine-tuned by Cognition, far cheaper than frontier models, putting those loop sessions around **$5 per session**.
- "If you're not willing to pay **$15 a day** to improve one of the core feature sets of your product, what are you doing?"
Spend it first, *then* engineer the token cost down.
- **His sharpest strategic claim: don't build your engineering motion inside a frontier lab's stack.**
If your whole workflow lives inside [[claude-code]] or Codex, those vendors are not incentivized to keep it economical for you long term; they are incentivized to lock you into their models and their process.
- **Independent agent labs** (Amp, Devin/Cognition, Factory, and Cursor with caveats) are incentivized to give you the best result at the lowest price, so they do the hard routing work: a high-effort frontier model for one task, SWE-1.7 for another, a check with Fable at the end.
His analogy is a **mortgage broker or travel agent**, making a lot of calls to get you the best price.
- Frontier labs are currently **subsidizing tokens** heavily - at ~$200/month you get near-infinite tokens - and he thinks that is unsustainable.
- **"Yes, and":** you are not abandoning frontier models by using an independent harness; you can still run their models inside these products.
He still uses Codex and praises the Mac app, and says a subsidized $200/month plan is excellent value for a local helper agent.
Just don't build your company's software factory on it.
- **Don't build your own software factory yet.**
If you're a one-person shop a frontier-lab plan is fine.
Once you have PMF, a real product, and you're starting to hire, you want an independent agent lab.
Building one yourself is what companies do when they get large enough, and doing it early is "stupid."

### Pillar 3: the software factory and building in public

- "The agents are going to be writing 100% of your code, reviewing 100% of your code, shipping 100% of your code. That's where we're going."
- Ryan credits ~**20 years** on **X** with paying real dividends, including this podcast appearance.
Share what you're learning publicly; it doesn't have to be polished.
The payoff isn't paid posting, it's the **network and relationships** - not immediately, but eventually.
- Saying **"I don't know"** is a perfectly good posture, followed by asking an agent to help you figure it out.
- Write **articles** on X specifically; the algorithm still rewards long-form.
- The host's worked example: his original co-host **Sahil Bloom** started writing during COVID about topics that interested him, in a Wikipedia-ish style, not claiming expertise but documenting what he was learning.
Outcome: 1M+ followers, a New York Times bestselling book, companies, and a fund.

## Connections

- [[cloud-agents-over-local]] - the source's central and most contested claim; **flagged contradiction** against [[building-5-ai-products-solo]] and [[inside-conductor-workflow]].
- [[manager-of-agents]] - the role reframe, and the decision-throughput ceiling that comes with it.
- [[independent-agent-lab-vs-frontier-lab]] - the vendor-strategy claim; **the wiki's first counter-position** to its own Claude Code-centric bias.
- [[self-improving-agent-loop]] - rubric-graded production conversations that open their own fix PRs; the operational sibling of [[outcome-rubric-iteration]].
- [[production-watchdog]] - a daily agent-written digest of real customer activity, linked back to the live UI.
- [[agents-as-cron-plus-markdown]] - **second source, same author**; the pattern has matured from cron + markdown into cloud playbooks with triage children.
- [[agent-as-employee]] - Grace as a named production agent with a job description.
- [[credential-vaults]] - the never-give-agents-prod-write-keys rule, approached from key custody rather than context isolation.
- [[model-routing]] - second source; here it is a *vendor* argument as much as a cost argument.
- [[agent-testing-instructions]] - the end-to-end signup playbook is this concept run as a scheduled production job.
- [[agent-observability]] - "observability is the hard part, not the automation."
- [[get-out-of-the-loop]] - **tempered**: he automates aggressively but still clicks through the whole app himself.
- [[build-in-public]] - second source, with a concrete 20-year payoff account.
- [[build-the-machine-first]] - the same author's earlier principle, now at PMF scale.
- [[agent-operations]] - the area this source anchors.
- [[ryan-carson]], [[devin]], [[claude-code]], [[openai]] - entities.

## Source

- **Author:** Ryan Carson (founder/CEO, Untangle), interviewed by a host addressed only as "Greg"
- **Title:** Running Teams of AI Agents - Ryan Carson
- **Format:** Podcast interview, ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/running-teams-of-ai-agents-ryan-carson.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-01

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix.
Model and product names the appendix marks `[?]` as unverified: **SWE-1.7**, **Fusion**, **Opus 4.8**, **GPT-5.6**, and **Inspect** (Ramp's in-house agent).
The claim that **Cursor** is "sort of owned by Elon" is preserved as spoken in the raw file and is explicitly flagged there as uncorroborated; it is **not** repeated as fact above.

Note also a naming correction against the wiki's existing record: the earlier source [[one-person-company-with-agents]] recorded the company as "Untangled"; this source consistently gives **Untangle**, and the entity page has been corrected accordingly.
