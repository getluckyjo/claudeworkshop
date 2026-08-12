# Station 4 — Keep your work safe (optional)

## Read the room first

This station is optional, and for a lot of beginners the right answer on day one
is **no**.

They've just watched their business go live on the internet. That's the win.
GitHub is the highest-friction, least-immediately-useful thing in this flow, and
pushing it can turn a great session into a confusing one.

Offer it in one line. Let them decline without any sense they're missing out:

> There's one more thing worth setting up eventually — somewhere your projects
> live permanently, so they're not stuck in a browser tab. Want to do it now, or
> park it for another day?

Both answers are fine. If they park it, note it and move to Station 5.

## If they say yes

**There is no GitHub connector** in the Claude connector directory. Don't send
them looking for one — that's a dead end and it'll dent their confidence.

The browser route is **Claude Code on the web** at
[claude.ai/code](https://claude.ai/code):

1. They go to claude.ai/code
2. Sign in with their Claude account — same one they're already using
3. Connect GitHub when prompted. If they don't have an account yet:
   [github.com/signup](https://github.com/signup) — free plan, and tell them to
   pick a **personal** username, not a company one. They'll have more than one
   business; `johannesleroux` ages better than `getluckygolf`.
4. From there Claude works on their projects in the cloud. Still no terminal,
   still no installing anything.

## What to actually say it's for

Skip branches, commits and pull requests entirely. Two reasons, both about their
business:

1. **It's a backup that remembers.** Every version of everything, forever. They
   can always get back to the version that worked.
2. **It's the plug other tools use.** Connect it once and things like automatic
   redeploys become possible later.

If they ask what a commit is, answer in one sentence and move on. Don't teach
git to someone who hasn't asked to learn it.

## Snags

**They can't find a GitHub connector**
Because there isn't one. Use claude.ai/code instead.

**GitHub signup wants two-factor auth**
It's required, and it's a good thing — this account will hold everything they
build. Walk them through it with an authenticator app or SMS.

**They already have a GitHub account but can't remember the login**
Password reset on github.com. If it's going to eat five minutes in a workshop,
park it as homework.

**They're overwhelmed**
Back off. Note it in their progress summary and move on. They have a live
website — the session already worked. GitHub will keep.
