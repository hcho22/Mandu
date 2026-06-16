---
name: daily-loop
description: Run hcho's daily operating loop: morning brief, one focused project block, and end-of-day closeout. Use when the user says "start my day", "daily loop", "morning brief", "plan my day", "focus block", "close out today", "end of day", or asks to save day-to-day time.
---

# Daily Loop

Runs a lightweight operating loop that turns the second brain into daily execution: orient, pick one focused project block, then close out with durable notes and next actions.

## When to use this skill

Trigger when hcho wants to:
- Start the day with a short execution plan.
- Choose one focused work block from current priorities.
- Close out the day with logs, changed-state capture, and next steps.
- Reduce day-to-day coordination overhead across Mandu and active repos.

## Inputs

Optional:
- A target project, e.g. `Agentic RAG`, `CompeteIntel`, or `projects/Learning/AI_Engineer/evals`.
- A time budget, e.g. "90 minutes" or "morning only".
- A mode: `morning`, `focus`, `closeout`, or full `daily loop`.

If no project is named, read `context/current-priorities.md` and pick from the highest active priority.

## Morning Brief

1. Run `date +%Y-%m-%d`.
2. Read:
   - `context/current-priorities.md`
   - `context/goals.md` if quarterly or goal context matters
   - relevant project README(s) under `projects/`
   - existing daily log for the target project, if today's file exists
3. Check worktree status for the relevant local repo(s), including external repos under `/Users/hcho/Developer/` when the project README points there.
4. Produce a compact brief:
   - current top priority
   - any dirty repo state that could block work
   - one recommended focused block
   - a 2-3 item execution plan
   - what not to do today unless explicitly requested

## Focused Project Block

1. Confirm the target outcome in one sentence.
2. Gather only the context required for that outcome.
3. Execute the work end to end when feasible:
   - implement the requested change
   - run relevant checks
   - update project docs/logs when the work changes durable state
4. Keep scope tight. Do not expand into a second project unless hcho redirects.
5. If blocked, record the exact blocker and the smallest next decision needed.

## End-of-Day Closeout

1. Inspect changed files and relevant repo statuses.
2. Create or update today's project log using the `daily-log` format:
   - `## Done`
   - `## Notes / Learnings`
   - `## Blockers`
   - `## Next`
3. Update `context/current-priorities.md` only when focus materially shifts.
4. Add decision-log entries only for meaningful, hard-to-reverse decisions.
5. Summarize:
   - what changed
   - what was validated
   - what remains next
   - any dirty repos or uncommitted work

## Guardrails

- Do not overwrite an existing daily log. Read it first and append/update deliberately.
- Do not commit or push unless hcho explicitly asks.
- Do not hide dirty worktrees; surface them clearly.
- Keep morning briefs short and action-oriented.
- Prefer one focused project block over a broad task list.

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- Start of every run: read `MEMORY.md` and apply relevant preferences.
- Writing is feedback-gated: append only when hcho explicitly says to remember something for this daily loop.
- Use dated bullets under `## Notes`, with the real date from `date +%Y-%m-%d`.
- Keep `MEMORY.md` under 100 lines; ask before pruning.
