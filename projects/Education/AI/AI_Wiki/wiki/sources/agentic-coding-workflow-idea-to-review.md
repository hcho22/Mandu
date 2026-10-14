---
type: source
title: "Agentic Coding Workflow: From Idea to Code Review"
source-type: guidebook
author: "Uncredited compiler; merges two John talk summaries with the Kun reconstruction guide"
url: local
date-ingested: 2026-10-14
date-created: unknown
tags: [agentic-engineering, workflow, code-review, feature-flags, loops, goals, claude-code, codex]
---

# Agentic Coding Workflow: From Idea to Code Review

A supplied beginner playbook that merges [[john-meta-engineer]]'s two talks ([[agentic-code-review-strategies]], [[stop-prompting-design-loops-and-goals]]) with the Kun reconstruction ([[kun-agentic-app-development-workflow]]) into one 11-phase pipeline from raw idea to reviewed, merged code, plus a short bridge to launch.
Its framing: Kun works from the front (intent, parallel research, visual architecture review, contracts, an orchestrator, a validation pipeline), John works from the back (gates, proof in the PR, a reviewer that did not write the code, review depth by blast radius, long goals with exit criteria), and the two reach the same conclusion.
Its one-line thesis: spend your attention on intent, boundaries, evidence, and risk; let agents do research, building, testing, and first-pass review; read code in proportion to what it could break.

It adds **no new primary evidence**.
Its value is the merge itself, a set of editor-authored structures, and a dated check of the tool commands against current documentation (2026-10-12).

## The pipeline

| # | Phase | Main output | Exit gate |
|---|---|---|---|
| 0 | Set up the workbench | Protected repo, short `AGENTS.md`, CI, a flag helper, secrets hygiene, first skills | An empty PR triggers CI; a placeholder flag switches |
| 1 | Capture intent | One-page product brief from an "intent dump" | A stranger could build from it |
| 2 | Research in parallel | Market and technical research, decision with rejected options | An option chosen with reasons and expected monthly cost |
| 3 | Architecture and the tree | Architecture docs with every component labeled trunk or leaf | You can explain every box and arrow |
| 4 | Prototype the experience | Clickable wireframes, design system, saved reference screens | Journeys approved; references readable by agents |
| 5 | Write the contract | PRD, 3-7 Given/When/Then scenarios with evidence, risk tiers, gating plan | Each scenario's result shows in the agent's own output |
| 6 | Plan the build | Atomic task cards, thin end-to-end slice first | Every task has tier, gate, criteria, required proof |
| 7 | Build with goals and loops | One branch per task in its own worktree | Goal condition met, proof visible |
| 8 | Prove it and open the PR | Evidence package, updated docs, short PR | Evidence matches scenarios; PR shorter than the diff |
| 9 | Review | Approved PR merged with its gate off | Review done at the tier's depth |
| 10 | Merge is not launch | Audited, canaried, released feature | Canary clean; gate opened or feature removed |

## Key claims and editor structures

Tags follow the source: **[John]** and **[Kun]** are attributed practices (Kun's second-hand via the reconstruction), **[Guide]** is the reconstruction's own adaptation, and **[Editor]** is this compiler's addition.

- **Risk and gating are decided while planning, not during review** [Editor]. Every component gets a trunk or leaf label in Phase 3 and a risk tier in Phase 5, so review depth is known before code exists ([[risk-based-agent-governance]], [[feature-gating-from-day-one]]).
- **Three risk tiers** [Editor, merging John's blast radius with Kun's per-project policies]: Low (leaf UI, gated experiments, internal tools; AI review plus a human skim), Medium (customer-facing features, important data flows; a human reads the key files), High (auth, payments, permissions, migrations, secrets, infrastructure, shared state, one-way doors; security review, every line read, a rollback plan).
- **One definition of "done," reused three times** [Editor]: the Phase 5 acceptance scenarios become the agent's exit criterion in Phase 7, the evidence checklist in Phase 8, and the reviewer's yardstick in Phase 9 ([[define-the-end-to-end-gate]]).
- **The builder never grades its own work** [Editor]: a fresh-context agent reviews before the PR opens, an AI reviewer checks it on GitHub, and a human reviews at the tier's depth ([[fresh-context-review]]).
- **Review as six ordered layers** [John, ordered by Editor]: triage with five safety questions (adds "is it a one-way door, such as a migration, deletion, public API change, or external send?"), static checks, fresh-context AI review, a PR reviewer bot, a babysitting loop, then human review by tier. A "leaf" task that ends up editing a shared reducer is re-triaged as trunk.
- **Bounded autonomy first** [Editor]: goals capped at 10-20 turns, on Low-tier tasks, lengthened as tests and evidence get stronger; John's 22-hour run is the far end, not the starting point ([[phased-autonomy]]).
- **Scale is deferred** [Guide]: one lead agent and one or two workers; Kun's fleet features (Second Mates, dispatch policy, Bearings and Ahoy digests, Herder) only once coordination itself is the bottleneck.
- **The babysitter fixes comments, it does not settle disagreements** [Editor]. Comments asking for a design or scope change go to the human, not into an endless fix cycle ([[adversarial-code-review]]).
- **Proof must come from the real app** [Kun + John]: run the real end-to-end scenario against real integrations with one failure path; "do not claim success from unit tests or a passing build alone" ([[proof-in-the-pr]]).
- **Templates** [Editor]: an `AGENTS.md` skeleton with an "escalate only when" list, a task card (scope, trunk or leaf, tier, gate, acceptance, proof, escalate-if), a `/goal` condition with constraints and a turn cap, and a PR template with Risk, Evidence, and Reviewer-focus sections.

## Where John and Kun differ

The source's own comparison, condensed.

| Topic | John | Kun | The playbook's resolution [Editor] |
|---|---|---|---|
| Reading code | Reads a lot, maybe more than before; depth follows trunk versus leaf | Reading every diff makes you the bottleneck | Evidence first for everyone; humans read trunk and High-tier code in full |
| Where validation runs | Proof in the PR, reviewer bots, a babysitting loop | A pre-PR pipeline (No Mistakes) with fresh-context review | Both |
| Autonomy | Long goal runs with strong exit criteria | An orchestrator dispatches workers and escalates only what needs a human | Start bounded, lengthen with maturity |
| Environments | Not discussed | One production environment for a tiny MVP | Add staging or preview before real user data |
| Side-project code quality | Relaxed | Not discussed | Production standards always |

## Tool facts, as checked by the compiler on 2026-10-12

Time-sensitive; recorded on [[claude-code]] and [[codex]] with this as-of date.

- **[[claude-code]] `/goal <condition>`** keeps working turn after turn until a separate evaluator model judges the condition met or impossible. The evaluator reads only what Claude has shown in the conversation, so the condition should name a visible check ("`npm test` exits 0"); add a turn cap; `/goal clear` stops it.
- **Claude Code `/loop`** reruns a prompt on an interval (`/loop 1h <prompt>`), lets Claude pace and end it when no interval is given, and in bare form tends the current branch's PR. Loops run only while the session is open and expire after 7 days; durable automation belongs in cloud routines (`/schedule`) or GitHub Actions.
- **Claude Code `/code-review`** (alias `/review`) reviews a branch, PR, or ref range in a background subagent with its own context; `--fix` applies findings, `--comment` posts them, `ultra` escalates to a deeper cloud review. `/security-review` is the security-focused variant.
- **Claude Code Review** (managed GitHub review) is a research preview for Team and Enterprise plans, triggered on PR open, on push, or by `@claude review`, tuned by a `REVIEW.md`, averaging $15-25 per review, and never blocking a merge on its own.
- **[[codex]] on GitHub** is the `chatgpt-codex-connector` bot: automatic reviews per repository, `@codex review` (optionally with a focus), and `@codex address that feedback`; review rules go in `AGENTS.md`.
- **Codex CLI `/goal`** exists behind a feature flag per third-party coverage only (said to arrive in v0.128).
- **No Mistakes** is public at `github.com/kunchenguid/no-mistakes`: `no-mistakes init` sets up a local gate remote, and `git push no-mistakes` runs review, tests, docs, and lint in a disposable worktree, opening a PR only once all pass.

## Contradictions resolved and flagged

- **Resolved: "loops and goals are interchangeable."** John's characterization ([[stop-prompting-design-loops-and-goals]]) does not match the documented Claude Code behavior: `/goal` continues until a condition holds, `/loop` reruns on a time interval. The documentation agrees with [[tharic]]'s distinction on [[verification-signal-picks-the-mechanism]]. John's statement stays recorded as his view.
- **Resolved: the "goals" used for hourly PR babysitting** ([[agentic-code-review-strategies]], flagged `[?]`) is interval work, which in Claude Code is `/loop`. John did not name his tool, and Codex was also in his setup, so this is the likely mapping, not a confirmed one.
- **Resolved: `/code-review` and the "ChatGPT Codex Connector"** are real names, per the compiler's check.
- **Still open: how much code to read.** The playbook does not settle John versus Kun; it picks a policy (evidence first, full reads for trunk and High tier). That is a recommendation, not evidence ([[get-out-of-the-loop]]).

## Evidence limits

- **A third-order source.** John's material arrives as two edited summaries of his talks, and Kun's as a third-party reconstruction of four videos; this playbook is built from those. It cannot corroborate either of them, and the wiki counts it as one cataloged source with zero new independent voices.
- The compiler is uncredited and the document undated; its tool checks are dated 2026-10-12 by its own statement.
- Many structures are explicitly editor additions: branch protection, the merged risk-tier table, moving trunk/leaf mapping into planning, Given/When/Then scenarios, all four templates, turn caps, the staging recommendation, the `REVIEW.md` tip, the human-review checklist, the cheat sheet, and per-phase gates.
- Codex details come from public GitHub bot messages and third-party articles, not OpenAI's documentation.
- Kun's own tools (Lavish, Treehouse, Herder, First Mate and Second Mates, Bearings and Ahoy) are marked "not verified" by the compiler.
- Products change quickly; the source itself says to confirm commands with `/help`.

Mandu's verification note (2026-10-14): the Claude Code build Mandu runs lists a `/code-review` skill that takes a branch, PR, or path target with `--fix`, `--comment`, and an `ultra` level, and a `/loop` skill that self-paces when the interval is omitted, which is consistent with the compiler's account.
The `/review` alias and the `/goal` evaluator behavior were not checked here.

## Connections

- [[risk-based-agent-governance]] - the three-tier table and re-triage of a "leaf" that edits shared state.
- [[define-the-end-to-end-gate]] - one set of acceptance scenarios reused as exit criterion, evidence checklist, and review yardstick.
- [[proof-in-the-pr]] - the evidence package as a Phase 8 gate.
- [[feature-gating-from-day-one]] - the gating plan written into the contract; merge with the gate off.
- [[phased-autonomy]] - bounded goals and the five-stage scaling ladder.
- [[verification-signal-picks-the-mechanism]] - documented `/goal` and `/loop` behavior resolves the interchangeability claim.
- [[fresh-context-review]] and [[adversarial-code-review]] - layered independent review, and the babysitter's escalation rule.
- [[merge-ready-vs-launch-ready]] - Phase 10 as its own gated phase.
- [[kun]], [[john-meta-engineer]], [[claude-code]], and [[codex]].
- [[agentic-engineering]] - the area's build-practice spine as a single procedure.

## Possible project applications

These are Mandu's observations and suggestions, not claims that the projects already follow the playbook.

- **hcho already runs much of Kun's stack.** First Mate is his firstmate home, Lavish renders his Immerse look boards, Treehouse holds the Immerse worktrees, and the No Mistakes skill is installed in his Claude Code. So the tools the compiler could not verify exist in his environment (presence observed, behavior not tested here).
- **Mandu already follows the shared-rules tip.** Kun's advice to share one set of global rules across agent tools, for example by symlinking, is what Mandu's `AGENTS.md` setup does: `CLAUDE.md` imports it and Codex's `.agents/skills/` entries link to the canonical skill copies.
- **hcho's own global instruction matches Kun's cost rule** nearly word for word: do not over-weight development cost; choose on quality, simplicity, robustness, scalability, and maintainability.
- [[projects/RepToday/README|Rep Today]]: its 73-check device checklist already plays the role of Phase 5 scenarios with recorded evidence. Its consequential areas (account deletion, health data, sync) are High tier in the playbook's terms, because their effects on real users' data cannot be switched off afterward; that argues for a full human read and a recovery plan on any change there, whatever the tests say.

## Source

- Title: "Agentic Coding Workflow: From Idea to Code Review," subtitled "A beginner-friendly, production-grade playbook that combines John's two talks with Kun's app-development workflow."
- Author: uncredited compiler.
- URL: local; the source lists the documentation pages and repositories it checked on 2026-10-12, including `code.claude.com` pages for `/goal`, `/loop`, code review, and worktrees, the `kunchenguid/no-mistakes` repository, and two third-party Codex articles.
- Built from: [[agentic-code-review-strategies]], [[stop-prompting-design-loops-and-goals]], and [[kun-agentic-app-development-workflow]].
- Raw: [[projects/Education/AI/AI_Wiki/raw/agentic-coding-workflow-idea-to-review|Preserved Markdown playbook]] (saved verbatim in `raw/`, immutable).
- Original inbox filename: `101226_agentic-coding-workflow.md`.
- Ingested: 2026-10-14, the third of three sources hcho asked to file in one batch, filed last so it could link the other two.
