# Do You Still Read Your Code? Agentic Code Review Strategies

*Reference summary of a YouTube talk by John, senior staff software engineer at Meta*

| | |
|---|---|
| **Speaker** | John, senior staff software engineer at Meta (self-described). He runs an AI tech news and tutorials channel as a side hobby. |
| **Format** | Opinion and strategy talk with slides, plus a demo app: "AI or Not" [?], a swipe-to-vote web app for guessing whether something is AI-generated |
| **Organization** | Thematic, in the video's order, which follows the code's journey: plan → build → review → launch |
| **Title** | Descriptive. The video's actual title isn't in the transcript. |

---

## Overview

The AI-coding community is split between two camps. One says "if you still read your code, you're too slow." The other says "agents still make dumb mistakes, so review everything." John's answer is **it depends: code review is a gradient.** He treats the codebase like a tree. **Trunk** code (entry points, shared state, infrastructure) gets deep human review. **Leaf** code (isolated or feature-gated) gets a skim, as long as the agent supplies proof.

What makes reading less code safe is the system around the review:

- feature gates planned from day one
- agent-supplied evidence in every PR (tests, runtime logs, screenshots or video, confidence levels)
- static checks for nits
- a review agent with fresh context, playing the adversary
- gated launches with A/B tests or canaries

He also warns that **merge-ready isn't launch-ready.** The final ~20% (audits, refactoring, polish) takes as long as the first 80% and needs human taste.

**Key takeaways**

- Scale review depth to the **blast radius** of a change, not to a fixed policy.
- **Gate everything** from the start. Being able to roll back is what lets you review less.
- Make agents **prove** their work. Proof replaces line-by-line reading.
- Review AI code with an **agent that didn't write it**.
- Nits are dead. **Automate style** with type checking and linting.
- **Merge-ready ≠ launch-ready.** Budget human time for the last 20%.

---

## Callout Legend

| Callout | Meaning |
|---|---|
| 💡 **Tip** | Specific, actionable advice or a trick |
| 🔧 **Tool** | A named tool, command, product, or feature |
| 📏 **General Rule** | Presented as a broadly applicable principle or standard practice |
| 🗣️ **Speaker Opinion** | John's personal view, preference, or practice, explicitly framed as his own |
| ⚠️ **Caution** | A pitfall, risk, or warning |

`[?]` marks an uncertain caption restoration. See [Appendix A](#appendix-a-caption-corrections).

---

## Contents

- [Overview](#overview)
- [Callout Legend](#callout-legend)
1. [The Code Review Debate](#1-the-code-review-debate)
2. [Agents Across the Journey to Production](#2-agents-across-the-journey-to-production)
3. [The Codebase as a Tree](#3-the-codebase-as-a-tree)
4. [Feature Gating from Day One](#4-feature-gating-from-day-one)
5. [Demand Proof in Every PR](#5-demand-proof-in-every-pr)
6. [Leaf vs Trunk Code and the Safety Questions](#6-leaf-vs-trunk-code-and-the-safety-questions)
7. [Leave Nits to Static Checks](#7-leave-nits-to-static-checks)
8. [The Review-Depth Knob](#8-the-review-depth-knob)
9. [Using AI Agents to Review Code](#9-using-ai-agents-to-review-code)
10. [Merge-Ready Is Not Launch-Ready](#10-merge-ready-is-not-launch-ready)
11. [Launch with Experiments and Canaries](#11-launch-with-experiments-and-canaries)
12. [Closing: An Evolving Position](#12-closing-an-evolving-position)
- [Quick Reference: Review-Depth Guide](#quick-reference-review-depth-guide)
- [Tools and References Mentioned](#tools-and-references-mentioned)
- [Appendix A: Caption Corrections](#appendix-a-caption-corrections)
- [Appendix B: Editorial Notes](#appendix-b-editorial-notes)

---

## 1. The Code Review Debate

**Key points**

- There are two camps:
  - **"Stop reading":** if you still review your code, you're not moving fast enough. Agents are probably already better reviewers than you.
  - **"Keep reading":** agents still make dumb mistakes. Unreviewed output is "AI slop," so slow down and review what you ship.
- Code volume has exploded. One person can spin up multiple agents and produce far more features and tests than before.
- It's now nearly impossible for one engineer to review even their *own* code, let alone everyone else's.
- John's position is **"it depends."** The right amount of review is a gradient, set by the code you're reviewing.

> 🗣️ **Speaker Opinion:** He calls the community "very split" on this topic. His own stance is "it depends," like "any good answer to any hard problem."

---

## 2. Agents Across the Journey to Production

**Key points**

- AI agents should be part of the code's whole path to production, not only the writing step: **Plan → Build → Review → Launch**.
- **Plan:** write the spec, make sure the feature is complete, and define evaluations and validation criteria *ahead of time*.
- **Build:** use **agentic validation**, so the AI can check and fix its own work and gets the code right more often.
- **Review:** the subject of the rest of the video.
- **Launch:** put the work behind a feature gate and run experiments on it.
- Together, the four stages answer *when* and *how much* to review.

> 📏 **General Rule:** Define validation criteria before building, so the agent (and you) have something objective to check against.

---

## 3. The Codebase as a Tree

**Key points**

- Think of the codebase as a tree. Some parts matter far more than others.
- **Trunk / root:**
  - main entry points, e.g. an `App.js` that wires in all the helpers
  - infrastructure code, such as image processing and networking
  - a bug here can affect the entire app
- **Leaf nodes:** isolated, one-off code with few or no dependents (more in [§6](#6-leaf-vs-trunk-code-and-the-safety-questions)).
- How hard you review should follow the **blast radius** of the change:
  - Core image-rendering infrastructure with many downstream dependencies: he reads it carefully.
  - A one-off leaf component: let agents check it with component or snapshot tests and visually verify the PR, as long as the PR includes proof.

> 📏 **General Rule:** Review effort ∝ blast radius. The more downstream dependencies a change has, the more human attention it deserves.

> 🗣️ **Speaker Opinion:** Matching your effort to how important the code is "really matters a lot." Plan for it from the very beginning; don't leave it to review time.

---

## 4. Feature Gating from Day One

**Key points**

- **Feature gating** means adding branching logic so a feature can be turned on or off. It's also called *feature toggling*.
- Doing it properly takes real infrastructure, but you can start with a simple **Boolean flag** in your code.
- When planning a new feature:
  - Think in broad strokes and **gate everything**.
  - **Separate leaf nodes** (code that doesn't touch the existing codebase) from **integration** work.
  - Plan the integration pieces carefully, and **gate the integration layers** specifically.
- Start coding only once you have a solid plan, a roadmap and gating in place. Then use agents to make **atomic changes**.

> 🔧 **Tool:** **LaunchDarkly**, a popular feature-toggling / feature-gating platform.

> 💡 **Tip:** Don't wait for flagging infrastructure. A plain Boolean flag is enough to start gating features today.

> 💡 **Tip:** Gating pays off most at the integration seams, so give them their own gates.

---

## 5. Demand Proof in Every PR

**Key points**

- For rock-solid PRs, push agents to **give you proof**. The types of proof:
  - **Unit tests:** skim the test names and asserts to quickly judge whether the logic is well covered.
  - **Runtime evidence:** runtime logs, which give the agent (and you) more visibility. He covers this in his *agentic engineering* video.
  - **Visual evidence:** screenshots or video of the UI change.
  - **Confidence levels:** he asks agents to state how confident they are in the code, the gating, and each part of the change.
- Build these proof requirements into your skills so every PR includes them.
- **UI proof demo:** for a "save card" feature in the demo app, the agent's screenshot shows the save button and the saved state. Seeing that proof made him "a lot more believing" of the code.
- Proof lets you move faster because you don't have to check behavior by hand. **Agentic validation is the core concept that lets you read less code.**

> 💡 **Tip:** After every AI change, ask for a video or UI screenshot as visual proof.

> 💡 **Tip:** Ask the agent to report a confidence level for each part of the change. Low confidence tells you where to look.

> 💡 **Tip:** Be careful when agents write tests, because they can write useless ones. Make your own skill "around not writing useless tests," so the tests stay meaningful as proof. He calls this "a little side tip."

> 🗣️ **Speaker Opinion:** "In my opinion," solid diffs come from agents supplying proof. The more proof there is up front on the PR, the less code you need to read.

---

## 6. Leaf vs Trunk Code and the Safety Questions

**Key points**

- **Leaf code** is written in isolation or fully gated off behind a feature gate. Examples, and how to validate them:
  - One-off components → component tests or snapshot tests
  - New infrastructure or logic, or a new endpoint you're integrating with → unit tests or integration tests
- **How he handles leaf code:** he spends much less time on it, mostly skimming to make sure nothing is obviously wrong.
- **Trunk example, a reducer:** reducers hold a lot of shared state.
  - Say you change existing behavior in a game action (the "advance cards" action [?]), for example to add a new card type.
  - If that change isn't gated, it changes production, with trickle-down effects and side effects.
  - He spends much more time reviewing a change like that.
- **Anchor on safety** by asking three questions:
  1. What is the **control experience** that should not change?
  2. If this change went wrong, **how bad could it be**?
  3. **Can I roll it back?** That depends on feature gating.
- If you can answer these, especially the last one, you can spend much less time on each change.

> 📏 **General Rule:** Leaf code that isn't wired into the main production codebase can move fast. Validate it with component, snapshot, unit, or integration tests.

> 💡 **Tip:** Run the three safety questions before you review. If the answer to "can I roll it back?" is a confident yes, you can skim.

> 🗣️ **Speaker Opinion:** "In my opinion, everything should be anchored on safety."

---

## 7. Leave Nits to Static Checks

**Key points**

- Nits and style preferences aren't that important anymore. Hand them to **static checking**: type checking and linting.
- Agents are very good at this kind of work. In the demo, a **Codex** reviewer flags lint issues and suggests style changes.
- Code is more fluid now. Refactors happen more often and are easier, especially when validation covers the code being refactored.

> 🔧 **Tool:** Type checkers, linters, and an AI reviewer such as **Codex** can handle style and lint comments automatically.

> 🗣️ **Speaker Opinion:** The old days of nit-picking ("this is my favorite way of writing code") are "kind of dead." Nits "don't really belong in the conversation of code reviews anymore."

---

## 8. The Review-Depth Knob

**Key points**

- Does he still read code? **Yes, "a lot."** He thinks he reads *more* code than before.
- He turns a mental knob for each change:
  - **Turn it up** if it's a core/trunk change, if it's infrastructure, or if it has many dependencies.
  - **Then ask:** Is it safe? Is it gated? If something goes wrong, what happens?
- The more dangerous the change, the more time he spends on it. That's especially true for a **one-way door**, a change that's hard or impossible to reverse.

> 💡 **Tip:** Before deciding how deeply to read a change, tag it twice: trunk or leaf, and reversible or one-way door.

> 🗣️ **Speaker Opinion:** "I still read a lot of code. I think I read more code than I did before." The knob is his own process ("I first ask myself…"), not an industry standard.

---

## 9. Using AI Agents to Review Code

> 🗣️ **Speaker Opinion:** AI is already "really good" at reviewing code, and "better than most humans." The problem is that a lot of people use it wrong.

### Use a Good Review Skill

- **Claude Code** and **Codex** both have strong built-in review tools. In his view, the default reviewers are good enough.

> 🔧 **Tool:** **Claude Code**: the `/code-review` [?] slash command. **Codex**: its built-in review agent, shown on screen.

### Review with an Adversarial Agent

- Use a new sub-agent, or a separate agent, that **doesn't have the context used to create the code**. He calls this an **adversarial review agent**.

> ⚠️ **Caution:** "The agents will cheat." An agent reviewing code it helped write leans on the earlier conversation and context, so its review is biased.

### Standardize PRs with a Template

- Give the agent a PR/diff template to work from. Your PRs then look and feel the same and always include the important parts.
- Without guidance, agents write a giant paragraph, "like a story."
- He offers his own template ("you could use my template if you want"), but it isn't in the transcript.

> ⚠️ **Caution:** His "biggest pet peeve" is a PR whose summary and test plan are longer than the code change itself. "Don't be that guy."

### Run Codex as a Reviewer on GitHub

- Everything above happens while the code is being generated. **Codex** also has a GitHub integration:
  - A Codex reviewer can run automatically whenever a PR is opened.
  - You can also call it on demand by tagging Codex on a PR, likely with an `@codex` mention [?].
- The integration shows up as the **ChatGPT Codex Connector** [?].
- He believes it uses a separate model trained specifically for reviewing, though he hedges ("I think").
- It costs money.

> 🔧 **Tool:** Codex GitHub integration (**ChatGPT Codex Connector** [?]): automatic AI review when a PR opens or when Codex is mentioned.

### Babysit PRs Automatically

- **Problem:** AI reviewers on GitHub leave comments. You fix them and resubmit, then more comments arrive, and the back-and-forth drags on.
- **Fix:** use **"goals"** [?] to babysit the PR. His example prompt:
  > "For this PR, can you babysit it every hour, check it every hour and make sure that you address any changes requests from the Codex agent."
- Every hour, the agent:
  - checks the PR
  - fixes any issues
  - re-runs local and agentic validations
  - updates the PR notes and resubmits

> 💡 **Tip:** Build this hourly babysitting loop into your own skill, so the review back-and-forth gets handled without you.

### Recap: The Review Toolkit

- Use an adversarial agent with fresh context.
- Use good review skills. The defaults are fine.
- Use a PR template, and have the agent add validation proof.
- Anchor on safety and gating.

---

## 10. Merge-Ready Is Not Launch-Ready

**Key points**

- If you work this way (deep reads on trunk code, skims on leaf code), "done" at the end of a coding session really means **about 80% done**.
- **"Broad strokes"** is his name for that first phase: getting everything gated and landed.
- The **last ~20%** makes the feature launch-ready, and it's where most of his human effort goes:
  - refactoring and cleaning up the codebase
  - running a group of agents to **audit all the code written** before launch, at a high level, for **performance, bugs, security**, and whether the feature **works to spec**
  - polishing details such as animations
- The last 20% takes **as long as the first 80%**, and it's the most important part.

> 🗣️ **Speaker Opinion:** "Even if it's merge ready, I don't think it's launch ready." The final 20% still needs "human taste." You can move fast at the start, but you still have to look at the work yourself.

> 💡 **Tip:** Before launch, run several agents to audit the whole feature for performance, bugs, security, and whether it matches the spec.

---

## 11. Launch with Experiments and Canaries

**Key points**

- When you're ready to launch, run **experiments** to confirm the code actually works.
- With a small user base you won't have the statistical power for a real A/B test. He still recommends **A/B tests** or **canary deployments**.
- Sending a trickle of traffic to the new feature through its gate surfaces bugs, crashes and fired alerts quickly. That's the point.
- **Why it matters:** when agents write the code, you physically can't read all of it in detail anymore.
- Aim for an "**agentic safeguard**," an "agentic garden" [?]: lots of tests, lots of validation, and agents checking the work. Keep the ability to **take back bad decisions with gating**.

> 📏 **General Rule:** Rolling a feature out gradually behind its gate (as a canary) surfaces bugs, crashes, and alerts early, before everyone sees the feature.

> ⚠️ **Caution:** A small user group can't support a statistically valid A/B test. Treat the rollout as a safety check, not a measurement, but still do it.

---

## 12. Closing: An Evolving Position

**Key points**

- His final answer: **yes, review code, but it depends. It's a gradient.**
- As models improve you'll probably review less, so lean on **agentic validation**:
  - Agents supply proof: video recordings, logs, screenshots.
  - You gate the change and gradually trust agents more.
  - If you can take things back with gating, it's safe to go.
- His view keeps changing. Today he's comfortable skimming some code, guided by the tree concept.
- **Last tip:** the better you understand your codebase, the easier review gets. You can quickly spot what touches the dangerous zones and what's a simple leaf node.

> 🗣️ **Speaker Opinion:** "Maybe after another few generations of the model, I might say, you know what? You don't need to read any of the code. So who knows?" For now, he thinks you still need to read some code and form a fine-tuned opinion of it.

> 💡 **Tip:** Learn your codebase's architecture. Knowing which parts are trunk and which are leaf is what makes fast, risk-based review possible.

---

## Quick Reference: Review-Depth Guide

*Synthesized from §3, §6 and §8. This is not a slide from the video.*

| | 🍃 Leaf code | 🌳 Trunk code |
|---|---|---|
| **What it is** | Isolated, or fully gated; not wired into main production code | Entry points, shared state, infrastructure, many dependents |
| **Examples from the video** | One-off UI component; new endpoint; new logic behind a gate | `App.js`; image processing / rendering; networking; a reducer with shared state |
| **How to validate** | Component and snapshot tests, unit and integration tests, visual proof in the PR | Proof in the PR **plus** careful human reading |
| **Human review** | Skim for anything obviously wrong | Read deeply, especially if it's ungated or a one-way door |
| **Safety net** | Feature gate | Feature gate, gated integration layers, and a canary or A/B rollout |

**Pre-review triage checklist**

- [ ] Is this a trunk change: core, infrastructure, or many dependencies?
- [ ] Is it gated? Can I roll it back?
- [ ] What control experience must not change?
- [ ] How bad is it if this goes wrong? Is it a one-way door?
- [ ] Does the PR include proof: tests, runtime logs, screenshots or video, confidence levels?
- [ ] Has a fresh-context (adversarial) agent reviewed it?

---

## Tools and References Mentioned

| Name | Type | Context in the video |
|---|---|---|
| **Claude Code** (`/code-review` [?]) | AI coding agent / review command | Built-in review; one of the recommended review tools |
| **Codex** (OpenAI) | AI coding agent | Built-in review agent; lint/style reviewer in the demo; GitHub PR reviewer |
| **ChatGPT Codex Connector** [?] | GitHub integration | Runs Codex reviews when a PR opens or Codex is mentioned |
| **"Goals"** [?] | Agent feature (name uncertain) | Hourly PR babysitting |
| **GitHub** | Code hosting | Where the Codex reviewer comments on PRs |
| **LaunchDarkly** | Feature-flag platform | Feature toggling / gating |
| Boolean flag | Technique | The simplest possible feature gate |
| Type checking, linting | Static checks | Replace human nit comments |
| Unit, integration, component, snapshot tests | Testing | Proof; validating leaf code |
| A/B tests, canary deployments | Launch techniques | Gradual, gated rollout |
| "AI or Not" demo app [?] | The speaker's demo | Swipe-to-vote web app used for the examples |
| *Agentic engineering* video | Related video, same channel | Agentic validation, runtime evidence |
| *Codex and Claude Code* video | Related video, same channel | Suggested follow-up |

---

## Appendix A: Caption Corrections

| # | Caption (as transcribed) | Rendered as | Confidence | Note |
|---|---|---|---|---|
| 1 | "one person can split up multiple agents" | "spin up multiple agents" | Likely | Fits the context: one person running many agents |
| 2 | "validation criterias" | "validation criteria" | Certain | Grammar |
| 3 | "a lot safe to land" | "a lot safer to land" | Certain | Grammar |
| 4 | "game action advanced cards" | the "advance cards" game action [?] | Uncertain | A reducer action shown on screen; the exact identifier isn't recoverable |
| 5 | "More of that changes a one-way door" | "If that change is a one-way door" | Likely | Makes sense of the sentence |
| 6 | "Claude Code and Codex have really good built reviews" | "built-in reviews" | Likely | Missing word |
| 7 | "for Claude Code, it's slash code review" | `/code-review` [?] | Uncertain | The command name as spoken. The exact name may depend on your Claude Code version and installed plugins, so check `/help`. |
| 8 | "an agent that doesn't have the context of the code that it was used to create the code" | "…doesn't have the context that was used to create the code" | Likely | The sentence is about keeping context separate |
| 9 | "or you could also like just add Codex here like that" | tagging Codex on the PR, likely `@codex` [?] | Uncertain | The action is shown on screen, not described |
| 10 | "essentially it's this chat to be the Codex connector" | "ChatGPT Codex Connector" [?] | Uncertain | Probably the name of Codex's GitHub integration |
| 11 | "use goals … to babysit a PR" | kept as "goals" [?] | Uncertain | Could be a product feature name, or a mis-caption, e.g. for a looping/scheduling command such as Claude Code's `/loop`. The behavior described is a recurring hourly check. |
| 12 | "an agentic safeguard, like an agentic garden" | kept as "agentic garden" [?] | Uncertain | Could be "agentic guard" or "guardrail" |
| 13 | "AI or Not" | kept [?] | Uncertain | Could be the demo app's name or just a description of it |

---

## Appendix B: Editorial Notes

- **Structure.** This is an opinion and strategy talk with slides, not a step-by-step tutorial, so the summary is organized by theme. It keeps the speaker's order, which roughly follows plan → build → review → launch.
- **Title.** The title is descriptive. The video's actual title isn't in the transcript.
- **Speaker.** He's identified only as "John." No surname is given.
- **Opinion vs. rule classification:**
  - 🗣️ **Speaker Opinion** is used where John explicitly marks a view ("in my opinion," "I think," "my pet peeve") or describes his own practice ("I spend a lot less time…").
  - 📏 **General Rule** is used for principles he presents as broadly applicable that also match standard engineering practice: review depth by blast radius, defining validation criteria up front, gradual rollout behind gates.
  - "Anchor on safety" appears twice. In §6 he explicitly frames it as opinion ("in my opinion, everything should be anchored on safety"), so it's classified 🗣️ throughout and isn't repeated as a 📏 rule in §11.
  - "The agents will cheat" is stated as fact, but it comes from his experience. It's classified ⚠️ **Caution** with direct attribution, not 📏.
  - The warning about PR summaries longer than the code is his self-described pet peeve. Because it's delivered as actionable advice, it's a ⚠️ **Caution** with attribution.
- **On-screen content.** Several examples were shown on screen: the unit tests, the save-card screenshot, the reducer, Codex's lint comments, and the GitHub integration. The summary describes only what's narrated.
- **Not in the transcript:** his PR template and links to the videos he references.
- **Omitted:** the channel intro, the subscribe request, and filler.
- **Added context:** "OpenAI" as Codex's vendor. The Quick Reference table and checklist are syntheses of what he says, not content from the video.
