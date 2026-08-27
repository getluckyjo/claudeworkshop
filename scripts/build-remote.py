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
            "itself."
        ),
        "building": "The launch, minus the typing",
        "why": (
            "You already know what the brand is. What stands between you and "
            "live is a few thousand words of product copy, SEO fields and "
            "policy pages that nobody enjoys writing and everybody writes "
            "badly under deadline. That is the part we hand over — in the "
            "brand's voice, decided by you once and applied everywhere."
        ),

        # The honest limit, named up front rather than discovered at minute 30.
        "cannot": {
            "label": "What this will not do, so you can stop waiting for it",
            "body": (
                "It will not build your Shopify store. Shopify is an admin you "
                "log into — the theme, the payment setup, the domain and the "
                "navigation are yours to click through, and no amount of asking "
                "changes that. Anyone who tells you otherwise is selling "
                "something.\n\n"
                "What it will do is produce everything that goes <em>into</em> "
                "the store, in a file Shopify imports directly. That is the "
                "part that actually costs a launch three weeks."
            ),
        },

        "needs": [
            "The new brand — name, what it is, who it's for, and how it's "
            "different from Platō. A paragraph is plenty; it doesn't need to be "
            "the finished positioning",
            "Your product list, however rough. Names, sizes, variants, prices, "
            "cost if you have it. A spreadsheet, a WhatsApp voice note "
            "transcribed, the back of an envelope — all fine",
            "Three or four things already written in the brand's voice. Even a "
            "packaging back-panel or a caption. This is the one that decides "
            "whether the output sounds like the brand or like a template",
            "Product photos, if they exist. Not required to start",
            "Your Platō copy, for contrast — so it can hear what to move away from",
        ],

        "repeats": (
            "A brand voice skill, so product forty costs what product one did. "
            "Then the same skill writes the launch emails, the collection "
            "descriptions and the social captions without being re-briefed each "
            "time."
        ),

        "sequence": {
            "title": "The five steps",
            "intro": (
                "Do them in order. Step 1 looks like the soft one and it is the "
                "one everything else rests on — skip it and steps 2 to 5 produce "
                "competent copy for a brand that could be anyone's. Each grey "
                "box is what to ask. Allow about three hours, or three sittings "
                "of an hour."
            ),
            "steps": [
                ("Write the voice down first",
                 "Here's the new brand — what it is, who it's for, how it "
                 "differs from Platō. Here are four things already written in "
                 "its voice, and here's some Platō copy for contrast. "
                 "Interview me until you could write as this brand yourself.",
                 "Let it ask questions and answer them properly. When it thinks "
                 "it has the voice, make it prove it: give it a product it has "
                 "never seen and ask for fifty words. If that comes back sounding "
                 "like the brand, you have something. If it comes back sounding "
                 "like a coffee brand, keep going — that's the gap you're paid to "
                 "close."),

                ("One product, argued over",
                 "Take one product from my list. Write the title, the "
                 "description, the SEO title and meta description, the tags, and "
                 "the image alt text. Show me your reasoning on the title.",
                 "Push back on this one until it's genuinely right — you're not "
                 "reviewing a product, you're setting the pattern the other "
                 "thirty-nine inherit. Ten minutes here saves an afternoon of "
                 "fixing the same flaw forty times."),

                ("The whole range, as a file Shopify eats",
                 "Now do the rest of the range the same way, and give me a "
                 "Shopify product import CSV — Handle, Title, Body (HTML), "
                 "Vendor, Type, Tags, Published, Option1 Name, Option1 Value, "
                 "Variant SKU, Variant Price, Variant Inventory Qty, Image Src, "
                 "Image Alt Text, SEO Title, SEO Description, Status.",
                 "Shopify → Products → Import takes that file directly. Import "
                 "into a <em>development</em> store first, or tick nothing as "
                 "published — either way you look at it in the admin before it can "
                 "be seen. Expect to reject a few. Reject them out loud and say "
                 "why, so the fix carries."),

                ("The pages nobody wants to write",
                 "Same voice: the About page, shipping, returns, FAQ, and the "
                 "three-email welcome flow for someone who has just bought for "
                 "the first time.",
                 "Give it your real terms — actual delivery times, the real "
                 "returns window, what happens if a bag arrives damaged. Invented "
                 "policy is a legal problem, not a copy problem, and it will "
                 "invent cheerfully if you leave a gap."),

                ("Make it repeat",
                 "That worked. Write it up as a skill so I can add a product "
                 "next month without explaining the brand again.",
                 "This is the step that turns three hours into an asset. Name it "
                 "after the brand, not after Platō — you'll launch another one, "
                 "and the voice should travel with the brand it belongs to."),
            ],
        },

        "watch": (
            "Two things will try to eat your afternoon. The first is the store "
            "itself — the theme, the fonts, the hero image. You're a creative "
            "director; that pull is real and it is not what this session is for. "
            "The second is doing the range before the voice. Both roads end with "
            "forty products that read like a template, and re-doing them costs "
            "more than doing them slowly once."
        ),

        "closing": (
            "You're doing this without me in the room, so one ask: when you hit "
            "something that doesn't work, write down what you asked and what came "
            "back before you work around it. That list is worth more to the next "
            "version of this than anything that went smoothly."
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
