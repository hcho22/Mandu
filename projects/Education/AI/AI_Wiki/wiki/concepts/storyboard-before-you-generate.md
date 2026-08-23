---
type: concept
tags: [agent-operations, creative, video, planning, marketing, control]
status: seed
source-count: 1
last-updated: 2026-08-21
---

# Storyboard Before You Generate

**For generative media, plan the structure first so the model executes a plan instead of improvising.**

From [[one-person-marketing-team]].
Asked for UGC-style video ads, Claude built a four-stage pipeline on its own rather than prompting a video model directly:

| Stage | Output | Why it exists |
|---|---|---|
| **Creators** | 4 consistent character images | A reusable brand avatar, so faces stay the same across ads |
| **Boards** | A storyboard per ad: selfie framing, cup and shaker, product open, close-up, drinking | The shot list the video must hit |
| **Video** | Generated from characters plus boards | Execution, now constrained |
| **QA** | Screenshot and review each clip | One clip rejected for a defective back panel |

The source's own phrasing for the middle step is the point: video generation is **controlled by a planned story** rather than improvised.

## Why the intermediate artifacts matter

A one-shot prompt to a video model gets you a sample from a distribution.
Ask twice and you get two unrelated people in two unrelated rooms.

Splitting the job into character, then board, then render turns a single lucky draw into a controlled composition, and it does two things at once:

- **Consistency across a set.** The character image is generated once and reused, which is why four ads can share a recurring avatar.
- **A reviewable checkpoint before the expensive step.** A storyboard is cheap and text-shaped; video is the most expensive thing in the run ([[make-the-agent-report-its-cost]]). Catching a wrong idea at the board stage costs nothing.

That second property is the general one.
**The stage worth inserting is the last cheap artifact before the expensive irreversible one.**

## Synthesis

This is [[phased-implementation]] and [[plan-code-validate]] applied to media instead of code, and the mapping is exact: the storyboard is the plan, the render is the build, the QA pass is the validation.
The wiki has a great deal of material on planning before an agent writes code and none, until now, on planning before an agent generates an image or a video, even though the cost asymmetry is far worse in media.

It is also the concrete answer to a question [[design-system-not-a-design]] raises without settling.
That page argues a *system* is a better agent deliverable than an *artifact*, because the system constrains everything downstream without further human input.
The character sheet is exactly that for video: not a design, but a reusable element that makes every subsequent render consistent by construction.
A brand avatar is a design system with a face.

The interesting detail is that **the agent invented this pipeline unprompted.**
It was asked for UGC ads and it produced a production process.
That belongs next to [[agent-over-engineering]], which warns that agents invent env tiers and audit trails nobody asked for and that cutting them is human work.
Here the invented scaffolding was correct and improved the output, which is the honest counterexample: the same tendency that produces waste in a codebase produces craft in a production pipeline.
The distinguishing question is probably whether the invented structure is *load-bearing for quality* or merely *load-bearing for completeness*.

Two limits.
The QA stage was self-review by the generating agent, which sits against [[self-referential-bias]] and is discussed on that page.
And the source's own verdict on the finished ads was that they are "still very ad-like" and visibly synthetic, so the pipeline delivered consistency and control, not persuasion.
His proposed fix is upstream of all of it: write and approve the scripts yourself, then feed approved scripts plus storyboards into generation.
That is [[slop-free-zones]] applied to creative work - draw the boundary at the words, automate everything after it.
