#!/usr/bin/env bash
# The download that goes to the cohort after the workshop.
#
#     ./scripts/build-assetpack-zip.sh
#
# Small on purpose — five things, no facilitator material, nobody's own skill.
set -euo pipefail
cd "$(dirname "$0")/.."
PACK="Entrepreneur Coach — asset pack"

./scripts/build-assetpack.py
echo

rm -rf "$PACK" "$PACK.zip"
mkdir -p "$PACK"
cp "assetpack/Asset pack.pdf"                       "$PACK/"
cp "assetpack/Project instructions — template.md"   "$PACK/"
cp handouts/cheatsheet.pdf                          "$PACK/Cheat sheet.pdf"
cp dist/entrepreneurcoach.zip                       "$PACK/entrepreneurcoach-skill.zip"
cp "docs/asset-pack-READ ME.txt"                    "$PACK/READ ME.txt"

zip -qr "$PACK.zip" "$PACK"
rm -rf "$PACK"
echo "  $PACK.zip  ($(du -h "$PACK.zip" | cut -f1))"
