---
name: application-packet
description: 'Build a job Application packet from hcho''s Master profile: a one-page resume made only of evidence-backed Claims in the posting''s own wording, answers for the application form''s actual text fields, and a gaps-to-own note, checked and rendered by build_packet.py. Use when hcho says "make a packet for <role>", "tailor my resume for", "prep my application to", "draft the application for", or picks a role from a scan to apply to. Also use when hcho says "submitted <company>" to mark a packet submitted. Never submits anything.'
---

# Application packet

Turns one job posting into a packet hcho can review and submit in about ten minutes.
The packet's facts come only from the Master profile (`projects/Job_Search/profile/`), so every line is true and traceable.
Terms (Master profile, Claim, Evidence scale, Skill index, Application packet, Account action) are defined in the root `CONTEXT.md`.

## Hard rules

- **Never submit, apply, or fill a form.** Submitting is an Account action hcho takes himself.
- **Only Claims.** Every resume line and answer cites Master profile Claims, and `build_packet.py` refuses numbers the cited Claims do not contain. Rephrase toward the posting's words; never add a fact, tool, number, or outcome.
- **Never copy from `projects/Job_Search/Resume/*.docx`.** Those older resumes contain overstated lines; the profile's `retired_phrases` lists them.
- **A missing fact is a profile change, not a wording trick.** If the packet needs something the profile lacks, find the evidence and add a Claim (or ask hcho), re-render the profile, then continue.
- **No em dashes** anywhere hcho will send. Use the `unslop` skill on every answer.

## Workflow

### 0. Start

- Read this skill's `MEMORY.md` and apply anything relevant.
- Run `python3 render_profile.py --check` in `projects/Job_Search/profile/`; fix any failure first.
- Get today's date with `date +%Y-%m-%d`.

### 1. Folder

- One folder per role: `projects/Job_Search/applications/<YYYY-MM-DD>-<company>-<role-slug>/`.
- If a folder for the same posting already exists, reuse it. Never overwrite a packet whose status is `submitted`.

### 2. Snapshot the posting into `posting.md`

- Fetch from the employer's ATS, not an aggregator:
  - Greenhouse: `https://boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>?pay_transparency=true&questions=true` (description plus the form's questions).
  - Ashby: `https://api.ashbyhq.com/posting-api/job-board/<org>?includeCompensation=true` (description); the form's fields come from the public job page.
  - Workday: `https://<tenant>.wd<N>.myworkdayjobs.com/wday/cxs/<tenant>/<site>/job/<path>` with `Accept: application/json`.
- Record: date read, live or closed, posted date, location and work mode, compensation, and **every form field** (which are free text, any word limits, whether a cover letter field exists).
- Then the description verbatim, with em dashes, en dashes, and curly quotes replaced by plain characters.

### 3. Confirm the fit before drafting

- Match each required line to the Skill index and Claims as Met (employer), Met (project), Partial, or Missing.
- Project time meets a years requirement only when the posting does not say "professional", "industry", or "research".
- A shortfall in years can be offset by shipped work; a missing core competency (the role's spine) cannot (job-hunter rule of 2026-06-22).
- If the honest score is below Fit 4, stop and tell hcho before drafting anything.
- Record the score in `role.fit`; for a borderline role, write the reasoning in the latest scan or re-score note.

### 4. Draft `packet.yaml`

Start from `assets/packet-template.yaml`.

- **Headline:** the role's language, no numbers unless a cited Claim has them.
- **Summary:** two or three sentences that answer the posting's core ask.
- **Experience:** periods in this order: `independent`, `omdena`, `career-break` (no bullets), `zebra`.
  - Pick about 12 to 15 bullets in total, the ones that answer the posting's required lines, most relevant first.
  - Label independent-period bullets with the project name exactly as the profile's `projects` list spells it, so the resume shows one project heading with its tagline.
  - Mirror the posting's terms where a Claim supports them.
- **Skills:** three or four groups, one line each, vocabulary terms only, ordered by the posting's keywords.
- **Answers:** one per free-text field on the actual form, using the field's own wording and limit (150 words if none is stated). First person, specific, and run through `unslop`. No cover note unless the form has a field for one.
- **Gaps:** every Partial or Missing line from step 3, plus anything public an interviewer may raise (a failing gate, a broken demo), each with how to own it honestly.

### 5. Build and check

```
python3 projects/Job_Search/applications/build_packet.py <folder>
```

- Fix every reported problem by changing wording or citations.
- **Stale numbers:** re-read each source, update the Claim's number and `as_of` in the profile, re-render the profile, then rebuild.
- **Over one page:** cut the least relevant bullets or tighten wording.
- Read the PDF with the Read tool and check the layout: headings, date alignment, wrapping, nothing on a second page.

### 6. Hand off

- Tell hcho, briefly: the folder, the fit, what to look at first, the answers, and the top gaps.
- Leave `status: draft`. When hcho approves, set `status: approved`.

### 7. After hcho submits

When hcho says "submitted <company>":

- Set `status: submitted` and `submitted_on: <today>` in `packet.yaml`, then rebuild so `packet.md` shows it.
- Update that role's Status in the latest scan note to `Applied (<date>)`.

## Files

- `projects/Job_Search/applications/build_packet.py`: the checker and renderer (tests in `test_build_packet.py`).
- Per packet: `packet.yaml` (source), `posting.md` (snapshot), and generated `Hyung_Cho_Resume.pdf`, `Hyung_Cho_Resume.docx`, `packet.md` (the review page).

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- **Start of every run:** read `MEMORY.md` and apply anything relevant before doing the work.
- **Writing is feedback-gated:** append only when hcho explicitly says to remember something for this skill (a "remember this", a correction, or a stated preference). Do not log routine runs.
- **How to append:** add a dated bullet under `## Notes` in the form `- [YYYY-MM-DD] <note>`, using the real date from `date +%Y-%m-%d`.
- **Cap:** keep `MEMORY.md` under 100 lines. When it nears the cap, tell hcho and ask which entries to prune. Never delete entries silently.
