# Station 4 — Build the business brain

**Layer 1 is a sold deliverable.** The workshop page promises "a Project that
knows your business" as the first thing they walk out with. Treat it as a
headline outcome with real time against it, not a two-minute tidy-up at the end.
Layer 2 — GitHub — is the optional half.

## The mental model to teach

Beginners lose work because nobody explains where things live. Give them this
frame once — it's four lines and it does a lot of work:

| | What it remembers | Set up in |
|---|---|---|
| **Your skill** (Station 2) | Who *you* are — your business, your voice | Once, forever |
| **A Project** | Everything about *one piece of work* — brand, docs, decisions | 2 minutes |
| **GitHub** | The work itself, every version of it | 5 minutes |
| **Vercel** | Keeping it live, updating when the work changes | Already done in Station 3 |

The line that lands: **a chat is disposable, a project is not.** Anything they
care about should live somewhere that outlives the conversation.

## Layer 1 — A Claude Project (everyone does this, properly)

Lowest friction thing in the entire flow, and most people have never opened the
menu. It's also the one that makes every future session shorter.

A Project is a container for related chats that carries its own knowledge and
instructions. Every conversation started inside it begins already knowing the
context — no re-explaining, no re-uploading the logo.

**Do it now, with them:**

1. Click **Projects** in the sidebar → **New project**
2. Name it after the actual thing — "Hole in One Challenge", not "Work"
3. Load it with real substance, not just branding:
   - **Their documents** — pricing, service list, standard terms, contracts,
     the messy real file they were asked to bring
   - **Their numbers** — last year's figures, the current model, whatever they'd
     have to re-explain otherwise
   - **Their standards** — what good looks like, what they'd reject, house style
   - **Brand assets** from Station 3 — logo, photos, colours, deck
4. Set the project instructions — a few lines on what this project is for and how
   Claude should behave inside it

**Push on step 3.** Most people add a logo and stop, and then wonder why the
Project doesn't feel like much. The difference between a folder and a business
brain is whether the real documents went in. They brought a messy file for
exactly this reason — put it in.

Then start a chat inside it and ask it something only their business would know.
That's the proof, and it's worth doing out loud.

**Why it matters commercially:** everything they've built today is stuck in one
conversation. Put it in a Project and every future piece of work — next pitch
site, next dashboard, next proposal, next month-end — starts already knowing the
business.

## Layer 2 — The build loop (anyone who shipped in Station 3)

Only worth doing if they built something in Station 3 that they'll want to change
again. Read the room — if they made a one-pager they'll touch twice a year, Layer
1 is enough.

For anything they'll keep working on, this is the loop that actually holds up:

**Claude Code on the web → GitHub → Vercel**

- **[claude.ai/code](https://claude.ai/code)** — Claude works on the project in
  the cloud. No terminal, no installing, nothing on their laptop. Sessions
  persist, and they can check on them from the Claude mobile app.
- **GitHub** — every version of the work, kept. Claude works on a branch and
  opens a pull request; they review and merge.
- **Vercel** — connected to the repo, so a merge redeploys the live site
  automatically.

Once it's wired, the whole loop is: *ask for a change → review it → merge → the
live site updates.* No commands, ever.

**Setting it up:**

1. Go to [claude.ai/code](https://claude.ai/code) and sign in with their Claude
   account — the same one they're already using
2. Connect GitHub when prompted. This authorises the Claude GitHub App. If they
   don't have an account: [github.com/signup](https://github.com/signup), free
   plan, and a **personal** username rather than a company one — they'll have
   more than one business
3. Push the Station 3 project into a repo
4. In Vercel, import that repo so future merges deploy automatically

Needs Pro, Max or Team. Claude Code on the web is a research preview, so say that
rather than presenting it as bulletproof.

## Read the room

Layer 1 is for everyone, and it's what was sold. Don't shortcut it.

**Layer 2 is genuinely optional on day one.** They've just put their business on
the internet; that's a good day. GitHub is the highest-friction thing in this
flow and pushing it can turn a great session into a confusing one. Offer it in
one line and let them decline cleanly:

> There's one more layer — it keeps every version of this and updates the live
> site whenever you change something. Worth doing now, or park it?

Both answers are fine. Note it and move to Station 5.

## What not to say

Skip branches, commits, merges and pull requests as concepts. If they ask, one
sentence, then move on. They don't need to understand git to benefit from it —
the loop above works whether or not they can define a commit.

## Snags

**They're looking for a GitHub connector**
There isn't one in the connector directory. Use claude.ai/code.

**GitHub signup demands two-factor**
Required, and a good thing — this account will hold everything they build. Walk
them through it with an authenticator app or SMS.

**Claude Code on the web won't see their repo**
The connected GitHub account needs access to it. Check they authorised the right
account — easy to get wrong if they have a personal and a work login.

**Project knowledge isn't being used**
Check they started the chat *inside* the project rather than in a normal chat.
Very common, and it looks like the feature is broken.

**They're overwhelmed**
Stop at Layer 1. A Project with their brand in it is a real win and takes two
minutes. Layer 2 will keep.
