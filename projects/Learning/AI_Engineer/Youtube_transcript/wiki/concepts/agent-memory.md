---
type: concept
tags: [memory, persistence, auto-memory, state, personalization]
date: 2026-07-03
source-count: 5
status: seeded
---

# Agent Memory

Persistent knowledge an agent carries across sessions - stores it reads and writes over time, self-updating memory, and per-skill memory files - as distinct from the transient context loaded into a single session.

## From the sources

[[claude-managed-agents]] provides memory as a managed primitive:

- Memory stores give Claude read/write persistent memory across sessions, so each session benefits from prior ones and gets better than the one before.
- You can read what Claude wrote about itself and manually edit memories when it got something wrong, or add your own.

[[every-claude-feature-ranked]] covers self-updating memory:

- Auto-memory (formerly "auto-dream") periodically searches back through your work and updates its own memory unprompted - it "dreams and makes itself smarter"; check whether it is on with /memory.

[[building-an-ai-skill-from-scratch]] scopes memory to a skill:

- memory.md improves the skill itself (a concise, reverse-chronological log of lessons), while the eval loop improves each run's output. Keep entries to 2-3 sentences, non-overlapping with evals, and use memory for vague, taste-level feedback that cannot be a pass/fail check.

[[building-your-own-ai-operating-system]] treats memory as a layer of the system:

- The .claude folder holds agent memory alongside agents, plans, rules, and skills; because models are stateless, memory plus loaded context is what stops each session from starting as a beginner.

[[startups-for-agents-agentic-web]] lists memory as core agent infrastructure:

- Memory is one of the six building blocks every agent needs ("what does it know about my preferences and rules?"), alongside identity, tools, inbox, wallet, and receipts.

## Synthesis

Memory is the durable counterpart to [[context-engineering]]: context is what you load into one session's window and pay tokens for, while memory is what survives between sessions so the system compounds. The sources draw a useful three-way distinction. **Managed memory stores** (CMA) are backend persistence the agent reads and writes as a tool - most powerful, and notably *editable by the human*, which matters because an agent that misremembers will keep acting on it. **Self-updating memory** (auto-memory) closes the loop automatically by periodically distilling recent work, trading control for zero maintenance. **Scoped memory files** (a skill's memory.md) keep lessons next to the thing they improve and are deliberately kept small, because a bloated memory file confuses the model - the same progressive-disclosure discipline as [[agent-skills]]. Two rules generalize: keep memory concise and non-overlapping with other layers (evals, context) or it becomes noise, and keep a human able to read and correct it. The boundary this wiki observes mirrors the repo's own: an agent's memory store holds domain and preference state, while this wiki holds domain *knowledge* - the same separation the Mandu memory system keeps between `memory/` (who hcho is, how to work) and the wikis (what the field knows). For the agentic web, memory graduates from a convenience to infrastructure: [[startups-for-agents-agentic-web]] lists it beside identity and wallet as something every agent-native product must provide.
