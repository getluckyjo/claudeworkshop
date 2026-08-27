#!/usr/bin/env python3
"""Build the remote version of the workshop — one workbook per person.

    ./scripts/build-remote.py

The in-person workbook (build-handouts.py) assumes a facilitator in the room:
short prompts, deliberate gaps, and someone to ask when a build goes sideways.
Remote has none of that, so these carry the whole sequence written out, the
snags named in advance, and an honest note about what the tool will not do.

Liezl was the first, run out of the 22 August cohort. This exists so the second
one didn't have to be bolted onto that cohort's build.

Everything lands in handouts/remote/.
"""

import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "handouts" / "remote"

SKILL_URL = "https://github.com/getluckyjo/claudeworkshop/raw/HEAD/dist/entrepreneurcoach.zip"


# --------------------------------------------------------------------------
# The people running it alone.
# --------------------------------------------------------------------------

PEOPLE = [
    {
        "slug": "inus",
        "name": "Inus Smuts",
        "business": "Platō Coffee Group",
        "role": "Creative Director",
        "bringing": (
            "A Shopify site for a new brand — one of the group's, not Platō "
            "itself. The design and the build, not the product copy."
        ),
        "building": "Design it by asking",
        "why": (
            "The products are the easy half and you know it. What you actually "
            "want is to change how the thing looks and works without waiting on "
            "a developer or fighting a theme editor that won't do the layout in "
            "your head. That is buildable, it needs no terminal, and by the end "
            "of this you should have changed something on a storefront yourself "
            "and watched it appear."
        ),

        "cannot": {
            "label": "Three jobs wearing one coat",
            "body": (
                "\u201cBuild a Shopify site\u201d is three different jobs, and "
                "they have nothing in common. <strong>The store setup</strong> — "
                "plan, payments, domain, shipping zones, tax — is you in the "
                "admin, clicking. Nothing here changes that. <strong>The "
                "products</strong> are copy and a CSV, or a direct connection if "
                "someone sets up an Admin API token; either way it's an "
                "afternoon and you've said it's the easy part.\n\n"
                "<strong>The third is the theme</strong> — layout, sections, how "
                "it looks and moves. That's the one worth your three hours, and "
                "it's the one people assume is off the table. It isn't."
            ),
        },

        "routes": {
            "title": "The loop, and why there's no terminal in it",
            "intro": ("A Shopify theme is a folder of files. Shopify publishes a "
                      "GitHub app that keeps a repository branch and a theme in "
                      "sync — push to the branch and the theme updates; edit in "
                      "the admin and it commits back. Put Claude on the "
                      "repository and the whole build becomes: ask for a change, "
                      "look at it, merge it, see it in the preview."),
            "options": [
                ("Set it up once",
                 "In Shopify: Online Store &rarr; Themes &rarr; duplicate the "
                 "theme you're working from. Connect the GitHub branch to <em>that "
                 "duplicate</em>, never the live one. Then go to claude.ai/code, "
                 "sign in with the same Claude account, connect GitHub, and open "
                 "the repository.",
                 "Twenty minutes, all of it clicking. The one thing to get right "
                 "is which theme the branch points at — the integration syncs to "
                 "whatever it's told, and pointing it at the live theme makes "
                 "every merge a deployment to customers. Claude Code on the web "
                 "needs Pro or Max, and it's a research preview, so treat it as "
                 "very good rather than bulletproof."),
                ("Then ask for sections, not pages",
                 "A section with a proper schema block shows up in the theme "
                 "editor with its own controls — heading, image, alignment, "
                 "full-bleed or not, whatever you specify.",
                 "This is the part worth reading twice. Ask for <em>a homepage</em> "
                 "and you get a fixed thing only Claude can change. Ask for <em>a "
                 "section with settings</em> and you get a new control in your own "
                 "editor that you design with afterwards, forever, without asking "
                 "anyone. You're not commissioning pages. You're building "
                 "yourself a control panel."),
            ],
            "verdict": ("One rule above all others: <strong>work on a duplicate.</strong> "
                        "A storefront taking orders is production. Nothing you do "
                        "in the next three hours should be able to touch what a "
                        "customer sees, and with an unpublished theme it can't."),
        },

        "needs": [
            "Access to the Shopify store, and a theme you're allowed to duplicate",
            "A GitHub account — free, and use a personal username rather than a "
            "company one; you'll launch more than one brand",
            "The brand: logo, fonts, colours, and whatever art direction exists "
            "even if it's a moodboard",
            "Three sites you'd be pleased to have made, and one you can't stand. "
            "The one you hate is worth more than the three you like",
            "Which theme the store is on. Dawn and Horizon behave differently and "
            "it changes what to ask for",
        ],

        "repeats": (
            "A skill carrying the brand's design rules — spacing, type scale, how "
            "it writes headings, what it never does. Then every new section "
            "arrives already looking like the brand instead of needing to be "
            "argued into it."
        ),

        "sequence": {
            "title": "The five steps",
            "intro": (
                "Roughly three hours, or three sittings. Be honest with yourself "
                "about the finish line: what you want by the end is the loop "
                "working and one section you built and then adjusted yourself. "
                "That's the moment it clicks. A whole storefront is the week "
                "after, and it goes fast once the loop exists."
            ),
            "steps": [
                ("Give it the eye before the work",
                 "Here's the brand — logo, fonts, colours, the moodboard. Here "
                 "are three sites I'd be proud of and one I can't stand. Tell me "
                 "what you think the visual rules are, and where I'm "
                 "contradicting myself.",
                 "Do this before anything is built. The last clause is the "
                 "valuable one — it's the closest thing to a second art director "
                 "in the room, and it will find the contradiction you've been "
                 "carrying since the pitch. Argue with it. Write down what you "
                 "settle on."),

                ("Wire the loop up",
                 "Walk me through connecting a Shopify theme to GitHub and then "
                 "to Claude Code, so I can change the theme by asking. I'm "
                 "duplicating the theme first and I am not touching the live one.",
                 "Twenty minutes of clicking, and the only step that matters is "
                 "pointing the branch at the duplicate. Once this works, "
                 "everything after it is conversation."),

                ("One section, built properly",
                 "Build me one section with a full schema block — settings for "
                 "the heading, the image, the alignment and whether it runs "
                 "full-bleed. Before you write any Liquid, tell me which theme "
                 "objects and filters you're relying on and which theme "
                 "architecture you're assuming.",
                 "That second sentence is doing real work: Liquid is where it "
                 "will invent a filter that doesn't exist, and asking it to state "
                 "its assumptions first surfaces the wrong one while it's still "
                 "cheap. Then merge it, open the theme editor, and move the "
                 "controls around. That is the whole point of the day."),

                ("Now the storefront",
                 "Same rules, the rest of it: the homepage, the product page, the "
                 "collection page. Sections with settings, not fixed layouts. "
                 "Show me each one before you move on.",
                 "Look at everything on a phone before you like it. Most coffee "
                 "gets bought on a phone in a queue, and a layout that sings on "
                 "your 27-inch monitor can be unusable at 390 pixels."),

                ("Make it repeat",
                 "Write the brand's design rules up as a skill — spacing, type "
                 "scale, how headings are written, what this brand never does — "
                 "so the next section arrives already right.",
                 "Name it after the brand, not after Platō. You'll launch another "
                 "one, and the rules should travel with the brand they belong to."),
            ],
        },

        "watch": (
            "Two things will cost you the afternoon. The first is editing in the "
            "theme editor while Claude is working on the same files — the sync "
            "runs both ways, so that's a real conflict. One or the other at a "
            "time. The second is the pull toward polish: you'll want to perfect "
            "the hero before the loop is even working. Get the loop working "
            "first, on something ugly. Ugly and live beats beautiful and "
            "theoretical, and you can make it beautiful in about four minutes "
            "once you can change it by asking."
        ),

        "closing": (
            "You're doing this without me in the room, so one ask: when something "
            "doesn't work, write down what you asked and what came back before "
            "you work around it. That list is worth more to the next version of "
            "this than anything that went smoothly."
        ),
    },
]


BRANDMARK = """<div class="brandmark">
    <span class="name">Johannes le Roux</span><span class="dot"></span>
    <span class="role">Entrepreneur Coach</span>
  </div>"""


def e(s):
    return html.escape(s, quote=False)


def head(title):
    return (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            f"<title>{e(title)}</title>\n"
            f'<link rel="stylesheet" href="../handout.css">\n</head>\n<body>\n')


def lines(n, short=False):
    cls = "lines short" if short else "lines"
    return f'<div class="{cls}">' + "<div></div>" * n + "</div>"


DELIVERABLES = [
    ("A Project that knows the brand", "Its documents, its rules, its voice — in one place that outlives the chat."),
    ("One real artefact", "A file you can use, off your own product list."),
    ("A skill that repeats it", "So the next one costs a fraction of the first."),
    ("One job running on a schedule", "The first thing that happens without you."),
]


def deliverables_list():
    items = "".join(f"<li><b>{e(t)}</b><span>{e(d)}</span></li>" for t, d in DELIVERABLES)
    return f'<ol class="deliverables">{items}</ol>'


def sequence_pages(seq):
    """Five steps, split across two pages so nothing is cramped."""
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
    <p class="small" style="margin:0">{note}</p>
  </div>""")

    return f"""
<section class="page">
  <h2>{e(seq['title'])}</h2>
  <p class="standfirst">{e(seq['intro'])}</p>
  {''.join(blocks[:2])}
</section>

<section class="page">
  {''.join(blocks[2:])}
</section>"""


def routes_page(p):
    r = p.get("routes")
    if not r:
        return ""
    blocks = []
    for i, (name, what, note) in enumerate(r["options"], 1):
        blocks.append(f"""
  <div style="margin-bottom:7mm">
    <p style="font-family:var(--display);font-size:9.5pt;font-weight:600;
       letter-spacing:var(--tracking-tight);margin:0 0 2mm 0">
      <span style="color:var(--red)">{i}</span>&nbsp;&nbsp;{e(name)}</p>
    <p style="margin:0 0 2mm 0">{what}</p>
    <p class="small" style="margin:0">{note}</p>
  </div>""")
    return f"""
<section class="page">
  <h2>{e(r['title'])}</h2>
  <p class="standfirst">{e(r['intro'])}</p>
  {''.join(blocks)}
  <div class="callout">
    <p>{r['verdict']}</p>
  </div>
</section>"""


def workbook(p):
    needs = "".join(f"<li>{e(n)}</li>" for n in p["needs"])
    cannot = p["cannot"]
    cannot_body = "".join(f"<p>{para}</p>" for para in cannot["body"].split("\n\n"))

    return head(f"Remote workbook — {p['name']}") + f"""
<section class="page cover">
  {BRANDMARK}
  <h1>Claude for<br><em>entrepreneurs.</em></h1>
  <div class="hero-rule"></div>
  <p class="lede">The remote version. Your own time, your own laptop, one real
  thing at the end of it.</p>

  <div class="namecard">
    <p class="who">{e(p['name'])}</p>
    <p class="what">{e(p['role'])} &nbsp;·&nbsp; {e(p['business'])}</p>
  </div>

  <div class="quoteblock">
    <p class="label">What you're bringing</p>
    <p>{e(p['bringing'])}</p>
  </div>

  <div class="coverfoot">
    <span>Run it in your own time &nbsp;·&nbsp; about 3 hours</span>
    <span>leroux.johannes@gmail.com</span>
  </div>
</section>

<section class="page">
  <h2>Before you start</h2>
  <p class="standfirst">Twenty minutes of setup. Do it the night before rather
  than at the top of the session — the one thing that reliably ruins a solo run
  is spending the first hour on an account problem.</p>

  <h3>1. A paid Claude plan</h3>
  <p>About R400 a month, billed by Anthropic. Then install the <strong>desktop
  app</strong>, not just the browser — the file handling is better and you'll be
  moving files. If your card declines it's almost always your bank blocking the
  international payment; enable that in your banking app and try again.</p>

  <h3>2. Add the workshop skill</h3>
  <p>Download it, and <strong>don't unzip it</strong>:</p>
  <p class="small" style="word-break:break-all">{SKILL_URL}</p>
  <p>In Claude: click your name bottom-left → Settings → Customize → Skills →
  upload the zip. You'll know it worked when <strong>Entrepreneur Coach</strong>
  appears in your list. Then open a <em>new</em> chat and type
  <em>help me get set up</em> — skills don't load into a conversation that was
  already running.</p>

  <h3>3. Have your material to hand</h3>
  <ul>{needs}</ul>

  <div class="note">
    <p class="label">One rule</p>
    <p>You won't be asked to write code, open a terminal, or install anything
    beyond the app. If a step ever seems to need it, that means the session has
    taken a wrong turn — not that you've missed something. Mail me.</p>
  </div>
</section>

<section class="page">
  <h2>What you walk out with</h2>
  <p class="standfirst">Four things, running on your own machine. Not notes about
  how you might do it later.</p>
  {deliverables_list()}

  <h3>Briefing, not prompting</h3>
  <p>The single biggest difference between people who find this underwhelming and
  people who don't. A prompt asks for a thing. A brief says what you're trying to
  achieve and hands over what's needed to do it.</p>
  <ol class="tight">
    <li><strong>The job.</strong> What you want done, and why it matters.</li>
    <li><strong>The context.</strong> The brand, the constraints, the deadline.</li>
    <li><strong>The material.</strong> The real file. Not a description of it.</li>
    <li><strong>What good looks like.</strong> How you'd know it was done properly.</li>
    <li><strong>The format.</strong> A spreadsheet, a page, a document, a file.</li>
  </ol>

  <div class="callout">
    <p><strong>Working alone, the failure mode is politeness.</strong> In a room
    I'd tell you to reject a bad answer out loud and say exactly what's wrong
    with it. On your own it's tempting to quietly fix it yourself and move on —
    which teaches it nothing, and you pay for the same flaw again on the next
    one. Say what's wrong. It's faster.</p>
  </div>
</section>

<section class="page">
  <h2>{e(p['building'])}</h2>
  <p class="standfirst">{e(p['why'])}</p>

  <div class="note">
    <p class="label">{e(cannot['label'])}</p>
    {cannot_body}
  </div>

  <h3>What repeats afterwards</h3>
  <p>{e(p['repeats'])}</p>

  <div class="note">
    <p class="label">Watch for</p>
    <p>{e(p['watch'])}</p>
  </div>
</section>
{routes_page(p)}
{sequence_pages(p['sequence'])}

<section class="page">
  <h2>Before you finish</h2>
  <p class="standfirst">Most training evaporates inside a fortnight, and solo
  runs evaporate faster because nobody asks you about it on the Monday. This is
  the page that decides whether yours does.</p>

  <div class="write">
    <p class="prompt">The brand's voice, in one sentence I'd defend in a meeting</p>
    {lines(2, short=True)}
  </div>

  <div class="write">
    <p class="prompt">What I built, and where it lives</p>
    {lines(3, short=True)}
  </div>

  <div class="write">
    <p class="prompt">What broke, or came back wrong — the useful list</p>
    {lines(5)}
  </div>

  <div class="write">
    <p class="prompt">The one thing I'll do by Friday</p>
    {lines(2, short=True)}
  </div>

  <h3>Then</h3>
  <p>{e(p['closing'])}</p>

  <p class="signature" style="margin-top:8mm">Johannes</p>

  <div class="coverfoot" style="margin-top:4mm">
    <span>Entrepreneur Coach</span>
    <span>leroux.johannes@gmail.com</span>
  </div>
</section>
</body></html>
"""


def find_chromium():
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        path = shutil.which(n)
        if path:
            return path
    for pattern in ("chromium-*/chrome-linux/chrome",
                    "chromium_headless_shell-*/chrome-linux/headless_shell"):
        found = sorted(Path("/opt/pw-browsers").glob(pattern))
        if found:
            return str(found[-1])
    sys.exit("Error: no Chromium found — can't render PDFs.")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    chrome = find_chromium()

    for p in PEOPLE:
        html_path = OUT / f"workbook-{p['slug']}.html"
        pdf_path = OUT / f"workbook-{p['slug']}.pdf"
        html_path.write_text(workbook(p))
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", "--virtual-time-budget=4000",
             f"--print-to-pdf={pdf_path}", html_path.as_uri()],
            check=True, capture_output=True,
        )
        print(f"  {pdf_path.relative_to(ROOT)}  ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
