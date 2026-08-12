---
name: ship
description: "Take a founder's idea from nothing to a live public URL in one session — build it, push it to GitHub, deploy it to Vercel, and hand back a link they can send to a customer. Use when someone wants to put something online, build a landing page or simple web tool for their business, deploy or redeploy a site, get a live link, or says they want to ship something. Also use for updating and redeploying something they already shipped. Runs as Station 3 of launchpad onboarding, or standalone any time after."
license: MIT
---

# Ship It

From idea to a link they can send someone. One session.

This is the skill the cohort will keep using long after the workshop, so make it
feel repeatable and unremarkable — the goal is that shipping stops feeling like
an event.

## Ground rules

**Simplest thing that works.** A single `index.html` with inline CSS deploys in
seconds, never breaks, and looks the same on every machine. Reach for a
framework only when they genuinely need one — a real app with data or accounts.
For a landing page, a menu, a booking form, a price list, a portfolio: plain
HTML wins every time.

**Ship early, polish live.** Get something on the internet in the first five
minutes, even if it's rough. Then iterate with them watching. The redeploy loop
is the thing you're actually teaching.

**Never spend money without asking.** Custom domains, paid plans, add-ons — all
need an explicit yes first. The free `.vercel.app` URL is the default.

## The flow

### 1. What are we shipping? (2 minutes, not 20)

One question: **what do you want the link to do?**

If they're vague, offer three concrete options based on their business and let
them pick. Don't run a discovery workshop — you can change anything in thirty
seconds once it's live, and that's a much better way to find out what they want.

Check `~/.claude/launchpad-progress.md` for business context so you're not
starting cold.

### 2. Build it

Make it good. This is the thing they show people — a link they're embarrassed by
is worse than no link.

- Real copy about their real business, not lorem ipsum
- Their actual contact details, actual prices, actual name
- Mobile-first. Most of their customers will open it on a phone.
- One clear call to action — call, WhatsApp, book, buy
- Fast: no external fonts or libraries unless they earn their place

Working folder:
```bash
mkdir -p ~/projects/<name> && cd ~/projects/<name>
```

### 3. Get it online

```bash
npx vercel --yes
```

First run opens a browser to log in. After that it's instant.

If they've done Station 2, put it on GitHub too so pushes auto-deploy:

```bash
git init && git add -A && git commit -m "First commit"
```
Then create the repo via the GitHub MCP tools and push.

### 4. Hand over the link

Give them the URL and tell them to send it to someone right now. Not later —
now, while you're both here.

### 5. Change something, together

**Do not skip this.** Ask for one change — headline, colour, phone number —
make it, redeploy, have them refresh.

This is the whole lesson. It's the moment shipping stops being something other
people do.

### 6. What's next

Two or three specific things they could add, sized to their business. Then stop.

## Coming back to it

When they return to change something:

1. `cd` into the project folder (check the progress file if they've forgotten
   where it is)
2. Make the change
3. `git push` if it's on GitHub — auto-deploys — or `npx vercel --prod` if not
4. Confirm the live URL updated

## Snags

**`npx vercel` asks a pile of setup questions**
`--yes` accepts the defaults. Defaults are almost always right for a static site.

**Deploys but 404s**
Entry file isn't `index.html`, or it's buried in a subfolder. Check the repo
root.

**Wrong Vercel account**
`npx vercel logout`, then log in again.

**They want a custom domain**
Good sign — they're taking it seriously. It costs money and needs DNS, so get an
explicit yes first, and consider parking it as homework rather than doing it
live in a workshop.

**Build fails on a framework project**
Read the actual build log via the Vercel MCP tools before guessing. Fix it and
redeploy — don't narrate the debugging at them.
