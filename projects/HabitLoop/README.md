# HabitLoop

**One-liner:** A personal habit tracker built from scratch as a backend-fundamentals learning project. Node.js + Express + Postgres, vanilla JS frontend, hand-rolled JWT auth.

**Repo:** https://github.com/hcho22/HabitLoop (private)

**Status:** Active, currently prioritized. Backend complete through **M8**: auth (signup/login/JWT/middleware), habits CRUD scoped to user, completions with a composite unique constraint, and the streaks endpoint. Next up: **M9** (minimal vanilla JS frontend), then **M10** (hardening). Last progress logged 2026-06-01.

## Why this project / how it fits

Part of the AI Eval / QA Engineer path. The goal is to internalize production-quality backend fundamentals (relational data modeling, HTTP, auth, async) by writing every line by hand. This depth supports the broader hardware-QA-to-AI-native pivot: stronger engineering foundations behind the evals/quality positioning.

## Important constraint: tutor mode

This is a **learning project**, not a product. Per the repo's `ROADMAP.md`, Claude acts as a tutor, not a code-writer.

- **Do NOT** write `.js`, `.sql`, or config files for hcho unless explicitly asked.
- **Do** help with: explanations, design discussion, debugging together, code review, trade-off analysis.
- The whole point is hcho writes every line. Push back if asked to "just write the endpoint."

## Stack

- **Backend:** Node.js + Express 5
- **Database:** Postgres via `pg` (no ORM, hand-written SQL and migrations)
- **Auth:** hand-rolled JWT (`jsonwebtoken`) + `bcrypt` password hashing
- **Frontend:** vanilla JS + `fetch()` (planned, Milestone 9)

## Roadmap (10 milestones, full detail in repo `ROADMAP.md`)

- **M0** Environment (Node, Postgres, project init)
- **M1** Hello Express (`GET /health`)
- **M2** Postgres connection + first table (`users`)
- **M3** Signup endpoint (bcrypt password hashing)
- **M4** Login + JWT issuance
- **M5** Auth middleware (`requireAuth`, `GET /me`)
- **M6** Habits CRUD, scoped to user (foreign keys, ownership scoping)
- **M7** Completions (many-to-one, composite unique constraint)
- **M8** Streaks (SQL window functions, gaps-and-islands)
- **M9** Frontend: minimal vanilla JS
- **M10** Hardening (validation, error handling, rate limiting, migration tool, tests)

## Daily tracking

Daily notes live in `log/`, one file per day (`YYYY-MM-DD.md`). Each entry records milestone focus, what got done, learnings, blockers, and next step.
