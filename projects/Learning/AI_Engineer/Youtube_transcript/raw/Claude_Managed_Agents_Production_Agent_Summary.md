# Build a Production-Ready Agent with Claude Managed Agents

*Workshop Summary · Code with Claude*

> A technical deep dive into the Claude Managed Agents (CMA) primitives — agents, environments, sessions, and events — building a real chat app live and deploying it to production.

---

## Overview

**What this is.** A hands-on, code-along workshop introducing **Claude Managed Agents (CMA)**: a set of API endpoints (usable today with any API key) that hand you production-ready, scalable agent infrastructure so you can pick the primitives you need and build your own product on top. The presenter walks through the four core building blocks, then live-builds a (fake) M&A deal-analysis web app called **"Deal"** from a starter repo — implementing session list/retrieve endpoints by hand, then handing the streaming work to Claude Code. It closes with newer capabilities (self-hosted sandboxes, MCP tunnels, multi-agent, credential vaults, memory stores) and the developer-console observability views.

---

## Table of Contents

1. [What Claude Managed Agents Is (Overview)](#1-what-claude-managed-agents-is)
2. [The Four Core Building Blocks](#2-the-four-core-building-blocks)
3. [Configuring Agents & Environments (Tools, Permissions, Sandboxes)](#3-configuring-agents--environments)
4. [Sessions & the Event Model](#4-sessions--the-event-model)
5. [Events in Depth (User, Agent, Session, Span)](#5-events-in-depth)
6. [New Capabilities: Self-Hosted Sandboxes & MCP Tunnels](#6-new-capabilities-self-hosted-sandboxes--mcp-tunnels)
7. [Live Build: The "Deal" App from the Starter Repo](#7-live-build-the-deal-app)
8. [Handing Off to Claude Code (the Claude API Skill)](#8-handing-off-to-claude-code)
9. [Outcomes, Multi-Agent & Live Observability](#9-outcomes-multi-agent--live-observability)
10. [Credential Vaults & Memory Stores](#10-credential-vaults--memory-stores)
11. [Why CMA: What You'd Otherwise Have to Build](#11-why-cma-what-youd-otherwise-build)

**Callout legend:**
- 💡 **Tip** — actionable advice
- 📘 **Rule / Capability** — general principle or feature
- 💬 **Opinion / Aside** — speaker's personal view

---

## 1. What Claude Managed Agents Is

The session is positioned as a more technical follow-up to earlier high-level talks. The goal: by the end, attendees can start building on CMA the same day, with laptops out and code running.

> 📘 **Definition · the core idea**
> CMA is a set of **API endpoints** (released and usable today with any API key) that give you scale-ready, production-ready agents plus all the surrounding primitives. You **pick and choose the primitives you need, ditch the rest**, and build your own product experience on top.

What CMA takes care of for you: giving Claude access to a computer; access to **credential vaults** (e.g., injecting MCP authentication for your end users, like their Linear MCP); the tool-calling harness; retries and error recovery in production; and primitives for **memory, context management, and multi-agent**.

> 💬 **Speaker's framing**
> These primitives make it easy to "skate the exponential" — i.e., automatically benefit from each new model family as it ships, without re-architecting.

> 💡 **Tip · Use the console for live debugging**
> CMA includes **observability views in the developer console** that let you live-debug what your agents are doing. The presenter returns to this repeatedly — it's a central part of the workflow, not an afterthought.

---

## 2. The Four Core Building Blocks

CMA has four main primitives you need to worry about (plus a few side ones):

| Block | What it is |
|---|---|
| **Agent** | A template: system prompt, skills, the set of tools it can use, which MCP servers it connects to, and per-tool permission controls. |
| **Environment** | A template for how Claude's sandboxes behave: network access, pre-installed packages, and (new) self-hosted sandboxes. |
| **Session** | An ongoing conversation between an end user and Claude — the equivalent of clicking "new" on claude.ai or entering Claude Code in a terminal. Needs an agent ID + environment ID to start. |
| **Events** | Sessions are ongoing event streams: you submit messages from your client, and the server returns SSE responses as Claude processes them. |

---

## 3. Configuring Agents & Environments

### Agent configuration
- Define the **system prompt**, **skills**, and the **tools** the agent can access.
- Choose which **MCP servers** it connects to.
- Set **per-tool permission controls**: e.g., a file-read tool can *auto-execute*, while executing `bash` or calling a database's MCP server *requires explicit approval* from your end users.

> 💡 **Tip · Withhold web access to reduce prompt-injection risk**
> Some agents should have `bash` and web search; others you'd deliberately **deny web access** so they can't be prompt-injected. Choose tools per agent based on the threat model.

### Environment configuration
- Define whether containers have **network access**.
- Pre-install packages from **npm** or **pip**.
- (New) Use **self-hosted environments/sandboxes** — bring your own via Cloudflare, Modal, or Vercel, or your own sandboxing fleet, instead of running on Anthropic's infrastructure.

---

## 4. Sessions & the Event Model

With an agent ID and environment ID, you start a **session**. From there your end users submit events — e.g., asking for a PR to be opened. When creating sessions you can also attach **GitHub repositories** for Claude to access, or **files preloaded into the container**; CMA downloads and provisions these on your behalf. Sessions are ongoing event streams: your client submits messages, and the server streams back what Claude is doing.

---

## 5. Events in Depth

### User events (things you submit)
- **Messages** from your user or auto-submitted by your platform — can include images, documents, or text.
- **Interrupts** to cut Claude off mid-task (e.g., if it's going off on a bad tangent) and steer it, or prevent a dangerous action.
- **Tool results** for custom tools you define and execute on your own platform.
- **Confirmations** for human-in-the-loop controls on server-executed tools.
- **Outcomes** — see the dedicated callout below.

> 📘 **Key capability · Outcomes**
> An outcome lets you pass Claude a **file or blob of text that acts as a spec/rubric**. Claude does a first-pass implementation, then enters a mode where it **iterates and checks its own work against the rubric repeatedly** until it satisfies it. The presenter calls this a very powerful way to set agents up for success.

### Agent events (things Claude does)
- Messages Claude sends back to the user.
- **Compaction** events when Claude needs to compact a too-large context window.
- Tools being executed (MCP tools or the default agent tools).
- **Multi-agent coordination** events when Claude spawns other agents to help.

### Session events
Lifecycle/state-transition events: entering a retry loop, errors, idling, termination, and outcome-processing (knowing when Claude enters the rubric-iteration mode).

### Span events

> 📘 **Why span events exist**
> They mark the start and end of known long-running operations (e.g., Opus 4.7 generating a very long document) so you and your users **don't think the system is stuck**.

---

## 6. New Capabilities: Self-Hosted Sandboxes & MCP Tunnels

> 📘 **Self-hosted sandboxes**
> Bring your own containers (Cloudflare, Vercel, Modal, or your own fleet) instead of Anthropic's — useful when private data shouldn't leave your VPC/perimeter. CMA simply tells you when Claude needs a new sandbox; you spawn one and connect it, and configure how it operates end to end.

> 📘 **MCP tunnels**
> A secure tunnel that lets Claude connect to **private MCP servers inside your own network** without ever exposing them on the internet — a way to safely connect private data sources to CMA.

---

## 7. Live Build: The "Deal" App

The build uses a **public starter repo** (the presenter encourages cloning it; it contains patterns from other workshop presenters too). The relevant directory targets **production-ready agents** and contains both a **starter** version and a **solution** version (to skip ahead). The demo product, "Deal," is a contrived M&A tool: a basic chat UI with sessions on the left and session info on the right, using the new **multi-agent** feature so different agent personas handle different jobs (e.g., one on macro industry trends, one on financial analysis with its own tools/MCP servers).

> 💬 **Speaker's aside**
> All companies in the demo are fake and "Deal" isn't a real product — it's a contrived example, with the hope attendees build more interesting things.

### Implementing endpoints by hand
- Runs the local server with **Bun** ("we all love bun here") — notes Bun hot-reloads so he didn't even refresh the page.
- **List sessions:** implements a stubbed endpoint using the Anthropic SDK — `client.beta.sessions.list` — and returns the data.
- **Retrieve session (to-do #4):** the get-session API response shows the agent, its available tools, its Linear MCP connection, and any defined outcomes.

> 💡 **Tip · You don't have to implement to-dos in order**
> The presenter numbered the to-dos but deliberately tackled them out of order (doing #4 early) — build in whatever order makes sense for understanding the APIs.

---

## 8. Handing Off to Claude Code

The harder part — the **streaming endpoint** (server-to-client streaming of session/agent events) alongside the send-events endpoint — he hands to **Claude Code** rather than writing by hand.

> 💡 **Tip · Claude Code ships with the Claude API skill by default**
> This skill makes Claude "really, really good" at using Anthropic's APIs, specifically the Managed Agents APIs. The takeaway: that's *all* you need to do to make Claude effective at building CMA integrations — point it at your to-dos and let it read the skill. In his words, "Claude can help you build your own Claude."

> 💬 **Honest aside**
> He notes Opus is "a little bit slow," and that Claude "sometimes gets a little lazy" (he had to prompt it to finish the rest of the endpoints). Realistic expectations, not a polished pitch.

### Docs & console as starting points
- Official developer docs cover endpoints for every primitive: creating/updating/fetching agents, environments, and sessions, plus sub-endpoints for listing/streaming session events and listing uploaded resources (files, GitHub repos) that you can add over time to keep a session alive.
- The console offers a **quick start** where you chat with Claude and it helps you build your agents and sessions, plus predefined templates as starting points.

> 📘 **Capability · Agents are versioned**
> If you make a change to a system prompt or tool list you're unhappy with, you can roll back to a previous version — old versions are never discarded.

---

## 9. Outcomes, Multi-Agent & Live Observability

To start a session he selects the **Linear MCP** and **memory stores** (this calls the create-session endpoint), with two suggestion chips: a plain message ("give me a quick read on Acme Robotics") and an **outcome** covering three fake companies (Bridgewell Dynamics, Norwood Automation, Acme Robotics) with data across Linear and uploaded files, asking Claude to iterate, criticize its own work, and check findings against the rubric.

### Watching it run live in the console
- Claude spawns **four other agents**, each with its own context window, that chat with their coordinator and pass updates along.
- Each independent agent shows as a horizontal line; you can drill into individual events (e.g., web-search inputs/outputs).
- You can monitor **how long tool calls take** to debug slow operations (e.g., an inefficient file).
- At the end, Claude emits an **outcome evaluation** indicating it reached a conclusion against the rubric.

> 📘 **Audience Q&A · "plugins" for agents**
> Asked whether you can put plugins into agents, the presenter said something along those lines is being explored to keep the Claude ecosystem cohesive and extensible; nothing shipped yet, but **agent definitions already operate much like plugins**, and more is coming "soon."

---

## 10. Credential Vaults & Memory Stores

> 📘 **Credential vaults**
> Provision MCP-server auth tokens once and store them securely with Anthropic. When Claude wants to use an MCP server (Linear, Figma, etc.) and you include that vault in the session, CMA **injects the tokens without Claude ever seeing them** — they never enter Claude's context window, making the whole thing more secure.

> 📘 **Memory stores**
> Give Claude access to one or several memory stores it can read from and write to over time, so each session benefits from prior sessions' memories and gets better than the one before.

> 💡 **Tip · Read — and edit — what Claude remembers**
> The presenter likes reading through memory stores to see what Claude wrote about itself, and **manually editing** memories when Claude got something wrong. You can also generate and add your own memories.

---

## 11. Why CMA: What You'd Otherwise Build

The closing argument: doing this yourself would mean building all of the following — CMA gives them out of the box (you don't have to use every primitive, but they're there if you need them):

- Your own **agent loop** (or using the Agent SDK) and a way to **host it remotely**.
- **Context management**, state transitions, and recovery from those transitions.
- Integrating **skills and MCP servers**.
- A **durable storage layer** for all events/threads/agent data.
- A **sandboxing fleet** (e.g., Cloudflare) that reacts to what Claude is doing.
- Secure, reliable **end-user authentication** — which the presenter notes is hard to do well.

---

*Summary generated from the workshop transcript. Caption misspellings were corrected (e.g., "cloud manage agents" → Claude Managed Agents, "Enthropic" → Anthropic, "cla/claw/clawed" → Claude, "Versel/Versell" → Vercel, "claw.ai" → claude.ai). Product names (Claude Managed Agents, Anthropic SDK, Bun, Linear/Figma MCP, Cloudflare, Modal, Vercel, Opus 4.7) and capabilities reflect the presenter's statements; opinions and asides are flagged as such.*
