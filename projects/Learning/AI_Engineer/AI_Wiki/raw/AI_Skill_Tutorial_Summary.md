# Building an AI Skill from Scratch: 5 Steps + Advanced Tips

*Detailed summary of a YouTube tutorial (≈19 min). The presenter builds an "edit-post" skill live in Claude Code and shares five practices for making skills that check and improve their own output.*

---

## Overview

An AI **skill** is a folder of instructions that an AI tool (e.g., Claude Code or Codex) can trigger for a given task. In this tutorial the presenter builds, live, a skill called **edit-post** that edits long-form newsletter posts in his own voice, and walks through a five-step method: **(1)** create the skill from your best examples and personal context; **(2)** make the skill's description explicit about when it should trigger; **(3)** test it manually and add an **evals.md** with pass/fail checks so the AI loops until its own output passes; **(4)** add a **memory.md** so the skill improves from past conversations; and **(5)** build (or copy) a "skill editor" skill that audits all your skills for AI slop and bloat. He closes by stressing that skills get output only ~80–90% of the way there — the final 10–20% is human review and taste.

> **How to read this summary**
> - 🟢 **[General rule]** — advice the speaker presents as a how-it-works fact or best practice.
> - 🟠 **[Speaker's opinion]** — the speaker's personal view, preference, or unverified claim.
> - Obvious caption errors were corrected: "clock code" → Claude Code, "scale" → skill, "AI slot" → AI slop, "Whisper Flow" → Wispr Flow, "mali" → manually, "codeex" → Codex, "washdown YouTube" → "Watch on YouTube."

---

## Table of Contents

1. [What an AI Skill Is & the 5-Step Plan (0:00)](#1-what-an-ai-skill-is--the-5-step-plan-000)
2. [Step 1 — Create the Skill from Examples & Personal Context (1:56)](#2-step-1--create-the-skill-from-examples--personal-context-156)
3. [Step 2 — Edit the Description So the Skill Triggers Reliably (5:00)](#3-step-2--edit-the-description-so-the-skill-triggers-reliably-500)
4. [Step 3 — Build an Eval Loop So the AI Fixes Its Own Mistakes (5:59)](#4-step-3--build-an-eval-loop-so-the-ai-fixes-its-own-mistakes-559)
5. [Step 4 — Add memory.md So the Skill Improves Over Time (11:54)](#5-step-4--add-memorymd-so-the-skill-improves-over-time-1154)
6. [Step 5 — Build a Skill Editor to Improve All Your Skills (13:40)](#6-step-5--build-a-skill-editor-to-improve-all-your-skills-1340)
7. [Where Human Taste Still Plays a Role (17:44)](#7-where-human-taste-still-plays-a-role-1744)
8. [Quick Recap — The 5 Steps](#quick-recap--the-5-steps)

---

## 1. What an AI Skill Is & the 5-Step Plan (0:00)

**Key points**

- 🟢 **[General rule]** A skill is simply **a folder with instructions** that the AI can trigger for a given task; by the end it contains several files (SKILL.md, examples, evals.md, memory.md).
- The live demo: build an **edit-post** skill for editing draft newsletters and other long-form copy, working in an empty **Claude Code** window. The presenter pastes the five steps in up front and tells the AI to follow them but wait for instructions.
- 🟠 **[Speaker's opinion]** The speaker says he is "completely AI skill pilled" — encoding personal knowledge and taste into reusable skills saves him significant time every week, and he promises it can do the same for viewers.

> ✦ **Tips & actionable advice**
> - The five steps previewed: **1)** create with best examples + personal context; **2)** be explicit about when the skill triggers (the description); **3)** test manually and build an eval so it checks its own work; **4)** build a memory.md so it improves over time; **5)** use a skill that improves all your skills (removes AI slop, tightens wording).

---

## 2. Step 1 — Create the Skill from Examples & Personal Context (1:56)

**Key points**

- Preparation: the presenter made **three text files of example posts** from his newsletter — personal posts, tutorial posts, and product-breakdown posts.
- Kickoff prompt (his standard opener): paste the three example files and say, in effect, *"I want to create an edit-post skill that helps me edit a draft newsletter or any long-form post based on these examples. Review the examples and ask me any questions; aim for a skill that's around one page."*
- The AI extracts patterns from the examples (a "Dear subscribers" opener, the hook, voice, short paragraphs, one-liners) and asks clarifying questions. His answers: invoking the skill should **edit a draft**; for the three post types, **auto-detect, then confirm**.
- First draft of **SKILL.md** includes: a workflow (detect post type → list gaps → rewrite), the post types with links to the example files, a post skeleton, and voice rules.

> ✦ **Tips & actionable advice**
> - 🟢 **[General rule]** **Give as many examples and as much personal context as you can** when kicking off skill creation.
> - 🟢 **[General rule]** **Keep SKILL.md separate from your examples/personal context.** Benefit 1: the AI doesn't re-read every example each run — it detects the post type from your draft and loads only the relevant example file. Benefit 2: you can share the generic SKILL.md without exposing personal example posts.
> - 🟢 **[General rule]** **Provide at least a couple of different examples** — with only one, the AI overfits to it and won't produce the output you actually want.

---

## 3. Step 2 — Edit the Description So the Skill Triggers Reliably (5:00)

**Key points**

- 🟢 **[General rule]** How triggering works: when you ask a question in Claude Code, Codex, etc., the AI does **not** read the whole skill — it reads only the **name and description**, and decides from the description whether to load the full skill.
- Therefore the description must state explicitly when to use the skill. The generated one — "Use when Peter pastes a draft post or newsletter, or asks to edit, title, or punch up a long-form piece" — was judged good enough to leave as-is.
- You can always trigger the skill manually (e.g., **/edit-post**), but that takes extra work each time.

> ✦ **Tips & actionable advice**
> - 🟢 **[General rule]** **Audit the description section** of every skill; otherwise it will not trigger reliably.
> - 🟢 **[General rule]** Phrase it as an explicit "**Use when XYZ…**" statement.

---

## 4. Step 3 — Build an Eval Loop So the AI Fixes Its Own Mistakes (5:59)

**Key points**

- 🟠 **[Speaker's opinion]** The speaker says this step is what other skill tutorials don't cover — and where "the magic" of skills lies.
- Manual test first: he pastes a real draft post. The skill correctly auto-detects a **tutorial-style post**, lists gaps (sponsor block missing, no numbered preview up front), and produces an edited draft.
- An **eval** = asking the AI to check its own work. Two types: **score-based** (e.g., "rate this post out of 5 and justify") and **pass/fail checks**.
- 🟠 **[Speaker's opinion]** Score-based evals "aren't that good" — the AI can't really tell a 3/5 from a 4/5 or 5/5 and will make it up. Pass/fail checks are more straightforward and reliable.
- He asks for **up to 10 pass/fail checks documented in evals.md**, then adds a crucial instruction to SKILL.md: **run the evals in a separate agent** with a clean context window (so grading isn't biased by the editing context), and if any check fails, the original agent must keep editing until **all evals pass**.
- Live loop result: run 1 — 3 of 10 checks failed (hypotheticals, AI-slop phrases); run 2 — 2 failed; run 3 — 2 failed; run 4 — 1 failed; **after 5 loops everything passed** (em dashes and "this is X, not Y" slop removed).
- The run also exposed problems with the evals themselves — you must verify both that the evals work correctly and that they're doing their job.
- 🟠 **[Speaker's opinion]** Building this loop is "so much more powerful" than just building the skill and calling it a day — the AI iterates while you go get coffee or lunch — though you still must check the results at the end.

> ✦ **Tips & actionable advice**
> - When the skill edits a draft, instruct it to **bold any changes it makes** — otherwise it's hard to see what changed.
> - Eval categories he dictated: **Introduction** (catches attention; crisp first 2–3 sentences; tutorial intros must include a "Watch on YouTube" link); **Voice** (authentic; no AI slop — no em dashes, no filler words like "leverage" or "delve," no "this is not X, this is Y" pattern, no strings of very short sentences); **Substance** (practical insights readers can apply right away); **Tone** (helpful, genuine, authentic); **Call to action** (clear CTA at the end with a list of steps).
> - Loop architecture: **edit agent → separate grading agent runs evals.md → failures sent back to the edit agent → repeat until all pass**.

> ⚙ **Tools & specifics mentioned**
> - **Claude Code** — the environment used to build and run the skill (Codex named as an alternative).
> - **Wispr Flow** — the dictation app the presenter uses to dictate prompts (he says he loves it; linked in the video description).
> - Files created so far: **SKILL.md**, three example files, **evals.md**.

---

## 5. Step 4 — Add memory.md So the Skill Improves Over Time (11:54)

**Key points**

- Distinction: the **eval loop improves the output** of each run, while **memory.md improves the skill itself** based on your conversations.
- **memory.md** = a reverse-chronological list of summaries of past conversations had while using the skill (e.g., the key lesson captured here: keep the grading agent and the edit agent separate).
- The first version was too long, so he gave feedback: memory entries must **not overlap with evals.md**, and each day should be captured in **2–3 brief sentences** (more only if needed). A bloated memory file ends up confusing the AI.
- 🟠 **[Speaker's opinion]** Memory is **optional**. It's most useful for feedback that can't be turned into an easy pass/fail eval — e.g., something vague like "make the voice more authentic."

> ✦ **Tips & actionable advice**
> - Keep memory.md **concise** (2–3 sentences per day) and non-overlapping with evals.md.
> - Use memory for **vague, taste-level feedback**; use evals for anything checkable as pass/fail.

---

## 6. Step 5 — Build a Skill Editor to Improve All Your Skills (13:40)

**Key points**

- The last step is a **skill that builds/edits skills**. As a demo, he has the AI output (in chat, not as files) what a one-page "skill-builder" skill would look like — it mirrors the tutorial: target structure with context/examples kept separate from SKILL.md, plus evals and memory, following the five steps.
- 🟢 **[General rule]** Why you need one: the AI writes most of the skill text, and if you don't pay attention it inevitably accumulates copy and turns into AI slop.
- Two options: tell the AI to build a skill-fixing skill from your own past skill-building conversations, or copy the presenter's **skill editor** skill, which adds rules for preventing AI-slop words, keeping skills concise, and following **progressive disclosure**.
- Demo: running the skill editor on the freshly built edit-post skill found it "full of" em dashes and "not X, but Y" phrasing; it removed those and fixed formatting — mostly cosmetic fixes, suggesting the original skill was structurally sound.
- 🟠 **[Speaker's opinion]** He doesn't believe in super-long skills humans won't bother to read — "every skill needs to be reviewed by human eyes" to be good.
- 🟠 **[Speaker's opinion]** Plug: his handcrafted, "AI-slop-free" skills (skill editor, personal adviser, health coach, infographic designer, and more) are available to paid newsletter subscribers at **behindthecraft.com** (link in the video description).

> ✦ **Tips & actionable advice**
> - Run a skill editor **periodically to audit existing skills**, or tag it in whenever you build a new skill, to keep everything concise.

---

## 7. Where Human Taste Still Plays a Role (17:44)

**Key points**

- 🟠 **[Speaker's opinion]** Even following all five steps, a skill's output is only about **80–90% there**. The difference between AI slop and good work is spending the last **10–20%** reviewing and handcrafting the output with your own taste and judgment — the skill "still misses stuff."
- His real newsletter workflow: spend significant time up front on the first draft (often dictating ideas) → have the AI do the initial edit pass with the edit-post skill and these best practices → spend the final 10–20% reading it through and applying common sense before publishing.
- Closing call to action: look at your past week, find where your time goes, and **build skills to streamline that work** — including evals and memory so the skills improve by themselves over time. (Plus the usual like-and-subscribe ask.)

---

## Quick Recap — The 5 Steps

| Step | What to do |
|------|------------|
| **1. Create** | Build the skill with AI using your personal context and best-in-class examples of the output you want (at least a few; keep them in separate files from SKILL.md). |
| **2. Trigger** | Be explicit in the skill's description about when it should fire: "Use when XYZ." |
| **3. Evals** | Test manually a few times, give feedback, then have it build evals.md with up to ~10 pass/fail checks; run evals in a separate agent and loop edits until all pass. |
| **4. Memory** | Add memory.md (concise, 2–3 sentences per day, non-overlapping with evals) so the skill improves from your conversations. |
| **5. Skill editor** | Build or copy a skill that audits your skills — removing AI slop, tightening wording, enforcing progressive disclosure. |

**One-glance reference — tools & files**

- **Tools:** Claude Code (or Codex) — where skills are built and triggered · Wispr Flow — dictation app · behindthecraft.com — presenter's newsletter with his paid skill library.
- **Skill folder anatomy:** **SKILL.md** (workflow, post types, skeleton, voice rules, "use when" description) · **example files** (kept separate) · **evals.md** (pass/fail checks) · **memory.md** (lessons learned).
