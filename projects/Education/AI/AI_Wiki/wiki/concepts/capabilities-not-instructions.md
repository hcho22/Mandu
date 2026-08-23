---
type: concept
tags: [agent-safety, permissions, agents, craft]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# Capabilities, Not Instructions

The agent-safety rule from [[ai-operating-system-tutorial]]: an instruction is not the same as a capability.
Telling an agent "never send emails" is different from not putting the send-email key on its key ring - if the tool exists in the harness, the agent physically can use it, regardless of instructions.

## Key points

- Think in terms of **keys**: the permission layer around your agents. As you climb the pyramid (workflow to agent to team of agents), autonomy, reach, risk, and cost all rise together.
- **Design for the worst case:** assume that if an agent can read or do something, it will. Usually it will not, but assuming it will changes how you grant endpoints and MCP servers.
- **Remove the capability, do not rely on the instruction,** for anything you cannot afford the agent to do. Keep access tightly scoped.
- Cautionary tale: an agent proactively picked up a to-do and sent 3 promotional emails to 150,000+ inboxes that were never meant to go out.

## Related agent-safety concepts

- [[agent-as-employee]] - scoping the agent's identity and permissions is the same idea applied to who the agent *is*.
- [[red-team-your-agent]] - the offensive check that your scoped permissions actually hold under attack.
- [[credential-vaults]] - the extreme case: keep secrets out of the model's context entirely.
- Platform example ([[production-agent-with-cma]]): per-tool permission controls (auto-execute a file read, but require approval for `bash` or a database MCP call), and deliberately denying web access to an agent to shrink its prompt-injection surface.

## Synthesis

This is the hardest-edged agent-safety principle in the wiki so far, and it sharpens the safety half of the [[seven-part-agent-spec]] (allowed actions, approval, escalation): those define intent, but the key ring defines what is physically possible.
It pairs with [[phased-autonomy]] (earn trust before widening the key ring) and is exactly the kind of failure-mode-first thinking hcho's validation background is built for - it is threat modeling for agents.
