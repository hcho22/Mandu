# Skills

Skills are reusable workflows that Claude Code auto-discovers here. Each skill is a folder containing a `SKILL.md`:

```
.claude/skills/<skill-name>/SKILL.md
```

Codex discovers skills in `.agents/skills/`, where each entry is a symlink back to the folder here, so both agents run the same copy. When you build a new skill, create it here and add the matching symlink (`ln -s ../../.claude/skills/<skill-name> .agents/skills/<skill-name>`). The one exception is `ingest`, described below.

Build skills organically: when you notice you are repeating the same request, turn it into a skill.

Every skill folder also carries a `MEMORY.md`: a free-form file the skill reads at the start of each run and appends to **only when hcho explicitly says to remember something**. Keep it under 100 lines. When you build a new skill, scaffold a `MEMORY.md` and add a `## Memory` section to its SKILL.md following the same read-on-start, feedback-gated-write pattern.

## Active skills

- **application-packet:** builds one role's Application packet from the Master profile (`projects/Job_Search/profile/`): a one-page resume (.pdf and .docx) whose every line cites evidence-backed Claims, answers for the form's actual text fields, and a gaps-to-own note. `projects/Job_Search/applications/build_packet.py` refuses unsupported numbers, retired phrases, stale numbers, and anything over one page. Asset: `application-packet/assets/packet-template.yaml`. This folder is the canonical copy; `.agents/skills/application-packet` is a symlink to it so Codex and Claude Code cannot drift.
- **job-hunter:** searches direct employer pages, full-time aggregators such as Indeed, and freelance marketplaces led by Upwork, then ranks opportunities by resume fit and engagement quality. Assets: `job-hunter/assets/companies.yaml` (Tier A/B/C company list) and `job-hunter/assets/search-sources.yaml` (the default source mix). References: scoring rubric, ATS patterns, company-list buckets.
- **daily-log:** creates or opens today's daily log for a tracked project path such as `projects/RepToday` or `projects/Immerse`, carrying forward the previous log's "Next" items. Asset: `daily-log/assets/daily-log-template.md`.
- **daily-loop:** runs hcho's daily operating loop: a morning brief, one focused project block, and an end-of-day closeout.
- **gr0wthlab-reader:** reads gr0wthlab's Review Queue, items, run reports, Weekly Read memos, and hcho's records (including the Weekly Read numbers he types on its sitting page) from its production clone (`~/gr0wthlab/ledger/`) to show status, applies a Go-To-Market Package change only when gr0wthlab's queue closed the item as approved and his decision record says approve, and gives hcho an approved Dispatch request to pass to firstmate. It never writes to gr0wthlab and never records a decision or a result; hcho decides and gives his numbers on gr0wthlab's sitting page. Contract: gr0wthlab's `docs/mandu-exchange.md`, version 8. This folder is the canonical copy; `.agents/skills/gr0wthlab-reader` is a symlink to it.
- **prd:** generates a Product Requirements Document for a new feature (clarifying questions, then a structured PRD with user stories and validation tests). Output: `.claude/agent/tasks/prd-[feature-name].md`.
- **ingest** (a global skill at `~/.claude/skills/ingest/`, available across all projects; Codex keeps an identical copy at `.agents/skills/ingest/`, so change both together): files one learning source into the right wiki, updating the source summary, affected pages, index, and log in a single pass. Run with no path, it takes the sole pending file in `inbox/`. It picks the destination from the Active wikis list in `AGENTS.md`, so it is most useful when run from within Mandu. Asset: `ingest/assets/source-summary-template.md`.

## Skills to build (backlog)

From the onboarding interview, recurring tasks worth turning into skills:

1. ~~**Resume + cover-letter tailoring**~~: built as `application-packet` on 2026-10-08.
2. **Company research:** build a pre-application / pre-interview dossier on a company.
3. **Interview prep:** eval / QA questions, behavioral, and system-design drills.
4. **Eval / LLM-QA study notes:** summarize papers and docs into structured study notes.
5. **Project README / documentation writer:** generate project writeups and READMEs.
6. **Weekly job-search digest:** weekly summary of new roles, application status, and next actions.

(`job-hunter` already covers scanning career pages for fitting roles.)
