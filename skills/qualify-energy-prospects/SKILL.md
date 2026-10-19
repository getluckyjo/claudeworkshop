---
name: qualify-energy-prospects
description: "Score a company for how much electricity it probably uses, before spending a meeting on it. Built for Trevor Davenport at Efficient Energy SA, who sells Best.Energy monitoring on a 60-month rental and needs to reach decision makers at large energy users. Use when qualifying or scoring a prospect, sizing a company's energy spend, deciding whether a lead is worth a meeting, building or filtering a prospect list from LinkedIn, Sales Navigator or Dripify, writing outreach or follow-up to an energy prospect, preparing a Gap Analysis Report, or working out the minimum energy spend a client needs for the system to pay for itself."
license: MIT
---

# Qualify energy prospects

**For Trevor Davenport, Efficient Energy SA.** Best.Energy monitoring, sold as a
60-month rental, pitched on finding more waste than the system costs.

The job: stop booking meetings with companies too small to be worth the drive.

## The thing to get right first

Trevor can find decision makers. Sales Navigator and Dripify do that fine. What
the current process doesn't do is check whether the **company** is worth
reaching — so qualification happens in the meeting, which is the most expensive
place it could possibly happen.

**So the order is wrong, not the tooling.** Qualify the company on energy, then
find the person inside it. Never the other way round.

Everything below serves that one reorder.

## Start with his own floor

Before scoring anything, make Trevor state a number. The pitch is *we find more
waste than the system costs*, and that sentence contains a minimum viable
customer whether or not anyone has written it down.

Ask for:

- The monthly rental for a typical install
- The share of spend he typically identifies as recoverable waste
- How much of that a client realistically acts on

Then compute the floor:

    minimum monthly electricity spend  =  monthly rental  ÷  (waste % × acted-on %)

If he says R12,000 a month, finds 15%, and clients act on half, the floor is
R160,000 a month. **Below that the deal cannot work on its own logic**, and any
meeting under it was always going to be a no.

Make him say the number out loud. "Large energy user" is a feeling; a rand
figure is a filter. Write it into the project so every later score is measured
against it. Everything after this is about estimating, from the outside, whether
a company clears it.

Read `references/scoring.md` for the full model, and
`references/signals-sa.md` for what's observable in South Africa specifically.

## How to score a company

Work down this ladder. Stop as soon as a signal disqualifies, and don't go
hunting for the next one — the point is to spend as little as possible on a
company that was never going to qualify.

1. **Industry** — energy intensity per rand of turnover varies by more than an
   order of magnitude. A 40-person foundry outspends a 400-person insurance
   brokerage several times over.
2. **Shift pattern** — the single most underrated multiplier. The same plant
   running 24/7 instead of one day shift uses roughly three times the
   electricity. Worth more than headcount, revenue and floor area put together.
3. **Equipment signature** — compressed air, industrial refrigeration, electric
   furnaces, injection moulding, kilns, ovens, large pumping, heavy HVAC. Any of
   these present at scale and the company is probably worth a look.
4. **Physical footprint** — roof area, number of sites, cooling towers and
   extraction visible from satellite.
5. **Tariff** — the most reliable public-ish signal in South Africa, and the one
   people answer without hesitating.
6. **Notified maximum demand, in kVA** — close to a direct read on size.
7. **Actual spend** — the answer, if anyone will give it.

**Score the company, then pick the person.** The decision maker only matters
once the company clears the floor.

## The question that replaces a wasted meeting

The fastest qualifier in the country is the tariff name, because operations and
finance people answer it without feeling interrogated — it's administrative, not
commercial.

> Which Eskom tariff are you on — Megaflex, Miniflex, Nightsave — or are you
> billed by the municipality as a large power user?

**Megaflex applies above 1 MVA of notified maximum demand.** So a company on
Megaflex is, by definition, a large energy user, and Trevor can stop guessing.
A company that doesn't know which tariff it is on has just told him something
too: nobody there is managing energy, which is the problem he sells into.

Follow with: **"What's your NMD in kVA?"** Anyone who answers that is worth a
meeting regardless of what else the list said.

Put both questions in front of the meeting — in the Dripify sequence, in the GAR
request form, on the phone. One answer replaces an hour and a drive.

## Reshaping the outreach

The Gap Analysis Report is a genuinely good lead magnet and it's being spent too
early. It's free, it's real work, and right now anyone can have one.

**Gate it on a qualifying answer, don't gate it behind a meeting.** Asking for
the tariff and the NMD in order to produce the GAR is not a hurdle — it's
obviously necessary information, so it reads as competence rather than
screening. Companies that answer have qualified themselves. Companies that
won't were never going to sign a 60-month rental.

When drafting sequences, keep three things straight:

- **Lead with the waste, not the hardware.** Nobody wants a monitoring system.
  They want to stop paying for something they aren't using.
- **The 500%-faster-than-inflation line is the hook** — it's specific, it's
  checkable, and every operations director in the country already feels it.
- **One industry at a time.** A sequence to cold storage and a sequence to
  plastics should not be the same sequence, because the waste is not in the same
  place. The GAR compares against peers worldwide — say which peers.

## What Trevor may be leaving on the table

Raise this once, then leave it with him.

**Section 12L.** The energy efficiency savings tax incentive was due to lapse at
the end of 2025 and National Treasury extended it to **31 December 2030**, at up
to **95c per kWh saved**. Claims require measurement and verification by a
SANAS-accredited body.

That matters commercially: his system is the measurement layer those claims need,
and it reframes the rental from a cost against savings to a cost against savings
*plus a deduction*. Check the current rate and rules before putting a number in
front of a client — this is tax, it moves, and it is his accountant's call not
his. But a 60-month rental that partly funds itself through a tax deduction is a
different conversation to one that doesn't.

## Snags

**A good industry with a bad site.** A food producer that outsourced its cold
chain has the SIC code and not the load. Equipment beats industry every time.

**Group versus site.** A listed group's sustainability report describes the
group; the meeting is about one plant. Score the site.

**Landlord-metered tenants.** In a multi-tenant park the tenant may not see a
meter or control the HVAC. The decision maker is the landlord, and that's a
different sell.

**Big spend, no authority.** Plenty of large users have a facilities manager who
agrees enthusiastically and can't sign. The qualification is energy *and*
authority — the first one is what's currently missing, but don't lose the second.

**Already monitored.** Some have a system nobody reads. That's not a lost lead,
it's a better one: the analysis is the product, and an unread dashboard is proof
the hardware alone doesn't solve it.

## Say these out loud

> What's the minimum monthly electricity spend where this still works for both
> of us? Until that's a number, every list is a guess.

> Score the company first. The decision maker is the second question, not the
> first.

> Which tariff are you on? One answer, and we both know whether this meeting is
> worth having.
