---
type: concept
tags: [agentic-engineering, agent-operations, browser-use, computer-use, tools, codex]
status: seed
source-count: 1
last-updated: 2026-08-05
---

# Browser Use vs Computer Use

Two distinct automation surfaces an agent can act through, distinguished in [[running-life-on-codex]] by [[jason-openai-codex]]:

- **Browser use** - operating inside the agent's in-app browser for **website** tasks. It supports OAuth/login and uses your **cookies**, so it works while logged into your accounts, and can drive **multiple tabs** at once.
- **Computer use** - **OS / application-level** control, for tasks that need the machine itself rather than a website (settings, desktop apps, file moves, app testing).

The rule of thumb: reach for browser use when the task lives on a logged-in website; reach for computer use when there is **no good API or web path** and you have to drive the actual application.

## Key points

- **Cookies are the capability.** A logged-in browser sees far more than a logged-out one; the agent inherits your authenticated sessions, which is what makes browser use powerful and also what makes it sensitive (it acts as you).
- **Multi-tab review beats a summary.** For comparison/shopping research, having the agent open each candidate in its own tab (then you review side-by-side and check out yourself) is faster to judge than a markdown write-up - the human keeps the final selection.
- **Computer use fills the API gaps.** Example: an Airtable export with no clean API - the agent opens the export, presses download, moves the file, and continues the pipeline; also general app testing.
- **Trust is calibrated by the operator, not the platform.** Jason does not yet let computer use complete purchases/checkouts autonomously - his own risk line, not a product limit ([[phased-autonomy]], [[cost-of-being-wrong]]).

## Synthesis

This names a distinction the wiki had only implicitly. [[agent-building-blocks]] lists "tools" abstractly and [[devin]] is noted for "reliable browser testing," but this is the first source to separate the **web surface** (logged-in, cookie-bearing, multi-tab) from the **OS surface** (app-level, for no-API tasks) and to attach a selection rule and a trust boundary to each.

The load-bearing caution for hcho is the authentication one: a cookie-bearing browser agent acts inside your live sessions, so the [[credential-vaults]] and [[capabilities-not-instructions]] discipline (don't rely on an instruction to keep an agent out of something it can technically reach) applies directly - the safe default is to gate the irreversible actions (purchases, sends, deploys) behind a human, exactly as Jason gates checkouts.
