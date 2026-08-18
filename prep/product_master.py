#!/usr/bin/env python3
"""Draft product master for Creative Beverages, built from the 1 Aug 2026 price
list plus the PnP and Massmart exports.

The price list carries no barcodes and no retailer article numbers, so this
mapping is by name and NEEDS KOWIE TO APPROVE IT. What the price list does give
is the canonical product name and the ex-VAT unit price — which turns his unit
counts into rands.

Prices are ex VAT, per single unit (case price / units per case).
"""

# canonical name -> (brand, pack, ex-VAT price per unit)
MASTER = {
    "CBC Lite Lager":            ("Cape Brewing Company", "340ml NRB", 292.17/24),
    "CBC Lager":                 ("Cape Brewing Company", "340ml NRB", 292.17/24),
    "CBC Amber Weiss":           ("Cape Brewing Company", "440ml NRB", 542.61/24),
    "CBC Pilsner":               ("Cape Brewing Company", "340ml NRB", 320.00/24),
    "CBC Krystal Weiss":         ("Cape Brewing Company", "340ml NRB", 361.74/24),
    "CBC Raspberry Weiss":       ("Cape Brewing Company", "340ml NRB", 361.74/24),
    "CBC Pale Ale":              ("Cape Brewing Company", "340ml NRB", 335.30/24),
    "CBC West Coast IPA":        ("Cape Brewing Company", "340ml NRB", 375.65/24),
    "CBC Milk Stout":            ("Cape Brewing Company", "340ml NRB", 292.17/24),
    "CBC Trueman Lager":         ("Cape Brewing Company", "340ml NRB", 222.61/24),
    "D&D Golden Lager":          ("Diesel & Dust", "340ml NRB", 357.26/24),
    "D&D Lite Lager":            ("Diesel & Dust", "340ml NRB", 357.26/24),
    "D&D Blonde Ale":            ("Diesel & Dust", "340ml NRB", 357.26/24),
    "Rekorderlig Strawberry-Lime":     ("Rekorderlig", "330ml CAN", 479.80/24),
    "Rekorderlig Strawberry-Lime 0%":  ("Rekorderlig", "330ml CAN", 375.65/24),
    "Rekorderlig Wildberries":         ("Rekorderlig", "330ml CAN", 479.80/24),
    "Rekorderlig Mango-Raspberry":     ("Rekorderlig", "330ml CAN", 479.80/24),
    "Rekorderlig Passion Fruit":       ("Rekorderlig", "330ml CAN", 479.80/24),
    "Rekorderlig Peach-Raspberry":     ("Rekorderlig", "330ml NRB", 542.61/24),
    "Teazy Peach":               ("Teazy Hard Ice Tea", "300ml CAN", 432.00/24),
    "Teazy Passion Fruit":       ("Teazy Hard Ice Tea", "300ml CAN", 432.00/24),
    "Teazy Wild Berry":          ("Teazy Hard Ice Tea", "300ml CAN", 432.00/24),
    "Teazy Lemon":               ("Teazy Hard Ice Tea", "300ml CAN", 432.00/24),
    "Lo Cal Crushed Berry":      ("Lo Cal", "300ml", 304.35/24),
    "Lo Cal Squeezed Citrus":    ("Lo Cal", "300ml", 304.35/24),
    "Lo Cal Twisted Lime":       ("Lo Cal", "300ml", 304.35/24),
    "Lo Cal Pressed Granadilla": ("Lo Cal", "300ml", 304.35/24),
    "Lo Cal Pressed Grape Fruit":("Lo Cal", "300ml", 304.35/24),
    "Origen Mezcal":             ("Mezcal", "750ml", 660.87),
}

# Retailer string -> canonical name. Approved by: NOBODY YET.
PNP = {
    "REKORDERLIG WILD BERRIES 330ML CAN": "Rekorderlig Wildberries",
    "REKORDERLIG MANGO RASPBERRY 330ML CAN": "Rekorderlig Mango-Raspberry",
    "REKORDERLIG PASSION FRUIT CAN 330ML": "Rekorderlig Passion Fruit",
    "REKORDERLIG STRAWBERRY LIME CAN 330ML": "Rekorderlig Strawberry-Lime",
    "REKORDERLIG PEACH RBERRY CIDER NRB 330ML": "Rekorderlig Peach-Raspberry",
    "REKORDERLIG STRAWBERRY-LIME 0% CAN 330ML": "Rekorderlig Strawberry-Lime 0%",
    "TRUEMAN LAGER NRB 340ML": "CBC Trueman Lager",
    "LO'CAL BERRY FRUIT SODA 300ML": "Lo Cal Crushed Berry",
    "LO'CAL GRANADILLA FRUIT SODA 300ML": "Lo Cal Pressed Granadilla",
    "LO'CAL GRAPEFRUIT FRUIT SODA 300ML": "Lo Cal Pressed Grape Fruit",
    "LO'CAL LIME FRUIT SODA 300ML": "Lo Cal Twisted Lime",
    "TEAZY PASSION FRUIT CAN 300ML": "Teazy Passion Fruit",
    "TEAZY PEACH CAN 300ML": "Teazy Peach",
    "TEAZY SPIRIT COOLER CAN WILD BERRY 300ML": "Teazy Wild Berry",
    "TEAZY LEMON CAN 300ML": "Teazy Lemon",
    "CBC LAGER 340ML": "CBC Lager",
    "CBC LITE LAGER 340ML": "CBC Lite Lager",
    "CBC AMBER WEISS CRAFT BEER 440ML": "CBC Amber Weiss",
    "CBC MILK STOUT NRB 340ML": "CBC Milk Stout",
    "CBC WEST COAST IPA NRB 340ML": "CBC West Coast IPA",
    "CBC PILSNER 340ML": "CBC Pilsner",
    "CBC PALE ALE NRB 340ML": "CBC Pale Ale",
    "CBC KRYSTAL WEISS 340ML": "CBC Krystal Weiss",
    "DIESEL & DUST GOLDEN LAGER NRB 340ML": "D&D Golden Lager",
    "DIESEL & DUST LITE LAGER 340ML": "D&D Lite Lager",
    "DIESEL & DUST BLOND ALE 340ML": "D&D Blonde Ale",
    # NOT ON THE AUGUST PRICE LIST — query with Kowie:
    "HAPPY DAYS BERRY CAN 300ML": None,
    "HAPPY DAY PASSION FRUIT CAN 300ML": None,
    "SUNCOVE PINEAPPLE FLAVOURED RUM 750ML": None,
    "SUNCOVE COCONUT FLAVOURED RUM 750ML": None,
    "MALACHITE FYNBOS GIN 750ML": None,
    "DISTILLERY ROAD GIN 750ML": None,
    "TRUEMAN LAGER NRB 660ML": None,   # price list has 340ml only
}

MASSMART = {
    "CBC AMBER WEISS NRB 440ML": "CBC Amber Weiss",
    "CBC LAGER NRB 340ML": "CBC Lager",
    "CBC LITE LAGER NRB 340ML": "CBC Lite Lager",
    "CBC PILSNER NRB 340ML": "CBC Pilsner",
    "REKORDERLIG MANGO RASPBERRY CANS 330ML": "Rekorderlig Mango-Raspberry",
    "REKORDERLIG PASSION FRUIT CANS 330ML": "Rekorderlig Passion Fruit",
    "REKORDERLIG STRAWBERRY LIME CANS 330ML": "Rekorderlig Strawberry-Lime",
    "REKORDERLIG WILD BERRIES CANS 330ML": "Rekorderlig Wildberries",
    "REKORDERLIG PEACH RASPBERRY NRB 330ML": "Rekorderlig Peach-Raspberry",
    "TEAZY ICE TEA CAN 300ML LEMON": "Teazy Lemon",
    "TEAZY ICE TEA CAN 300ML PASSION FRUIT": "Teazy Passion Fruit",
    "TEAZY ICE TEA CAN 300ML PEACH": "Teazy Peach",
    "TEAZY ICE TEA CAN 300ML WILD BERRY": "Teazy Wild Berry",
    "HAPPY DAYS CAN 300ML BERRY": None,
    "HAPPY DAYS PASSION FRUIT 300ML CAN": None,
    "9999ORIGEN MEZCAL ESPADIN 750ML": "Origen Mezcal",
}

def price(canonical):
    return MASTER[canonical][2] if canonical in MASTER else None


# ---------------------------------------------------------------------------
# Portfolio split.
#
# Kowie wants Patch reported separately from the rest of the range. That isn't a
# preference — Checkers already structures the account that way: one vendor
# number (196005) with two sub-ranges, 01-CREATIVE PATCH and 02-CREATIVE
# BEVERAGE DISTRIBUTORS.
#
# So don't build two systems. Build one, with portfolio as a column, and let
# "separate" be a filter. If he ever wants them together it's a toggle, not a
# rebuild.
# ---------------------------------------------------------------------------

PATCH = {
    "Patch Margarita":       ("Patch", "150ml CAN", None),
    "Patch Paloma":          ("Patch", "150ml CAN", None),
    "Patch Mojito":          ("Patch", "150ml CAN", None),
    "Patch Espresso Martini":("Patch", "150ml CAN", None),
    "Patch Negroni":         ("Patch", "150ml CAN", None),
    "Patch Old Fashioned":   ("Patch", "150ml CAN", None),
}
# Prices are None: Patch is not on the 1 Aug 2026 price list. Checkers reports
# rand sales directly, so the Checkers view doesn't need them — but any PnP or
# Makro Patch listing will price as blank until Kowie sends a Patch price list.

MASTER.update(PATCH)


def portfolio(canonical):
    """'Patch' or 'Core' — the only split Kowie has asked for."""
    return "Patch" if canonical in PATCH else "Core"


# Checkers identifies products by Article Key, which is stable and numeric —
# far better than the name matching the other two retailers force on us.
CHECKERS_PATCH = {
    "10938912": "Patch Margarita",
    "10938913": "Patch Paloma",
    "10938914": "Patch Mojito",
    "10938915": "Patch Espresso Martini",
    "10938916": "Patch Negroni",
    "10938917": "Patch Old Fashioned",
}
