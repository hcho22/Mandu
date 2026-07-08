---
type: concept
tags: [agent-safety, security, secrets, mcp]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Credential Vaults

A Claude Managed Agents security primitive, from [[production-agent-with-cma]]: provision MCP-server auth tokens once, store them securely, and have the platform inject them when needed **without the tokens ever entering Claude's context window**.

## Key points

- Claude can use an MCP server (Linear, Figma) whose credentials it never sees.
- Complemented by MCP tunnels (reach private MCP servers without exposing them to the internet) and self-hosted sandboxes (keep private data in your VPC).
- The design principle: keep secrets out of the model's context entirely, rather than trusting it not to leak them.

## Synthesis

This is [[capabilities-not-instructions]] applied to secrets: do not rely on the model to protect a credential it can see - make it physically impossible for the credential to enter its context.
It is the defensive counterpart to [[red-team-your-agent]] (which tries to exfiltrate secrets) and a concrete agent-security pattern hcho can point to when discussing production-AI safety.
