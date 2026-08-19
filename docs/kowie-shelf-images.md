# Shelf images over WhatsApp — a note for Kowie

**Question, 18 Aug:** merchandising companies send hundreds of shelf photos a day
over WhatsApp, from every store. How do we screen that and get a daily report?

Short answer: **the photographs are not the hard part, and the report is not the
point.** Read on before anyone builds anything.

---

## 1. Start with what only a photograph can tell you

You already know a great deal about stock without a single image. PnP sends stock
on hand and a sales rate per store per week. Checkers sends listed versus active
and six weeks of units. Makro sends 30 days of daily stock and sales.

So don't build a system that tells you what those files already tell you. Build
one that answers what they **can't**:

| Question | Retailer file | Photograph |
|---|---|---|
| Do they have stock? | **Yes** | — |
| Is it **on the shelf**? | No | **Yes** |
| How many facings, and next to whom? | No | **Yes** |
| Is the price right and the promo up? | No | **Yes** |
| Is it in the right place in the aisle? | No | **Yes** |

**The prize is phantom stock** — the store's system says it has 40 units, the
photo says the shelf is empty, so the stock is in the back room and nobody has
faced it up. That costs you sales while every report you own says you're fine.

Nothing you currently receive can find that. The photos plus the retailer file
can, and neither can alone. **That is the report worth building**, and it is one
line long most days: *these 6 stores show stock in the system and an empty shelf.*

Not "here are 300 photos, summarised."

## 2. WhatsApp is the hard part, and it isn't the AI

Reading a shelf photo is the easy bit. The problem is that a WhatsApp image
arrives with no idea **which store it is**. Hundreds a day, no store code, no
date beyond the timestamp, no SKU, and often no caption. Whatever you build, the
first thing it needs is structure at the point of capture.

Three ways to get it, cheapest first:

**A · Fix the caption. Costs nothing, do it this week.**
Every image must carry the store code as the caption — `WD17 Langebaan`. One
rule, told once to the merchandising agency. It turns an unusable stream into a
sortable one and needs no software at all. **Do this regardless of what else you
build**, because every option below depends on it.

**B · One WhatsApp group per region, or per merchandiser.**
Narrows the guess. Still needs the caption for store-level accuracy, but it means
a missing caption is recoverable rather than lost.

**C · WhatsApp Business API — the real build.**
Images land at a webhook instead of a phone, get stored with sender, timestamp
and caption, and are processed automatically. This is the version that scales.
It is also a **project, not an afternoon**: a WhatsApp Business sender has to be
registered through Meta, which takes days to weeks and involves business
verification. Start that clock early if you want it.

## 3. Screen by exception, never by volume

Do not summarise 300 photos. Nobody reads that, and by Thursday you won't open it.

The flow that works:

```
image + store code
      ↓
is our product visible?         → no  → flag
how many facings?               → down vs last week → flag
is the shelf empty or gapped?   → yes → flag
price ticket correct?           → no  → flag
      ↓
everything else: counted, not reported
```

Then cross the flags against that retailer's stock file:

- **Empty shelf + system shows stock** → phantom stock. Call the store.
- **Empty shelf + system shows zero** → genuine out of stock. Call the buyer.
- **On shelf but facings down** → someone else took your space. Call the account.

Three different phone calls. That distinction is the entire value of the exercise,
and it's invisible without both sources.

## 4. What the daily report should look like

One WhatsApp message or email to you, before your first meeting:

> **Tue 19 Aug · 284 images from 96 stores**
> 6 phantom stock — system says stock, shelf is empty: Hyper Bloemfontein,
> Canal Walk, Cresta, Somerset Mall, Gateway, Menlyn
> 3 lost facings — Rekorderlig Passion Fruit down from 4 to 2: Constantia,
> Lakeside, Tygervalley
> 2 no coverage — no photo received in 6 days: Klerksdorp, Polokwane
> Everything else: 273 images, nothing to act on

**"No photo received" is the line that pays for the whole thing.** It audits the
merchandising company you're paying. Right now you have no way of knowing which
stores they actually visited — and a merchandiser who knows the photos are being
counted behaves differently.

## 5. What to do, in order

1. **This week, free:** mandate the store code as the caption. One email to the
   agency.
2. **Week 2:** start the WhatsApp Business sender registration if you want option
   C. The clock is long, so start it before you need it.
3. **Week 2–3:** get the images somewhere reachable — a shared Drive folder per
   week is enough to begin, even if someone exports them by hand at first.
4. **Then build:** screening plus the cross-check against your retailer file,
   producing the exception report above.
5. **Only then** consider facings and share-of-shelf. It's the most interesting
   number and the least urgent.

## 6. Scope, honestly

**This is not a Saturday build.** Hundreds of images a day, an inbound WhatsApp
integration and a Meta registration is a several-week project, and pretending
otherwise would waste your workshop block.

What Saturday gives you is the half that makes this one work: the Checkers read,
the habit of running one account properly, and the skill pattern you'd reuse
here. **Step 1 above costs nothing and can be sent from your phone on Monday** —
and without it, none of the rest works anyway.

Worth revisiting at the 14-day call, when the caption rule has had two weeks to
bed in and you can see how much of the stream is actually usable.
