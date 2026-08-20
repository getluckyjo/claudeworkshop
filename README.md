# Entrepreneur Coach

**Get set up with Claude, properly.** Built for the Entrepreneur Coach workshop
cohort — Saturday 22 August 2026, CHIPS, 21 Roodehek Street, Gardens.

No terminal. No coding. It all happens in the Claude app.

Most people leave an AI workshop impressed and then do nothing on Monday. The
gap isn't motivation, it's setup. This closes it.

By the end you'll have a Project that knows your business, your real data
connected, one real thing built — a model, a deck, a dashboard, a site, whatever
is actually useful to you — a skill that repeats how you work, and one job
running on a schedule without you.

**Workshop cohort:** installing this is part of your pre-work, and we run the
session together on the day — three hours. **On your own:** allow about
45 minutes and take it one stop at a time. You can stop anywhere and come back.

---

## Three steps

Do this on a laptop, not your phone.

### 1. Download the skill

**[⬇ Download entrepreneurcoach.zip](https://github.com/getluckyjo/claudeworkshop/raw/HEAD/dist/entrepreneurcoach.zip)**

One click. It lands in your **Downloads** folder.

> ⚠️ **Don't open or unzip it.** Leave it exactly as it is — Claude wants the zip
> file itself. If your Mac unzipped it automatically and you now have a *folder*
> called `entrepreneurcoach`, ignore that folder and use the `.zip` file
> next to it.

### 2. Add it to Claude

1. Go to **[claude.ai](https://claude.ai)** and sign in
2. Click your **name or initials** in the bottom-left corner
3. Click **Settings**
4. Click **Customize** in the menu
5. Find the **Skills** section
6. Click the button to add or upload a skill
7. Choose **entrepreneurcoach.zip** from your Downloads folder

You'll know it worked when **Entrepreneur Coach** appears in your list of skills.

### 3. Ask Claude to start

Open a **new chat** — not this one — and type:

> **Help me get set up**

That's it. Claude takes it from there. It asks about your business first, then
does the work. You'll click "Approve" in a pop-up now and then, and answer some
questions. Nothing else.

*Nothing happening?* Type `/entrepreneurcoach` instead — that starts it directly.

---

## What happens

Seven stops, one at a time. You can stop anywhere and pick it up later — Claude
keeps track.

| | | |
|---|---|---|
| **0** | What are you building | Two questions. Everything after this is about your actual business. |
| **1** | Switch on your tools | Your real inbox, calendar or accounts. Claude stops being clever and starts being useful. |
| **2** | Teach Claude your business | How you work and how you write, captured once. Then it just knows. |
| **3** | Ship something real | A model, a deck, a dashboard, a pitch site, a small tool — your call. Real, and you change it by asking. **This is the one.** |
| **4** | Build the business brain | A Project holding your documents, numbers and standards, so nothing gets lost in a chat. |
| **5** | Make it repeat | One job running on a schedule. The first thing that happens without you. |
| **6** | Your first week | Three specific things to try, and one you'll actually do by Friday. |

Stuck on one? Skip it and come back. Stop 2 needs nothing but a conversation and
is worth the whole session on its own.

---

## What you need

- A Claude account (Pro or Max)
- The Claude desktop app, or a browser
- One real, messy file from your business — not a tidy example

That's the list. You don't need GitHub, you don't need to know what a terminal
is, and there's nothing to install beyond the app itself.

**On cost:** what you build can be published free either way, and Claude explains
the trade-off before you choose. The quickest route needs no account at all. If
you go the Vercel route for a customer-facing site, the free tier is aimed at
personal projects, so a commercial site may need a paid plan eventually — Claude
tells you that up front rather than after you've sent the link around.

---

## A word on safety

Claude will ask to connect real things — your email, your calendar. Worth
knowing before you say yes:

- Claude **reads** freely, but **asks before it sends, changes or deletes**
  anything
- You can switch any connection off in seconds, from the same screen you added it
- **Nobody should ever ask you to paste a password or an API key into a chat.**
  Everything here is proper browser sign-in. If something asks you for a secret,
  stop and ask me.

---

## Something not working?

Tell Claude what happened — it can fix most of it, and it's got proper
troubleshooting notes built in.

Still stuck? [Open an issue](https://github.com/getluckyjo/claudeworkshop/issues)
on this repo, or grab me on the day.

---

## For the curious

```
claudeworkshop/
├── dist/entrepreneurcoach.zip          what you download
├── skills/entrepreneurcoach/           what's inside it
│   ├── SKILL.md                the flow
│   └── references/             detailed notes for each stop
│       ├── connectors.md       stop 1 — Google, Microsoft, Xero
│       ├── your-skill.md       stop 2 — process and voice skills
│       ├── ship.md             stop 3 — files and links
│       ├── project.md          stop 4 — the business brain
│       ├── schedule.md         stop 5 — recurring jobs
│       └── troubleshooting.md  when something breaks
├── scripts/package-skill.sh    rebuilds the zip after edits
└── docs/workshop-runsheet.md   facilitator notes
```

It's all plain text. Open it, read it, change it — it's yours. If you edit
anything under `skills/`, run `./scripts/package-skill.sh` to rebuild the zip.

---

Built for the cohort. Take it, fork it, make it yours.

**Johannes Le Roux**
[entrepreneurcoach.co.za](https://www.entrepreneurcoach.co.za/workshop)

MIT licensed.
