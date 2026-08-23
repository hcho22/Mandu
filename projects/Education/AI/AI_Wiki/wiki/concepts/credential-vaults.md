---
type: concept
tags: [agent-safety, security, secrets, mcp]
status: established
source-count: 3
last-updated: 2026-08-01
---

# Credential Vaults

A Claude Managed Agents security primitive, from [[production-agent-with-cma]]: provision MCP-server auth tokens once, store them securely, and have the platform inject them when needed **without the tokens ever entering Claude's context window**.

## Key points

- Claude can use an MCP server (Linear, Figma) whose credentials it never sees.
- Complemented by MCP tunnels (reach private MCP servers without exposing them to the internet) and self-hosted sandboxes (keep private data in your VPC).
- The design principle: keep secrets out of the model's context entirely, rather than trusting it not to leak them.

## Two practitioner accounts (2026-08-01)

The pattern showed up independently in two of this batch's sources, which upgrades it from a vendor primitive to a working practice.

**Per-access authorization** ([[agentic-full-stack-build]]).
Kun keeps all secrets in a vault where, when an agent needs one, a dialog shows **which agent is asking and what command is proposed**, and he approves or denies each one.
The token is passed as an **environment variable**, so the agent can call the API but never sees it in plaintext.
He deliberately declined blanket allow-rules for his cloud provider account.

**Why `.env` files fail** - and this is the sharpest argument for the whole pattern:

> "Those environment files can be quite easy to get stolen... maybe the agent has published that secret to another public file, or sent it as part of a public API call."

The load-bearing clause is what follows: **since you're not reading every tool call, you have no idea when a secret has leaked.**
That ties secret handling directly to [[get-out-of-the-loop]] - the more you delegate without watching, the less a credential-in-context is survivable.

**Never give agents production write keys** ([[running-teams-of-ai-agents]]).
[[ryan-carson]] approaches the same problem from key custody rather than context isolation: production writes are dangerous and agents *will* do something bad, so keys live in a password manager and the workflow is built so the agent **asks you for the key** when it needs to write to prod.
You paste it into that session, and both of you are explicit about what is happening.

**The shared permission philosophy**, stated almost identically by both: give the agent broad permissions and capabilities everywhere, and require **explicit human authorization at the production boundary**.
That is [[phased-autonomy]] drawn as a hard line around one blast radius rather than as a gradual ramp.

## Synthesis

This is [[capabilities-not-instructions]] applied to secrets: do not rely on the model to protect a credential it can see - make it physically impossible for the credential to enter its context.
It is the defensive counterpart to [[red-team-your-agent]] (which tries to exfiltrate secrets) and a concrete agent-security pattern hcho can point to when discussing production-AI safety.

With three sources the concept has a clearer shape: **context isolation and key custody are two different defenses**, and the practitioners use both.
Isolation stops the secret being *in* the transcript; custody stops the agent holding a key whose misuse would be unrecoverable.
Note that [[building-at-the-frontier]]'s prompt-injection-resistance claim does nothing to relax either one - an uninjectable agent with a production write key is still one ordinary bug away from a bad outcome.
