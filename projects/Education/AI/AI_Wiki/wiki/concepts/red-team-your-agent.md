---
type: concept
tags: [agent-safety, security, prompt-injection, evals]
status: developing
source-count: 2
last-updated: 2026-08-01
---

# Red-Team Your Agent

The practice from [[one-person-company-with-agents]] of deliberately attacking your own agent to test its security before trusting it.
Ryan Carson had the interviewer, and even his sisters, try to prompt-inject R2; it held up and leaked nothing sensitive.

## Key points

- Test resistance to prompt injection and data exfiltration (credentials, personal data) as a standing check, not a one-off.
- It is the offensive complement to [[capabilities-not-instructions]]: verify that scoped permissions actually hold under attack.
- Pairs naturally with an [[evals]] mindset - a security eval set of adversarial prompts.

## The frontier claim that complicates this (2026-08-01)

[[building-at-the-frontier]] reports that **Claude Opus 5 does not appear to be prompt-injectable.**
A year earlier a model reading a web page instructing it to do X, Y, Z *and* delete everything on the user's computer would have complied; [[boris-cherny]] says it no longer does, and that Anthropic **can no longer demonstrate a successful prompt injection.**

The defense is three stacked layers: a well-aligned model (~3 years of alignment research), a **prompt-injection classifier** on all traffic built on mechanistic-interpretability work that inspects the neurons activating during an injection, and the auto-mode classifier.

**Boris's own caveats, which must travel with the claim:**
"We cannot demonstrate it" is a statement about Anthropic's internal red-teaming, **not a guarantee**.
And two of the three layers live in the **serving stack**, not the raw weights - so the resistance is a property of using Anthropic's hosted product, not of the model you might self-host or of any other vendor's stack.

**What this does and does not retire.**
If injection resistance holds, a large amount of defensive scaffolding built around the "lethal trifecta" becomes unnecessary, and Boris says to re-examine yours.
What it does **not** retire is this page's actual practice.
Red-teaming is how you *find out* whether it holds for your agent, your tools, and your data - and a claim from the vendor is the least appropriate thing to accept without testing.
If anything the claim raises the value of independent red-teaming, because the failure mode has shifted from "everyone knows this is exploitable" to "everyone assumes it isn't."

It also does not touch [[capabilities-not-instructions]], which is about what the agent *can* reach rather than what it can be talked into. An uninjectable agent holding a production write key is still one bug away from a bad day - see [[credential-vaults]].

## Synthesis

Red-teaming is agent security expressed as validation, and it is one of the most direct bridges from hcho's hardware-QA/validation background to a differentiated AI-quality skill (adversarial testing, threat modeling for agents).
The 2026-08-01 update sharpens rather than weakens that bridge: the interesting question moved from "can this be injected" to "**can I demonstrate that it can't**, on my stack, with my tools attached" - which is a validation question, and a harder one.

It anchors the offensive side of agent safety alongside [[capabilities-not-instructions]] and [[agent-as-employee]], with [[data-contamination]] and [[contamination-detection]] as the evaluation-integrity siblings.
