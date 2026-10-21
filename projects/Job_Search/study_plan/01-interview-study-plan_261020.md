# Interview study plan

_Created 2026-10-20._
This plan draws on the gaps section of each Application packet in `applications/` and on the requirements in each posting.
It covers the six applications listed below.
Talking points that come out of this study belong in [interview-prep.md](../interview-prep.md), not here.

| Sent | Company | Role | Packet |
|---|---|---|---|
| 2026-10-14 | OpenRouter | AI Provider Operations & Support Engineer (Fit 5) | `applications/2026-10-08-openrouter-ai-provider-ops/` |
| 2026-10-14 | Arbiter AI | QA Engineer, Voice AI Agents | `applications/2026-10-14-arbiter-ai-qa-engineer-voice-ai/` |
| 2026-10-14 | Disney | Software Engineer II (GenAI) | `applications/2026-10-14-disney-software-engineer-ii-genai/` |
| 2026-10-20 | MiniMed | Senior SDET, Embedded Software/Firmware | `applications/2026-10-19-minimed-senior-sdet-embedded/` |
| 2026-10-20 | Syllo | Senior Data Scientist, AI Evaluation | `applications/2026-10-20-syllo-senior-data-scientist-ai-evaluation/` |
| 2026-10-20 | AssemblyAI | Software Engineer, Agent Experience | `applications/2026-10-20-assemblyai-software-engineer-agent-experience/` |

## Priority at a glance

| # | Topic | Applications | Why it ranks here |
|---|---|---|---|
| 1 | Explaining your own code without notes | All 6 | Agents wrote most of it; Disney bans AI tools in interviews; every story you tell depends on it |
| 2 | Eval design and the statistics behind it | Syllo, Arbiter, AssemblyAI, OpenRouter, Disney | Your lead story, and Syllo will test the math |
| 3 | LLM API mechanics and debugging | OpenRouter, Disney, AssemblyAI, Arbiter | OpenRouter likely has a live API-debugging exercise |
| 4 | Python and SQL with no AI help | Disney, MiniMed, Syllo, Arbiter, AssemblyAI | With 2 paid software years, a coding screen is likely |
| 5 | MCP and agent skills | AssemblyAI, Disney | A named gap in both |
| 6 | Voice AI basics | AssemblyAI, Arbiter, OpenRouter | New domain for all three |
| 7 | Medical-device testing and embedded interfaces | MiniMed | The biggest gap, but only one role needs it |
| 8 | LLMOps (running LLM apps in production) | Disney, OpenRouter, Arbiter | Your evidence here is thin |
| 9 | Domain basics to talk about, not claim | Arbiter, Disney, Syllo | One hour each |

## Suggested order

1. **This week:** topics 1, 3, and 2.
   The 10-14 applications are the likeliest to call first, and OpenRouter is your only Fit 5.
2. **Ongoing:** topic 4 in short daily sessions.
3. **Next:** topics 5 and 6.
   The MCP server from topic 5 also creates new evidence for your profile.
4. **Only if MiniMed calls:** topic 7.
5. **Before the matching interview:** topics 8 and 9, an hour each.

## 1. Explaining your own code without notes

- [ ] **Purvia agent loop.**
  Study the tool dispatch in `backend/main.py` and the 5-iteration cap.
  Also study the sub-agent's "read a chunk or finalize" loop, and how orphaned tool calls get repaired.
- [ ] **Hybrid retrieval.**
  Reciprocal rank fusion (RRF) merges two ranked lists by adding up 1/(k + rank) for each result.
  The stem-prefix keyword tier is the search-tier fix you added after a question retrieved nothing.
- [ ] **Access control in the retrieval SQL.**
  Row-level security (RLS) is Postgres rules that filter rows for each user.
  Know why filtering after retrieval loses most results for a user who can see only 1% of the data.
- [ ] **The 2026-10-16 fixes.**
  PR #184 fixed the E7 escalation-eval judge.
  PR #186 and `docs/adr/0015-answer-gate-value-extraction.md` hardened the answer gate; read them alongside `docs/evals.md` section 6.
  Know why a bare yes/no judge failed once it saw the context, what the five designs were, and why gpt-5-mini lost.
- [ ] **Rep Today Coach proxy (`proxy/src/worker.js`).**
  Know the App Attest check, the subscription check, `store: false`, and the timeout.
- [ ] **Update the story for the 10-14 applications.**
  The OpenRouter, Arbiter, and Disney packets describe the gates as failing.
  Arbiter's cover letter says "I haven't landed the fix yet."
  The fixes merged on 2026-10-16, and no scheduled run confirms them until 2026-11-01.
  Lead with that, and check the 2026-11-01 results before any interview after that date.

**Done when:** you can sketch each one in three minutes, and you can answer "who wrote this?" in one sentence.

## 2. Eval design and the statistics behind it

- [ ] **How LLM-as-judge fails.**
  Judges can favor an answer's position or its length.
  They can grade whether a draft is true instead of whether it answers the question, which was your E7 bug.
  Two judges can disagree with each other, or with humans; Cohen's kappa measures agreement after removing agreement you'd get by chance.
- [ ] **Eval structure.**
  Prefer pass/fail checks over 1-5 scores.
  Know golden sets (fixed test questions with known answers), regression gates in CI, and offline vs online evals.
- [ ] **Small-sample statistics. Syllo will probe this hardest.**
  The Wilson confidence interval is the standard interval for a pass rate.
  1 miss out of 11 is consistent with a true rate anywhere from about 2% to 38%.
  0 out of 11 still allows a true rate up to about 26%.
  The "rule of three" says that with zero failures in n tries, the 95% upper bound is about 3/n.
  So showing a rate under 5% takes about 60 should-escalate questions with no misses.
  That is the honest critique of your own 11-row E7 set, and a strong answer.
- [ ] **Experiment design.**
  Know A/B tests, sample size, and power.
  Multiple comparisons matter: testing five judge designs makes one look good by luck, and the Bonferroni correction adjusts for that.
  Repeat runs at temperature above 0.
- [ ] **Conversation QA for Arbiter.**
  Know scoring rubrics and transcript analysis.
  Practice sorting a problem into agent behavior, configuration, data, or platform bug.
- [ ] **Agent evals for AssemblyAI.**
  Know task success rate, time to first working call, and checks on the agent's sequence of steps.

**Sources you already have** (in AI_Wiki):

- [llm-as-judge](../../Education/AI/AI_Wiki/wiki/concepts/llm-as-judge.md)
- [agent-eval-and-stats](../../Education/AI/AI_Wiki/wiki/concepts/agent-eval-and-stats.md)
- [pass-fail-over-score-evals](../../Education/AI/AI_Wiki/wiki/concepts/pass-fail-over-score-evals.md)
- [ci-eval-gates-and-drift](../../Education/AI/AI_Wiki/wiki/concepts/ci-eval-gates-and-drift.md)
- [offline-vs-online-evals](../../Education/AI/AI_Wiki/wiki/concepts/offline-vs-online-evals.md)

**Done when:** you can explain, without notes, why 0 of 11 doesn't prove a rate under 5%.

## 3. LLM API mechanics and debugging

- [ ] **The three API shapes OpenRouter names.**
  These are OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages.
  Know how they differ in roles, where the system prompt goes, the tool-call format, and streaming events.
- [ ] **Tool calling and structured outputs** (responses forced to match a JSON schema).
- [ ] **Streaming.**
  Server-Sent Events (SSE) are a one-way HTTP stream of events.
- [ ] **Failures.**
  Know 429 rate limits, retry with backoff, timeouts, context-length errors, and falling back to another provider.
- [ ] **Debugging.**
  Reproduce a failing call with cURL and Postman, and read the status, headers, and body.
- [ ] **Launch checks for OpenRouter.**
  Know time to first token, tokens per second, quality spot checks, per-token pricing, quotas, and deprecations.

**Done when:** you can write, from memory, a raw cURL request with a tool call for each of the three APIs.

## 4. Python and SQL with no AI help

- [ ] **Python.**
  Practice core data structures, classes, exceptions, pytest fixtures and parametrize, HTTP calls, async basics, and parsing logs and JSON.
- [ ] **JavaScript/TypeScript basics** for AssemblyAI and MiniMed: async/await, fetch, and Node.
- [ ] **SQL** for Syllo and Arbiter.
  Practice joins, GROUP BY, CTEs, window functions such as ROW_NUMBER and LAG, and how NULLs behave.

**Done when:** you can finish a 30-minute practical task in each language with no AI help.

## 5. MCP and agent skills

- [ ] **MCP (Model Context Protocol).**
  MCP is an open standard for connecting AI apps to tools and data.
  Learn the three roles: host, client, and server.
  Learn what a server exposes: tools, resources, and prompts.
  Learn the two transports: stdio for local servers, streamable HTTP for remote ones.
  Learn auth: OAuth for remote servers vs plain API keys.
- [ ] **Agent skills.**
  Know the SKILL.md format and how the description decides when a skill gets used.
  Know progressive disclosure, where a short skill file points to separate detail files, and how to write evals for skills.
- [ ] **For AssemblyAI:** `llms.txt` and docs written for machines to read.
- [ ] **Best move: build something.**
  Build a small public MCP server, for example one that wraps AssemblyAI's transcription API.
  Measure a coding agent with and without it.
  Then ask Mandu to add it to the Master profile as a Claim.

**Sources:**

- [building-skills](../../Education/AI/AI_Wiki/wiki/concepts/building-skills.md)
- [skill-eval-loop](../../Education/AI/AI_Wiki/wiki/concepts/skill-eval-loop.md)
- [skills-vs-plugins](../../Education/AI/AI_Wiki/wiki/concepts/skills-vs-plugins.md)
- [agentic-web](../../Education/AI/AI_Wiki/wiki/areas/agentic-web.md)
- The MCP spec at modelcontextprotocol.io.

## 6. Voice AI basics

- [ ] **Speech-to-text.**
  WER (word error rate) counts substitutions, deletions, and insertions, divided by the number of words in the reference transcript.
  Diarization means labeling who spoke when.
  Know batch vs streaming, partial vs final transcripts, and latency.
- [ ] **Voice agent pipeline.**
  The pipeline is speech-to-text, then the LLM, then text-to-speech.
  It also has to detect when the user's turn ends and handle interruptions.
- [ ] **Call QA for Arbiter.**
  Know dropped calls, failed handoffs, and disposition logic (how the system records a call's outcome).
- [ ] **Hands-on.**
  Transcribe a file with AssemblyAI's API and compute WER against a transcript you write by hand.

**Done when:** you can explain WER and why it misses errors that change the meaning.

## 7. Medical-device testing and embedded interfaces (MiniMed only)

- [ ] **Standards and process.**
  IEC 62304 is the medical-device software lifecycle, with safety classes A, B, and C.
  ISO 13485 is the quality management system.
  Know design controls and risk management; ISO 14971 is the usual risk standard, though the posting says only "risk-management processes".
  CAPA means corrective and preventive action.
  A traceability matrix links requirements to risks, tests, and results.
- [ ] **Verification vs validation.**
- [ ] **Test benches.**
  HIL (hardware-in-the-loop) runs the real controller against a simulated environment.
  SIL (software-in-the-loop) runs the code against simulated hardware.
- [ ] **Embedded interfaces.**
  Refresh UART, SPI, I2C, CAN, USB, and BLE from your EE degree, and learn pyserial for test scripts.
- [ ] **Reading C/C++ firmware.**
  Learn enough about state machines and interrupts to design tests from the code.
- [ ] **Fault injection and recovery testing.**

If your Zebra work involved USB, serial, or Bluetooth, tell Mandu.
That can become an attested Claim, which MiniMed's packet currently can't use.

## 8. LLMOps (running LLM apps in production)

- [ ] Tracing with LangSmith or OpenTelemetry, and structured logs.
- [ ] Latency and cost per request, and monitoring dashboards.
- [ ] Azure Application Insights for Disney.

**Source:** [agent-observability](../../Education/AI/AI_Wiki/wiki/concepts/agent-observability.md)

## 9. Domain basics to talk about, not claim

- [ ] **HIPAA (Arbiter).**
  PHI means protected health information.
  Know the "minimum necessary" rule, business associate agreements, and de-identification.
- [ ] **Azure (Disney):** Azure OpenAI, Functions, and App Service.
- [ ] **Legal AI (Syllo):** the litigation lifecycle, e-discovery, and privilege.
