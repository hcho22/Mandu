---
type: concept
tags: [system-design, security, architecture]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Client Never Touches the Database

From [[building-robust-apps-with-ai]]: a hard security rule of [[system-design]] - the client must never query the database directly.
The correct flow is always **client -> server -> database -> server -> client**.

## Why

- If the client talks to the DB, anyone can open the Network tab (or inspect element) and read your API key/credentials - "you're absolutely cooked."
- This is Ross's main reservation about the common Supabase pattern: it offers a server library, but most people query from the client and lean on row-level security (RLS), which he calls "a fool's game."

## Synthesis

This is the one non-negotiable in an area otherwise governed by [[engineering-trade-offs]]: a concrete threat model with a single correct answer.
It is exactly the kind of security-boundary reasoning that is easy for a "vibe coder" to skip and natural for someone with a validation/QA background to catch - a small, high-leverage example of the judgment [[system-design]] is really about.
Relates to [[capabilities-not-instructions]] (make the boundary structural, not a note you hope holds) and [[credential-vaults]] (keep secrets out of any surface an attacker can reach).
