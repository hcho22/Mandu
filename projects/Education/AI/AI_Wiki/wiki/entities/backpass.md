---
type: entity
tags: [tool, open-source, agentic-engineering, agents-md, self-improvement, kun]
status: seed
source-count: 1
last-updated: 2026-08-27
---

# backpass

An open-source (MIT) CLI by [[kun]] that automates the **backward pass** on a project memory file - reading agent session transcripts and proposing budgeted edits to `AGENTS.md` / `CLAUDE.md`.
Introduced in [[agents-md-is-a-neural-net]].
Run it with `npx -y backpass` in a repo you recently worked on; `github.com/kunchenguid/backpass`.

Its design is the method of [[agents-md-as-neural-net]] turned into a pipeline: **one run is one gradient step.**

## The pipeline

1. **Collect.** Pulls samples from the local transcript stores of common harnesses (Claude Code, Codex, pi, opencode, grok, Cursor) directly from disk, tying each session to the repo by cwd or git remote.
2. **Distill.** Reduces each transcript to what carries the loss signal - what was asked, what the agent said, a one-line shape of each tool call - a 96-99% reduction with no model involved.
3. **Compute loss.** A cheap per-transcript model call produces the evidence against each addressable unit of the file; anything without a verbatim quote is discarded in code, not by a prompt.
4. **Aggregate gradients deterministically.** Per-unit positive and negative counts, a relevance share, near-duplicate gaps clustered across sessions, and any gap seen in fewer than two sessions dropped.
5. **Gradient step.** One high-reasoning call proposes the edits, and mechanical gates run: at most five edits, two sessions for a new rule, a verbatim quote on every edit, and a post-edit file that fits the budget. A violation gets exactly one re-prompt naming the breach; a second fails loudly and writes nothing. Token deltas are measured from the actual text, never from model-reported numbers.
6. **Human-gated apply.** `backpass apply` presents the proposed edits in `lavish-axi` ([[review-plans-as-artifacts]]) with each diff and its evidence; the human accepts or rejects each, and rejections are remembered so the same edit does not return without new evidence.

## The flags are the training knobs

- `--budget` = model size (the token ceiling for the always-loaded file)
- `--max-edits` = learning rate (step size per run)
- `--min-gap-evidence` = batch size (minimum sessions before a gap counts)
- `--since` = training window

## Why it fits the wiki

`backpass` is the shipped, rigorous version of [[self-updating-config]]: where Pigford's learnings-skill mines the chat you just had, backpass mines the transcript stores across every harness, enforces verbatim-quote evidence in code, and gates on an explicit budget.
It is the fourth tool the wiki records from [[kun]], after **First Mate** (orchestration, [[one-orchestrator-agent]]), **Lavish** (interactive review artifacts, [[review-plans-as-artifacts]]) - which backpass reuses for its apply step - and **No Mistakes** (local validation pipeline).
The reuse is worth noting: the same "present it as an annotated artifact and let the human accept per-element" mechanism that Lavish gives his build workflow is what makes the memory-training loop human-gated rather than autonomous.

## Notes

The tool is the clearest single instance in the wiki of [[looking-at-your-data]] pointed at **agent session logs** rather than product traffic: the transcripts are the data, the addressable units of the memory file are the labels, and the loss is where they disagree.
Directly relevant to hcho as a portfolio-shaped pattern and as something to actually run against Mandu's own long, rule-dense configuration.
