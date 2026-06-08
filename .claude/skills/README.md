# Skills

Skills are reusable workflows that Claude Code auto-discovers here. Each skill is a folder containing a `SKILL.md`:

```
.claude/skills/<skill-name>/SKILL.md
```

Build skills organically: when you notice you are repeating the same request, turn it into a skill.

Every skill folder also carries a `MEMORY.md`: a free-form file the skill reads at the start of each run and appends to **only when hcho explicitly says to remember something**. Keep it under 100 lines. When you build a new skill, scaffold a `MEMORY.md` and add a `## Memory` section to its SKILL.md following the same read-on-start, feedback-gated-write pattern.

## Active skills

- **job-hunter:** scans target company career pages and ranks roles by fit against the resume. Assets: `job-hunter/assets/companies.yaml` (Tier A/B/C company list). References: scoring rubric, ATS patterns, company-list buckets.
- **daily-log:** creates or opens today's daily log for a tracked project (defaults to HabitLoop) at `projects/<Project>/log/<date>.md`, carrying forward the previous day's "Next" items. Asset: `daily-log/assets/daily-log-template.md`.
- **prd:** generates a Product Requirements Document for a new feature (clarifying questions, then a structured PRD with user stories and validation tests). Output: `.claude/agent/tasks/prd-[feature-name].md`.
- **ingest:** files one raw source into a wiki, updating the source summary, affected concept pages, index, and log in a single pass. Asset: `ingest/assets/source-summary-template.md`.

## Skills to build (backlog)

From the onboarding interview, recurring tasks worth turning into skills:

1. **Resume + cover-letter tailoring:** tailor resume and cover letter to a specific role and company.
2. **Company research:** build a pre-application / pre-interview dossier on a company.
3. **Interview prep:** eval / QA questions, behavioral, and system-design drills.
4. **Eval / LLM-QA study notes:** summarize papers and docs into structured study notes.
5. **Project README / documentation writer:** generate project writeups and READMEs.
6. **Weekly job-search digest:** weekly summary of new roles, application status, and next actions.

(`job-hunter` already covers scanning career pages for fitting roles.)
