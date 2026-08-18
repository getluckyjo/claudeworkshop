#!/usr/bin/env python3
"""Kowie's three questions, answered in rands instead of units.

Pass the PnP and Massmart exports as arguments, or edit the paths below.
Prices come from product_master.py, built off the 1 Aug 2026 price list.

    python3 analyse.py <pnp.xlsx> <massmart.xlsx>

Caveat that matters: the dead-stock figure is Creative Beverages product sitting
in retailer stores. 96% of those lines came via Stock Transfer, meaning the
retailer moved it from their own DC — so the retailer owns it. It is revenue
already banked, not cash owed. It matters as a reorder gap and a delisting risk,
not as inventory on his balance sheet. Say it that way.
"""

import sys
import openpyxl
import pandas as pd

import product_master as m

PNP = sys.argv[1] if len(sys.argv) > 1 else "pnp.xlsx"
MASSMART = sys.argv[2] if len(sys.argv) > 2 else "massmart.xlsx"

DEAD_COVER_DAYS = 365


def load_pnp(path):
    df = pd.read_excel(path)
    df.columns = [c.strip() for c in df.columns]
    for c in ("SOH Qty", "DROS Qty", "Days Cover"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["canonical"] = df["Article description"].map(m.PNP)
    df["unit_price"] = df["canonical"].map(lambda c: m.price(c) if c else None)
    # Kowie to confirm the status filter — this is the assumption, stated once.
    active = df[
        (df["Site Profile"] != "Distribution center")
        & (df["Listing Status"] == "L")
        & (df["Site Article Status"].astype(str).str.zfill(2) == "04")
    ]
    return df, active.dropna(subset=["unit_price"])


def main():
    raw, priced = load_pnp(PNP)
    print(f"PnP: {len(raw)} rows in, {len(priced)} active and priced\n")

    dead = priced[priced["Days Cover"] > DEAD_COVER_DAYS].copy()
    dead["value"] = dead["SOH Qty"] * dead["unit_price"]
    print(f"DEAD STOCK  ({DEAD_COVER_DAYS}+ days cover)")
    print(f"  {len(dead)} lines · {dead['SOH Qty'].sum():,.0f} units · "
          f"R{dead['value'].sum():,.0f} ex VAT")
    print(dead.groupby("Site Description")["value"].sum().nlargest(5).round(0).to_string())

    oos = priced[priced["SOH Qty"] == 0].copy()
    oos["per_day"] = oos["DROS Qty"] * oos["unit_price"]
    print(f"\nOUT OF STOCK")
    print(f"  {len(oos)} lines · {oos['Site Code'].nunique()} stores · "
          f"R{oos['per_day'].sum():,.0f}/day lost")

    print("\nREVENUE BY PRODUCT (rand per day, all listed stores)")
    daily = priced.assign(r=priced["DROS Qty"] * priced["unit_price"])
    by_product = daily.groupby("canonical")["r"].sum().sort_values(ascending=False)
    total = by_product.sum()
    for name, val in by_product.items():
        print(f"  {name:<32} R{val:>8,.0f}   {val/total*100:4.1f}%")
    print(f"  {'TOTAL':<32} R{total:>8,.0f}")

    # Massmart: stock present, nothing sold in 30 days.
    ws = openpyxl.load_workbook(MASSMART, read_only=True, data_only=True)[
        "1. Daily SOH Performance"
    ]
    lines = value = 0
    for r in ws.iter_rows(min_row=6, values_only=True):
        art, site = r[0], r[1]
        if not art or site == "Makro Riversands DC":
            continue
        soh = [c for c in r[2:32] if c is not None]
        sales = [c for c in r[32:62] if c is not None]
        canonical = m.MASSMART.get(art)
        unit = m.price(canonical) if canonical else None
        if unit and soh and soh[0] > 0 and sum(sales) == 0:
            lines += 1
            value += soh[0] * unit
    print(f"\nMASSMART dead lines (stock, no sales in 30 days)")
    print(f"  {lines} lines · R{value:,.0f} ex VAT")


if __name__ == "__main__":
    main()
