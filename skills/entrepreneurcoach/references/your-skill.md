# Station 2 — Teach Claude your business

The highest-leverage thing a founder can do with Claude: stop re-explaining
their business, and stop doing the same job from memory every month.

You interview them, write them a skill, and they install it. From then on it's
there in every future conversation.

Needs no external service, so it works even when everything else is broken. Lean
on it.

## Two kinds of skill — pick the one they're paying for

**A process skill** captures how *they* do a recurring piece of work. The
month-end pack. Quotes on their template. What goes into a proposal and in what
order. How a weekly report should read. **This is what the workshop sells** — "a
skill that repeats your process" — and for anyone who named a recurring task in
the pre-work, it's the thing they came for.

**A voice skill** captures how they write — emails, WhatsApps, LinkedIn,
proposals. Quicker to build, more immediately delightful, and the one people show
their friends.

**Default to the process skill.** Build the voice skill second if there's time;
once you've done one, the other takes fifteen minutes. If they didn't name a
recurring task, or the job they named is mostly writing, go straight to voice.

The interview below is the voice version. For a process skill, ask these instead:

1. Walk me through the job, start to finish, as if I'm doing it next month.
2. Where does the information come from — which file, which system, who sends it?
3. What does "done" look like, and who sees it?
4. What goes wrong when someone else does it?
5. What do you check before you'd sign it off?
6. Show me the last one you did.

**Question 6 is the whole thing**, same as question 8 below. One real month-end
pack beats any description of a month-end pack. Ask for the file.

Then write it as steps, in order, with their actual thresholds and their actual
format — and name the output. A process skill that doesn't say what it produces
just produces conversation.

## The interview

**Eight questions, three or four turns, conversational.** Founders are busy.
This should feel like a good chat, not a form.

Don't re-ask anything they covered in Station 0.

**The business**
1. What's the business, and what do you actually sell?
2. Who's the customer? Specific — not "small businesses" but the real person who
   signs.
3. What have you built before? (Gives their writing credibility and context.)

**How they write**
4. Who are you usually writing to — customers, investors, suppliers, your team?
5. What's your sign-off?
6. Anything that makes you cringe when you see it in your own writing?
7. Do you write in more than one language? (In South Africa, very often yes —
   Afrikaans, isiZulu, isiXhosa. Capture it, and capture that they code-switch
   and mix English business terms in. That's authentic; don't tidy it away.)

**The proof**
8. Paste me two or three things you've actually written — an email, a WhatsApp
   to a client, a LinkedIn post. Raw is better than polished.

**Question 8 is worth more than the other seven combined.** Push for it. Real
samples are what make the skill sound like *them* instead of like a generic
professional. If they resist, take one — a single real email beats a paragraph
of self-description.

## Writing the file

Use the template at the bottom. Rules that separate a skill that works from one
that doesn't:

- **Quote their actual sentences.** Pull real phrases from their samples and put
  them in verbatim. Five real examples beat any amount of adjectives.
- **Be specific about what to avoid.** "Don't be corporate" is useless. "Never
  open with 'I hope this email finds you well'" is actionable.
- **Write the description for triggering** — it must list the situations where
  this should fire, because that description is all Claude sees when deciding
  whether to load it.
- **Under 150 lines.** Long skills get skimmed. Sharp ones get followed.
- **Invent nothing.** If they didn't tell you, leave it out.

Naming: a voice skill goes after **them**, not their company — `sarah-voice`, not
`bloomcatering-voice`. People run more than one business; their voice moves with
them. A process skill goes after **the job** — `month-end-pack`, `client-quote`,
`weekly-numbers` — because that's what they'll look for when they want it.
Lowercase and hyphens only.

## Getting it installed

They can't zip a file without a terminal, so **start with the route that needs no
files at all**:

> Open a new chat and ask Claude to create a skill for you, then paste in the
> text I've just written.

Claude builds and installs it conversationally. No downloading, no uploading, no
file handling. For a beginner this is far and away the easiest path — reach for
it first.

If they'd rather have the file, give them the finished SKILL.md as a
**downloadable file** (not a wall of text in the chat), then walk them through
it one click at a time, waiting for confirmation at each step:

1. Click their **name or initials**, bottom-left
2. **Settings**
3. **Customize**
4. Find the **Skills** section
5. Add or upload a skill
6. Choose the file

Same menus on the desktop app and the browser, so don't make a thing of which
they're on.

Tell them what success looks like: the skill's name appears in their list.

## Then test it

**Immediately.** Not a demo of it — the real job.

- **Voice skill:** one real thing they need to write this week, to an actual
  person. Watching it come back in their own words is what makes them believe it.
- **Process skill:** run the job. Next month's pack, this week's quote, the
  report that's due. Feed it the real file they brought.

Refine once based on their reaction. There will be something. There always is —
usually that it's too long, or it invented a step they don't do.

Then tell them it's just a text file they own — they can change it any time, or
ask Claude to update it as the business grows.

---

## Template

Fill this in from the interview. **Delete any section you got nothing for** — an
empty section is worse than a missing one, because it invites invention.

```markdown
---
name: <firstname>-voice
description: "Write in <Full Name>'s personal voice and style. Use whenever <Firstname> asks to write, draft, refine or polish any text — emails, WhatsApp messages, LinkedIn posts, proposals, pitch decks, or any written content. Also trigger on 'refine', 'polish', 'make this better', or any request to rewrite something in their tone. Captures their style as <one-line identity>. Use it even for short messages and quick refinements."
---

# Writing in <Firstname>'s Voice

You are writing for <Full Name> — <role, city, one line of who they are>.

<One paragraph: what they've built, what they're building now, why anyone should
listen to them. This is what gives their writing authority.>

<If they work in more than one language, say so plainly: "X is bilingual in
English and Afrikaans. When they write in Afrikaans, match it — don't switch to
English unless asked." Note that they code-switch and mix in English business
terms, and that this is authentic and shouldn't be cleaned up.>

## Tone

<Three adjectives from the interview, then how they actually come across — with a
concrete example from a real sample. Not "professional yet approachable."
Something true and specific.>

## What does NOT sound like them

<Straight from question 6. Concrete.>
- <e.g. "I hope this email finds you well">
- <e.g. "Furthermore" / "In addition to the above">
- <e.g. hedging: "I was just wondering if perhaps...">

## What DOES sound like them

<Real phrases from their samples. Verbatim. At least five. This section carries
more weight than everything else in the file.>
- "<real phrase>"
- "<real phrase>"

## Writing rules

- Paragraph length: <what they actually do>
- Opening: <their style>
- Closing: <their style>
- Sign-off: "<their actual sign-off>"

### When refining their drafts
<Firstname> writes fast and raw. "Refine" means:
1. Fix spelling and grammar
2. Smooth the flow
3. **Keep THEIR words** — don't swap their phrasing for generic corporate language
4. Same length or shorter, never longer

Not wanted: jargon they didn't use, press-release tone, everything bolded, the
personal touch stripped out.

## The business

**<Business Name>** — <what it does, who it serves, how it makes money, where
it's going. Enough that Claude can write about it credibly without asking.>

<Repeat for past ventures — they're credibility, and they come up more than
people expect.>

## Their voice in action

<Two or three real samples, lightly cleaned. Label what each demonstrates. This
is the most valuable part of the file.>

**<e.g. Quick WhatsApp to a client>:**
> <real sample>

---

When in doubt: "Would <Firstname> actually say this out loud?" If it sounds like
it came from a communications department, rewrite it.
```
