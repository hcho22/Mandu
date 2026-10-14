# Agentic Coding Workflow: From Idea to Code Review

*A beginner-friendly, production-grade playbook that combines John's two talks with Kun's app-development workflow*

| | |
|---|---|
| **Sources** | **John** (senior staff software engineer at Meta, self-described): summaries of *Agentic Code Review Strategies* and *Stop Prompting, Start Designing Loops and Goals*. **Kun**: *Agentic App Development Workflow*, a beginner reconstruction of four of his videos. |
| **Audience** | Beginner developers who want to ship production software with AI coding agents |
| **Scope** | From a raw idea to reviewed, merged code, plus a short bridge to launch |
| **Organization** | Procedural: 11 phases (0–10). Each phase ends with a gate to pass before moving on. |
| **Tool facts** | Claude Code, Codex and No Mistakes details were checked against current docs and repos on 2026-10-12 (see [Appendix A](#appendix-a-term-verification-and-corrections)) |

---

## Overview

The two sources reach the same conclusion from opposite ends.

- **Kun works from the front.** He captures intent, runs research in parallel and reviews architecture visually before any code exists. Then he writes contracts, has an orchestrator agent dispatch isolated workers, and sends every change through an independent validation pipeline.
- **John works from the back.** He gates every feature and makes agents prove their work inside the PR. Reviews come from an agent that didn't write the code, and human review depth follows the change's blast radius. His second talk adds autonomy: long-running loops and goals that stop on a verifiable exit criterion.

This workflow joins them into one pipeline. The idea underneath it:

> **Spend your attention on intent, boundaries, evidence and risk. Let agents do the research, building, testing and first-pass review. Read code in proportion to what it could break.**

**What was optimized** [Editor]

- **Risk and gating are decided while planning, not during review.** Every task is tagged trunk or leaf and Low, Medium or High before any code is written, so you know its review depth in advance.
- **One definition of "done" is reused three times.** The acceptance scenarios from Phase 5 become the agent's exit criterion in Phase 7, the evidence checklist in Phase 8 and the reviewer's yardstick in Phase 9.
- **The builder never grades its own work.** A fresh-context agent reviews before the PR opens, an AI reviewer checks it on GitHub, and a human reviews at the depth the risk tier requires.
- **Scale is deferred.** You start with one lead agent and one or two workers. Kun's fleet features come later, once coordination is your real bottleneck.

**Key takeaways**

- Don't code until you have a brief, an architecture you can explain box by box, and written acceptance scenarios.
- Gate everything. Being able to switch a feature off is what lets you review less of it.
- Give agents goals with a verifiable exit criterion, plus the tools, context and checks to finish without you.
- "Done" means the real app passes a real end-to-end scenario, with the evidence attached to the PR.
- Have an agent that didn't write the code review it. Let linters handle style.
- Read trunk code deeply and skim leaf code. As a beginner, read everything rated High no matter what.
- Merge-ready isn't launch-ready. Budget time for an audit and a gradual rollout.

---

## How to Use This Document

### Source Tags

Every practice carries a tag so you can see where it came from.

| Tag | Meaning |
|---|---|
| **[John]** | From John's talks |
| **[Kun]** | Kun's own practice, as reported in the reconstruction guide |
| **[Guide]** | The reconstruction guide's own beginner adaptation, not something Kun said he does |
| **[Editor]** | Added, merged or reordered in this document; not in either source |

### Callout Legend

| Callout | Meaning |
|---|---|
| 💡 **Tip** | Specific, actionable advice or a trick |
| 🔧 **Tool** | A named tool, command, product or feature |
| 📏 **General Rule** | A principle presented as broadly applicable that also matches standard engineering practice |
| 🗣️ **Speaker Opinion** | A personal view or practice of John or Kun, framed as their own |
| ⚠️ **Caution** | A pitfall, risk or warning |

`[?]` marks an uncertain term carried over from the source summaries. See [Appendix A](#appendix-a-term-verification-and-corrections).

### Phase Layout

Every phase has the same parts:

- **Goal**: what the phase produces
- **You / Agents**: who does what
- **Steps**: the work, in order
- **Outputs**: files that land in the repo
- **Exit gate**: a checklist. Don't start the next phase until every box is checked.

---

## Contents

- [Overview](#overview)
- [How to Use This Document](#how-to-use-this-document)
- [The Workflow at a Glance](#the-workflow-at-a-glance)
- [Phase 0: Set Up the Workbench](#phase-0-set-up-the-workbench)
- [Phase 1: Capture Intent](#phase-1-capture-intent)
- [Phase 2: Research in Parallel](#phase-2-research-in-parallel)
- [Phase 3: Decide the Architecture and Map the Tree](#phase-3-decide-the-architecture-and-map-the-tree)
- [Phase 4: Prototype the Experience](#phase-4-prototype-the-experience)
- [Phase 5: Write the Contract](#phase-5-write-the-contract)
- [Phase 6: Plan the Build](#phase-6-plan-the-build)
- [Phase 7: Build with Goals and Loops](#phase-7-build-with-goals-and-loops)
- [Phase 8: Prove It and Open the PR](#phase-8-prove-it-and-open-the-pr)
- [Phase 9: Review](#phase-9-review)
- [Phase 10: Merge Is Not Launch](#phase-10-merge-is-not-launch)
- [Cheat Sheet: One Feature, End to End](#cheat-sheet-one-feature-end-to-end)
- [Scaling Up Later](#scaling-up-later)
- [Where John and Kun Differ](#where-john-and-kun-differ)
- [Prompt Library](#prompt-library)
- [Templates](#templates)
- [Tools and Commands Reference](#tools-and-commands-reference)
- [Appendix A: Term Verification and Corrections](#appendix-a-term-verification-and-corrections)
- [Appendix B: Editorial Notes](#appendix-b-editorial-notes)
- [Sources](#sources)

---

## The Workflow at a Glance

<!-- pipeline -->
```text
 0 SET UP -> 1 INTENT -> 2 RESEARCH -> 3 ARCHITECTURE -> 4 PROTOTYPE -> 5 CONTRACT
                                                                            |
 10 LAUNCH <- 9 REVIEW <- 8 PROVE <---------- 7 BUILD <---------- 6 PLAN <--+
```

| # | Phase | You decide | Agents do | Main output | Gate |
|---|---|---|---|---|---|
| 0 | Set up | Tools and rules | Scaffold config and CI | Repo, `AGENTS.md`, CI, flags | CI runs on an empty PR |
| 1 | Intent | What and why | Organize, challenge | `PRODUCT_BRIEF.md` | A stranger could build from it |
| 2 | Research | Which option | Market and technical research | Two research reports | Option chosen, with reasons |
| 3 | Architecture | Boundaries | Diagrams, reviews | `ARCHITECTURE.md` with trunk/leaf map | You can explain every box |
| 4 | Prototype | The experience | Wireframes, design system | Approved reference screens | Journeys approved |
| 5 | Contract | "Done" and risk | Draft PRD and scenarios | `PRODUCT.md`, `TESTING.md`, risk and gate plan | Scenarios are checkable |
| 6 | Plan | Order | Slice into tasks | `TASKS.md` | Every task has tier, gate, criteria |
| 7 | Build | Escalations only | Implement, self-validate | Branches in worktrees | Goal condition met |
| 8 | Prove | Spot-check | Evidence, PR | PR with evidence | Evidence matches scenarios |
| 9 | Review | Merge or not | Static checks, AI review, babysitting | Approved PR | Tier's review done |
| 10 | Launch | Rollout | Audit, canary | Released feature | Canary clean, gate opened |

### Beginner Minimum vs Production Build

| Practice | Beginner minimum | Production build |
|---|---|---|
| Agents | One lead and 1–2 workers | Lead, workers and a separate validator; Second Mates later |
| Instructions | One short `AGENTS.md` | Plus skills, path-scoped rules and review rules |
| CI | Tests and lint | Plus type check, security scan, end-to-end tests, branch protection |
| Feature gates | A Boolean flag in config | A flag platform with per-user rollout (e.g. LaunchDarkly) |
| Review | `/code-review` and you | Pre-PR gate, GitHub AI reviewer, human review by tier |
| Environments | Local and production (Kun's MVP) | Plus a staging or preview environment before real user data [Editor] |
| Rollout | Flip the flag | Canary or A/B test with alerts |

---

## Phase 0: Set Up the Workbench

**Goal:** A repository where agents can work safely and every change gets checked automatically.

**You:** pick tools and write the rules. **Agents:** scaffold configs and CI.

**Steps**

1. **Create the repo and protect `main`.** Require a pull request and passing CI before anything merges. [Editor]
2. **Pick one agent harness**, such as Claude Code or Codex, and learn it before adding a second. [Guide]
3. **Write a short instruction file** (`AGENTS.md`). It loads in every session, so keep it small and put situational know-how into skills instead (template: [AGENTS.md skeleton](#agentsmd-skeleton)). It should cover: [Kun]
    - a map of the repo
    - build, test and lint commands
    - conventions
    - a "never do" list
    - when to escalate to you
4. **Wire up the automatic checks.** Run a formatter, linter, type checker and unit tests in CI on every PR. Later, these replace human comments about style. [John]
5. **Add a feature-flag mechanism.** A Boolean flag in config is enough to start. Move to a flag platform when you need per-user rollouts. [John]
6. **Set up secrets hygiene.** [Kun]
    - Put `.env` in `.gitignore`.
    - Use a secret manager for production credentials.
    - Give agents minimum-scope keys.
    - Require your confirmation before destructive or production actions.
7. **Prepare isolation for parallel work**, with one git worktree per agent. [Kun]
8. **Create your first three skills** (reusable instruction files): [Editor, built from John's practices]
    - `prove-it`: the evidence package from Phase 8
    - `pr-template`: the PR format from Phase 8
    - `no-useless-tests`: rules for meaningful tests, from John's side tip
9. **Make the environment reproducible.** This step is optional for beginners. Kun version-controls his whole Mac setup with Nix, Nix-Darwin and Home Manager, so agents always see the same tools. [Kun]

**Outputs:** repo, `AGENTS.md`, CI workflow, flag helper, `.gitignore`, skills folder.

**Exit gate**

- [ ] `main` is protected; merging needs a PR and green CI
- [ ] An empty test PR triggers lint, type check and tests in CI
- [ ] `AGENTS.md` lists the build and test commands and the escalation rule
- [ ] No secrets are in the repo, and `.env` is ignored
- [ ] You can switch a placeholder feature on and off with a flag

> 🔧 **Tool** [Editor, verified]: Claude Code reads `CLAUDE.md`, and current versions also support `AGENTS.md`; its memory docs explain when each loads. Skills live in `.claude/skills/<name>/SKILL.md` and subagents in `.claude/agents/`. Hooks can auto-format after edits or block edits to protected files. Codex reads `AGENTS.md`.

> 💡 **Tip** [Kun]: Keep the always-loaded instruction file minimal. Move anything that only matters sometimes, such as deployment steps or migration rules, into a skill so it loads only when needed.

> 💡 **Tip** [Kun]: Share one set of global rules across all your agent tools, for example by symlinking the same file into each tool's expected location. Then switching models doesn't mean rebuilding your process.

> 📏 **General Rule** [Kun]: Never commit secrets. Configuration belongs in Git; credentials don't.

> ⚠️ **Caution** [Guide]: Don't spend weeks customizing your terminal before you have a product. The minimum above is enough to start.

---

## Phase 1: Capture Intent

**Goal:** Turn the idea in your head into a one-page product brief before any code exists.

**You:** explain the idea in plain language, including what you're unsure about. **Lead agent:** organize it, find contradictions and list open questions.

**Steps**

1. **Start one lead session** and tell it not to write code. Kun calls his orchestrator **First Mate**. [Kun]
2. **Do an "intent dump."** Cover who it's for, their problem, what success feels like, what the app must never do, what data must survive, platforms, privacy concerns and unknowns. Don't worry about terminology. [Kun]
3. **Have the agent organize and challenge it.** It turns the dump into a brief and flags anything contradictory or unnecessary ([Prompt A](#prompt-a-kickoff)). [Guide]
4. **Answer its questions**, then approve the brief.

**Output:** `docs/PRODUCT_BRIEF.md`

**Exit gate**

- [ ] Users and their problem are named
- [ ] Goals and **non-goals** are listed
- [ ] Each main user journey is described in a sentence
- [ ] Data that must be stored is listed
- [ ] Unknowns and open decisions are listed
- [ ] A stranger could build from this brief

> 🗣️ **Speaker Opinion** [Kun]: He starts with a long, unstructured explanation and lets the agent do the organizing, instead of opening with database tables or "build me the app."

> 💡 **Tip** [Editor]: If typing slows you down, dictate the intent dump. Rambling is fine. Leaving things out is what hurts.

---

## Phase 2: Research in Parallel

**Goal:** Know whether to build this and which architecture fits, before committing to anything.

**You:** challenge assumptions and decide. **Agents:** two separate researchers working at the same time.

**Steps**

1. **Launch a market researcher** ([Prompt B](#prompt-b-research)). It should find existing products, what they do well, the gap, ideas worth borrowing, and whether building is justified. [Kun]
2. **Launch a technical researcher at the same time.** It compares 2–4 viable architectures on frontend, backend, database, auth, hosting, cost, offline behavior, security, deployment, backup and testing. Ask for options, not code. [Kun]
3. **Challenge the recommendation.** [Kun]
    - Kun rejected a hosted-backend suggestion on cost and had the agent compare a low-cost self-hosted VPS.
    - Ask: Is it assuming scale we don't have? Is a managed service worth its price? Is it inventing requirements?
4. **Record the decision and the rejected options**, with reasons.

**Outputs:** `docs/research/MARKET_RESEARCH.md`, `docs/research/TECHNICAL_OPTIONS.md`, and the decision noted in the brief.

**Exit gate**

- [ ] You know at least two alternatives and why you're building anyway
- [ ] One architecture is chosen, with reasons and an expected monthly cost
- [ ] Rejected options and the reasons are written down

> 📏 **General Rule** [Kun]: Agents propose; you decide. A recommendation is a starting point, not a verdict.

> 🗣️ **Speaker Opinion** [Kun]: One of his global preferences is not to over-weight development cost when choosing a design. Agents make robust solutions cheap to build, so choose on quality, simplicity, robustness, scalability and maintainability. That isn't a license to pick the most complex option.

> 💡 **Tip** [John]: Look for harnesses that turn one prompt into a lot of work, or "fewer tokens in, more tokens out." His example is ChatGPT Deep Research: the same question produces far more output because of the tooling behind it.

---

## Phase 3: Decide the Architecture and Map the Tree

**Goal:** Boundaries you can explain in plain English, and a map of which parts are dangerous to change.

**You:** review diagrams, cut premature complexity and approve. **Agent:** produce diagrams and decision cards.

**Steps**

1. **Ask for a visual architecture review**, not a long memo ([Prompt C](#prompt-c-architecture-review-and-tree-map)). It should include: [Kun]
    - system, data-flow and auth-flow diagrams
    - the data model and API responsibilities
    - the source of truth for each data type
    - deployment and failure modes
    - open decisions
2. **Apply the architecture rules** below. [Kun]
3. **Run an anti-overengineering pass** ([Prompt D](#prompt-d-anti-overengineering)). Remove anything premature, duplicated or aimed at problems you don't have. Keep security, data-integrity and maintainability boundaries. Kun cut auditing and export ideas this way. [Kun]
4. **Draw the tree.** Label every component trunk or leaf. [John; moved to planning by Editor]
    - **Trunk:** entry points, shared state, auth, the data layer, payments, infrastructure, and anything with many dependents.
    - **Leaf:** isolated screens, one-off components, and new endpoints behind a gate.
5. **Save the decisions to the repo.**

**Architecture rules** [Kun, from his wallet-app example]

1. **Separate presentation from authority.** The UI collects intent. The backend enforces identity, permissions, business rules and durable state.
2. **Model the business, not the screens.** `Wallet`, `Loan` and `LedgerEntry` outlive any screen.
3. **Expose domain actions, not generic database writes.** Use `POST /wallet/deposit`, not `POST /db/updateRow`.
4. **Name a source of truth and an owner for every piece of data.**
5. **Treat authentication and authorization separately.** Authentication asks who you are; authorization asks what you may do.
6. **Define entities and relationships before agents create tables.**
7. **Keep the MVP simple but real.** Use fewer moving parts, never fewer safety boundaries.

**Outputs:** `docs/ARCHITECTURE.md` (including the trunk/leaf map), `docs/DATA_MODEL.md`, `docs/API.md`, `docs/AUTH.md`.

**Exit gate**

- [ ] You can explain every box and arrow in plain English
- [ ] Every data type has a source of truth and an owner
- [ ] Roles and their permissions are written down
- [ ] Every component is labeled trunk or leaf
- [ ] Premature features are cut and listed as deferred

> 📏 **General Rule** [John]: Review effort follows blast radius. The trunk/leaf map you draw now decides how hard each future change gets reviewed.

> 🔧 **Tool** [Kun]: Kun reviews plans in **Lavish**, which turns an agent's plan into an interactive HTML page he can annotate. Without it, ask the agent for one HTML page with Mermaid diagrams and decision cards. [Editor]

> 💡 **Tip** [Kun]: Run the architecture review again once code exists. Kun audits what agents actually built (API boundaries, auth flow, database shape), not only what they planned.

> ⚠️ **Caution** [Kun]: If you can't explain what every box does, don't start implementing.

---

## Phase 4: Prototype the Experience

**Goal:** Approved screens and flows that agents can later check their work against.

**You:** click through and give concrete feedback. **Agent:** build clickable wireframes, then a design system.

**Steps**

1. **Ask for clickable HTML wireframes** of the key journeys, and reject text descriptions. Cover: [Kun]
    - onboarding and sign-in
    - the home screen and the primary action
    - settings
    - empty and error states
    - any admin or parent mode
2. **Click through and give feedback** until the flow makes sense. Is the primary action obvious? What happens with no data, or when something fails? [Guide]
3. **Create a design system** (colors, type, components, icon direction) before writing production UI code. [Kun]
4. **Save reference screens.** They become exit criteria, because the agent can compare screenshots of its build against them. [John]

**Outputs:** prototype, approved journey list, design system, and reference screens in `docs/design/`.

**Exit gate**

- [ ] Each MVP journey has an approved screen flow
- [ ] Empty, loading and error states exist
- [ ] Reference screens are saved where agents can read them

> 💡 **Tip** [John]: Generate design screens before building. AI is good at comparing screenshots, so the screens double as a test the agent can run on itself.

> 🔧 **Tool** [John]: Figma specs, or the design tool John calls Pen (formerly Pencil) [?], supplied the screens that served as exit criteria in his roughly 22-hour build.

> 📏 **General Rule** [Guide]: Prototype for behavior, not polish. Polish comes in Phase 10.

---

## Phase 5: Write the Contract

**Goal:** Written definitions of the MVP, of "done," of risk, and of how each part can be switched off.

**You:** approve scope, scenarios and risk tiers. **Agent:** draft the documents.

**Steps**

1. **Write the PRD** (`docs/PRODUCT.md`). Include: [Kun; section list from Guide]
    - problem, users, goals and non-goals
    - user journeys and functional requirements
    - stored data, roles and permissions
    - technical constraints
    - the MVP definition, deferred features and acceptance criteria
2. **Write the acceptance scenarios** (`docs/TESTING.md`). Write 3–7 end-to-end scenarios in Given/When/Then form, each listing the evidence that proves it. Include at least one failure path. These are your validation criteria, defined before building. [John + Kun]
3. **Assign a risk tier** to each component or feature area, using the table below. [Editor, merging John's blast radius with Kun's per-project policies]
4. **Write the gating plan.** [John]
    - Name the flag that covers each feature.
    - Keep leaf work separate from integration work.
    - Give each integration seam its own gate.
5. **Freeze scope.** Anything not in the MVP goes on the deferred list.

**Risk tiers**

| Tier | Typical areas | Rollback | Review depth in Phase 9 |
|---|---|---|---|
| **Low** | Leaf UI, gated experiments, internal tools, docs | Flag off or revert | AI review and a human skim |
| **Medium** | Customer-facing features, important data flows, auth-adjacent UI | Flag off | AI review, and a human reads the key files |
| **High** | Auth, payments, permissions, migrations, secrets, infrastructure, shared state, one-way doors | May be impossible | AI and security review, a human reads every line, rollback plan |

**Example scenario** (based on Kun's MVP gate)

```gherkin
Scenario S-01: Saved data survives sign-out (MVP gate)
  Given a new parent account signed in through the real auth provider
  When they add a child and deposit 10 into the child's wallet
  And they sign out, then sign back in
  Then the child's balance shows 10
  And a second account cannot read that wallet
Evidence: simulator recording, API response log, database row
```

**Outputs:** `docs/PRODUCT.md`, `docs/TESTING.md`, and a risk and gating plan (in `docs/ARCHITECTURE.md` or a separate `docs/RISK.md`).

**Exit gate**

- [ ] Each scenario's result can be shown in the agent's own output (test result, recording, log)
- [ ] At least one failure path is covered
- [ ] Every component has a tier, and every feature has a gate
- [ ] The deferred list exists

> 📏 **General Rule** [John]: Define validation criteria before building, so the agent and you have something objective to check against.

> 📏 **General Rule** [John]: Gate everything, and give integration layers their own gates. Being able to roll back is what makes lighter review safe.

> 💡 **Tip** [Editor]: Write each scenario so its proof appears in the agent's own output. Claude Code's `/goal` evaluator, for example, judges only what shows up in the conversation; it doesn't run checks itself.

> 🗣️ **Speaker Opinion** [Kun]: For a tiny MVP he skipped dev, staging and production tiers and ran a single production environment. [Editor] For a production build that will hold real user, paid or sensitive data, add a staging or preview environment before launch.

---

## Phase 6: Plan the Build

**Goal:** A queue of small, gated tasks that can each be verified on their own, in a safe order.

**You:** approve the order and what runs in parallel. **Agent:** slice the work into tasks.

**Steps**

1. **Build the thinnest end-to-end slice first.** For example: sign in → create one domain object → persist it → fetch it → display it. This exposes architecture mistakes early. [Guide]
2. **Then expand in vertical slices.** Each feature goes requirement → UI → API and domain logic → database → tests → evidence. Don't build every screen first and "connect the backend later." [Guide]
3. **Make each task atomic** and fill in a [task card](#task-card). [John]
4. **Order tasks by dependency.** Contracts (data model, API, auth) come first. After that, three tracks can run in parallel: backend, frontend, and integration and testing. [Kun]
5. **Mark which tasks can run in parallel:** only tasks whose contracts are already written and that touch different areas.

**Output:** `docs/TASKS.md`, or issues in your tracker.

**Exit gate**

- [ ] The first task is the thin end-to-end slice
- [ ] Every task has a scope, trunk or leaf label, tier, gate, acceptance criteria and required proof
- [ ] Parallel tasks don't touch the same files or contracts

> 📏 **General Rule** [Kun]: Run work in parallel only after the contracts are clear. Otherwise parallelism just produces incompatible implementations faster.

> 💡 **Tip** [Editor]: Size each task so its diff stays reviewable for its tier: small for trunk changes, larger for gated leaf work.

---

## Phase 7: Build with Goals and Loops

**Goal:** Agents implement each task until its exit criterion is met, with little hand-holding.

**You:** answer escalations and watch outcomes, not keystrokes. **Agents:** implement, run checks, test their own work and push at checkpoints.

**Steps**

1. **Isolate each worker** in its own branch and worktree. [Kun]
2. **Give each worker three ingredients.** [John]
    - **Tooling:** MCP or CLI access to everything it needs (test runner, simulator, browser, deploy CLI), so it doesn't stop to ask.
    - **Context:** the docs from Phases 3–5, plus anything else it can query through a CLI or a file.
    - **Exit criteria:** the task's acceptance criteria and reference screens.
3. **Set a goal with a verifiable condition and safety clauses** (see [Goal condition](#goal-condition)): [John + Kun + Editor]
    - Push at checkpoints.
    - Archive files; never delete them.
    - Don't change other areas or contracts; escalate instead.
    - Stop after N turns.
4. **Let it validate its own work.** It runs tests, drives the simulator or browser, works through edge cases one by one, and compares screenshots with the reference screens. [John]
5. **Escalate only what needs a human.** Kun's instruction to his agent amounts to: don't ask me unless there's something only I can do. [Kun]
6. **Route work to the right model** if you use several. Use stronger models for architecture and hard debugging, and cheaper ones for simple fixes. [Kun]
7. **Keep the number of active workers small** enough that you know what each one is doing. [Guide]

**Output:** one branch per task, each in its own worktree, with commits pushed at checkpoints.

**Exit gate**

- [ ] The goal condition is met, and you can see the proof in the agent's output
- [ ] No escalations are waiting on you
- [ ] The branch is pushed and has no changes outside the task's scope

> 🔧 **Tool** [Editor, verified]: **Claude Code** `/goal <condition>` keeps working turn after turn until a separate evaluator model judges the condition met or impossible. `/goal` shows status and `/goal clear` stops it.
>
> - The evaluator only reads what Claude has shown in the conversation, so state the check, e.g. "`npm test` exits 0."
> - Add a clause like "or stop after 20 turns" to bound the run.
> - Run it in auto mode so each turn doesn't wait on tool approvals.
> - `claude --worktree <name>` starts a session in its own worktree under `.claude/worktrees/`.

> 🔧 **Tool** [Editor]: **Codex CLI** has its own `/goal`, with `pause`, `resume` and `clear`. Third-party coverage says it arrived in v0.128 behind a feature flag (`codex features enable goals`). Check your version.

> 📏 **General Rule** [John]: A good goal has an exit criterion the agent can verify with high confidence, such as tests, evals or design specs.

> 💡 **Tip** [John]: Before a long run, work out the roadblocks (logins, deploy access, test data) and give the agent the tools to get past them.

> 🗣️ **Speaker Opinion** [John]: He had one goal running for about 22 hours. It worked only because the tools, context and exit criteria were already in place; copied on its own, the same goal "probably won't work."

> 🗣️ **Speaker Opinion** [John]: In his estimate, most people can actively handle only 2–3 agents at once. If your screen is a wall of terminals, "chances are you're probably doing it wrong." Design loops instead of babysitting.

> ⚠️ **Caution** [John]: His relaxed attitude to code quality was for an internal side project. At work he uses goals at a smaller scale.

> ⚠️ **Caution** [Editor]: Start with bounded autonomy: goals capped at 10–20 turns, on Low-tier tasks. Lengthen the runs as your tests and evidence get stronger.

---

## Phase 8: Prove It and Open the PR

**Goal:** A PR that shows the change works, so reviewers read the evidence first and the code second.

**You:** spot-check the evidence. **Agent:** collect evidence, update docs and write the PR.

**Steps**

1. **Run the real end-to-end scenario** on the real app against real integrations, including one failure path ([Prompt F](#prompt-f-prove-it)). A passing build or a screen running on mock data isn't done. [Kun]
2. **Collect the evidence package.** [John, plus Kun's end-to-end result]
    - **Tests:** named and asserted clearly enough to judge at a glance
    - **Runtime logs** from the scenario
    - **Screenshots or video** of every UI change
    - **Confidence levels** for each part: the code, the gating and the tests
    - **The end-to-end scenario result** [Kun]
3. **Update the docs** the change affects, such as `API.md` or lessons in `AGENTS.md`. [Kun]
4. **Run a pre-PR check in a fresh context.** This is [layer 3 of Phase 9](#93-fresh-context-agent-review), run early. Kun's No Mistakes pipeline does this automatically: it rebases, reviews, tests, updates docs, lints, then opens the PR. [Kun]
5. **Write the PR from the [template](#pr-template)**, keeping it short and structured. [John]

**Output:** an open PR with the evidence attached or linked, and the affected docs updated.

**Exit gate**

- [ ] The end-to-end scenario passed, with evidence attached
- [ ] The tests would fail if the feature broke
- [ ] The PR names the gate and how to switch it off
- [ ] Confidence levels are stated, and low-confidence parts are flagged
- [ ] The docs are updated
- [ ] The PR description is shorter than the diff

> 📏 **General Rule** [Kun]: The first implementation is a draft. Validation is a separate engineering phase.

> 💡 **Tip** [John]: After every UI change, ask the agent for a screenshot or video.

> 💡 **Tip** [John]: Ask for a confidence level on each part of the change. Low confidence tells you where to read.

> 💡 **Tip** [John]: Agents can write useless tests. Keep a skill about *not* writing useless tests, so the tests stay meaningful as proof.

> ⚠️ **Caution** [John]: His "biggest pet peeve" is a PR whose summary and test plan are longer than the code change. "Don't be that guy."

> 🔧 **Tool** [Kun, verified]: **No Mistakes** is public at github.com/kunchenguid/no-mistakes.
>
> - `no-mistakes init` sets up a local gate remote.
> - `git push no-mistakes` runs review, tests, docs and lint in a disposable worktree, and opens a PR only once everything passes.
> - It works with several coding agents and installs a `/no-mistakes` agent skill.

> 🗣️ **Speaker Opinion** [John]: The more proof a PR includes up front, the less code you need to read. He calls agentic validation the core idea that lets you read less code.

---

## Phase 9: Review

**Goal:** Catch what matters with the least human attention, and spend your attention where a bug would hurt.

**You:** decide whether to merge, after reading at the depth the tier calls for. **Agents:** run static checks, review in a fresh context, and fix reviewer comments.

**Steps** (layers, in order)

```text
9.1 Triage -> 9.2 Static checks -> 9.3 Fresh-context AI review -> 9.4 PR reviewer bot
     -> 9.5 Babysit loop -> 9.6 Human review by tier -> Merge
```

**Output:** an approved PR, merged with its feature gate still off.

### 9.1 Triage the Change

Answer five safety questions before reading any code. [John]

1. Is this trunk or leaf?
2. Is it gated? Can I roll it back?
3. What control experience must not change?
4. How bad is it if this goes wrong?
5. Is it a one-way door, such as a data migration, deletion, public API change or external send?

Then confirm or raise the tier from Phase 5. A "leaf" task that ends up editing a shared reducer is a trunk change. [John]

> 🗣️ **Speaker Opinion** [John]: "In my opinion, everything should be anchored on safety." If you can answer "can I roll it back?" with a confident yes, you can spend much less time on the change.

### 9.2 Let Static Checks Handle Nits

Linting, formatting and type checks run in CI. Neither humans nor AI reviewers should comment on style. [John]

> 🗣️ **Speaker Opinion** [John]: The old days of nit-picking ("this is my favorite way of writing code") are "kind of dead."

### 9.3 Fresh-Context Agent Review

A reviewer that never saw the conversation that produced the code checks the diff against the original requirement and the architecture ([Prompt G](#prompt-g-fresh-context-review)). [John + Kun]

> ⚠️ **Caution** [John]: "The agents will cheat." An agent reviewing code it helped write leans on that earlier context, so its review is biased.

> 🔧 **Tool** [Editor, verified]: Claude Code's **`/code-review`** (alias `/review`):
>
> - Reviews your branch, a PR number or a ref range in a background subagent with its own context.
> - `--fix` applies the findings and `--comment` posts them on the PR.
> - `/code-review ultra` escalates to a deeper cloud review.
>
> **`/security-review`** focuses on security. Codex CLI has its own **`/review`**. A custom reviewer subagent in `.claude/agents/` also works.

### 9.4 AI Reviewer on the Pull Request

> 🔧 **Tool** [John, verified by Editor]: **Codex on GitHub** (the `chatgpt-codex-connector` bot):
>
> - Turn on automatic reviews per repo in Codex settings, or comment `@codex review` on a PR. You can add a focus, e.g. `@codex review for security regressions`.
> - Comment `@codex address that feedback` to have it update the PR.
> - Put repository review rules in `AGENTS.md`.
>
> John notes it costs money.

> 🔧 **Tool** [Editor, verified]: **Claude Code Review** is a research preview for Team and Enterprise plans.
>
> - It reviews when a PR opens, on every push, or when you comment `@claude review`. `@claude review always` also subscribes the PR to later pushes.
> - Findings are tagged 🔴 Important, 🟡 Nit or 🟣 Pre-existing.
> - Tune it with a `REVIEW.md` file at the repo root.
> - Reviews average $15–25 each, and it never blocks a merge on its own.

> 🗣️ **Speaker Opinion** [John]: AI is already "really good" at reviewing code, "better than most humans," but many people use it wrong. He considers the default reviewers in Claude Code and Codex good enough.

> 💡 **Tip** [Editor]: In `REVIEW.md` or your `AGENTS.md` review rules, tell the reviewer to skip anything CI already enforces and to cap nits. That keeps AI review focused on correctness.

### 9.5 Babysit the PR Automatically

Reviewer bots leave comments; you fix them and push; more comments arrive. John automates this loop. Every hour, an agent: [John]

- checks the PR
- fixes requested changes
- re-runs local and agentic validation
- updates the PR notes and pushes

Use [Prompt H](#prompt-h-pr-babysitter) to set it up.

> 🔧 **Tool** [Editor, verified]: Claude Code's **`/loop`**:
>
> - `/loop 1h <prompt>` reruns a prompt every hour.
> - `/loop <prompt>` lets Claude pick the interval and end the loop when the work is done.
> - A bare `/loop` runs a built-in maintenance prompt that tends the current branch's PR: review comments, failing CI and merge conflicts.
> - Loops only run while the session is open, and they expire after 7 days. For durable automation, use cloud routines (`/schedule`) or GitHub Actions.

> 💡 **Tip** [John]: Build the babysitting loop into a skill, so the back-and-forth with reviewers happens without you.

> ⚠️ **Caution** [Editor]: The babysitter should fix reviewer comments, not settle disagreements. Comments that ask for a design or scope change go to you, not into an endless fix cycle.

### 9.6 Human Review at the Right Depth

| Tier | You read | Also required | Who merges |
|---|---|---|---|
| **Low** (leaf, gated) | Evidence, test names, and a skim of the diff for anything obviously wrong | AI review clean | You, after CI. Auto-merge only for toy or internal projects [Kun] |
| **Medium** | Evidence, plus every file that touches a contract or shared code | AI review clean, end-to-end evidence | You |
| **High** (trunk, ungated, one-way door) | Every line, including migrations and config | Security review, rollback plan, staged rollout plan | You; on a team, a second human as well [Editor] |

**What to look for when you read** [Editor, built from Kun's architecture questions and John's safety questions]

- [ ] It does what the scenario says, and nothing else
- [ ] No API, schema, auth flow or shared state changed without an escalation
- [ ] Data changes only through domain actions, and permissions are checked on the server
- [ ] The gate exists, defaults to off, and switching it off restores the control experience
- [ ] Migrations are backward-compatible or reversible
- [ ] The tests would fail if the feature broke
- [ ] No secrets or personal data appear in code, logs or error messages
- [ ] It matches `ARCHITECTURE.md`, or the doc was updated in the same PR

> 🗣️ **Speaker Opinion** [John]: He still reads "a lot" of code, and thinks he reads *more* than before. He turns a mental knob up for trunk, infrastructure, many-dependency changes and one-way doors, and down for gated leaf work.

> 🗣️ **Speaker Opinion** [Kun]: If reading every diff is your only safety mechanism, your attention becomes the bottleneck. Build contracts, tests, independent review and evidence, then read code where the risk warrants it.

> ⚠️ **Caution** [Guide]: Until you have more engineering experience, don't auto-merge anything that matters. Use the stronger process by default.

> 💡 **Tip** [John]: The better you know your codebase, the faster review gets. You can tell at a glance what touches the dangerous zones and what's a simple leaf.

**Exit gate**

- [ ] The triage answers are recorded in the PR, and the tier is confirmed
- [ ] CI is green, with no style comments left for humans
- [ ] Fresh-context and PR-bot findings are fixed or explicitly accepted
- [ ] Human review is done at the depth the tier requires
- [ ] The PR merged with its gate off

---

## Phase 10: Merge Is Not Launch

**Goal:** Turn merged, gated code into a released feature, safely.

**You:** decide when to widen the rollout, and apply your own taste to the polish. **Agents:** audit the feature, fix findings, and reproduce bug reports.

**Steps**

1. **Treat merged-and-gated work as about 80% done.** John calls this first phase "broad strokes": everything gated and landed. [John]
2. **Audit before launch.** Run several agents over the whole feature, looking at performance, bugs, security and whether it matches the spec ([Prompt I](#prompt-i-pre-launch-audit)). [John]
3. **Refactor and polish:** clean up the code, and refine details such as animations. This is where human taste matters most. [John]
4. **Roll out gradually.** Open the gate to a small slice of users (a canary) or run an A/B test, and watch errors, crashes and alerts. [John]
5. **Feed problems back.** Route bug reports to the lead agent, reproduce them end to end, fix them in an isolated worktree, and record the lesson in the project memory. [Kun]

**Output:** a released feature with its gate fully open, and lessons recorded in `AGENTS.md` or a skill.

**Exit gate**

- [ ] Audit findings are fixed or explicitly accepted
- [ ] The canary ran clean for the agreed window
- [ ] The gate is open to everyone, or the feature has been removed
- [ ] Lessons are added to `AGENTS.md` or a skill

> 🗣️ **Speaker Opinion** [John]: "Even if it's merge ready, I don't think it's launch ready." The last 20% takes as long as the first 80% and needs human taste.

> 📏 **General Rule** [John]: Rolling out gradually behind a gate surfaces bugs, crashes and alerts before everyone sees the feature.

> ⚠️ **Caution** [John]: A small user base can't support a statistically valid A/B test. Treat the rollout as a safety check, not a measurement, but still do it.

---

## Cheat Sheet: One Feature, End to End

[Editor] The daily loop once Phases 0–6 are done, shown with Claude Code commands. Codex equivalents are in the [reference table](#tools-and-commands-reference).

1. **Pick the next task card.** Note its tier, gate and acceptance criteria.
2. **Isolate it:** `claude --worktree t-07`
3. **Set the goal:** `/goal …` using the [Goal condition](#goal-condition) template, in auto mode.
4. **Prove it:** run [Prompt F](#prompt-f-prove-it) and check the evidence.
5. **Review in a fresh context:** `/code-review`, then fix the findings.
6. **Open the PR** from the template. The AI reviewer runs, and `/loop 1h …` babysits it.
7. **Triage**, then do human review at the tier's depth, then merge with the gate off.
8. **Open the gate** to a canary, watch it, open it fully, and add any lesson to `AGENTS.md`.

---

## Scaling Up Later

Adopt the logic first and the scale later. [Guide]

| Stage | Setup | Add it when |
|---|---|---|
| 1 | One app, one agent, one `AGENTS.md`, one end-to-end test plan | Always start here |
| 2 | One lead, two workers (frontend and backend), one fresh-context reviewer | One agent reliably produces validated features |
| 3 | Separate agents for research, design, build and validation | Contracts are stable and you still know every active objective |
| 4 | Risk policies, with auto-merge for the Low tier only | Tests and evidence have proven reliable |
| 5 | Second Mates, multiple machines, fleet summaries | Coordination itself is the bottleneck |

**Kun's fleet features** [Kun]

- **Second Mates:** persistent managers, one per project. Each keeps its project's context and runs its own crew, reporting up to First Mate.
- **Dispatch policy:** the harness, model and reasoning level are chosen by task type, difficulty, cost and remaining quota.
- **Per-project policies:** for example a direct PR, a PR with automatic merge for low-risk projects, No Mistakes, or required human review.
- **Bearings and Ahoy:** Bearings is a snapshot of current work, recently landed work and unresolved decisions. Ahoy is a catch-up of what First Mate has told you since your last message.
- **Issue intake:** bug reports from Discord and X are routed back to First Mate.
- **Remote machines:** **Herder**, his agent-aware terminal multiplexer, shows agents running on other machines, such as a headless Mac Mini.

**John's recurring loops** [John]

- Hourly PR babysitting
- Status check-ins every 1–2 hours
- Summaries of message threads he follows, every 3 hours

> 📏 **General Rule** [Guide]: Add hierarchy only when coordination is genuinely your bottleneck, not because it looks advanced.

---

## Where John and Kun Differ

| Topic | John | Kun | This workflow [Editor] |
|---|---|---|---|
| Reading code | Still reads a lot, maybe more than before; depth follows trunk vs leaf | Reading every diff makes you the bottleneck; rely on evidence, independent review and risk gates | Everyone reads the evidence first; humans read trunk and High-tier code in full |
| Where validation runs | Proof in the PR, reviewer bots on GitHub, a babysitting loop | A pre-PR pipeline (No Mistakes) with a fresh-context review | Both: a pre-PR check, then a PR reviewer |
| Autonomy | Long goal runs (about 22 hours) with strong exit criteria | An orchestrator dispatches workers and escalates only what needs a human | Start bounded (turn caps, Low tier) and lengthen runs as the setup matures |
| Planning artifacts | A spec, validation criteria and design screens | An intent dump, parallel research, visual reviews in Lavish, a PRD | Kun's front-end sequence plus John's exit criteria |
| Rollback | Feature gates from day one; canary deployments | Infrastructure as code, controlled secrets, risk policies | Gates, infrastructure as code and tier-based rollout |
| Environments | Not discussed | One production environment for a tiny MVP | Add staging or a preview environment before real user data |
| Code quality on side projects | Relaxed for an internal side project | Not discussed | Production standards always |

---

## Prompt Library

Prompts A, B, D, F and G adapt the reconstruction guide's prompts [Guide]. C and E were added here [Editor]. H and I are built from John's descriptions [John]. Replace anything in `<angle brackets>`.

### Prompt A: Kickoff

Phase 1.

```text
You are my lead engineer. Do not write code yet.
I'll describe an app in plain English. Organize it into: users, their problem,
goals, non-goals, main user journeys, data that must be stored, roles and
permissions, integrations, assumptions, unknowns, and draft MVP acceptance
criteria. Point out contradictions and anything that looks unnecessary.
Ask me up to 5 questions, then write docs/PRODUCT_BRIEF.md (one page).
```

### Prompt B: Research

Phase 2. Run the two parts as separate agents.

```text
[Market researcher]
Using docs/PRODUCT_BRIEF.md, find existing products that solve this problem.
For each: what it does well, what it misses, and its price. Then state the gap
and whether building is justified. Write docs/research/MARKET_RESEARCH.md.

[Technical researcher]
Using docs/PRODUCT_BRIEF.md, compare 2-4 viable architectures: frontend,
backend, database, auth, hosting, monthly cost at our expected scale, offline
behavior, security boundaries, deployment, backups, testing.
Do not assume enterprise scale. Do not implement anything.
Recommend one and say what would change your mind.
Write docs/research/TECHNICAL_OPTIONS.md.
```

### Prompt C: Architecture Review and Tree Map

Phase 3.

```text
Turn the chosen architecture into a review I can follow without a CS background:
system diagram, data flow, auth flow, data model, API responsibilities, source
of truth and owner for each data type, deployment, main failure modes, and open
decisions. Explain every box in plain English.
Then label every component TRUNK (entry point, shared state, auth, data,
payments, infrastructure, many dependents) or LEAF (isolated, few dependents),
with a one-line reason each.
Output one HTML page with Mermaid diagrams, then save the decisions to
docs/ARCHITECTURE.md, docs/DATA_MODEL.md, docs/API.md and docs/AUTH.md.
```

### Prompt D: Anti-Overengineering

Phase 3.

```text
Act as a skeptical principal engineer. In docs/ARCHITECTURE.md, find anything
premature, duplicated, unnecessarily expensive, or solving a problem we don't
have yet. Propose cuts. Do not remove security, data-integrity or
maintainability boundaries just to make the system smaller.
List each cut as "deferred" with the trigger that would bring it back.
```

### Prompt E: Task Goal

Phase 7. See the [Goal condition](#goal-condition) template.

### Prompt F: Prove It

Phase 8.

```text
Test this change as a real user would. Use the real app and the real
integration path wherever practical. Run the scenarios in docs/TESTING.md
that this task touches, plus one failure path. Then produce the evidence:
- each test name and what it asserts
- runtime logs for the scenario
- screenshots or a short video of every UI change
- your confidence (high/medium/low) in the code, the gating and the tests,
  with a reason for anything below high
Do not claim success from unit tests or a passing build alone.
```

### Prompt G: Fresh-Context Review

Phase 9. Run it in a new session or subagent.

```text
You did not write this change. Review the diff against the original
requirement (docs/TASKS.md, task <id>) and docs/ARCHITECTURE.md.
Look for: wrong behavior, permission or security problems, data-integrity
issues, contract changes that weren't escalated, missing error handling,
tests that would still pass if the feature broke, a missing or leaky feature
gate, and drift from the architecture. Ignore style; CI handles it.
Classify the change TRUNK or LEAF and Low/Medium/High risk, with reasons.
List findings by severity with file:line.
```

### Prompt H: PR Babysitter

Phase 9, adapted from John's example.

```text
/loop 1h Check PR #<n>. Address every change request from the AI reviewer and
any failing CI job: fix it, re-run the local tests and the e2e scenario, update
the PR notes, and push. If a comment asks for a design or scope change, don't
change the design; summarize it for me and wait. When the PR is approved and
green, say so in one line.
```

Leave out `1h` to let Claude pace the loop and stop it once the PR is clean.

### Prompt I: Pre-Launch Audit

Phase 10.

```text
Before launch, audit the whole <feature> (every merged PR behind flag <flag>).
Run separate reviewers for: performance, bugs and edge cases, security, and
conformance to docs/PRODUCT.md. Each reports findings by severity with
file:line. Then propose a cleanup and refactor list. Don't fix anything yet.
```

---

## Templates

All templates were written for this document [Editor]. John offered a PR template in his talk, but it isn't in the transcript.

### AGENTS.md Skeleton

```markdown
# AGENTS.md

## Project map
- app/      client (UI only; no business rules)
- backend/  API service (domain actions only)
- docs/     product, architecture, testing, tasks
- infra/    infrastructure as code

## Commands
- Setup: `make setup`
- Test: `make test`   End-to-end: `make e2e`
- Lint and types: `make check`

## Rules
- Read docs/PRODUCT.md and docs/ARCHITECTURE.md before changing behavior.
- New features ship behind a flag in config/flags, default off.
- Never commit secrets. Never delete files; move them to archive/.
- Use .github/pull_request_template.md and attach evidence to every PR.

## Escalate to a human only when
- a change touches an API, schema, auth flow or shared state
- a decision changes scope, cost or security
- you need a credential or an action only the owner can take

## Lessons learned
- (one line each time an agent repeats a mistake)
```

### Task Card

```markdown
### T-07 Save card
- Scope: user can save a card and see it under Saved
- Area: src/features/save-card/   Type: LEAF   Tier: Low
- Gate: flag `save_card` (default off)
- Depends on: T-03 (cards API)
- Acceptance: scenario S-04 in docs/TESTING.md; screen matches docs/design/save-card.png
- Proof: tests, screenshot of saved state, confidence levels
- Escalate if: the cards API or the shared store needs to change
```

### Goal Condition

This example is for Claude Code's `/goal`. Codex's `/goal` takes a plain-language objective in the same spirit.

```text
/goal Task T-07 "Save card" is done when:
1. `npm test` and `npm run e2e -- save-card` both exit 0 in this conversation.
2. A screenshot of the saved state is in evidence/t-07/ and matches
   docs/design/save-card.png.
3. The feature is behind flag `save_card` (default off), and switching it off
   restores current behavior.
Constraints: change only src/features/save-card/ and its tests. Commit and push
at each passing checkpoint. Never delete files; move them to archive/. If an
API, schema or shared state must change, stop and ask me.
Or stop after 25 turns and report where you are.
```

### PR Template

```markdown
## What and why
One or two sentences. Task: T-07

## Risk
Trunk/Leaf: LEAF · Tier: Low · Gate: `save_card` (default off) · Rollback: flag off

## Evidence
- Tests: save_card.test.ts (saves, unsaves, persists after reload)
- E2E: S-04 passed (evidence/t-07/e2e.log)
- UI: evidence/t-07/saved.png
- Confidence: code high · gating high · tests medium (no offline case yet)

## Reviewer focus
Up to three bullets: where to look first, and why.
```

---

## Tools and Commands Reference

| Name | What it is | Phase | Status |
|---|---|---|---|
| **Claude Code** | Anthropic's coding agent (terminal, desktop, IDE, web) | All | Verified |
| `CLAUDE.md` / `AGENTS.md` | Instruction files the agent loads | 0 | Verified |
| Skills (`.claude/skills/`) and subagents (`.claude/agents/`) | Situational instructions; specialized helper agents | 0, 8, 9 | Verified |
| Hooks | Scripts that run on agent events, e.g. auto-format, protected files | 0 | Verified |
| `claude --worktree <name>` | Session in its own git worktree | 7 | Verified |
| `/goal <condition>`, `/goal`, `/goal clear` | Keep working until a condition holds | 7 | Verified |
| `/loop [interval] [prompt]` | Rerun a prompt on an interval; bare form tends the PR | 9 | Verified |
| Routines (`/schedule`) | Cloud scheduled or event-triggered runs | 9 | Verified |
| `/code-review` (alias `/review`), `--fix`, `--comment`, `ultra` | Local review in a fresh-context subagent | 9 | Verified |
| `/security-review` | Security-focused review | 9 | Verified |
| Claude Code Review (`@claude review`, `REVIEW.md`) | Managed GitHub PR review (Team/Enterprise) | 9 | Verified |
| **Codex** (OpenAI) | OpenAI's coding agent (CLI, IDE, cloud) | 7, 9 | From source |
| Codex `/goal` | Persistent goal with pause, resume and clear | 7 | Third-party sources only |
| Codex `/review` | Code review in the CLI | 9 | Third-party sources only |
| Codex on GitHub (`chatgpt-codex-connector`, `@codex review`) | Automatic or on-demand PR review | 9 | Verified |
| **No Mistakes** (`no-mistakes init`, `git push no-mistakes`) | Pre-PR validation gate in a disposable worktree | 8 | Verified |
| **Lavish** | Kun's interactive HTML planning and review tool | 3, 4 | Kun's tool; not verified |
| **Treehouse** | Kun's wrapper around git worktrees | 7 | Kun's tool; not verified |
| **Herder** | Kun's agent-aware terminal multiplexer | Scaling | Kun's tool; not verified |
| **First Mate / Second Mate** | Kun's orchestrator and per-project manager agents | 1, 7, Scaling | Kun's setup; not verified |
| **Bearings / Ahoy** | Kun's fleet status summaries | Scaling | Kun's setup; not verified |
| Git worktrees | Isolated checkouts of one repo | 7 | Standard Git |
| LaunchDarkly | Feature-flag platform | 0, 10 | From source |
| Figma; Pen (formerly Pencil) [?] | Design tools for reference screens | 4 | From source; Pen name uncertain |
| ChatGPT Deep Research | Research harness | 2 | From source |
| Nix, Nix-Darwin, Home Manager | Reproducible developer environment | 0 | From source |
| OpenTofu | Infrastructure as code | 0, 10 | From source |

---

## Appendix A: Term Verification and Corrections

| # | Term in source | Rendered here | Status | Note |
|---|---|---|---|---|
| 1 | Claude Code `/code-review` [?] (John) | `/code-review`, alias `/review` | Resolved | Confirmed in Claude Code docs. It runs as a background subagent with its own context. |
| 2 | "goals" [?] for hourly PR babysitting (John) | `/loop` for interval babysitting; `/goal` for condition-driven work | Clarified | Both Claude Code and Codex now have `/goal`. Interval-based reruns are Claude Code's `/loop`. |
| 3 | "Loops and goals are pretty interchangeable" (John) | Kept as his opinion | Clarified | In Claude Code they differ: `/goal` continues until a condition holds; `/loop` reruns on a time interval. |
| 4 | "ChatGPT Codex Connector" [?] | `chatgpt-codex-connector` GitHub bot | Resolved | Seen on public PRs, which use `@codex review`. |
| 5 | Tagging Codex on a PR, "likely `@codex`" [?] | `@codex review`, `@codex address that feedback` | Resolved | Taken from the bot's own help text. |
| 6 | The "loop" keyword (John, video 2) | Claude Code `/loop` | Likely | John didn't name the tool; Codex was also in his setup. |
| 7 | Pen (formerly Pencil) [?] | Kept with `[?]` | Unresolved | Not checked; it's only an example of a design tool. |
| 8 | "Agentic garden" [?] | Not used | Editorial | His surer phrase, "agentic safeguard," is the idea kept here. |
| 9 | No Mistakes (Kun) | `no-mistakes` | Resolved | Public repo: github.com/kunchenguid/no-mistakes. |
| 10 | Lavish, Treehouse, Herder, First Mate, Second Mate, Bearings, Ahoy (Kun) | Kept as named | Not verified | Kun's own tools and terms, as reported in the guide. |
| 11 | Codex `/goal` | Codex CLI `/goal` behind a feature flag | Partly verified | Third-party coverage only; it's said to have arrived in v0.128.0. |
| 12 | "AI or Not" demo app, Opus 4.8, the claims about Peter Steinberger and Boris Cherny | Omitted | n/a | Not needed for the workflow. |

The source material contains no caption errors to correct directly, because John's material arrived as edited summaries and Kun's as a reconstruction guide. This appendix therefore records verification of the `[?]` items already flagged in those documents.

---

## Appendix B: Editorial Notes

**Structure**

The workflow is organized procedurally, in build order, because it's a synthesized process rather than a summary of one talk.

**How reliable each source is**

- John's material comes from two edited summaries of his talks, so it's second-hand. Uncertainty markers from those summaries are carried over.
- Kun's material comes from a third-party reconstruction of four videos. That guide adds its own adaptations, such as its prompts, its docs list and its staged learning path.
- To keep these apart, **[Kun]** marks what the guide reports Kun doing, and **[Guide]** marks the guide's own suggestions. All attributions to Kun are second-hand.

**Opinion vs general rule**

- 🗣️ is used when a speaker frames something as their own view or practice, or when the choice depends on context. Examples: John's "I read more code than before," and Kun's single production environment.
- 📏 is used for principles presented as broadly applicable that also match standard practice. Examples: review effort follows blast radius; define validation criteria first; don't commit secrets.

**Judgment calls on classification**

- "Agents propose; you decide" is 📏, because it's presented as a general principle.
- "Don't over-weight development cost" is 🗣️, because the guide describes it as one of Kun's own global preferences.
- "The agents will cheat" is ⚠️ with attribution, consistent with the earlier John summary.
- "Add hierarchy only when coordination is the bottleneck" is 📏 [Guide], because it's the guide's advice rather than Kun's stated rule.

**Editor additions**

These aren't in either source:

- branch protection
- the merged risk-tier table, and moving trunk/leaf mapping into planning
- the Given/When/Then scenario format
- all four templates
- turn caps on goals
- the staging-environment recommendation for production
- the `REVIEW.md` tip
- the human-review checklist
- the cheat sheet
- phase gates for every phase

**Omitted or compressed**

- The step-by-step Nix setup, which is long and optional; see Kun's guide.
- Fleet details, compressed into [Scaling Up Later](#scaling-up-later).
- The Deep Research demo details, channel intros, and claims about other people's roles.

**Tool facts**

- These were checked on 2026-10-12, and the products change quickly. Run `/help` in your tool to confirm.
- Codex details come from public GitHub bot messages and third-party articles, not OpenAI's docs.

---

## Sources

**Provided documents**

- John: *Do You Still Read Your Code? Agentic Code Review Strategies* (summary)
- John: *Stop Prompting, Start Designing Loops and Goals* (summary)
- *Agentic App Development Workflow: A beginner-friendly reconstruction of Kun's latest workflow*

**Checked on 2026-10-12**

- [Claude Code: Keep Claude working toward a goal (`/goal`)](https://code.claude.com/docs/en/goal.md)
- [Claude Code: Run prompts on a schedule (`/loop`)](https://code.claude.com/docs/en/scheduled-tasks.md)
- [Claude Code: Code Review and `/code-review`](https://code.claude.com/docs/en/code-review.md)
- [Claude Code: Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees.md)
- [Claude Code docs map](https://code.claude.com/docs/en/claude_code_docs_map.md)
- [kunchenguid/no-mistakes on GitHub](https://github.com/kunchenguid/no-mistakes)
- [Example Codex GitHub review on openai/codex PR #8454](https://github.com/openai/codex/pull/8454)
- [Codex CLI `/goal` workflows (third-party)](https://codex.danielvaughan.com/2026/05/01/codex-cli-goal-workflows-persistent-long-horizon-task-execution/)
- [Codex Code Review rules in AGENTS.md (third-party)](https://agentpedia.codes/blog/codex-code-review-agents-md-rules)
