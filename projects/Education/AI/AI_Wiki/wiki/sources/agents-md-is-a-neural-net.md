---
type: source
title: "Your AGENTS.md is a Neural Net"
source-type: blog
author: "Kun Chen"
url: "https://blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net"
date-ingested: 2026-08-27
date-created: 2026-08-22
tags: [agentic-engineering, agents-md, claude-md, context-engineering, self-improvement, skills, budget, first-mate, kun]
concepts: [agents-md-as-neural-net, two-level-agent-memory, four-bad-memory-states, skills-as-release-valve, self-updating-config, ablation-driven-development, principles-over-constraints, building-skills]
---

# Your AGENTS.md is a Neural Net

Kun Chen's argument that a project-level agent memory file (`AGENTS.md` / `CLAUDE.md`) should be treated like a neural network you **train**, not a file you **edit**.
The short version he states up front: handwrite your user-level file (your preferences, which you own), and treat your project-level files like weights - give them a size budget and train them on the sessions that actually ran.
It is the wiki's third source from [[kun]] (after [[building-products-with-agents]] and [[agentic-full-stack-build]]), and the first that is purely about **configuring** the agent rather than building with it.
He closes by open-sourcing the tool that runs the loop, [[backpass]] (MIT), which turns the method into a repeatable pipeline where one run is one gradient step.

## Key claims

### Memory files rot in four predictable ways
- Any project memory file older than a few months is in one of [[four-bad-memory-states|four bad states]]: **empty** (a tool created it, the agent re-derives everything), **bloated** (every dumb thing an agent did got a pasted-in rule, now 900 lines paid for on every session and diluting the rules that matter), **stale** (rules describe a build system replaced in March), or **drifted** (`AGENTS.md` and `CLAUDE.md` disagree, and each harness gets a different set).
- The common root cause is that the file is edited **transactionally, from anecdotes**, and appending is easier than consolidating and pruning.

### Two files, two opposite jobs
- The **user-level file is yours and handwritten**: preferences and opinions you own (prefer quality over dev cost, reproduce a bug end-to-end before fixing, fix the flaky test you walked past). Small, hand-written, changed rarely, and no tool or agent should "optimize" it. See [[two-level-agent-memory]].
- The **project-level file is a neural net**: it loads into the system prompt of sessions that run on the project and steers behavior "not too differently from a fine-tuned LoRA on top of the model." Instead of editing it, decide a token budget and train it.

### The training-loop mapping
- The project `AGENTS.md` is the **weights**; the token budget is the **model size** (bigger holds more but costs more at inference); every session is a **forward pass** (the file loads, the agent works, the file is untouched); the gap between what the agent did and what you wanted is the **loss**; reading transcripts and updating the file is the **backward pass**. See [[agents-md-as-neural-net]].
- Most people stop at the forward pass - they *use* the file every session but never run the backward pass to refine it against loss. The training signal already exists (every harness writes a transcript); nobody reads it.

### The backward pass is a discipline with five parts
- **Evidence from transcripts, not anecdotes** - the loss signal is the session logs, not your memory of being annoyed last Tuesday; treat each list item/paragraph as an addressable unit and ask, per session, was it followed, violated, or wrong, and what did the agent get wrong that no unit covers.
- **Batch before you update** - one bad session is noise; only a batch reveals a real pattern. This single constraint removes most bloat, because most pasted rules were one-incident reactions that never recurred.
- **Small steps** - a handful of edits per pass (about five), each an add/remove/rewrite/extraction. A large step on a memory file is indistinguishable from starting over, and you lose what was working.
- **Respect the budget; skills are the release valve** - at or near budget, updates are zero-sum, so every addition names the removal or extraction that pays for it. See [[skills-as-release-valve]].
- **A human gate writes** - nothing is committed until a person accepts each edit.

### The budget/skills triage rule
- Pick a budget for the always-loaded file (his example: 5,000 tokens).
- **Broad** instructions (matter in ~20%+ of sessions, or are safety-critical) stay in the memory file.
- **Narrow with a detectable trigger** become a [[building-skills|skill]].
- **Narrow with no detectable trigger** are deletion candidates.

### The tool ([[backpass]])
- `npx -y backpass` in a repo you recently worked on; the shape is the method turned into a pipeline.
- Collects transcripts from common harness stores (Claude Code, Codex, pi, opencode, grok, Cursor), ties each session to the repo by cwd or git remote, and distills each transcript to the loss signal (a 96-99% reduction with no model involved).
- Gradients are aggregated deterministically (per-unit positive/negative counts, relevance share, near-duplicate gaps clustered across sessions, and any gap seen in fewer than two sessions dropped).
- One high-reasoning call proposes the edits; mechanical gates enforce at most five edits, two sessions for a new rule, a verbatim quote on every edit, and a post-edit file that fits the budget. A gate violation gets one re-prompt; a second fails loudly and writes nothing.
- `backpass apply` presents the proposed edits in `lavish-axi` ([[review-plans-as-artifacts]]); the human accepts or rejects each, and rejections are remembered so the same edit does not return without new evidence.
- The flags are the training knobs under their real names: `--budget` is model size, `--max-edits` is learning rate, `--min-gap-evidence` is batch size, `--since` is the training window.
- His rhythm: one run a week per active repo.

## Connections

- [[agents-md-as-neural-net]] - the central metaphor and the full forward-pass/backward-pass mapping.
- [[two-level-agent-memory]] - handwrite the user-level file, train the project-level file; opposite treatment for the two levels.
- [[four-bad-memory-states]] - empty, bloated, stale, drifted, and the transactional-editing root cause.
- [[skills-as-release-valve]] - the budget-triage rule that decides what stays, what becomes a skill, and what gets deleted.
- [[backpass]] - the MIT tool that automates the backward pass; entity page.
- [[self-updating-config]] - **second source, and the rigorous version.** Pigford's learnings-skill is the same loop; this source supplies the discipline (verbatim-quote evidence, batching, budget, human gate) and a shipped tool.
- [[ablation-driven-development]] - **the complementary anti-bloat method.** Ablation is a periodic full reset keyed to model releases; this is a weekly small step keyed to transcript loss. Both are evidence-driven and budget-respecting; see the tension note below.
- [[principles-over-constraints]] - "every instruction is re-read on every invocation" is exactly the budget/model-size economics, stated as training cost.
- [[building-skills]] - narrow-with-a-trigger units graduate into skills; the release valve that keeps the memory file inside budget.
- [[skills-vs-plugins]] - the skill is the atom the release valve extracts to.
- [[capabilities-not-instructions]] - a memory file is a soft control surface; budgeting it is the benign cousin of removing what you cannot allow.
- [[kun]] - third source from this author; recovers his handle and domain.
- [[claude-code]], [[codex]], [[opencode]] - the harnesses whose transcript stores the tool reads.
- [[agentic-engineering]] - the area this source most directly populates.

## Source

- **Author:** Kun Chen (L8 principal engineer, ex-Meta/Microsoft/Atlassian; builder of First Mate, Lavish, No Mistakes, and now backpass)
- **Title:** Your AGENTS.md is a Neural Net (subtitle: "And here's how to properly train it with gradient descent")
- **URL:** https://blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net
- **Published:** 2026-08-22
- **Raw:** `raw/Your AGENTS.md is a Neural Net.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-27

### Provenance note

This is a clean first-party blog post (not an auto-captioned transcript), so unlike the two earlier Kun sources it needs no caption-correction caveats.
It also **recovers the identifiers the [[kun]] entity deliberately left blank**: the byline is "Kun Chen," the domain is `blog.kunchenguid.com`, and the tool repo is `github.com/kunchenguid/backpass`, so `kunchenguid` is his handle. The entity page has been updated accordingly.
