---
type: concept
tags: [ai-operating-system, framework, architecture]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# The Four C's Framework

The architecture of an [[ai-operating-system]], from [[ai-operating-system-tutorial]]: build the layers in order, each depending on the one before.

## The four layers

1. **Context** - it knows your business (a fresh session can answer "what does this business do and who works here?").
2. **Connections** - what it can actually touch: calendar, tasks, messages, revenue, meetings, knowledge (via APIs / MCP servers), rather than you copy-pasting.
3. **Capabilities** - how you do work, usually encoded as skills ("when writing a LinkedIn post, use this style and framework").
4. **Cadence** - turning the above into things that happen automatically, unprompted.

Order matters: no reliable cadence without capabilities, no capabilities without connections, no connections without context.

## Getting started

Self-audit where you go each week for seven categories: revenue, customer data, calendar, internal comms, tasks, meetings, knowledge - and connect those sources one at a time.

## Synthesis

The framework is a practical build sequence for [[context-is-king]]: it operationalizes "give the model good fuel" into concrete layers.
Capabilities map onto [[building-skills]] and cadence onto scheduled automation; the whole stack is an instance of [[agentic-engineering]].
