# The New Code: Specifications as the New Unit of Programming

- **Speaker:** Sean Grove, OpenAI (alignment research)
- **Talk:** *The New Code*, AI Engineer World's Fair 2025, ~21 min
- **Source:** YouTube auto-caption transcript, corrected (all changes logged in [Appendix A](#appendix-a-caption-corrections))

---

## Overview

Sean Grove argues that code is only a small slice of what engineers actually produce. The real work is structured communication, and as models improve, the person who communicates intent best becomes the most valuable programmer. Today's prompting habits invert this: we keep the generated code and throw away the prompt that held the intent. He proposes the **written specification** as the durable source artifact, using OpenAI's **Model Spec** (versioned Markdown with per-clause test prompts) as the worked example and the **GPT-4o sycophancy rollback** as proof that a spec works as a "trust anchor." Specs can also be made executable: with **deliberative alignment**, one document serves as both training and eval material. He closes by framing specs as code, the US Constitution as a national spec, and a call to start every AI feature with a spec.

**Key takeaways**

- Code is roughly 10–20% of an engineer's value; the rest is structured communication *(speaker's estimate)*.
- Prompts are the source and code is the binary. Keep and version the spec, not just the output.
- Code is a lossy projection of intent; a robust spec can generate code, docs, tutorials, even podcasts.
- Make specs testable: clause IDs plus challenging prompts, graded against the spec.
- For your next AI feature: spec first, define success criteria, make it executable, test against it.

## How to Read This Document

| Callout | Meaning |
|---|---|
| 💡 **Tip** | Actionable advice you can apply directly |
| 🔧 **Tool** | A named tool, artifact, technique, or resource |
| 📏 **General Rule** | Established practice, verifiable fact, or a principle that follows from a stated premise |
| 🗣️ **Speaker Opinion** | The speaker's estimate, prediction, thesis, or proposal |
| ⚠️ **Caution** | A pitfall or cost to watch for |

`[?]` marks an uncertain caption restoration. Classification judgment calls are explained in [Appendix B](#appendix-b-editorial-notes).

## Table of Contents

1. [Intro and Agenda](#1-intro-and-agenda)
2. [Code vs. Communication](#2-code-vs-communication)
3. [Vibe Coding and the Discarded Prompt](#3-vibe-coding-and-the-discarded-prompt)
4. [Why Specs Beat Code](#4-why-specs-beat-code)
5. [Anatomy of a Spec: The OpenAI Model Spec](#5-anatomy-of-a-spec-the-openai-model-spec)
6. [Case Study: GPT-4o Sycophancy](#6-case-study-gpt-4o-sycophancy)
7. [Making Specs Executable](#7-making-specs-executable)
   - [7.1 Deliberative Alignment](#71-deliberative-alignment)
   - [7.2 Specs as Code](#72-specs-as-code)
8. [Lawmakers as Programmers](#8-lawmakers-as-programmers)
9. [Call to Action and Open Questions](#9-call-to-action-and-open-questions)
10. [Action Checklist](#action-checklist)
11. [Appendix A: Caption Corrections](#appendix-a-caption-corrections)
12. [Appendix B: Editorial Notes](#appendix-b-editorial-notes)

---

## 1. Intro and Agenda

**Key points**

- Sean works in alignment research at OpenAI. His thesis: **specifications are the new code**, delivering on the industry's long-held dream of writing your intentions once and running them everywhere.
- Roadmap of the talk:
  1. Code vs. communication, and why specs may be the better approach
  2. Anatomy of a spec, using the OpenAI **Model Spec**
  3. Communicating intent to humans: the **GPT-4o sycophancy** case study
  4. Making specs executable and communicating intent to models
  5. Thinking of specs as code, then open questions

> **🗣️ Speaker Opinion** — "Specs are the new code" is the talk's central thesis. It is argued throughout, not presented as settled fact.

## 2. Code vs. Communication

**Key points**

- Audience poll: many hands stayed up for "the most valuable professional artifact I produce is code." Sean calls this natural, since code is tangible: you can point to it, measure it, and debate it.
- A typical workflow is mostly communication: **talk** to users → **distill** their stories → **ideate** on goals → **plan** → **share** plans with colleagues → **translate** plans into code → **test and verify**.
- Verification isn't about the code itself. It asks whether the running code achieved its goals and relieved the user's problem.
- Structured communication is the bottleneck: knowing *what* to build, *how*, *why*, and *whether* it was built correctly and met the original intent.

> **🗣️ Speaker Opinion** — Code is roughly **10–20%** of the value an engineer brings; the other **80–90%** is structured communication. *(His estimate; no data cited.)*

> **🗣️ Speaker Opinion** — As models improve, this bottleneck will be felt more starkly: "the person who communicates most effectively is the most valuable programmer." If you can communicate effectively, you can program.

> **📏 General Rule** — Judge work by its effects on the world (did it solve the user's problem?), not by the code itself.

## 3. Vibe Coding and the Discarded Prompt

**Key points**

- Vibe coding feels good because it is **communication-first**: you describe intentions and desired outcomes, and the model handles the grunt work. Code is a secondary, downstream artifact.
- The odd part: prompts carry our intentions and values, yet we treat them as ephemeral and throw them away once we have the code.
- Compiler analogy: with TypeScript or Rust, nobody prizes the compiled binary (or what V8 executes). Binaries are regenerated from source on every build, so **the source is the valuable artifact**.
- With LLMs we do the opposite: keep the generated code and delete the prompt, like shredding the source and carefully version-controlling the binary.
- A written spec aligns humans on shared goals and lets you check whether you're actually synchronized. It is the artifact you discuss, debate, refer to, and sync on.

> **📏 General Rule** — Build outputs are regenerated from source; the source, not the binary, is the artifact of record.

> **💡 Tip** — Don't discard your prompts. Capture intent and values in a written spec and keep it versioned as the source of truth. *(Implied by the speaker's analogy; see Appendix B.)*

> **🗣️ Speaker Opinion** — "If you don't have a specification, you just have a vague idea."

## 4. Why Specs Beat Code

**Key points**

- Decompile a C binary and you get no comments and no well-named variables; you have to work backwards to infer intent. Even good source code doesn't embody all of a team's intentions and values.
- A spec that captures the communication work encodes every requirement needed to *generate* the code.
- Multi-target analogy: source compiles to **ARM64, x86, or WebAssembly** because it holds enough information. A sufficiently robust spec given to models can likewise produce **TypeScript, Rust, servers, clients, documentation, tutorials, blog posts, and podcasts**.
- Spec writing is a universal skill, not just a coder's: product managers write product specs, and lawmakers write legal specs.

> **🗣️ Speaker Opinion** — **Code is a lossy projection of the specification.** Stated as fact, but it is the talk's core argument.

> **💡 Tip** — *The podcast test* (for companies with developer customers): if you fed your entire codebase into a podcast generator, would the result tell users how to succeed and reach their goals? If not, that knowledge lives outside your code.

> **🗣️ Speaker Opinion** — The new scarce skill is writing specs that fully capture intent and values. Whoever masters it becomes the most valuable programmer, and there's "a reasonable chance" that will be today's coders.

## 5. Anatomy of a Spec: The OpenAI Model Spec

**Key points**

- OpenAI released the **Model Spec** last year (2024): a living document that tries to clearly and unambiguously express the intentions and values OpenAI wants its shipped models to have.
- It was updated in February (2025) and **open-sourced on GitHub**. The "implementation" is simply **a collection of Markdown files**.
- Why Markdown works: it is human-readable, versioned, and change-logged. Because it is natural language, non-engineers in **product, legal, safety, research, and policy** can read, debate, and contribute to the *same source*. It is the one artifact that aligns everyone in the company.
- Natural language can't always capture nuance unambiguously, so **every clause has an ID** (e.g., `sy73` [?]). A matching file in the repo (`sy73.md`) holds one or more **challenging prompts** for that clause. The document therefore encodes its own success criteria for the model under test.

> **🔧 Tool** — **OpenAI Model Spec**: open source on GitHub; plain Markdown files; one ID per clause, each with a file of example prompts.

> **💡 Tip** — Give every clause a stable ID and pair it with a file of hard example prompts. The spec then ships with its own test cases, and nuance that prose can't pin down is pinned down by examples.

> **💡 Tip** — Write specs in plain Markdown so non-technical stakeholders can contribute to the same artifact engineers use.

## 6. Case Study: GPT-4o Sycophancy

**Key points**

- A recent **GPT-4o** update caused extreme sycophancy. In one example, a user called out the model for being sycophantic at the expense of impartial truth, and the model praised the user for their insight. Other esteemed researchers found similarly concerning examples.
- Shipping sycophancy **erodes trust** and raises questions: Was it intentional? Accidental? Why wasn't it caught?
- The Model Spec had included a section, **"Don't be sycophantic,"** since its release. It explains that sycophancy may feel good in the short term but is bad for everyone in the long term.
- Because the spec is the agreed set of intentions and values, behavior that contradicts it **must be a bug**. OpenAI **rolled back**, **published studies and blog posts**, and **fixed it**.
- In the interim, the spec served as a **trust anchor**: a public statement of what is and isn't expected.
- Even if a spec did nothing but align humans, it would already be incredibly useful.

> **📏 General Rule** — When a spec is the agreed source of truth, behavior that contradicts it is a bug by definition, not a debatable design choice.

> **💡 Tip** — Write expectations down *before* an incident. A pre-existing spec lets you (and outsiders) answer "intentional or accidental?" immediately and gives everyone a shared reference point.

> **⚠️ Caution** — Sycophancy feels good in the moment but erodes trust over time. It is a failure mode worth naming explicitly in your spec, as the Model Spec does.

## 7. Making Specs Executable

The goal is to align not just humans but **models, and the artifacts they produce**, against the same spec.

### 7.1 Deliberative Alignment

**Key points.** The technique, from OpenAI's **deliberative alignment** paper:

1. Take your **spec** plus a set of **very challenging input prompts**.
2. **Sample** responses from the model under test or training.
3. Give the **response + original prompt + policy** to a **grader model**, which scores how well the response aligns with the spec.
4. **Reinforce the weights** based on that score.

- The same document becomes **both training material and eval material**.
- The alternative, putting the spec in context (a system or developer message) on every sample, is useful and yields a somewhat aligned model, but it **takes compute away from the problem you're actually solving**.
- Training moves the policy from **inference-time compute into the weights**, so the model "feels" the policy and applies it like muscle memory.
- Specs can cover anything: **code style, testing requirements, safety requirements**.

> **🔧 Tool** — **Deliberative alignment** (OpenAI paper): spec + hard prompts → sample → grader model scores against the spec → reinforce.

> **💡 Tip** — Pair your spec with hard prompts and have a grader model score outputs against it. One artifact gives you both an eval suite and a training signal.

> **⚠️ Caution** — Prompting with the full spec every time aligns the model only somewhat, and it spends compute that would otherwise go to the task.

### 7.2 Specs as Code

**Key points**

- Even though the Model Spec is "just Markdown," it helps to think of it as code. Specs **compose**, are **executable** and **testable**, have **interfaces** where they touch the real world, and can be **shipped as modules**.
- Spec work runs into the same problem domains as programming, so a parallel toolchain applies, aimed at **intentions rather than syntax**:

| Programming tool | Spec equivalent |
|---|---|
| **Type checker**: ensures dependent modules agree on their interfaces | **Consistency check**: if Department A's and Department B's specs conflict, surface it early and possibly block publication |
| **Unit tests** | **Embedded tests**: the policy carries its own test prompts (clause ID → challenging prompts) |
| **Linter** | **Ambiguity linter**: flags overly ambiguous language that confuses both humans and models and degrades the resulting artifacts |

> **🗣️ Speaker Opinion** — The consistency check and ambiguity linter are proposals ("you can imagine…"), not tools he describes as existing. The embedded unit tests already exist in the Model Spec.

> **💡 Tip** — Treat ambiguous wording in a spec as a defect. It confuses people *and* models, and everything generated from it gets worse.

## 8. Lawmakers as Programmers

**Key points**

- The **US Constitution** is "literally a national model specification":

| Constitution | Spec / programming analogue |
|---|---|
| Written text, aspirationally clear and unambiguous | Shared policy everyone can refer to as the status quo, even if they disagree with it |
| Amendments | Versioning: bumping and publishing updates |
| Judicial review | A **grader** assessing how well a situation aligns with the policy |
| Hard cases (the world is messy; part of the distribution gets missed) | Heavy "compute" spent working out how the law applies |
| Precedent | An **input/output pair**: a **unit test** that disambiguates and reinforces the original spec |
| Chain of command | Who has authority to direct or override whom |
| Enforcement over time | A **training loop** aligning everyone toward shared intentions and values |

- One artifact **communicates intent, adjudicates compliance, and evolves safely**.
- The pattern is universal: **programmers** align silicon via code specs, **product managers** align teams via product specs, **lawmakers** align humans via legal specs, and **anyone writing a prompt** is writing a proto-spec to align AI models.
- Specs let you ship **faster and safer**, and everyone can contribute. Whoever writes the spec (PM, lawmaker, engineer, marketer) is now the programmer.
- **Software engineering has never been about code.** A definition the speaker credits to "Josh" [?]: *"Engineering is the precise exploration by humans of software solutions to human problems."* The shift is from disparate machine encodings to a unified human encoding.

> **🗣️ Speaker Opinion** — Lawmakers may become programmers, or programmers lawmakers. *(Speculative.)*

> **🗣️ Speaker Opinion** — Whoever writes the spec is now the programmer, and coding, while a wonderful skill, is not the end goal.

> **💡 Tip** — Treat every prompt as a proto-spec. You are already a spec author, so write prompts with the same care for intent and success criteria.

## 9. Call to Action and Open Questions

> **💡 Tip — Spec-first workflow for your next AI feature**
>
> 1. **Start with the specification.** What do you actually expect to happen?
> 2. **Define success criteria.**
> 3. **Debate** whether it is clearly written down and communicated.
> 4. **Make the spec executable:** feed it to the model.
> 5. **Test** against the model, and test against the spec.

**Open questions**

- **What does the IDE of the future look like?** His hope: an *integrated thought clarifier*. As you write a spec, it pulls out ambiguity and asks you to clarify, helping people communicate intent to each other and to models.
- **What is both amenable to, and in desperate need of, specification?** His answer: **aligning agents at scale**. He cites a line he likes (source not named [?]) about realizing you never told the agent what you wanted, and maybe never fully understood it yourself. He calls this "a cry for specification."
- **Hiring:** OpenAI has started a new **agent robustness team**, and he invites people to join and help deliver safe AGI for the benefit of all humanity.

> **🗣️ Speaker Opinion** — The "integrated thought clarifier" is a speculative vision of future tooling, not an existing product.

---

## Action Checklist

- [ ] Write the spec before the prompt or code: expected behavior plus success criteria.
- [ ] Keep specs and prompts versioned as the source of truth; treat generated code as a build output.
- [ ] Use plain Markdown so non-engineers can read and contribute.
- [ ] Give each clause a stable ID and a file of challenging example prompts.
- [ ] Use a grader model to score outputs against the spec; reuse the same set as evals (and as a training signal if you train models).
- [ ] Hunt down ambiguous wording; it degrades outputs for humans and models alike.
- [ ] Check specs from different teams for conflicts before publishing.
- [ ] When behavior contradicts the spec, treat it as a bug: roll back, explain publicly, fix.

---

## Appendix A: Caption Corrections

| # | Caption (as transcribed) | Corrected to | Confidence |
|---|---|---|---|
| 1 | "the 40 syphency issue", "an update to 40" | GPT-4o | High |
| 2 | "syphency", "syphy", "syphants", "sophantic", "syopency", "sycopency", "sick of fantic" | sycophancy / sycophants / sycophantic ("Don't be sycophantic") | High |
| 3 | "ideulate", "ideulating" | ideate / ideating | High |
| 4 | "underelling" | underselling | High |
| 5 | "when we prompt elements" | when we prompt LLMs | High |
| 6 | "erodess" | erodes | High |
| 7 | "a greater model" | a grader model | High |
| 8 | "llinters" | linters | High |
| 9 | "disperate" | disparate | High |
| 10 | "ARM 64 x86 or web assembly" | ARM64, x86, WebAssembly | High |
| 11 | "sy73.mmarkdown or md" | `sy73.md` | High |
| 12 | "sy73" (clause ID) | Kept as `sy73`; consistent both times it appears, but the exact ID format can't be verified from audio captions | Medium [?] |
| 13 | "inte like integrated thought clarifier" | integrated thought clarifier (false start removed) | High |
| 14 | "aligning agent at scale" | aligning agents at scale | Medium |
| 15 | "keep their head up" | keep your hands up | High |
| 16 | "rein reinforces" | reinforces (stutter) | High |
| 17 | "I want to thank Josh for this uh credit" | Kept as "Josh"; surname and affiliation not given | Low [?] |
| 18 | "I love this line of like you then you realize that you never told it what you wanted…" | Paraphrased; original source of the quoted line not named | Medium [?] |
| 19 | "My name is Sean" | Sean Grove (added from the event's talk page; see Appendix B) | High |
| 20 | "model spec" | Model Spec (proper noun) | High |

## Appendix B: Editorial Notes

- **Structure.** The source is a talk, not a step-by-step tutorial, so it is organized thematically. Sections follow the official chapter list on the [AI Engineer talk page](https://ai.engineer/talks/specifications-are-the-new-code): Intro, Code vs Communication, Vibe Coding, Spec Power, Model Spec, Sycophancy Case, Executable Specs, Lawmakers as Programmers, Call to Action. "Specs as code" is split out as 7.2 because the speaker lists it as a separate agenda item.
- **Context added from outside the transcript.** The speaker's surname, talk title, event, and ~21-minute runtime come from the talk page. The years in "last year (2024)" and "February (2025)" are inferred from the 2025 talk date.
- **Classification rule.** 📏 General Rule covers established engineering practice, verifiable fact, or a principle that follows directly from a stated premise. 🗣️ Speaker Opinion covers estimates, predictions, the talk's thesis claims, and proposals introduced with "you can imagine" or similar.
- **Judgment calls.**
  - "Code is a lossy projection of the spec" (§4): stated as fact; classified 🗣️ as the talk's core argument.
  - "A written spec aligns humans" (§3): left as a key point (established practice). The stronger line, "without a spec you just have a vague idea," is flagged 🗣️.
  - "Spec contradiction = bug" (§6): 📏, because it follows from treating the spec as the agreed source of truth.
  - "Judge work by its effects" (§2): 📏, a widely shared principle the speaker restates.
  - "Don't discard your prompts" (§3): 💡, implied by the speaker's shredding analogy rather than stated as an instruction.
  - Spec-first workflow (§9): the speaker's explicit instructions, presented as a 💡 Tip.
  - Toolchain table (§7.2): consistency check and linter flagged 🗣️ as proposals; embedded tests described as existing.
- **Cleanup.** Filler words, false starts, `[Music]` tags, and audience-interaction asides were removed without individual logging. Quotes are short and verbatim from the corrected transcript.
