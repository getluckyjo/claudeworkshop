# Troubleshooting

Fix it yourself. The person on the other side is a beginner in a workshop, not a
support engineer. Read what went wrong, sort it, move on — don't narrate the
debugging at them.

**Never** solve a problem by sending them to a terminal. If that seems like the
answer, it isn't.

## Connectors

**Connected, but the tools aren't available in this chat**
Toggled off for this conversation. They can enable it in the chat's connector
settings. This is the single most common one — check it first.

**Pop-up opens then hangs**
Pop-up blocker, or they're signed into a different account in that browser. An
incognito window signed into the right account usually fixes it.

**Wrong Google account connected**
Common when someone has personal and business Gmail. Disconnect, sign out of
Google in that browser, reconnect with the right one.

**They can't find Settings**
Profile icon, bottom left. Then Connectors. Walk them there one click at a time.

## Skills

**They can't find where skills live**
Click their **name or initials** in the bottom-left → **Settings** →
**Customize** → **Skills**. It used to be under Capabilities, so anyone
following an older guide will be looking in the wrong place.

**They unzipped the file and now have a folder**
Very common on a Mac, which unzips downloads automatically. The upload wants the
`.zip` file itself, not the folder. It'll still be sitting in Downloads next to
the folder — point them at that.

**The upload wants a .zip and they have a loose file**
Don't try to talk a beginner through zipping anything. Use the other route:
start a new chat, ask Claude to create the skill, paste in the content. Same
result, no file handling.

**Uploaded, but nothing happens when they ask for help**
Three things, in order: are they in a **new** chat (skills don't load into a
conversation that was already running), does the skill appear in their list, and
have they tried typing `/entrepreneurcoach` directly rather than asking in plain
language.

**Skill uploaded but doesn't seem to do anything**
Skills fire based on their description. If it's not triggering, the description
is too narrow — widen it to name the actual situations ("when drafting emails,
posts, proposals..."). Then have them re-upload.

**Name rejected**
Lowercase and hyphens only, 64 characters max, and it can't contain "claude" or
"anthropic".

## Going live

**Vercel connector missing**
Settings → Connectors → Vercel → Connect. If it's connected but unavailable in
the chat, it's toggled off for the conversation.

**Vercel signup asking for payment details**
They've landed on a paid tier. Personal account, Hobby plan, free. Back out and
pick again.

**Deployed but the page is blank or 404s**
Entry file needs to be `index.html` at the root of the file tree.

**The live URL asks visitors to log in**
Deployment protection. Deploy to `production`, or use `get_access_to_vercel_url`
for a temporary link while sorting it.

**Vercel is just not cooperating and time is short**
Build it as an artifact and publish that instead. They get a public link, they
keep the momentum, and Vercel becomes homework. Do not let a signup problem cost
them the moment — that moment is the whole point of the session.

## GitHub

**They're looking for a GitHub connector**
There isn't one. Use [claude.ai/code](https://claude.ai/code).

**Overwhelmed by it**
Skip it. It's genuinely optional. A beginner with a live website and a working
inbox assistant had a great session — GitHub adds nothing to that today.

## When you're properly stuck

Don't let one person's problem eat the room.

1. Note the blocked station in their progress summary
2. Move to a station that works — **Station 2 needs nothing external at all** and
   is worth the whole workshop on its own
3. Come back at the end, or leave it as homework

Someone who finished four of six stations and knows exactly what's outstanding
is in a much better place than someone who spent the session watching you fight
a pop-up blocker.
