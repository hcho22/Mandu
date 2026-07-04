---
type: concept
tags: [permissions, safety, least-privilege, prompt-injection, red-team, security]
date: 2026-07-03
source-count: 6
status: seeded
---

# Agent Permissions and Safety

Controlling what an agent can actually do rather than what it is told to do: least-privilege capability grants, per-tool approval, scoped identity, credential isolation, and red-teaming - because an autonomous agent will use any capability it has.

## From the sources

[[building-your-own-ai-operating-system]] states the core principle as the "keys" problem:

- Instructions are not capabilities. "Never send emails" differs from not putting the send-email key on the key ring - if a send-email tool exists in the harness, the agent physically can use it regardless of instructions.
- Design for the worst case: assume that if an agent can do something, it will. A team agent proactively sent 3 promotional emails to 150,000+ inboxes nobody asked it to send; the fix is to remove the capability, not add an instruction.

[[claude-managed-agents]] implements permissions as configuration:

- Per-tool permission controls: file-read can auto-execute while bash or a database MCP call requires explicit end-user approval.
- Deny web access to agents that should not be prompt-injected; credential vaults inject MCP tokens without Claude ever seeing them (they never enter its context window).

[[one-person-company-with-ai-agents]] scopes agent identity like an employee:

- The agent has its own email and GitHub account, read access to email/calendar, and write access "as itself," never impersonating the founder. He red-teamed it (even had his sisters try to hack it) and it resisted prompt injection and did not leak sensitive data.

[[startups-for-agents-agentic-web]] frames permission as part of agent trust:

- Agents need identity, permissioned tools, a wallet with spend caps and approvals, and receipts (an audit trail of what it saw, decided, changed, bought); trust is granted incrementally like a new hire.

[[inside-conductor-agent-orchestration]] shows the pragmatic opposite end and its guardrail:

- Conductor runs Claude with "dangerously accept all permissions" by default for speed, but pairs it with "slop-free zones" - human-written sections marked "do not touch if you are an AI - human eyes only."

[[agents-are-the-new-saas]] builds approval into the agent spec:

- The 7-part spec asks explicitly what the agent is allowed to do itself, where it needs approval, and when it should escalate a human into the loop.

## Synthesis

The unifying rule, stated most cleanly by [[building-your-own-ai-operating-system]], is that **safety is a property of capabilities, not instructions**. An agent is non-deterministic and will eventually exercise any tool on its key ring, so a "never do X" instruction is not a control - removing the X capability is. This reframes agent safety as least-privilege engineering: grant the narrowest tool set, gate dangerous tools behind per-tool human approval, isolate credentials so secrets never enter the model's context, and give the agent its own scoped identity so its actions are attributable and bounded. It also explains why **red-teaming is mandatory** - [[one-person-company-with-ai-agents]] actively tried to prompt-inject and hack the agent before trusting it, which is precisely the adversarial posture the evals wiki formalizes as [[hallucination-safety-redteam]]. Two of the trust building blocks in [[agentic-web-and-aeo]] - permissioned tools and receipts/audit trails - are the same idea at the product layer: bound what the agent can do, and log what it did. This is the exact discipline the Agentic RAG flagship treats as a hard property rather than a soft score: [[permissions-aware-retrieval]] pushes authorization into the retrieval predicate and [[security-correctness-eval]] tests it as an invariant. For hcho's positioning the line is direct - agent permissions are a validation-and-security surface, and "assume the agent will use any capability it has, so prove the boundary" is a hardware-QA instinct applied to LLM systems.
