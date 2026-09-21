---
type: concept
tags: [workflow, agentic-engineering, code, worktrees]
status: developing
source-count: 2
last-updated: 2026-09-16
---

# Phased Implementation

The build method from [[building-5-ai-products-solo]]: research, then plan, then implement in small, individually testable phases rather than one large pass.

## Key points

- **Research** produces a high-level document (technical approach, what to port vs ignore, how systems interact).
- **Implementation** breaks the work into phases where each phase = one PR = one git branch; some plans run 30+ phases so each step can be personally tested.
- Each phase runs in a **fresh, isolated git worktree** - a shippable unit and a rollback checkpoint - which reduces [[context-rot]].
- A **progress/decisions file** carries context across phases so fresh agent sessions know where they are and do not repeat mistakes.
- Review the plan's **objectives**, not just its task list.

## Workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] recommends proving one thin end-to-end path before expanding features across UI, domain/API logic, persistence, and tests.
Its beginner adaptation favors integrated vertical slices over completing a mock frontend and connecting the backend later.

## Synthesis

This is the discipline that makes agent-built software verifiable: small units are testable, reviewable ([[adversarial-code-review]]), and revertible.
It is the same "constrain first, widen on evidence" instinct as [[phased-autonomy]] and the [[minimal-useful-agent]] ladder, applied to the build process, and it is where hcho's habit of testing each step end-to-end fits naturally.
