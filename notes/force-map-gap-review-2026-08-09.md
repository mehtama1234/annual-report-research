# Force Map Gap Review

Date: 2026-08-09

## What this checks

This note compares:

- `ibis-industries/forces/` force slugs
- `indexes/force-map.csv` coverage inside `annual-report-research`

## Current result

Mapped force slugs: `17`

Unmapped force slugs: `3`

Unmapped list:

1. `the-graying-market`
2. `the-immigration-squeeze`
3. `the-labor-squeeze`

## Why these remain open

The current annual-report archive is strong in:

- large-cap technology
- financials
- healthcare
- industrial infrastructure
- operational services
- defensive consumer goods

It is weaker in:

- senior housing and age-linked consumer services
- immigration- and labor-bottleneck operators
- additional skilled-trades and caregiving bottleneck operators

So the remaining force gaps are mostly not tagging failures. They are exposure gaps.

## Best next anchors by uncovered force

### 1. `the-graying-market`

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

### 2. `the-immigration-squeeze`

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

### 3. `the-labor-squeeze`

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

1. `the-labor-squeeze`
2. `the-graying-market`
3. `the-immigration-squeeze`

## Recommendation

Do not force the three remaining slugs into `force-map.csv` yet with weak evidence.

Use the current file for high-confidence mappings only, and treat this note as the queue for the next company-selection pass.

That keeps the bridge index credible while making the remaining thematic gaps explicit.
