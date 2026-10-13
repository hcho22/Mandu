# Token Maxing with Agents: Video Summary

_Reference summary of a YouTube tutorial by Theo (creator of T3 Code) on getting, accessing and burning AI-agent tokens_

## Overview

Theo argues that the best way to get value from coding agents is to run many of them in parallel, all day and overnight, and to fund that with flat-rate **Claude** and **Codex** subscriptions instead of API billing. The video moves through five parts: (1) getting more tokens, (2) accessing them through one residential IP with a proxy, (3) using tokens well, (4) using tokens “poorly” (offloading silly and small tasks), and (5) using tokens while you sleep by moving dev work to a cheap always-on Linux box.

The through-line is a mindset shift: humans are single-threaded and agents are multi-threaded, so you are the bottleneck. Hand agents problems rather than solutions, de-risk both sides of the merge button, and treat threads like an email inbox you clear rather than a history you re-read.

**Callout key**

- 💡 **Tip**: practical advice you can act on
- 🔧 **Tool**: named tools, products and commands
- 📏 **General Rule**: something the speaker states as broadly true or a firm constraint
- 🗣️ **Speaker Opinion**: the speaker's personal view, estimate or rumor
- ⚠️ **Caution**: risk, ban or terms-of-service warning

---

## Table of Contents

- [1. Opening and Ban Risk](#1-opening-and-ban-risk)
- [2. Sponsor Segment: Parallel](#2-sponsor-segment-parallel)
- [3. Roadmap and Pre-empted Objections](#3-roadmap-and-pre-empted-objections)
  - [Planned order](#planned-order)
  - [Objections he expects, and his replies](#objections-he-expects-and-his-replies)
- [4. Part 1: Getting More Tokens](#4-part-1-getting-more-tokens)
  - [Subscription vs API math](#subscription-vs-api-math)
  - [Why the subsidy exists](#why-the-subsidy-exists)
  - [Codex resets multiply the value](#codex-resets-multiply-the-value)
  - [Data controls and when the API is still right](#data-controls-and-when-the-api-is-still-right)
  - [Which subscriptions are worth it](#which-subscriptions-are-worth-it)
- [5. Part 2: Accessing Tokens at Scale](#5-part-2-accessing-tokens-at-scale)
  - [Ground rules for accounts and IPs](#ground-rules-for-accounts-and-ips)
  - [CLIProxyAPI](#cliproxyapi)
  - [Changes Theo says you almost have to make](#changes-theo-says-you-almost-have-to-make)
  - [Limits math (Claude)](#limits-math-claude)
  - [Tailscale and the fleet-management repo](#tailscale-and-the-fleet-management-repo)
  - [Reset mechanics and the use-it-or-lose-it mindset](#reset-mechanics-and-the-use-it-or-lose-it-mindset)
  - [Update added later: Opus 5.5](#update-added-later-opus-55)
- [6. Part 3: Using Tokens Well](#6-part-3-using-tokens-well)
  - [De-risk both sides of the merge button](#de-risk-both-sides-of-the-merge-button)
  - [Bring the agent in when you start thinking](#bring-the-agent-in-when-you-start-thinking)
  - [Let the agent span the whole path](#let-the-agent-span-the-whole-path)
- [7. Running Many Threads with T3 Code](#7-running-many-threads-with-t3-code)
  - [Threads are tasks, not history](#threads-are-tasks-not-history)
  - [Shortcuts and features he highlights](#shortcuts-and-features-he-highlights)
  - [Prompt patterns from live examples](#prompt-patterns-from-live-examples)
- [8. Part 4: Using Tokens Poorly](#8-part-4-using-tokens-poorly)
  - [What the real workflow looks like](#what-the-real-workflow-looks-like)
  - [T3 Code setup](#t3-code-setup)
- [9. Part 5: Using Tokens While You Sleep](#9-part-5-using-tokens-while-you-sleep)
  - [Handling resource limits](#handling-resource-limits)
- [10. Closing](#10-closing)
- [Appendix A: Caption Corrections](#appendix-a-caption-corrections)
- [Appendix B: Editorial Notes](#appendix-b-editorial-notes)

---

## 1. Opening and Ban Risk

- Hook question: how many agent threads are running *right now*? Fewer than five means you are not using the opportunity; more than five and you will still pick up edge cases and solutions.
- Theo frames the video as one Anthropic would not want people to watch, and says he has taken steps to reduce ban risk.
- Ban track record (his own account): across **30+ Claude accounts** shared between him and friends, one friend was banned **twice**. Both bans were temporary and reinstated almost immediately. The cause: he was on a **VPN** while registering an account with a credit card for a business that was not his.
- Mid-video disclosure (“Leo from the future” in captions, i.e. Theo): this might get you banned and may violate terms of service; he cannot be held liable.

> ⚠️ **Caution:** Theo says plainly that the methods in this video may violate provider terms of service and could get accounts banned. His claim that bans have been rare is based only on his own and his friends' experience.

> ⚠️ **Caution:** Do not run these methods on Google accounts. If a Google account is banned you lose far more than Gemini access.

> 🗣️ **Speaker Opinion:** Theo says there is no real use for Gemini models anyway, so nothing is lost by skipping them.

## 2. Sponsor Segment: Parallel

Paid sponsor read, summarized for completeness. Treat the performance claims as sponsor claims.

- Pitch: agents without search are nearly useless; agents with fast, accurate search are far better.
- Live demo: Parallel returned results in **just over 1 second**; OpenAI's search endpoint took **over 6 seconds**.
- Other Parallel products named: a **monitor** (notifies agents when pages change), a **response API** (synthesized answers to search queries), **extract endpoints** (send a URL, get back structured data, including JS-heavy pages), and an **MCP** server to plug Parallel into existing agents.
- Offer: **5,000 free requests per month** and **$80 in credit** for new sign-ups, via swordv.link/parallel.

> 🔧 **Tool:** **Parallel**: search, monitor, response API, extract endpoints and MCP for agents. Free tier is 5,000 requests per month.

> 🗣️ **Speaker Opinion:** Theo says he historically liked OpenAI's built-in search but found Parallel “night and day” better. This is a sponsored statement.

## 3. Roadmap and Pre-empted Objections

### Planned order

- How to get enough tokens.
- How to access them once you have them.
- How to use them well, then poorly (which he calls more fun and more important).
- How to use them while you and your laptop are asleep.

Stated goal: not a formula to copy, but ideas and examples that show how he operates with agents, which he credits for **100+ PRs a day, part-time**. The best outcome would be viewers building their own approaches and bringing him solutions he had not thought of.

### Objections he expects, and his replies

| Objection | Theo's reply |
|---|---|
| “This only works for side projects, not real apps.” | Says similar strategies are used at companies as large as AWS, Microsoft and some Fortune 500 firms (learned via friends, not named or verified), including the subscription approach. |
| “Not all of us are rich.” | Says the approach saves a large amount of money and works at small and large scale. Claims the “300k+” spend figures people have seen are not what he actually pays; his worst case is roughly **$1,000 in for every 50,000 of tokens out** [?]. |
| “You're paid off by OpenAI/Anthropic.” | Says he has paid each of them more than the commenter is worth. |

> 🗣️ **Speaker Opinion:** All of these rebuttals are Theo's assertions. The large-company examples are second-hand and unnamed.

## 4. Part 1: Getting More Tokens

### Subscription vs API math

Theo's core claim: **$200 on an API buys $200 of tokens**, while the flat-rate subscriptions return far more.

| Plan | Approx. token value (Theo's estimate) | Notes |
|---|---|---|
| Claude API, $200 | $200 | Baseline for comparison |
| Codex API, $200 | $200 | Same as above |
| Claude subscription, $200/month | ~**$8,000** | Only ~**$4,000** of that is **Fable** because Fable has a separate 50% limit. Still ~20x on Fable. |
| Claude subscription, $100/month | About half the $200 total | But only about a **quarter** of the hourly limit, so the **5-hour limit** is much tighter and harder to burn fully. Theo does not recommend it. |
| Codex subscription, $200/month | ~**$12,000** | No split between the top model and cheaper models; you just get tokens. |

> 💡 **Tip:** Theo's suggested path: save for the $200 tier, burn it, find a way to make money from what you built, then reinvest and add more accounts.

> 🗣️ **Speaker Opinion:** He recommends skipping the $100 Claude tier. This is a personal recommendation based on his usage patterns, not a rule.

### Why the subsidy exists

- **Fable** API pricing: **$10 per million tokens in, $50 per million out**.
- When Anthropic announced **Claude Mythos Preview** in April (internal use for **Project Glasswing** partners), it quoted **$25/M in and $125/M out** for continued use afterwards. Theo reads Fable's price as roughly **70% cheaper** than that intended rate.
- Rumored margin on API tokens: about **95%** (napkin math from people he knows). He says Anthropic cut prices to protect its lead and make competitors harder to justify.
- He claims Anthropic rents compute from **SpaceX** (stated in passing, not explained).
- Combined with the ~1:40 subscription subsidy, he says to “mentally double” the Claude and Codex numbers.

> 🗣️ **Speaker Opinion:** The 95% margin, the SpaceX compute rental, the claim that OpenAI would never charge less than Mythos pricing, and the quip that OpenAI only ever keeps, cuts or doubles prices are all Theo's inference or rumor, not confirmed figures.

### Codex resets multiply the value

- Theo cites **14 resets in 30 days** (as counted by someone he saw, crediting **Tibo**), about one reset every 2 to 3 days.
- So a weekly allowance of roughly $4k behaves more like a 3-day number, and a $200 Codex sub could be worth up to ~**$24,000**.
- OpenAI has **temporarily paused new $200 Codex subscriptions**. Theo fears this video will make that worse.
- Resets tend to land on Friday evenings, when enterprise API demand is low.

> 🗣️ **Speaker Opinion:** He believes OpenAI gives resets on Fridays hoping power users burn capacity before enterprises return Monday. He also says he would shift his sleep schedule to keep using the subsidy and expects providers may eventually push subsidized use to off-peak hours.

### Data controls and when the API is still right

> 💡 **Tip:** In **Codex**: **Settings → Data controls → “Improve the model for everyone” → off**. Theo says that once this is off, a personal plan's terms are effectively identical to a Team account's. A similar setting exists in **Claude Code** (he did not show where).

> 🗣️ **Speaker Opinion:** He claims many companies quietly pay for personal-tier subscriptions with data sharing off, and that every API dollar spent for privacy reasons is “80 to 90 cents thrown away”. The company claim is unverifiable; the privacy equivalence is his reading of the terms.

> 📏 **General Rule:** Subscriptions are for your own work: running prompts on your codebase, agents triaging your GitHub issues, and similar. **Do not use them to serve user-facing or public traffic.** For that, use the API.

> ⚠️ **Caution:** Using subscription accounts as a cheap replacement for the API to serve end users is against the rules; Theo says that is when you deserve a ban.

### Which subscriptions are worth it

- Only **Claude** and **Codex** subscriptions give a **95 to 98%** discount on tokens.
- **Cursor** likely gets about **30 to 50% off** at best from Anthropic; **OpenCode** and **T3 Chat** subscriptions have far smaller subsidies.
- **Grok**: might make sense if “Grok 4.7” [?] lands well, but he says Grok models cannot stay coherent for long enough to token-max.

> 🗣️ **Speaker Opinion:** These comparisons are Theo's estimates of provider deals, not published figures.

## 5. Part 2: Accessing Tokens at Scale

### Ground rules for accounts and IPs

- In his earlier video he showed two Claude Code subs where changing auth in another tab let a running task recover. That does not scale to many accounts, machines and threads.
- Claude Code auth breaks every **2 to 3 days**; you need a system that manages it from one shared place.

> 📏 **General Rule:** Theo's guidance: route everything through **one residential IP**, from one place, rather than many machines logging in at once.

> ⚠️ **Caution:** Do not sign into Claude or Codex (especially **Claude Code**) from a **VPS** or cloud server. He says Anthropic is aggressive about sign-ins and requests from known server IP ranges (AWS, Hetzner and similar), because of resellers and distillation concerns. Avoid VPNs and avoid simultaneous traffic from multiple computers.

### CLIProxyAPI

> 🔧 **Tool:** **CLIProxyAPI** (“CLI Proxy API”): you sign into it with OAuth for Codex and Claude; it maintains the auth and exposes an API that Claude Code and Codex point to instead of the normal OAuth servers.

- Theo started from a fork called **VibeProxy** and has since forked it heavily; his dashboard looks different from the stock one.
- The dashboard is served from **management.html**.

> 💡 **Tip:** First token-maxing task: give an agent a screenshot of a dashboard you like and ask it to restyle the proxy UI to match. He says a stronger model (**Fable** over weaker ones) will manage it.

### Changes Theo says you almost have to make

- **Account prioritization.** Default behavior spreads traffic evenly across accounts. Change it to prefer the account whose limit **resets soonest**, so you burn what is about to expire. Skip this only if you keep hitting 5-hour limits across all accounts.
- **WebSocket for Codex.** By default Codex subs do not use WebSocket; enabling it greatly reduces latency in message passing. He calls the setup a little annoying.
- **Session affinity and account affinity.** Prompts in the same thread should go to the same account, because **caches are account-specific**. Switching accounts mid-thread (for example 800k tokens in) forces a cache rebuild; per-prompt or per-tool-call switching would be wasteful. Cache lifetime is **5 minutes**. Stock CLIProxyAPI handles this well by default.

> 💡 **Tip:** Watch cache read and write volumes. If they look huge, ask the agent: “How are we handling session affinity? Are we writing cache more than we should be?”

> ⚠️ **Caution:** Theo warns that a weaker model (he names Opus) might set up affinity incorrectly. Verify it.

### Limits math (Claude)

- Theo says 100% of the **5-hour** limit on the **20x** plan equals exactly **40% of the 7-day Fable** limit, and about **20% of the full 7-day** limit.
- Ignore the greyed “Opus bucket” column in his dashboard; only the 5-hour and the Fable 7-day matter.

> 🗣️ **Speaker Opinion:** If you hit 5-hour limits even with several accounts, he says to slow down. He also calls Opus “a trash model” and avoids it (see the Opus 5.5 update below). The 40%/20% figures are his own calculation.

### Tailscale and the fleet-management repo

- The proxy is reached over **Tailscale** on his tailnet, using the default port [?] and a `*.ts.net` hostname. Because it is only reachable on the tailnet, it works **without an API key**.
- He keeps a **fleet-management repo** that documents every machine and a “set up a box” file listing what each machine should have: `rg`, `fd` [?], `jq`, `tmux`, `btop`, Node, Python, build tools, Codex and Claude Code configured to use the proxy.
- Workflow for a new machine: set up **SSH**, open the fleet repo in Claude Code, Codex or **T3 Code**, give the agent the box and SSH key, tell it to set the machine up, then approve the **Tailscale** device request when it pops up.
- Result: **5 Claude accounts and 4 Codex accounts** behind one residential IP, with all machines connecting over Tailscale.
- Pointing Claude Code and Codex at the proxy is “trivial”: have your agent swap two variables in the config. Both tools support custom API endpoints because many companies use **AWS Bedrock**. The **Codex desktop app** now shows the proxy name in a corner.
- Alternative: keep a normal install and create a second instance with a **different home directory** and its own command.

> 💡 **Tip:** Have your agent do the config. Theo says he will not explain it step by step.

> ⚠️ **Caution:** Use Claude subscriptions **only inside Claude Code**, via the proxy. Using them in other tools will get accounts banned, he says.

> ⚠️ **Caution:** Setting an API key for another project on the proxy broke all his inference, since it normally runs with no key. Check before changing proxy auth.

### Reset mechanics and the use-it-or-lose-it mindset

|  | Codex | Claude |
|---|---|---|
| What a reset does | Resets the weekly limit **and its timer**, so a sub renewing in a day now renews in 7 days | Resets only the **percentages** back to 100%; dates and times stay the same |
| Types | **Banked** (click any time, costlier to OpenAI) and **immediate** | One type only |
| Practical effect | Can leave all accounts ~6 days from renewal; Theo holds ~10 banked resets across subs | A reset a day before renewal means burn everything now or lose it |

> 🗣️ **Speaker Opinion:** Mindset: think of a subscription as a gift of about $4,000 per week that **vanishes** if unspent, the opposite of API-price thinking. Theo calls this the “depressed” mindset of feeling money lost. This is his personal framing.

### Update added later: Opus 5.5

Theo inserted a later clip: **Opus 5.5** did not exist when he filmed. All advice still applies, and Opus 5.5 behaves much like **Fable 5.1**. He found it hard to hit limits with Opus 5.5 on one sub, so you may need fewer accounts and may not need the proxy at all.

> 🗣️ **Speaker Opinion:** He says Opus 5 was “a useless dumpster fire” and Opus 5.5 is a “pretty good model”.

## 6. Part 3: Using Tokens Well

Theo points to a separate video about coding with one hand (after surgery) for more examples. The question to hold in your head: **how can I use more tokens to care less?** How early can the agent join, and how long can it run before you need to look?

### De-risk both sides of the merge button

- **Before merge:** make it likely that by the time you see the PR, it is safe to merge. Theo estimates **10 to 15%** of his tokens go to writing code and **85 to 90%** to verifying it.
- Cutting the chance of a bad or flawed PR from **5% to 1%** lets you spend far less attention per PR.
- **After merge:** make bad changes easy to revert and catch problems before users do.

> 📏 **General Rule:** If undoing a bad change takes **more than 15 seconds**, you probably should not be vibe coding yet; fix your systems first. (Stated as Theo's rule of thumb.)

### Bring the agent in when you start thinking

- Theo changed from bringing an agent in after he had decided what to do to bringing it in when he starts thinking. Example: after ~3 weeks of active thought on a problem, he asked an agent for a stupid simple solution and got one.
- He is explicit he is **not** saying stop thinking: decide whether a problem is worth thinking about *before* spending the time on it.
- **Give the agent the problem, not the solution.** Handing it a screenshot and “fix it” often works; if it fails, you have learned the problem is hard and deserves your brain.
- He compares this to managing a team: hand over problems, and if the first solutions come back wrong, you know the problem is novel and you should dive in.

> 💡 **Tip:** Sequence: give the problem → let the agent try autonomously → intervene only if it fails.

> 🗣️ **Speaker Opinion:** “Don't outsource thinking, scale it.” Theo argues it is a better use of time to think about problems agents cannot solve, or to read the solutions they can, than to think for days on something an agent solves in minutes. He pushes back respectfully on a view from “Dan” [?] who disagrees.

> 🗣️ **Speaker Opinion:** If you are not employed as a dev, do not stack subs until you are making money. Burn your own money when you have it, and someone else's (e.g. your employer's) when you do not.

### Let the agent span the whole path

- Many people only let agents work between “knowing what you want” and “PR filed”. Theo wants the agent on the whole range from first hearing of a problem to merge, possibly even merging itself once you trust it.
- Your job then becomes talking to users and handling failures.
- Example run: ~30 minutes to implement and test, open the PR, wait ~15 minutes for AI code review, ~10 minutes fixing, another ~15-minute wait, then ready. That is over an hour you can spend dispatching other threads.

## 7. Running Many Threads with T3 Code

> 🗣️ **Speaker Opinion:** Theo says alternatives to T3 Code struggle once you have more than three threads, and that competitors have copied but not matched it. He builds T3 Code, so treat the comparison as an interested party's opinion.

### Threads are tasks, not history

- Treat threads as to-dos. When a thread is not working it should not demand attention.
- In **T3 Code** you check **Settle** on a finished thread and it leaves the sidebar. Settle is distinct from archive. Goal: **inbox zero**; end the day with threads either gone or running.
- Context-switching costs are not solved; the sidebar just shows which context needs you.
- Theo believes this mindset is easier with ADHD.
- Rule he states strongly: **agents are multi-threaded, humans are single-threaded; you are the bottleneck.** Design work so agents unblock themselves and you enter later.

### Shortcuts and features he highlights

| Feature | What it does |
|---|---|
| `Cmd+Enter` | Sends the prompt and runs the thread **in the background**, leaving you where you are (instead of plain Enter). |
| `Cmd+Shift+O` | New thread. |
| Environment/machine selector (bottom left) | Choose which computer runs the thread. Projects with the same git origin are grouped across machines. Theo uses Linux boxes for long runs and Macs for mobile or computer use. |
| Load balancing (Settings; built by **Maria**) | Auto-distributes threads across all connected servers. |
| Worktrees (default for new threads) | Each thread starts in a new git worktree so agents do not collide. |
| Auto-settle | Default: threads untouched for **3 days**. Theo set it to **7**. |
| Snooze | Hides a thread to be your problem later. |
| Merge disappears the thread | Merging the PR removes the thread from the sidebar. |
| Working threads rendered semi-transparent | Theo's UI choice so you look at them less. |

> 💡 **Tip:** Do not check threads until they show **done** or **input** in the corner.

> 💡 **Tip:** Say in the prompt that the agent may merge if it meets stated conditions. Theo guesses about half his threads are archived without him ever reading the final message.

> 📏 **General Rule:** Few things are a worse use of time than watching an agent work. If it succeeds, merge. If it fails, read the reasoning trace or ask the agent why.

> 🗣️ **Speaker Opinion:** On agents breaking each other's work: worktrees are “not perfect but good enough”, and current models can resolve branch-already-checked-out problems on their own (new branch, clone, etc.). He does not look and says you should not spend time on it.

> 🗣️ **Speaker Opinion:** Malware worry: he says if you think an agent is more likely than you to install malware, you are probably less careful than the agent. A rant, not a general rule.

### Prompt patterns from live examples

- **Problem plus ideas, not a prescribed fix.** For a confusing device-management UI in T3 Connect settings (disconnect seems permanent; update is offered but remove is not), he pasted a screenshot and described the issues. He told the agent to implement directly if confident, otherwise produce **mocks using his HTML skill** to choose between.
- **Feasibility first.** For a paragraph-chunked streaming idea he first asked how hard it would be; the agent said not hard (and estimated “half a day”, which he mocks as models not knowing how long work takes). Then he asked it to build it, file a PR **and** spin up a **Tailscale** environment to try, all in one message.
- **Ask it to babysit.** “Can you babysit this PR and make sure everything is good?” makes the agent monitor the PR continuously.

> 💡 **Tip:** Bundle everything you will need on your next visit (preview environment, PR, babysitting) into the same prompt, so the next time you open the thread you can merge.

> 💡 **Tip:** Theo wants a minimal message queue (pending message sent after the next tool call, or a **steer** button to send immediately) in T3 Code.

## 8. Part 4: Using Tokens Poorly

The “poor” uses are small offloads that save your brain. Theo frames them as silly on purpose.

- Understand a hard-to-parse teammate PR; ask an agent what changed in the **Orchestrator V2** rewrite (worked on by **Julius**) instead of interrupting him.
- Triage all your open PRs and pick what to focus on today.
- Find an email across five inboxes (he opens ChatGPT for this).
- Collect medical records from his inbox and browser dashboards; this ran 30+ minutes while he fired off four more prompts in T3 Code.
- Sweep all GitHub projects and unfinished work on a machine, using many sub-agents, to find abandoned ideas worth reviving. He says this prompt was a deliberate burn of leftover limit.
- Ask about the state of an old PR you have forgotten and why it should merge.

> 💡 **Tip:** When a limit is about to reset with usage left, find silly tasks to burn it on. You learn more than expected, and agents are very good at triaging large numbers of PRs.

> 🗣️ **Speaker Opinion:** Mindset: you should be asking agents things that feel silly, like Googling “where did I leave my keys”. If nothing you ask feels silly, you are not offloading enough.

### What the real workflow looks like

- His real sidebar: **10+ threads** plus a monitor, across **5 Claude Code subs**, with usage left over. Some threads ran 30 minutes, some **18 hours** (started before bed).
- Next morning: go through them one at a time and decide merge, follow-up or discard, like an email inbox; spin up new threads for newly noticed fixes.
- Why other tools fall short, in his view: sidebars do not prioritize work or remove completed work, search is not trustworthy enough to recover old threads, and the sidebar is not shared across machines. His T3 Code sidebar mixes threads from several MacBooks, a server named **Alvin**, **BB1** and a main cloud server, and also shows on his phone.

### T3 Code setup

> 🔧 **Tool:** **T3 Code**: free and open source; supports your Claude/Codex subscriptions; works well with CLIProxyAPI.

- On a new box: SSH in and run `npx t3 connect`, click the link, sign in. Then control the machine from the web, mobile or desktop app with nothing else installed (needs Claude Code or Codex, ideally with a sub or the proxy).
- `npx t3 serve` instead lets you connect over **Tailscale** directly, with no use of T3's servers. He mentions built-in Tailscale support [?].
- Without Tailscale, **T3 Connect** currently allows **3 devices** for free; he wants to raise this.

> 💡 **Tip:** Add “also set up T3 Code so I can connect remotely over Tailscale” to your fleet repo's set-up instructions so agents install it on every new server.

## 9. Part 5: Using Tokens While You Sleep

- If you ever skip sending a prompt because you must close your laptop, move dev work **remote**.
- Recipe: take an old computer, install **Ubuntu**, add **Tailscale**, run **CLIProxyAPI** so traffic comes from your residential IP, and connect it with **T3 Code**.
- Budget route: get a free old laptop or desktop from friends or family with **at least 8 GB RAM and 4+ cores**; Facebook Marketplace works too.
- Proof of concept: his server **Alvin** has **32 cores**, was running ~6 threads and showed about **0%** in `btop`. Typical agent work uses 1 to 2 threads and **60 to 80 watts**.
- A GMKtec mini PC he recommended in a tweet sold out and rose in price.

> 🗣️ **Speaker Opinion:** Avoid Macs for parallel agent work. Theo blames macOS's file system and security policy for bottlenecks, and says a Linux box will feel better immediately. This is his experience, not a benchmark.

> 🗣️ **Speaker Opinion:** Cloud VPSs are a poor choice here: a Hetzner box with 32 GB RAM and 16 threads is about **$275/month**, versus roughly **$700** for owned hardware (32 GB RAM, 1 TB drive), which pays for itself in about 2.5 months, and server IPs risk bans. Delivered sarcastically; the figures are his.

### Handling resource limits

> 💡 **Tip:** If agents run CI locally (e.g. a Rust project saturating all cores), move CI to GitHub, to **Blacksmith** or **Depot**, to another server, or add a queue so builds run one after another. Maria switched to the **Blacksmith CLI** so CI ran off her RAM-constrained machine.

> 🗣️ **Speaker Opinion:** He deliberately does not list every solution, because your constraints will differ from his. The fun, he says, is this new class of problems: tuning CI triggers, core usage and running the same task several times on one box.

Closing sentiment in this section: he finds engineering the most fun it has ever been because he fires off threads and goes to dinner, skates or queues for a game, then checks a couple from his phone. He quotes Maria (“remote work is the best”) after she set up a Linux box.

## 10. Closing

- Go start threads, spin up more accounts if useful, and burn tokens “before the subsidization ends, if it ever does”.
- He invites PRs to T3 Code (“we'll probably ignore them, but we might merge them”).
- Offers a future video on how subsidization plays out long-term.

## Appendix A: Caption Corrections

Corrections applied to the auto-generated captions. Items marked **[?]** are uncertain and were left flagged rather than guessed.

| Caption / heard | Restored | Confidence |
|---|---|---|
| Claw accounts | Claude accounts | Certain |
| cloud code / Cloud (the product) | Claude Code / Claude | Certain |
| codeex / codecs | Codex | Certain |
| Glass Wing | Project Glasswing | Certain |
| Mythos preview | Claude Mythos Preview | Certain |
| Fable 51 / Opus 55 | Fable 5.1 / Opus 5.5 | Certain |
| CLI proxy / CLI Proxy API | CLIProxyAPI | Likely |
| vibe proxy | VibeProxy | Likely |
| tail scale / tails scale | Tailscale | Certain |
| tailet | tailnet | Certain |
| tailet 318 is the default | Default proxy port, unclear [?]. Left unspecified in the summary. | [?] |
| Micro.ts.net | A `*.ts.net` Tailscale hostname [?] | [?] |
| management html page | management.html | Likely |
| RGFD | `rg`, `fd` [?] (ripgrep, fd) | [?] |
| t-mxb | tmux | Certain |
| web saga | WebSocket [?] | [?] |
| Astra | Unclear [?]; used for an OpenAI model in the Codex context. Avoided in the summary. | [?] |
| Soul | Unclear [?]; “cheaper models like Soul”. Avoided in the summary. | [?] |
| Tibo / T-Mo | Tibo (Codex-related OpenAI figure) [?]; “T-Mo” likely the same person | [?] |
| Grock 47 | Grok 4.7 [?] | [?] |
| Leo from the future | Theo from the future | Likely |
| JSE thinks this | Unintelligible [?]; omitted | [?] |
| HNER | Hetzner | Certain |
| BTOP | btop | Certain |
| Buntu / Ubuntu | Ubuntu | Certain |
| GMK tech | GMKtec [?] | [?] |
| you shin | you SSH in | Certain |
| Curser / Open code / T3 chat | Cursor / OpenCode / T3 Chat | Likely |
| tople guide | top-level guide | Likely |
| $1,000 for every 50,000 of tokens | As spoken; likely means $1,000 spent per $50,000 of tokens used [?] | [?] |
| d-tail scale built in | Unclear [?]; likely built-in Tailscale support | [?] |
| Dan | Unknown person; left as spoken [?] | [?] |
| poll request | pull request | Certain |

## Appendix B: Editorial Notes

- **Ordering:** the transcript has no timestamps or chapter markers, so sections follow the order of the narration. “Part 3b” (T3 Code workflow) is split from Part 3 for scanning; Theo moves between them fluidly.
- **Callout classification:** claims about margins, internal provider deals, other companies' practices, and competitor products are classified as 🗣️ Speaker Opinion because they are inference, rumor or interested-party comment. Operational constraints he states as fixed (data-sharing setting, no public traffic on subscriptions, Claude subs only in Claude Code) are 📏 General Rule or ⚠️ Caution.
- **Arithmetic judgment call:** Theo first says 80 to 85% of tokens go to verification, then corrects to 85 to 90%; the summary uses 85 to 90% (consistent with his 10 to 15% coding figure).
- **Ambiguous limit math:** the “40% of 7-day Fable” and “20% of full 7-day” statements are kept as spoken without reconciliation.
- **Unverified:** pricing, margins, subsidy ratios, reset counts and ban claims are the speaker's own and were not independently checked. The sponsor segment is marked as such.
- **Third parties:** Maria, Julius, Steven and Jeff appear as first names only and are left as spoken.
