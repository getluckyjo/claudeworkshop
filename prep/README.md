# Kowie prep — Creative Beverages

Working files from profiling his retailer exports before the 22 August session.
Not part of the skill; this is facilitator prep for one attendee.

- `product_master.py` — draft mapping of PnP and Massmart product strings to the
  canonical names on the 1 Aug 2026 price list, with ex-VAT unit prices.
  **Nobody has approved this mapping.** It's by name, because the price list
  carries no barcodes and no retailer article numbers.
- `analyse.py` — runs the three questions against PnP, and the dead-lines check
  against Massmart, in rands rather than units.

Run: `python3 analyse.py`

## What matters, in one line

He asked for out-of-stocks first. Out-of-stocks cost him about **R600 a day**.
Dead stock is over **R1m**. The money is on the other side of the question he
asked.
