#!/usr/bin/env bash
# Assemble the one download Johannes actually prints and sends from.
#
#     ./scripts/build-pack.sh
#
# Rebuilds the handouts and the invoices first, then lays everything out in the
# order the Saturday morning happens: emails to send, then print, then the
# facilitator material. The zip is gitignored on purpose — regenerate it rather
# than committing it, so it can never drift from the scripts.
set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$PWD"
PACK="Entrepreneur Coach — 22 August 2026"

./scripts/build-handouts.py
echo
./scripts/build-invoices.py
echo

rm -rf "$PACK" "$PACK.zip"
mkdir -p "$PACK"/{"1 Print — workbooks","2 Invoices","3 Facilitator","4 Kowie prototype","5 Brand","6 For Liezl — remote","7 Emails to send"}

# 1 — everything that goes through the printer. Liezl's is emailed, not printed.
for f in handouts/workbook-*.pdf; do
  [[ "$f" == *liezl* ]] && continue
  cp "$f" "$PACK/1 Print — workbooks/"
done
cp handouts/cheatsheet.pdf "$PACK/1 Print — workbooks/"

# 2 — invoices
cp invoices/*.pdf "$PACK/2 Invoices/"

# 3 — facilitator
cp handouts/facilitator-pack.pdf     "$PACK/3 Facilitator/"
cp notes/kowie-shelf-images.pdf      "$PACK/3 Facilitator/"
cp docs/session-2026-08-22.md        "$PACK/3 Facilitator/Session plan.md"
cp docs/workshop-runsheet.md         "$PACK/3 Facilitator/Runsheet.md"
cp docs/pre-work-emails-2026-08-22.md "$PACK/3 Facilitator/Pre-work emails (all sent).md"

# 4 — Kowie's worked example. Insurance, not a handout.
cp "prep/checkers/Creative Beverages - Checkers read.xlsx" "$PACK/4 Kowie prototype/"
cp prep/checkers/checkers-read/SKILL.md "$PACK/4 Kowie prototype/checkers-read SKILL.md"
cp prep/checkers/README.md              "$PACK/4 Kowie prototype/" 2>/dev/null || true

# 5 — brand
cp signature/signature.html signature/signature.txt "$PACK/5 Brand/"
cp signature/signature-mark.png "$PACK/5 Brand/" 2>/dev/null || true
cp signature/README.md          "$PACK/5 Brand/" 2>/dev/null || true
cp dist/entrepreneurcoach.zip   "$PACK/5 Brand/entrepreneurcoach-skill.zip"

# 6 — Liezl runs hers alone, so she gets the workbook, the map and the skill
cp handouts/workbook-liezl.pdf handouts/cheatsheet.pdf "$PACK/6 For Liezl — remote/"
cp dist/entrepreneurcoach.zip  "$PACK/6 For Liezl — remote/"

# 7 — the things to actually send
cp emails/*.txt "$PACK/7 Emails to send/"

cp "docs/START HERE.txt" "$PACK/START HERE.txt"

zip -qr "$PACK.zip" "$PACK"
rm -rf "$PACK"
echo "  $PACK.zip  ($(du -h "$PACK.zip" | cut -f1))"
