---
type: source
title: "Building Your Own AI Operating System"
source-type: tutorial-summary
author: "Nate (AI automation creator; possibly Nate Herk - see [[nate-herk]], unconfirmed)"
url: "local"
date-ingested: 2026-07-08
date-created: unknown
tags: [ai-operating-system, second-brain, claude-code, context-engineering, agent-safety, skills]
---

# Building Your Own AI Operating System

A summarized YouTube tutorial on turning Claude Code (running Claude Opus) into a single "second brain" / executive assistant that runs the creator's businesses - an [[ai-operating-system]] (AIOS).
Structured around two frameworks: the Three M's (Mindset, Method, Machine) and the [[four-cs-framework]] (Context, Connections, Capabilities, Cadence).
Core claim: the model is not the differentiator (everyone has the same one); [[context-is-king|your context is]].

This source is unusually meta for hcho: it describes almost exactly the Mandu setup this wiki lives in.

## Key claims

- **The default shift:** do every task from [[claude-code]] first, before Chrome or other apps, because Claude Code runs the same model as the chat UI but accumulates context as you go. This shrinks the tool stack and cuts context-switching.
- **[[context-is-king]]:** the model is the engine, your context is the fuel; models are stateless (a fresh session only knows global rules + `CLAUDE.md` + the files you give it); treat tokens like money.
- **[[four-cs-framework]]:** build Context to Connections to Capabilities to Cadence, in that order - each layer depends on the previous. Connections = what it can touch (calendar, tasks, messages, revenue); Capabilities = how you work, usually encoded as skills; Cadence = things that happen automatically.
- **Organize as plain files and folders;** there is no single right way, the only real failure mode is so much disorganized context that neither you nor the AI can find things. Staying in plain files keeps you tool-agnostic (agents/claude/codex folders).
- **Agent safety - [[capabilities-not-instructions]]:** "instructions are not capabilities." Saying "never send emails" differs from not putting the send-email key on the key ring. Design for the worst case: assume if an agent can do something, it will; remove the capability entirely for anything you cannot afford. (Cautionary tale: an agent proactively sent 3 promos to 150,000+ inboxes that were not meant to go out.)
- **[[phased-autonomy]] (the bike method):** grant autonomy in stages, only after a skill earns it; every run makes the skill better.
- **[[building-skills]]:** build forward (from your cadence, via a skill creator) or reverse-engineer (do a task end-to-end, then have Claude Code extract the reproducible skill); evolve every skill on every use; even a repeated prompt deserves a skill (e.g. a global `session-handoff` skill).
- **Mindset:** treat the AIOS as a mentor; "you can outsource your thinking, but you cannot outsource your understanding"; judge every new skill against your North Star metric, and define productivity as moving the needle, not hours worked. Expect a short-term ~20% dip when automating a manual process before the long-term payoff.

## Connections

- [[ai-operating-system]] - founding source for this concept.
- [[agentic-engineering]] - the AIOS is agentic engineering applied to your own work; "context engineering" and skills are shared pillars.
- [[capabilities-not-instructions]] extends the safety half of the [[seven-part-agent-spec]] (allowed actions, approval, escalation) with a hard rule: remove the key.
- [[phased-autonomy]] is the deployment-side sibling of [[start-as-a-workflow]] and the [[minimal-useful-agent]] ladder.
- [[claude-code]] / [[anthropic]] - the harness the whole system runs on.
- Meta: this is a template for hcho's own "second brain / AI OS" priority; and for what AI_Wiki plus Mandu already are.

## Source

- **Author:** Nate (AI automation creator; runs a Skool community + AIOS course)
- **Title:** Building Your Own AI Operating System
- **URL:** local summary (YouTube tutorial)
- **Raw:** [[AI_Operating_System_Tutorial_Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
