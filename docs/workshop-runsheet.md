# Workshop runsheet — 22 August

Facilitator notes. Not for the cohort.

## The night before

- [ ] Repo is public. Test the install from a clean machine or a fresh session:
      `/plugin marketplace add getluckyjo/claudeworkshop`
- [ ] Run `/launchpad:onboard` end to end yourself. Every station.
- [ ] Have the two install lines on a slide, big. People will be typing them.
- [ ] Ask people to install Claude Code **before** they arrive. This is the
      single biggest time sink on the day.

## Pre-workshop message to the cohort

> Before Friday, please install Claude Code — it takes 5 minutes:
>
> 1. Install Node from nodejs.org (take the LTS version)
> 2. Open your terminal and run: `npm install -g @anthropic-ai/claude-code`
> 3. Run `claude` and sign in
>
> If you get stuck, don't stress — we'll sort it on the day. Just try first so we
> can spend the time building instead of installing.
>
> Also worth doing: create a GitHub account at github.com/signup if you don't
> have one.

## Timing (90 minutes)

| Time | What |
|---|---|
| 0:00 | Why this matters. Show a live URL you built in five minutes. Don't explain, demonstrate. |
| 0:10 | Everyone installs the plugin. Fix stragglers while the room works. |
| 0:20 | `/launchpad:onboard` — Stations 0 and 1. Everyone at the same place. |
| 0:30 | Station 2 — GitHub. Expect this to be the slowest one. |
| 0:45 | **Station 3 — Vercel.** The big moment. Everyone gets a live URL. Do a round of the room and have people read theirs out. |
| 1:05 | Station 4 — Connectors. Demo on your own real inbox first. |
| 1:15 | Station 5 — their own skill. This is the one they'll thank you for. |
| 1:25 | Station 6 — first mission. Send them out with three specific things. |

## What will actually go wrong

**Node/npm not installed.** The number one blocker. Have the nodejs.org link
ready and expect 2–3 people.

**Corporate laptops.** Locked-down machines block OAuth callbacks to localhost.
Fallback: move them to claude.ai in the browser and do connectors + skills there.
They still get real value. Don't let one laptop eat the room.

**Everyone hits GitHub auth at once.** Consider walking the room through GitHub
signup as a group before turning them loose, rather than 12 people getting stuck
individually.

**Someone races ahead.** Give them `/launchpad:ship` and let them build a second
thing. They become your floor assistant.

**Someone falls behind.** The progress file is the safety net. Get them to
Station 3 (live URL) at minimum — that's the one that makes the day worth it.

## The one thing that matters

If people leave with nothing else, they should leave with **a live URL they
changed themselves.** That's the moment the whole thing clicks. Protect the time
for Station 3 even if you have to cut Station 4 short.

## After the workshop

- [ ] Send the repo link again — most people won't have bookmarked it
- [ ] Ask for the URLs they shipped. Great social proof for the next cohort.
- [ ] Note what broke and fix it in the repo before the next one runs
