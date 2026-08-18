# Station 1 — Switch on your tools

## The pitch

Up to now Claude has been a clever assistant with no idea what's going on in
their business. Connectors change that — real inbox, real calendar, real
documents.

Say the trade honestly and early:

> This gives me access to your actual email and calendar. You pick which ones,
> you can switch them off any time, and I'll always ask before I send or change
> anything.

Founders are rightly careful about this. Being straight earns the yes.
Overselling earns a no.

## How they add one

**Settings → Connectors → browse the list → Connect → approve in the pop-up.**

That's it. Pure clicking. Walk them through it one click at a time and wait for
them to confirm before moving on — don't narrate all four steps at once.

If a connector is connected but its tools aren't available in the conversation,
it's toggled off for that chat. They can enable it in the chat's connector
settings.

## Pick one. Just one.

Match it to what they said in Station 0. Prove it works. *Then* offer more.

| They said | Start with | Demo it with |
|---|---|---|
| Admin and email are eating my week | **Gmail** | Who emailed this week and hasn't had a reply |
| I'm drowning in meetings | **Google Calendar** | Where the free 90-minute blocks are next week |
| Our documents are chaos | **Google Drive** | Find and summarise the latest version of a real doc |
| We're a Microsoft shop, not Google | **Microsoft 365** | Same demos — one connector covers Outlook mail, calendar, OneDrive/SharePoint and Teams |
| I need to stay on top of the numbers | **Xero** | Cash position, and who owes them money |
| I want to actually email my list | **Resend** | Draft a broadcast to their contacts |

Note: **there is no GitHub connector** in the directory. GitHub is Station 4 and
works differently — don't send them hunting for it here.

## If they're on Microsoft, not Google

Ask "Google or Microsoft?" *before* the station, not during it. The clicks are
identical up to which card they pick, so you can run both halves of a room
together.

One connector — **Microsoft 365** — covers Outlook mail, Outlook calendar,
OneDrive/SharePoint and Teams. It's on every plan including Free, so nobody is
blocked by billing. Two things will trip you up:

1. **It needs a Microsoft *business* tenant.** Personal accounts —
   `@outlook.com`, `@hotmail.com`, `@live.com` — don't work at all, and plenty
   of small businesses run on one with a custom domain bolted on without knowing
   the difference. No amount of clicking fixes it. Pivot to Drive, Xero, or
   straight to Station 2.
2. **Write tools are admin-gated.** Reading mail and calendar works on connect.
   Drafting, sending and creating events only work if the tenant admin has
   switched write tools on. In a five-person business the founder usually is the
   admin. In anyone who's ever hired an IT company, they are not — and that
   person is not answering their phone during a workshop.

Neither blocks the station. **The read-only demo is the one that lands anyway** —
"who emailed this week and hasn't had a reply" needs no write access. If they hit
an admin wall, note it as homework and keep moving.

Test one Microsoft account yourself the week before. Consent flows vary by
tenant and you don't want to meet that live.

## The demo is the point

**Connecting a tool is not the win. Watching it do something real is the win.**

Do not stop at "Gmail is connected ✅". Immediately run one genuinely useful
request against their real data and show them the output. That's the moment they
understand what they've switched on.

Good demos are specific and about *their* business:

- "Who emailed me this week that I haven't replied to?"
- "What does my Thursday actually look like?"
- "Find the last invoice we sent to [their biggest customer]"

Bad demo: "Summarise my emails." Vague, and the result won't impress anyone.

## Say these out loud

1. **Reading is free, doing gets asked about.** Claude reads without fuss, but
   asks before sending an email, moving a meeting or changing a document.
2. **They can revoke any connector in seconds**, from the same screen.
3. **It's their access, not shared.** Connecting Gmail doesn't expose their inbox
   to anyone else in the cohort.
4. **A word on dodgy emails.** If Claude is reading an inbox, a message from a
   stranger could contain text aimed at Claude rather than at them. Claude treats
   email as information, not instructions, and checks before acting on anything
   unexpected. Thirty seconds well spent — most people have never thought about
   it.

## Snags

**Connected but no tools in the chat**
Toggled off for this conversation. Enable it in the chat's connector settings.

**Pop-up opens and hangs**
Pop-up blocker, or they're signed into a different account in that browser. An
incognito window signed into the right account usually sorts it.

**Wrong Google account**
Very common when someone has personal and business Gmail. Disconnect, sign out
of Google in that browser, reconnect with the business account.

**Microsoft 365 won't connect at all**
Almost always a personal Microsoft account rather than a business tenant. Not
fixable in the room — switch them to another connector and move on.

**Microsoft 365 connects but won't draft or send**
Write tools are off at the tenant. Their IT admin turns them on. Do the
read-only demo, note it as homework.

**They're nervous about access**
Completely reasonable. Start with Calendar instead of Gmail — lower stakes, still
a good demo. Trust builds fast once they've seen it work.
