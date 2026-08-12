# Station 2 — GitHub

## The pitch (say this, in your own words)

GitHub is where their work lives. Two things it buys them:

1. **It's a backup that thinks.** Every version of everything, forever. They can
   always go back to the version that worked.
2. **It's the plug everything else uses.** Vercel, Claude Code on the web, and
   most tooling they'll touch later all connect through GitHub. Set it up once,
   and the rest gets easier.

Don't explain branches, commits, or merges. If they ask, answer in one sentence
and move on.

## Step 1 — Do they have an account?

Ask. If no:

- Send them to https://github.com/signup
- Free plan is fine — no need for anything paid
- Advise a **personal** username, not a company one. They'll have more than one
  business. `johannesleroux` ages better than `getluckygolf`.
- Tell them to turn on two-factor auth when prompted. GitHub requires it anyway,
  and this is the account that will hold everything they build.

Wait until they confirm they're in before continuing.

## Step 2 — Connect the GitHub MCP server

This plugin ships the GitHub MCP server config, so it should already be
registered. Verify:

```bash
claude mcp list
```

If `github` is listed but not authenticated, tell them:

> Run `/mcp`, pick **github**, and approve it in the browser window that opens.

If it isn't listed at all (older Claude Code build, or the plugin's MCP config
didn't load), add it manually:

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

Then `/mcp` to authenticate via OAuth.

**Never** ask them to generate a personal access token and paste it somewhere.
OAuth through `/mcp` is the safe path and it's fewer steps.

## Step 3 — Git identity on their machine

Separate from the GitHub account — this is what stamps their name on their work.
Check and set it yourself:

```bash
git config --global user.name
git config --global user.email
```

If blank:

```bash
git config --global user.name "Their Name"
git config --global user.email "their@email.com"
```

Use the same email as their GitHub account so their commits link up properly.

## Step 4 — Their first real repo

Do not create a hello-world. Use whatever they're actually working on — the
notes from Station 0, a project folder they already have, or the site you're
about to build in Station 3.

If they have no project folder yet, make one:

```bash
mkdir -p ~/projects/<their-project> && cd ~/projects/<their-project>
```

Then, in order:

1. Write a real `README.md` — what the business is, what this project does. One
   paragraph. Use their Station 0 answer.
2. `git init` (check `git branch -m main` if the default isn't `main`)
3. `git add -A && git commit -m "First commit"`
4. Create the remote repo using the GitHub MCP tools (or `git remote add` if
   they already made one in the browser)
5. `git push -u origin main`

## Step 5 — Make them look at it

This matters more than it sounds. Give them the URL:

```
https://github.com/<username>/<repo>
```

Tell them to open it. Seeing their own README rendered on github.com is the
moment it stops being abstract. Wait for them to confirm they see it.

## Common snags

**"Support for password authentication was removed"**
They're on an HTTPS remote with no credential helper. Easiest fix is the GitHub
CLI if installed (`gh auth login`), otherwise switch to SSH and generate a key.
Walk them through it — don't hand them a link.

**Push rejected, "fetch first"**
The remote has commits theirs doesn't (usually a README GitHub auto-created).
`git pull --rebase origin main` then push again.

**Repo created but empty on github.com**
They created it in the browser and never pushed, or pushed to a different
branch. Check `git remote -v` and `git branch`, then push to `main`.

**They committed something with an API key in it**
Take it seriously, don't be casual about it. Rotate the key first — assume it's
burned. Then remove it from the file, commit, and add the file to `.gitignore`.
Explain that git history is permanent, which is exactly why the rotation comes
first.
