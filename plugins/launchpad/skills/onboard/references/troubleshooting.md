# Troubleshooting

Fix it yourself where you can. The person on the other side of this is a founder
in a workshop, not a support engineer. Read the error, act, move on.

## Ground control

**`claude: command not found`**
Claude Code isn't installed or isn't on PATH.
```bash
npm install -g @anthropic-ai/claude-code
```
If npm itself is missing, they need Node first — https://nodejs.org (LTS). On a
Mac with Homebrew: `brew install node`.

**Claude Code is on an old version**
```bash
claude update
```
Plugin skills, MCP config in plugins, and `/plugin` all need a reasonably recent
build. If `/plugin` isn't recognised, this is almost always why.

**`git: command not found`**
- Mac: `xcode-select --install`
- Windows: https://git-scm.com/download/win
- Linux: `sudo apt install git`

**They're working in their home folder or Downloads**
Don't lecture. Just offer:
```bash
mkdir -p ~/projects/<project-name> && cd ~/projects/<project-name>
```

**Permission errors on `npm install -g`**
Don't reach for `sudo`. Use a Node version manager instead — `nvm` on Mac and
Linux — or install Node via Homebrew, which puts things somewhere writable.

## Plugin and marketplace

**`/plugin marketplace add` fails**
- Check the repo is public and the spelling is exact: `getluckyjo/claudeworkshop`
- Confirm network access — corporate laptops sometimes block git over HTTPS
- Try the full URL form: `/plugin marketplace add https://github.com/getluckyjo/claudeworkshop`

**Plugin installs but `/launchpad:onboard` isn't found**
Run `/reload-plugins`. If the install summary mentioned it, this is expected.
Then check `/plugin` to confirm launchpad is listed and enabled.

**Marketplace was added but shows no plugins**
`/plugin marketplace update` to refresh the local copy — they may have an older
snapshot from before a change was pushed.

## MCP

**Server listed but tools missing**
Not authenticated. `/mcp` → pick the server → approve in browser.

**`/mcp` opens a browser but nothing happens**
Popup blocker, or wrong account signed in. Incognito window usually sorts it.

**Tools worked and then stopped**
Token expired or the server dropped. `/mcp` to reconnect. If that fails,
`claude mcp remove <name>` and add it again.

**Corporate laptop blocking everything**
Some managed devices block OAuth callbacks to localhost. If they're stuck, don't
burn the whole session on it — move them to claude.ai in the browser with
connectors instead, and note it in the progress file.

## When you're properly stuck

Don't let one person's broken laptop eat the room.

1. Note the blocked station in `~/.claude/launchpad-progress.md`
2. Skip ahead to a station that does work — Station 5 (their own skill) needs no
   external service at all and is genuinely valuable on its own
3. Come back to the blocker at the end, or after the workshop

A cohort member who finished four of six stations and knows exactly what's
outstanding is in a far better position than one who spent the whole session
watching someone debug their PATH.
