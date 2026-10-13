# CreativeBridge

**One-liner:** A K-12 mobile story-writing app where users build narratives collaboratively with AI across grade levels. React Native + Expo, multi-AI backend (GPT-4o-mini for stories, Stable Diffusion 3.5 for images, Claude Skills SDK for quality).

**Repo:** https://github.com/hcho22/CreativeBridge (**public since 2026-10-08**; hcho made it public so its Master profile Claims have evidence anyone can open. The 2026-10-08 decision log noted one committed OpenAI key in its history that had to be revoked first; Mandu has no record that it was.)

**Milestone:** **TestFlight complete** (target — see `context/current-priorities.md`).

---

## Status

_Update this line as the project moves. Last reviewed: 2026-06-01._

- **Phase:** Mature build, COPPA-compliant, on iOS TestFlight. Feature set is largely implemented (see feature-status table below). Remaining work is release-readiness and polish toward the TestFlight-complete milestone.
- **Confirm with hcho:** exact current state of each in-progress item, and the real blocker list.

## Todos

Working board. Check items off as they land; add new ones at the top of each section.

### Release / TestFlight (grounded in the repo's deploy tooling)

- [ ] `npm run lint` and `npm run test:coverage` green
- [ ] `bash scripts/pre-deployment-check.sh` passes (pre-deploy validation)
- [ ] `npm run eas:build:ios` succeeds (EAS iOS build)
- [ ] `npm run eas:submit:testflight` (TestFlight submission)
- [ ] `npx ts-node scripts/smoke-tests-production.ts` passes post-submit
- [ ] TestFlight build reviewed and approved by Apple

### Bugs

- [ ] _(none logged yet — add as found)_

### Polish / UX

- [ ] _(add items)_

### Post-launch / backlog

- [ ] _(add items)_

## Feature status

Derived from the repo README, which describes these as built. Mark each as you verify on the current TestFlight build. Legend: `Shipped` / `In progress` / `Planned`.

| Area | Feature | Status |
| --- | --- | --- |
| Story | Grade-level creation (K-2 / 3-5 / 6-8 / 9-12) | Shipped (verify) |
| Story | AI-assisted 5-round collaborative writing (GPT-4o-mini) | Shipped (verify) |
| Story | Continuation with "Previously Written" context | Shipped (verify) |
| Story | Advanced search + cosine-similarity scoring | Shipped (verify) |
| Story | Download/export with theming | Shipped (verify) |
| Images | Generation via Stable Diffusion 3.5 (costs 1000 XP) | Shipped (verify) |
| Images | Display modal + adaptive glass background | Shipped (verify) |
| Auth | Clerk OAuth (Google/Apple) → Convex JWT | Shipped (verify) |
| Auth | Supabase email/password legacy + account linking | Shipped (verify) |
| Profile | XP economy, streaks, onboarding (150 XP) | Shipped (verify) |
| Quality | Claude Skills SDK content assessment | Shipped (verify) |
| Voice | Native speech recognition + on-device TTS | Shipped (verify) |
| Platform | iOS + Android via Expo / EAS | iOS on TestFlight; Android (verify) |

## Tech stack

- **Frontend:** React Native 0.81.5 + Expo 54 + TypeScript 5.8; React Navigation v7; Context API
- **Backend (primary):** Convex (real-time DB, native Clerk auth, file storage)
- **Backend (fallback):** Supabase (Postgres + RLS for legacy users)
- **AI:** OpenAI GPT-4o-mini (stories), Replicate Stable Diffusion 3.5 (images), Claude Skills SDK (quality)
- **Auth:** Clerk (OAuth) → Convex JWT verification
- **Testing:** Jest + Detox (E2E)
- **Build/Release:** EAS Build for iOS/Android, TestFlight submission

## How Claude helps

Built, production-shaped portfolio project (not tutor mode). Help here means status tracking, release-checklist execution, bug triage, code review, test/build debugging, and demo/portfolio framing. This is also a portfolio asset for the AI Evals positioning (multi-AI orchestration, content-quality assessment, monitoring/anomaly detection).

## Daily tracking (optional)

To log a working session, say "log my CreativeBridge progress" and the `daily-log` skill will create `projects/CreativeBridge/log/<date>.md` on first use.
