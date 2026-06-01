# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---

[2026-05-31] DECISION: Make `/Users/hcho/Mandu` the single second-brain root; the job search becomes its first project (`projects/job-search/`). | REASONING: A built assistant ("Mandu") already existed in `Job_Hunter/`; one consolidated brain beats two competing ones, and job-hunting is the current #1 workstream, which fits the projects/ model. | CONTEXT: Initial AI-OS setup; chosen over keeping two parallel brains or fully dissolving the job-search content.

[2026-05-31] DECISION: Root assistant takes a neutral "executive assistant" identity. | REASONING: Template-literal framing fits an engineer's working relationship better than carrying forward the old "CLI creature" SOUL persona. | CONTEXT: Old IDENTITY.md/SOUL.md retired to `archives/job-hunter-legacy/` (kept, not deleted).

[2026-05-31] DECISION: Reshape the business-shaped template files for a solo job-seeker. | REASONING: User is a solo AI engineer with no business/team/revenue; literal "revenue streams / products / team" files don't apply. | CONTEXT: work.md = Career & Work (job search + portfolio); team.md = solo note; goals.md = job-search milestones (Q2 2026).

[2026-05-31] DECISION: Standardize on Claude Code native auto-memory across the whole brain; retire the manual daily-notes memory loop. | REASONING: Three overlapping memory systems existed; native auto-memory + decisions/log.md is lighter and is what the template prescribes. No SessionStart hook actually existed to remove. | CONTEXT: Strategic content from old MEMORY.md migrated into live files; raw daily notes archived read-only under `projects/job-search/archive/`.

[2026-05-31] DECISION: Move the existing `job-hunter` skill to `.claude/skills/job-hunter/`. | REASONING: Claude Code only auto-discovers skills under `.claude/skills/`; leaving it inside the project folder would make it un-invokable. | CONTEXT: Deviation from the template's "leave skills empty" rule — justified because it migrates an existing skill rather than authoring a new one.

[2026-05-31] DECISION: Run the full 6-section onboarding interview rather than auto-filling from existing files. | REASONING: User opted for the complete template interview; existing files (USER.md, resume, MEMORY.md) are used to cross-check, not skip questions. | CONTEXT: Interview drives the context files, communication-style rule, and the Skills-to-Build backlog.
