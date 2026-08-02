# PRD: Account Deletion (App Store Guideline 5.1.1(v))

**Status:** Implementation-ready. Not started.
**Opened:** 2026-07-31
**Blocks:** TestFlight / App Store submission. This is a hard rejection blocker, not a nice-to-have.
**Repo:** `/Users/hcho/Developer/RepToday/ios`

## Why this exists

The 2026-07-16 GTM pre-publication checklist carried this as an unverified item: *"Account deletion path:
because optional Sign in with Apple exists, App Store Guideline 5.1.1(v) account-deletion requirements
attach - verify the build satisfies them before submission."*

Verified 2026-07-31 against the built app. **It does not.** The app ships Sign in with Apple with zero
deletion path - no "Delete Account", no "Delete my data", and no reachable sign-out anywhere in the UI.

This corrects a standing assumption in `context/current-priorities.md` that Rep Today's next step "is not
more build." One mandatory build remains before submission is possible.

## Current state (audited 2026-07-31)

**Account creation exists:**

| What | Where |
|---|---|
| Entitlement | `RepToday/RepToday.entitlements:13-16` (`com.apple.developer.applesignin`) |
| UI button | `Views/Onboarding/OnboardingView.swift:204-214` |
| Credential handling | `ViewModels/OnboardingViewModel.swift:158-174` |
| Ceremony | `Services/Auth/AppleSignInAuthorizing.swift:70-97` |
| Production wiring | `DI/ServiceContainer.swift:166` |

Sign-in is optional (falls back to a local UUID), but Apple treats *supports account creation* as
triggering 5.1.1(v) regardless of whether the user must use it.

**Deletion capability that exists but is unreachable dead code:**

- `AppleAuthService.signOut()` - `Services/Auth/AppleAuthService.swift:43-45`. Clears only the Keychain
  identifier. Called from tests and mocks only; no view or view model calls it.
- `CoreDataUserService.deleteCurrentUser()` - `Persistence/CoreDataUserService.swift:44-53`. Deletes all
  `CDUser` records. Zero non-test call sites.

**No Settings surface exists.** The Profile tab is a placeholder: `Views/RootView.swift:48-56` renders
`PlaceholderTabView` with an icon, title, and subtitle - no options, no navigation, no toolbar.
`OnboardingView.swift:266` acknowledges "there is no profile-edit surface yet."

**No credential revocation anywhere.** No `getCredentialState`, no `appleid.apple.com/auth/revoke`. There is
no backend that could revoke: `convex/` is empty and `proxy/src/worker.js:12` states "Nothing is persisted:
no KV, no D1, no cache."

## Data stores a deletion path must clear

| Store | Location | Existing delete capability | Gap |
|---|---|---|---|
| **Keychain** (Apple user identifier) | `Services/Auth/AuthCredentialStore.swift:39-108`; service `com.reptoday.app.auth`, account `apple.user.identifier` | `clear()` at :94, never invoked | Must be called. Its own doc comment (:34-36) notes it **survives reinstall** - leaving it resurrects the identity |
| **CoreData → CloudKit private DB** (`CDUser`, `CDWorkoutLog`, `CDSessionPolicy`), container `iCloud.com.reptoday.app` | `Persistence/PersistenceController.swift:23-31, 45, 122-133` | `deleteCurrentUser()` (users only); `deleteLog(id:)` is per-id only (`CoreDataWorkoutLogService.swift:56-67`) | Needs bulk purge; `SessionPolicyStore` (`Services/Programmer/DeterministicSessionPolicyService.swift:220-225`) has **no delete method at all** |
| **CoreData local** (`CDActiveSession`) | `PersistenceController.swift:11-13`; `Services/ActiveSession/ActiveSessionStore.swift:19` | `clear(for: userId)` exists and is already used (`ReadyViewModel.swift:294`) | Reuse |
| **UserDefaults** | `Utilities/AppState.swift:19-51` - `AppState.isOnboarded`, `AppState.selectedTab` | None | Must reset, or the user lands in the main tabs with no profile (`ReadyViewModel.swift:136` "No profile found yet.") |
| **HealthKit** (write-only workouts + active energy) | `Services/Health/HealthKitService.swift:31-33, 53-71` | None | Not strictly required by 5.1.1(v), but samples are app-attributed via `HKMetadataKeyExternalUUID` and should be offered for removal |

## Stories

### US-D01 - Profile/Settings screen

Replace `PlaceholderTabView` at `Views/RootView.swift:48-56` with a real `ProfileView`.

- Shows the current movement basics (read-only is acceptable for this story; profile editing is out of scope).
- Contains a `Section` with a destructive **Delete Account** row, tinted `.red`.
- The path must be findable, not buried. One tap from the Profile tab.
- **AC:** the Profile tab renders a real screen; Delete Account is visible without scrolling on the smallest
  supported device (iPhone SE class).

### US-D02 - Bulk delete methods on the persistence protocols

Two protocol methods do not exist and must be added.

- `deleteAllLogs(for userId:)` on `WorkoutLogServiceProtocol` (`Services/Protocols/ServiceProtocols.swift:121-125`).
- `delete(for userId:)` on `SessionPolicyStore` (`Services/Programmer/DeterministicSessionPolicyService.swift:220-225`).
- **AC:** both are implemented against CoreData, mocked in the test doubles, and unit-tested for the
  delete-everything-for-this-user case including the zero-records case.

### US-D03 - AccountDeletionService orchestration

A new service, wired through `DI/ServiceContainer.swift`, that performs the full teardown in order:

1. Delete all `CDUser`, `CDWorkoutLog`, `CDSessionPolicy`, `CDActiveSession` records across **both** store
   configurations, then save, so the CloudKit mirror propagates tombstones.
2. Call `AuthCredentialStore.clear()` (`AuthCredentialStore.swift:94`) to remove the Keychain identifier.
   Non-optional: it survives reinstall.
3. Clear `AppState.isOnboarded` and `AppState.selectedTab` (`AppState.swift:48-51`).
4. Route back to onboarding.

- Must be idempotent and safe to run when the user never signed in with Apple (local-UUID case).
- **AC:** after deletion, a relaunch lands on onboarding with no residual profile, no logs, and no Keychain
  identifier. Verified by deleting, force-quitting, relaunching.

### US-D04 - Confirmation flow

- Tapping Delete Account presents a confirmation alert naming what is destroyed (profile, workout history,
  and, if applicable, the Sign in with Apple link) and stating it cannot be undone.
- Destructive action is the non-default button.
- **AC:** cancelling leaves all data intact; confirming runs US-D03 exactly once even on double-tap.

### US-D05 - Sign in with Apple credential handling

Nothing in the codebase revokes the credential today, and reviewers frequently reject Sign in with Apple
apps that delete local data without addressing the token. With no backend, two viable options:

- **(a)** Call `ASAuthorizationAppleIDProvider().getCredentialState(forUserID:)`, and on deletion present
  clear guidance plus a deep link to Settings → Apple ID → Sign in with Apple to stop using the Apple ID.
- **(b)** Stand up a proxy endpoint that calls `https://appleid.apple.com/auth/revoke`. The proxy exists
  (`proxy/`) but is explicitly stateless, so this adds a real server dependency and Apple client-secret
  key management.

**Recommendation: (a).** It is honest about the on-device architecture, adds no server dependency and no
key rotation burden, and matches the app's "nothing leaves the device" privacy story - which is also the
story the privacy policy and App Store nutrition labels will tell. Revisit only if review pushes back.

- **AC:** the deletion flow surfaces the Apple ID guidance when a Sign in with Apple credential was used,
  and does not surface it in the local-UUID case.

### US-D06 - HealthKit sample removal (optional, recommended)

- Offer, as a checkbox or a second confirmation step, deletion of app-authored HealthKit workouts via
  `HKHealthStore.delete`, matching on `HKMetadataKeyExternalUUID`.
- Default to **off**. Deleting the user's health history without explicit intent is worse than leaving it.
- **AC:** when checked, app-authored samples are removed and no other app's samples are touched.

## Out of scope

- Profile editing (this is a deletion story, not a profile story).
- Any change to the deterministic engine, paywall, or session loop.
- Backend account systems. The app stays on-device.

## Verification

- Unit tests for US-D02 and US-D03 orchestration, including the never-signed-in path.
- One UI test driving the full flow: Profile tab → Delete Account → confirm → lands on onboarding.
- Manual on-device check: delete, force-quit, relaunch, confirm onboarding and empty history. Then sign in
  with Apple again and confirm a clean new identity rather than the resurrected old one - this is the check
  that catches a missed Keychain clear.

## Downstream

Clearing this unblocks the remaining pre-submission items in
`/Users/hcho/Developer/RepToday/gtm/06-redteam/pre-publication-checklist.md`:
privacy policy authoring and hosting, App Store Connect record and name reservation, trademark clearance,
and the on-device screenshot capture.
