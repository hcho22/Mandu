# Agentic App Development Workflow
## A beginner-friendly reconstruction of Kun's latest workflow

**Purpose:** Turn the four supplied YouTube transcripts into one practical workflow you can follow to build a real application with AI coding agents while still protecting software architecture, product quality, and maintainability.

> **Source note:** This guide is based only on the four transcripts you supplied. I read them in the order provided and treated that sequence as chronological because each later transcript explicitly refers back to earlier videos/workflows.
>
> I normalized a few obvious speech-to-text spellings where the intended software is clear, such as **Nix**, **Nix-Darwin**, **Home Manager**, **WezTerm**, **tmux**, **Neovim**, **Postgres**, **OpenTofu**, and **Git worktree**. When a product name was less certain, I describe its role rather than silently inventing a correction.

---

# 1. The big idea

Kun's workflow is not primarily a faster way to type code.

It is a system for turning one human into the **captain of an AI engineering team**.

The human spends most of the valuable attention on:

1. deciding what should be built,
2. clarifying requirements,
3. choosing architecture,
4. reviewing product and technical tradeoffs,
5. deciding risk,
6. and validating that the finished product actually behaves correctly.

The agents spend most of their time on:

- research,
- prototyping,
- implementation,
- repetitive setup,
- infrastructure,
- debugging,
- testing,
- code review,
- documentation,
- pull-request preparation,
- and coordination.

His latest workflow therefore moves the human **away from watching every tool call or reviewing every line of code** and toward managing intent, architecture, evidence, and risk.

A useful mental model is:

```text
YOU
Captain
  |
  v
FIRST MATE
Main orchestrator / single conversation
  |
  +------------------+------------------+------------------+
  |                  |                  |                  |
  v                  v                  v                  v
Research agent    UX agent         Backend agent      Infra agent
  |                  |                  |                  |
  +------------------+------------------+------------------+
                           |
                           v
                    Working product
                           |
                           v
                    Validation pipeline
                           |
                           v
                         PR
                           |
                           v
                    Human judgment
```

In the newest transcript, this expands further:

```text
Captain
   |
   v
First Mate
   |
   +---------------- Second Mate: Project A ----------------+
   |                                                        |
   |       + crew mate + crew mate + crew mate              |
   |                                                        |
   +---------------- Second Mate: Project B ----------------+
   |                                                        |
   |       + crew mate + crew mate                          |
   |                                                        |
   +---------------- Direct crew mates ---------------------+
```

The point is not "use lots of agents." The point is:

> **Keep your own attention focused on the highest-value decisions and delegate work that can be researched, implemented, tested, or coordinated by agents.**

---

# 2. How the workflow evolved across the four transcripts

## Transcript 1 - Build the ship, onboard agents, then delegate

The first transcript establishes most of the philosophical foundation.

Kun starts with a terminal-centered environment and explains why he prefers keeping his hands on the keyboard. He uses a terminal emulator, tmux, and Neovim, then introduces multiple coding-agent harnesses.

The important workflow ideas are:

### A. Agents need onboarding

He does not treat every new agent session as a blank chatbot.

He uses:

- a **global memory file** for preferences that should apply everywhere,
- a **project memory file** for project-specific conventions and lessons,
- and **skills** for instructions that are useful only in certain situations.

This is important architecturally because the agents are taught:

- how the repository is organized,
- how important components work,
- how the project is tested,
- what conventions exist,
- and what mistakes should not be repeated.

His project memory becomes a form of accumulated engineering knowledge.

### B. Keep always-loaded memory small

He intentionally keeps the global memory minimal because it is loaded into every session.

Conditional knowledge is moved into skills so the agent only loads it when needed.

The architecture lesson is broader:

> Do not dump your entire project into every prompt. Give agents a stable map, then let them progressively load detailed instructions when the task requires them.

### C. Plan visually before implementation

For complex work he uses **Lavish**, which turns planning into an interactive HTML artifact rather than a long terminal response.

The agent can present:

- alternative approaches,
- mockups,
- diagrams,
- decisions,
- and items requiring human input.

Kun can annotate specific elements and send targeted feedback.

This becomes one of the most important patterns in the later transcripts:

> **Research -> visualize -> decide -> implement.**

### D. Do not automatically trust "done"

When implementation finishes, he does not consider the task complete.

He uses a validation pipeline called **No Mistakes**. The transcript says it can:

1. create/prepare a branch,
2. understand the original intent from the agent session,
3. rebase on the latest main branch,
4. resolve merge conflicts,
5. perform an adversarial review in a fresh context,
6. correct clear defects,
7. escalate ambiguous product decisions,
8. test the change end to end,
9. collect evidence,
10. update documentation,
11. check for remaining issues,
12. push the branch,
13. create a pull request,
14. and continue monitoring the PR.

This is one of the strongest ideas in the entire workflow:

> **The first implementation is a draft. Validation is a separate engineering phase.**

### E. Parallel work requires isolation

When several agents work on the same repository, Kun does not let them all modify the same working directory.

He uses Git worktrees, later wrapped by a tool called **Treehouse**, so each worker has an isolated copy/worktree.

This prevents agents from stepping on one another.

### F. First Mate removes coordination overhead

Instead of personally managing every agent, he introduces **First Mate**.

First Mate:

- receives the captain's request,
- decides how to divide it,
- creates isolated workspaces,
- launches agents,
- monitors them,
- runs validation,
- and brings the important decisions back to the human.

This is the core of the later workflow.

---

## Transcript 2 - Make the development environment reproducible

The second transcript is less about product development and more about ensuring the entire engineering environment can be reproduced.

The main ideas are:

### A. Infrastructure for the developer matters too

Kun wants a fresh Mac to be reproducible without manually clicking through configuration.

He uses a declarative setup based on:

- Nix,
- Nix-Darwin,
- Home Manager,
- Homebrew managed through configuration,
- symbolic links into a version-controlled dotfiles repository,
- and a rebuild script.

### B. Version-control the environment

His terminal, editor, shell, fonts, plugins, memory files, and application configuration live in source-controlled configuration.

This means the workstation itself becomes rebuildable.

### C. Herder replaces tmux in the newer setup

He later prefers **Herder**, an agent-aware terminal multiplexer.

Instead of understanding only terminal panes, Herder can understand agent sessions and show their status.

This foreshadows the latest workflow, where many concurrent agents may exist.

### D. Share global rules across agent harnesses

The same global agent rules are linked into the expected locations for different coding-agent tools.

This lets Kun switch models or harnesses without rebuilding his entire operating method.

That is a major principle:

> **Make the workflow agent-agnostic. Models and harnesses will change. Your engineering process should survive those changes.**

---

## Transcript 3 - Build a real app from scratch

This transcript is the most useful source for understanding his complete app-building sequence.

He starts with no project files and builds a working iOS app and backend.

The sequence is extremely instructive.

### Step 1: Start with one orchestrator

He starts Herder, then launches First Mate.

He tells First Mate the project name and lays down operating rules for which model the crew should use.

### Step 2: Ramble the full product idea

He does not begin by writing database tables or asking an agent to "build the app."

He gives First Mate a long natural-language explanation covering:

- who the product is for,
- the problem it solves,
- the educational goal,
- parent mode,
- child mode,
- virtual rather than real money,
- cross-device data,
- cloud persistence,
- and uncertainties.

This is the **intent dump**.

The agent's job is to organize it.

### Step 3: Run discovery work in parallel

First Mate launches two separate workstreams:

1. **market research**, and
2. **technical research**.

This is a crucial ordering decision.

He does not start coding before answering:

- Does this product need to exist?
- What alternatives already exist?
- What architecture would fit it?

### Step 4: Challenge the technical recommendation

The first technical recommendation suggests a hosted backend service.

Kun disagrees with the assumed cost.

Rather than blindly accepting the agent's recommendation, he asks it to compare alternatives and include a low-cost self-hosted VPS.

This illustrates the correct human role:

> Agents propose. The captain challenges assumptions and decides.

### Step 5: Use Lavish for architecture review

Instead of reading a 351-line technical report, he asks First Mate to bring the technical proposal into Lavish.

He reviews:

- backend options,
- estimated cost,
- authority boundaries,
- identity,
- data flow,
- recovery,
- and diagrams.

He removes requirements he considers premature, such as some auditing/export ideas.

This is a direct example of **preventing overengineering before code exists**.

### Step 6: Prototype the user experience in parallel

While backend research continues, he launches a separate UX workstream.

He first receives text, rejects that as insufficient, and asks for **real HTML wireframes** in Lavish.

He clicks through the prototype and gives concrete feedback.

Only after the flow makes sense does he ask the agent to capture the agreed product requirements in a PRD/README.

### Step 7: Turn decisions into durable project documentation

The product requirements are written into the repository.

That means the repository now contains not just code, but the current product contract.

### Step 8: Create the repository and adopt PR workflow

The local project is published to GitHub.

He then transitions from local changes to a pull-request-based workflow.

At this early prototype stage he intentionally does **not** enable the heaviest validation pipeline yet.

This shows that validation should be **risk-based**, not ritualistic.

### Step 9: Establish a design system before UI implementation

He uses a design tool to create a reusable design system and screen concepts from the PRD.

He gives product-level feedback:

- make it friendlier for children,
- adjust visual tone,
- select an icon direction,
- and create reusable assets.

Then the approved design system is handed back to First Mate for implementation.

### Step 10: Build backend and infrastructure while design happens

While UI design is underway, First Mate starts parallel backend work.

The transcript shows several important technical decisions:

- backend separated from the open-source frontend,
- backend repository kept private,
- native iOS/iPadOS frontend,
- cloud-hosted backend,
- Postgres,
- Sign in with Apple,
- HTTPS,
- a VPS,
- Cloudflare-managed DNS,
- OpenTofu for infrastructure-as-code,
- and a secrets vault for controlled credential access.

The exact technologies are specific to this app, but the process is reusable:

> **Define boundaries, choose ownership, codify infrastructure, and control secrets before agents freely operate production systems.**

### Step 11: Keep the server authoritative

In the architecture review, the backend is the authority rather than letting the phone directly mutate database tables.

The transcript shows domain-oriented API concepts around:

- identity,
- family,
- child,
- wallet,
- loan,
- ledger entries,
- and sessions.

The key architectural principle is:

> Client apps should ask the backend to perform meaningful domain actions. The backend should enforce identity, permissions, and invariants.

### Step 12: Integrate frontend and backend before declaring MVP

The first UI implementation initially uses mock data.

Kun explicitly rejects that as "done."

He defines the real MVP gate:

- simulator runs the actual iOS app,
- app talks to the real backend,
- user signs in using the real Apple flow,
- user performs a real action,
- data is stored in the cloud,
- and signing out/in returns the same data.

That is genuine end-to-end validation.

### Step 13: Let the agent test and debug the integration

When sign-in fails, Kun tells First Mate to keep testing and debugging rather than immediately asking him to intervene.

He says, in effect:

> Do not ask me unless there is something only I can do.

That is how agent autonomy is increased without giving up the acceptance criteria.

### Step 14: Perform an architecture review even after code exists

While a bug is being fixed, Kun asks for a backend architecture review in Lavish.

He reviews:

- API boundaries,
- authentication flow,
- and database shape.

So architecture review is not only a pre-coding event. It is also used to audit what agents actually built.

### Step 15: Verify the real product

The workflow ends with an actual end-to-end test:

- sign in,
- add balance,
- switch to child view,
- verify the value,
- sign out,
- sign in again,
- confirm persisted cloud data.

Only then does he consider the MVP working.

---

## Transcript 4 - Scale from one project to a fleet

The fourth transcript is the newest workflow.

The basic app-development loop does not disappear. Instead, Kun adds an operating system around it for many projects and many agents.

### A. One First Mate becomes the main interface to everything

He says he works across many projects from one First Mate session.

Instead of switching between projects and remembering state, First Mate maintains the fleet-level context.

### B. Dispatch is policy-driven

Before assigning a worker, First Mate can inspect rules that decide which:

- harness,
- model,
- and reasoning level

fit the task.

Examples described in the transcript include different preferences for:

- UI work,
- image-generation work,
- difficult architecture/planning,
- straightforward bug fixes,
- and default development.

It can also consider remaining subscription quota.

The general lesson is not the exact model names.

The lesson is:

> **Route work based on task type, risk, and available resources instead of using the most expensive model for everything.**

### C. Second Mates own domains/projects

As First Mate becomes overloaded, Kun introduces **Second Mates**.

A Second Mate:

- owns a project/domain,
- remembers that project's context,
- manages its own crew,
- and reports upward to First Mate.

This creates hierarchy rather than one orchestrator directly micromanaging dozens of workers.

### D. Remote machines become part of the fleet

Herder can represent agents running on multiple machines.

Kun uses a headless Mac Mini for some project-specific Second Mates while working from a MacBook.

The principle is that compute placement becomes another orchestration detail.

### E. The fleet has explicit project policies

Projects can use different validation/merge policies.

The transcript describes combinations such as:

- direct PR,
- direct PR plus automatic merge for low-risk projects,
- No Mistakes,
- and human review requirements.

The key is **risk-based governance**.

A toy project does not need the same ceremony as a production application.

### F. Visual decision-making remains central

Even at high throughput, agents still bring prototypes into Lavish.

Kun reviews visual alternatives and makes focused decisions instead of trying to infer design quality from code diffs.

### G. "Bearings" and "Ahoy" protect human attention

As many tasks run at once, First Mate can produce fleet summaries.

The transcript describes:

- **Bearings**: a snapshot of current work, recently completed work, and unresolved decisions.
- **Ahoy**: a concise catch-up of what First Mate has told him since his last message, including decisions still waiting on him.

This solves a real multi-agent problem:

> Humans lose track before agents run out of compute.

### H. Issues can enter from multiple surfaces

Kun shows bug reports coming from Discord and X being routed back to the same First Mate.

The important architectural/process idea is that the orchestrator becomes the single place that holds intent, even when requests originate elsewhere.

---

# 3. Kun's latest app-development workflow, reconstructed

Below is the latest workflow expressed as a repeatable sequence.

---

## Phase 0 - Prepare the engineering operating system

### Goal

Make the development environment predictable before building products.

### Source-derived practices

- version-control workstation configuration,
- use a consistent terminal/editor environment,
- use an agent-aware session manager,
- maintain shared global agent rules,
- maintain project-specific memory,
- use skills for conditional knowledge,
- keep the workflow model/harness agnostic.

### Beginner version

You do **not** need to reproduce his full terminal setup before building your first app.

Minimum:

1. Git and GitHub
2. one coding-agent environment you are comfortable with
3. a repository
4. a project instruction file such as `AGENTS.md`
5. a way to run tests
6. a way to create isolated branches/worktrees

Do not spend weeks customizing tools before you have a product.

---

# 4. Phase 1 - Intent before architecture

## Step 1: Give the orchestrator an "intent dump"

Explain the app naturally.

Include:

- who uses it,
- what problem they have,
- what a successful experience feels like,
- what the app should do,
- what it should never do,
- what data must survive,
- devices/platforms,
- privacy/security concerns,
- and what you are still unsure about.

Do not worry about perfect terminology.

### Beginner prompt

> I want to build a new app. Do not start coding yet. First organize my description into users, problems, goals, non-goals, major workflows, data that must be stored, integrations, unknowns, and decisions we still need to make. Challenge anything that sounds contradictory or unnecessary.

### Deliverable

A one-page product brief.

---

# 5. Phase 2 - Validate the product and architecture in parallel

## Step 2: Market/product research

Ask a separate worker to answer:

- What products already solve this?
- What do they do well?
- What gap remains?
- Which ideas are worth borrowing?
- Is there a reason to build this instead of using an existing product?

### Deliverable

A short competitor/gap report.

## Step 3: Technical research

At the same time, ask another worker to investigate:

- frontend platform,
- backend options,
- database,
- authentication,
- file/media storage if needed,
- cloud/hosting,
- external services,
- expected cost,
- offline behavior,
- security boundaries,
- deployment,
- backup/recovery,
- and testing.

### Deliverable

An architecture-options report, **not code**.

## Step 4: Challenge assumptions

Do what Kun did with backend cost.

Ask:

- Is the agent assuming scale we do not have?
- Is it adding enterprise infrastructure to a three-user MVP?
- Is a managed service buying enough value to justify its cost?
- Is it inventing requirements?
- Is it optimizing for development effort instead of long-term simplicity?
- Is there a simpler design that preserves the important boundaries?

This is where your judgment matters most.

---

# 6. Phase 3 - Turn architecture into something you can see

## Step 5: Require diagrams and decision cards

For a beginner, do not accept a 300-line architecture memo as the only explanation.

Ask the agent to produce:

1. a system diagram,
2. a data-flow diagram,
3. an authentication flow,
4. a list of major components,
5. a database/data-model diagram,
6. an API responsibility list,
7. the open decisions,
8. the risks,
9. and a plain-English explanation of each.

### Beginner-friendly architecture diagram

For a typical app with a backend:

```text
[ iPhone / Web App ]
        |
        | HTTPS
        v
[ Backend API ]
        |
        +------ verifies login / permissions
        |
        +------ applies business rules
        |
        v
[ Database ]

Optional side systems:
- File storage
- Email/SMS
- Payments
- AI provider
- Analytics
```

If you cannot explain what every box does, do not start implementation yet.

---

# 7. Phase 4 - Design the product experience before production UI code

## Step 6: Prototype major journeys

Kun uses HTML artifacts/wireframes because they are fast to change.

Ask for clickable prototypes of:

- onboarding,
- sign in,
- home/dashboard,
- the primary action,
- important settings,
- errors/empty states,
- and any admin/parent/operator mode.

The goal is **behavior**, not polish.

### Ask yourself

- Can a first-time user tell what to do?
- Is the primary action obvious?
- What happens when there is no data?
- What happens when something fails?
- Are privileged actions clearly separated?
- Does the flow match the intended user, not the developer?

## Step 7: Convert approved decisions into a PRD

Once the product flow is coherent, put the decisions into the repository.

A good beginner PRD should contain:

```text
1. Problem
2. Users
3. Goals
4. Non-goals
5. User journeys
6. Functional requirements
7. Data that must be stored
8. Permissions / roles
9. Technical constraints
10. MVP definition
11. Explicitly deferred features
12. Acceptance criteria
```

The PRD becomes a reference point for later agents.

---

# 8. Phase 5 - Establish the software architecture

This is the part I would emphasize most strongly for a non-CS beginner.

Kun's process protects architecture by making boundaries explicit before agents generate large amounts of code.

## Architecture Rule 1: Separate presentation from authority

The UI should render state and collect user intent.

The backend should enforce:

- identity,
- permissions,
- business rules,
- and durable state.

Do not let every screen directly manipulate database tables.

## Architecture Rule 2: Model the business, not the screens

In the wallet example, the system has concepts such as:

- parent identity,
- family,
- child,
- wallet,
- loan,
- ledger entry,
- and session.

Those are domain concepts.

A screen may change tomorrow. A `Wallet` or `Loan` is still part of the business.

## Architecture Rule 3: Prefer domain actions over generic database CRUD

Instead of exposing:

```text
POST /database/updateRow
```

prefer actions that reveal intent:

```text
POST /wallet/deposit
POST /loan/create
POST /loan/payment
```

The exact endpoint names are illustrative, but the principle matches the architecture in the transcript: the backend exposes a narrow domain interface rather than making the client the database administrator.

## Architecture Rule 4: Decide who owns each piece of truth

For each data item, answer:

- Where is the source of truth?
- Who is allowed to change it?
- Can it be cached locally?
- What happens if the device is offline?
- How is it reconciled later?

## Architecture Rule 5: Treat authentication and authorization as different things

Plain English:

- **Authentication** = Who are you?
- **Authorization** = What are you allowed to do?

The wallet example distinguishes a parent's identity and permissions from a child's read-oriented experience.

Do not stop at "the user is logged in." Define what every role may read or change.

## Architecture Rule 6: Define data relationships before agents create random tables

A beginner-friendly schema exercise:

```text
User
  |
  +-- belongs to --> Family
                       |
                       +-- has --> Child Profile
                                      |
                                      +-- has --> Wallet
                                                    |
                                                    +-- Ledger Entries
                                                    +-- Loans
```

Before implementation, ask the architecture agent:

> For every table/entity, explain why it exists, its identifier, who owns it, its relationships, and which operations can modify it.

## Architecture Rule 7: Keep the MVP architecture simple but real

Kun explicitly rejects unnecessary environment tiers in the MVP.

That is a valuable rule:

> Avoid fake enterprise architecture. Keep the minimum architecture that still has correct security, boundaries, persistence, and recoverability.

"Simple" does not mean "put everything in one giant file."

It means fewer moving parts with clean responsibilities.

---

# 9. A practical architecture package to require before coding

For your own app, ask your agent team to create these files before serious implementation:

```text
/docs/PRODUCT.md
/docs/ARCHITECTURE.md
/docs/DATA_MODEL.md
/docs/API.md
/docs/AUTH.md
/docs/TESTING.md
/docs/DEPLOYMENT.md
AGENTS.md
```

This file list is my beginner-friendly adaptation of the workflow, not a literal list Kun mandates.

### `PRODUCT.md`

What the app must do and what is out of scope.

### `ARCHITECTURE.md`

Major components and why they exist.

### `DATA_MODEL.md`

Entities, relationships, ownership, and constraints.

### `API.md`

Frontend/backend contract.

### `AUTH.md`

Login method, roles, permissions, token/session flow.

### `TESTING.md`

Critical end-to-end scenarios.

### `DEPLOYMENT.md`

How the system reaches production and how to recover it.

### `AGENTS.md`

Repository map, commands, conventions, and lessons agents must remember.

If the agents cannot keep these documents consistent with the implementation, the architecture will drift.

---

# 10. Phase 6 - Make infrastructure reproducible

The real-app transcript uses several practices that are valuable even for small projects.

## Infrastructure as code

Kun asks for the VPS setup to be represented with OpenTofu.

The general principle:

> A server you can recreate from configuration is safer than a server you configured manually and cannot remember.

For your app, infrastructure code should explain:

- server/provider,
- network rules,
- DNS assumptions,
- databases/services,
- deployment inputs,
- and backups.

## Controlled secrets

The transcript shows a secrets vault requiring authorization before agents use production credentials.

The lesson is more important than the specific vault product:

> Do not casually paste production secrets into prompts, source files, or repositories.

A beginner rule:

- never commit secrets,
- use a dedicated secret manager,
- give the agent the minimum credential scope,
- and require confirmation for destructive or production-sensitive actions.

## One environment may be enough initially

Kun rejects development/staging/production duplication for a tiny MVP and uses one production environment.

That is context-specific, but the general rule is:

> Add environments when they solve a real risk or collaboration problem, not because large companies have them.

For a beginner app handling sensitive/paid/customer data, you may still want a separate non-production environment earlier. Make the decision based on risk.

---

# 11. Phase 7 - Parallel implementation without losing architecture

Once product and architecture are settled, First Mate can split implementation.

A sensible dependency graph is:

```text
Track A - Backend
  1. data model
  2. auth/session layer
  3. domain services
  4. API endpoints
  5. deployment

Track B - Frontend
  1. app shell/navigation
  2. design system
  3. auth UI
  4. domain screens
  5. API client

Track C - Integration/Test
  1. seed/test data
  2. end-to-end scenarios
  3. error-path checks
  4. evidence capture
```

These can run in parallel **only after the contracts are clear**.

Otherwise parallelism produces incompatible implementations faster.

## Use isolated workspaces

Every implementation agent should have:

- its own branch/worktree,
- a clearly scoped task,
- explicit acceptance criteria,
- and a rule against modifying unrelated architecture without escalation.

---

# 12. Phase 8 - Define "done" as end-to-end behavior

This is arguably the most important practice for a beginner using coding agents.

Agents can create impressive-looking code that is not truly integrated.

Kun's MVP test was not:

> "The frontend builds."

It was closer to:

1. launch the actual app,
2. use the real authentication system,
3. talk to the real backend,
4. perform a real domain action,
5. persist the result in the real database,
6. sign out,
7. sign back in,
8. verify the same data returns.

Your app needs similarly concrete scenarios.

### Example acceptance test

For a task manager:

```text
Given a new user
When I sign up
And create a project
And add a task
And close the app
And reopen it
Then the project and task still exist
And another user cannot read them
```

That tests architecture, not merely UI.

---

# 13. Phase 9 - Separate implementation from validation

The first-pass agent should not be the only judge of its own work.

Kun uses a separate pipeline with fresh-context review.

For your version, require:

1. implementation agent finishes,
2. second agent reviews against original intent,
3. automated tests run,
4. end-to-end behavior is tested,
5. evidence is collected,
6. documentation is updated,
7. risk is assessed,
8. then a PR is opened.

### Evidence can be

- screenshots,
- video,
- test logs,
- API responses,
- browser recordings,
- simulator recordings,
- or command output.

This is far more useful than an agent saying "all done."

---

# 14. Phase 10 - Use risk to decide how much human review is needed

Kun's newest workflow explicitly uses different policies for different projects.

That is sophisticated and worth copying conceptually.

## Low risk

Examples:

- toy project,
- visual experiment,
- internal prototype,
- easily reversible change.

Possible process:

- agent review,
- automated tests,
- direct PR,
- maybe automated merge.

## Medium risk

Examples:

- normal customer-facing feature,
- important data flow,
- auth-adjacent UI,
- non-destructive backend change.

Process:

- independent agent review,
- end-to-end tests,
- evidence,
- human PR review.

## High risk

Examples:

- authentication,
- payments,
- permissions,
- destructive migration,
- production secrets,
- customer data,
- irreversible infrastructure.

Process:

- architecture review,
- independent implementation review,
- security-focused review,
- end-to-end validation,
- rollback plan,
- and explicit human approval.

### Beginner recommendation

Until you have more engineering experience, **do not use automatic/YOLO merges for important applications**.

Use the stronger process by default.

---

# 15. Phase 11 - Feed real usage back into the system

The workflow does not end at deployment.

The latest transcript shows issues arriving from external surfaces and being funneled back to First Mate.

The loop becomes:

```text
User feedback / bug
        |
        v
First Mate
        |
        v
Reproduce end to end
        |
        v
Find root cause
        |
        v
Fix in isolated workspace
        |
        v
Validate
        |
        v
PR / release
        |
        v
Update project memory if a reusable lesson was learned
```

This is how the project memory becomes more valuable over time.

---

# 16. The latest fleet workflow

Once you can safely build one app, Kun's newest system adds scale.

## First Mate

The only agent you normally talk to.

Responsibilities:

- understand the request,
- locate project context,
- dispatch work,
- monitor workers,
- retry transient failures,
- bring decisions back to you,
- and enforce project policy.

## Second Mate

A persistent manager for one project/domain.

Use when one First Mate has too many detailed project tasks.

Responsibilities:

- preserve project-specific context,
- own the local backlog,
- manage crew mates,
- and report meaningful outcomes upward.

## Crew Mate

A task worker.

Examples:

- investigate a bug,
- prototype a design,
- implement a feature,
- write tests,
- review architecture,
- perform market research.

## Dispatch policy

Select model/harness by:

- task category,
- difficulty,
- capability,
- cost/quota,
- and project importance.

## Project policy

Select validation by:

- blast radius,
- release behavior,
- reversibility,
- and consequence of failure.

## Fleet status

Use summaries such as Bearings/Ahoy to answer:

- What is running?
- What landed?
- What is blocked?
- What decision is waiting on me?
- What did I miss while reviewing something else?

This is what makes many-agent development manageable.

---

# 17. What I recommend you use as a beginner

Kun's newest setup is optimized for a very experienced engineer.

You should adopt the **logic** before adopting the full scale.

## Stage 1 - One app, one agent

Use:

- one repository,
- one coding agent,
- one `AGENTS.md`,
- one PRD,
- one architecture document,
- one end-to-end test plan.

Learn to make one agent produce a correct, validated feature.

## Stage 2 - One orchestrator + two workers

Use:

- one main agent as your First Mate,
- one frontend worker,
- one backend worker,
- isolated Git branches/worktrees,
- a third fresh-context reviewer when a feature is complete.

## Stage 3 - Parallel research + implementation

Add separate agents for:

- product research,
- architecture research,
- design prototype,
- implementation,
- validation.

Keep the number small enough that you can still understand every active objective.

## Stage 4 - Risk policies

Define:

- what can auto-merge,
- what needs you,
- what needs independent review,
- and what production actions require explicit approval.

## Stage 5 - Second Mates and multiple machines

Only add these when you are genuinely bottlenecked by coordination.

Do not add hierarchy because it looks advanced.

---

# 18. The beginner "golden path" for building an app

If you want one sequence to follow every time, use this.

## 1. Explain the problem

Do not code.

Output: `PRODUCT_BRIEF.md`

## 2. Research alternatives

Run product and technical research in parallel.

Output:

- `MARKET_RESEARCH.md`
- `TECHNICAL_OPTIONS.md`

## 3. Make architecture decisions

Review visual diagrams and tradeoffs.

Output:

- `ARCHITECTURE.md`
- `DATA_MODEL.md`
- `AUTH.md`
- `API.md`

## 4. Prototype user flows

Use HTML/wireframes.

Output:

- clickable prototype,
- list of approved journeys.

## 5. Freeze MVP scope

Write the PRD and explicitly list deferred ideas.

Output: `PRODUCT.md`

## 6. Create repository structure

Example:

```text
app/
backend/
docs/
tests/
infra/
```

Your real layout may differ. The important thing is that responsibilities are obvious.

## 7. Build the thinnest end-to-end slice first

Before building 20 screens, prove one complete path.

Example:

```text
sign in
  -> load user
  -> create one domain object
  -> persist it
  -> fetch it again
  -> display it
```

This exposes architecture mistakes early.

## 8. Expand features in vertical slices

For each feature:

```text
requirement
 -> UI
 -> API/domain logic
 -> database
 -> tests
 -> end-to-end evidence
```

Do not build the entire frontend first and "connect the backend later."

## 9. Validate independently

Use a fresh agent/context.

## 10. Review risk

Decide whether you need to inspect the code closely.

## 11. Merge through PR

Keep history and evidence.

## 12. Release and observe

Use real feedback to create the next tasks.

---

# 19. Prompts you can reuse

These prompts are my beginner-friendly adaptation of the patterns in the transcripts.

## A. Project kickoff

> You are my lead engineer. Do not write code yet. I will describe the app in plain English. Organize it into users, problems, goals, non-goals, major user journeys, data requirements, roles/permissions, integrations, assumptions, unknowns, and MVP acceptance criteria. Identify contradictions and ask yourself what is unnecessarily complex. Produce a concise product brief.

## B. Architecture research

> Research 2-4 viable architectures for this product. Compare frontend, backend, database, authentication, hosting, expected operating cost, security, deployment, backups, and testing. Optimize for simplicity, maintainability, robustness, and appropriate scale. Do not assume enterprise scale. Do not implement anything yet.

## C. Architecture review

> Turn the proposed architecture into a beginner-friendly review. Show a system diagram, auth flow, data model, API boundaries, source of truth for each major data type, deployment diagram, major failure modes, and open decisions. Explain every box in plain English.

## D. Anti-overengineering review

> Act as a skeptical principal engineer. Identify anything in this architecture that is premature, duplicated, unnecessarily expensive, or solving a problem we do not currently have. Do not remove security, data integrity, or maintainability boundaries just to make the system smaller.

## E. Implementation task

> Implement only this scoped feature. First read the product and architecture docs. Preserve the defined component boundaries. If the feature requires changing an architectural contract, stop and escalate the decision instead of silently redesigning the system. Add tests and update affected documentation.

## F. End-to-end validation

> Test this feature as a real user would experience it. Use the real application and real integration path wherever practical. Reproduce the original requirement from start to finish, test the important failure case, and provide evidence. Do not declare success based only on unit tests or compilation.

## G. Fresh-context review

> Review this change from scratch against the original requirement and architecture. Look for incorrect behavior, security/permission problems, data integrity issues, unnecessary complexity, missing error handling, test gaps, and architecture drift. Classify risk as low, medium, or high and explain why.

---

# 20. Architecture questions you should always be able to answer

Before allowing agents to build a large amount of code, make sure you can answer these in plain English.

### Product

- Who is the user?
- What is the primary job the app performs?
- What is explicitly not in the MVP?

### Frontend

- Which screens exist?
- Where does UI state live?
- Which data is cached locally?
- What happens offline?

### Backend

- Why does the backend exist?
- Which business rules does it enforce?
- Which operations can clients request?

### Data

- What are the core entities?
- Which entity owns which data?
- What must never be duplicated or become inconsistent?
- What needs an audit/history trail?

### Identity

- How does a user prove who they are?
- Which roles exist?
- What can each role read?
- What can each role modify?

### Integration

- Which third-party services exist?
- What happens when each is unavailable?
- Which secrets are required?

### Deployment

- How is production created?
- How is it updated?
- How is it backed up?
- How would you restore it?

### Quality

- What are the five most important end-to-end scenarios?
- What evidence proves each works?
- What failures would be high risk?

If an AI agent cannot explain these clearly, it should not be allowed to bury the answer inside generated code.

---

# 21. What not to copy blindly from Kun

## Do not copy his scale before you copy his discipline

Ten agents can produce ten times the confusion if:

- scope is ambiguous,
- architecture is undefined,
- branches are not isolated,
- acceptance criteria are weak,
- and nobody independently validates the work.

## Do not assume his exact technology stack is your stack

The wallet app uses choices appropriate to that project.

Your app may need a different:

- client,
- backend language,
- hosting provider,
- database,
- auth provider,
- or deployment model.

Copy the **decision process**, not the brand names.

## Do not let "cheap to build with AI" justify bad architecture

One of Kun's explicit global preferences is to avoid over-weighting development cost when making technical decisions.

AI can implement more robust solutions quickly.

That does not mean "use the most complex architecture."

It means:

> Choose based on quality, simplicity, robustness, scalability, and maintainability rather than assuming a good solution is too expensive to implement.

## Do not manually inspect everything either

If your only safety mechanism is reading every generated diff, your own attention becomes the bottleneck.

Instead, develop:

- architecture contracts,
- automated tests,
- independent reviews,
- evidence,
- and risk-based gates.

Then use code review where risk warrants it.

---

# 22. The most important architectural insight from all four transcripts

Kun's newest workflow works because he has **layers of control**.

```text
Layer 1 - Intent
What are we trying to accomplish?

Layer 2 - Product contract
What exactly should the user experience do?

Layer 3 - Architecture
Which components own which responsibilities?

Layer 4 - Agent instructions
How should workers operate in this repository?

Layer 5 - Isolation
Can workers make changes without colliding?

Layer 6 - Implementation
Can agents build the scoped change?

Layer 7 - Verification
Does the real product satisfy the original intent?

Layer 8 - Risk gate
How much human attention does this change deserve?

Layer 9 - Learning
What should the project remember so the mistake is not repeated?
```

Without these layers, "agentic development" is just fast code generation.

With them, it starts to look like an engineering organization.

---

# 23. Recommended workflow for you

Because you are approaching this without a traditional coding/CS background, I would use this operating rule:

> **Never let the agent's ability to implement something become the reason you skip understanding its boundaries.**

You do not need to understand every line of Swift, TypeScript, Python, SQL, or infrastructure code.

You **do** need to understand:

- which component is responsible,
- where the data lives,
- who is allowed to change it,
- what external services it depends on,
- what happens when something fails,
- and what test proves the feature works.

That level of understanding is enough to act as the captain.

For your first serious app, I would keep the active team to:

```text
You
 |
 v
First Mate / Lead Agent
 |
 +-- Product + architecture researcher
 +-- Implementation agent
 +-- Independent validation agent
```

Add frontend/backend parallel workers only after the architecture documents and API/data contracts are stable.

Add Second Mates only when you have multiple substantial projects or the First Mate itself becomes the coordination bottleneck.

---

# 24. One-page checklist

## Before coding

- [ ] Intent dump captured
- [ ] Market alternatives checked
- [ ] MVP/non-goals written
- [ ] UX journey prototyped
- [ ] Architecture diagram reviewed
- [ ] Data model reviewed
- [ ] Authentication/authorization explained
- [ ] API boundaries defined
- [ ] Infrastructure/cost decision made
- [ ] Deferred ideas explicitly listed

## Before parallel implementation

- [ ] Repository instructions exist
- [ ] Agents have isolated branches/worktrees
- [ ] Every task has acceptance criteria
- [ ] Shared contracts are written down
- [ ] No worker may silently redesign architecture

## Before calling a feature done

- [ ] Builds successfully
- [ ] Automated tests pass
- [ ] Real end-to-end scenario passes
- [ ] Important failure path tested
- [ ] Evidence captured
- [ ] Independent review completed
- [ ] Documentation updated
- [ ] Risk classified

## Before merging

- [ ] Human decision made for medium/high risk
- [ ] No unresolved architecture questions
- [ ] No secrets exposed
- [ ] Migration/rollback considered when relevant
- [ ] PR explains intent, change, tests, evidence, and risk

## After release

- [ ] Observe real behavior
- [ ] Capture user feedback
- [ ] Reproduce bugs end to end
- [ ] Feed reusable lessons into project memory
- [ ] Keep memory concise; move conditional procedures into skills

---

# 25. Final summary

Kun's latest workflow can be reduced to this:

```text
1. Tell one orchestrator what you want.
2. Let it split discovery into parallel research.
3. Review product and architecture visually before coding.
4. Write the decisions into durable project documentation.
5. Prototype the user journey.
6. Establish clear frontend/backend/data/auth boundaries.
7. Build infrastructure reproducibly and guard secrets.
8. Parallelize implementation only after contracts are clear.
9. Integrate against real systems early.
10. Define "done" with end-to-end behavior.
11. Validate in a separate fresh context.
12. Use evidence and risk to decide how much human review is needed.
13. Merge through a controlled PR process.
14. Feed real-world lessons back into project memory.
15. Scale from crew mates to Second Mates only when coordination becomes the bottleneck.
```

The core lesson is not that you need Kun's exact tools.

The core lesson is:

> **Use AI to increase implementation throughput, but use architecture, written intent, isolated work, independent validation, end-to-end evidence, and risk-based human judgment to keep that throughput under control.**

That is the part of his workflow that will help you build maintainable software even without a traditional CS degree.

---

# Source basis

- **Transcript 1:** Initial full agentic engineering workflow - terminal setup, agent memory/skills, Lavish, No Mistakes, long-running agents, worktrees/Treehouse, and First Mate.
- **Transcript 2:** Reproducible development environment - Nix/Nix-Darwin, Home Manager, terminal/editor configuration, Herder, and shared agent memory.
- **Transcript 3:** Real application built from scratch - market and technical research, UX prototype, PRD, design system, backend/infrastructure, controlled secrets, real authentication, and end-to-end MVP validation.
- **Transcript 4:** Advanced high-throughput workflow - model dispatch rules, quota-aware routing, Second Mates, multiple machines, per-project risk policies, Bearings/Ahoy summaries, and external issue intake.
