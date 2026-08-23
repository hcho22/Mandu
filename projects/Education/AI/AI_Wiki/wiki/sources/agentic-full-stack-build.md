---
type: source
title: "Building a Real Full-Stack App with an Agentic Workflow (Edie's Wallet)"
source-type: video
author: "Kun (ex-Meta, Microsoft, Atlassian; L8 principal engineer)"
url: "local"
date-ingested: 2026-08-01
date-created: unknown
tags: [agentic-engineering, orchestration, context-management, secrets, cost, design-system, e2e-validation, gpt, first-mate, lavish]
concepts: [one-orchestrator-agent, review-plans-as-artifacts, anchor-cost-in-real-pricing, agent-over-engineering, compaction-over-context-window, define-the-end-to-end-gate, design-system-not-a-design, ramble-then-structure, credential-vaults, model-selection, context-rot, sub-agents]
---

# Building a Real Full-Stack App with an Agentic Workflow

Kun (ex-Meta, Microsoft, Atlassian; L8 principal engineer) follows up his earlier agentic-engineering video by building a **real project from scratch, live**: *Edie's Wallet*, a virtual allowance tracker for his son.

This is the wiki's **second source from this author**, after [[building-products-with-agents]], and it is the practical companion to it.
The earlier source gave the principles ([[get-out-of-the-loop]], [[plan-code-validate]], [[fresh-context-review]]).
This one runs them end to end - empty terminal to a native iOS app signing in with a real Apple ID against a real backend on a self-hosted VPS - and, critically, shows the **three places the agent was wrong** and human judgment was still required.

**He never reads source code.**
He talks to a single orchestrator agent, reviews interactive artifacts, and steers with judgment calls.

**The thesis:** you don't need the most capable model for everything, you don't need to watch every tool call, and you don't need to manage context windows by hand.
What you *do* need is judgment about scope, cost, and where the agent is wrong.

## Key claims

### The workflow stack

| Layer | Tool |
|---|---|
| Terminal / session manager | Herder (agent-aware tmux replacement) |
| Orchestration | First Mate (one "captain-facing" agent plus delegated crewmates) |
| Harness + model | Pi agent running GPT-5.6 Luna at `xhigh` |
| Planning and review | Lavish (interactive HTML artifacts, diagrams, inline feedback) |
| Design | Claude Design (design system, Sonnet, not Opus) |
| Secrets | Atomic Vault (per-access authorization) |
| Infra | Hetzner VPS + OpenTofu + Cloudflare DNS |
| Guardrails (deferred) | No Mistakes (local validation pipeline) |

### One orchestrator, not many sub-agents

- **First Mate's model:** you (the "captain") talk to exactly **one** agent, and it juggles everything else by dispatching work to "crewmates."
This cuts cognitive load and context-switching burden.
- **Crewmates beat conventional sub-agents:** "It's really hard for you to look at what a sub-agent is doing, and it's also hard to steer a sub-agent."
Here a crewmate is just a normal agent session in an ordinary terminal tab that you can drop into and steer in plain language.
- When a crewmate finishes its report, First Mate closes the tab automatically.
- The real benefit he names: "I don't have the mental load to worry about which agent needs to be steered versus not. I just talk to First Mate."
- **Lay down ground rules in the very first prompt** - model, reasoning level, and harness for all delegated work - before any real work starts.
- He runs **calm mode** by default, which hides all tool calls, script runs, and skill invocations.
With the weaker models of one or two years ago, watching tool calls was genuinely useful for catching wrong turns; with today's models he rarely needs to, so the noise is no longer worth reading.

### The kickoff ramble

- He dictates roughly **3,000 characters** of unstructured requirements in one go, describing the problem, product, and constraints as they occur to him, then lets the agent rationalize it.
"I just ramble, try to explain everything I have in mind to First Mate, and let the agent figure things out."
- He requested **two parallel workstreams** in that ramble: market research (does this app already exist? if so he'd install it) and technical research (how would we build this end to end?).
- **Run market validation before writing code.**
- **State the non-negotiable constraints explicitly** in the ramble - virtual money only, multi-device cloud sync.
These are the assumptions that would otherwise get silently invented for you.
- **Mine the research twice.** The first pass answers "should we build this?"; a second pass over the same research answers "what should we steal?"
He rated the agent's filtering as good judgment, since it kept only ideas matching what he had already said he wanted.

### Reviewing plans as artifacts, not markdown

- The technical scout returned a **351-line `report.md`** - a wall of text he didn't want to read and, more importantly, **couldn't easily give targeted feedback on**.
So he had the review re-run in **Lavish**, which renders plans as interactive HTML artifacts where you can annotate any individual element, queue decisions, and view rendered architecture diagrams.
- **Diagrams expose hidden requirements.**
Reading the architecture diagram is how he caught auditing and encrypted export being baked into the plan: "Otherwise we wouldn't have discovered that there are some hidden requirements being baked into the plan."
- **The one place the model was actually wrong: cost.**
The plan recommended hosted Supabase Pro at **$25/month** and estimated self-hosted VPS at **$30-60/month**.
He pushed back on both - three users don't justify SaaS, and the VPS estimate contradicted his experience with Hetzner.
He queued feedback that a low-cost VPS should land around **$5/month**; the agent searched real cloud pricing, re-anchored, and came back recommending a budget VPS at **~$5.50/month**.
- **Make the agent anchor cost recommendations in searched, real pricing.**
Its default estimates can be wrong by an order of magnitude and quietly drive the architecture decision.
- Architecture principle settled in the artifact: **"the phone is a client, Postgres is the referee"** - narrow domain RPCs with membership checks, local cache, retry/reconcile.
- **Say "wireframes, not mocks."**
His first front-end attempt came back as a markdown file defining prototype *scope*, not something he could click.
The correction was real HTML prototypes in a Lavish artifact, explicitly wireframes rather than polished UX mocks.
- **When you're blocked waiting on one workstream, start another.**

### Context windows and compaction

- The session ran through **four auto-compactions with no visible degradation**.
At one point context sat at ~70% of 272K; after compaction it dropped to **9.5%**, and the agent still knew exactly what was being built.
- **"Compaction is really becoming an implementation detail that most people should not worry about anymore.**
Just let the agent run, let the agent compact when needed, and it will just keep going."
He relies entirely on auto-compaction and never triggers it proactively.
- **Claude's 1M-token context window doesn't make much practical difference here, because compaction quality matters more than raw window size.**
- Mechanics: Codex has a **server-side compaction** capability better than any other he knows of, but running GPT models in another harness like Pi does *not* get it automatically.
The fix is the `pi-openai-server-compaction` extension.
- **Persist important state to files. That's what makes compaction safe.**
Because dispatched crewmate tasks are documented to files, anything lost in compaction can be retrieved when the agent actually needs it.
- He caps requests at **272K** deliberately, citing an OpenAI-reported bug where requests exceeding the context cap are charged higher than usual.

### Secrets and permissions

- All secrets live in **Atomic Vault**, an open-source project by **Max Howell** (creator of Homebrew), which is why he trusts a young project.
- When an agent needs a secret, an authorization dialog shows *which agent* is asking and *what command* is proposed, and he approves or denies each one.
The token is passed through as an **environment variable**, so the agent can call APIs with it but never sees it in plaintext.
He deliberately did not use blanket allow-rules for his Hetzner account.
- **Why not `.env` files:** "Those environment files can be quite easy to get stolen... maybe the agent has published that secret to another public file, or sent it as part of a public API call."
Since you're not reading every tool call, **you have no idea when a secret has leaked**.
- **His permission philosophy:** give the agent a lot of permissions and capabilities, but anything touching **production** requires explicit authorization from you.
- He asks for declarative infra (**OpenTofu**) from the start so the VPS isn't a hand-configured snowflake.
- For browser work he lets the agent drive his **already-authenticated Chrome** via Chrome DevTools MCP, with remote debugging left on permanently.
He's comfortable delegating this specifically because "these are the things that wouldn't have a disastrous outcome."

### Design system, not a design

- He used **Claude Design** and deliberately created a **design system** rather than a one-off design, so future components and screens can be built without reinventing every element.
- Inputs: product name, GitHub repo URL, and a note that the repo contains no source code, only a README with requirements.
He told it to figure out the main screens and to **feel free to challenge any prescribed user experience**.
- **Letting the design agent challenge the PRD is what produced usable screens** rather than a literal transcription of his requirements.
- Model choice: Opus was overloaded so he ran **Sonnet**, and it worked out.
"Sonnet is not going to be able to come up with very, very clever solutions, but here I also don't think the problem is too complex."
- Ask explicitly for **iOS-formatted icon assets**; iOS has specific size/format requirements the design tool won't satisfy by default.

### The three corrections, and defining done

**1. Invented environment tiers.** The plan proposed deploying a *development* backend alongside production.
He cut it - one production MVP environment.
His note: **GPT models, especially 5.6, have a tendency to over-engineer.**

**2. The wrong hostname.** The iOS app was built while DNS was still being wired up, so the front-end agent pointed at the wrong address.
First Mate detected it, dispatched a worker to fix it, and told him as an FYI.

**3. The name assumption.** The brand is *Edie's Wallet*, but the UI copy assumed the user is named Edie ("Edie does not need an account").
Other families will use it.
The fix landed a configurable child nickname per family.

- **Watch for invented environment tiers, audit trails, and export features. Cutting them is where the human still adds value.**
- **Define the end-to-end gate explicitly.**
His MVP gate was: the iOS app running in the simulator, signing in with his **real Apple account**, connected to the **real backend on the VPS**.
Framing the test that way **forced the plan to expose the remaining gaps** - the app was still on mock data.
It converts vague "it's built" reports into a concrete remaining-work list.
- **The prompt he reuses constantly:** *"Try to do some end-to-end testing and figure out what the actual bug is. Don't ask me unless there is something only I can do."*
His reasoning: agents are very capable as long as they keep trying - "they just need some encouragement."
- **When to turn on No Mistakes** (his local validation pipeline): "If this is a code change you would otherwise have a human review for you, then you should turn on No Mistakes."
Prototypes: off. Real MVP code: on.
He needs it precisely *because* he isn't reviewing code himself.

### The closing thesis

- The entire full-stack app - market research, technical planning, backend, infrastructure, design system, and iOS app - was built with **GPT-5.6 Luna**, and with **Sonnet** rather than Opus for design.
- Across the whole session, **the single place where he felt the model wasn't smart enough was the VPS cost decision**, and that was because it reasoned from wrong pricing data rather than reasoned badly.

## Connections

- [[one-orchestrator-agent]] - the captain/crewmate model; a named alternative to fan-out [[sub-agents]].
- [[review-plans-as-artifacts]] - interactive artifacts over long markdown; the mechanism that makes [[read-what-the-agent-writes]] actually happen.
- [[anchor-cost-in-real-pricing]] - the one failure mode that survived a whole session; agent cost estimates silently drive architecture.
- [[agent-over-engineering]] - invented environment tiers, audit trails, and exports as the recurring thing a human must cut.
- [[compaction-over-context-window]] - **contradiction flagged** against [[context-rot]]: four clean auto-compactions, and compaction quality beating raw window size.
- [[define-the-end-to-end-gate]] - the explicit done-gate that converts "it's built" into a work list.
- [[design-system-not-a-design]] - build the vocabulary, not the screen; and invite the design agent to challenge the PRD.
- [[ramble-then-structure]] - 3,000 unstructured characters plus explicit non-negotiables beats a tidy spec.
- [[credential-vaults]] - **second source**, and the strongest statement of why `.env` files fail once you stop reading tool calls.
- [[model-selection]] - a full production build on a non-frontier model, with the one failure precisely located.
- [[sub-agents]] - **tempered**: steerability and observability are named as the weakness of the sub-agent pattern.
- [[phased-autonomy]] - permissions liberal everywhere, explicit authorization at the production boundary.
- [[get-out-of-the-loop]], [[plan-code-validate]], [[fresh-context-review]] - the same author's earlier principles, here executed.
- [[agent-testing-instructions]] - his reusable E2E prompt is this concept compressed to one sentence.
- [[client-never-touches-the-database]] - "the phone is a client, Postgres is the referee."
- [[agentic-engineering]] - the area this source most directly populates.
- [[openai]], [[anthropic]] - entities.

## Source

- **Author:** Kun (ex-Meta, Microsoft, Atlassian; L8 principal engineer); creator of First Mate, Lavish, and No Mistakes
- **Title:** Building a Real Full-Stack App with an Agentic Workflow - "Edie's Wallet" from empty terminal to working MVP
- **Format:** YouTube walkthrough (live build); ingested as a detailed summary with a caption-correction appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/agentic-workflow-real-project-summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-01

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries its own corrections appendix.
Tool and product names flagged `[?]` there and not independently verified: **Herder**, **Atomic Vault**, **Chrome DevTools MCP**, **Kiddo Bank**, **Tibo**, and "Apple's auth kit" (likely AuthenticationServices).
The author's GitHub handle and personal domain were not recoverable from the captions and were omitted rather than guessed.

Note that this author is the same "solo L8 builder" recorded in [[building-products-with-agents]]; that page identified him only by seniority, and this source names him as **Kun**.
