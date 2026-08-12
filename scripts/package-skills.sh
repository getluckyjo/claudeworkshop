#!/usr/bin/env bash
# Package each Launchpad skill as a .zip for upload to claude.ai.
#
#   claude.ai -> Settings -> Capabilities -> Skills -> Upload skill
#
# Use this if you work in the browser or the desktop app rather than the
# terminal, where plugins aren't available.
#
# Usage: ./scripts/package-skills.sh [output-dir]     (default: ./dist)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/plugins/launchpad/skills"
OUT_DIR="${1:-$REPO_ROOT/dist}"

if ! command -v zip >/dev/null 2>&1; then
  echo "Error: 'zip' is not installed." >&2
  echo "  macOS:  already there, or 'brew install zip'" >&2
  echo "  Ubuntu: sudo apt install zip" >&2
  exit 1
fi

if [ ! -d "$SKILLS_DIR" ]; then
  echo "Error: no skills directory at $SKILLS_DIR" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

count=0
for skill_path in "$SKILLS_DIR"/*/; do
  [ -d "$skill_path" ] || continue
  skill_name="$(basename "$skill_path")"

  if [ ! -f "$skill_path/SKILL.md" ]; then
    echo "Skipping $skill_name — no SKILL.md"
    continue
  fi

  rm -f "$OUT_DIR/$skill_name.zip"
  # Zip from the skills dir so the archive contains <skill_name>/SKILL.md
  ( cd "$SKILLS_DIR" && zip -rq "$OUT_DIR/$skill_name.zip" "$skill_name" -x '*.DS_Store' )
  echo "  $skill_name.zip"
  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  echo "No skills found to package." >&2
  exit 1
fi

echo
echo "Packaged $count skill(s) into $OUT_DIR"
echo "Upload at: claude.ai -> Settings -> Capabilities -> Skills"
