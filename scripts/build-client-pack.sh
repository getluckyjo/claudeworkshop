#!/usr/bin/env bash
# Assemble the email attachments for one remote client.
#
#     ./scripts/build-client-pack.sh <slug> "<Name — Business>" [invoice-no]
#     ./scripts/build-client-pack.sh trevor "Trevor Davenport — Efficient Energy SA" EC-2610-01
#
# Numbered in the order the covering email refers to them, because an inbox
# sorts attachments however it likes. Their own skill is included when
# dist/<slug>-*.zip or a named skill exists — still zipped, since Claude wants
# the zip and an unpacked folder is the commonest way a skill install fails.
#
# The output is gitignored. Regenerate it rather than committing it, so it
# can't drift from the workbook and invoice it was built from.
set -euo pipefail

cd "$(dirname "$0")/.."
SLUG="${1:?usage: build-client-pack.sh <slug> \"<Pack name>\" [invoice-no] [skill-name]}"
PACK="${2:?pack name required}"
INVOICE="${3:-}"
SKILL="${4:-}"

WORKBOOK="handouts/remote/workbook-$SLUG.pdf"
[ -f "$WORKBOOK" ] || { echo "No $WORKBOOK — run ./scripts/build-remote.py first" >&2; exit 1; }

rm -rf "$PACK" "$PACK.zip"
mkdir -p "$PACK"

n=1
cp "$WORKBOOK"            "$PACK/$n Workbook — ${PACK%% —*}.pdf";  n=$((n+1))
cp handouts/cheatsheet.pdf "$PACK/$n Cheat sheet.pdf";             n=$((n+1))

if [ -n "$SKILL" ] && [ -f "dist/$SKILL.zip" ]; then
  cp "dist/$SKILL.zip"    "$PACK/$n $SKILL (skill).zip";           n=$((n+1))
fi

if [ -n "$INVOICE" ]; then
  INV="invoices/$INVOICE-$SLUG.pdf"
  [ -f "$INV" ] || { echo "No $INV — run ./scripts/build-invoices.py first" >&2; exit 1; }
  cp "$INV"               "$PACK/$n Invoice $INVOICE.pdf";         n=$((n+1))
fi

zip -qr "$PACK.zip" "$PACK"
rm -rf "$PACK"
echo "  $PACK.zip  ($(du -h "$PACK.zip" | cut -f1))"
unzip -Z1 "$PACK.zip" | grep -v '/$' | sed 's|^[^/]*/|    |'
