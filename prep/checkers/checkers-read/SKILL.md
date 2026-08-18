---
name: checkers-read
description: "Turn the weekly Checkers Vendor Article Sales exports into Creative Beverages' account read — out of stock, selling, not selling — with Patch reported separately from the core range. Use whenever Kowie shares a Checkers export, asks for the weekly retailer read, asks about Patch performance, distribution gaps, activation, listings that aren't selling, or wants last week's Checkers numbers refreshed."
---

# The Checkers read

You are producing the weekly account read for **Creative Beverages** from
Checkers' `Vendor Article Sales` export. Kowie is the GM. He wants decisions,
not a data dump.

## The account

One vendor number, **196005**, with two sub-ranges. Checkers separates them and
so do we:

- **01 — CREATIVE PATCH.** Canned cocktails, 150ml: Margarita, Paloma, Mojito,
  Espresso Martini, Negroni, Old Fashioned.
- **02 — CREATIVE BEVERAGE DISTRIBUTORS.** The core range — Rekorderlig ciders,
  CBC beers, Teazy, Diesel & Dust, Lo Cal, The Duchess.

**Always report Patch separately from the core range.** Never merge them into a
single total unless he explicitly asks. Patch is the growth story and gets
buried the moment it's averaged into 27 other products.

## Reading the file

Use the **`Consolidated View`** sheet. Real data starts at row 11; anything whose
first cell isn't a number is a category banner or a repeated header — skip it.

Columns: `0` article key · `1` article · `2` pack label · `3` sell UOM ·
`5` listed sites · `8` active stores · `9` sell price incl ·
`10-15` weekly units, oldest to newest · `18` latest period sales excl VAT ·
`20` stock qty · `21` weeks of stock.

**`Separate View`** has the same data at store level (tens of thousands of rows).
Only go there when he asks which stores.

## The three rules that decide whether the numbers are right

Every article appears **once per sellable pack** — single, 4-pack, 24-pack — and
again per purchasing org. Those are different products on shelf, each with its
own price and its own sales.

1. **Rand sales: add them up across every pack row.** They're separate sales.
   Dropping the multipacks loses most of the revenue — Margarita is R374k, of
   which R320k is the 4-pack.
2. **Units: never add them across pack rows.** One row counts single cans, the
   next counts 4-packs. Convert first: `units × pack size` from the sell UOM
   (`EA-1` → 1, `PK1-4` → 4, `PK2-24` → 24). Report eaches.
3. **Store counts: take the highest per article, never the sum.** The same
   stores repeat on every pack row. Checkers' own `Vendor and VSR Total View`
   sums them, which is why its listing count reads about 3× too high — do not
   quote that sheet's listings or units back to him.

**Always reconcile before reporting.** Your total rand sales must match the
`Latest Period Sales` figure on `Vendor and VSR Total View` exactly, per
sub-range. If it doesn't, something is wrong — say so rather than reporting it.

## What the read contains

**1. Headline, two lines.** Patch sales and core sales for the period, each with
the change on the previous week.

**2. Distribution gaps — lead with this.** Listed stores versus active stores per
product, worst gap first. This is the biggest number in his business and it is
not what he originally asked for: the core range runs at roughly 47% activation,
and the CBC beers sit near 14% — listed in about 950 stores, selling in about
140. Anything listed with **zero** active stores gets called out by name.

**3. What's selling.** Top products by rand, with the pack split where it
matters. The pack mix is a real decision for him.

**4. What isn't.** Products with listings and little or no movement, and stock
sitting against no sales.

**5. Questions, not assertions.** If something looks contradictory — a product
with zero active stores that nonetheless recorded sales — ask, don't explain it
away.

## How to write it

- **Short.** He is a GM with a week to run. Three lines and what to do about it
  beats a page.
- **Rands, not units**, wherever both are available. Checkers reports rand
  directly, so no price list is needed for this account.
- **Name stores and products.** "Family Grahamstown, Rekorderlig Passion Fruit"
  is actionable; "several stores" is not.
- **Never present a number you couldn't reconcile.** Flag it instead.

## Refreshing the workbook

He has `Creative Beverages - Checkers read.xlsx`. Rebuild it from new exports
rather than editing it by hand — the Data sheet feeds every other sheet, so
replacing the data refreshes the whole thing.

## What this does not do

**It does not combine Checkers with PnP or Makro.** Each retailer measures
something different — PnP reports a 13-week averaged sales rate, Makro actual
daily units, Checkers weekly POS units and rand — over different periods, with
no shared product code. Kowie has asked for accounts run separately for now.
If he ever wants them combined, that starts with a product master he approves,
not with a formula.
