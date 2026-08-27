# Building on Shopify

Read this when someone's build is a Shopify store — a new brand, a relaunch, a
theme they've outgrown. It's a different shape to the rest of Station 3, because
Shopify is a hosted platform rather than a blank page, and the useful answer
depends entirely on which part of it they mean.

## First, split the question

"Build me a Shopify site" is three jobs wearing one coat. Ask which one they
mean before offering anything, because the answers have nothing in common:

| They mean | What that actually is | Can we do it |
|---|---|---|
| **The store setup** | Plan, payments, domain, shipping zones, tax, navigation | **No.** Shopify admin, them, clicking. Say so plainly |
| **The products** | Titles, descriptions, SEO, tags, variants, images | **Yes**, two ways — see below |
| **The design and build** | Theme, layout, sections, the way it looks and moves | **Yes**, and this is the interesting one |

Most people asking a creative or brand person's version of the question mean the
third. Most people asking an operator's version mean the second. Get this wrong
and you'll spend the session on the part they didn't care about.

**Never touch a live theme.** Whatever the route, duplicate the theme first, or
work on an unpublished one. A storefront taking orders is production. Say this
out loud once, early — it costs five seconds and it's the mistake that ends a
session badly.

## The products

Two routes. The transport is never the bottleneck — writing forty product
descriptions that sound like the brand is the work, and that's identical either
way. Choose on what they want *between* the writing and the shop floor.

**A product import CSV.** Claude builds it; they open it, read it, fix it, then
Shopify → Products → Import. Needs nothing but Claude. The spreadsheet is a
review gate — they see everything before a single product exists in a real store.
**Default to this**, especially for a launch, and especially when the store
carries brand equity that isn't theirs alone to risk.

Columns Shopify expects: `Handle`, `Title`, `Body (HTML)`, `Vendor`, `Type`,
`Tags`, `Published`, `Option1 Name`, `Option1 Value`, `Variant SKU`,
`Variant Price`, `Variant Inventory Qty`, `Image Src`, `Image Alt Text`,
`SEO Title`, `SEO Description`, `Status`.

**Straight into the store, over the Admin API.** Claude creates and edits
products, sets inventory, reads orders. Real, and worth knowing about — but be
precise about what it takes, because the obvious assumption is wrong. **Shopify's
own MCP servers do not do this.** Storefront and Checkout are shopper-facing;
Dev MCP is documentation and code validation. Writing to a store means a
third-party MCP server wrapping the GraphQL Admin API, plus an Admin API token
generated from a custom app in their Shopify admin. In any business bigger than
one person, that token is infrastructure someone owns — it's a conversation, not
a decision they make in the room.

Earn the second route on the first. Once a brand-voice skill exists and they
trust what comes out of it, the connector is the obvious tool for the
month-after work: a seasonal range, a price change across forty SKUs.

## The design and build — the good one

Here's the thing worth knowing, and most people don't: **the loop is the same one
in `project.md`, with Shopify where Vercel would be.**

    Claude Code on the web  →  GitHub  →  Shopify

Shopify publishes a GitHub app that syncs a repository branch with a theme. Push
to the branch and the theme updates in the admin; edit in the admin and it
commits back to the branch. So the whole build becomes: *ask for a change →
review it → merge → look at it in the theme preview.* No terminal, ever.

**Setting it up:**

1. In Shopify admin: **Online Store → Themes**. Duplicate the theme they want to
   work on, or add a new one. **Connect the GitHub branch to that unpublished
   theme, not the live one.** The integration will happily sync to whatever it's
   pointed at, and pointing it at the live theme means every merge is a
   deployment to customers
2. Connect the repository through Shopify's GitHub app
3. Go to [claude.ai/code](https://claude.ai/code), sign in with the same Claude
   account, connect GitHub, and open that repository
4. Ask for changes in plain language. Claude works on a branch and opens a pull
   request; they review and merge; Shopify picks it up

Needs Pro, Max or Team, and Claude Code on the web is a research preview — say
that rather than presenting it as bulletproof.

**The two-way sync is the sharp edge.** Because the admin commits back, someone
editing in the theme editor while Claude works on the same files produces a
genuine conflict. Not fatal, but tell them: one or the other at a time, and pull
before starting a session.

## What to actually ask for

The instinct is to ask for a page. Better is to ask for **sections with proper
schema** — because a section with a well-written `{% schema %}` block appears in
the theme editor with its own controls, and then they can design without code
forever after.

That's the real unlock for anyone with an eye: **Claude builds the section, they
design in the visual editor.** Say it in those words. A creative director who
realises they've just been handed a new control panel — not a fixed page — is the
moment this lands.

So:

- *"Build me a homepage"* → a fixed thing only Claude can change
- *"Build me a section with settings for the heading, the image, the alignment
  and whether it's full-bleed"* → something they own

Start from a real theme rather than nothing. Horizon and its family are free on
the Theme Store and are what Shopify builds against now — blocks nest up to eight
levels deep, against two in Dawn and the older Online Store 2.0 themes. Dawn is
still perfectly good and better documented. **There is no automatic migration
from Dawn to Horizon**, so if they're on Dawn and happy, build on Dawn; don't
start a re-platform in a three-hour session.

## Make Claude check itself

Liquid is where it will invent — a filter that doesn't exist, an object that
isn't available in that template. Shopify ships a **Dev MCP** server that fixes
this: it searches Shopify's live documentation, introspects the Admin and
Storefront GraphQL schemas, and **validates Liquid against the theme schema**
before a file is written.

Be straight about who can use it. It runs as a local stdio process via npx, so
it belongs to someone working in Claude Code, not to someone in the desktop app's
Connectors screen. For a founder on the desktop app, the honest substitute is
cheaper and nearly as good:

> Before you write any Liquid, tell me which Shopify theme objects and filters
> you're relying on and which version of the theme architecture you're assuming.

That one question catches most of it, because it forces the assumption into the
open where they can see it's wrong.

## Snags

**"Can you just design it for me?"** — Yes, and this is where taste has to do
some work. Ask for their brand first: logo, fonts, colours, three sites they
like and one they hate. Without that it produces a competent, anonymous store.
With it, it produces theirs.

**They edit in the theme editor mid-session.** Conflicts with the GitHub sync.
One at a time.

**The theme they bought is encrypted or minified.** Some paid themes ship
compiled CSS and are genuinely painful to work in. Check early; if it's bad, a
free Horizon theme is a better base than fighting one they paid for.

**They want the live store changed now.** Slow it down. Preview the unpublished
theme, look at it on a phone, then publish. Publishing is one button and it can
wait ten minutes.

**Apps overwrite theme code.** Some Shopify apps inject into theme files. If
something reappears after being removed, an app is putting it back — not Claude.

## Say these out loud

> There are three different jobs inside "build my Shopify site." Which one is
> eating your time?

> I can't set up your payments or your domain — that's you in the admin. What I
> can do is build the theme, and give you controls so you can keep designing it
> without me.

> We're working on a duplicate. Nothing you do in the next hour can touch what
> your customers see.

> Don't ask me for a page. Ask me for a section with settings, then design it
> yourself in the editor.
