---
type: concept
tags: [agent-safety, security, prompt-injection, evals]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Red-Team Your Agent

The practice from [[one-person-company-with-agents]] of deliberately attacking your own agent to test its security before trusting it.
Ryan Carson had the interviewer, and even his sisters, try to prompt-inject R2; it held up and leaked nothing sensitive.

## Key points

- Test resistance to prompt injection and data exfiltration (credentials, personal data) as a standing check, not a one-off.
- It is the offensive complement to [[capabilities-not-instructions]]: verify that scoped permissions actually hold under attack.
- Pairs naturally with an [[evals]] mindset - a security eval set of adversarial prompts.

## Synthesis

Red-teaming is agent security expressed as validation, and it is one of the most direct bridges from hcho's hardware-QA/validation background to a differentiated AI-quality skill (adversarial testing, threat modeling for agents).
Expect the LLM-security and contamination sources in `raw/` to deepen this into a fuller security area; for now it anchors the offensive side of agent safety alongside [[capabilities-not-instructions]] and [[agent-as-employee]].
