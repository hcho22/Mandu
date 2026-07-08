# Building Your Own AI Operating System — Tutorial Summary

> **YouTube Tutorial · Detailed Summary**
> How the creator turned Claude Opus 4.8 — run through **Claude Code** rather than the web chat — into a single "second brain" / executive assistant that runs his businesses.

**Frameworks at a glance**

- **The 3 M's** — Mindset · Method · Machine
- **The 4 C's** — Context · Connections · Capabilities · Cadence

---

## Overview

This is a deliberately **mindset-heavy** walkthrough of how to build a personal **AI Operating System (AIOS)** — a place you do all your work first, instead of jumping between Chrome tabs and desktop apps. The creator's core claim is that the model isn't the differentiator (everyone has the same one); **your context is**. The talk is structured around two frameworks: the **Three M's** (Mindset, Method, Machine) for approach and the **Four C's** (Context, Connections, Capabilities, Cadence) for architecture. It also covers the "default shift" to Claude Code, token economy, file/folder organization, agent safety and permissions, building and evolving skills, and how to keep the system improving over time. Two free resources are offered: a **Skool community** with a ~3-hour AIOS course, and a **GitHub repo** you can clone to onboard your own system.

---

## Table of Contents

1. [What Is an AI Operating System?](#1-what-is-an-ai-operating-system) — *what it is & why Opus 4.8*
2. [The Default Shift](#2-the-default-shift) — *mindset*
3. [Context Is King](#3-context-is-king) — *mindset*
4. [The Four C's Framework](#4-the-four-cs-framework) — *architecture*
5. [Connections: Wiring It Up](#5-connections-wiring-it-up) — *method*
6. [The `/insights` Command](#6-the-insights-command) — *tooling*
7. [Organizing Your AIOS](#7-organizing-your-aios) — *most-requested topic*
8. [Permissions & Safety: The "Keys" Problem](#8-permissions--safety-the-keys-problem) — *risk*
9. [The Bike Method: Building Trust in Phases](#9-the-bike-method-building-trust-in-phases) — *mindset*
10. [Building Skills](#10-building-skills) — *method*
11. [Treat Your AIOS Like a Mentor](#11-treat-your-aios-like-a-mentor) — *mindset*
12. [Dashboards & Visualization](#12-dashboards--visualization) — *personal preference*
13. [Key Takeaways & Resources](#13-key-takeaways--resources)

---

### How to read the call-out boxes

| Marker | Meaning |
|---|---|
| 💡 **TIP** | Tip / actionable advice |
| 🛠️ **TOOLS** | Tools & proper nouns mentioned |
| 📏 **RULE** | General rule |
| 💬 **OPINION** | Speaker's personal opinion |
| ⚠️ **CAUTION** | Warning |

---

## 1. What Is an AI Operating System?

*What it is & why he tested Opus 4.8*

- His main project is called **"Herk 2"**. It began as an executive assistant / second brain, and he now treats it as his actual **operating system**.
- He works out of a tab in **VS Code** (running **Claude Code**) by default — reaching for it *before* Chrome or any desktop app. That "reach for it first" habit is the whole idea.
- The analogy: like Windows, macOS, or iOS, an AIOS is simply the layer through which you interact with all your systems and get work done.
- It has access to "basically everything": meeting transcripts, Skool posts, YouTube transcripts, LinkedIn posts, Slack threads, ClickUp threads, and email. He says it can recall business details faster than he can.

> 🛠️ **TOOLS — Tools & names mentioned**
> Claude Opus 4.8 / 4.7 / 4.6 · Claude Code · VS Code · Slack · ClickUp · email · Skool · YouTube · LinkedIn

> 💬 **OPINION — His "feel" of the models**
> He liked **Opus 4.6** more than **4.7** ("a feel thing"), and says **4.8 feels more like 4.6** — which he counts as a win. His critique of 4.7: it sometimes had "an attitude," sometimes lied, and sometimes spent too many tokens / went out of bounds of the request. He notes 4.8 brings a big improvement in honesty.

> 💡 **TIP — Pointer**
> He has a separate deep-dive video specifically on the Opus 4.8 launch (referenced in-video).

---

## 2. The Default Shift

*Mindset*

- An AIOS only pays off **if you actually use it** — otherwise there's no ROI.
- His old pattern: **Claude Chat** on the web for writing (YouTube outlines, LinkedIn posts, Skool posts), and **Claude Code** only for code (Python scripts, automations).
- The realization: Claude Code runs the *same underlying model* as Claude Chat — so use Claude Code even for non-code work (brainstorming, thinking, writing), because it accumulates context as you go.
- Moving everything into Claude Code let him shrink his tech stack (fewer Claude projects, fewer SaaS tools) — more efficient, potentially cheaper, and far less context-switching.

> 📏 **RULE — The default shift**
> For any task, try to do it **from Claude Code first**, without opening Chrome or other apps. Frame your day as "do X, Y, Z — all inside Claude Code." Once that becomes the default, the context compounds.

---

## 3. Context Is King

*Mindset*

- **"AI isn't king."** Everyone has the same models, so the model isn't your edge — your context is. (If the model were the edge, everyone's LinkedIn posts would go viral.)
- Mental model: the **model is the engine**; your **context is the fuel**. Good fuel → useful, non-generic output.
- **Treat tokens like money.**
- Models are **stateless**: a fresh Claude Code session loads global rules + `CLAUDE.md`, then any files / instructions / memories you've given it — otherwise it's a beginner every time.

> 💡 **TIP — The context self-test**
> Open your Claude Code project and ask: *"Based on what's going on in our business, what should I do next week?"*
> - **Bad answer** → you need better context and better "hands" to pull data from the right sources.
> - **Good answer** → a solid starting point (with always-room-to-improve).

> 💬 **OPINION — Advice / self-promotion**
> If this already feels over your head, **upskill on Claude Code basics first** before building a full AIOS. He points to his free Skool community and a ~3-hour AIOS course (built around the Four C's) — which he says is the largest AI automation community on Skool.

---

## 4. The Four C's Framework

*Architecture (plus the Three M's)*

Two frameworks anchor the talk: the **Three M's** — Mindset, Method, Machine — for approach, and the **Four C's** for the architecture of what you give the model access to.

- **Context** — it knows your business. *Test:* a fresh session can answer "What does this business do and who works here?"
- **Connections** — what it can actually *touch*: calendar, tasks, messages ("what did John send yesterday?"), team chat — versus you copy-pasting context in.
- **Capabilities** — *how you do work*: skills / instruction files (e.g., "when Nate writes a LinkedIn post, use this style, these analogies, this framework"). True capability = it understands how *you* work; these are usually **skills**.
- **Cadence** — turning all of the above into things that *happen automatically* (while your laptop is closed, without being asked).

> 📏 **RULE — Build in order**
> Each layer depends on the one before it: **Context → Connections → Capabilities → Cadence.** You can't get reliable cadence without capabilities, capabilities without connections, or connections without context.

---

## 5. Connections: Wiring It Up

*Method*

- His own connections include **ClickUp, all local files, Google Workspace, QuickBooks, YouTube, Fireflies**, and more.
- How to decide what to connect: do a **self-audit** — where do you actually go, week to week, to find things? List your desktop apps, paid software, and the Chrome bookmarks you click constantly.
- Connect things **one at a time** via API endpoints or MCP servers to build a strong "bank" of connections.

> 💡 **TIP — 7 categories to connect first**
> 1. Revenue figures
> 2. Customer data / customer communication
> 3. Calendar
> 4. Internal communication
> 5. Tasks / project management
> 6. Meetings
> 7. Knowledge
>
> Ask "where do I go to look for each of these?" and connect that source.

> 🛠️ **TOOLS — Tools & connection methods**
> ClickUp · Google Workspace · QuickBooks (+ QuickBooks API) · YouTube · Fireflies · Skool API · Stripe API · MCP servers · API endpoints

> 💡 **TIP — Start from zero**
> The free **GitHub repo** includes onboarding skills that interview you, help you connect sources, and audit you — useful if you're starting from scratch.

---

## 6. The `/insights` Command

*Tooling*

- Run `/insights` in Claude Code to generate a report analyzing your **local Claude Code sessions**; it outputs an **HTML file** you open in a browser.
- Default look-back is **30 days** (his showed only ~**12 days** because he recently got a new PC).
- The report surfaces: what's working, what's hindering you, quick wins to try, skills / ambitious workflows, where things go wrong, features to try, and new usage patterns.

> 💡 **TIP — Make it a habit**
> Don't read it once. **Re-run `/insights` every couple of weeks (or monthly)** to watch how your usage evolves and keep streamlining. You can also have Claude Code brainstorm with you on the findings and iterate.

---

## 7. Organizing Your AIOS

*His most-requested topic*

- **Don't stress — there's no single "right" way.** It's all just folders and files.
- Because it's plain files/folders: you're **tool-agnostic** (his repo has `agents`, `claude`, and `codex` folders, so he can drive the same OS with multiple coding agents), and the AI can crawl, search, and reorganize everything.
- He edits `CLAUDE.md` / `AGENTS.md` **almost every day** (adding knowledge or tightening it) and moves projects/files around **weekly** (new quarterly priorities, new projects, scrapped projects).
- His structure includes **decisions, audits, archives**, and **"other worlds"** — folders that are entire standalone Claude Code projects (e.g., scheduled automations, his YouTube OS, the book he's writing).
- Even projects living *outside* the main OS stay findable because he keeps documentation pointing to where each one lives.
- Example artifact: this very video ("Opus 4.8 operating system") — its outline, visual plan, and diagrams were built inside the OS, with diagrams drawn in **Excalidraw**.

> 📏 **RULE — The only real failure mode**
> The single thing that breaks an AIOS is **so much disorganized context that neither you nor the AI can find things**. As long as it's findable, the exact layout doesn't matter.

> 💡 **TIP — Kill the scavenger hunt**
> One source of truth ends the "where did I put that?" hunt. Example: he couldn't recall whether a doc was in Slack or ClickUp, asked the OS to find it, and it surfaced it in ~**10 seconds**. Give your system access to *touch everything* so it can find things.

> 💬 **OPINION**
> You don't have to copy how Nate (or any creator or friend) organizes things. However you want to work is fine — that flexibility is "the beauty of it."

---

## 8. Permissions & Safety: The "Keys" Problem

*Risk management*

- As you climb the **"AI systems pyramid"** — workflows → AI agents → teams of agents — autonomy and reach rise, and so do **risk and cost**.
- Think in terms of **"keys"**: the permission layer around your agents.
- Critical distinction: **instructions are not the same as capabilities.** Saying "never send emails" is different from not putting the send-email key on the key ring. If a send-email tool exists in the agent's harness, it *physically can* use it regardless of your instructions.

> ⚠️ **CAUTION — Real cautionary tale**
> An AI agent on his team sent **3 promotional emails to over 150,000 inboxes** that weren't supposed to go out — they had to apologize and take down the page. Nobody told it to send them; the agent *proactively* picked up a to-do/task and interpreted it as "make and send these emails."

> 📏 **RULE — Design for the worst case**
> **Assume that if an agent can read or do something, it will.** (Usually it won't — but assuming it will changes how you grant endpoints/MCP servers.) Don't rely on instructions for safety; **remove the capability/key entirely** for anything you can't afford the agent to do, and keep access tightly scoped.

> 💬 **OPINION — The human note**
> He wasn't mad at the team member involved — he framed the incident as a valuable learning experience for the whole team, himself included.

---

## 9. The Bike Method: Building Trust in Phases

*Mindset*

- Building skills/automations is like **teaching a kid to ride a bike**: you don't just hand over the bike and say "go."
- You walk alongside, hold the handle, keep a hand on their back, and correct their drift. Each run earns more trust; gradually you take your hands off, remove the training wheels, then let them ride down the street — but you *still watch* until it's "earned its spot."
- Lower barriers to entry (easy to build and ship same-day) should **not** create a false sense of security. Too much trust in something that isn't ready is dangerous.

> 📏 **RULE — Phase the trust**
> Grant autonomy in stages, and only after a skill has earned it. **Every time you run a skill it gets better — it's not a waste of time.**

---

## 10. Building Skills

*Method*

His `.claude` folder contains **agent memory, agents, plans, rules,** and **skills**. He has many skills; some he's promoted to **global** so they work in any directory, not just inside the Herk 2 project.

### Two ways to build a skill

- **Forward:** Look at your cadence — what you do every Monday / every day / many times a day. Tell Claude Code to use the **skill creator**; give it the end goal plus the tools and considerations you normally have in mind; build, correct, get output, give feedback, iterate. (A skill might take ~**50 tries** before you like it.)
- **Reverse-engineer (his more common method):** Do a task end-to-end with Claude Code, then say: *"This output is great — look back at our conversation. What did we do? What did you think about? What tools did you need? What questions did you ask me?"* and build a skill that reliably reproduces that output.

> 📏 **RULE — Evolve every use**
> Every time you use a skill, give it feedback and update it. (His LinkedIn-writing skill: after each post he tells it "this part was good, this wasn't — change it so it doesn't happen next time.")

> 💬 **OPINION — Clarification added on review**
> A skill **isn't only** a big workflow or SOP. It can be as simple as a prompt you keep retyping — turn that repeated prompt into a skill / slash command.

### Worked example — the `session-handoff` skill

> 🛠️ **TOOLS — Example skill + commands**
> He built a **session-handoff** skill (installed **globally**) for when he wants to clear context or move a session from Claude Code to **Codex** or a new terminal. It used to be a prompt he retyped many times a day.
>
> **What it outputs:** a full breakdown — what you did, files created, open decisions, what's next — plus "pick up here," deferred / open questions, where it started, decisions locked, and key files.
>
> **Workflow:** run the skill → `/copy` → `/clear` → paste into the fresh session to resume with clean context. He'll share this exact skill in his free Skool community.

> 💡 **TIP — Actionable starting point**
> List the things you do on a cadence and build skills for those first. **Reverse-engineering a finished piece of work is often the easiest way** to create a reliable skill.

---

## 11. Treat Your AIOS Like a Mentor

*Mindset*

- Think of the AIOS as a **mentor**, not just a chatbot or an automation.
- When you feel doubt ("I don't know how AI could do this"), your brain defaults to the comfortable, known **manual** process (e.g., pulling quarterly reports and running formulas by hand).
- Instead, ask the system: *"Here's a process I do at the end of every month, here's the tool I need — how can I actually do this?"* It will walk you through options, suggest ideas, and test things with you.
- There's a **short-term cost**: a new skill can be slower than your manual process at first — roughly a **20% dip** — but the long-term automation is far faster. The question is whether the dip is worth the long-term climb (versus staying flat by never changing).
- Your **judgment must stay in the loop**: you still read everything and add your own spin. You can't outsource everything.

> ❝ **"You can outsource your thinking, but you cannot outsource your understanding."**
> — a quote the speaker repeatedly returns to

---

## 12. Dashboards & Visualization

*Personal preference*

- He showed an **Obsidian** graph visualizing all his files, but admits he doesn't use it much for the Herk 2 project.
- You *can* run Claude Code from Obsidian's terminal; he keeps some Obsidian projects (YouTube transcripts, tools, breakdowns) where a visual view is genuinely nice.
- You do **not** need a fancy dashboard, agent uptime view, etc., to have an AIOS. He works by talking to different agents across tabs.
- He considered building a dashboard, but when he asked what he'd actually want to see, he found nothing important he couldn't already see or have Claude Code pull on demand.

> 💬 **OPINION — Clearly flagged as preference**
> This is personal preference — there's no right or wrong. If you're a visual person and want a dashboard, build one with Claude Code. He personally just doesn't see much value in it.

> 📏 **RULE — The North Star test**
> Judge every new feature or skill against your **North Star** (your ultimate monthly goal). If it doesn't move you closer, don't do it. His metrics: **free Skool members** and **monthly recurring revenue**. A pretty dashboard showing metrics doesn't necessarily *improve* the metrics — what matters is that the metrics exist and he can pull them instantly.

> 💡 **TIP — What productivity means**
> Productivity is **not** "how many hours did I work today." It's "**did I move the needle closer to my goal?**" That reframe is how to stop drowning in AI tools and context-switching.

---

## 13. Key Takeaways & Resources

- **Two frameworks:** the Three M's (Mindset, Method, Machine) and the Four C's (Context → Connections → Capabilities → Cadence, built in that order).
- **Default shift:** do everything in Claude Code so context compounds.
- **Context is king**; tokens are money; models are stateless.
- **Organize** as plain files/folders, keep it findable, stay tool-agnostic.
- **Safety:** remove capabilities (don't rely on instructions); phase trust via the bike method.
- **Skills:** build forward or by reverse-engineering; evolve them every use; even a repeated prompt deserves a skill.
- **Mindset:** treat it as a mentor, protect your own understanding, and measure against your North Star.

> 🛠️ **TOOLS — Free resources offered**
> **Skool community** — free; includes a ~3-hour course on building your AIOS around the Four C's; described as the largest AI automation community on Skool.
>
> **GitHub repo** — free; clone it to onboard your own AIOS, with onboarding skills that interview, connect, and audit you. (Also shared inside the Skool community.)

---

### A note on transcription cleanup

Obvious auto-caption errors were corrected for accuracy — "cloud code/chat" → **Claude Code / Claude Chat**; "callmd / cloud.mmd / agents.mmd" → **`CLAUDE.md` / `AGENTS.md`**; "school" → **Skool** (the platform); "GBD 5.5" → **GPT-5.5**; "chat GBT" → **ChatGPT**; "codeex" → **Codex**; "Excal" → **Excalidraw**. Project and tool names that could not be verified from the captions — **"Herk 2"** and **"OpenClaw"** — are kept as heard; their exact spelling is uncertain.
