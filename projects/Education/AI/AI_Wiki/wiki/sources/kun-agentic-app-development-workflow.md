---
type: source
title: "Agentic App Development Workflow: A beginner-friendly reconstruction of Kun's latest workflow"
source-type: tutorial-summary
author: "Uncredited local compiler; talks attributed to Kun Chen"
url: local
date: 2026-09-16
date-ingested: 2026-09-16
date-created: unknown
tags: [agentic-engineering, architecture, workflow, orchestration, validation, reproducibility]
---

# Kun's Agentic App Development Workflow

A local guide reconstructs an app-development workflow from four supplied YouTube transcripts attributed to [[kun]].
It describes agent onboarding and isolated worktrees, reproducible development environments, a real full-stack build, and project fleets managed through one orchestrator.
Its reusable sequence is to clarify intent, research options, review architecture and user flows, capture decisions, build integrated slices, validate independently, and review risk before release.
The guide also supplies its own beginner prompts, documentation templates, adoption stages, and checklists.

## Key claims

- Human attention belongs on intent, boundaries, tradeoffs, acceptance evidence, and risk; research, implementation, testing, and coordination can be delegated.
- A complete intent dump includes constraints, non-goals, privacy, offline behavior, data ownership, and uncertainties before agents fill gaps themselves.
- Product and technical research can run in parallel; proposed costs and requirements still need to be challenged.
- Interactive architecture diagrams and clickable user flows help surface hidden requirements and targeted feedback.
- Write agreed product, API, identity, data, and deployment contracts into durable documentation, revisiting them when integration exposes gaps.
- Parallel workers need isolated workspaces, stable shared contracts, and scoped acceptance criteria.
- Build a thin real end-to-end slice before broad feature coverage, then expand in testable vertical slices.
- Compilation, mock screens, and a completion claim are weaker evidence than a real authenticated action that persists and can be retrieved.
- Separate implementation from fresh-context validation and keep evidence proportional to the consequence of failure.
- Use different review and merge policies for reversible prototypes and consequential authentication, payment, permission, secret, or migration changes.
- Reproducible configuration, small always-loaded memory, conditional skills, and harness-independent rules support continuity.
- One First Mate interface, project-scoped Second Mates, and fleet digests can reduce coordination burden; add hierarchy for an actual bottleneck.

## Beginner adaptation

The compiler recommends starting with one app and one agent, then adding isolated workers and an independent reviewer as needed.
Its suggested documentation package and reusable prompts are teaching aids, not a verified list of files Kun requires.
The practical acceptance pattern is a real journey through the application, authority boundary, persistence, retrieval, and a relevant failure or permission case.
Choose technologies from product requirements instead of copying the wallet app's stack.

## Evidence and limitations

This is a secondary reconstruction, not the four original transcripts or independently reproduced test evidence.
The raw guide supplies no video URLs, publication dates, or compiler byline.
Its claimed chronology follows transcript order and backward references rather than verified upload dates.
Some names are explicitly normalized from speech-to-text.
Overlap with [[building-products-with-agents]] and [[agentic-full-stack-build]] is likely but cannot be mapped exactly from the supplied source basis.
This adds one cataloged source and a useful teaching sequence, not four independent confirmations of the wiki's claims.
Reported tool capabilities, model preferences, cost assumptions, and production practices remain source claims rather than current product documentation.

## Connections

- [[plan-code-validate]] and [[ramble-then-structure]] - turn complete intent and discovered constraints into an executable contract.
- [[review-plans-as-artifacts]] and [[design-system-not-a-design]] - review behavior and component vocabulary before production UI.
- [[one-orchestrator-agent]] - project managers extend one human interface without making every worker the human's coordination responsibility.
- [[phased-implementation]] - thin integrated paths precede broad frontend/backend expansion.
- [[define-the-end-to-end-gate]] and [[agent-testing-instructions]] - real dependencies and failure cases determine completion evidence.
- [[fresh-context-review]] - validation is a separate phase against original intent.
- [[skills-as-release-valve]] - minimal onboarding and conditionally loaded knowledge complement reproducible tooling.
- [[client-never-touches-the-database]] - server authority over domain actions is transferable; the example does not prove all secure client database access invalid.
- [[risk-based-agent-governance]] - match review, merge, and production authority to consequence and reversibility.
- [[reproducible-agent-environment]] - reconstruct workstation, shared rules, and infrastructure while keeping secrets outside version control.
- [[agentic-engineering]], [[agent-operations]], and [[system-design]] - build practice, fleet coordination, and authority boundaries meet in one workflow.

## Source

- Author: uncredited compiler; talks attributed to Kun Chen.
- Title: Agentic App Development Workflow: A beginner-friendly reconstruction of Kun's latest workflow.
- URL: local; original transcript URLs are not supplied.
- Raw: [Immutable raw guide](../../raw/260916_Kun_Agentic_App_Development_Workflow_Beginner_Guide.md).
- Ingested: 2026-09-16.
- Publication date: unknown; the filename's date was not treated as verified authorship or video chronology.
