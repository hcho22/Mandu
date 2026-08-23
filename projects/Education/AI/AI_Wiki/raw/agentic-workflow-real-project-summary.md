# Building a Real Full-Stack App with an Agentic Workflow
### Summary of Kun's walkthrough — "Edie's Wallet" from empty terminal to working MVP

---

## Overview

Kun (ex-Meta, Microsoft, Atlassian; L8 principal engineer) follows up his 600,000-view agentic engineering workflow video by building a **real project from scratch, live**: *Edie's Wallet*, a virtual allowance tracker for his son that also teaches basic financial concepts (balance, loans, repayment, interest).

The session goes from an empty terminal to a working end-to-end MVP: a native iOS app signing in with a real Apple ID against a real backend on a self-hosted VPS. Notably, **he never reads source code** — he talks to a single orchestrator agent, reviews interactive artifacts, and steers with judgment calls.

**The stack of the workflow itself:**

| Layer | Tool |
|---|---|
| Terminal / session manager | Herder (agent-aware tmux replacement) |
| Orchestration | First Mate (one "captain-facing" agent + delegated crewmates) |
| Harness + model | Pi agent running GPT-5.6 Luna at `xhigh` reasoning |
| Planning & review | Lavish (interactive HTML artifacts, diagrams, inline feedback) |
| Design | Claude Design (design system, Sonnet — not Opus) |
| Secrets | Atomic Vault (per-access authorization) |
| Infra | Hetzner VPS + OpenTofu + Cloudflare DNS |
| Guardrails (deferred) | No Mistakes (local validation pipeline) |

**The thesis:** you don't need the most capable model for everything, you don't need to watch every tool call, and you don't need to manage context windows by hand. What you *do* need is judgment about scope, cost, and where the agent is wrong.

**Callout legend:** 💡 Tip · 🛠️ Tool · 📏 General Rule · 💬 Speaker Opinion · ⚠️ Caution

---

## Table of Contents

1. [Environment and Setup](#1-environment-and-setup)
2. [The Kickoff Ramble](#2-the-kickoff-ramble)
3. [Parallel Scouts, Quotas, and Fast Mode](#3-parallel-scouts-quotas-and-fast-mode)
4. [Market Research and Inspiration Mining](#4-market-research-and-inspiration-mining)
5. [Technical Planning in Lavish](#5-technical-planning-in-lavish)
6. [Front-End Prototyping](#6-front-end-prototyping)
7. [Repo, PRD, and the No Mistakes Rule](#7-repo-prd-and-the-no-mistakes-rule)
8. [Context Windows and Compaction](#8-context-windows-and-compaction)
9. [Design System with Claude Design](#9-design-system-with-claude-design)
10. [Backend Build: Secrets, VPS, Infrastructure as Code](#10-backend-build-secrets-vps-infrastructure-as-code)
11. [Apple Developer Setup and DNS via Browser Control](#11-apple-developer-setup-and-dns-via-browser-control)
12. [Correcting the Agent: Over-Engineering and Assumptions](#12-correcting-the-agent-over-engineering-and-assumptions)
13. [Backend Architecture Review](#13-backend-architecture-review)
14. [End-to-End Validation and Wrap-Up](#14-end-to-end-validation-and-wrap-up)
15. [Appendix: Caption Corrections](#15-appendix-caption-corrections)

---

## 1. Environment and Setup

He starts from an empty terminal — tools installed, no project files yet.

**Herder** is his session manager, a replacement for tmux. Its advantage: it *understands agents*, where traditional terminal multiplexers only understand terminals, panes, and shells. It provides an agents side panel (showing working directory and which harness each session runs) and a keybind that opens an agent search pane for jumping between or searching sessions by title.

**First Mate** is his own open-source project. The model: you (the "captain") talk to exactly one agent — the First Mate — and it juggles everything else by dispatching work to "crewmates." This cuts cognitive load and context-switching burden.

**Setup is trivial:** `git clone` the First Mate repo, `cd` into it, and launch your agent inside it. That's it.

For the harness he uses the **Pi agent** — his favorite for running any model that isn't Claude. Default was GPT-5.6 at `xhigh`; he deliberately switched to **GPT-5.6 Luna** at `xhigh` to make the session harder and more uncertain.

**First prompt (ground rules):** create a new local repo called *Edie's Wallet*, add a dummy README, make an initial commit — and establish that *every task and every crewmate is dispatched to a Pi agent running GPT-5.6 Luna at `xhigh`*.

> 💬 **Speaker Opinion** — "A lot of the time we try to use the best model possible for everything, because that's just going to give us better results. But actually you don't really need the best model for everything — you can get a lot out of these more efficient models."

> 💡 **Tip — Calm mode.** First Mate ships a `calm mode` (currently Pi agent only) that hides all tool calls, script runs, and skill invocations. The terminal shows only your prompt and First Mate's response. He runs this by default.

> 💬 **Speaker Opinion** — With the weaker models of one or two years ago, watching tool calls was genuinely useful for catching wrong turns and steering. With today's models he rarely needs to, so the noise is no longer worth reading.

> 📏 **General Rule** — Lay down ground rules (model, reasoning level, harness for all delegated work) in the very first prompt, before any real work starts.

---

## 2. The Kickoff Ramble

He dictates roughly **3,000 characters** of unstructured requirements in one go — describing the problem, the product, and the constraints as they occur to him, then letting the agent rationalize it.

**What the ramble contained:**

- **Problem:** allowance is currently tracked in a notebook or from memory; it breaks down once there are multiple rules for earning and spending.
- **Educational goal:** introduce basic financial concepts gradually and naturally — balance, loans, how credit cards work, making repayments, interest on savings.
- **Platform:** iOS only for now (his son mostly uses an iPad; he also has a Mac).
- **Modes:** parent mode (deposit, manage withdrawals) and child mode (read-only view of balance, loans, activity).
- **Hard constraint:** the money is **virtual** — a tracker, not real money.
- **Data:** must be portable and cloud-stored, since the parent manages from a phone while the child uses an iPad, and devices change.
- **Two parallel workstreams requested:** (1) market research — does an app like this already exist? If so he'd just install it; (2) technical research — how would we build this full stack, end to end?

> 💡 **Tip — Just ramble.** "This is typically how I kick off a new project. I just ramble, try to explain everything I have in mind to First Mate, and let the agent figure things out."

> 📏 **General Rule** — Run market validation before writing code. If the app already exists exactly as specified, install it instead of building it.

> ⚠️ **Caution** — State the non-negotiable constraints explicitly in the ramble (virtual money only, multi-device cloud sync). These are the assumptions that would otherwise get silently invented for you.

---

## 3. Parallel Scouts, Quotas, and Fast Mode

First Mate spun up two Herder tabs — market research and technical research — and confirmed both crewmates were running GPT-5.6 Luna at `xhigh` as instructed.

**Context window:** the GPT model default cap here is **272K tokens**. He watches the token counter as a liveness signal — if it's moving, the agent isn't stuck.

**Quota tracking:** a menu bar widget tracks all subscription quotas in one place — Claude, Codex, and a Kimi subscription (his Grok quota was already used up). He noted a Codex quota reset from **Tibo**, which is why he still had headroom.

**Codex fast mode:** he enabled it with `codex fast on` via the Codex fast extension in Pi. Checking another session showed it was already on there too — the setting applies across all sessions.

**Crewmate observability:** crewmates are ordinary agents running in ordinary Herder tabs. You can drop into any one of them and steer it in plain language.

> ⚠️ **Caution — Context cap and billing.** He caps requests at 272K deliberately. OpenAI reported a bug where requests exceeding the context cap are charged higher than usual — he cites this as a reason people complain that "Codex is draining my quota very quickly."

> 💡 **Tip — Fast mode is a latency-for-cost trade.** He normally leaves it off because GPT models are already fast; he turned it on only because it was a live demo. Note that it affects *all* sessions, not just the current one.

> 💬 **Speaker Opinion** — First Mate's crewmates beat conventional sub-agents: "It's really hard for you to look at what a sub-agent is doing, and it's also hard to steer a sub-agent." Here, a crewmate is just a normal agent session you can talk to.

> 💡 **Tip — Automatic teardown.** When a crewmate finishes its report, First Mate closes the tab. Previously he'd been manually creating terminal tabs, checking which agent was done, collecting reports, and closing tabs himself.

---

## 4. Market Research and Inspiration Mining

**The market scout's finding:** no current iOS app matches the full brief — virtual-only money, parent-controlled writes, child read-only. It listed closest references (e.g. a Kiddo Bank–style product, web-only) with their individual strengths, and recommended prototyping Edie's Wallet rather than installing a replacement.

Later, while other work ran, he sent the research *back through* the agent: analyze the market research and extract concepts from competing products worth drawing inspiration from.

**Concepts surfaced:**

- Read-only kids view
- Money buckets — spend / save / give goals
- A meaningful activity timeline
- Approval requests — the child proposes actions, the parent approves
- **Lessons attached to real actions** — after a deposit explain balance; before spending explain trade-offs; when borrowing explain principal
- Virtual loan simulator
- Flexible allowance rules (currently handled manually in his household)
- Gentle gamification
- Avoid: heavy ads

**Recommended inspiration mix:** privacy, iPad-first design, read-only child mode, family ledger, recurring allowance, contextual lessons.

> 💬 **Speaker Opinion — Gamification.** Mixed feelings: it definitely gets kids more interested, but it "feels a little bit manipulative to kids."

> 💡 **Tip — Mine the research twice.** The first pass answers "should we build this?" A second pass over the same research answers "what should we steal?" He rated the agent's filtering as good judgment — it kept only the ideas that matched what he'd already said he wanted.

---

## 5. Technical Planning in Lavish

The technical scout's initial recommendation: **native SwiftUI iPad app, Supabase, Postgres row-level security, an immutable server-side ledger, SwiftData local cache, no real-money integrations** (with CloudKit also raised).

The report was a **351-line `report.md`** — a wall of text he didn't want to read and, more importantly, couldn't easily give targeted feedback on. So he asked First Mate to run the review in **Lavish** instead.

**What Lavish is:** his own tool that renders plans as interactive HTML artifacts. You can annotate any individual element with feedback, queue decisions, and view rendered architecture diagrams. The Lavish editor also auto-fixes layout problems in agent-generated artifacts before presenting them.

**The cost argument — the one place the model was wrong.** The revised plan recommended hosted Supabase Pro at **$25/month**, and estimated self-hosted VPS at **$30–60/month**. He pushed back on both: three users (him, his wife, his son) don't justify paying for SaaS, and the VPS estimate contradicted his experience with Hetzner. He queued feedback that a low-cost VPS should land around **$5/month**. The agent searched real cloud pricing, re-anchored, and came back recommending a **budget VPS at ~$5.50/month**, plus roughly **20% more for backups**. Decision: VPS.

**Other decisions made in the artifact:**

- **Auth:** Sign in with Apple now; Google sign-in later for wider reach — not today, today is an MVP for one child.
- Keep an **identities table** so multiple auth identities can link to one account.
- **Architecture principle:** "the phone is a client, Postgres is the referee" — narrow domain RPCs with membership checks, local cache, retry/reconcile.
- **Scope cuts:** deleted audit events and encrypted export as over-engineering for the initial scope.
- **Child sign-in:** parent-managed profile, with a parent-set PIN gating parent-only actions.
- **Recovery:** daily backups plus nightly export, instead of expensive point-in-time recovery.

> 💬 **Speaker Opinion** — "I don't want to jump to the conclusion that we need to pay for SaaS." His experience with Supabase is that once complexity grows it gets expensive — and with zero users, scale isn't the problem to solve. He also liked the agent's own framing, "buy operational simplicity before buying infrastructure," while still overriding its conclusion.

> 📏 **General Rule** — Make the agent anchor cost recommendations in searched, real pricing. Its default estimates can be wrong by an order of magnitude and quietly drive the architecture decision.

> 💡 **Tip — Review plans as artifacts, not markdown.** Interactive review lets you queue per-element feedback and decisions instead of writing "change section 4" against a 351-line file.

> ⚠️ **Caution — Diagrams expose hidden requirements.** Reading the architecture diagram is how he caught auditing and encrypted export being baked into the plan: "Otherwise we wouldn't have discovered that there are some hidden requirements being baked into the plan."

---

## 6. Front-End Prototyping

While backend research ran, he opened a second workstream: prototype the front end so the user experience can be nailed in parallel.

**First result was wrong-shaped.** The UX crewmate produced a markdown file defining prototype *scope* — not something he could click. His correction: build **real HTML prototypes in a Lavish artifact**, no iOS code required, focused on **wireframes** — screens, concepts, user flow — explicitly *not* polished UX mocks.

**Screens in the journey map:** welcome, family setup, pair device, PIN gate, parent dashboard, child wallet, activity detail, allowance rule, loan and repayment, lesson path. The prototype also included controls to go offline, sync pending changes, and reset the prototype.

**Decisions answered in the artifact:**

- Should the child be able to request points? **No** — if he wants points, he asks in person.
- Where do loans live? **A card on the wallet detail flow.**
- How should lessons open? **A short linear starter path.**

**Feedback he gave:**

- Use the **local currency (USD)**, not an invented unit like "tokens" or "points" — that's what his son already receives as allowance.
- The child wallet already lists recent activity, yet there's a separate "recent activity" button — redundant.
- Don't rebuild the prototype; just absorb the feedback and write a **PRD as a markdown file in the repo** (as the README for now).

> 💡 **Tip — Say "wireframes, not mocks."** Asking explicitly for unpolished wireframes gets a playable prototype fast; UI polish comes later, from the design system.

> 📏 **General Rule** — When you're blocked waiting on one workstream, start another. He repeatedly prototypes multiple things at once to make fast progress on full-stack projects.

> 💬 **Speaker Opinion** — The device-pairing flow was an unprompted win: "Oh, pairing means another device. That's actually pretty thoughtful," since he'd be setting up on his iPhone while his son uses the iPad.

---

## 7. Repo, PRD, and the No Mistakes Rule

The README became the PRD — problem, target user, settled decisions. He then had the work committed and the repo published to GitHub as a **public** repo.

**Identity check:** First Mate asked which GitHub account to use before creating the remote. He approved of the question — multiple identities can be logged into the GitHub CLI at once.

**Workflow choice:** direct PR workflow, no **No Mistakes** yet.

**What No Mistakes is:** another of his tools — a local validation pipeline that runs against every single code change, to build confidence that generated code is mergeable. He needs it precisely *because* he isn't reviewing code himself.

**The rename.** The product had been spelled "Eddie's Wallet"; the correct spelling is **Edie**. He said so in one sentence, and First Mate handled the local repo rename, the GitHub repo rename, the project description, and a PR correcting every occurrence in the README.

He also told First Mate that PRs don't need his approval for now — once it has reviewed a PR, it can merge — with a stronger approval flow after the MVP is built.

> 📏 **General Rule — When to turn on No Mistakes.** "If this is a code change you would otherwise have a human review for you, then you should turn on No Mistakes. If it's something you work by yourself and don't want a human peer review for, then you wouldn't want to turn on No Mistakes either." Prototypes: off. Real MVP code: on.

> 💬 **Speaker Opinion** — On the rename: "This is the thing I really love about First Mate — it takes care of things. I don't need to think about what are all the things I have to do to get things like this corrected." Do I rename the local repo first? The upstream? He no longer has to sequence it.

---

## 8. Context Windows and Compaction

The session ran through **four auto-compactions** with no visible degradation. At one point context sat at ~70% of 272K; after compaction it dropped to **9.5%**, and the agent still knew exactly what was being built.

**Compaction mechanics he flags:**

- Codex has a **server-side compaction** capability that works better than any other he knows of.
- When running GPT models in another harness like the Pi agent, that server-side compaction *doesn't* happen automatically — Pi uses its own compaction algorithm by default.
- The fix: install the **`pi-openai-server-compaction`** extension in the Pi agent, and GPT models running in Pi will use OpenAI's server-side compaction. Better for long-running tasks.

He also credits First Mate: because dispatched crewmate tasks are documented to files, anything lost in compaction can be retrieved when the agent actually needs it.

> 💡 **Tip** — Install `pi-openai-server-compaction` if you run GPT models in the Pi agent on long tasks.

> 💬 **Speaker Opinion** — "Compaction is really becoming an implementation detail that most people should not worry about anymore. Just let the agent run, let the agent compact when needed, and it will just keep going." He relies entirely on auto-compaction and never triggers it proactively.

> 💬 **Speaker Opinion** — Claude's 1M-token context window doesn't make much practical difference here, because compaction quality matters more than raw window size.

> 📏 **General Rule** — Persist important state (task assignments, decisions, reports) to files. That's what makes compaction safe.

---

## 9. Design System with Claude Design

He used **Claude Design**, and deliberately created a **design system** rather than a one-off design: once the system is established, future components and screens can be built and changed without reinventing every element, and consistency is guaranteed from that point on.

**Inputs he gave it:** product name (Edie's Wallet), the GitHub repo URL, and a notes field explaining that the repo contains no source code — only a README with the requirements. He told it to figure out the main screens, and to **feel free to challenge any prescribed user experience** and use its own judgment. Target feel: fun, educational, friendly for kids; good control and transparency for parents.

**Model choice:** Opus was overloaded, so he ran **Sonnet**. He wanted to use Fable but chose to stay frugal — and Sonnet worked out.

**The feedback loop:**

1. Reviewed the generated design system: brand icon, wordmark, a gold/golden palette (his son likes gold), neutrals.
2. Flagged a component where text wasn't centered — fixed on the next pass.
3. Main critique after clicking through real screens: **it doesn't feel like a children's app.** Asked it to lean into fun and friendly.
4. Requested **app icon options** to review. Chose the piggy bank over wallet and coin concepts; asked for the piggy to be bigger and for **icon images formatted for direct use in an iOS app**.
5. Result: bouncing piggy, large type, balance clearly visible — "good enough."

He then exported the whole thing as a **project archive zip**, and handed the local download path to First Mate to copy into the repo and build against.

> 💡 **Tip — Create a design system, not a design.** It's the difference between one screen and a consistent, extensible UI vocabulary.

> 💡 **Tip — Let the design agent challenge the PRD.** Explicitly inviting it to override prescribed UX is what produced usable screens rather than a literal transcription of his requirements.

> ⚠️ **Caution** — Ask explicitly for iOS-formatted icon assets; iOS has specific size/format requirements the design tool won't satisfy by default.

> 💬 **Speaker Opinion** — On using Sonnet: "Sonnet is not going to be able to come up with very, very clever solutions, but here I also don't think the problem is too complex."

---

## 10. Backend Build: Secrets, VPS, Infrastructure as Code

First Mate created **three parallel workstreams**: backend API, DB schema and boundary, and VPS foundation with backups and deployment automation.

**Secrets — Atomic Vault.** He keeps all secrets in Atomic Vault, an open-source project built by **Max Howell**, the creator of Homebrew — which is why he trusts a young project. He's been giving Max feedback from his own usage.

How it works in practice: when an agent needs a secret, an authorization dialog shows *which agent* is asking and *what command* is proposed, and he approves or denies each one. The token is passed through as an **environment variable**, so the agent can call APIs with it but never sees it in plaintext. Blanket allow-rules are possible; he deliberately didn't use them for his Hetzner account.

**Hetzner.** He told First Mate his API token was stored as `HCLOUD_TOKEN`. It provisioned one dedicated server quickly, at a monthly cost (before taxes and traffic) well below the earlier $30–60 estimate.

**Infrastructure as code.** He interrupted to redirect the VPS workstream toward **OpenTofu**, so the machine and resources are declared in a file that can be audited, committed, and source-controlled. First Mate redirected the relevant workstream without him needing to know which agent was affected.

> ⚠️ **Caution — Why not `.env` files.** "Those environment files can be quite easy to get stolen... maybe the agent has published that secret to another public file, or sent it as part of a public API call." Since you're not reading every tool call, you have no idea when a secret has leaked.

> 📏 **General Rule — His permission philosophy.** Give the agent a lot of permissions and capabilities — but anything touching **production** requires explicit authorization from you. "As we delegate more and more things to agents, this is going to become more and more important."

> 💡 **Tip** — Ask for declarative infra (OpenTofu / Terraform-style) from the start so the VPS isn't a hand-configured snowflake.

> 💬 **Speaker Opinion** — The real benefit of the First Mate pattern: "I don't have the mental load to worry about which agent needs to be steered versus not. I just talk to First Mate."

---

## 11. Apple Developer Setup and DNS via Browser Control

He asked for the **exact steps and URLs** for the Apple Developer work — then decided to delegate that too: First Mate drove his actual Chrome window using **Chrome DevTools MCP**.

**Prerequisite:** Chrome's **remote debugging** must be enabled beforehand (under Inspect). Without it, the agent gets an isolated browser window without your credentials. He leaves it on permanently; each new agent session requests permission before taking control.

**What happened:** the first attempt failed because the app's display name was invalid. He fed back the error he'd seen on screen — the agent had missed the dialog — and told it to check for disallowed characters and retry. It then chose the bundle ID, confirmed the team ID, registered the app ID, and added the **Sign in with Apple** capability.

**DNS and HTTPS.** He pointed the agent at his Cloudflare account, where he manages domains and DNS. The token was in the same vault as `CLOUDFLARE_API_TOKEN` (he initially mis-stated the name and corrected himself). The agent added a DNS record for a subdomain of his own domain pointing at the VPS, and the backend came up live on verified HTTPS.

**A transcription aside:** his own dictation contained a misspelling of the app name (the Whisper model's transcription is usually good enough but does slip). Luna inferred the correct spelling from prior context and used the right domain anyway.

**Deployment automation** was deferred. His usual approach: put all devices and the VPS on a single **Tailscale** subnet so they can talk to each other, and optionally add GitHub Actions runners to the same subnet.

> 💡 **Tip** — Turn on Chrome remote debugging once and leave it on, so agents can drive your already-authenticated browser rather than a blank one.

> ⚠️ **Caution — Pick delegable browser tasks.** He's comfortable handing over the browser here specifically because "these are the things that wouldn't have a disastrous outcome."

> 💡 **Tip — Feed back what you saw.** When the agent stalls on a web form, tell it the error message you observed — it may have missed the dialog entirely — and tell it to retry rather than doing the clicks yourself.

---

## 12. Correcting the Agent: Over-Engineering and Assumptions

Three interventions where human judgment was still required:

**1. Environment tiers.** The implementation plan proposed deploying a *development* backend alongside production. He cut it: one production MVP environment, no dev/prod split. His note — GPT models, especially 5.6, have a tendency to over-engineer. For a new app on a VPS nobody knows about, there's no reason for environment tiers.

**2. The wrong hostname.** The iOS app was built while DNS was still being wired up, so the front-end agent didn't know the final record and pointed at the wrong address. First Mate detected it, dispatched a worker to fix it, and told him as an FYI — no action needed.

**3. The name assumption.** The brand is *Edie's Wallet*, but the UI copy assumed the user is named Edie ("Edie does not need an account"). Other families will use it. He asked for neutral terms; First Mate dispatched a parallel crewmate to make the change while testing continued, landing a **configurable child nickname per family**.

**Defining done.** He set an explicit MVP gate: the iOS app running in the simulator, signing in with his **real Apple account**, connected to the **real backend on the VPS**. Framing the test this way forced the plan to expose the remaining gaps — the app was still on mock data.

> 📏 **General Rule** — Define the end-to-end gate explicitly ("simulator + real Apple sign-in + real backend"). It converts vague "it's built" reports into a concrete remaining-work list.

> 💡 **Tip — The prompt he reuses constantly.** *"Try to do some end-to-end testing and figure out what the actual bug is. Don't ask me unless there is something only I can do."* His reasoning: agents are very capable as long as they keep trying — "they just need some encouragement."

> ⚠️ **Caution** — Watch for invented environment tiers, audit trails, and export features. Cutting them is where the human still adds value.

---

## 13. Backend Architecture Review

With the bug fix in flight, he opened another parallel workstream: review the deployed backend **in Lavish**, focusing on three things — what API endpoints were exposed, how authentication is handled, and what DB schema was created. He never opened the source.

**What the review showed:**

- **Request flow:** iOS client → HTTPS → **Fastify** API, with a health endpoint; Apple passes identity tokens to the issuer; a session service (bearer hash) and a wallet service sit behind it; data persists in Postgres.
- **Endpoints are domain operations, not generic table writes** — Apple authentication, `me`, family, wallet, child view — each rendering a different screen's data shape.
- **Schema:** parent identities, sessions, families (connecting parents to children, supporting multiple children), children, wallets, loans, ledger entries.
- **Verdict:** nothing over-engineered, boundaries narrow, "pretty straightforward actually."

> 💡 **Tip — Audit without reading code.** Reviewing endpoints, auth flow, and schema in a visual artifact is enough to catch over-engineering and confirm boundaries.

> 📏 **General Rule** — Prefer narrow domain RPCs with membership checks over generic table access from the client.

---

## 14. End-to-End Validation and Wrap-Up

The final test, in the iOS simulator:

1. **Sign in with Apple** — worked, using his real Apple account.
2. Parent view: added **$10**, reviewed, recorded — balance updated.
3. Child view: **$10** visible.
4. Signed out and back in — data returned from the server, confirming cloud persistence and the full request path.

**Next steps he named:** a **TestFlight** build installed on his son's iPad for real use, and further UI iteration to foreground the child view and make the parent view more hidden.

**Closing thesis:** the entire full-stack app — market research, technical planning, backend, infrastructure, design system, and iOS app — was built with **GPT-5.6 Luna**, and with **Sonnet** rather than Opus for design. Across the whole session, the single place where he felt Luna wasn't smart enough was the **VPS cost decision**, and that was because it reasoned from wrong pricing data.

> 💬 **Speaker Opinion** — "We built this real full-stack app from scratch using GPT-5.6 Luna, and we couldn't even use Opus for Claude Design — we used Sonnet, and it worked out pretty well."

> 💬 **Speaker Opinion — On talking to agents.** He noticed himself apologizing to the agent for a wrong secret name: "We actually waste a lot of tokens saying things that are not technically necessary, but it makes me feel good by saying it."

---

## 15. Appendix: Caption Corrections

Auto-caption errors corrected in this summary. Items marked **[?]** are best-guess reconstructions where the intended term is uncertain.

| In the transcript | Corrected to | Note |
|---|---|---|
| "T-max" | tmux | Terminal multiplexer |
| "aentic" | agentic | — |
| "PI agent" | Pi agent | Agent harness |
| "GP 5.6", "GBT 5.6" | GPT-5.6 | — |
| "on X high" | `xhigh` | Reasoning effort level |
| "not cloud", "cloth quota" | not Claude, Claude quota | — |
| "cloud design" | Claude Design | — |
| "set", "Sonet" | Sonnet | — |
| "codeex" | Codex | — |
| "com mode" | calm mode | First Mate feature |
| "Gro" | Grok | — |
| "superbase" | Supabase | — |
| "postgress" | Postgres | — |
| "swift data" | SwiftData | — |
| "cloudkit" | CloudKit | — |
| "fastify" | Fastify | Node.js web framework |
| "Hner", "Hester" | Hetzner | VPS provider |
| "Hcloud token" | `HCLOUD_TOKEN` | Hetzner API token |
| "cloudflare API_key" | `CLOUDFLARE_API_TOKEN` | Speaker self-corrected on camera |
| "open tofu" | OpenTofu | — |
| "tail scale" | Tailscale | — |
| "test flight" | TestFlight | — |
| "god rail" | guardrail | — |
| "explain principle" | explain principal | Loan terminology |
| "revealed PRs" | reviewed PRs | — |
| "MVP DOM" | MVP done | — |
| "Edd's Wallet", "Eddie's Wallet" | Edie's Wallet | Speaker explicitly corrects this on camera |
| "PI openAI server compaction" | `pi-openai-server-compaction` | Pi agent extension |
| "Chrome DevTools Axi" | Chrome DevTools MCP **[?]** | Browser-control integration |
| "autonomic bolt", "atomic vault" | Atomic Vault **[?]** | Secrets manager by Max Howell |
| "Herder" | Herder **[?]** | Kept as heard; agent-aware tmux replacement |
| "baby menu widget" | menu bar widget **[?]** | Quota-tracking widget |
| "kiddo bank" | Kiddo Bank **[?]** | Competitor app name |
| "Tibo" | Tibo **[?]** | Person granting Codex quota resets |
| "Apple's off kit" | Apple's auth kit **[?]** | Likely AuthenticationServices |
| "kunchen go ID", "kunchenjoid.com", "kenjoid.com" | GitHub handle / personal domain **[?]** | Spelling not recoverable from captions; omitted rather than guessed |

---

*Summary of a YouTube tutorial by Kun. All tool names, figures, and quotes preserved as spoken; editorial corrections documented above.*
