---
type: concept
tags: [skills, prompting, claude-code, reuse, progressive-disclosure]
date: 2026-07-03
source-count: 8
status: seeded
---

# Agent Skills

A skill is a folder of instructions (a markdown SKILL.md plus optional examples, evals, and memory) that an agent triggers for a recurring task, turning a repeated prompt into a reusable, versionable "recipe."

## From the sources

[[building-an-ai-skill-from-scratch]] gives the canonical anatomy and a 5-step method:

- A skill is a folder of instructions; create it from your best examples plus personal context, aiming for a ~one-page SKILL.md, and keep SKILL.md separate from the examples so the AI loads only what it needs and the generic skill stays shareable.
- Triggering depends entirely on the description: the AI reads only the name and description to decide whether to load the full skill, so it must say explicitly "Use when XYZ."
- The advanced steps add an eval loop (see [[evals-for-agents]]), a memory.md (see [[agent-memory]]), and a "skill editor" skill that audits all skills for slop.

[[every-claude-feature-ranked]] ranks skills the #1 feature:

- Markdown recipes make the agent perform tasks far more consistently than re-typing prompts; they live in .claude, are shareable and continuously refined, can chain to other skills, and work in Claude Code, chat, and Cowork. Even a four-sentence prompt deserves to be a skill.

[[building-your-own-ai-operating-system]] covers how to build and evolve them:

- Two methods: forward (from your cadence) or reverse-engineering a finished task ("look back at our conversation; what did we do?"). Evolve every skill on each use; a skill may take ~50 tries before you like it. Promote useful skills to global.

[[building-5-ai-products-solo]] treats skills as a reusable library:

- ~A dozen open-source skills orchestrate the whole workflow (build, research, learnings, but-for-real, ui.sh, support); he iterates the skill prompts themselves in Chops ("be meaner").

[[one-person-company-with-ai-agents]] reframes agents as skills plus schedule:

- "Agents are cron jobs and markdown files" - a good skill file is half of what makes an agent work; playbooks are skill-like docs whose value is improving them over time.

[[inside-conductor-agent-orchestration]] and [[claude-managed-agents]] show skills inside the harness:

- Conductor tunes a few-hundred-line CLAUDE.md plus skills files as the customizations that matter most.
- In CMA, an agent is configured with skills, and Claude Code ships with a Claude API skill that makes it "really good" at the Managed Agents APIs.

[[working-with-fable-5-in-claude-code]] shows skills as thin bridges to another model, with hard-won authoring rules:

- His kept skills (Codex review, implementation, computer use) mostly wrap GPT-5.5/Codex so Claude borrows its strengths without building them in. Confirms the description-first mechanic: the model sees only a skill's *description* until it invokes it, so the description must carry enough to decide.
- Authoring lessons from iterating: get the *commands* inside a skill right (the rare miss is very annoying), prompt Codex *simply* (don't prompt it like Claude), and handle the empty-result case explicitly so the parent model doesn't get confused and re-run. Broaden trigger descriptions to a sensible default.
- Emphatic rule: "Don't blindly copy someone else's skills/config" - screenshot them, have a model guide you to build your own, and be unafraid to edit and break things.

## Synthesis

Skills are the reusable unit of the whole agentic-building movement: every source independently converges on "encode a repeated task as a markdown file the agent triggers." The design principles are consistent and worth stating as rules. **Progressive disclosure** - keep SKILL.md short and split examples/context into separate files - exists because the trigger decision and the run both read only what they need, which is a token-economy and reliability argument, not just tidiness. **The description is the trigger surface**: a skill that does not say "Use when XYZ" will not fire, so description quality gates whether the skill is ever used. **Skills compound only if they evolve** - the learnings/memory loop and the periodic skill-editor audit keep them from rotting into AI slop (see [[human-taste-and-ai-slop]]). A skill sits one level below an agent: [[one-person-company-with-ai-agents]] and [[claude-managed-agents]] both treat an agent as a skill (or set of skills) plus a schedule ([[scheduled-agent-autonomy]]) plus permissions ([[agent-permissions-and-safety]]). This is the same mechanism this very repo uses - the `ingest` skill that produced this page is a SKILL.md with the exact anatomy described here - which makes "I build and maintain agent skills" a concrete, demonstrable talking point rather than an abstract claim.
