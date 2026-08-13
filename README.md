# Claude for Entrepreneurs

**Get set up with Claude, properly, in about half an hour.** Built for the
Entrepreneur Coach workshop cohort — 22 August.

No terminal. No coding. No installing anything. It all happens in your browser.

Most people leave an AI workshop impressed and then do nothing on Monday. The
gap isn't motivation, it's setup. This closes it.

By the end you'll have your email and calendar connected, something real live on
the internet that you can change just by asking — a pitch site, a dashboard, a
one-pager, whatever's actually useful to you — and Claude permanently taught
about your business so you never explain it twice.

---

## Three steps

Do this on a laptop, not your phone.

### 1. Download the skill

**[⬇ Download claudeforentrepreneurs.zip](https://github.com/getluckyjo/claudeworkshop/raw/HEAD/dist/claudeforentrepreneurs.zip)**

One click. It lands in your **Downloads** folder.

> ⚠️ **Don't open or unzip it.** Leave it exactly as it is — Claude wants the zip
> file itself. If your Mac unzipped it automatically and you now have a *folder*
> called `claudeforentrepreneurs`, ignore that folder and use the `.zip` file
> next to it.

### 2. Add it to Claude

1. Go to **[claude.ai](https://claude.ai)** and sign in
2. Click your **name or initials** in the bottom-left corner
3. Click **Settings**
4. Click **Customize** in the menu
5. Find the **Skills** section
6. Click the button to add or upload a skill
7. Choose **claudeforentrepreneurs.zip** from your Downloads folder

You'll know it worked when **Claude for Entrepreneurs** appears in your list of skills.

### 3. Ask Claude to start

Open a **new chat** — not this one — and type:

> **Help me get set up**

That's it. Claude takes it from there. It asks about your business first, then
does the work. You'll click "Approve" in a pop-up now and then, and answer some
questions. Nothing else.

*Nothing happening?* Type `/claudeforentrepreneurs` instead — that starts it directly.

---

## What happens

Six stops, one at a time. You can stop anywhere and pick it up later — Claude
keeps track.

| | | |
|---|---|---|
| **0** | What are you building | Two questions. Everything after this is about your actual business. |
| **1** | Switch on your tools | Your real inbox and calendar. Claude stops being clever and starts being useful. |
| **2** | Teach Claude your business | It learns what you sell and how you write. Once. Forever. |
| **3** | Ship something real | A one-pager, a pitch site, a dashboard or a small tool — your call. Live on the internet, and you change it by asking. **This is the one.** |
| **4** | Set up your project | Where your brand and your work live, so nothing gets lost in a chat. |
| **5** | Your first week | Three specific things to try, written for your business. |

Stuck on one? Skip it and come back. Stop 2 needs nothing but a conversation and
is worth the whole session on its own.

---

## What you need

- A Claude account (Pro or Max)
- A browser
- About 30 minutes

That's the list. You don't need GitHub, you don't need to know what a terminal
is, and you won't be asked to install anything.

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
├── dist/claudeforentrepreneurs.zip          what you download
├── skills/claudeforentrepreneurs/           what's inside it
│   ├── SKILL.md                the flow
│   └── references/             detailed notes for each stop
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
