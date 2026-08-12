# Station 3 — Vercel

## The pitch

This is the station that lands. Everything before it was plumbing — this is the
part where they get a link they can send to a customer today.

Say it plainly: **"By the end of this station you'll have a live web address for
your business, and you'll be able to change it by asking me."**

## Step 1 — Account

https://vercel.com/signup — **sign up with GitHub**. Not email. Not Google.

This matters and is worth one sentence of explanation: signing up with GitHub is
what makes deploys automatic. Push a change, the site updates. Sign up with
email and they'll be stuck wiring it together manually later.

Hobby plan is free and is genuinely enough for what most of the cohort needs.

## Step 2 — Connect the Vercel MCP server

Ships with this plugin. Verify:

```bash
claude mcp list
```

If `vercel` is listed but unauthenticated:

> Run `/mcp`, pick **vercel**, approve in the browser.

If it isn't listed:

```bash
claude mcp add --transport http vercel https://mcp.vercel.com
```

Then `/mcp` to authenticate.

## Step 3 — Ship something

Two paths. Pick based on what they told you in Station 0.

### Path A — they already have a project

Deploy what they have. Push to GitHub first (Station 2), then import the repo
into Vercel. The Vercel MCP tools can do most of this; fall back to
https://vercel.com/new if the tooling stalls.

### Path B — they have nothing yet (most of the cohort)

**Build them something real, right now.** Not a demo. A one-page site for their
actual business, using their Station 0 answer — what they do, who it's for, how
to contact them.

Keep it to a single `index.html` with inline CSS. No framework, no build step,
no `npm install`. It deploys in seconds and it never breaks in a live room.

Make it genuinely good-looking — this is the artifact they show people. Then:

```bash
npx vercel --yes
```

First run will ask them to log in — browser opens, they approve, done.

Ask before you buy or claim a domain, and never run a paid action without their
explicit go-ahead. The free `.vercel.app` URL is the right default for today.

## Step 4 — The moment

Give them the URL. Then say something like:

> That's live on the internet right now. Send it to someone.

Then prove the loop works — ask them for one change (headline, colour, phone
number), make it, redeploy, and have them refresh. **This is the single most
important thirty seconds of the whole onboarding.** It's when "AI helps me code"
becomes "I can change my own website by asking."

## Step 5 — Wire up auto-deploy

If the project is on GitHub and imported into Vercel, every push now redeploys
automatically. Tell them that in one sentence. Don't explain CI/CD.

## Common snags

**Build fails on a framework project**
Read the build log — `get_deployment_build_logs` via the Vercel MCP tools, or
the dashboard. Usually a missing dependency or a wrong build command. Fix it
yourself and redeploy; don't narrate the debugging.

**"No Output Directory named 'public' found"**
Static project without config. Either move files into `public/`, or set the
output directory to the project root in Vercel's settings.

**Deployed but showing a 404**
Their entry file isn't `index.html`, or it's inside a subfolder. Check what's
actually at the repo root.

**Wrong Vercel account / team**
`npx vercel logout` then log in again with the right account. Check
`list_teams` if they're in more than one.

**They want a custom domain**
Great instinct, and it's a real moment — but it costs money and involves DNS.
Note it in the progress file as a follow-up rather than doing it live in the
workshop, unless there's time and they're keen.
