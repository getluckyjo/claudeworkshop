# Station 3 — Put something live

The station that lands. Everything else is useful; this one is the moment they
tell people about.

Say it plainly up front:

> In the next few minutes you'll have a real web address for your business, and
> you'll be able to change it just by asking me.

## Two ways to do it

### Option A — Deploy to Vercel (do this one)

The Vercel connector can **deploy files directly** — no GitHub, no git, no
command line, nothing installed. You write the site, you ship it, they get a
real URL.

Tool: `deploy_to_vercel`. Pass the file tree, a project name, and
`target: "production"` to go live.

They'll need a free Vercel account and the connector switched on:
**Settings → Connectors → Vercel → Connect** (sign in with email or GitHub —
whichever they find easier; email is fine).

Preview vs production:
- `target: "preview"` — a shareable link, good for a first look
- `target: "production"` — the real one. Use this for the URL they'll actually
  send to people.

### Option B — An Artifact (fallback, or for something scrappy)

If Vercel signup is stalling, or they just want to see something fast, build it
as an artifact and publish it. They click **Share** on the artifact and get a
public link — no account, no connector, nothing to sign up for.

It's a genuinely good fallback that keeps the momentum. It's not a business
website — no custom domain — but it proves the loop and they leave with a link.

**Don't let a Vercel signup problem cost them the moment.** Artifact first, move
Vercel to homework if you have to.

## Build them something real

Not a demo. Not lorem ipsum. A one-page site for their actual business using
their Station 0 answer.

- Their real name, real offer, real contact details
- **Mobile first** — most of their customers will open it on a phone
- One clear call to action: call, WhatsApp, book, buy
- Genuinely good-looking. This is the thing they show people; a link they're
  embarrassed by is worse than no link.
- Plain HTML with inline CSS. No framework, no build step, nothing that can
  break in a live room.

If they don't know what they want, don't run a discovery session. Offer three
concrete options, let them pick, and build it. You can change anything in thirty
seconds once it's live — that's a much better way to find out what they want.

## Then change something

**Do not skip this.**

Ask them for one change — headline, colour, phone number. Make it. Redeploy.
Have them refresh.

This is the whole lesson. It's the moment shipping stops being something other
people do. Give it the airtime it deserves.

## Hand it over properly

Give them the URL and tell them to send it to someone **right now**, while
you're both still here. Not later. Later never happens.

Then note the URL in their progress summary so they can find it again.

## Snags

**Vercel connector not showing up**
Settings → Connectors → find Vercel → Connect. If it's connected but the tools
aren't available in this chat, it's toggled off for the conversation — they can
enable it in the chat's connector settings.

**Vercel sign-up asking about teams or plans**
Personal account, Hobby plan, free. That's all they need. Skip anything that
asks for a card.

**Deployment succeeded but the page looks wrong**
Check the entry file is `index.html` at the root of the file tree you sent.

**They want their own domain name**
Good instinct — it's a real step up. But it costs money and involves DNS, so get
an explicit yes first, and consider parking it as homework rather than burning
workshop time on it.

**The URL asks people to log in**
The deployment has protection enabled. Deploy to `production`, or use
`get_access_to_vercel_url` for a temporary shareable link while you sort it out.
