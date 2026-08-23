---
type: source
title: "Turning Claude into a One-Person Marketing Team"
source-type: tutorial-summary
author: "Nate Herk (AI automation creator)"
url: "local"
date-ingested: 2026-08-21
date-created: unknown
tags: [agent-operations, marketing, claude-code, context-engineering, creative, cost, brand, tutorial]
concepts: [three-ps-business-context, own-the-context-layer, agent-interviews-you-for-context, make-the-agent-report-its-cost, storyboard-before-you-generate, design-system-not-a-design, ai-slop, test-breadth-over-conviction, building-skills, context-is-king, marketing-agent]
---

# Turning Claude into a One-Person Marketing Team

A beginner-facing walkthrough of building a persistent marketing "team" inside [[claude-code]], connected to [[higgsfield]] (a multi-model image and video aggregator) through an MCP connector.
[[nate-herk]] uses a fictional brand, PerkForm (a canned protein coffee), to run the whole arc end to end: create the project folder, load business context and brand guidelines, connect Higgsfield, then generate a website, 18 ad creatives, a sizzle reel, 5 Instagram carousels, UGC video ads, and finally an Excel creative tracker.

**This is the wiki's weakest-evidence source on distribution and its most useful on cost.**
Set expectations accordingly.
There is no real brand, no real spend, no audience, and no performance data, so nothing here is evidence that any of the output works.
What it does supply, and what nothing else in the wiki has, is **itemized dollar cost for a full creative production run** and a clean statement of why you put an agent in front of a generation tool at all.

Read it as the amateur-tier companion to [[building-marketing-agents]], which is the same territory done by a practitioner with real clients and real data.

## Key claims

### The core argument: the tool is commodity, the context layer is not

You could use Higgsfield directly.
Routing everything through a Claude Code project instead buys three things the generation tool cannot supply:

| What the project adds | Effect |
|---|---|
| **Persistent business context** | The agent understands the business, avatar, and positioning on every request |
| **Reusable skills** | A carousel or a UGC ad is produced the same way every time |
| **Enforced brand guidelines** | Colors, logo system, and typography are followed automatically |

This is filed as [[own-the-context-layer]].
The source states the underlying mechanic plainly: Claude Code is not being used for coding here, it is being used **because it works out of directories and projects**, and that is what makes context compound across sessions.

### The Three Ps as minimum viable context

Before any tooling, state three things about the business: **Pain**, **Person**, **Promise**.
Everything downstream - website copy, ad angles, carousel hooks, UGC scripts - is derived from them.

The source's claim is that this is what stops output from reading as [[ai-slop]]: assets need purpose and intent behind them, and the intent comes from the Three Ps rather than from the model.
Filed as [[three-ps-business-context]].

### `grill me`: let the agent extract your context

A skill whose stated purpose is to relentlessly interview the user about a topic until shared understanding is reached, one question at a time, saving the interview as project context.
It is offered as the fix for "I do not know what context to give it": instead of writing a context dump, you let the agent pull it out of you.
Filed as [[agent-interviews-you-for-context]].

The source also makes the point that **skills are not only for generation** - intake and discovery are repeatable workflows too.

### Build the skill after you like the output

Rather than designing a skill up front, wait until a deliverable comes back right, then say "I loved carousel 2, make a skill around that style."
The negative form works too: "I do not like carousel 3, never make them like that again."
This is the reverse-engineering method already in [[building-skills]], stated at the level of a single artifact.

### The four-part prompt pattern, and cost reporting

Every generation prompt in the source states four things:

1. The **motivation** (why this exists).
2. The **end goal** (what the deliverable is).
3. **Where to save the output**.
4. **Report the cost at the end.**

Claude infers the rest from project context.
Asking for the cost on every single generation is what makes the later analytics tracker possible at all.
Filed as [[make-the-agent-report-its-cost]].

### The real cost numbers

The most transferable data in the source.

| Deliverable | Produced | Cost |
|---|---|---|
| BOGO ad creatives | 18 static ad images | **$3.43** |
| Instagram carousels | 5 carousels, roughly 7-8 slides each | **$9.56** |
| Sizzle reel | 1 vertical + 1 landscape, music and edits | **$17.55** |
| UGC video ads | 4 characters, storyboards, QA pass, videos | Highest of the four; **figure not stated** |

Static image generation is close to free at this volume.
Video is two orders of magnitude more expensive per deliverable.
The source's own framing on the sizzle reel is the honest one: $17.55 against hiring a video editor for the same output is not a close comparison.

Note the missing number.
The most expensive line item is the one the source never quotes, which is a real gap in a source whose main contribution is cost data.

### The UGC pipeline: storyboard before you generate

Claude built this pipeline itself, and it is the most structurally interesting thing in the source:

1. **Creators** - 4 consistent character images, reusable as a recurring brand avatar.
2. **Boards** - a storyboard per ad (selfie framing, cup and shaker, product open, close-up, drinking), so video generation executes a planned story rather than improvising.
3. **Video** - generated from characters plus boards.
4. **QA** - Claude screenshotted and reviewed its own videos, and **rejected one clip** with the note "back panel" before reporting the job finished.

Filed as [[storyboard-before-you-generate]].
The QA step is flagged against [[self-referential-bias]] below.

### The brand guidelines PDF became the design system

Claude read the brand guidelines PDF and reported pulling the design system **straight from the guidelines rather than inventing one**, then applied it everywhere without being asked again - including, unprompted and to the speaker's visible surprise, to the formatting of the Excel tracker.
Strong corroboration for [[design-system-not-a-design]].

On the website specifically, it also chose to **open on the pain, not the product** ("Your morning shouldn't require two drinks"), which is [[creative-is-the-targeting]] arrived at independently.

### Volume negates luck

More creatives means more chances to hit.
Once assets are live you have performance data, and data lets you iterate.
The proposed loop: connect Claude to real performance data, review weekly, make more of what worked.

**That loop was never built.**
The source stops at the tracker spreadsheet with an empty "angle performance" tab.
See the caveat under [[test-breadth-over-conviction]].

### Ask the agent what it sees

When the file panel rendered a dragged-in folder as an unreadable item, the speaker did not guess from the interface.
He asked Claude directly whether it could see all 11 product shots, and Claude returned a full inventory confirming them.
The defect was cosmetic.
Small point, good habit: **when the UI confuses you, the agent is a better inspector of your own filesystem than the UI is.**

### Separate the copy from the art

All 18 creatives were saved, including **blank versions with no copy**.
A future promotion swaps new copy onto existing graphics instead of regenerating images, or takes one winning line and applies it across all 18.
This is a cheap reuse discipline that makes the [[test-breadth-over-conviction]] variant count affordable.

### The honest critiques the speaker makes of his own output

Worth recording, because they are the most credible parts of the source:

- **The UGC ads are "still very ad-like."**
"You can kind of tell it's an AI avatar still... they're very salesy. You can tell it's not completely organic."
His proposed fix is to have Claude analyze real UGC first, or to write and approve the scripts himself before feeding them to video generation.
- **The sizzle reel got the logo wrong.**
- **Higgsfield is not the cheapest option** for any individual model; the argument for it is aggregation plus the Marketing Studio.
- **The website is not live.**
It ran on `localhost:8931`, which means it existed only on his machine.
- **Realistic expectations:** "You can't just expect to throw one prompt out there and then go viral."
What is demonstrated is how far you get *before* you apply research and taste, not a finished result.

## Contradictions and boundaries flagged

### This is not a [[marketing-agent]] by the wiki's own definition

The source calls it a "marketing team."
Against Cody Schneider's three requirements in [[marketing-agent]], it satisfies **none** of them:

| Requirement | Present here |
|---|---|
| Data clarity (unified cross-channel data) | No. One Excel file with an empty performance tab |
| Autonomous decision-making on a cadence | No. Every generation is human-triggered in a chat |
| Infrastructure (pipeline, warehouse, hosting) | No |

What it actually is, precisely, is a **context-rich creative studio**: a very good production tool with a human in the loop on every request.
That is a legitimate and useful thing, and the source oversells it by calling it a team.

The distinction matters because the wiki now holds both ends of the same spectrum.
[[building-marketing-agents]] is the loop with the data layer and no context layer described in detail.
This source is the context layer with no loop and no data layer.
Neither is complete, and **the interesting system is the union**, which no source in the wiki has yet documented.

### The self-QA pass sits against [[self-referential-bias]]

The wiki's position, backed four independent ways, is that a model grades its own output too leniently and the checker must not be the thing that did the work.
Here the same agent that generated the videos screenshotted and reviewed them, and **it did reject one**.

Recorded, not resolved.
The likely reconciliation is that the defect class was visual and objective (a garbled logo panel), which is closer to a [[functional-scorers|functional check]] than to a judgment call, and self-review plausibly survives on objectively checkable defects while still failing on quality.
A single anecdote from a source with no measurement is not evidence against four that have it.

## Connections

- [[own-the-context-layer]] - **the source's thesis**: the generation tool is commodity, the project holding your context is not.
- [[three-ps-business-context]] - Pain, Person, Promise as the minimum context that makes output specific.
- [[agent-interviews-you-for-context]] - the `grill me` pattern; elicitation as intake.
- [[make-the-agent-report-its-cost]] - a cost line on every generation, plus the four-part prompt pattern.
- [[storyboard-before-you-generate]] - plan the creative structure so generation executes a plan rather than improvising.
- [[design-system-not-a-design]] - second source; the guidelines PDF became the system and propagated unprompted.
- [[ai-slop]] - the Three Ps as the marketing-side anti-slop mechanism, and the speaker's own "still very ad-like" verdict on his best output.
- [[creative-is-the-targeting]] - "open on the pain, not the product," reached independently of Andromeda.
- [[test-breadth-over-conviction]] - "volume negates luck"; but volume without measurement, which is the caveat.
- [[building-skills]] - build the skill after you like an output; skills for intake, not only generation.
- [[context-is-king]] - second source for the `CLAUDE.md`-plus-context-files structure.
- [[marketing-agent]] - **boundary**: this is a studio, not an agent, by that page's own three requirements.
- [[self-referential-bias]] - **tension**: an agent self-QA pass that actually rejected its own output.
- [[unified-data-warehouse-for-agents]] - the creative tracker is the poor man's version, and it is empty.
- [[claude-code]] - seventh source; the first that uses it for no coding at all.
- [[higgsfield]] / [[nate-herk]] - the tool and the author.
- [[agent-operations]] - the area this source populates, under agents pointed at distribution.

## Source

- **Author:** Nate Herk, AI automation creator
- **Title:** Turning Claude into a One-Person Marketing Team (Claude Code + Higgsfield walkthrough)
- **Format:** Video tutorial, ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/claude-higgsfield-marketing-team.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-21

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix.
Items its author explicitly marks as unverified, and which are therefore not asserted as fact here: **GPT Image 2** (exact product naming uncertain), **scroll-world** (repo name and casing not confirmed) and its author's name, and a throwaway demo SaaS name.
"Soul" is noted there as probably Higgsfield's own image model rather than part of a compound name, and is treated that way above.

**No date is recorded on the source.**
An internal folder stamp reads `ugc ads 08-20` and the raw file was added to `raw/` on 2026-08-21, so the recording is very likely 2026-08-20, but that is inference and `date-created` is left `unknown`.

**Author identification is probable, not confirmed.**
See [[nate-herk]] for the open question of whether this is the same "Nate" as [[ai-operating-system-tutorial]].

**The brand is fictional and the numbers are production costs, not results.**
PerkForm does not exist, nothing was published, and no ad was ever served.
Every dollar figure is what it cost to *make* an asset.
Nothing in this source speaks to whether any of it would work.
