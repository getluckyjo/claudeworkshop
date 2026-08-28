#!/usr/bin/env python3
"""Build the one-page CV, on the Entrepreneur Coach brand.

    ./scripts/build-cv.py

Aimed at a specific role rather than being a general career history — the
ROLE dict at the top says which. A CV that answers a job ad's own bullets in
its own order beats a chronology, and one page forces that discipline.

Reuses handouts/fonts.css so Geist is embedded and the PDF prints identically
anywhere. The layout is its own stylesheet: a CV wants far denser type than a
workbook, so nothing is shared with handout.css but the tokens.
"""

import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "cv"

ROLE = {
    "target": "Entrepreneurship Instructor (AI Training) · Alignerr / Labelbox",
    "slug": "johannes-le-roux-cv-alignerr",
}

CONTACT = [
    ("leroux.johannes@gmail.com", "mailto:leroux.johannes@gmail.com"),
    ("entrepreneurcoach.co.za", "https://www.entrepreneurcoach.co.za"),
    ("linkedin.com/in/johannesleroux", "https://www.linkedin.com/in/johannesleroux/"),
    ("Cape Town, South Africa", None),
]

PROFILE = (
    "Operator first, instructor second. I have built and sold consumer brands, "
    "and I now teach founders how to run them — which means most weeks I read "
    "business plans, models and go-to-market thinking and say plainly which "
    "parts would not survive a real market. That is the judgement this role "
    "asks for, pointed at AI output instead of a founder's deck."
)

SECTIONS = [
    ("Teaching entrepreneurship", [
        ("Entrepreneur Coach", "Founder · Cape Town",
         "One-to-one coaching and small-group workshops for owner-operators — "
         "unit economics, pricing, route to market, and the decision to commit "
         "capital or not. Founding cohorts sell out at R3,500 a seat, eight "
         "people at a time, in a market where free AI content is abundant."),
        ("UCT Graduate School of Business", "Facilitator · executive education",
         "International immersion programmes for EMBA and executive groups, "
         "including China. Programme design and company visits, working with "
         "cohorts of experienced operators, not students."),
        ("Claude for Entrepreneurs", "Three-hour applied workshop",
         "Written and run end to end: curriculum, materials, and per-attendee "
         "preparation. Each participant arrives with a real business problem "
         "and a real, messy file and leaves with a working artefact built off "
         "their own numbers. Published, repeatable, and open-sourced."),
    ]),

    ("Building and selling businesses", [
        ("The Duchess", "Co-founder · alcohol-free drinks",
         "Built from nothing to more than 10 million units sold across five "
         "countries. Retail listings, distribution and export — the full "
         "commercial arc, not the pitch-deck version of it."),
        ("Get Lucky Golf Club", "Founder · golf activation platform",
         "Hole-in-One Challenge across 30+ premium courses and 600+ golf days a "
         "year, tech-enabled with AI shot-tracing and video capture. Revenue "
         "across entry fees, sponsorship and partnerships; currently expanding "
         "beyond South Africa."),
        ("DOPE Drinks", "Founder · cannabis beverages, USA",
         "A brand built for a regulated, fast-moving US category — and useful "
         "practice at judging plans that assume regulation will behave."),
    ]),

    ("Working with AI, in practice", [
        ("Applied AI for operators", "Teaching and building",
         "I teach non-technical founders to get real work out of AI systems, "
         "and I build alongside them: retailer sales analysis across three "
         "national grocery chains, subscription viability models, project "
         "profitability tools, live commercial sites. Seventeen things shipped "
         "in a year, without being a developer."),
        ("Evaluating AI output critically", "Where this role fits",
         "The recurring job in my work is catching where a plausible-looking "
         "answer is wrong: a total that triple-counts because the file repeats "
         "each product per pack size; a subscription model that only hits its "
         "target if churn is assumed away; a forecast whose margin survives "
         "only because working capital was left out."),
    ]),
]

STRENGTHS = [
    ("Business models & venture viability",
     "Unit economics, contribution margin, working capital, break-even, "
     "channel economics."),
    ("Reading plans and decks critically",
     "Where the market sizing is wishful, where the CAC assumption is "
     "borrowed, where the plan silently needs a second raise."),
    ("Financial projections",
     "Building them, and spotting the ones that only work because something "
     "was left out."),
    ("Structured written feedback",
     "The daily work of coaching: say what is wrong, why it matters, and what "
     "to do instead."),
    ("Independent, async delivery",
     "Two businesses and a coaching practice run on self-set deadlines. "
     "Remote, task-based work is how I already operate. English and "
     "Afrikaans."),
]


def e(s):
    return html.escape(s, quote=False)


CSS = """
@import url("fonts.css");

:root {
  --paper: #FFFFFF;
  --bone: #F4F4F1;
  --ink: #0E0E10;
  --ink-soft: #2A2A2D;
  --muted: #6F6F73;
  --rule: #DEDCD5;
  --red: #F25C2A;
  --sans: "Geist", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --serif: Georgia, "Times New Roman", serif;
}

@page { size: A4; margin: 0; }

* { box-sizing: border-box; }

html, body { margin: 0; padding: 0; background: var(--paper); }

body {
  font-family: var(--sans);
  font-size: 8.2pt;
  line-height: 1.38;
  color: var(--ink-soft);
  -webkit-font-smoothing: antialiased;
}

.sheet {
  width: 210mm;
  min-height: 297mm;
  padding: 11mm 14mm 9mm;
  display: flex;
  flex-direction: column;
  gap: 4mm;
}

/* ---- masthead --------------------------------------------------------- */

header { border-bottom: 2px solid var(--ink); padding-bottom: 2.8mm; }

.name {
  font-family: var(--serif);
  font-style: italic;
  font-weight: bold;
  font-size: 23pt;
  line-height: 1;
  letter-spacing: -0.015em;
  color: var(--ink);
  margin: 0;
}
.name .dot { color: var(--red); }

.tagline {
  font-size: 9.6pt;
  color: var(--ink);
  margin: 1.6mm 0 0 0;
  font-weight: 500;
}

.target {
  font-size: 7.4pt;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--red);
  font-weight: 600;
  margin: 0 0 2mm 0;
}

.contact {
  margin: 2.6mm 0 0 0;
  font-size: 8pt;
  color: var(--muted);
}
.contact a { color: var(--muted); text-decoration: none; }
.contact span.sep { color: var(--rule); padding: 0 1.6mm; }

/* ---- profile ---------------------------------------------------------- */

.profile {
  background: var(--bone);
  padding: 3mm 3.8mm;
  font-size: 8.4pt;
  line-height: 1.46;
  color: var(--ink);
  margin: 0;
}

/* ---- sections --------------------------------------------------------- */

h2 {
  font-size: 7.4pt;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--ink);
  font-weight: 600;
  margin: 0 0 2mm 0;
  padding-bottom: 1.2mm;
  border-bottom: 1px solid var(--rule);
}

.entry { margin-bottom: 2.6mm; }
.entry:last-child { margin-bottom: 0; }

.entry .line {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 5mm;
  margin-bottom: 0.9mm;
}
.entry .org { font-weight: 600; color: var(--ink); font-size: 8.8pt; }
.entry .meta {
  color: var(--muted);
  font-size: 7.8pt;
  text-align: right;
  white-space: nowrap;
}
.entry p { margin: 0; }

/* ---- strengths grid --------------------------------------------------- */

.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2mm 7mm;
}
.grid .k { font-weight: 600; color: var(--ink); display: block; }
.grid .v { color: var(--muted); }

/* ---- foot ------------------------------------------------------------- */

footer {
  margin-top: auto;
  padding-top: 2.4mm;
  border-top: 1px solid var(--rule);
  display: flex;
  justify-content: space-between;
  font-size: 7.4pt;
  color: var(--muted);
}
footer .avail { color: var(--ink); font-weight: 600; }
"""


def contact_line():
    parts = []
    for label, href in CONTACT:
        parts.append(f'<a href="{href}">{e(label)}</a>' if href else e(label))
    return '<span class="sep">·</span>'.join(parts)


def section(title, entries):
    rows = []
    for org, meta, body in entries:
        rows.append(
            f'<div class="entry"><div class="line">'
            f'<span class="org">{e(org)}</span>'
            f'<span class="meta">{e(meta)}</span></div>'
            f"<p>{e(body)}</p></div>"
        )
    return f"<section><h2>{e(title)}</h2>{''.join(rows)}</section>"


def build():
    strengths = "".join(
        f'<div><span class="k">{e(k)}</span><span class="v">{e(v)}</span></div>'
        for k, v in STRENGTHS
    )
    body = "".join(section(t, entries) for t, entries in SECTIONS)

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Johannes le Roux — CV</title>
<link rel="stylesheet" href="cv.css"></head>
<body>
<div class="sheet">

  <header>
    <p class="target">Applying for &nbsp;·&nbsp; {e(ROLE['target'])}</p>
    <p class="name">Johannes le Roux<span class="dot">.</span></p>
    <p class="tagline">Not a coach. An operator who coaches.</p>
    <p class="contact">{contact_line()}</p>
  </header>

  <p class="profile">{e(PROFILE)}</p>

  {body}

  <section>
    <h2>What I bring to the brief</h2>
    <div class="grid">{strengths}</div>
  </section>

  <footer>
    <span class="avail">Available 10–40 hours a week · remote · UTC+2</span>
    <span>References and written samples on request</span>
  </footer>

</div>
</body></html>
"""


def find_chromium():
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(n)
        if p:
            return p
    for pat in ("chromium-*/chrome-linux/chrome",
                "chromium_headless_shell-*/chrome-linux/headless_shell"):
        f = sorted(Path("/opt/pw-browsers").glob(pat))
        if f:
            return str(f[-1])
    sys.exit("Error: no Chromium found.")


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "cv.css").write_text(CSS)
    shutil.copy(ROOT / "handouts" / "fonts.css", OUT / "fonts.css")

    html_path = OUT / f"{ROLE['slug']}.html"
    pdf_path = OUT / f"{ROLE['slug']}.pdf"
    html_path.write_text(build())
    subprocess.run(
        [find_chromium(), "--headless", "--disable-gpu", "--no-sandbox",
         "--no-pdf-header-footer", "--virtual-time-budget=4000",
         f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, capture_output=True,
    )
    print(f"  {pdf_path.relative_to(ROOT)}  ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
