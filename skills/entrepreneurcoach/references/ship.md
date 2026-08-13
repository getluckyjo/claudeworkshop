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

Ask what would actually be useful, and offer six shapes:

**1. A spreadsheet model** — a cashflow forecast, margin analysis by product or
channel, a pricing model, a month-end pack rebuilt from source. Often the single
highest-value artefact in the room, especially for an established business, and
the one an owner will still be using in a year. Build it as a real working file
with real formulas — not a picture of a model.

**2. A document or deck** — an investor deck they can defend, a proposal on
their template, the SOP they've never written down. Right when a specific person
or institution expects a file: a bank, a board, a tender, an auditor.

**3. A one-pager** — they need to be found, or take bookings and enquiries.
The right call if they have no web presence, or theirs is embarrassing.

**4. A pitch site** — they're raising, or selling into partners and sponsors.
A link that opens on a phone in one tap beats a 4MB attachment nobody downloads,
and they can update it after every meeting without resending anything. Strong for
anyone mid-raise or chasing sponsorship.

**5. A dashboard** — they need to *see* something: sales, cash, bookings,
pipeline. Often the one they'd never have thought to ask for.

**6. A small tool** — a quote calculator, a booking form, a pricing estimator,
something their team or customers actually use. Great when they describe a
repetitive job someone does by hand.

Pick from their Station 0 answer. *"I'm chasing sponsors"* — pitch site. *"I
never know where the money is"* — dashboard, or a cashflow model if they need to
plan rather than watch. *"Month-end swallows a week"* — spreadsheet, every time.
Don't run a discovery session; offer the two or three that fit, let them choose,
build it. You can change anything in thirty seconds once it exists.

## File or link?

Ask one question: **what happens to this after they leave the room?**

- **Someone else has to edit it** → file. A model handed over as a web page is
  useless to the accountant who has to work in it.
- **A bank, board, tender or auditor expects it** → file. The world already said
  what format it wants.
- **They'll send it to many people and change it often** → link. One URL, always
  current, no resending.
- **They need to watch numbers move** → dashboard, live.

**Where a page genuinely is better, build it rather than argue for it.** Someone
asking for a pitch deck to email around is usually naming the format they've
always used, not the outcome they want. Offer it in one line — *"I'll make it a
link instead; it opens on a phone and you can change it after every meeting"* —
then build it. Almost nobody asks for the PDF back once they've seen the page.

**And when both help,** build the page and print it to PDF for the version that
has to be attached. Design it so it prints: white background, sensible page
breaks, no dark full-bleed sections that eat a cartridge.

Don't argue the point. If they need a file, they need a file.

## Before you build: ask, and get their brand

**Don't start building off one sentence.** The gap between a generic template and
something they're proud to send is about four questions and a logo.

Ask these, in one turn, conversationally:

1. Who's going to open this link, and what do you want them to do?
2. What are the three things they need to know?
3. Any numbers worth leading with? (Founders undersell their own scale — push
   here. "600+ golf days a year" lands harder than "we run events.")
4. What should it *feel* like — premium, friendly, sharp, understated?

Then ask for their brand. **Say it as an upload, because most people don't
realise they can:**

> Drop in whatever you've got — logo, a photo or two, your colours, an old deck
> or brochure. Even a screenshot of your Instagram works. I'll pull the styling
> from it.

What to do with what you get:
- **Logo** — embed it as a data URI so the page stays self-contained
- **Deck, brochure or existing site** — read the colours, fonts and tone off it
  and match them; don't invent a new brand
- **Photos** — use them. Real photos of the real business beat stock every time
- **Nothing at all** — pick a restrained palette, say what you chose, and tell
  them it's a five-second change once they find the logo

This is the difference between "that's neat" and "I'm sending this to a sponsor
tonight." Don't skip it to save two minutes.

## Which way to ship it

**Building a file? Skip this section.** A spreadsheet, document or deck is
finished when it's in their hands — there's no hosting decision, no account, no
signup. Hand it over and go straight to "Then change something".

For anything that needs to be a link, there are two routes. **Be straight about
the trade-off before you pick** — founders resent discovering a cost or a limit
after they've told people about the link.

| | **Artifact** | **Vercel** |
|---|---|---|
| **Cost** | Included in their Claude plan. Nothing extra, ever. | Free tier covers personal projects. A commercial site may need a paid plan — check current terms. |
| **Public link** | ✅ Publish and share — anyone with the link, no sign-in | ✅ Public by default |
| **Their own domain** | ✗ Always a claude.ai link | ✅ Domain costs extra (~annual fee) |
| **Live data from their Xero / Gmail / Calendar** | ✅ Can call their connectors | ✗ Can't reach their accounts |
| **Setup needed** | None at all | Free account + connector |
| **Outlives their Claude subscription** | ✗ Tied to their Claude account | ✅ Theirs, independent |
| **Looks like a real business** | Fine, but the URL gives it away | ✅ Especially with a domain |

### Choosing

**Artifact** when it's for them or a small circle, needs live numbers, or they
want zero setup. Perfect for a dashboard, an internal tool, or getting something
in front of them in ninety seconds.

**Vercel** when it's customer-facing and needs to look like a real business —
a one-pager, a pitch site, anything they'll put a domain on later.

**The two rows people miss:**

- **Live data only works as an artifact.** A dashboard on Vercel holds numbers
  baked in at build time — fine as a snapshot for a sponsor, useless as something
  they check on Mondays.
- **An artifact lives inside their Claude account.** If they ever stop paying, it
  goes. Anything the business genuinely depends on belongs on Vercel.

**Not sure? Artifact first.** It's free and instant, they see it working, and
moving it to Vercel later is a two-minute job. Don't let a signup form stand
between a beginner and their first win.

> ⚠️ **Facilitator:** Vercel's free tier is intended for non-commercial use, so a
> business site may need a paid plan. Check their current pricing and terms
> before the workshop and tell the room straight — an entrepreneur who finds out
> later feels misled, and that's the one thing that undoes a good session.

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

**Do not skip this.** It works the same whatever you built.

Ask for one change — a headline, a colour, a growth assumption, a price. Make it.
Rebuild. Have them look.

On a site: redeploy and refresh. On a model: change the assumption and watch the
five years redo themselves. On a deck: reorder the argument. Same lesson either
way, and it's the reason they'll come back to Claude on Monday. Give it airtime.

## Hand it over

Give them the link — or the file — and get it in front of someone **right now**,
while you're both still here. Send the link, email the model to their accountant,
WhatsApp the one-pager to a customer. Later never happens. Note it in their
progress summary.

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
