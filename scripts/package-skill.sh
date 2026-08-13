#!/usr/bin/env bash
# Rebuild dist/claudeforentrepreneurs.zip from skills/claudeforentrepreneurs/.
#
# For Johannes, not the cohort — they just download the zip from GitHub.
# Run this after editing anything under skills/, then commit the zip.
#
# The zip has SKILL.md at its ROOT (with references/ alongside it), which is
# what claude.ai expects at Settings -> Customize -> Skills.
#
# Usage: ./scripts/package-skill.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_NAME="claudeforentrepreneurs"
SKILL_DIR="$REPO_ROOT/skills/$SKILL_NAME"
OUT="$REPO_ROOT/dist/$SKILL_NAME.zip"

command -v zip >/dev/null 2>&1 || {
  echo "Error: 'zip' is not installed (macOS has it; Ubuntu: sudo apt install zip)" >&2
  exit 1
}

[ -f "$SKILL_DIR/SKILL.md" ] || {
  echo "Error: no SKILL.md at $SKILL_DIR" >&2
  exit 1
}

# Validate frontmatter against the limits claude.ai enforces on upload.
python3 - "$SKILL_DIR/SKILL.md" "$SKILL_NAME" <<'PY'
import re, sys
text = open(sys.argv[1]).read()
expected = sys.argv[2]
fm = re.match(r'^---\n(.*?)\n---\n', text, re.S)
if not fm:
    sys.exit("Error: SKILL.md has no YAML frontmatter")
name = re.search(r'^name:\s*(.+)$', fm.group(1), re.M)
desc = re.search(r'^description:\s*(.+)$', fm.group(1), re.M)
if not name or not desc:
    sys.exit("Error: frontmatter needs both 'name' and 'description'")
n = name.group(1).strip().strip('"')
d = desc.group(1).strip().strip('"')

if len(n) > 64 or not re.fullmatch(r'[a-z0-9-]+', n):
    sys.exit(f"Error: name '{n}' must be <=64 chars, lowercase letters/digits/hyphens only")
if len(d) > 1024:
    sys.exit(f"Error: description is {len(d)} chars, claude.ai limit is 1024")
if n != expected:
    print(f"  ! warning: frontmatter name '{n}' differs from directory '{expected}'")
# Undocumented in Anthropic's own docs, but some third-party guides claim
# claude.ai rejects names containing these. Warn rather than block.
for w in ('claude', 'anthropic'):
    if w in n:
        print(f"  ! note: name contains '{w}'. Not reserved in the official docs,")
        print(f"    but if the upload is rejected, that's the first thing to change.")

print(f"  name: {n}  ({len(n)} chars)")
print(f"  description: {len(d)}/1024 chars")
PY

mkdir -p "$(dirname "$OUT")"
rm -f "$OUT"
( cd "$SKILL_DIR" && zip -rq "$OUT" . -x '*.DS_Store' )

echo
echo "Built $OUT"
unzip -l "$OUT" | sed 's/^/  /'
echo
echo "Commit it so the cohort can download it directly from GitHub."
