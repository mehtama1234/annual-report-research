# Capital Flow URI Category Economics Matrix Pass 1

## Purpose

This pass turns the URI Specialty category work into an evidence matrix.

It answers:

`For each Specialty category, what number do we have, what number do we still not have, and what source would upgrade the claim?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-category-economics-matrix-pass-1.csv`

## Source Boundary

This pass uses:

- `capital-flow-uri-specialty-category-source-boundary-pass-1.md`
- `capital-flow-uri-fleet-type-revenue-estimate-pass-1.md`
- `capital-flow-uri-ancillary-matting-margin-bridge-pass-1.md`
- `capital-flow-uri-owned-rental-segment-economics-pass-1.md`
- `capital-flow-uri-owned-rental-segment-trend-pass-1.md`
- `capital-flow-uri-segment-asset-return-proxy-pass-1.md`
- `capital-flow-uri-yak-matting-acquisition-economics-pass-1.md`

This pass is:

`category-economics-matrix-visible`

It is not:

`category-unit-economics-visible`

or:

`category-ROIC-visible`

## Matrix

| Category | FY 2025 Revenue Evidence | Margin | OEC | Capex | Utilization | Productivity | Source Strength |
|---|---:|---|---|---|---|---|---|
| Power/HVAC | `1.519B USD` rounded estimate | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Included in broad fleet/product/business mix only | Revenue-scale estimate visible |
| Trench Safety | `0.690B USD` rounded estimate | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Included in broad fleet/product/business mix only | Revenue-scale estimate visible |
| Fluid Solutions | `0.966B USD` rounded estimate | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Included in broad fleet/product/business mix only | Revenue-scale estimate visible |
| Mobile Storage/modular | `0.414B USD` rounded estimate | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Included in broad fleet/product/business mix only | Revenue-scale estimate visible |
| Surface Protection Mats | `0.552B USD` rounded estimate; Yak had `353M USD` 2023 adjusted revenue and `322M USD` FY2024 post-acquisition revenue | Yak had `171M USD` 2023 adjusted EBITDA, but ongoing URI Matting margin is not disclosed | Acquired rental-equipment fair value was `127M USD`, but OEC is not disclosed | Not disclosed | Not disclosed | Q4 2025 Matting project timing was a qualitative negative mix driver | Revenue-scale estimate plus Yak acquisition economics visible |

## What We Actually Know

The strongest category-level number is approximate revenue scale, except for Matting/Yak where acquisition-level economics are now visible.

The strongest Specialty segment-level numbers are:

- FY `2025` Specialty equipment-rentals revenue: `4.641B USD`
- FY `2025` Specialty gross profit: `2.024B USD`
- FY `2025` Specialty gross margin: `43.6%`
- H1 `2026` Specialty capital expenditures: `817M USD`
- H1 `2026` Specialty gross margin: `43.1%`

Those are segment numbers, not category numbers. They do not let us allocate margin, OEC, capex, utilization, or ROIC to Power/HVAC, Trench, Fluid, Mobile Storage/modular, or Surface Protection Mats. The Yak acquisition numbers improve Matting evidence, but they still do not disclose ongoing Matting category ROIC inside URI.

## What This Changes

The remaining URI question is now sharper:

`Which Specialty category is absorbing incremental capital, and does that category earn attractive returns?`

Current public evidence can size category revenue. For Matting/Yak, it can also show pre-acquisition adjusted revenue, adjusted EBITDA, mat count, purchase-price allocation, and acquisition funding. It still cannot answer ongoing category ROIC.

The most useful next sources are:

- product-line investor day slides
- acquisition presentation materials, especially Yak/surface protection mats
- fleet/OEC schedules by category
- category-level capex commentary
- category-level gross-margin or EBITDA commentary
- operating metric disclosure around rental rate, time utilization, and mix by category

## Safe Claim

`URI now has category-economics matrix visibility: Power/HVAC, Trench Safety, Fluid Solutions, Mobile Storage/modular, and Surface Protection Mats can be sized with rounded FY2025 revenue estimates, and Matting/Yak has acquisition-level revenue, EBITDA, mat-count, purchase-accounting, and funding evidence. But the current source set still does not disclose ongoing category margin, category OEC, category capex, category utilization, or category ROIC inside URI. The next proof step is post-acquisition product-line unit economics, not more aggregate segment math.`

## Claims Not To Make Yet

Do not say:

- Power/HVAC has known category margin
- Trench Safety has known category margin
- Fluid Solutions has known category OEC
- Mobile Storage/modular has known capex intensity
- Surface Protection Mats has known ongoing URI category margin or ROIC
- Matting explains all Specialty margin compression
- Specialty segment margin can be allocated across categories from public filings
- category revenue growth proves category return quality

## Next Concrete Work

The next URI evidence gates are:

1. Use `capital-flow-uri-yak-matting-acquisition-economics-pass-1.md` for Matting acquisition-level economics.
2. Search URI investor day and acquisition decks for post-acquisition product-line economics.
3. Build a source queue for category OEC, capex, margin, utilization, and ROIC.
4. Reconcile category revenue estimates to Specialty segment revenue if a better source appears.
5. Compare URI's Specialty category disclosure against HRI, Sunbelt/Ashtead, and other rental peers for category unit-economics leakage.
