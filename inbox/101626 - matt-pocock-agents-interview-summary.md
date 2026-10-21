# Building with AI Agents: Communication, Fundamentals & the Trust Ladder

**Interview summary** · Host: **Nate Herk** · Guest: **Matt Pocock** *(surname inferred — the transcript uses "Matt" only; see [Appendix D](#appendix-d-editorial-notes))*
**Source:** YouTube video transcript (auto-generated captions) · **Format:** conversational interview, organized by theme in conversation order

---

## Overview

Matt Pocock, a self-taught developer who coded by hand for about 10 years (roughly 8 of them professionally), says he stopped writing code himself around December 2025, when Claude Opus 4.5 arrived. His central argument is that the bottleneck in working with agents is **communication**, not model intelligence. Agents perform in proportion to the environment you give them: codebase quality, tests, feedback loops, and shared vocabulary. That makes classic software-engineering fundamentals matter *more* now, not less. The conversation covers his skills (`/teach`, `grill-me`, `grill-with-docs`), why spec-driven development failed for him, why he runs Opus 5.5 on **medium** effort, where the career opportunities are, and how beginners should "climb the trust ladder."

**Five takeaways**

1. **Tell agents what you care about.** The human–agent communication gap never fully closes, however smart the model.
2. **Fix the environment before shopping for models.** Code quality, tests, and letting the agent run and see the app gave Matt his biggest gains.
3. **Surface unknown unknowns** by having the agent interview you before it builds.
4. **Use one precise vocabulary** (DDD's "ubiquitous language") across client, code, UI and prompts.
5. **Start small and earn trust.** Learn the brake before the accelerator, and give agents boring, verifiable work first.

## Callout Legend

| Callout | Meaning |
|---|---|
| 💡 **Tip** | Actionable advice you can apply directly |
| 🔧 **Tool** | A named tool, skill, model or product |
| 📏 **General Rule** | A principle presented as broadly true, or drawn from established practice |
| 🗣️ **Speaker Opinion** | A personal view, preference or hot take, attributed to **Matt** or **Nate** |
| ⚠️ **Caution** | A pitfall, limitation or warning |

`[?]` marks an uncertain caption restoration. Every correction is listed in [Appendix C](#appendix-c-caption-corrections).

## Table of Contents

1. [From Hand-Coding to Agents](#1-from-hand-coding-to-agents)
2. [Why Fundamentals Matter More Now](#2-why-fundamentals-matter-more-now)
3. [Trusting What Agents Teach You](#3-trusting-what-agents-teach-you)
4. [Career Opportunities in the AI Shift](#4-career-opportunities-in-the-ai-shift)
5. [Unknown Unknowns and Intent](#5-unknown-unknowns-and-intent)
6. [Standing Out When Everyone Builds Fast](#6-standing-out-when-everyone-builds-fast)
7. [Communication Is the Core Skill](#7-communication-is-the-core-skill)
8. [War Story: Spec-Driven Development](#8-war-story-spec-driven-development)
9. [Why Models Still Need Your Input](#9-why-models-still-need-your-input)
10. [Speed, Setup, and Effort Levels](#10-speed-setup-and-effort-levels)
11. [Getting Started: Climb the Trust Ladder](#11-getting-started-climb-the-trust-ladder)
12. [Give Agents Boring Work First](#12-give-agents-boring-work-first)
13. [Looking Ahead](#13-looking-ahead)
14. [Where to Find Matt](#14-where-to-find-matt)

**Appendices:** [A. Tools, Skills and Resources](#appendix-a-tools-skills-and-resources) · [B. Sponsor and Promo Segments](#appendix-b-sponsor-and-promo-segments) · [C. Caption Corrections](#appendix-c-caption-corrections) · [D. Editorial Notes](#appendix-d-editorial-notes)

---

## 1. From Hand-Coding to Agents

**Key points**

- Matt taught himself to code and coded by hand for about **10 years**: as an amateur first, then roughly **8 years** professionally.
- He was a skeptic for a long time. In the year before the shift he could see the benefits and the excitement, but it "hadn't quite clicked."
- His threshold was the release of **Claude Opus 4.5** and the rise of **OpenClaw**, around **December 2025**. That's when he decided he would never write a line of code himself again.
- Throughout his career he was drawn to improving the environment his colleagues worked in: building things that helped them ship faster, and teaching other developers, even more senior ones. Once agents became good, he applied those same skills to making *agents* better and faster.

> 🗣️ **Speaker Opinion (Matt, relayed by Nate)** — Learning to code is a lot easier than people make it out to be.

> 🗣️ **Speaker Opinion (Matt)** — Opus 4.5 (≈ December 2025) is when agents became "really, really good." Before that, his environment-improving skills didn't pay off with agents.

> 💡 **Tip** — Matt's experience: the skills you use to make a human team work better (tooling, standards, teaching) transfer directly to directing agents.

---

## 2. Why Fundamentals Matter More Now

**Key points**

- People underestimate the communication barrier between human and agent. However smart the model, the agent doesn't know precisely what you want or what you care about, so you have to tell it, again and again.
- Agents perform according to their environment. In a neglected, "garbage vibe-coded" codebase where nobody cares about the code (only the outputs), you get garbage out.
- **Thought experiment:** imagine running an organization of **100 human coders**. How would you **raise the floor** so that the *worst* coder performs better?
- People have worked on exactly this problem for about **20 years**. The books on it (writing good tests, adding checks so the codebase improves over time, stopping whole classes of bugs, preventing mistakes) read as if they were written last week.
- You don't need a deep technical background to start. The first step is to care about this and get curious. Agents are good teachers, and if you ask the right questions they'll pick up that you care and push you in that direction.

> 🗣️ **Speaker Opinion (Matt)** — "In my opinion," the best way to get the best work out of agents is to tell them what you care about.

> 📏 **General Rule** — Garbage in, garbage out: an agent in a rubbish environment produces rubbish.

> 💡 **Tip** — Run the "100 coders" thought experiment on your own project: which tests, checks and guardrails would lift your weakest contributor? Build those for your agents.

> 💡 **Tip** — Read the established software-engineering literature on testing and code quality. Matt finds it directly applicable to agentic work.

> ⚠️ **Caution** — Caring only about outputs while ignoring the codebase degrades every future agent session.

---

## 3. Trusting What Agents Teach You

**Key points**

- Nate says about **80%** of what he learned in the past year was taught to him by agents, and asks how far that can be trusted.
- Matt's answer: you shouldn't trust it. Be skeptical of anything anyone tells you. He calls himself a born skeptic; early on he dismissed AI as the next Web3/crypto bubble.
- He stays skeptical unless he can read the **primary source**.
- He designed `/teach` around this. It fetches high-trust, high-quality primary sources, then breaks them down with quotes and attribution, linking to exactly where each point comes from.
- Hallucinations have dropped a lot but still happen ("Fable still does it"), just less often.
- How he actually uses teach sessions: get introduced to a topic, then go read the primary source. The session gives him the language he needs to interpret it.

> 🔧 **Tool** — **`/teach`** (Matt's skill, from `mattpocock/skills`): researches high-quality primary sources and explains them with quotes, attribution and links.

> 📏 **General Rule** — Don't accept AI-taught material on trust; verify it against the primary source.

> 💡 **Tip** — Use AI as an on-ramp, not the destination. Let it introduce a topic and its vocabulary, then read the original.

> ⚠️ **Caution** — Hallucinations are rarer, not gone. Even current frontier models (Matt names Fable [?]) still invent things.

---

## 4. Career Opportunities in the AI Shift

**Key points**

- Any period of massive change creates opportunities, because adoption happens unevenly.
- Matt sees many **teaching** opportunities: every organization he talks to is meeting resistance in getting AI adopted.
- He flags ethical concerns as his own view. Parts of the AI world have dubious ethics; he cites Anthropic using novels for training and paying for them later, and the strain AI puts on the energy system. But AI isn't going away, because there is an economic incentive for it.
- Openings he sees: building applications that embed AI, and going into companies as someone who can use AI to improve and develop their systems.
- **Nate's scenario:** a non-technical salesperson with a full-time job. Should they learn to build and start consulting, or use AI at work to get promoted?
- **Matt's answer:** take a narrow view and build the skills that will be useful either way. People assume agents have no learning curve ("just talk to it"). In his experience they do, and better models *hide* the curve rather than remove it.
- The skills that make up that curve:
  - What can you trust from an agent?
  - How do you organize agents?
  - How do you get agents to behave the way you want?
  - How do you control, and design, the information agents receive? In what forms and data structures?
  - How do you turn agents into reusable processes, or turn your processes into something agents can follow?
- Agents are strong at code because code is easy to verify, as with math, where agents can generate proofs and solve hard problems. Real-world knowledge work is much harder for agents because it's harder to verify.
- Matt struggled for a long time to adopt agents for his own day-to-day work, trying "innumerable processes" before landing on one he's happy with and still improving.
- After about **1–1.5 years** of using agents he still finds this hard, which is exactly why he sees it as a massive opportunity.

> 🗣️ **Speaker Opinion (Matt)** — The biggest opportunity is figuring out agent processes for **knowledge work** and bringing them to organizations, because every organization does things slightly differently.

> 📏 **General Rule** — Agents perform best where output is easy to verify (code, math). Knowledge work lags because verification is harder.

> ⚠️ **Caution** — "Agents have no learning curve" is a myth. Newer models hide the curve; they don't remove it.

> 💡 **Tip** — Whether you aim to consult or to get promoted, invest in the transferable skills listed above: calibrating trust, organizing agents, designing information, and turning processes into agent workflows.

> 🗣️ **Speaker Opinion (Matt)** — Ethical criticism of AI (training-data sourcing, energy use) is partly correct, but AI is here to stay because of economic incentives.

---

## 5. Unknown Unknowns and Intent

**Key points**

- Nate asks how a non-technical person can drive with intent without things falling through the cracks (codebase setup, properly scoped API keys, and so on). In his experience, just being aware enough to make the agent look into something goes a long way.
- Matt sees no divide between "regular person" and coder here. Developers face exactly the same problem.
- *The Pragmatic Programmer*: no one knows exactly what they want. Everyone carries **unknown unknowns** into any specification.
- A person talking to an agent is like a non-developer talking to a developer. There's a communication barrier, and the listener has to work out what you care about.
- **`grill-me`**, one of his most-used skills, tells the agent to interview you relentlessly about what you're building. That draws out more context about what you care about and fleshes out the unknown unknowns.
- Typical unknown unknowns: **security**, **how you deploy it**, and things you simply haven't thought of. If you don't address them, the agent will make something up, or assume it's unimportant because you didn't mention it. You end up with weird behavior, or something very different from what you imagined.
- The skill is **being aware of unknown unknowns**: knowing you could be missing things, and not trusting that your design is complete.
- Turning an idea into code is a translation from fuzzy human thinking into executable statements that have to link together. The translation exposes weaknesses in the design, and some of them only show up once code exists.
- **Nate's experience:** when building client automations, he tried to predict edge cases and add guardrails, but production (especially with human inputs) still surprised him. He told clients upfront that he would monitor the system so that failures happened safely.

> 📏 **General Rule** — "No one knows exactly what they want." (*The Pragmatic Programmer*)

> 🔧 **Tool** — **`grill-me`** (Matt's skill): the agent interviews you relentlessly about the plan before it builds anything.

> 💡 **Tip** — Before building, have the agent grill you, and explicitly probe security, deployment and edge cases.

> ⚠️ **Caution** — Whatever you don't mention, the agent may invent or treat as unimportant.

> 📏 **General Rule** — Design weaknesses surface during translation into code. Some can't be found until the code exists.

> 💡 **Tip (Nate)** — Set client expectations early: real-world inputs are unpredictable, so commit to monitoring and to making sure failures happen safely.

---

## 6. Standing Out When Everyone Builds Fast

**Key points**

- Nate describes a **trust gap**: anyone can lock themselves in a room for a weekend and come out with a portfolio on Monday. How do you stand out to a cold prospect weighing ~20 vendors, or an employer weighing ~20 people for a promotion?
- Matt's caveat: he has never been in that competitive position. He already had a large audience and reputation when he did freelance consulting.
- What he thinks people want: someone they can work with, who understands what they care about and can cross the communication gap.
- He now thinks vibe coding is actually a good thing for this, because you're just trying to reach an endpoint quickly.
- Ship something fast that shows you understand their business, that you care about what they care about, and that you have real acumen in building something real for them.
- People who aren't "AI-pilled" don't yet realize how quickly high-quality work can be produced with agents, so you may need to adjust how you present your work to them.
- **Nate's takeaway:** trust comes from humanness (caring about what the client cares about and protecting their business) more than from showcasing builds or frameworks.

> ⚠️ **Caution** — Matt says outright that he can't offer concrete advice here, because he has never bid competitively. Treat this section as informed opinion.

> 💡 **Tip** — Win a prospect with a quick, tailored prototype that proves you understand *their* business.

> 🗣️ **Speaker Opinion (Matt)** — Vibe coding is now a good thing for prototypes, where speed to an endpoint matters most.

> 🗣️ **Speaker Opinion (Matt, half-joking)** — If a one-day turnaround unsettles a client, charge them for five days and "sit on your bum for four."

> 🗣️ **Speaker Opinion (Nate)** — Humanness beats a flashy portfolio.

---

## 7. Communication Is the Core Skill

**Key points**

- Asked what sets his successful students apart, Matt says they are the **best communicators**, and that this has always been true of developers and non-developers alike.
- Top-tier developers write detailed, easy-to-read reports about what changed in a code change. The clarity of their thinking ends up in the product they create.
- People who don't do this get worse results. They can't communicate what they want to the agent, can't communicate what's wrong, and aren't thinking in clear terms and boundaries.
- The quality of your thinking and language matters twice: when talking to the client, and when talking to the agent about what the client wants.
- **DDD (domain-driven design)** sounds complicated, but its core is the idea of a **ubiquitous language**: the terms in the code match how developers talk about the product, how the client asks for it, and how users use it.
- **Example:** an **order** should look the same in the code, the database, the UI, and your conversations with the client.
- Iterating on that language and making it precise aligns what the client wants with what you're actually building.
- **`grill-with-docs`** is a modified `grill-me` that builds this domain language as you go.
- Many coders haven't heard of DDD, but Matt has found it extraordinary for building with agents.
- *Aside:* Nate jokes about "JDD," jealousy-driven development: telling Claude that a rival ("Astro" [?]) does it better. Matt lists other "X-driven" approaches: spec-driven, README-driven and behavior-driven development.

> 🗣️ **Speaker Opinion (Matt)** — The most successful people, developers or not, are the best communicators. *(He presents this as a long-standing truth; it rests on his observation of students and colleagues.)*

> 📏 **General Rule** — DDD's ubiquitous language: one vocabulary across code, database, UI, team, client and users.

> 💡 **Tip** — Pin down core domain terms (e.g., "order") precisely and use them identically everywhere, including in your prompts.

> 💡 **Tip** — Write clear, detailed change reports. If you can't say what's wrong, the agent can't fix it.

> 🔧 **Tool** — **`grill-with-docs`** (Matt's skill): a `grill-me` variant that builds the domain language as you go. *[Editor's note: per the skill's published description, it records terms in a `CONTEXT.md` glossary and decisions in ADRs.]*

> 🗣️ **Speaker Opinion (Matt)** — "I can't recommend this technique enough." DDD has been extraordinary for building with agents.

---

## 8. War Story: Spec-Driven Development

**Key points**

- Matt was intrigued by a talk by **Sean Grove** (then at OpenAI) at the **AI Engineer** conference arguing that **specs are the new code** *[talk title: "The New Code"]*.
- The theory: you no longer write code. You write a very detailed specification (agents can help), then have an agent turn the spec into code.
- The idea is still very popular, with many frameworks built around it. Matt calls the term muddy; his own definition of **spec-driven development** is keeping the specs around and refining them as you go.
- Before he built his skills, he tried it seriously on his "pride and joy": a **custom video editor**, a sort of version of **Descript** with AI writing and thumbnail design, which he uses for everything.
- He kept wanting to look at the code, and saw it getting worse and worse while the agent produced worse and worse results.
- He persisted for **months**, reasoning that the speaker was from OpenAI and must know what he was talking about.
- **The turning point:** ditch the specs and focus on the code, because **code is the environment the agent operates in**. An agent in a bad codebase is the dog sitting calmly in a burning house: it won't produce good code.
- What "good code" means to him: a codebase that's **easy to make changes in**, where a change won't break something the agent didn't think about and everything is easy to modify.
- Once he refocused on code quality, things started working and he could "kick things into gear."

> 🗣️ **Speaker Opinion (Matt)** — Spec-driven development "just did not work" for him. This is one practitioner's months-long experience, not a universal verdict; he acknowledges the approach remains popular.

> 🗣️ **Speaker Opinion (Matt)** — The code, not the spec, is the agent's real environment, so that's where to invest.

> 📏 **General Rule** — A good codebase is one that's easy to change safely.

> 💡 **Tip** — Keep reading the code even when an agent writes it. Quality decay shows up there before results collapse.

> ⚠️ **Caution** — Treating specs as the source of truth while ignoring code quality can let the codebase, and the agent's output with it, quietly degrade.

---

## 9. Why Models Still Need Your Input

**Key points**

- Nate asks why ever-better models don't already understand and apply these concepts natively.
- Matt: it comes back to the communication barrier. Models can't know what you care about until you tell them, and **skills** are one way of telling them.
- Harnesses (**Claude Code**, **Claude.ai**, **Codex**) have more impact on results than people think.
- Models will keep improving, but they will never read your mind or align with you perfectly every time.
- So there will always be some process layer on top, helping a "genius developer" understand what you want. A great product takes a really good product manager *and* a really good developer: someone has to care, look at the outputs, and add their taste.

> 📏 **General Rule** — Models can't know what you care about until you tell them.

> 🗣️ **Speaker Opinion (Matt)** — People underrate the impact of the harness on results.

> 🗣️ **Speaker Opinion (Matt)** — No model will ever be good enough to read your mind, so a process layer will always be needed.

> 💡 **Tip** — Encode what you care about in skills so you're not re-explaining it every session.

---

## 10. Speed, Setup, and Effort Levels

**Key points**

- The speed-up is "outrageous," not comparable to coding by hand.
- He currently has **four agents** working on different projects, each given long-term tasks and goals ("go and figure it out").
- He's experimenting with a **"chief of staff" skill** for sub-agent management, which feels like having "a team of eight developers" shipping for him. He checks in, makes sure their plans are good, and grills them.
- **Output:** around **200–300 GitHub commits a day**, versus about **20 a day** for a good day before.
- **Setup:** **Claude Code** with **Claude Opus 5.5**, which he calls an excellent model: much better and more efficient than Opus 5.
- **Hot take on effort:** most people run far too high an effort level. He uses **Opus 5.5 on medium** and is considering going lower, for better token efficiency and faster replies. Because he has raised the floor, his agents don't need to work that hard: they write code that passes the tests, and the tests catch problems.
- He doesn't hop between models and harnesses. They're essential, but his biggest gains come from improving the environment agents operate in.
- **Example:** his video editor was hard for an agent to operate. It had many third-party dependencies, including **OBS** running locally while he also records with it. After he fixed that, the agent could open it in the browser, click through it, take screenshots and actually run the application. That alone produced a massive jump in output quality, because the agent had much better data. He thinks he could get similarly good results with Opus 4.5 under that setup.
- **Mental model:** agents are employees in his company. Make the company as good as possible, and the baseline employee does better.
- **Nate's view:** don't stress about the newest model and its benchmarks. Before Opus, Sonnet was already good enough to automate a lot of knowledge work, and Opus 5.5 on low beats it. Someone like Matt on a very old model could still out-produce someone on Opus 5.5 who can't communicate.

> 🔧 **Tool** — **Claude Code + Claude Opus 5.5 (medium effort)**: Matt's current setup.

> 🔧 **Tool** — **"Chief of staff" skill** (Matt's, experimental): sub-agent management across long-running tasks.

> 🗣️ **Speaker Opinion (Matt, "hot take")** — Most people set effort too high. Medium, or lower, gives better token efficiency and speed.

> ⚠️ **Caution** — Matt ties his low-effort setting to his raised floor: the agents only need to write code that passes the tests, and the tests catch the rest. The setting and the safety net go together.

> 💡 **Tip** — Give the agent eyes and hands on your app: let it run, browse, click through and screenshot it. This was Matt's single biggest quality jump.

> 💡 **Tip** — Invest in the environment before shopping for models. Matt believes even Opus 4.5 would do well in a well-built environment.

> 🗣️ **Speaker Opinion (Nate)** — Communication skill matters more than model version.

---

## 11. Getting Started: Climb the Trust Ladder

**Key points**

- Matt's suggested starting point, with acknowledged self-interest: his skills.
- Pick any of the main harnesses (**Claude Code**, **Codex**, **GitHub Copilot**) and don't spend long choosing. Just try it.
- He borrows the **trust ladder** from **Lauren Tan** ("poteto" [?] on Twitter, who he says works at "GrokBot" [?]), whom he recently interviewed. You won't trust your agent the first time you see it work, and that's a good impulse.
- **Driving analogy:** what's the first pedal you learn? The **brake**. Pushing on blindly burns through your rate limits, produces work you didn't want, and never gives you a feel for the tool.

**Matt's progression**

1. Open the model and give it some prompts. Start in an **empty folder**, and use **VS Code** so you can look inside the code.
2. Have a concrete idea or mission you want to build toward. Without one, motivation is harder and the feedback loop is weaker; seeing a cool idea come to life is "a multiplier."
3. **Watch the agent like a hawk.** Understand everything it does and everything the harness gives you, until you can feel when you trust it and when you understand it.
4. Then expand: run **two agents**, write a couple of **skills** for custom behavior, and connect **data sources** such as Slack, Twitter and Gmail.
5. Integrate it into your life and work. His example: he dictates a task to his **watch** → it pings a system → the task lands in his **to-do list** → an agent triages it.

- **Nate's analogy:** it's like teaching a kid to ride a bike. You watch closely and adjust. You don't teach ten kids at once, and you don't send twenty onto the highway and go take a nap.

> 📏 **General Rule** — Trust in agents is earned incrementally. Don't trust them blindly at the start.

> 💡 **Tip** — Learn the brake before the accelerator: small steps and close observation.

> ⚠️ **Caution** — Rushing ahead burns through rate limits and produces work you didn't want.

> 🗣️ **Speaker Opinion (Matt)** — Don't overthink the choice of harness.

> 🔧 **Tool** — Harnesses: Claude Code, Codex, GitHub Copilot · Editor: VS Code · Integrations: Slack, Twitter, Gmail.

---

## 12. Give Agents Boring Work First

**Key points**

- Nate notes that Elon, Boris and Sam (and others) have all said some version of "give our model your most ambitious tasks," and asks why they'd push that message.
- Matt thinks the **opposite**: give it your most menial, boring work, the stuff you hate doing. For example, drafting replies to people who are asking you for things.
- Give it simple, achievable tasks where you can measure the output and how good it is.
- It's also useful for brainstorming and for thinking through how to turn ideas into execution; `grill-me` helps there.
- The real value for him is automating the boring stuff so he can focus on the strategic layer.
- **His writing workflow:** for his written content, he uses **Sonnet 5.5** to produce a first draft, then iterates on it. He disliked writing it and used to pay people to do it; now the work is more interesting to him.
- Hand it low-stakes jobs, where mistakes don't matter much because you can go in and correct them.

> 🗣️ **Speaker Opinion (Matt)** — Contrary to "give it your most ambitious tasks," start with boring, menial work.

> 💡 **Tip** — Choose tasks that are low-stakes and measurable (e.g., drafting replies) so you can judge quality and fix errors cheaply.

> 🔧 **Tool** — **Claude Sonnet 5.5** for first drafts of written content; **`grill-me`** for brainstorming.

---

## 13. Looking Ahead

**Key points**

- Matt frames this carefully: he's "a teacher, not a pundit." He's in **Oxfordshire**, not SF; nobody is whispering the future into his ear; and he turns down most offers to preview things because he wants things to work *now*. That has also helped his sanity.
- **Software factories:** ways to automate initiating work and improving codebases over time, by themselves.
- Agents are currently bad at thinking long-term about a codebase. He wants to turn them into the "annoying developer" on every team who insists on doing it the right way, not the fast way, for the benefit of whoever comes next. He thinks that's achievable.
- **Organizing many agents:** nobody has found the right way yet, and nothing he's seen has convinced him. He sees huge potential here.
- **Open models:** they're improving, and an open model as good as Opus 5.5 would delight him. He doesn't need models to be better than that. Beyond that, he wants more token efficiency and a "plain-speaking" model that ships work quickly.

> 🗣️ **Speaker Opinion (Matt)** — Everything in this section is explicitly personal excitement, not prediction. He deliberately avoids previews and hype and focuses on making things work now.

> ⚠️ **Caution** — Agents today are weak at long-term codebase stewardship: they favor the fast way over the right way.

---

## 14. Where to Find Matt

- **aihero.dev** (AI Hero), including his newsletter
- **Twitter/X**
- **YouTube**

---

## Appendix A. Tools, Skills and Resources

| Name | Type | Context | Section |
|---|---|---|---|
| `/teach` | Skill (Matt's) | Primary-source-grounded teaching with quotes and attribution | [3](#3-trusting-what-agents-teach-you) |
| `grill-me` | Skill (Matt's) | Agent interviews you relentlessly; surfaces unknown unknowns; brainstorming | [5](#5-unknown-unknowns-and-intent), [12](#12-give-agents-boring-work-first) |
| `grill-with-docs` | Skill (Matt's) | `grill-me` variant that builds a DDD ubiquitous language | [7](#7-communication-is-the-core-skill) |
| "Chief of staff" skill | Skill (Matt's, experimental) | Sub-agent management | [10](#10-speed-setup-and-effort-levels) |
| Claude Code | Harness | Matt's daily driver | [9](#9-why-models-still-need-your-input), [10](#10-speed-setup-and-effort-levels), [11](#11-getting-started-climb-the-trust-ladder) |
| Claude.ai | Harness | Named as an example harness | [9](#9-why-models-still-need-your-input) |
| Codex | Harness | Named as an example harness | [9](#9-why-models-still-need-your-input), [11](#11-getting-started-climb-the-trust-ladder) |
| GitHub Copilot | Harness | Suggested starter option | [11](#11-getting-started-climb-the-trust-ladder) |
| VS Code | Editor | For looking inside the code while learning | [11](#11-getting-started-climb-the-trust-ladder) |
| Claude Opus 4.5 | Model | His "threshold" model (≈ Dec 2025) | [1](#1-from-hand-coding-to-agents), [10](#10-speed-setup-and-effort-levels) |
| Claude Opus 5 / 5.5 | Model | Current daily model, medium effort | [10](#10-speed-setup-and-effort-levels) |
| Claude Sonnet 5.5 | Model | First drafts of written content | [12](#12-give-agents-boring-work-first) |
| Fable [?] | Model | Cited as still hallucinating occasionally | [3](#3-trusting-what-agents-teach-you) |
| OpenClaw | Agent project | Part of the Dec 2025 inflection point | [1](#1-from-hand-coding-to-agents) |
| OBS | App | Local dependency of his video editor | [10](#10-speed-setup-and-effort-levels) |
| Descript | App | Reference point for his custom video editor | [8](#8-war-story-spec-driven-development) |
| Slack, Twitter, Gmail | Integrations | Data sources to connect once you trust the agent | [11](#11-getting-started-climb-the-trust-ladder) |
| *The Pragmatic Programmer* | Book | "No one knows exactly what they want" | [5](#5-unknown-unknowns-and-intent) |
| Domain-Driven Design (DDD) | Methodology | Ubiquitous language | [7](#7-communication-is-the-core-skill) |
| "The New Code" (Sean Grove) | Talk | "Specs are the new code" | [8](#8-war-story-spec-driven-development) |
| Lauren Tan | Person | Source of the "trust ladder" framing | [11](#11-getting-started-climb-the-trust-ladder) |
| aihero.dev | Website | Matt's site and newsletter | [14](#14-where-to-find-matt) |
| Hostinger VPS (KVM 2) | Hosting (sponsor) | See Appendix B | [B](#appendix-b-sponsor-and-promo-segments) |

---

## Appendix B. Sponsor and Promo Segments

These segments interrupt the interview. They're collected here so the thematic sections stay focused.

**Hostinger VPS (paid sponsorship, read by Nate)**

- Your own server with dedicated CPU and RAM and full root access, so what you build can live somewhere other than your laptop.
- Recommended plan: **KVM 2**, with **2 vCPUs, 8 GB RAM, 100 GB storage**; upgradable later.
- **Claude Code template**: comes with Claude Code preinstalled, so you can start building at first login.
- **Snapshots** before changes with rollback, and **weekly backups** included.
- An AI agent in Hostinger's web console helps with server tasks, errors and deployments in plain English.
- Link: **hostinger.com/nateherkvps**. Code **`nateherk`** gives an extra **10% off any yearly plan**, on top of current pricing.

**Nate's free AI OS kit (self-promotion)**

- Based on his framework, the "Herk loop" [?]: **context, connections, capabilities, cadence**.
- Includes **six skills**: it helps you set up a "brain," set your business priorities, and interviews you.
- He describes it as how he built his own AI operating system. The link is in the video description.

---

## Appendix C. Caption Corrections

| # | Caption text | Corrected to | Confidence | Note |
|---|---|---|---|---|
| 1 | "Open Claw" | OpenClaw | High | Agent project name |
| 2 | "{slash} teach" | `/teach` | High | Skill invocation |
| 3 | "Cloud Code template" | Claude Code template | High | Hostinger template (sponsor segment) |
| 4 | "Herc loop" | Herk loop [?] | Medium | Named for Nate Herk; his published framework is the "Four Cs" (Context, Connections, Capabilities, Cadence) |
| 5 | "math is very easy to uh is very far" | math is very easy to verify | Medium [?] | Parallels the preceding "code is very easy to verify" |
| 6 | "grill me" / "Grill Me" | `grill-me` | High | Skill name as published in `mattpocock/skills` |
| 7 | "Grill with Docs" | `grill-with-docs` | High | Skill name as published in `mattpocock/skills` |
| 8 | "the pragmatic programmer" | *The Pragmatic Programmer* | High | Book title (Hunt & Thomas) |
| 9 | "behavioral-driven development" | behavior-driven development (BDD) | High | Standard term |
| 10 | "readme-driven development" | README-driven development | High | Capitalization |
| 11 | "Shawn Grove" | Sean Grove | High | Speaker of "The New Code" |
| 12 | "the AI engineer" | AI Engineer (conference) | High | Event where the talk was given |
| 13 | "Dscript" | Descript | High | Video-editing app |
| 14 | "spectrum development" / "spectrum of development" | spec-driven development | High | Matches the surrounding discussion of specs |
| 15 | "local code is great" | Claude Code is great [?] | Medium | Contrasted with "Codex sucks" in a mock hot take |
| 16 | "five was" | Opus 5 | High | "Opus 5.5 … much better model than five was" |
| 17 | "Sonic 5.5" | Sonnet 5.5 | High | Claude model |
| 18 | "web 3 crypto" | Web3 / crypto | High | Formatting |
| 19 | "Potato on Twitter" | "poteto" [?] | Medium | Lauren Tan's commonly used handle; not verified for this context |
| 20 | "GrokBot" | *unchanged* [?] | Low | Lauren Tan's current employer could not be verified |
| 21 | "Astro's doing this way better" | *unchanged* [?] | Low | Probably a rival model or tool name; unclear |
| 22 | "I here we are at dev" | aihero.dev | High | Matt Pocock's site and newsletter (AI Hero) |

---

## Appendix D. Editorial Notes

- **Organization:** the source is a conversational interview, not a step-by-step tutorial, so it's organized thematically in conversation order rather than procedurally.
- **Speaker identification:** the host is **Nate Herk** (from the sponsor link and code and his AI OS framework). The guest appears only as "Matt"; **Matt Pocock** is inferred from the skills discussed (`/teach`, `grill-me` and `grill-with-docs` are published in `mattpocock/skills`), the aihero.dev site, and the Oxfordshire location.
- **Callout classification rules:**
  - Statements Matt frames with "in my opinion," "for me," "hot take," or personal experience → 🗣️ Speaker Opinion.
  - Principles attributed to established sources (*The Pragmatic Programmer*, DDD, "garbage in, garbage out") → 📏 General Rule.
  - Host statements are tagged **(Nate)**; everything else is Matt.
- **Judgment calls:**
  - "The best communicators are the most successful": Matt frames it as "always been true," but it rests on his own observation, so it's classified 🗣️ with a note.
  - "Models can't know what you care about until you tell them" and "agents do best where output is easy to verify" are stated as fundamental claims rather than preferences → 📏.
  - "Code is the environment the agent operates in" is Matt's core thesis but stems from his own experience → 🗣️.
- **Added from outside the transcript** (marked in text):
  - The talk title "The New Code" and Sean Grove's OpenAI affiliation at the time.
  - The `CONTEXT.md` / ADR detail for `grill-with-docs`, from the skill's published description.
- **Interpretations:**
  - "Fable" (Section 3) is read as Anthropic's Claude Fable model [?]; Matt does not elaborate.
  - "Elon, Boris, and Sam" (Section 12) are given by first name only; likely Elon Musk, Boris Cherny and Sam Altman [?].
  - The "dog sitting there with the house on fire" (Section 8) is most likely a reference to the "This is fine" meme.
  - Matt dates his threshold to "December last year, 2025." Claude Opus 4.5's public release was in late November 2025, so his dating is approximate.
- **Omitted or minimized:**
  - Nate's passing mention of an Anthropic announcement about restricting cruelty toward Claude is unverified and tangential, so it's not summarized.
  - Matt's remarks on AI ethics are reported as his opinion without elaboration.
  - Small talk (e.g., whether swearing is allowed) is omitted.
