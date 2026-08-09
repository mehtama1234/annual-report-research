# Force Map Gap Review

Date: 2026-08-09

## What this checks

This note compares:

- `ibis-industries/forces/` force slugs
- `indexes/force-map.csv` coverage inside `annual-report-research`

## Current result

Mapped force slugs: `16`

Unmapped force slugs: `4`

Unmapped list:

1. `commodity-whiplash`
2. `the-graying-market`
3. `the-immigration-squeeze`
4. `the-labor-squeeze`

## Why these remain open

The current annual-report archive is strong in:

- large-cap technology
- financials
- healthcare
- industrial infrastructure
- operational services
- defensive consumer goods

It is weaker in:

- agriculture and commodity producers
- homebuilding and property-capital edge cases outside the current real-estate set
- senior housing and age-linked consumer services
- immigration- and labor-bottleneck operators

So the remaining force gaps are mostly not tagging failures. They are exposure gaps.

## Best next anchors by uncovered force

### 1. `commodity-whiplash`

Current archive companies with partial relevance:

- Caterpillar
- Waste Management
- PepsiCo

Why they are only partial:

- They feel second-order commodity pressure through equipment demand, packaging, fuel, logistics, and input cost swings.
- They do not directly express fertilizer, mining, crop-price, or farm-margin economics as the center of the business.

Best new anchor candidates:

- CF Industries
- Mosaic
- Deere
- Nutrien
- Newmont

Priority: high if you want the force map to reflect producer and farm-cycle economics rather than only downstream pass-through.

### 2. `the-graying-market`

Current archive companies with partial relevance:

- UnitedHealth Group
- Abbott
- Johnson & Johnson
- Thermo Fisher
- Chubb

Why they are only partial:

- The archive already captures healthcare utilization, chronic care, diagnostics, medtech, and insurance economics.
- It is still light on direct senior housing, elder-care services, and age-targeted consumption.

Best new anchor candidates:

- Brookdale Senior Living
- Welltower
- Ventas
- Humana
- Align Technology

Priority: medium-high. Healthcare evidence is already present, so this is more about refining the force with age-specific operators.

### 3. `the-immigration-squeeze`

Current archive companies with partial relevance:

- ABM
- HCA Healthcare
- Rollins
- Waste Management
- UPS

Why they are only partial:

- These companies are labor-intensive and exposed to wage, turnover, and field-service staffing pressure.
- They do not directly express farm-labor, food-processing, construction-labor, or immigration-policy dependence as the center of the story.

Best new anchor candidates:

- Tyson Foods
- Lennar
- D.R. Horton
- BrightView
- United Rentals

Priority: medium-high if labor-policy and immigration exposure are meant to be a named cross-sector theme.

### 4. `the-labor-squeeze`

Current archive companies with partial relevance:

- ABM
- HCA Healthcare
- UPS
- Rollins
- Cintas
- Eaton

Why they are only partial:

- The archive already shows labor scarcity, wage pass-through, and route-density or service-productivity responses.
- It is lighter on direct skilled-trades, construction labor, and caregiving bottlenecks.

Best new anchor candidates:

- Comfort Systems USA
- Quanta Services
- EMCOR
- Kelly Services
- BrightSpring Health

Priority: medium. This is the easiest uncovered force to improve using the current archive plus a few targeted additions.

## Practical ranking

If the goal is to improve the bridge fastest, the best next collection priorities are:

1. `commodity-whiplash`
2. `the-labor-squeeze`
3. `the-graying-market`
4. `the-immigration-squeeze`

## Recommendation

Do not force the four remaining slugs into `force-map.csv` yet with weak evidence.

Use the current file for high-confidence mappings only, and treat this note as the queue for the next company-selection pass.

That keeps the bridge index credible while making the remaining thematic gaps explicit.
