# Running a One-Person Company with AI Agents

*How a solo founder uses Open Claw, Devin, and Codex to do the work of ten people*

**Tutorial Summary · Featuring Ryan Carson (Untangled) · Interview / walkthrough format**

---

## Overview

This walkthrough explains how a solo founder runs an entire startup — engineering, marketing, sales, and operations — using AI agents instead of employees. The central thesis: **agents are just "cron jobs and markdown files."** If you set up a good recurring schedule (cron) and a good instruction file (skill), an agent can do a lot. The catch, stated repeatedly, is that the setup is genuinely hard and fiddly, and the real shift for founders is that you now invest heavily in systems, documentation, and processes up front — the opposite of old MVP advice.

**How to read the callout boxes:**

- 🟢 **TIP** — Tip / trick / actionable advice
- 🔵 **TOOL** — Tools & resources
- 🟠 **OPINION** — Personal opinion (the speaker's take/prediction, not a documented fact)
- 🟣 **RULE** — General rule / principle
- 🔴 **WATCH OUT** — Pitfall or caveat

---

## Table of Contents

1. [The Core Thesis: Agents Are Cron Jobs + Markdown Files](#1-the-core-thesis-agents-are-cron-jobs--markdown-files)
2. [Claw Chief: Turning Open Claw Into a Chief of Staff / EA](#2-claw-chief-turning-open-claw-into-a-chief-of-staff--ea)
3. [How the Open Claw Setup Is Managed (VS Code, SSH, Codex)](#3-how-the-open-claw-setup-is-managed)
4. [Cron Jobs & Skills: The EA Sweep and the DRY Principle](#4-cron-jobs--skills-the-ea-sweep-and-dry)
5. [Slack as the Control Surface](#5-slack-as-the-control-surface)
6. [Treating the Agent Like a Real Employee](#6-treating-the-agent-like-a-real-employee)
7. [The Prospecting / Cold Outreach Machine](#7-the-prospecting--cold-outreach-machine)
8. [Bugs, Pitfalls & the Limits of Out-of-the-Box Tooling](#8-bugs-pitfalls--limits-of-out-of-the-box-tooling)
9. [The Engineering Stack: Devin & Cloud Development](#9-the-engineering-stack-devin--cloud-development)
10. [Shipping a Feature End-to-End](#10-shipping-a-feature-end-to-end)
11. [Marketing, Ads & Content Automation](#11-marketing-ads--content-automation)
12. [Brand & Design Consistency with AI Image Models](#12-brand--design-consistency-with-ai-image-models)
13. [The Big Takeaway: Build the Machine First](#13-the-big-takeaway-build-the-machine-first)

---

## 1. The Core Thesis: Agents Are Cron Jobs + Markdown Files

The recurring mantra of the entire video: the most important thing to understand about agents is that **they are cron jobs and markdown files**. If an agent has a good cron (a deterministic, repeatable schedule) and a good skill (a markdown instruction file), it can accomplish a great deal. The speaker says he is shipping **at least 10 PRs a day, sometimes a lot more**.

A second framing theme: onboarding and training agents is far easier than humans. Agents retain all their training, can be continuously improved, and never leave taking their training with them.

> 🟣 **RULE** — An agent = a good cron (when it runs) + a good skill file (how it works). Nail those two things and the agent can do a lot.

> 🟠 **OPINION** — "It's almost easier to onboard and train agents than to train humans — a million times easier." He stresses he loves people and is a person himself, but agents are hundreds of times faster to onboard, retain all training, and can be improved over time. A human who leaves "exits with all the training," whereas an agent keeps it.

> 🔴 **WATCH OUT (stated repeatedly)** — Anyone claiming they're "waving a wand" and getting Open Claw to transform their life or business "is not being truthful to you." This stuff is still genuinely hard and fiddly to set up.

---

## 2. Claw Chief: Turning Open Claw Into a Chief of Staff / EA

The speaker, who has employed human executive assistants before, set out to turn his Open Claw instance — nicknamed **R2** — into an excellent executive assistant / chief of staff. He built and **open-sourced a system called Claw Chief**, which is essentially just a set of markdown files plus some cron jobs.

**What R2 does via Claw Chief:**

- Schedules meetings and parses booking links (e.g. clicks into a Calendly and books time).
- Every 15 minutes sweeps the inbox, calendar, and priorities, then pings him in Slack.
- Proactively follows up on emails — e.g. if a meeting-scheduling email got no reply, R2 pings that person.
- Does business development outreach: researches potential BD contacts daily, logs them in a spreadsheet, and reaches out as him to book meetings.

**Key files inside Claw Chief:**

- **priority map** — the single most important file. It lists the projects and people that are a priority so the agent can make good decisions. It is *long-term* (think quarterly for business priorities) and *super long-term* for the people who matter (family, friends, key business contacts). Not a weekly task list.
- **auto resolver** — instructions telling R2 how to resolve a question or task on its own when it can.
- **agents.md** — loads context and states that the main priority is the priority map.

> 🟢 **TIP** — To replicate this: grab the open-source Claw Chief repo, tell your Open Claw to look at it, and have it install itself. Then customize your priority map and auto resolver.

> 🔵 **TOOL** — **Open Claw** (the open-source agent platform being configured throughout) · **Claw Chief** (the speaker's open-sourced EA/chief-of-staff layer — markdown files + crons) · **R2** (his personal name for his Open Claw instance).

---

## 3. How the Open Claw Setup Is Managed

R2 physically lives on a **MacBook Pro in the speaker's closet**. He manages it remotely rather than touching the machine directly:

- He uses **VS Code** to work on R2, and also keeps **Codex, Claude Code, and Devin** open.
- He **SSHes into the MacBook over Tailscale** — described as "a perfect way to configure your Open Claw."
- He runs a **Codex plugin**, logged in with his **ChatGPT Pro subscription ($200/month)**, and configures R2 mostly by talking to Codex rather than editing config files or the Open Claw dashboard by hand.

**The self-inspection trick:** He keeps a **clone of the open-source Open Claw project** in his workspace so the agent can inspect its own source code. He'll tell Codex to pull the latest changes on the Open Claw repo, read the source, and figure out how to update itself to do something — or, if Open Claw has broken itself and can't self-repair, to diagnose why.

> 🟢 **TIP (explicitly called a "pro tip")** — Keep a clone of Open Claw's own source code in your workspace so the agent can read how it works and update or fix itself. Conceptually, this is "an agent that fixes Open Claw" sitting on top of Open Claw.

> 🟠 **OPINION** — Right now OpenAI is "really subsidizing tokens." For $200/month he estimates he gets "$2,000–$3,000 worth of tokens." His stance: "take the moment while it lasts" — he wants to be frugal with investor money. (The interviewer agrees.)

> 🟢 **TIP — why remote management matters** — Because the Mac is inaccessible (in a closet, and he was traveling in Japan), being able to SSH in via Codex and have the agent fix Open Claw is what keeps it running when it goes down. Both call this "very smart."

---

## 4. Cron Jobs & Skills: The EA Sweep and DRY

The main driver of R2 is a cron called the **executive assistant sweep**, which runs **every 15 minutes** and simply instructs the agent to "use the existing executive assistant skill." The speaker notes the cron message is intentionally minimal — he'd even shorten it further to just "use this skill."

**Crons vs. heartbeats:** In Open Claw, **heartbeats are not reliably time-triggered**. A heartbeat is closer to the agent saying "whenever I think about it, I should do this." A **cron is deterministic and repeatable** — runs every 15 minutes, guaranteed. He found crons to be the "bulletproof" way to do something on a schedule.

> 🟣 **RULE — DRY (Don't Repeat Yourself)** — Don't put a big instruction in the cron that's then repeated in the skill. The cron should be minimal ("use this skill"); all the detail lives once, in the skill file.

> 🟠 **OPINION / CAVEAT** — On heartbeats: "Maybe someone from the Open Claw team will correct me, or maybe that's gotten better, but I find crons are the bulletproof way." So this is his experience, not a documented guarantee.

> 🟢 **TIP** — Build a custom "heartbeat" out of a cron job (e.g. every 15 min) that points at a single skill, rather than relying on Open Claw's built-in heartbeat.

---

## 5. Slack as the Control Surface

R2's primary communication channel is **Slack**, set up as a **custom Slack app** (which required a manifest and was, in his words, "a pain in the ass" and "very fiddly"). He persists with it because he wants the setup to be as custom to him as possible.

A key Slack technique: instead of using direct messages, he created a dedicated channel (e.g. **"Ryan R2"**) so he can use **threads**. Each topic gets its own thread, keeping related thoughts contained.

> 🟢 **TIP** — Use a dedicated Slack *channel* (not DMs) for your agent so you can spin up a thread per topic. The speaker calls threading "important" and says he doesn't understand operating without it.

> 🟠 **OPINION (Slack vs. Telegram)** — The interviewer notes Telegram makes conversations hard to organize and even sends "random porn bot messages" you can't block — "not a very serious work environment." Both agree Slack is "great... very professional," largely because of threading.

> 🟢 **TIP — test your agent's security** — The interviewer admits he tried to "prompt inject R2." It held up well, giving only generic information and not leaking anything like credit cards. The speaker had even asked his sisters to try to hack his Open Claw. Implicit lesson: red-team your agent.

---

## 6. Treating the Agent Like a Real Employee

A repeated principle: treat your Open Claw the way you'd treat a real human employee. Concretely, R2 has:

- Its **own email address** on his domain.
- Its **own GitHub account**.
- **Read access** to his email and calendar (as you'd grant a human EA).
- **Write access to the calendar as itself** — never creating things as him.

**Example workflow:** when someone emails wanting to meet, he copies R2 and says "find us a time." R2 checks his calendars, proposes times, and books the meeting — with the invite coming **from R2** and him added as an attendee, exactly like a real assistant. (He notes this very call was scheduled this way.)

> 🟣 **RULE** — Give the agent its own real identity and real (scoped) permissions — its own email, its own GitHub, read access where an EA would have it, and write access "as itself," not impersonating you.

> 🔵 **TOOL** — **Agent Mail** (a YC startup giving an agent its own email address) · **Todoist** (he switched task storage from markdown files to Todoist — good API, free; R2 can read/write/update tasks) · **Google CLI** (the Gmail helper, "a little better" than the previous tool).

> 🟠 **OPINION / FORWARD LOOK** — He notes "Every" just launched a "+1" — Open Claw in the cloud, on demand, plug-and-play. He believes people will build **billion-dollar businesses** doing that and that everyone will want pluggable "digital employees." But he personally wants to stay "as close to the metal" as possible right now to deeply learn how Open Claw works inside a business.

---

## 7. The Prospecting / Cold Outreach Machine

A **prospecting skill** runs **once a day** and finds people for him to meet. He says it has already generated roughly **10 to 20 cold-outreach meetings in the last couple of weeks**.

For his company Untangled (a divorce/family-law product), the instruction is essentially "add verified Connecticut prospects to Untangled's outreach sheet." The agent finds family-law attorneys and mediators, locates their LinkedIn, logs them in a **Google Sheet used as the CRM**, drafts the email, and actually sends it — as him, from **ryancarson.com** (a ~25-year-old domain chosen for deliverability), using a service key for send access.

> 🔵 **TOOL** — **Firecrawl** (API, ~$20/month) for agent search and crawl (`Firecrawl scrape`), preferred over the **Brave API** that Open Claw nudges you toward · **Google Sheets** as the current CRM (Postgres may come later) · **LinkedIn** for finding/verifying prospects.

> 🟠 **OPINION** — On the Brave API: "I just don't think it's very good." Paying ~$20/month for Firecrawl is "really worth it" for a good agent search/crawl API.

> 🟣 **RULE** — Equip your agent with the right tools — a good search/crawl API is an example of augmenting the agent rather than accepting weak defaults.

---

## 8. Bugs, Pitfalls & Limits of Out-of-the-Box Tooling

**Avoiding duplicate outreach:** To stop the agent emailing the same prospect twice, the rule lives in the system: contacts are tracked in the spreadsheet, and the standing instruction is to always check whether you've emailed someone before. He says this hasn't happened once — but it works *because* you took the time to set up the system.

> 🟣 **RULE** — You must be "overly specific and pedantic" when specifying instructions — things you'd never need to tell a human (like "always check if you've emailed this person"). But you do it once, and then never again.

**The "fresh email instead of reply" bug:** R2 appeared to reply to emails by sending a brand-new email instead of replying in-thread. The cause: a markdown file instructed it to **CC his other account** (he has an Untangled account and a personal account). R2 *was* replying in the thread correctly, but the CC to his other address made it look like a new email arriving. The agent was doing exactly what it was told.

> 🔴 **WATCH OUT** — The agent will follow your instructions literally. Pay close attention to what your markdown files actually say — a stray "CC my other account" line caused a confusing, hard-to-diagnose bug.

**On building your own harness vs. using Open Claw:** He resists the temptation to ditch Open Claw and build a custom harness, because "then you end up maintaining it instead of working." He sticks with **out-of-the-box Open Claw plus custom skills and custom crons**, including **out-of-the-box memory** (tempted by alternatives but decided not to mess with it).

> 🟠 **OPINION** — Constantly switching between agents to optimize them "is not real work... You can make good YouTube videos off of it, but it's not real output." He hasn't even tried "Hermes" yet, on purpose.

> 🟣 **RULE (the customization line)** — Find the line between personalization/power tools and over-building: "buy a couple tools off the shelf, get a custom drill, but don't build a custom machine."

> 🟠 **OPINION — aside on planning** — He switched his **weekly** priority list to **paper** this week (crediting his wife's system), because he was bouncing too much between "today" and "this quarter" and lacked weekly visibility. The interviewer uses a whiteboard limited to three tasks. Both frame this as a focus aid, not an anti-AI stance. He also notes agents are inevitably "a little sycophantic," so weigh their agreement accordingly.

---

## 9. The Engineering Stack: Devin & Cloud Development

For engineering he uses **Devin**, and notably **does no local development**. Devin spins up a real, perfectly configured production **VM in the cloud** for each task, eliminating local headaches (wrong port, stale dependencies, Homebrew conflicts).

He acknowledges Devin "wasn't very good" 1–2 years ago but says it's "freaking amazing" now because "this always works." Setup takes about **an hour** to get dependencies installed and `npm run dev` working — after which it's reusable.

**Schedules + playbooks:** Devin **schedules** (the same cron-job idea) run automations against **playbooks**. Example: a **weekly full case coverage** automation that runs the entire user journey through his app — from sign-up to completing a divorce case — automatically once a week. A **playbook** is like a skill: it tells Devin how to perform the whole run-through. He also runs **smoke tests** that sign up, use a feature, record the screen, and report breakages.

> 🔵 **TOOL** — **Devin** (cloud-only engineering agent; reliable built-in browser testing) · **Schedules** (Devin automations = cron jobs with playbooks attached) · **Playbooks** (skill-like instruction docs for how to execute a process; the key is improving them over time).

> 🟠 **OPINION / PREDICTION** — "Most serious people are going to move to just use cloud engineering." He doesn't think it makes much sense to code on your local machine "very often, if ever." Devin's reliable, deterministic in-cloud browser testing is the feature that won him over.

> 🟣 **RULE** — The pattern — automations that run playbooks, with the playbooks continuously improved — is powerful "whether you use Devin or not."

---

## 10. Shipping a Feature End-to-End

His full workflow for a new Untangled feature:

- **Plan in Devin**, in a heavily customized environment (lots of agents.md files, knowledge, and skills). "Everybody has to start there."
- **Brain-dump by voice** using **WhisperFlow**: talk through everything he's thinking about the feature.
- **"Help me make a PRD"** — he has a skill that turns the dump into a PRD, mostly by getting the agent to **ask clarifying questions**. Then it writes the PRD as a markdown file.
- **"Build it"** — he works in **one thread** and lets the harness handle **auto-compaction** in the background; he no longer manually stops/restarts threads.
- **Walk away** for 10–20 minutes (or switch context). Devin's browser feedback loop screencasts the feature, often spots problems in its own PR, fixes them, and returns.
- **Land the PR** via a playbook called **land PR**, used 10–20 times a day.

**Process discipline as a solo founder:** He runs a full software-development lifecycle "designed for a very large team" even though he's solo, because agents, like humans, need reproducible processes that don't depend on him. **Everything is a PR.** He rarely reads code anymore — he reads PRs, and mostly reads the markdown and what the agent says about the change.

> 🟣 **RULE** — To get a "code factory" where agents write/review/ship close to 100% of the code, you need a real SDLC: **everything is a PR**, with reproducible processes that don't rely on you.

> 🟢 **TIP** — Create a `land PR` playbook that tells the agent exactly how to review, resolve, and merge a PR without you. Build features from a voice brain-dump → clarifying-question PRD skill → "build it."

> 🔵 **TOOL** — **WhisperFlow** (voice dictation to AI; also the episode sponsor) · **Codex (GPT-5.5)** (newly released, "really good in Codex"; good auto-compaction) · **Devin** (primary build/ship agent). He says he hasn't used **Claude Code** in a long time.

> 🟠 **OPINION** — "I think it's state of the art" (Devin). On build-vs-buy, he favors good off-the-shelf tools (Devin, Codex) over Claude Code *for his workflow* — an explicit personal preference, not a universal recommendation.

---

## 11. Marketing, Ads & Content Automation

He stresses that building features is now almost trivial; the hard part is **go-to-market: getting users and revenue**. Founders must do both product *and* marketing.

**Google Ads via CLI:** He had Devin build a **CLI for the Google Ads API**, with full **upsert capability** (insert, update, delete any campaign). He no longer uses the Google Ads UI at all — he just chats with Devin daily: "How's our campaign doing? How can we optimize it?" Setup was: talk to Devin, build the CLI, give it an API key, create an app.

> 🟠 **OPINION** — Google Ads is "so freaking complex" you used to need an agency. Agents handle that complexity well — and he's "probably not that good in the Google Ads UI" anyway.

**Content pipeline (a nightly "machine"):**

- Interview an expert; record/edit with **Descript**, chopping into **60-second segments**.
- Upload the MP4s to a **Google Drive** folder.
- A Devin **playbook runs every night**: checks the folder for MP4s, calls **Gemini** to watch each video and write a description, then has **OpenAI's image model** create a cover image, then Gemini writes the copy.
- Publishes everything to social via **Publer** (good publishing API).

> 🔵 **TOOL** — **Descript** (recording/editing, clip-chopping) · **Gemini** (watches videos, writes descriptions and copy) · **OpenAI image model ("Image 2")** (cover images — "Image 2" is the speaker's naming) · **Publer** (social publishing via API) · **Google Ads API + custom CLI** (managed entirely by chatting with Devin).

> 🟣 **RULE** — "You're trying to build the machine." Operate the marketing machine yourself first to learn it, then hire someone to run it later.

---

## 12. Brand & Design Consistency with AI Image Models

He gets consistent, on-brand imagery from prompts, but emphasizes there's a real **setup cost**. The approach mirrors his other systems: create a **design.md** plus a library of **reference images**.

He paid a human designer — **Brett from Design Joy, ~$6,000/month** — to do the initial branding and a library of social images. Now he feeds those as reference images alongside a strong design.md, and finds OpenAI's new image model can reproduce the brand "completely." He notes this is similar to how **Claude Design** works.

> 🟣 **RULE** — For brand consistency, build a `design.md` plus reference images, then let the image model generate against them — the same "instruction file + references" pattern used everywhere else.

> 🟠 **OPINION** — "It's important to pay a designer to do the first cut." We're in a world that "needs the taste and experience of a very good designer" for the initial brand/layout/social images — but after that, Claude Design plus OpenAI's image model can produce "unlimited, perfectly branded imagery." (The interviewer jokes this "just saved $6,000 a month.")

> 🔵 **TOOL** — **Design Joy** (designer subscription, ~$6k/month, for initial brand work) · **Claude Design** (used together with image generation) · **OpenAI image model** + `design.md` + reference images (the brand-reproduction stack).

---

## 13. The Big Takeaway: Build the Machine First

The closing synthesis: most of the work now is **setting up the system that does the work**. Taking the time to build the system means (1) you understand how the work actually happens and can refine it, and then (2) you either add more agents to augment it, or hire a human who is augmented with agents.

This inverts old startup advice. Founders used to "do the bare minimum to get the MVP out" and avoid systems, processes, and documentation. **Now it's the reverse:** invest heavily up front in your SDLC, documentation, and reference images, wire them into crons and skill files — and then you're "doing the work of 10 people." But "the setup is pretty brutal."

He notes he built Untangled's MVP in his free time before raising, so the product was largely done; now the focus is go-to-market. He has raised a **$2M seed round** and has money to hire, but plans **not to hire for a while** — wanting to understand and feel the pain of every job before hiring an "agent-augmented person" to fill it.

> 🟣 **RULE (the thesis, restated)** — Take the time to set up the system to do the work — you'll understand it, refine it, and only then augment with more agents or an agent-augmented human. Understand and do every job before you hire to fill it.

> 🟠 **OPINION** — Building features is "almost trivial now"; the real skill is go-to-market, adoption, and product-led growth. In his words, "almost everybody is a founder now — even if you're not." Companies used to bifurcate into product vs. marketing people; now you have to do it all.

> 🟢 **TIP — where to find the speaker** — He's "everywhere as Ryan Carson" — searching his name will find him.

---

*Summary generated from the provided tutorial transcript. Tool names, numbers, and proper nouns preserved as stated by the speaker; obvious caption misspellings corrected (e.g. "To Doist" → Todoist, "OpenClaw/Open Claw" normalized). Where the speaker offered a prediction or preference rather than a documented fact, it is flagged as a Personal Opinion. "Image 2," "GPT-5.5," and "Every +1" are reproduced as named by the speaker and may differ from official product names.*
