# Learning

## Current scope

Mandu's learning library covers anything hcho studies, organized by subject as material arrives.
New `.md` sources enter through the shared `inbox/`; hcho runs `/ingest` to have Mandu preserve the source, organize useful knowledge, connect relevant projects, and report back.

- General AI knowledge lives in [[projects/Education/AI/AI_Wiki/wiki/index|AI_Wiki]].
- Marketing knowledge lives in [[projects/Education/Marketing/wiki/index|Marketing]], beginning with content libraries and source-grounded writing.
- [[projects/Education/AI/LLM_Evals/README|LLM_Evals]] retains the parked curriculum, exercises, and study history; reusable eval knowledge lives in AI_Wiki.
- Other subject areas are created only when relevant material arrives.
- Reusable knowledge has one authoritative home and links to the projects where it can be applied.

## Historical setup (superseded)

The role-first organization, active-evals status, and paths below describe an older setup and do not govern current filing.

**One-liner:** A continuous learning-tracking project. Structured, logged self-study that builds the skills to land an AI Engineer / AI Product Engineer / AI Evals Engineer role.

**Status:** Active. Current track: **Evals** (see `evals/`).

## Why this project / how it fits

Directly serves the #1 goal: land an AI evals / quality engineering role at an AI-native company while building and learning production-quality skills. The portfolio projects (CreativeBridge, Agentic RAG, HabitLoop) demonstrate built work; this project tracks the deliberate study behind it: concepts, hands-on exercises, and demonstrable competence. It is the "learning" half of "building and learning production-quality projects."

## Structure

Learning is organized as **career track → topic**. A career track is a role-oriented folder (e.g., `AI_Engineer/`); inside it, each topic is a subfolder with its own README (plan, progress, resources) and a `log/` of study sessions.

| Career track | Topic | Status | Folder |
| --- | --- | --- | --- |
| AI Engineer | Evals — AI Eval / QA: offline+online evals, LLM-as-judge, RAG metrics, CI gates, red-teaming | In progress | `AI_Engineer/evals/` |

Future topics under AI Engineer: agent evaluation, fine-tuning, RAG architecture, LLMOps, model serving. Add a new subfolder when a topic begins, and add a row to the table above.

## How Claude helps

This is learning, so Claude is a **study partner**, not a doer:

- Explain concepts step by step, with analogies and worked examples.
- Quiz me (plans include quizzes and Feynman-style re-explanation checks) and grade my answers honestly.
- Review hands-on exercise output and eval code.
- Track progress: which session and ladder level I am on, and what is next.
- Connect what I learn to the portfolio projects and to interview talking points.

## Tracking

Per-track study sessions are logged under `<track>/log/`. A session log records: session/level focus, objectives, what got done, the hands-on result, learnings, blockers, and the next step. Created on first use.
