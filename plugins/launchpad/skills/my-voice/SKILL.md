---
name: my-voice
description: "Interview a founder about their business and writing style, then generate a personal skill file into ~/.claude/skills/ so Claude permanently knows their company, their customers, and how they write. Use when someone wants Claude to stop asking about their business every session, wants to write in their own voice, asks to create a personal or business-context skill, asks how to make Claude remember things about their company, or runs /launchpad:my-voice. Also use as Station 5 of the launchpad onboarding flow."
license: MIT
---

# Build Their Own Skill

The single highest-leverage thing a founder can do with Claude is stop
re-explaining their business every time they open a session.

This skill runs a short interview and writes them a permanent skill file. After
this, Claude knows what they sell, who buys it, and how they write — in every
future session, forever.

## What you're producing

One file at:

```
~/.claude/skills/<their-name>-voice/SKILL.md
```

Name it after them, not their company. People run more than one business; their
voice moves with them. `sarah-voice`, not `bloomcatering-voice`.

Use `references/template.md` as the structure to fill in.

## The interview

**Keep it to eight questions across three or four turns.** Founders are busy and
this should feel like a good conversation, not a form.

If they've already done Station 0 of onboarding, read
`~/.claude/launchpad-progress.md` first and **don't ask what they've already
answered.** Nothing kills momentum like being asked the same question twice.

Ask in small batches — two or three at a time, conversationally:

**The business**
1. What's the business, and what do you actually sell?
2. Who's the customer? Be specific — not "small businesses" but the real person
   who signs.
3. What have you built before? (This gives their writing credibility and
   context.)

**How they write**
4. Who are you usually writing to — customers, investors, suppliers, your team?
5. What's your sign-off?
6. Anything that makes you cringe when you see it in your own writing?
7. Do you write in more than one language? (In South Africa, very often yes —
   Afrikaans, isiZulu, isiXhosa. Capture it, and capture that they code-switch.)

**The proof**
8. Paste me two or three things you've actually written — an email, a WhatsApp
   to a client, a LinkedIn post. Raw is better than polished.

Question 8 is worth more than the other seven combined. **Push for it.** Real
samples are what make the skill sound like them instead of like a generic
professional. If they resist, take one — a single real email beats a paragraph
of self-description.

## Writing the file

Read `references/template.md` and fill it in.

Rules that make the difference between a skill that works and one that doesn't:

- **Quote their actual sentences.** Pull real phrases out of the samples they
  gave you and put them in the file verbatim. "What does sound like them" with
  five real examples beats any amount of adjectives.
- **Be specific about what to avoid.** "Don't be corporate" is useless. "Never
  open with 'I hope this email finds you well'" is actionable.
- **Write the description for triggering.** It must list the situations where
  this should fire — drafting, refining, polishing, emails, proposals, posts —
  because that description is all Claude sees when deciding whether to load it.
- **Keep it under 150 lines.** Long skills get skimmed. Sharp ones get followed.
- Don't invent anything. If they didn't tell you, leave it out.

## After you write it

1. Show them the file and tell them where it lives.
2. **Test it immediately.** Ask them for one real thing they need to write this
   week — an actual email to an actual person — and draft it using the new
   skill. Watching it come back in their own voice is what makes them believe
   it.
3. Refine once based on their reaction. There will be something. There always
   is.
4. Tell them how to keep it alive: it's just a text file, they can edit it any
   time, or ask Claude to update it as the business changes.

## Sharing it

If they want it on claude.ai and Claude Desktop too, not just the terminal:

```bash
cd ~/.claude/skills && zip -r ~/Desktop/<name>-voice.zip <name>-voice
```

Then: **claude.ai → Settings → Capabilities → Skills → upload the zip.**

Now it follows them across every surface they use.
