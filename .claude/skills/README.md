# Skills

Skills are reusable workflows that Claude Code auto-discovers here. Each skill is a folder containing a `SKILL.md`:

```
.claude/skills/<skill-name>/SKILL.md
```

Build skills organically: when you notice you are repeating the same request, turn it into a skill.

## Active skills

- **job-hunter:** scans target company career pages and ranks roles by fit against the resume. Assets: `job-hunter/assets/companies.yaml` (Tier A/B/C company list). References: scoring rubric, ATS patterns, company-list buckets.

## Skills to build (backlog)

From the onboarding interview, recurring tasks worth turning into skills:

1. **Resume + cover-letter tailoring:** tailor resume and cover letter to a specific role and company.
2. **Company research:** build a pre-application / pre-interview dossier on a company.
3. **Interview prep:** eval / QA questions, behavioral, and system-design drills.
4. **Eval / LLM-QA study notes:** summarize papers and docs into structured study notes.
5. **Project README / documentation writer:** generate project writeups and READMEs.
6. **Weekly job-search digest:** weekly summary of new roles, application status, and next actions.

(`job-hunter` already covers scanning career pages for fitting roles.)
