# The scoring model

A number between 0 and 100, and a band. The point is not precision — it is to
rank a list of four hundred companies so the top forty get the effort, and to
make the reason for each score inspectable rather than a feeling.

Score from whatever is known. Partial information is normal; say what's missing
rather than guessing at it silently.

## The inputs

### 1. Industry energy intensity — up to 30

How much electricity the sector uses per rand of turnover. This is the cheapest
signal available and the least reliable on its own, which is why it caps at 30.

**High (25–30).** Foundries and smelting. Galvanising. Cement, lime, bricks and
ceramics. Glass. Pulp and paper. Industrial chemicals. Cold storage and ice.
Abattoirs and meat processing. Dairies. Industrial bakeries. Plastics —
injection moulding and extrusion especially. Textile dyeing and finishing.
Industrial laundries. Data centres. Water and wastewater treatment. Mining and
mineral processing.

**Medium (12–20).** General food and beverage. Automotive components.
Engineering and fabrication. Packaging converters. Printing. Pharmaceutical
manufacturing. Hospitals. Hotels and resorts. Large shopping centres. Cold
retail. Poultry and intensive agriculture under cover.

**Low (3–10).** Light assembly. Warehousing without refrigeration. Offices,
professional services, finance, insurance. Education. Dry retail. Call centres.

**Zero.** Consultancies, agencies, brokerages, anyone whose largest load is
lighting and laptops. These are not prospects at any headcount.

### 2. Shift pattern — up to 25

The most underweighted variable in most prospect lists, and the one that most
often explains why two identical-looking companies have very different bills.

| Pattern | Score |
|---|---|
| 24/7, continuous process | 25 |
| Three shifts, five or six days | 20 |
| Two shifts | 13 |
| Single day shift | 6 |
| Office hours only | 2 |

Continuous refrigeration counts as 24/7 even when nobody is on site — the
compressors do not go home. This catches cold stores that look like warehouses
on paper.

### 3. Equipment signature — up to 25

Score the heaviest two present, not everything.

| Present at scale | Score |
|---|---|
| Electric arc or induction furnace, smelting | 25 |
| Industrial refrigeration, blast freezing, ice | 22 |
| Injection moulding, extrusion, blow moulding | 20 |
| Kilns, industrial ovens, dryers, autoclaves | 18 |
| Large compressed air (>100 kW installed) | 16 |
| Large pumping — water, slurry, irrigation | 15 |
| Heavy HVAC, clean rooms, controlled atmosphere | 12 |
| Welding lines, plating, surface treatment | 12 |
| Conveying, packing, general plant | 7 |
| Lighting and office HVAC only | 0 |

Compressed air deserves its own note: it is usually the single most wasteful
system on a site, leaks are invisible without metering, and a plant with a big
compressor room is a strong prospect almost regardless of what it makes.

### 4. Scale — up to 20

Use whichever is known, best signal first.

| Signal | Score |
|---|---|
| NMD above 2 MVA | 20 |
| NMD 1–2 MVA, or on Megaflex | 17 |
| Municipal large power user, or on Miniflex | 12 |
| Covered floor area above 10,000 m² | 12 |
| Covered floor area 3,000–10,000 m² | 8 |
| Multiple sites, each mid-size | 8 |
| Under 3,000 m², single site | 3 |

## The bands

| Score | Band | What to do |
|---|---|---|
| 75–100 | **Priority** | Research the decision maker properly. Personal approach, named plant, named waste. Worth a drive |
| 55–74 | **Qualify** | Worth outreach, but ask the tariff question before booking anything |
| 35–54 | **Hold** | Sequence them, don't chase. Revisit if they expand or add a shift |
| Under 35 | **Decline** | Off the list. Not a soft no — a no, so the time goes where it pays |

Any company whose estimated monthly spend sits below the floor is **Decline**
regardless of score. The floor overrides the model; the model only exists
because spend usually isn't known.

## Estimating spend from the score

Rough, and say so. Useful for ranking, not for a proposal.

    estimated monthly spend  ≈  covered m²  ×  intensity factor  ×  shift multiplier

Intensity factor, rand per m² per month at a single day shift:

| Band | R/m²/month |
|---|---|
| High intensity | 55–160 |
| Medium | 20–50 |
| Low | 6–18 |

Shift multiplier: single 1.0 · two 1.7 · three 2.4 · continuous 3.0.

A 6,000 m² injection moulding plant on three shifts: 6,000 × 90 × 2.4 ≈ **R1.3m
a month**. Clears almost any floor, and worth a proper approach.

A 6,000 m² dry warehouse on a day shift: 6,000 × 11 × 1.0 ≈ **R66,000**. Looks
substantial, isn't. This pairing is exactly the mistake the model exists to stop
— same building, same staff count, twenty times the bill.

**Always show the working.** Trevor needs to be able to look at a score and
disagree with it; a number he can't interrogate is a number he won't trust, and
he knows his market better than any model does. When he overrides it, ask why
and write the reason down — that's how the weightings get better.

## Output format

For a single company:

    Company          ·  score  ·  band
    Industry         ·  <sector>, <high/medium/low> intensity        <n>/30
    Shift            ·  <pattern>                                    <n>/25
    Equipment        ·  <what, and how you know>                     <n>/25
    Scale            ·  <m², sites, tariff, NMD>                     <n>/20
    Estimated spend  ·  R<low>–R<high> per month
    Clears floor     ·  yes / no / unknown
    Unknown          ·  <what would most change this score>
    Next             ·  <the single next action>

The **Unknown** line matters as much as the score. One phone call to fill the
biggest gap beats re-scoring on what's already known.

For a list: rank by score, group by band, and put the Decline group at the
bottom with one-line reasons. Those reasons are what stops the same dead company
being re-researched in three months.
