#!/usr/bin/env python3
"""Build the day-one asset pack — the thing every attendee was promised.

    ./scripts/build-assetpack.py

Deliberately does NOT contain anyone's own skill. Those were written live in
block 8 off whatever had just worked, so they exist on seven laptops and
nowhere else. Promising them back would mean inventing them. Instead the pack
carries the parts that are the same for everyone — the Project template, the
prompt library, and how to rebuild or extend a skill on their own — and says
plainly that their skill is theirs to keep going.

Reuses handouts/handout.css, so it looks like the workbooks they already have.
"""

import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assetpack"
DATE = "Saturday 22 August 2026"
CALL = "Friday 4 September, 10:00"


def e(s):
    return html.escape(s, quote=False)


def head(title):
    return (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            f"<title>{e(title)}</title>\n"
            f'<link rel="stylesheet" href="handout.css">\n</head>\n<body>\n')


BRANDMARK = """<div class="brandmark">
    <span class="name">Johannes le Roux</span><span class="dot"></span>
    <span class="role">Entrepreneur Coach</span>
  </div>"""


def prompts(title, standfirst, groups):
    """A page of prompts. groups is [(heading, [(prompt, note), ...]), ...]."""
    out = []
    for heading, items in groups:
        out.append(f"<h3>{e(heading)}</h3>")
        for prompt, note in items:
            out.append(
                '<div style="background:var(--bone);padding:3.5mm 4.5mm;margin:0 0 1.5mm 0">'
                f'<p style="margin:0;font-size:10pt">&ldquo;{e(prompt)}&rdquo;</p></div>'
                f'<p class="small" style="margin:0 0 5mm 0">{e(note)}</p>'
            )
    return (f'<section class="page">\n<h2>{title}</h2>\n'
            f'<p class="standfirst">{e(standfirst)}</p>\n' + "\n".join(out) + "\n</section>\n")


# --------------------------------------------------------------------------
# The prompt library. Everything here was either used in the room or is the
# prompt someone needed and didn't have. Nothing aspirational.
# --------------------------------------------------------------------------

LIBRARY = [
    ("Briefing instead of prompting", [
        ("Here's what I'm trying to achieve, here's my business, here's the "
         "actual file, and here's how I'd know it was done properly. Ask me "
         "what's missing before you start.",
         "The whole of block 3 in one line. The last sentence is the part "
         "people leave off, and it's the part that saves the round trip."),
        ("Before you answer, tell me what you'd need from me to do this "
         "properly.",
         "Use it when an answer comes back thin. Nine times out of ten the "
         "problem was the brief, not the model."),
        ("That's not it. Here's what's wrong with it, specifically.",
         "Correcting is faster than re-prompting. Say what's wrong rather than "
         "asking again in different words."),
    ]),
    ("Working with your own files", [
        ("Here's the export. Before you analyse anything, tell me what's in it "
         "— what each column means, what the row count is, and what looks "
         "wrong or inconsistent.",
         "Always do this first with a file you haven't used before. Every "
         "real-world export has a trap in it and this is how you find it "
         "before it's baked into a number."),
        ("What in this file would give me a wrong answer if I wasn't careful?",
         "Blanks that mean 'not applicable' rather than zero, repeated rows, "
         "totals mixed in with detail. Ask it directly."),
        ("Reconcile your total against the total in the file itself, and tell "
         "me if they don't match.",
         "The single most useful sentence in this library if you work with "
         "numbers. Never accept a figure that hasn't been checked against "
         "something the file already says."),
    ]),
    ("Making it a real thing", [
        ("Don't give me this in the chat. Make it a file I can open and send.",
         "Spreadsheet, document, deck, page. Chat text isn't a deliverable and "
         "asking is all it takes."),
        ("Build it so I can change the assumptions and everything updates.",
         "The difference between a number and a model. Ask for it explicitly "
         "or you'll get a snapshot."),
        ("Now change one assumption and show me what it does to the answer.",
         "This is the moment it stops being a document and starts being a "
         "tool. Do it once and you'll never accept a static file again."),
    ]),
    ("Getting it to sound like you", [
        ("Here are three things I've actually written. Use these, not a "
         "professional register.",
         "Real samples beat any amount of describing your tone. Raw is better "
         "than polished — send the WhatsApp, not the press release."),
        ("Read that back and tell me which parts sound like a machine wrote "
         "them. Then fix those.",
         "Works better than asking it to 'sound more human', which produces a "
         "different kind of machine."),
        ("Shorter. Take out anything I wouldn't say out loud.",
         "The most-used prompt in the room on Saturday, by a distance."),
    ]),
    ("Making it repeat", [
        ("That worked. Write it up as a skill so I can do it again next month "
         "without explaining it.",
         "Say this the moment something works, while the steps are still in "
         "front of you. That's how every skill in the room got made."),
        ("Every Monday at 07:00, do this and send me three lines and what I "
         "should do about it.",
         "You never need a menu to set up a schedule — just ask. The three "
         "lines matter: a scheduled job that writes an essay gets ignored "
         "inside a fortnight."),
        ("Run it once now so I can see what Monday will actually look like.",
         "Fire it immediately rather than waiting a week to discover it's "
         "wrong."),
    ]),
    ("When you're stuck", [
        ("Tell me what you think I'm actually trying to do here, before you do "
         "anything.",
         "Cheapest way to catch a wrong turn. If its answer surprises you, "
         "that's the problem found."),
        ("What's the simplest version of this that would still be useful to me "
         "on Monday?",
         "For when the thing you asked for has grown three heads."),
        ("What am I not asking you that I should be?",
         "Worth running at the end of any real piece of work."),
    ]),
]


PROJECT_TEMPLATE = """# Project instructions — fill this in

Paste this into your Project's instructions and replace everything in
angle brackets. Delete any line you have no real answer for. An empty
section is worse than a missing one, because it invites invention.

---

This project is <the business, in one sentence a stranger would understand>.

I am <your name>, <your role>. I sell <what you actually sell> to <who
actually signs — the specific person, not "small businesses">.

## What matters in this business

- <the number you'd check first on a Monday morning>
- <the thing that goes wrong most often>
- <what "good" looks like, and what you'd reject out of hand>

## How I want you to work with me

- <plain language / no jargon / short answers / show your working — pick
  what's true for you>
- Give me files I can open and send, not answers in the chat, unless I
  say otherwise
- If you need something from me to do the job properly, ask before you
  start
- If you're not sure, say so. Don't fill the gap with something
  plausible
- <how you write: sign-off, language, anything that makes you cringe>

## What's in here

<list the documents you've loaded, and what each one is for>

---

## What to actually load in

The Project is only worth what you put in it. Most people add a logo and
stop, then wonder why it doesn't feel like much.

  [ ] Your pricing, service list and standard terms
  [ ] The real, messy file you brought on Saturday
  [ ] Last year's numbers, or the current model
  [ ] Two or three things you've written yourself, so it has your voice
  [ ] Logo, product photos, an old deck or brochure

Then start a chat inside the Project and ask it something only your
business would know. That's the proof.

## The one habit that makes this stick

Start your work inside the Project, not in a blank chat. Everything you
loaded is sitting in there, and a blank chat knows none of it. This is
the single thing that separates the people it works for from the people
it doesn't.
"""


def cover():
    return head("Asset pack") + f"""
<section class="page cover">
  {BRANDMARK}
  <h1>The asset<br><em>pack.</em></h1>
  <div class="hero-rule"></div>
  <p class="lede">What was the same for everyone on Saturday, written down so you
  can use it without me in the room.</p>

  <div class="namecard">
    <p class="who">Claude for entrepreneurs</p>
    <p class="what">{e(DATE)} &nbsp;·&nbsp; CHIPS, Gardens</p>
  </div>

  <div class="quoteblock">
    <p class="label">Your own skill isn't in here</p>
    <p>On purpose. Everyone's was written live off whatever had just worked, so
    they're all different and they live on your laptop, not mine. Handing you a
    generic one back would be worse than useless.</p>
    <p>What's in here instead is how to rebuild it, extend it, or write the next
    one — page 4.</p>
  </div>

  <div class="coverfoot">
    <span>14-day call &nbsp;·&nbsp; {e(CALL)}</span>
    <span>leroux.johannes@gmail.com</span>
  </div>
</section>

<section class="page">
  <h2>What's in here</h2>
  <p class="standfirst">Five things. The first one is the one that decides
  whether any of this survives the fortnight.</p>

  <ol class="deliverables">
    <li><b>Project instructions — a template</b><span>A text file to paste into
      your Project and fill in, plus the list of what to load in beside it. This
      is the one to do first.</span></li>
    <li><b>The prompt library</b><span>Eighteen prompts that did real work on the
      day, grouped by what they're for. Not a list of clever tricks — the ones
      you'll actually reach for.</span></li>
    <li><b>Writing your own skill</b><span>The interview questions, the rules
      that separate a skill that works from one that gets ignored, and the
      no-file way to install it.</span></li>
    <li><b>The cheat sheet</b><span>The same one from Saturday. Where every
      screen lives, and what to do when something breaks.</span></li>
    <li><b>The workshop skill</b><span>The zip you installed as pre-work. Keep
      it — it's how you pick up any station you want to run again.</span></li>
  </ol>

  <div class="note">
    <p class="label">Do one thing</p>
    <p>Not three. The people this works for are the ones who used it on the
    Monday, not the ones with the longest list. If you only do one thing out of
    this pack, fill in the Project instructions and put your real documents
    behind them.</p>
  </div>

  <div class="callout">
    <p><strong>The 14-day call is {e(CALL)}, online.</strong> One win and one
    blocker each. Come with something you actually tried, even if it broke —
    especially if it broke.</p>
  </div>
</section>
"""


def skill_page():
    return """
<section class="page">
  <h2>Writing your own <em>skill</em></h2>
  <p class="standfirst">Yours evolved in the room and it's yours to keep going.
  This is how to rebuild it, extend it, or write the next one — and there will be
  a next one, because the second is always easier than the first.</p>

  <h3>Two kinds, and they're not the same job</h3>
  <ul>
    <li><strong>A voice skill</strong> teaches Claude how you write. Name it
    after <em>you</em> — <kbd>sarah-voice</kbd>, not <kbd>company-voice</kbd>.
    You'll run more than one business; your voice moves with you.</li>
    <li><strong>A process skill</strong> teaches Claude a job you do over and
    over. Name it after <em>the job</em> — <kbd>month-end-pack</kbd>,
    <kbd>weekly-numbers</kbd>, <kbd>client-quote</kbd> — because that's what
    you'll look for when you want it.</li>
  </ul>

  <h3>The interview, if you're doing a voice skill</h3>
  <p>Answer these in a chat and ask Claude to turn them into a skill.</p>
  <ol class="tight">
    <li>What's the business, and what do you actually sell?</li>
    <li>Who's the customer? The specific person who signs, not a category</li>
    <li>What have you built before?</li>
    <li>Who are you usually writing to?</li>
    <li>What's your sign-off?</li>
    <li>What makes you cringe when you see it in your own writing?</li>
    <li>Do you write in more than one language? Say so, and say that you mix
    English business terms in. That's authentic — don't let it tidy that away</li>
    <li><strong>Paste in two or three things you've actually written.</strong>
    An email, a WhatsApp to a client, a LinkedIn post. Raw beats polished</li>
  </ol>
  <p><strong>Question 8 is worth more than the other seven put together.</strong>
  A single real email beats a paragraph of describing yourself.</p>

  <h3>What separates one that works from one that gets ignored</h3>
  <ul class="tight">
    <li><strong>Quote your actual sentences.</strong> Five real phrases beat any
    amount of adjectives</li>
    <li><strong>Be specific about what to avoid.</strong> "Don't be corporate" is
    useless. "Never open with <em>I hope this email finds you well</em>" is
    something it can act on</li>
    <li><strong>Say when it should fire.</strong> The description is all Claude
    sees when deciding whether to use it, so list the situations</li>
    <li><strong>Keep it under 150 lines.</strong> Long ones get skimmed, sharp
    ones get followed</li>
    <li><strong>Invent nothing.</strong> Leave out what you don't know. A blank
    section invites it to make something up</li>
  </ul>

  <div class="note">
    <p class="label">Installing it without touching a file</p>
    <p>You can't zip a file without a terminal, and you don't need to. Open a new
    chat and say: <em>"Create a skill for me from this"</em>, then paste the text
    in. Claude builds and installs it in the conversation. That's the whole
    thing — the upload route is for when someone hands you a file.</p>
  </div>

  <div class="callout">
    <p><strong>Test it on the real job, immediately.</strong> Not a demo of it —
    the actual thing you need to write or run this week. There will be something
    to fix, there always is, usually that it's too long or it invented a step you
    don't do. Fix it once and it's done. It's a text file you own, and you can
    change it whenever the business does.</p>
  </div>
</section>
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
    sys.exit("Error: no Chromium found — can't render PDFs.")


def main():
    OUT.mkdir(exist_ok=True)
    for asset in ("handout.css", "fonts.css"):
        shutil.copy(ROOT / "handouts" / asset, OUT / asset)
    if (ROOT / "handouts" / "fonts").is_dir():
        shutil.copytree(ROOT / "handouts" / "fonts", OUT / "fonts", dirs_exist_ok=True)

    body = (cover()
            + prompts("The prompt <em>library</em>",
                      "Everything here either did real work on Saturday or is the "
                      "prompt somebody needed and didn't have. Nothing aspirational.",
                      LIBRARY)
            + skill_page()
            + "</body></html>\n")

    html_path = OUT / "asset-pack.html"
    pdf_path = OUT / "Asset pack.pdf"
    html_path.write_text(body)
    subprocess.run([find_chromium(), "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--virtual-time-budget=4000",
                    f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                   check=True, capture_output=True)
    (OUT / "Project instructions — template.md").write_text(PROJECT_TEMPLATE)
    print(f"  {pdf_path.relative_to(ROOT)}  ({pdf_path.stat().st_size // 1024} KB)")
    print(f"  {(OUT / 'Project instructions — template.md').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
