# Kowie's Checkers prototype

What he should walk out of block 7 with, built ahead of time so the facilitator
knows it works. **Use it as insurance, not as a handout** — Kowie watching it get
built off his own file is the moment the workshop is selling.

| | |
|---|---|
| `build_report.py` | Reads both Checkers exports, writes the workbook |
| `Creative Beverages - Checkers read.xlsx` | The artefact |
| `checkers-read/SKILL.md` | The process skill — the reusable half |

```
python3 build_report.py <core.xlsx> <patch.xlsx> "Creative Beverages - Checkers read.xlsx"
python3 /root/.claude/skills/synced/xlsx/scripts/recalc.py "Creative Beverages - Checkers read.xlsx" 540
```

Recalculation needs a generous timeout — LibreOffice takes several minutes on
this workbook.

## The workbook

- **Read me** — what it is, how to refresh it, the three traps, and the two open
  questions for Kowie
- **Summary** — Patch against the core range, latest period
- **Distribution gaps** — listed versus active, worst gap first, with
  zero-activation lines shaded
- **By product** — one row per article, formulas pulling from Data
- **Data** — one row per article and pack, straight from the exports

Blue cells come from the file; black cells are formulas; green links across
sheets. Replace the Data sheet and everything else recalculates, which is the
whole point — next week is a refresh, not a rebuild.

## The check that matters

Totals reconcile to each export's own `Vendor and VSR Total View`:
**R803,732.61** core and **R954,647.47** Patch, to the cent. Any method that
doesn't reconcile is wrong, and the check takes ten seconds. Teach him that
before you teach him anything else.

## Why this file is easy to get wrong

Every article appears once per sellable pack. Rand values must be added across
those rows; unit counts must not be, because one row counts cans and the next
counts 4-packs; store counts must not be either, because they repeat.

Both obvious moves — "sum everything" and "de-duplicate to one row per article" —
produce a confidently wrong answer. That's what makes it a good teaching file.
