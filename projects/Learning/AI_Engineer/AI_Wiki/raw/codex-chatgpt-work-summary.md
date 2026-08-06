# Running Your Life on Codex: Jason (OpenAI Codex Team) on Automations, Skills & Browser Use

**Source:** Interview with Jason, OpenAI Codex team (Developer Experience) — YouTube tutorial transcript

## Overview

This is a conversation between a host and Jason, a member of OpenAI's Codex team, about how he personally uses **Codex** and the new **ChatGPT Work** app to run large parts of his professional and personal life. Topics covered include: the difference between ChatGPT Work and Codex, model/effort-level selection, organizing long-running "pinned threads," building a "Chief of Staff" automation that reads Slack/email/Linear on a schedule, personal writing-voice skills, the difference between skills and plugins, browser/computer-use automation, and building a custom app (a drum-practice tool) using a goal/plan/worklog workflow. The conversation closes with reflections on team culture at OpenAI and where Codex is headed next.

---

## Table of Contents

1. [ChatGPT Work vs. Codex](#1-chatgpt-work-vs-codex)
2. [Choosing Models & Effort Levels](#2-choosing-models--effort-levels)
3. [Organizing Threads & Projects](#3-organizing-threads--projects)
4. [The Obsidian Vault as Central Memory](#4-the-obsidian-vault-as-central-memory)
5. [Building a "Chief of Staff" Automation](#5-building-a-chief-of-staff-automation)
6. [Getting Started: Your First Heartbeat Prompt](#6-getting-started-your-first-heartbeat-prompt)
7. [Personal Voice Skills (Write Me, Tweet Me, Email Me)](#7-personal-voice-skills-write-me-tweet-me-email-me)
8. [Managing Skill Bloat & Self-Improving Skills](#8-managing-skill-bloat--self-improving-skills)
9. [Skills vs. Plugins](#9-skills-vs-plugins)
10. [Browser Use & Computer Use](#10-browser-use--computer-use)
11. [Building an App from Scratch: The Drum Practice Tool](#11-building-an-app-from-scratch-the-drum-practice-tool)
12. [Goal / Plan / Worklog Workflow](#12-goal--plan--worklog-workflow)
13. [Philosophy: Taste, Iteration & the "Manager" Feeling](#13-philosophy-taste-iteration--the-manager-feeling)
14. [Team Culture at OpenAI](#14-team-culture-at-openai)
15. [What's Next for Codex](#15-whats-next-for-codex)
16. [Corrections / Transcription Notes](#16-corrections--transcription-notes)

---

## 1. ChatGPT Work vs. Codex

**Key points:**
- ChatGPT Work is essentially a different **view/UX** on top of the same Codex experience — not a fundamentally different product.
- Codex surfaces developer-centric details: git history, pull requests, code changes.
- Work hides those details for non-coding tasks (e.g., making slides) where seeing "20 lines of Python" isn't useful.
- Jason says he now does a lot of his own work inside **Work** because he doesn't review most of the code Codex writes for him.

> 💡 **Tip:** If your task is primarily coding-related and you want visibility into git/PRs, use **Codex**. If it's general productivity work (slides, docs, scheduling), use **ChatGPT Work** for a cleaner UX.

> 🗣️ **Speaker opinion:** "A lot of us don't review code anymore" — Jason and the host both note this as their personal practice, not a universal recommendation.

---

## 2. Choosing Models & Effort Levels

**Key points:**
- Referenced models: **GPT-5.6**, with variants **Terra** and **Luna** (per transcript — see correction note below), each with different effort levels.
- Jason's default: **Sole [likely "5.6"] Medium** effort for most day-to-day work (reading Slack, managing calendar, scheduling meetings) — these tasks don't need peak intelligence.
- For building prototype apps (e.g., his drum-learning app), he sets effort to **Extra High** or **Ultra** and lets Codex run for hours on a complex goal.

> 💡 **Tip:** Match effort level to task complexity — use **Medium** for routine admin/ops work, and **Extra High / Ultra** for long, complex build-out sessions.

> 🗣️ **Speaker opinion:** This is Jason's personal default; he frames it as "for the most part," not a hard rule.

---

## 3. Organizing Threads & Projects

**Key points:**
- Jason's Codex workspace is organized into **pinned threads**, each acting as a persistent workspace.
- Examples of his pinned threads: automations reading Reddit/Twitter/LinkedIn for feedback signals, "Chief of Staff" threads (daily/weekly), Dev Day planning, a "mission video" project, agents API work, personal drumming project, slide-making.
- He does **not** run hundreds of background threads — nearly everything is a small number of long-running pinned threads.
- **Compaction** is handled automatically so long-running threads don't lose previous context.
- For extra/overflow work, he spins up **sub-agents** rather than overloading the main thread — though he's "a little more cautious" about when to do this compared to fully automatic sub-agent spin-up available in **Ultra mode**.

> 🔧 **Tool/Feature:** Compaction (automatic context management for long-running pinned threads).

> 💡 **Tip:** Keep a small number of persistent, pinned threads as long-running "workspaces" rather than creating a new thread per task.

> 🗣️ **Speaker opinion:** Jason is personally more cautious about spinning up sub-agents than the automatic behavior Ultra mode allows.

---

## 4. The Obsidian Vault as Central Memory

**Key points:**
- Jason keeps almost all of his context in an **Obsidian** vault called **"Vault"** — described as basically his only "project."
- A second project, **"Animate Codex,"** is a side project for moving things around visually.
- Other code repos (a monorepo, demo projects) all originate from the vault; if something needs to go to GitHub or the cloud, he pulls from the vault as the source of truth.
- The vault is **just markdown files** — no database. Organized into directories for: projects, people, notes, daily notes, and preferences.
- He rarely opens Obsidian himself — it exists mainly to give his **agent** context. Occasionally useful for himself to see rendered images and cross-links.

> 🔧 **Tool:** Obsidian (used purely as a structured folder of markdown files, not for its UI/database features).

> 💡 **Tip:** Use a single, consistently structured markdown vault as your single source of truth/context for the agent, organized by category (projects / people / notes / daily notes / preferences).

> 🗣️ **Speaker opinion:** Obsidian's specific benefit (image rendering, cross-links) is something Jason finds "nice" occasionally — not essential to the workflow.

---

## 5. Building a "Chief of Staff" Automation

**Key points:**
- Jason has a **daily** and a **weekly** Chief of Staff automation built on **scheduled tasks**.
- Daily automation runs at **9:00 a.m., 1:00 p.m., and 5:00 p.m.**
- Each run:
  - Reads all Slack messages
  - Reads Twitter DMs (via **computer use**)
  - Reads unanswered emails
  - Reads his **Linear** board
  - If something on Linear needs cleanup (e.g., a status update), Codex updates it directly
- Gives him a consolidated view of what needs attention — e.g., surfaced an upcoming trip to **Brazil** he needed to arrange, and a package he needed to pick up.
- **Flight check-in automation:** If Codex finds a booking confirmation + reference number in email, it checks in for the flight and **texts the boarding pass** to his personal phone.
- Also monitors for meeting prep artifacts (e.g., a Linear ticket created ahead of a meeting) and calendar items — e.g., screenshotting a mentioned event (production happening in Toronto) and adding it to his calendar.

> 🔧 **Tools referenced:** Slack, Twitter DMs (via computer use), Email, Linear, Calendar, scheduled tasks.

> 💡 **Tip:** Set recurring scheduled automations (e.g., 3x/day) that read across all your communication surfaces and give you one consolidated "what needs my attention" briefing.

> ⚠️ **Caution:** Jason explicitly notes this level of automation "is not something that just comes for free" — it was built up incrementally over time through iteration and specific feedback.

---

## 6. Getting Started: Your First Heartbeat Prompt

**Key points:**
- For someone starting from scratch (just email, calendar, Slack), Jason recommends a simple initial prompt:

> **Example starter prompt (paraphrased from Jason):**
> "Turn this thread into a heartbeat. I want you to check my emails, my Slack, my Linear every [interval] — whenever it makes sense, e.g., 9 a.m., 1 p.m., 5 p.m. — and tell me what I need to prioritize."

- From there, iterate with specific feedback:
  - "Now I want you to make sure everything has a link."
  - "I want you to start using Linear."
  - Eventually Codex began **pre-drafting Slack responses and emails** rather than just flagging that a message arrived — it now provides a link to a pre-written draft ready for review/edit/send.
- Jason does **not** have Codex auto-send Slack messages in all cases — it depends on context. Example of when he does allow auto-send: "make a pull request, check the tests, once green, DM Andrew on Slack with the PR link and preview URL."
- For the heavier Chief of Staff thread (reading ~40 emails, ~100 Slack messages), he prefers to stay more "surgical" and not fully automate replies.

> 💡 **Tip:** Start with a simple "heartbeat" prompt, then layer on preferences incrementally through direct feedback rather than trying to specify everything upfront.

> ⚠️ **Caution:** Full auto-send of messages is not applied uniformly — reserve it for well-defined, lower-risk workflows (e.g., PR status updates) rather than broad inbox/Slack triage.

---

## 7. Personal Voice Skills (Write Me, Tweet Me, Email Me)

**Key points:**
- Jason built a **"write me" skill**: connects to Slack (via a Slack connector), reads a past week of his messages, and builds a skill that mimics his writing voice.
- Refined further with nuance: talk differently to **external users vs. team members**, and differently to an **executive vs. a coworker**.
- Additional personal skills in his repo:
  - **Tweet me** skill
  - **Email me** skill
  - A skill that turns voice transcripts into blog posts
  - A skill that turns videos of him into video essays
- These skills are **iteratively edited over time** as he gives feedback — not "solved" in one shot.

> 🔧 **Tools/Skills named:** write me skill, tweet me skill, email me skill, voice-transcript-to-blog-post skill, video-to-video-essay skill.

> 💡 **Tip:** Build a "voice" skill for each channel (email, Slack, Twitter) by pointing Codex at your own historical messages, then refine it by explicitly telling it how tone should shift by audience (external vs. internal, executive vs. peer).

---

## 8. Managing Skill Bloat & Self-Improving Skills

**Key points:**
- Jason periodically cleans up his skill library rather than letting it bloat indefinitely.
- All Codex sessions are stored in a database (session JSON) — he doesn't know exactly where, but he can ask Codex to analyze history directly:

> **Example prompt:** "Look at the past 400 sessions. Which skills were never used? Can you clean things up? Can you interview me and go through this process?"

- Example outcomes from this review: identifying rarely used data-analysis skills to delete (and reinstall later if needed); consolidating multiple overlapping Slack skills; considering merging "write me," "Slack-y me," and "email me" into one unified skill.
- Jason compares this to managing a new hire: "You have to tell them a lot of information and give them feedback, and they change over time... it's not the fact that I'm going to have a skill that just runs forever perfectly."
- He built a skill called **"self-improve"** (about 4 months prior to this recording) that reviews which skills are called most often, reads the sessions where they were invoked, and surfaces consistent feedback patterns.
- Example of a skill improving itself: a **"Slack honey"** skill (per transcript — see correction note) noticed a recurring pattern — Jason always asked Codex to reply back into Slack once a task requested via Slack was completed. Over time, Codex began doing this automatically without being asked each time.

> 🔧 **Tool/Skill named:** self-improve skill.

> 💡 **Tip:** Periodically ask Codex to audit your own skill usage history (e.g., "read the last 200 Slack messages / tweets / blog posts and tell me what's changed") to keep writing-voice skills current.

> 💡 **Tip:** When you find yourself giving the same follow-up correction repeatedly (e.g., "now post that back to Slack"), that's a signal to have the skill absorb that step permanently.

> 🗣️ **Speaker opinion:** Jason frames skill maintenance as ongoing and never "perfect" — an explicit personal philosophy, not a product guarantee.

---

## 9. Skills vs. Plugins

**Key points:**
- A **skill** is one component of a **plugin**.
- A **plugin** bundles: multiple skills, potentially multiple **MCP servers**, and other resources/scripts.
- Example: Jason's individual write skill + Slack-y skill + email skill could be bundled into a single plugin called **"Better Writing"** to share with a team.
- As of "last week" (relative to the interview), OpenAI opened up the ability for anyone to **submit their own plugins** to the **Codex plugin directory**.
  - Skill-only submissions are reviewed quickly.
  - Submissions including **MCP servers** go through a more thorough security audit process.

> 🔧 **Tool/Feature:** Codex plugin directory (public submission now open).

> 📏 **General rule:** Skill = one reusable capability/instruction set. Plugin = a packaged bundle of skills + MCP servers + scripts/resources, meant to be shared more broadly (e.g., with a team).

---

## 10. Browser Use & Computer Use

**Key points:**
- Jason's favorite Codex feature. Notable anecdote: while on a bike ride, a colleague asked him to re-export a video because subtitles were broken. Jason used **remote control from his phone to his MacBook**, texted Codex to use **computer use** to locate the video, identify the export tool, fix and re-export it, and post the result back to Slack — then set it to check the Slack thread every 30 minutes for feedback and iterate (V2, V3, V4). By the time he got home, the video had been approved and used as the launch video for **"Migrate to Codex."**
- **Browser inside Codex** supports OAuth/login and can use your **cookies**, so it can operate while logged into your accounts — giving it access to much more information than a logged-out session.
- Codex's in-app browser can control **multiple tabs simultaneously** — useful for research/comparison tasks.
- Example: for a shopping research task, instead of just producing a markdown summary, Jason asked Codex to research, form a recommendation, and **open every product in its own tab** — so when he returned, he could review all options side-by-side and manually check out on the one he agreed with.
- **Distinction between browser use and computer use:**
  - **Browser use** = operating within Codex's in-app browser for website-based tasks (logged in).
  - **Computer use** = controlling the application/settings level (used when something requires OS/app-level control rather than a website).
- Jason's own computer-use examples: an internal open-source program form that outputs to **Airtable**, where he still has to manually download a CSV — his automation opens the export, presses download, moves the file to another drive, and continues the pipeline. Also used for general **app testing**.
- Jason personally does not yet trust computer use enough to let it make purchases/checkouts on its own, though he notes other people already do this.

> 🔧 **Tools/Features:** In-app Codex browser (OAuth + cookie-based login), multi-tab control, computer use (OS/app-level automation), remote control (phone → MacBook).

> 💡 **Tip:** For research/comparison tasks, ask Codex to open each candidate result in its own browser tab rather than summarizing to a markdown file — it's faster to review visually.

> 💡 **Tip:** Use computer use for tasks with no good API path (e.g., manual CSV exports from tools like Airtable) by having Codex directly interact with the download/export UI.

> ⚠️ **Caution:** Jason personally does not let computer use complete purchases/checkouts autonomously yet — presented as his own risk tolerance, not a platform limitation.

---

## 11. Building an App from Scratch: The Drum Practice Tool

**Key points:**
- Context: Jason ordered a drum kit and wanted to learn **rudiments** (basic sticking patterns) via **call-and-response** practice (someone plays a beat, you copy it).
- He asked Codex to build an app with: a library of rudiments, adjustable tempo, and the ability to add new concepts as he learns them.
- The app evolved to allow: uploading **any YouTube video**, extracting the drum track, muting/removing the drums, and playing along — a custom, personalized learning tool.
- Jason is clear this was **not built in one shot** — approximately **one week of iterative work**, not a single long six-hour run, though long unattended runs are also part of his workflow.

> 🗣️ **Speaker opinion:** Jason explicitly pushes back on the idea that a single long autonomous run ("I ran a goal for six hours") is the main story — he stresses these tools grow through iteration over time.

---

## 12. Goal / Plan / Worklog Workflow

**Key points:**
- Before building, Jason has an extended conversation with Codex about the problem space (e.g., feeding in YouTube videos about drum practice, hand/foot coordination, etc.) to identify the core skills needed.
- From that conversation, Codex generates three artifacts, part of a skill library entry called **"ultra goal"**:
  1. **Goal MD file** — the success criteria. Example: "at some point I want you to be able to paste in a YouTube URL and actually extract the different parts of the drum set." Work continues until this is achieved.
  2. **Plan MD file** — implementation detail (e.g., "write this in React," "use these technologies," "read the documentation if you don't know how to use them").
  3. **Worklog** — a running log Jason reviews to understand what's happening/what's blocking (e.g., "getting stuck on this permissioning issue"), updated continuously since long threads use compaction and he won't read every message.

> 🔧 **Tool/Skill named:** "ultra goal" skill (generates goal/plan/worklog files).

> 💡 **Tip:** Don't write the goal file yourself — describe your desired outcome/success criteria to Codex in conversation and have **Codex** generate its own goal.md, since it tends to produce better-scoped goals than a human writing it directly.

> 💡 **Tip:** Keep the goal as an editable file — if scope expands, edit the goal file directly and the run will pick up the new scope without needing to restart.

- **Verification example:** Jason's actual goal.md for the drum app specified that Codex must use **computer use** to open the app itself, upload a specific test YouTube video (by video ID), and confirm the data comes back out correctly — i.e., goals should specify a **verifiable** success condition, not just a vague feature request.
- **On design/mockups:** Jason no longer generates mockup images before building (a step he says was more necessary in an earlier model generation — referred to in the transcript as "the 5.5 world"). With the current generation (referred to as "5.6"), front-end output quality is good enough without image-gen mockups, provided you specify tools like **Tailwind** and **Shadcn (shadcn/ui)**.

> 📏 **General rule (Jason's framing):** Goals should be built around a verifiable end-state ("open the app, upload X, confirm Y comes back"), not just a general feature description.

> 🗣️ **Speaker opinion:** The claim that mockup image generation is no longer necessary with the current model generation is Jason's personal experience/preference.

---

## 13. Philosophy: Taste, Iteration & the "Manager" Feeling

**Key points:**
- Question raised: now that "coding is solved," what should people actually learn? Jason's answer: **taste** — the ability to articulate what you don't like about something.
- Analogy: "if you want taste, you have to eat" — you develop the vocabulary to critique and improve outputs by exposing yourself to lots of outputs and practicing articulating what's wrong.
- His recommended approach for beginners (including those without an engineering background): have Codex build something first, then focus on **being specific about dissatisfaction** rather than needing to know the technical vocabulary upfront (e.g., Tailwind, video processing pipelines) before starting.
- Example of increasingly specific feedback: not just "make it better," but "I don't have keyboard shortcuts to change the tempo — add a keyboard shortcut system," or "I don't like that I can't switch between these two panels — why does it flicker so much?" (Codex explains: not eagerly loading the page — then fixes it.)
- Jason's core claim: **"The only job left is to understand what you don't like about something and put it into words and tell the AI."**
- On the "manager" feeling: the host raises that many people now feel like they're managing AI rather than doing hands-on craft. Jason says he does **not** personally relate to feeling like "a manager" — he frames his role instead as caring about outcomes and quality, not about hard work or hands-on code per se. Success for the drum app, in his view, is that he actually learns to play drums better and that others can use/share the tool.

> 🗣️ **Speaker opinion (explicitly philosophical, flagged by both speakers as such):** Jason's framing of "taste" as the core remaining skill, and his personal disagreement with the "manager" framing, are his individual perspectives — not stated as a general rule for everyone.

> 💡 **Tip:** When giving feedback to an AI coding agent, aim for specific, actionable critiques (what's wrong and ideally why) rather than vague instructions like "make it better."

---

## 14. Team Culture at OpenAI

**Key points:**
- Jason attributes the Codex/DX team's culture — caring deeply about the community and users — as coming "top down" from **Tibo** (team/product lead referenced in the conversation).
- Both speakers agree that direct, transparent engagement with the community (rather than corporate press-release-style communication) is valuable.

> 🗣️ **Speaker opinion:** This entire section is opinion/anecdote from Jason and the host about team culture and communication style — not a factual/product claim.

---

## 15. What's Next for Codex

**Key points:**
- Jason: Codex has so far been primarily a **desktop** experience; the team is moving more of that capability into the **ChatGPT Work** cloud experience.
- Some automations that previously ran in Codex can now run in **ChatGPT Work** directly in the cloud.
- Stated goal: work shouldn't have to stop when you close your laptop.
- **Live/voice calling feature** referenced as something discussed previously with the host — described as an upcoming direction ("voice of the future"), with continued investment in dictation.
- Jason's contact info: Twitter/X handle **@JXNLCO** (per transcript audio, see correction note); broader product updates via **OpenAI Devs**.

> 🔧 **Tools/Products referenced:** ChatGPT Work (cloud), Codex (desktop), dictation/voice features.

---

## 16. Corrections / Transcription Notes

The following items were unclear or likely mis-transcribed in the source captions. Flagged here rather than silently guessed:

| Transcript text | Likely correction / note |
|---|---|
| "GPT 5.6 so terra and luna" | Model/variant names are unclear from audio — likely refers to specific effort-level or model tier names, but exact spelling could not be confirmed. Flagged `[?]`. |
| "Sole medium" | Likely refers to a specific model name + "Medium" effort level; exact model name unclear from transcript. Flagged `[?]`. |
| "Kashiva staff" | Almost certainly "Chief of Staff" (used correctly elsewhere in transcript) — corrected throughout this document. |
| "Slack honey skill" | Unclear — possibly a specific skill name/nickname that didn't transcribe cleanly. Left as-is with `[?]` flag; treat literal name with caution. |
| "JXNLCO" (Twitter handle) | Transcribed phonetically from audio ("at JXNLCO") — spelling not independently verified. Flagged `[?]`. |
| "codeex" / "cudex" / "kodex" / "hodex" | All normalized to **Codex** throughout, per consistent correct usage elsewhere in the transcript. |
| "chatbtd" / "chatb" / "chatbt" | Normalized to **ChatGPT** / **ChatGPT Work** based on context. |
| "por requests" | Corrected to **pull requests**. |
| "appshot" | Corrected to **screenshot**. |
| "astudio.google.com" (sponsor segment) | Preserved as stated; likely shorthand for Google AI Studio's URL. |

**Note:** A sponsor segment for **Google AI Studio** (mid-transcript) was excluded from the thematic summary above as it is unrelated advertising content, not part of the Codex tutorial.
