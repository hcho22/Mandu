# Graph Engineering, Clearly Explained

**Source:** *Startup Ideas Podcast* — hosted by Greg Isenberg

## Overview

Greg Isenberg breaks down "graph engineering," a term trending on Twitter/X, and explains why — unlike some viral AI buzzwords — it's a genuinely useful mental model. His core argument: prompt engineering improves the *question* you ask AI, context engineering improves the *information* you give AI, but graph engineering improves the *work design around* AI — turning a single messy AI chat into a structured workflow of steps, parallel jobs, checks, and human approvals. The episode covers the vocabulary (jobs, arrows, state), the difference between knowledge graphs and agent graphs, a worked startup-research example, three levels of implementation (manual → file-based → automated), and real-world applications in customer support, content creation, and coding.

---

## Table of Contents

1. [What Is Graph Engineering?](#1-what-is-graph-engineering)
2. [Basic Vocabulary: Jobs, Arrows, State](#2-basic-vocabulary-jobs-arrows-state)
3. [Two Types of Graphs: Knowledge Graphs vs. Agent Graphs](#3-two-types-of-graphs-knowledge-graphs-vs-agent-graphs)
4. [When Should You Use Graph Engineering?](#4-when-should-you-use-graph-engineering)
5. [Worked Example: Should I Launch a Shopify Bookkeeping Product?](#5-worked-example-should-i-launch-a-shopify-bookkeeping-product)
6. [Three Levels of Building a Graph](#6-three-levels-of-building-a-graph)
7. [Real-World Applications](#7-real-world-applications)
8. [The Big Mistake to Avoid](#8-the-big-mistake-to-avoid)
9. [The Compounding Value: Graphs Create Memory](#9-the-compounding-value-graphs-create-memory)
10. [How to Get Started This Week](#10-how-to-get-started-this-week)

---

## 1. What Is Graph Engineering?

> 💡 **General Rule:** Prompt engineering = better questions. Context engineering = better information. **Graph engineering = better design of the work itself**, so it doesn't all live inside one giant AI chat.

**The problem with the "normal" approach:** You open a chat, ask "Should I build this idea?", and get a confident-sounding answer with market size, competitors, and a go-to-market plan. It *feels* like research was done. But in reality, **one model in one pass** decided what mattered, researched it, interpreted the evidence, wrote the recommendation, *and* graded its own confidence — all without any checks.

**The graph version** breaks this into distinct roles:
- A **planner** breaks the question into angles
- Separate **researchers** look at customer, competitors, distribution, pricing, risk
- A **skeptic** tries to kill weak findings
- A **merger** turns surviving evidence into a one-page recommendation
- A **human** approves the decision before acting

> 🗣️ **Speaker Opinion:** Isenberg says graph engineering is one of the few viral AI terms that's actually useful, unlike hype-driven phrases that "make everyone feel behind."

---

## 2. Basic Vocabulary: Jobs, Arrows, State

A **graph** = jobs connected by arrows.
- **Job** = a step in the workflow
- **Arrow** = what happens next
- **State** = the shared notes moving through the workflow ("what does the system know so far")

**Example — Customer Support:** Answering a ticket isn't one step. It's: understand the issue type → check account history → search docs/policy → draft a response → decide if a human needs to review it before sending. Drawing these out and connecting them *is* a graph.

**Example — Content (YouTube episode):** research → thesis → examples → hook → script → title ideas → thumbnail directions → Excalidraw → final "does this sound human?" pass. Some steps are sequential (thesis before script), others can run in parallel (one researcher finds examples while another finds counterarguments), then merge back into the script.

> ⚠️ **Caution:** Chat interfaces make everything feel sequential (research → summary → draft → edits → titles), which works for simple tasks but gets slow, fuzzy, and hard to trust once work has multiple interdependent pieces.

> 💡 **Tip:** Think of a graph like designing a small team: one person plans, several work in parallel, one checks the work, one merges it, and a human approves the final step.

---

## 3. Two Types of Graphs: Knowledge Graphs vs. Agent Graphs

This is where most confusion about "graph" in AI comes from — there are two distinct meanings.

### Knowledge Graphs
Help AI reason over **relationships between things** — e.g., *this customer works at this company → this company uses this product → this product connects to this tool → this support issue relates to this feature → this feature is owned by this team.*

- Solves a limitation of normal RAG: RAG retrieves text chunks that look similar to the query, but struggles when the answer requires connecting different people, companies, topics, claims, and events.
- **Tool mentioned:** Microsoft GraphRAG

### Agent Graphs
About **how work moves** — planner hands off to researchers who work in parallel, a skeptic checks findings, a synthesizer merges, a human approves.

> 💡 **General Rule:** *Knowledge graphs help AI understand how information connects. Agent graphs help AI understand how work should move.* The best systems eventually use both.

> 🗣️ **Speaker Opinion:** Isenberg notes this episode is intentionally focused on **agent graphs** because that's the version usable *today* by founders, creators, operators, and small teams.

---

## 4. When Should You Use Graph Engineering?

> 💡 **General Rule:** Use a graph when the work has **multiple steps**, some steps **can run in parallel**, and the final output **needs checking** before it matters.

**Skip it for:** brainstorming 10 names, summarizing a short email.

**Use it for:** deep research, go-to-market plans, support ticket triage, code review, sales call prep, customer feedback synthesis, recurring content production.

**Shape to picture:** a diamond — one question splits into multiple parallel paths, gets checked, then merges back into one answer.

---

## 5. Worked Example: Should I Launch a Shopify Bookkeeping Product?

A full walkthrough of the agent-graph structure applied to a real startup question.

| Step | Role | What Happens |
|---|---|---|
| 1 | **Planner** | Breaks the question into: customer pain, competitive landscape, go-to-market wedge, pricing pressure, risk |
| 2a | **Researcher — Customer** | Are Shopify merchants using QuickBooks? Spreadsheets? Hiring bookkeepers? Annoyed at tax time? Want automation or a monthly cleanup? |
| 2b | **Researcher — Competitors** | Existing Shopify bookkeeping tools? Accounting firms doing it manually? App store solutions? Upwork/Fiverr freelancers software could replace? |
| 2c | **Researcher — Distribution** | Where do merchants hang out? What newsletters? Which agencies have trust? What app categories/search terms reveal buying intent? |
| 3 | **Skeptic** | What claims are actually supported? What evidence is stale? Which competitors are being ignored? Where is pain being confused with willingness to pay? Where did the AI sound confident without proving anything? |
| 4 | **Merge** | Turns surviving evidence into a recommendation: pursue, pause, or kill? What's the wedge? Who's the first customer? What to test this week? What evidence would change our mind? |
| 5 | **Human Gate** | Decide next action — e.g., record a landing page teardown, interview 10 agency owners, build a cost calculator, or walk away |

> 💡 **Tip:** Steps 2a–2c (the three researchers) can run **in parallel** since they don't depend on each other.

> ⚠️ **Caution:** "A lot of AI research fails because the same model that writes the answer also grades the answer." Isenberg compares this to asking someone to write their own performance review — checking must be **its own separate job**.

> 🗣️ **Speaker Opinion:** "Graph engineering does not magically make the decision for you. It gives you a better way to produce the evidence you use to make the decision."

---

## 6. Three Levels of Building a Graph

> 🗣️ **Speaker Opinion:** Isenberg explicitly warns against starting too fancy — jumping straight to LangGraph, AutoGen, or a custom agent framework on day one. "The first rep is to draw the graph before you automate the graph."

### Level 1 — Manual (Beginner)
Run the graph by hand, giving each job its own "lane": customer research lane, competitor research lane, distribution research lane, checker lane, merge lane.

> 💡 **Tip:** Use a blank **Excalidraw** or **TLDraw** board. Write the final outcome at the top, draw the jobs (Planner, Customer Researcher, Competitor Researcher, Distribution Researcher, Skeptic, Merge, Human Approval), then draw the arrows connecting them.

> 💡 **Tip:** Run the manual version **three times** successfully before thinking about tools/automation. If the manual version doesn't produce noticeably better work, automating it will just produce mediocre work faster.

### Level 2 — File-Based (Intermediate)
Use something like **Claude Code** or a repo where each step writes its own file:
- Planner writes `plan.md`
- Researchers write `customer.md`, `competitors.md`, `distribution.md`
- Skeptic writes `review.md`
- Merge step writes `recommendation.md`

> 💡 **Tip:** This leaves a paper trail — you can see what happened, compare versions, and reuse the structure weeks later.

### Level 3 — Automated (Advanced)
Orchestration tools to actually run the graph:

| Tool | Best For |
|---|---|
| **LangGraph** | State checkpoints, persistence, human-in-the-loop approvals, reliable control over agent workflow execution |
| **AutoGen / GraphFlow** | Directed workflows with sequential steps, parallel steps, conditional branches, and loops |
| **n8n, Make.com** | Graphs that touch everyday business systems — Slack, email, Airtable, CRM |

> ⚠️ **General Rule:** "If you automate a workflow you do not understand, you get a mess. If you understand the workflow first, automation then becomes super obvious." The tool should come *after* the workflow is understood, not before.

> 🗣️ **Speaker Opinion:** Isenberg says he may create a follow-up advanced tutorial using LangGraph or Claude Code if there's interest, but this episode intentionally stops at Level 1 and Level 2.

---

## 7. Real-World Applications

### Customer Support
Classify issue (billing / product confusion / bug / cancellation risk / other) → check account context (new customer? high value? prior contact? frustration level?) → search docs/internal policy/wiki/Notion → draft reply → checker reviews for accuracy, tone, risk → human approves anything involving refunds, account changes, angry customers, legal risk, or promises the company might regret.

> 🗣️ **Speaker Opinion:** "It's better than saying 'AI, answer this support ticket' because the support ticket is not the real workflow. The real workflow is understanding, researching, drafting, checking, and approving."

### Content Creation
Research → thesis → examples → hook → draft script → checker (are examples specific? does pacing work? does the hook earn attention based on what formats are working? does it sound like the person would actually say it?) → branches into title ideas, thumbnail concepts, captions, b-roll.

> 🗣️ **Speaker Opinion:** This mirrors "how a real content lead you'd hire would actually do the work."

### Coding
Plan → one agent edits code → another reviews the diff → another runs tests → another checks the UI in a browser → another looks for edge cases → human approves the final pull request.

> 💡 **General Rule:** The model writing code is only one part of the workflow — the leverage is in the planning, testing, reviewing, inspecting, and deciding what's safe to ship.

> 💡 **General Rule:** Graph engineering makes quality less dependent on someone remembering "the perfect prompt." It makes review more consistent, delegation cleaner, approval more explicit, and gives you a place to layer in tools, memory, checks, and permissions over time — turning AI work from chat into an operating system.

---

## 8. The Big Mistake to Avoid

> ⚠️ **Caution:** More agents ≠ better output. Sometimes more agents just means more noise, five AI workers confidently repeating the same wrong idea, or a system that spends more time coordinating than thinking.

> 🗣️ **Speaker Opinion:** "The goal is not to make the biggest graph possible. I've seen people on X go viral with these big graphs, but that's not the goal. The goal is to make the **smallest graph that improves the quality of work**."

A good graph should:
- Remove fake waiting
- Separate workers from checkers
- Put human approval where mistakes are expensive
- Stop when the answer is good enough (no unnecessary continuation)
- Leave behind useful state — notes, evidence, drafts, sources, decisions — for reuse later

---

## 9. The Compounding Value: Graphs Create Memory

> 💡 **General Rule:** The real compounding value of graph engineering isn't just that one task gets better — it's that your work starts **producing memory**. Every customer research graph creates better customer notes. Every content graph creates better examples and audience insights. Every support graph creates better product feedback.

> 🗣️ **Speaker Opinion:** "The context becomes the moat, because the graph produces the work but it also produces the memory that makes the next graph smarter."

---

## 10. How to Get Started This Week

A step-by-step starter process:

1. **Pick one workflow** you already run with AI weekly (e.g., researching ideas, prepping podcast episodes, reviewing landing pages, analyzing customer feedback).
2. **Write the final output in one sentence** — e.g., "I want a one-page recommendation on whether this startup idea is worth testing."
3. **List the jobs a great human would do** — clarify the question, research customers, research competitors, research distribution, research risks, check the evidence, make the recommendation.
4. **Draw arrows** where work actually depends on a prior step (e.g., customer and competitor research can happen simultaneously; the skeptic needs research done first; the final recommendation needs the skeptic's pass first).
5. **Add one human gate** before the expensive decision. Calibrate strictness: a private memo needs a light gate; a customer email, public post, code deploy, refund, or anything touching production data needs a strict gate.
6. **Run it manually once.** Don't build an automation project yet — just create the jobs and the arrows.

> 💡 **Tip:** Summary checklist — pick one workflow, draw the jobs and arrows, delete the fake waiting, run independent jobs in parallel, add a skeptic, merge the survivors, and approve the final step yourself. That's your first graph.

> 🗣️ **Speaker Opinion:** Isenberg frames graph engineering as "the next logical step after prompting," and believes the people who get the most out of AI will be those who know how to break work into the right pieces, give each piece the right context, check the output, and keep the human in the right place.

---

## Appendix: Caption Corrections

The following terms were corrected from likely auto-caption misspellings/errors in the source transcript:

| Transcript (as captioned) | Corrected |
|---|---|
| "Langraph" | LangGraph |
| "autogen graph flow" | AutoGen / GraphFlow |
| "nadn make.com" | n8n, Make.com |
| "nannn, make.com" | n8n, Make.com |
| "TL draw" | TLDraw |
| "plan.mmd" / "review.mmd" | plan.md / review.md (context indicates markdown files, consistent with "recommendation MD") |
| "Greg Eisenberg" | Greg Isenberg (host of Startup Ideas podcast) |

---

*Summary generated from a transcript of the Startup Ideas Podcast episode "Graph Engineering, Clearly Explained," hosted by Greg Isenberg.*
