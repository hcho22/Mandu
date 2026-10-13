---
type: entity
tags: [tool, claude-code, anthropic, agentic-engineering]
status: established
source-count: 8
last-updated: 2026-10-02
---

# Claude Code

Anthropic's ([[anthropic]]) agentic coding CLI/tool, built by [[boris-cherny]] among others.
Runs the Claude models in an agent harness with memory, context management, slash commands, skills, sub-agents, and scheduled loops.

## What shows up in the wiki

- [[ai-operating-system-tutorial]] - the substrate of a personal [[ai-operating-system]]: do all work in Claude Code first so context compounds; the home for [[building-skills]] and the [[capabilities-not-instructions]] key ring.
- [[ai-era-50-career-tips]] - named (with Codex) as one of only two agentic coding tools "survived in production," and the tool to master for [[agentic-engineering]]; Opus 4.5 is the generation that made it "click."
- [[production-agent-with-cma]] - ships a built-in Claude API skill that makes it "really good" at building on Anthropic's Managed Agents APIs ("Claude can help you build your own Claude").
- [[every-claude-feature-ranked]] - a 500-hour tour of its feature surface (Skills #1; status line, routines, sub-agents vs [[agent-teams]], [[checkpoint-rewind]], auto-memory, /goal, /insights).
- [[working-with-fable-5]] - Theo's ([[theo-t3]]) production workflow: reasoning-effort control ([[reasoning-effort-discipline]]), `CLAUDE.md` as a [[model-selection]] glossary, [[model-routing]] by shelling out to Codex via `bash`, JS **workflows** (fan-out + judge panel) vs **sub-agents**, and the long-running **"goal"** that ran ~5 hours to clear a backlog.
- [[designing-loops-and-workflows]] - **the first primary-source account**, from [[tharic]] on the Claude Code team.
- [[one-person-marketing-team]] - **the first source that uses it for no coding at all**: a marketing project generating a website, ads, video, and a spreadsheet, driving [[higgsfield]] over MCP.
- [[token-maxing-with-agents]] - Theo's claim that Claude subscriptions may be used only inside Claude Code; it accepts a custom API endpoint (as used for AWS Bedrock), and he reports its subscription auth needing renewal every two to three days. Driven across machines from [[t3-code]].

## Used as a project shell, not a coding tool ([[one-person-marketing-team]])

The seventh source is the outlier in this list and worth separating out, because its whole argument rests on a property of the tool rather than on the model.

> Despite the name, it is not being used for coding.
> It is being used **because it works out of directories and projects**, which is what lets context compound over time.

Practical surface from that source, aimed at a non-technical user:

- **Desktop app**, installed per OS and signed into with an existing subscription; the interface is a chat box plus a folder picker, and a "local" indicator shows it is running against your own machine.
- **Open folder plus Trust workspace** is the setup step, and the source correctly flags what trusting grants: reading, adding, editing, and moving files inside that folder.
- **Files panel** (three dots, top right) gives a live file-tree view of what the agent is creating, which is the observability surface for a user who will never read a diff.
- **Custom connectors** (Customize -> Connectors -> Add custom connector) take an MCP URL and an OAuth grant, after which the agent operates the third-party tool directly.

The generalized claim is filed as [[own-the-context-layer]]: what the tool actually sells here is the project directory, and everything else is rented.

## The orchestration primitives (from the team, [[designing-loops-and-workflows]])

- **`/loop`** - the general mechanism for iterative, orchestrated work.
- **`/goal`** - reminds the agent of its exit condition so it does not stop early; for when spec and exploration are already done.
- **Workflows** - the most powerful of the three; spin up [[sub-agents]] that do the work in parallel and verify it, making a non-deterministic task closer to deterministic. Implemented as a JS file that can be saved into a skill.
- **The selection rule** is [[verification-signal-picks-the-mechanism]]: deterministic check takes `/goal`, subjective check takes a workflow with a rubric and a separate verifier ([[self-referential-bias]]).

## Product and org facts from that source

- **The system prompt was cut by 80%,** on the reasoning that smarter models need less direction, fewer constraints, and fewer examples ([[principles-over-constraints]]).
- **HTML artifacts** are used broadly at Anthropic for sharing plans, PRs, status reports, and incident reports; at time of recording they were on Team and Enterprise plans, not Max or Pro.
- **Claude in Slack ("cloud tag")** is the async sibling surface: parallel and background work (explorations, PR specs, babysitting a PR) happens there, focused iterative work happens in Claude Code. Every agent and channel has its own memory, and skills trigger from natural language with no special syntax.
- **`simplify`**, a repo-cleanup tool by [[boris-cherny]], is named as the answer to workspace slop.
- MCP context cost "depends on the MCP"; the MCP team has invested in reducing it via tool search.

## Notes

Central node across the AI-builder sources hcho is ingesting; the Fable5, claude-features-ranked, Claude-managed-agents, and now the Claude Code team interview all extend it.
Relevant to hcho directly: mastery of Claude Code is repeatedly framed as independently hireable.
Note the evidentiary shift with the sixth source: prior entries describe the tool from outside, and this one describes the intent behind it from inside, which is why the two accounts of workflows (Theo's fan-out-plus-judge-panel and Tharic's verify-against-a-rubric) agree on structure without either citing the other.
