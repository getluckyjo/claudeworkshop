#!/usr/bin/env python3
"""Build the 22 August cohort invoices as PDFs.

    ./scripts/build-invoices.py

Johannes is a sole proprietor and not VAT registered, so no VAT line appears
and every invoice carries "No VAT applicable" — same wording as the website.

Every seat is shown at the founding rate of R3,500 with any trade exchange or
complimentary allowance as its own credit line, rather than just billing the net
amount. That keeps the value of the seat on the record, makes the exchange
visible to both sides, and means an invoice reconciles against the published
price rather than looking like an ad-hoc number.
"""

import html
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "invoices"

ISSUED = "18 August 2026"
DUE = "Before Saturday 22 August 2026"
COHORT = "Claude for entrepreneurs — Saturday 22 August 2026, Ideas Cartel, Claremont"
SEAT_RATE = 3500

FROM = {
    "entity": "Johannes le Roux",
    "sub": "Sole proprietor, trading as Entrepreneur Coach",
    "addr": ["Ideas Cartel, Claremont", "Cape Town, 7708", "South Africa"],
    "email": "leroux.johannes@gmail.com",
}

BANK = {
    "Account holder": "Johannes le Roux",
    "Bank": "Capitec Bank",
    "Account number": "1308914456",
    "Branch code": "470010",
}

# credit: (label, description, amount) or None
INVOICES = [
    {
        "no": "EC-2608-01", "slug": "kowie",
        "to": "Creative Beverages",
        "attn": "Kowie Lotter",
        "sub": "Reg 2017/060976/07",
        "email": "kowie@creativebeverages.co.za",
        "credit": ("Trade exchange", "Agreed part-exchange against the seat fee. Terms to be confirmed.", 1750),
    },
    {
        "no": "EC-2608-02", "slug": "danielle",
        "to": "d distillery (Pty) Ltd",
        "attn": "Danielle",
        "sub": "Reg 4200286518",
        "email": "accounts@dona.co.za",
        "credit": None,
    },
    {
        "no": "EC-2608-03", "slug": "reni",
        "to": "The Almond Girl (Pty) Ltd",
        "attn": "Reni le Roux",
        "sub": "Reg 4830322600",
        "email": "info@thealmondgirl.co.za",
        "credit": None,
    },
    {
        "no": "EC-2608-07", "slug": "tertius",
        "to": "Awakening Journeys (Pty) Ltd",
        "attn": "Tertius",
        "sub": "Reg 2020/461338/07",
        "email": "joliph@live.com",
        "credit": None,
    },
    {
        "no": "EC-2608-04", "slug": "liezl",
        "to": "Cape of Storms Apothecary",
        "attn": "Liezl Kruger",
        "sub": "",
        "email": "liezlkruger.sa@gmail.com",
        "credit": ("Trade exchange", "Full exchange against the seat fee. Terms to be confirmed.", SEAT_RATE),
    },
    {
        "no": "EC-2608-05", "slug": "carla",
        "to": "Modern Muse Tarot",
        "attn": "Carla le Roux",
        "sub": "",
        "email": "carla.potgter@gmail.com",
        "credit": ("Trade exchange", "Full exchange against the seat fee. Terms to be confirmed.", SEAT_RATE),
    },
    {
        "no": "EC-2608-06", "slug": "maxime",
        "to": "Maxime Davenport",
        "attn": "",
        "sub": "",
        "email": "maximeedavenport@gmail.com",
        "credit": ("Complimentary seat", "Seat offered at no charge. No payment due.", SEAT_RATE),
    },
]

BRANDMARK = """<div class="brandmark">
  <span class="name">Johannes le Roux</span><span class="dot"></span>
  <span class="role">Entrepreneur Coach</span>
</div>"""


def e(s):
    return html.escape(str(s), quote=False)


def rands(n):
    return f"R{n:,.2f}"


def render(inv):
    credit = inv["credit"]
    total = SEAT_RATE - (credit[2] if credit else 0)

    rows = [f"""<tr>
      <td>Workshop seat — founding rate
        <div class="desc">{e(COHORT)}<br>3 hours, 8 seats. Includes the pre-work,
        the 14-day group call and the 30-day written review.</div></td>
      <td class="r">{rands(SEAT_RATE)}</td></tr>"""]
    if credit:
        rows.append(f"""<tr class="credit">
      <td>{e(credit[0])}<div class="desc">{e(credit[1])}</div></td>
      <td class="r">−{rands(credit[2])}</td></tr>""")
    rows.append(f"""<tr class="total">
      <td class="lab">Total due &nbsp;·&nbsp; No VAT applicable</td>
      <td class="r">{rands(total)}</td></tr>""")

    if total > 0:
        payment = f"""<div class="pay">
  <p class="lbl">Payment</p>
  <div class="grid">
    <div>{''.join(f'<p><span class="k">{e(k)}</span><br><span class="v">{e(v)}</span></p>' for k, v in list(BANK.items())[:2])}</div>
    <div>{''.join(f'<p><span class="k">{e(k)}</span><br><span class="v">{e(v)}</span></p>' for k, v in list(BANK.items())[2:])}</div>
  </div>
  <p style="margin-top:3mm;font-size:9pt;color:var(--muted)">
    Please use <b style="color:var(--ink)">{e(inv['no'])}</b> as your payment reference.</p>
</div>"""
        terms = ("<b>Payment before the workshop.</b> The seat is held for 5 days from the date of "
                 "this invoice and confirmed once settled — at 8 seats I can't hold them open longer. "
                 "Full refund up to 7 days before the workshop; inside 7 days I'll move you to the "
                 "next cohort at no charge.")
    else:
        payment = f"""<div class="settled">
  <p class="hd">Nothing to pay.</p>
  <p>This invoice records the value of the seat for both our records. {e(credit[1])}</p>
</div>"""
        terms = ("<b>No payment due.</b> Your seat is confirmed. Issued so the value of the seat is "
                 "on record for both sides.")

    attn = f'<p class="sub">Attention: {e(inv["attn"])}</p>' if inv["attn"] else ""
    sub = f'<p class="sub">{e(inv["sub"])}</p>' if inv["sub"] else ""

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{e(inv['no'])} — {e(inv['to'])}</title>
<link rel="stylesheet" href="invoice.css"></head><body>
{BRANDMARK}

<div class="top">
  <h1>Invoice</h1>
  <div class="meta">
    <b>{e(inv['no'])}</b><br>
    Issued {e(ISSUED)}<br>
    Due {e(DUE)}
  </div>
</div>

<div class="parties">
  <div>
    <p class="lbl">From</p>
    <p class="nm">{e(FROM['entity'])}</p>
    <p class="sub">{e(FROM['sub'])}</p>
    {''.join(f'<p class="sub">{e(l)}</p>' for l in FROM['addr'])}
    <p class="sub">{e(FROM['email'])}</p>
  </div>
  <div>
    <p class="lbl">Billed to</p>
    <p class="nm">{e(inv['to'])}</p>
    {attn}{sub}
    <p class="sub">{e(inv['email'])}</p>
  </div>
</div>

<table>
  <thead><tr><th>Description</th><th class="r">Amount</th></tr></thead>
  <tbody>{''.join(rows)}</tbody>
</table>

{payment}

<p class="terms">{terms}</p>

<p class="sig">Johannes</p>
<div class="foot">
  <span>Johannes le Roux &nbsp;·&nbsp; Entrepreneur Coach</span>
  <span>entrepreneurcoach.co.za</span>
</div>
</body></html>"""


def find_chromium():
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        p = shutil.which(n)
        if p:
            return p
    found = sorted(Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome"))
    if found:
        return str(found[-1])
    sys.exit("Error: no Chromium found.")


def main():
    OUT.mkdir(exist_ok=True)
    chrome = find_chromium()
    total_due = 0
    for inv in INVOICES:
        h = OUT / f"{inv['no']}-{inv['slug']}.html"
        p = OUT / f"{inv['no']}-{inv['slug']}.pdf"
        h.write_text(render(inv))
        subprocess.run([chrome, "--headless", "--disable-gpu", "--no-sandbox",
                        "--no-pdf-header-footer", "--virtual-time-budget=4000",
                        f"--print-to-pdf={p}", h.as_uri()], check=True, capture_output=True)
        due = SEAT_RATE - (inv["credit"][2] if inv["credit"] else 0)
        total_due += due
        print(f"  {p.name:<28} {inv['to'][:30]:<32} {rands(due):>12}")
    print(f"\n  {'':<28} {'TOTAL RECEIVABLE':<32} {rands(total_due):>12}")
    print(f"  {'':<28} {'seat value delivered':<32} {rands(SEAT_RATE*len(INVOICES)):>12}")


if __name__ == "__main__":
    main()
