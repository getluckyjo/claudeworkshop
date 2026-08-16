#!/usr/bin/env python3
"""Build the workshop handouts as HTML, then render them to PDF with Chromium.

For Johannes, not the cohort. Run after editing anything in here:

    ./scripts/build-handouts.py

Everything lands in handouts/. The .html files are intermediates — the PDFs are
what you print. Re-run it when the other four seats fill; add a dict to
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
VENUE = "Ideas Cartel, Claremont"

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
            "One retailer's export in, three answers out — who's out of stock, "
            "who's selling, who isn't. Then a skill that does the same thing to "
            "the other three, so retailer two is a ten-minute job instead of a "
            "rebuild."
        ),
        "needs": [
            "Last week's exports from all four retailers — untidied, as they arrive",
            "Which store codes matter to you and which are noise",
            "What 'slow' means in your business — a number, not a feeling",
        ],
        "repeats": (
            "A skill for the other three retailers, and a Monday morning read "
            "waiting for you before your first meeting."
        ),
        "watch": (
            "One retailer done properly beats four done badly. We'll be "
            "straight with you about how much of the Monday read runs on its "
            "own versus waiting for you to drop the file in."
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
            "Your logo and a couple of product photos",
        ],
        "repeats": (
            "A reply skill in your voice, and a morning check on who enquired "
            "and hasn't heard back."
        ),
        "watch": (
            "You'll finish before the rest of the room. Come find me — the "
            "same trick pointed at your Meta ad questions is a twenty-minute "
            "build."
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
        "building": "Your new positioning, on one page",
        "why": (
            "A new model and a new audience is the build. What you're now "
            "selling, who it's for, and why it's different — written down "
            "properly, in one place, so every quote, post and conversation "
            "says the same thing."
        ),
        "needs": [
            "Who the new audience is, as specifically as you can manage",
            "What you're selling them that you weren't selling before",
            "Anything you've already written about the new direction — rough is fine",
        ],
        "repeats": (
            "A skill that keeps your writing consistent while the story is "
            "still settling, and a weekly prompt that asks you the questions "
            "you should be answering."
        ),
        "watch": (
            "Yours is the most open brief in the room, which makes it the "
            "easiest one to spend three hours exploring and leave empty-handed. "
            "We'll name the artefact early and hold you to it."
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
  <p class="standfirst">{e(DATE)} · {e(TIME)} · {e(VENUE)} · four of eight seats</p>
  {schedule_table()}

  <div class="note">
    <p class="label">Four people, not eight</p>
    <p>Double the per-person time. Spend the surplus on Danielle and Kowie —
    theirs are the hard builds. Reni finishes early and becomes your demo. Liezl
    needs the brief narrowed for her or she'll explore for three hours.</p>
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
  <p class="standfirst">Three of four are physical-product businesses with stock.
  Danielle and Kowie have the same problem from opposite ends — data about
  product movement arriving faster than anyone can turn it into a decision. Sit
  them together, and let that overlap land when the four jobs go on the board.</p>
  {''.join(briefs)}

  <div class="callout">
    <p><strong>Only Danielle uses Claude daily.</strong> The other three are
    weekly. The briefing block matters more than the run sheet assumes — don't
    rush it to buy time elsewhere.</p>
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
