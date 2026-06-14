# Fridge to Fork (F2F)

> **Archived 2026-06-14.** Shipped — submitted to the Hugging Face "Build Small / Backyard AI" hackathon and moved to `archives/F2F/`. Preserved read-only; no further work tracked.

**One-liner:** The weeknight "what's for dinner?" decider. Snap 1-3 photos of your fridge/pantry, confirm what the app detected, set a few controls, and get 2-3 dinners built mostly from what is on hand — each with a time estimate, servings, a "from your fridge / you'll also need" split, and short numbered steps. Goal: photo to committed dinner plan in under a minute.

**Repo:** https://github.com/hcho22/F2F (private)

**Status:** Shipped (archived 2026-06-14). Submitted to the Hugging Face **Build Small / Backyard AI** hackathon by the 2026-06-15 deadline. Completed build order: Modal + vLLM backend -> end-to-end loop -> controls and honesty mechanics -> Off-Brand UI polish -> "I made this" logging -> 5+ real weeknights of usage -> demo video + social post.

## Why this project / how it fits

A shipped, deadline-driven small-model app that broadens the portfolio beyond evals into production vision-language deployment, while keeping the same quality-engineering instincts:

- **Small-model discipline:** one `Qwen2.5-VL-7B-Instruct` (well under the hackathon's 32B cap) does both jobs — reads the photo and writes the recipes.
- **Structured output as a reliability property:** vLLM **guided / JSON-schema decoding** guarantees valid structured JSON from the model. Correctness is a property of the serving layer, not a hope — the same theme as the evals projects.
- **Honest UX over fake precision:** a mandatory human confirm step sits between the vision guess and the recipes (recipes are only ever built from the confirmed pantry), estimates instead of fake gram-level math, and an explicit "you'll also need" list. Picky-kid notes are hard exclusions but explicitly not allergy-safe.
- **Serverless GPU economics:** a Modal scale-to-zero backend behind a free Hugging Face Space frontend.

Interview-relevant: deploying a small VLM under real constraints, guaranteeing structured output, and designing honesty mechanics into an AI product.

## What it does

1. **Snap** — upload 1-3 photos of the fridge / counter / pantry.
2. **Confirm** — detected ingredients show as editable chips; you fix misreads and confirm. Recipes are only ever built from this confirmed list, never a raw vision guess.
3. **Tune** — cuisine, number of people, a time cap, a "make it healthier" toggle, and free-text picky-kid notes.
4. **Cook** — get 2-3 dinner cards; pick one, cook it, tap "I made this" to log the night.

## Tech stack

| Layer | Choice |
| --- | --- |
| Model | `Qwen/Qwen2.5-VL-7B-Instruct` (vision + recipe text) |
| Serving | vLLM with guided / JSON-schema decoding |
| Compute | Modal (serverless GPU, scale-to-zero) |
| App / UI | Gradio (custom theme + CSS, custom HTML recipe cards) |
| Hosting | Hugging Face Space (free CPU tier; calls the Modal backend) |
| Persistence | Modal volume (usage log + plate photos) |

## Architecture

- **Frontend:** a Gradio app on a free HF Space (the required artifact and the custom "Off-Brand" UI). Holds no model; calls the backend over authenticated HTTPS.
- **Backend:** Modal serverless GPU running the model via vLLM. Two endpoints — `POST /extract` (photo -> ingredients) and `POST /generate` (confirmed pantry + controls -> 2-3 dinners), both schema-locked guided JSON. Scales to zero; kept warm during demo windows.
- **Persistence:** the usage log (date, dish, confirmed pantry, optional finished-plate photo) persists to a Modal volume, since the free Space disk is ephemeral.

## Hackathon constraints and badges

- **Small model only** — Qwen2.5-VL-7B, well under 32B. (required)
- **Gradio app hosted as an HF Space.** (required)
- **Off-Brand** (custom frontend beyond default Gradio) — the badge being chased.
- **Off the Grid** — intentionally forfeited; a Modal call is a cloud API, traded for a fast, reliable demo rather than faked.

## Key docs (in the repo)

- `.claude/agent/tasks/prd-fridge-to-fork.md` — the PRD (full design and build sequence).
- Plan: `~/.claude/plans/i-want-to-build-ethereal-clock.md`.

## How Claude helps

Built project, not tutor mode. Help here: code review, Modal + vLLM backend debugging, Gradio UI polish, critique of the eval / honesty mechanics, demo-video and social-post prep, and keeping the 6/15 hackathon deadline on track.

## Daily tracking

Given the tight deadline, worth daily-tracking. Say "log my F2F progress" and the `daily-log` skill will create `projects/F2F/log/<date>.md`.
