# Station 3 — Ship something real

The station that lands. Everything else is useful; this one is what they tell
people about afterwards.

Say it plainly up front:

> In the next few minutes you'll have something real on the internet for your
> business, and you'll be able to change it just by asking me.

## It doesn't have to be a website

This is the mistake to avoid. "Let's build you a landing page" is the obvious
move and it's often the *least* useful thing for the founder in front of you —
plenty of them already have a website they don't need another of.

Ask what would actually be useful, and offer four shapes:

**1. A one-pager** — they need to be found, or take bookings and enquiries.
The right call if they have no web presence, or theirs is embarrassing.

**2. A pitch site** — they're raising, or selling into partners and sponsors.
A link that works on a phone beats a 4MB PDF deck nobody opens. Strong for
anyone mid-raise or chasing sponsorship.

**3. A dashboard** — they need to *see* something: sales, cash, bookings,
pipeline. Often the highest-value option for an established business, and the
one they'd never have thought to ask for.

**4. A small tool** — a quote calculator, a booking form, a pricing estimator,
something their team or customers actually use. Great when they describe a
repetitive job someone does by hand.

Pick from their Station 0 answer. If they said *"I'm chasing sponsors"*, that's a
pitch site. *"I never know where the money is"* — dashboard. Don't run a
discovery session; offer the three that fit, let them choose, build it. You can
change anything in thirty seconds once it exists.

## Which way to ship it

This decision matters, and it comes down to one question: **does it need live
data, or does it need to be public?**

| | Deploy to Vercel | Build as an artifact |
|---|---|---|
| Public link, anyone can open | ✅ | ✅ (once published) |
| Custom domain later | ✅ | ✗ |
| **Reads their live Xero / Gmail / Calendar** | ✗ | ✅ |
| Needs no signup at all | ✗ | ✅ |

**Rule of thumb:** anything the public sees — one-pager, pitch site, tool — goes
to **Vercel**. Anything that shows *their own live numbers* — a dashboard — is
better as an **artifact**, because it can call their connectors and pull real
data. A deployed static site can't reach their Xero.

A dashboard can go to Vercel too, but the numbers have to be baked in at build
time. That's fine for a snapshot they send a sponsor; useless as a thing they
check on Mondays. Be straight with them about which they're getting.

### Deploying to Vercel

`deploy_to_vercel` sends the file tree directly — no GitHub, no git, no command
line, nothing installed. `target: "production"` for the real thing,
`target: "preview"` for a first look.

They'll need a free Vercel account and the connector on: **Settings → Connectors
→ Vercel → Connect.** Email signup is fine and is one less thing to explain.

### Building as an artifact

No account, no connector, nothing to sign up for. They click **Share** to publish
and get a public link. Also the right fallback if a Vercel signup stalls — don't
let a signup form cost them the moment.

## Build it properly

Not a demo. Not lorem ipsum. Their real business, their real numbers, their real
contact details, from Station 0.

- **Mobile first.** Most of the people they send it to will open it on a phone.
- One clear call to action — call, WhatsApp, book, buy, invest.
- Genuinely good-looking. This is what they show people; a link they're
  embarrassed by is worse than no link.
- Plain HTML with inline CSS. No framework, no build step, nothing that can
  break in a live room.

## Then change something

**Do not skip this.**

Ask for one change — a headline, a colour, a number. Make it. Redeploy. Have
them refresh.

This is the whole lesson, and it's the reason they'll come back to Claude on
Monday. Give it the airtime.

## Hand it over

Give them the link and tell them to send it to someone **right now**, while
you're both still here. Later never happens. Note it in their progress summary.

## Snags

**Vercel connector missing**
Settings → Connectors → Vercel → Connect. If it's connected but the tools aren't
available in the conversation, it's toggled off for that chat.

**Vercel signup asking for card details**
They've landed on a paid tier. Personal account, Hobby plan, free.

**Deployed but blank or 404**
Entry file must be `index.html` at the root of the file tree.

**The live URL asks visitors to log in**
Deployment protection. Deploy to `production`, or use `get_access_to_vercel_url`
for a temporary link while sorting it.

**Dashboard shows nothing**
If it's an artifact pulling live data, the viewer needs the relevant connector
switched on — including them. If it's on Vercel, the data was baked in at build
time and won't refresh; rebuild it or move it to an artifact.

**They want a custom domain**
Good instinct, real step up, but it costs money and involves DNS. Get an explicit
yes first, and consider parking it as homework rather than burning workshop time.
