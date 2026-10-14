# Skills

Skills are reusable workflows that Claude Code auto-discovers here. Each skill is a folder containing a `SKILL.md`:

```
.claude/skills/<skill-name>/SKILL.md
```

Build skills organically: when you notice you are repeating the same request, turn it into a skill.

Every skill folder also carries a `MEMORY.md`: a free-form file the skill reads at the start of each run and appends to **only when hcho explicitly says to remember something**. Keep it under 100 lines. When you build a new skill, scaffold a `MEMORY.md` and add a `## Memory` section to its SKILL.md following the same read-on-start, feedback-gated-write pattern.

## Active skills

- **application-packet:** builds one role's Application packet from the Master profile (`projects/Job_Search/profile/`): a one-page resume (.pdf and .docx) whose every line cites evidence-backed Claims, answers for the form's actual text fields, and a gaps-to-own note. `projects/Job_Search/applications/build_packet.py` refuses unsupported numbers, retired phrases, stale numbers, and anything over one page. Asset: `application-packet/assets/packet-template.yaml`. This folder is the canonical copy; `.agents/skills/application-packet` is a symlink to it so Codex and Claude Code cannot drift.
- **job-hunter:** scans target company career pages and ranks roles by fit against the resume. Assets: `job-hunter/assets/companies.yaml` (Tier A/B/C company list). References: scoring rubric, ATS patterns, company-list buckets.
- **daily-log:** creates or opens today's daily log for a tracked project path such as `projects/HabitLoop`, `projects/F2F`, or `projects/Learning/AI_Engineer/evals`, carrying forward the previous log's "Next" items. Asset: `daily-log/assets/daily-log-template.md`.
- **gr0wthlab-reader:** reads gr0wthlab's Review Queue, items, run reports, and hcho's records from its production clone (`~/gr0wthlab/ledger/`) to show status, applies a Go-To-Market Package change only when gr0wthlab's queue closed the item as approved and his decision record says approve, and gives hcho an approved Dispatch request to pass to firstmate. It never writes to gr0wthlab and never records a decision; hcho decides on gr0wthlab's sitting page. Contract: gr0wthlab's `docs/mandu-exchange.md`, version 7. This folder is the canonical copy; `.agents/skills/gr0wthlab-reader` is a symlink to it.
- **prd:** generates a Product Requirements Document for a new feature (clarifying questions, then a structured PRD with user stories and validation tests). Output: `.claude/agent/tasks/prd-[feature-name].md`.
- **ingest** (now a global skill at `~/.claude/skills/ingest/`, available across all projects): files one raw source into a wiki, updating the source summary, affected concept pages, index, and log in a single pass. Asset: `ingest/assets/source-summary-template.md`. Defaults to the evals pilot wiki and resolves other targets from this project's `CLAUDE.md` Wikis section, so it is most useful when run from within Mandu.

## Skills to build (backlog)

From the onboarding interview, recurring tasks worth turning into skills:

1. ~~**Resume + cover-letter tailoring**~~: built as `application-packet` on 2026-10-08.
2. **Company research:** build a pre-application / pre-interview dossier on a company.
3. **Interview prep:** eval / QA questions, behavioral, and system-design drills.
4. **Eval / LLM-QA study notes:** summarize papers and docs into structured study notes.
5. **Project README / documentation writer:** generate project writeups and READMEs.
6. **Weekly job-search digest:** weekly summary of new roles, application status, and next actions.

(`job-hunter` already covers scanning career pages for fitting roles.)
