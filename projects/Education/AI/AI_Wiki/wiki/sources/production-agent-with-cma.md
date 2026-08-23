---
type: source
title: "Build a Production-Ready Agent with Claude Managed Agents"
source-type: tutorial-summary
author: "Anthropic (Code with Claude workshop)"
url: "local"
date-ingested: 2026-07-08
date-created: unknown
tags: [claude-managed-agents, anthropic, agent-infrastructure, observability, agent-safety, evals]
---

# Build a Production-Ready Agent with Claude Managed Agents

A summarized Anthropic ([[anthropic]]) workshop introducing Claude Managed Agents (CMA): a set of API endpoints that hand you production-ready, scalable agent infrastructure so you pick the primitives you need and build your product on top.
It live-builds a fake M&A app ("Deal"), handing the hard streaming work to [[claude-code]] via its built-in Claude API skill.

## The four primitives ([[managed-agent-primitives]])

- **Agent:** a template - system prompt, skills, tools, which MCP servers it connects to, and per-tool permission controls.
- **Environment:** a template for sandbox behavior - network access, pre-installed packages, and self-hosted sandboxes (bring your own via Cloudflare/Modal/Vercel).
- **Session:** an ongoing conversation (needs an agent ID + environment ID); can attach GitHub repos or preloaded files.
- **Events:** sessions are event streams (user events, agent events, session lifecycle, span events).

## Key claims

- **[[outcome-rubric-iteration|Outcomes]]:** pass Claude a file/blob that acts as a spec/rubric; it does a first pass, then iterates and checks its own work against the rubric until satisfied. Anthropic's native version of the [[skill-eval-loop]].
- **Per-tool permissions and threat-modeled tool choice:** a file-read tool can auto-execute while `bash` or a database MCP call requires explicit user approval; deliberately **deny web access** to some agents so they cannot be prompt-injected. This is [[capabilities-not-instructions]] built into the platform.
- **[[credential-vaults]]:** MCP auth tokens are injected without ever entering Claude's context window - secrets Claude never sees.
- **MCP tunnels / self-hosted sandboxes:** connect private MCP servers and keep private data inside your own network/VPC.
- **Memory stores:** read/write memory across sessions so each session benefits from prior ones; you can read and manually edit what Claude remembered (ties to [[self-updating-config]] and [[context-is-king]]).
- **[[agent-observability]]:** console views live-debug agent runs - drill into events, watch tool-call timing, see multi-agent coordination and span events (so long operations do not look stuck).
- **Agents are versioned** (roll back a bad system-prompt/tool change; old versions kept).
- **"Skate the exponential":** the primitives let you auto-benefit from each new model family without re-architecting - a platform expression of [[build-for-the-model-of-the-future]].
- Honest asides: Opus is "a little slow" and "sometimes gets lazy" (had to be prompted to finish).

## Connections

- [[managed-agent-primitives]], [[outcome-rubric-iteration]], [[agent-observability]], [[credential-vaults]], [[build-for-the-model-of-the-future]] - the concepts.
- [[outcome-rubric-iteration]] is the same rubric-until-pass pattern as the [[skill-eval-loop]] and [[fresh-context-review]] - now a first-class API.
- [[capabilities-not-instructions]] / [[red-team-your-agent]] - per-tool permissions and web-access denial are platform-level versions of scoping the key ring and reducing injection surface.
- [[agent-observability]] extends [[looking-at-your-data]] to agent traces; relevant to hcho's LangSmith observability in Agentic RAG.
- [[sub-agents]] - CMA's multi-agent coordination (Claude spawns agents with their own context windows).

## Source

- **Author:** Anthropic (Code with Claude workshop)
- **Title:** Build a Production-Ready Agent with Claude Managed Agents
- **Tools cited:** Claude Managed Agents API, Anthropic SDK, Bun, Linear/Figma MCP, Cloudflare/Modal/Vercel sandboxes, Opus 4.7.
- **Raw:** [[Claude_Managed_Agents_Production_Agent_Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
