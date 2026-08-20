#!/usr/bin/env python3
"""Build the workshop handouts as HTML, then render them to PDF with Chromium.

For Johannes, not the cohort. Run after editing anything in here:

    ./scripts/build-handouts.py

Everything lands in handouts/. The .html files are intermediates — the PDFs are
what you print. Re-run it as seats fill; add a dict to
ATTENDEES and it picks them up.
"""

import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "handouts"

DATE = "Saturday 22 August 2026"
TIME = "10:00 – 13:00"
VENUE = "CHIPS · 21 Roodehek Street, Gardens"

# --------------------------------------------------------------------------
# The room. One dict per seat.
# --------------------------------------------------------------------------

ATTENDEES = [
    {
        "slug": "danielle",
        "name": "Danielle",
        "business": "d distillery",
        "role": "Founder",
        "job": [
            "A connected model that forecasts demand by brand and SKU, works "
            "backwards to what needs ordering and when, and feeds a rolling "
            "cash-flow forecast.",
            "Before committing to a large production run I want to model the "
            "full opportunity — costs, price, margin, payment terms, funding, "
            "interest, sell-through — change assumptions and immediately see "
            "what I need to charge and how fast I need to sell it.",
        ],
        "building": "Your project profitability model",
        "why": (
            "You named five models. You're leaving with the one that decides "
            "whether the other four are worth building — the go/no-go on a "
            "production run. Costs in, price in, terms in; out comes what you "
            "need to charge, how much you need to sell, and how quickly."
        ),
        "needs": [
            "Your real cost lines for one product — inputs, production, packaging",
            "What you actually sell it for, by channel",
            "Payment terms both ways, and what borrowing costs you",
            "One production run you're weighing up right now",
        ],
        "repeats": (
            "A skill that runs your appraisal the same way every time, and a "
            "weekly cash position with committed runs in it."
        ),
        "watch": (
            "Don't try to build all five models today. Five inputs you can "
            "change beats fifty you can't remember."
        ),
    },
    {
        "slug": "kowie",
        "name": "Kowie Lotter",
        "business": "Creative Beverages",
        "role": "GM",
        "job": [
            "A lot of data from Checkers, PnP, Makro and Tops — stock on hand "
            "and sales-out at store level, weekly.",
            "I want it turned into usable information: stores out of stock, top "
            "performing stores, slow selling stores.",
        ],
        "building": "Your weekly retailer read",
        "why": (
            "Your three retailers send three unrelated formats measuring three "
            "different things, so we build one account at a time — starting "
            "with Checkers, where the money and the trend are. Out of stock, "
            "selling, not selling, in rands. Patch reported separately, the way "
            "Checkers already structures it."
        ),
        "needs": [
            "The Tops export, if it comes — everything else is in, thank you",
            "Which Site Article Statuses count as active, and which are noise",
            "Whether Happy Days, Suncove, Malachite and Distillery Road are still "
            "live — they're in PnP's data but not on the August price list",
            "What 'slow' means in your business — a number, not a feeling",
        ],
        "repeats": (
            "A skill that turns a Checkers export into your read, so next week "
            "is a drag-and-drop — then the same pattern for PnP and Makro. And "
            "a Monday morning brief waiting before your first meeting."
        ),
        "watch": (
            "Every file has a trap. Checkers repeats each article once per pack "
            "size, so totals come out 3 to 5 times too big. PnP's Days Cover "
            "reads zero for stores that are fully stocked but not selling. "
            "Makro's blanks mean 'not listed', not 'none left'. We fix those "
            "first, then build. One account properly beats four half-done."
        ),
    },
    {
        "slug": "reni",
        "name": "Reni le Roux",
        "business": "The Almond Girl",
        "role": "Founder",
        "job": [
            "Replying to website requests about becoming a stockist, sending "
            "the price list and brochure, and replying to Meta ads where a "
            "customer wants to know about a specific product.",
        ],
        "building": "A stockist page, and the reply that sends it",
        "why": (
            "Stop attaching a price list and a brochure to every enquiry. One "
            "link, always current, opens on a phone in one tap. Then a skill "
            "that drafts the reply in your voice with the link already in it."
        ),
        "needs": [
            "Your current price list and brochure",
            "Your stockist terms — minimums, margins, lead times",
            "Two or three enquiries you've answered well, so it sounds like you",
            "A few of the 'when is it back in stock' emails, and roughly when "
            "your next batches are due",
            "Your logo and a couple of product photos",
        ],
        "repeats": (
            "One reply skill in your voice covering both kinds of enquiry — a "
            "stockist gets the stockist link, a customer asking about stock "
            "gets the availability link and a date. Plus a morning check on "
            "who has written in and not heard back."
        ),
        "watch": (
            "You'll finish before the rest of the room, so we have a second "
            "build ready: an availability page for customers. Your plug-in "
            "tells people when something is back; it can't tell them WHEN it "
            "will be back, which is what they keep emailing to ask. Publish "
            "the date and most of those emails stop being sent at all."
        ),
    },
    {
        "slug": "carla",
        "name": "Carla le Roux",
        "business": "Modern Muse",
        "role": "Founder",
        "job": [
            "Difficult to say — I'd like to set up automatic bookings and "
            "invoicing for my new coaching website.",
        ],
        "building": "Your site, live — taking bookings",
        "why": (
            "You leave with a coaching site on the internet that takes a "
            "booking. The booking lands in your inbox, and the next morning "
            "the invoice is already drafted on your template with the right "
            "client, the right session and the right amount. You check it and "
            "send it."
        ),
        "needs": [
            "The sessions you sell, what each one costs, and how long they run",
            "Who they are for, in a sentence you would say out loud",
            "An invoice you've sent recently — the real one, so we match your format",
            "Your banking details as they appear on invoices",
            "Your logo and a photo of you. People book a person, not a service",
        ],
        "repeats": (
            "A skill that turns any booking into a finished invoice, and a "
            "morning check for yesterday's bookings and anything unpaid."
        ),
        "watch": (
            "Two things we are not doing on the day: card payments on the site, "
            "and your own domain. Both are sign-ups and money rather than "
            "builds, and both will eat the whole afternoon if we let them. You "
            "leave with a live web address and invoices going out by EFT — "
            "which is how most coaches get paid anyway."
        ),
    },
    {
        "slug": "maxime",
        "name": "Maxime Davenport",
        "business": "Self employed",
        "role": "Project manager · creative producer · marketing manager",
        "job": [
            "Tracking and logging data manually.",
        ],
        "building": "A log that fills itself in",
        "why": (
            "You stop typing things into a spreadsheet. You tell it what "
            "happened in plain words — or paste in the email, the brief, the "
            "call notes — and it lands in the right row, in the right format, "
            "under the right client. Then it rolls itself up at the end of "
            "the week."
        ),
        "needs": [
            "The thing you're currently logging by hand — the actual file, however rough",
            "What you do with it once it's logged: invoice, report, status update?",
            "Who sees the output, and how often they need it",
        ],
        "repeats": (
            "A skill that turns a sentence into a logged entry, and a weekly "
            "roll-up that writes itself."
        ),
        "watch": (
            "Your brief is six words, so we'll spend the first two minutes "
            "narrowing it. Bring the file and it narrows itself."
        ),
    },
    {
        "slug": "tertius",
        "name": "Tertius",
        "business": "Awakening Journeys (Pty) Ltd",
        "role": "Co-founder",
        "job": [
            "Understanding and interpreting my co-founder's ideas and proposals "
            "to Claude. Re-prompting and editing until it feels like both of us "
            "are understood and the output is useful.",
            "A bigger need — we are not even at the implementation stage of "
            "integrating our invoicing and accounting (QuickBooks).",
        ],
        "building": "Stop being the translator",
        "why": (
            "Right now you sit between your co-founder and Claude, turning "
            "their thinking into something it understands, then editing until "
            "it sounds like both of you. That's a job you've quietly taken on. "
            "We're going to write it down instead — so Claude arrives already "
            "understanding how the two of you think, and either of you can "
            "work with it directly."
        ),
        "needs": [
            "Two or three of your co-founder's proposals or ideas, in their own words",
            "The version you ended up with after re-prompting and editing",
            "What Claude keeps getting wrong about your business",
            "An invoice you've sent recently, and how it gets into QuickBooks today",
        ],
        "repeats": (
            "A skill that carries both of you, so neither has to explain the "
            "business again — and a first pass at the invoicing, drafted in "
            "your format ready to enter."
        ),
        "watch": (
            "Two jobs here and only one is an afternoon. The QuickBooks "
            "integration is a real project, and you said yourselves you're not "
            "at that stage yet. What we can do today is remove the retyping "
            "around invoices — and fix the translating, which costs you more "
            "hours a week than you think."
        ),
    },
    {
        "slug": "liezl",
        "name": "Liezl Kruger",
        "business": "Cape of Storms Apothecary",
        "role": "R&D",
        "job": [
            "Open to all tips, moving into a new business model and target "
            "audience.",
        ],
        "building": "Does the subscription box actually work?",
        "why": (
            "You have the direction — a R1,000 monthly box, Cape Town only. "
            "What you don't have yet is whether the numbers hold. So we build "
            "the model: what goes in the box, what it costs you, what's left, "
            "and what it really takes to get to a thousand subscribers. Then "
            "you change the assumptions until you find a version you believe."
        ),
        "needs": [
            "Your product list with prices, and roughly what each costs to make",
            "What delivery costs you per order today",
            "Your best guess at how many subscribers would cancel in a month",
            "Anything you've already written about the new direction — rough is fine",
        ],
        "repeats": (
            "A monthly subscriber review — who joined, who left, where the run "
            "rate to a thousand stands."
        ),
        "sequence": {
            "title": "Working through it",
            "intro": ("You're doing this on your own, so here are the five steps in "
                      "order. Do them in order — step 1 does more than it looks like "
                      "it does, and the whole thing rests on it. Each box is what to "
                      "ask; the rest is you."),
            "steps": [
                ("Build the box",
                 "I'm putting together a R1,000 monthly subscription box. Here's "
                 "what I sell and what it costs — help me fill the box.",
                 "Keep going until it reaches R1,000. If you run out of things to "
                 "put in before you get there, that is the finding. Sit with it."),
                ("Cost it",
                 "Now add what each one costs me to make, plus packaging and "
                 "delivery, and show me what's left per box.",
                 "That number is your contribution per box. Everything else "
                 "depends on it."),
                ("The engine",
                 "If 5% of subscribers cancel every month, how many new ones do I "
                 "need each month to reach 1,000 within a year?",
                 "Then ask: what if churn were 3% instead? The difference is the "
                 "most useful thing on this page."),
                ("Break it on purpose",
                 "What if the box were R750? What if it went out every second "
                 "month? What if I had four items at R250 instead of twelve?",
                 "And one more, which is the one worth sitting with: what could go "
                 "in the box that isn't a product?"),
                ("Name the answer",
                 "Given all of that, which version of this do I actually believe?",
                 "Write it down. That's the version you build."),
            ],
        },
        "watch": (
            "You're running this one yourself, so work through the five steps "
            "on the next page in order — they're built to be done in sequence, "
            "and step 1 does more than it looks like it does. Don't take the "
            "plan on faith, including mine: change the price, change how often "
            "the box goes out, change what's in it. The version you land on "
            "should be one you argued yourself into."
        ),
    },
]

SCHEDULE = [
    ("10:00", "12′", "Setup and triage", "Logged in, everything working. Problems solved now, not at 11:30."),
    ("10:12", "13′", "Name the job", "Four jobs on the board. That list is the spine of the session."),
    ("10:25", "20′", "Briefing, not prompting", "Rewrite your worst prompt as a proper brief. Watch what changes."),
    ("10:45", "30′", "Build the business brain", "A real Project — your documents, your numbers, your standards."),
    ("11:15", "15′", "Break", "The café is downstairs."),
    ("11:30", "30′", "Point it at real data", "Connect your email, drive or accounts. Ask about your own numbers."),
    ("12:00", "35′", "Delegate the job", "Hand over the job you named. Get back something real."),
    ("12:35", "15′", "Make it repeat", "Turn what worked into a skill. Put it on a schedule."),
    ("12:50", "10′", "Commit and close", "One thing you'll do by Friday. We book the 14-day call here."),
]

DELIVERABLES = [
    ("A Project that knows your business", "Your documents, numbers and standards, in one place that outlives the chat."),
    ("Live data", "Your real email, drive or accounts — not a demo."),
    ("One real artefact", "Built in the room, off your own numbers."),
    ("A skill that repeats your process", "The job you do every month, captured once."),
    ("One job running on a schedule", "The first thing that happens without you."),
    ("A 14-day call and a 30-day review", "Because the room is only a third of it."),
]


BRANDMARK = """<div class="brandmark">
    <span class="name">Johannes le Roux</span><span class="dot"></span>
    <span class="role">Entrepreneur Coach</span>
  </div>"""


def e(s):
    return html.escape(s, quote=False)


def head(title):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<link rel="stylesheet" href="handout.css">
</head>
<body>
"""


def schedule_table():
    rows = []
    for t, d, name, detail in SCHEDULE:
        cls = ' class="break"' if name == "Break" else ""
        rows.append(
            f'<tr{cls}><td class="time">{t}</td><td class="dur">{d}</td>'
            f"<td><strong>{e(name)}</strong><br>{e(detail)}</td></tr>"
        )
    return (
        '<table><thead><tr><th>Time</th><th></th><th>What</th></tr></thead>'
        "<tbody>" + "".join(rows) + "</tbody></table>"
    )


def deliverables_list():
    items = "".join(
        f"<li><b>{e(t)}</b><span>{e(d)}</span></li>" for t, d in DELIVERABLES
    )
    return f'<ol class="deliverables">{items}</ol>'


def lines(n, short=False):
    cls = "lines short" if short else "lines"
    return f'<div class="{cls}">' + "<div></div>" * n + "</div>"


def sequence_page(a):
    """An extra page of prompts, for anyone working through their build alone."""
    seq = a.get("sequence")
    if not seq:
        return ""
    blocks = []
    for i, (name, prompt, note) in enumerate(seq["steps"], 1):
        blocks.append(f"""
  <div style="margin-bottom:7mm">
    <p style="font-family:var(--display);font-size:9.5pt;font-weight:600;
       letter-spacing:var(--tracking-tight);margin:0 0 2mm 0">
      <span style="color:var(--red)">{i}</span>&nbsp;&nbsp;{e(name)}</p>
    <div style="background:var(--bone);padding:3.5mm 4.5mm;margin:0 0 2mm 0">
      <p style="margin:0;font-size:10pt">&ldquo;{e(prompt)}&rdquo;</p>
    </div>
    <p class="small" style="margin:0">{e(note)}</p>
  </div>""")
    return f"""
<section class="page">
  <h2>{e(seq['title'])}</h2>
  <p class="standfirst">{e(seq['intro'])}</p>
  {''.join(blocks)}
</section>"""


def workbook(a):
    job = "".join(f"<p>{e(p)}</p>" for p in a["job"])
    needs = "".join(f"<li>{e(n)}</li>" for n in a["needs"])

    return (
        head(f"Workbook — {a['name']}")
        + f"""
<section class="page cover">
  {BRANDMARK}
  <h1>Claude for<br><em>entrepreneurs.</em></h1>
  <div class="hero-rule"></div>
  <p class="lede">3 hours, your laptop, one job you actually hate. You leave with it running.</p>

  <div class="namecard">
    <p class="who">{e(a['name'])}</p>
    <p class="what">{e(a['role'])} &nbsp;·&nbsp; {e(a['business'])}</p>
  </div>

  <div class="quoteblock">
    <p class="label">The job you named</p>
    {job}
  </div>

  <div class="coverfoot">
    <span>{e(DATE)} &nbsp;·&nbsp; {e(TIME)}</span>
    <span>{e(VENUE)}</span>
  </div>
</section>

<section class="page">
  <h2>What you walk out with</h2>
  <p class="standfirst">6 things, running, on your own machine. Not notes about
  how you might do it later.</p>
  {deliverables_list()}

  <h3>Bring</h3>
  <ul class="tight">
    <li>A laptop and a charger</li>
    <li>One real, messy file from your business — not a tidy example</li>
    <li>Your logo, a couple of photos, an old deck or brochure if you have one</li>
    <li>Claude installed and signed in, with the workshop skill added</li>
  </ul>

  <div class="note">
    <p class="label">One rule</p>
    <p>You won't be asked to write code, open a terminal, or install anything
    beyond the app itself. If a step ever seems to need it, say so — it means
    we've taken a wrong turn, not that you've missed something.</p>
  </div>
</section>

<section class="page">
  <h2>The three hours</h2>
  <p class="standfirst">Roughly a quarter teaching, the rest you, doing it.</p>
  {schedule_table()}

  <div class="callout">
    <p><strong>If you fall behind, get to 12:00.</strong> That's the block that
    makes the day worth it. Everything before it is setup and everything after
    it is making it repeat — but the middle is where you hand over a real job
    and get something back.</p>
  </div>
</section>

<section class="page">
  <h2>Briefing, not prompting</h2>
  <p class="standfirst">The single biggest difference between people who find
  this underwhelming and people who don't. A prompt asks for a thing. A brief
  says what you're trying to achieve and hands over what's needed to do it.</p>

  <h3>The five parts</h3>
  <ol>
    <li><strong>The job.</strong> What you actually want done, and why it matters.</li>
    <li><strong>The context.</strong> Your business, your numbers, your constraints.</li>
    <li><strong>The material.</strong> The real file. Not a description of the file.</li>
    <li><strong>What good looks like.</strong> How you'd know it was done properly.</li>
    <li><strong>The format.</strong> A spreadsheet, a page, a document, an email.</li>
  </ol>

  <div class="write">
    <p class="prompt">Write your worst prompt here — the one that gave you a
    disappointing answer.</p>
    {lines(3, short=True)}
  </div>

  <div class="write">
    <p class="prompt">Now write it as a brief.</p>
    {lines(9)}
  </div>
</section>

<section class="page">
  <h2>{e(a['building'])}</h2>
  <p class="standfirst">{e(a['why'])}</p>

  <h3>What it needs from you</h3>
  <ul>{needs}</ul>

  <h3>What repeats afterwards</h3>
  <p>{e(a['repeats'])}</p>

  <div class="note">
    <p class="label">Watch for</p>
    <p>{e(a['watch'])}</p>
  </div>

  <div class="write">
    <p class="prompt">Notes — assumptions, numbers, things to fix later</p>
    {lines(7)}
  </div>
</section>

{sequence_page(a)}
<section class="page">
  <h2>Before you leave</h2>
  <p class="standfirst">Most training evaporates inside a fortnight. This is the
  page that decides whether yours does.</p>

  <div class="write">
    <p class="prompt">The one thing I'll do by Friday</p>
    {lines(2, short=True)}
  </div>

  <div class="write">
    <p class="prompt">What I built today, and where it lives</p>
    {lines(3, short=True)}
  </div>

  <div class="write">
    <p class="prompt">What I'd build next, if this works</p>
    {lines(3, short=True)}
  </div>

  <h3>What happens now</h3>
  <ul class="tight">
    <li><strong>Day 1</strong> — your asset pack: Project template, the skill you
    built, my prompt library</li>
    <li><strong>Day 14</strong> — a 60-minute group call. One win and one blocker
    each. This is the call that decides whether it sticks</li>
    <li><strong>Day 30</strong> — a written review: what's working, what isn't,
    what's next</li>
  </ul>

  <h3>Stuck between now and then</h3>
  <p>Tell Claude what happened — it can fix most of it. If it can't, mail me.
  I'd rather hear about it on the Tuesday than at the 14-day call.</p>

  <p class="signature" style="margin-top:10mm">Johannes</p>

  <div class="coverfoot" style="margin-top:4mm">
    <span>Entrepreneur Coach</span>
    <span>leroux.johannes@gmail.com</span>
  </div>
</section>
</body></html>
"""
    )


def cheatsheet():
    return (
        head("Cheat sheet")
        + f"""
<section class="page">
  {BRANDMARK}
  <h2>Where <em>everything</em> lives</h2>
  <p class="standfirst">The four screens you'll actually need. Stick this on the
  wall — it's the thing people forget by Wednesday.</p>

  <div class="cols">
    <div>
      <h3>Skills</h3>
      <ol class="steps">
        <li>Your name or initials, bottom left</li>
        <li><kbd>Settings</kbd></li>
        <li><kbd>Customize</kbd></li>
        <li>Find <kbd>Skills</kbd></li>
        <li>Add or upload</li>
      </ol>
      <p style="font-size:9pt;color:var(--muted)">It moved out of Capabilities.
      Any guide older than a few months sends you to the wrong menu.</p>

      <h3>Connectors</h3>
      <ol class="steps">
        <li><kbd>Settings</kbd></li>
        <li><kbd>Connectors</kbd></li>
        <li>Find the one you want</li>
        <li><kbd>Connect</kbd></li>
        <li>Approve in the pop-up</li>
      </ol>
      <p style="font-size:9pt;color:var(--muted)">Switch any of them off from the
      same screen, in seconds.</p>
    </div>
    <div>
      <h3>Projects</h3>
      <ol class="steps">
        <li><kbd>Projects</kbd> in the sidebar</li>
        <li><kbd>New project</kbd></li>
        <li>Name it after the real thing</li>
        <li>Add your documents and numbers</li>
        <li>Start chats <em>inside</em> it</li>
      </ol>
      <p style="font-size:9pt;color:var(--muted)">If it doesn't seem to know your
      business, check you started the chat inside the project.</p>

      <h3>Schedules</h3>
      <ol class="steps">
        <li>Just ask, in plain words</li>
        <li>"Every Monday at 7am, …"</li>
        <li>Find them under Routines or Tasks</li>
        <li>Pause or delete from there</li>
      </ol>
      <p style="font-size:9pt;color:var(--muted)">You never have to find a menu to
      set one up. Only to switch it off.</p>
    </div>
  </div>

  <h3>When it goes wrong</h3>
  <table>
    <tbody>
      <tr><td style="width:62mm"><strong>Uploaded a skill, nothing happens</strong></td>
        <td>Start a <em>new</em> chat. Skills don't load into a conversation that was already running.</td></tr>
      <tr><td><strong>Downloaded the skill and got a folder</strong></td>
        <td>Your Mac unzipped it. The <kbd>.zip</kbd> is still in Downloads next to it — use that.</td></tr>
      <tr><td><strong>Connector pop-up hangs</strong></td>
        <td>Pop-up blocker, or you're signed into the wrong Google account in that browser. Try incognito.</td></tr>
      <tr><td><strong>Connected, but it can't see anything</strong></td>
        <td>It's switched off for this chat. Turn it on in the chat's own connector settings.</td></tr>
      <tr><td><strong>Your scheduled job writes an essay</strong></td>
        <td>Ask for three lines and what you should do about it. Don't fix it with formatting.</td></tr>
      <tr><td><strong>Something asks for a password or a key</strong></td>
        <td>Stop. Nothing here needs one. Ask me.</td></tr>
    </tbody>
  </table>

  <div class="note">
    <p class="label">The habit that makes it stick</p>
    <p>Start work inside your Project, not in a blank chat. Everything you loaded
    today is sitting in there — and a blank chat knows none of it.</p>
  </div>

  <div class="coverfoot" style="margin-top:8mm">
    <span>Johannes le Roux &nbsp;·&nbsp; Entrepreneur Coach</span>
    <span>{e(DATE)}</span>
  </div>
</section>
</body></html>
"""
    )


def facilitator_pack():
    briefs = []
    for a in ATTENDEES:
        job = " ".join(a["job"])
        briefs.append(
            f"""
<div style="border-top:2px solid var(--ink);padding-top:3mm;margin-bottom:7mm">
  <p style="margin:0 0 1mm 0"><strong style="font-family:var(--display);font-size:14pt;font-weight:normal">{e(a['name'])}</strong>
    <span style="color:var(--muted)"> — {e(a['business'])}, {e(a['role'])}</span></p>
  <p style="font-size:9pt;color:var(--muted);margin:0 0 2.5mm 0"><em>{e(job)}</em></p>
  <p style="margin:0 0 1.5mm 0"><strong>Build:</strong> {e(a['building'])}</p>
  <p style="margin:0 0 1.5mm 0"><strong>Needs:</strong> {e('; '.join(a['needs']))}</p>
  <p style="margin:0"><strong>Watch:</strong> {e(a['watch'])}</p>
</div>"""
        )

    return (
        head("Facilitator pack")
        + f"""
<section class="page">
  <p class="eyebrow eyebrow-red">Facilitator pack &nbsp;·&nbsp; not for the cohort</p>
  <h2>Run of show</h2>
  <p class="standfirst">{e(DATE)} · {e(TIME)} · {e(VENUE)} · 6 of 8 seats</p>
  {schedule_table()}

  <div class="note">
    <p class="label">Where your attention goes</p>
    <p>Block 7 is 35 minutes across six people. Don't try to see everyone.
    Kowie first — nothing of his works until the retailer files parse. Then
    Liezl: she has a real brief now, but the findings have to be hers, so ask
    and wait rather than telling. Then one check on Carla. Danielle, Reni and
    Maxime can run unaided; put Reni's finished link on the projector.</p>
  </div>

  <h3>Before Saturday</h3>
  <ul class="tight">
    <li><strong>Phone Liezl.</strong> Ten minutes. What's the new model, who's the new audience</li>
    <li><strong>Chase Kowie's retailer files.</strong> Last week's exports, all four, untidied. Highest-value email you send this week</li>
    <li>Confirm Danielle is on Xero — if not, her connector is Drive</li>
    <li>Confirm Reni can hand over her price list and brochure</li>
    <li>Amended pre-work out: skill install, Google or Microsoft, bring your brand, bring the messy file</li>
    <li>Check where scheduled tasks live in your build, and set one up yourself</li>
  </ul>
</section>

<section class="page">
  <h2>The room</h2>
  <p class="standfirst">Three camps. Danielle and Kowie turn data into
  decisions. Reni and Carla turn a request into a response. Maxime's data only
  exists because she types it. Sit Danielle and Kowie together, and let the
  overlap land when the jobs go on the board.</p>
  {''.join(briefs)}

  <div class="callout">
    <p><strong>Danielle and Maxime use Claude daily; the other four are
    weekly.</strong> The briefing block matters more than the run sheet assumes —
    don't rush it to buy time elsewhere unless the last two seats sell.</p>
  </div>

  <div class="coverfoot" style="margin-top:8mm">
    <span>Entrepreneur Coach</span>
    <span>Facilitator copy</span>
  </div>
</section>
</body></html>
"""
    )


def find_chromium():
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    # Playwright's bundled build, which is what's present on the cloud runners.
    for pattern in ("chromium-*/chrome-linux/chrome", "chromium_headless_shell-*/chrome-linux/headless_shell"):
        found = sorted(Path("/opt/pw-browsers").glob(pattern))
        if found:
            return str(found[-1])
    sys.exit("Error: no Chromium found — can't render PDFs.")


def to_pdf(chrome, html_path, pdf_path):
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--virtual-time-budget=4000",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        check=True,
        capture_output=True,
    )


def main():
    OUT.mkdir(exist_ok=True)
    chrome = find_chromium()

    pages = [(f"workbook-{a['slug']}", workbook(a)) for a in ATTENDEES]
    pages.append(("cheatsheet", cheatsheet()))
    pages.append(("facilitator-pack", facilitator_pack()))

    for name, markup in pages:
        html_path = OUT / f"{name}.html"
        pdf_path = OUT / f"{name}.pdf"
        html_path.write_text(markup)
        to_pdf(chrome, html_path, pdf_path)
        size = pdf_path.stat().st_size // 1024
        print(f"  {pdf_path.relative_to(ROOT)}  ({size} KB)")

    print(f"\nBuilt {len(pages)} PDFs into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
