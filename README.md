# Launchpad

**Claude tooling for founders.** Built for the Entrepreneur Coach workshop cohort — 22 August.

Most people leave an AI workshop impressed and then do nothing on Monday. The gap
isn't motivation, it's setup. This closes that gap.

Run one command and Claude walks you through the whole thing: GitHub connected,
Vercel deploying, your connectors switched on, your first live URL, and a
personal skill that teaches Claude your business so you never explain it again.

Takes about 30 minutes. You don't need to be technical.

---

## Get started

Open your terminal, and run:

```
/plugin marketplace add getluckyjo/claudeworkshop
/plugin install launchpad@entrepreneur-coach
```

If it tells you to run `/reload-plugins`, do that. Then:

```
/launchpad:onboard
```

That's it. Claude takes it from there — it asks about your business first, then
does the setup work itself. You'll be clicking "Approve" in a browser now and
then, not typing commands you don't understand.

**Don't have Claude Code yet?** Install it first:

```bash
npm install -g @anthropic-ai/claude-code
```

No Node on your machine? Grab it from [nodejs.org](https://nodejs.org) (take the
LTS version), then run the line above.

---

## What you get

**`/launchpad:onboard`** — the guided setup. Six stations, one at a time, and you
can stop and pick up where you left off. It keeps track for you.

**`/launchpad:ship`** — idea to a live web address, in one session. Use it on the
day, use it every time after.

**`/launchpad:my-voice`** — a short interview about your business and how you
write, and it builds you a permanent skill file. After this, Claude knows what
you sell, who buys it, and how you talk. Every session, forever.

---

## The six stations

| | | |
|---|---|---|
| **0** | What are you building | Two questions. Everything after this is tailored to your actual business. |
| **1** | Ground control | Thirty seconds of checks so nothing bites you later. |
| **2** | GitHub | Where your work lives. Backup that thinks, and the plug everything else uses. |
| **3** | Vercel | A live link you can send to a customer today. This is the one that lands. |
| **4** | Connectors | Your real inbox, your real calendar. Claude stops being clever and starts being useful. |
| **5** | Your own skill | Stop re-explaining your business every session. |
| **6** | First mission | Three specific things to try this week, written for your business. |

Stuck on a station? Skip it and come back. Station 5 needs nothing external and
is worth doing on its own.

---

## In the browser instead of the terminal?

Plugins are a Claude Code thing. If you're working on claude.ai or in the Claude
desktop app, you can still take the best part with you — package a skill as a zip
and upload it:

```bash
./scripts/package-skills.sh
```

Then go to **claude.ai → Settings → Capabilities → Skills** and upload the zip
you want. Your connectors get set up in **Settings → Connectors** — no terminal
needed at all.

---

## What's actually in here

```
claudeworkshop/
├── .claude-plugin/marketplace.json     the catalogue
├── plugins/launchpad/
│   ├── .claude-plugin/plugin.json
│   ├── .mcp.json                       GitHub + Vercel, pre-wired
│   └── skills/
│       ├── onboard/                    the six-station flow
│       ├── ship/                       idea to live URL
│       └── my-voice/                   builds your personal skill
├── scripts/package-skills.sh           zip skills for claude.ai
└── docs/workshop-runsheet.md           facilitator notes
```

Installing the plugin also wires up the GitHub and Vercel MCP servers for you.
You'll authenticate them with `/mcp` — a browser window, one click, no tokens to
copy and paste anywhere.

---

## A word on safety

The onboarding will ask you to connect real things — your GitHub, your email,
your calendar. Worth knowing:

- Claude reads freely, but **asks before it sends, changes or deletes anything**
- You can revoke any connector in seconds, from the same screen you added it
- **Never paste an API key or token into a file in a repo.** Everything here uses
  browser sign-in instead. If something ever asks you to paste a secret, stop and
  ask.

---

## Something broken?

Claude can fix most of it — tell it what went wrong and it'll sort it out. There
are proper troubleshooting notes in
`plugins/launchpad/skills/onboard/references/troubleshooting.md`.

Still stuck? Open an issue on this repo, or grab me on the day.

---

Built for the cohort. Take it, fork it, make it yours.

**Johannes Le Roux**
[entrepreneurcoach.co.za](https://www.entrepreneurcoach.co.za/workshop)

MIT licensed.
