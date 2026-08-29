# Capital Flow URI Specialty Category Source Boundary Pass 1

## Purpose

This pass answers the next URI question:

`Can we see which specialty product categories are large enough to matter, and do we get category margin or OEC?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-specialty-category-source-boundary-pass-1.csv`

## Source Boundary

This pass uses:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-10k-10k.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q4-ex99-earnings-release.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/earnings-transcripts/2025-q4-fool-transcript.html`

This pass is:

`specialty-category-mix-visible`

It is not:

`specialty-category-margin-visible`

or:

`specialty-category-OEC-visible`

## Category Mix In The 2025 10-K

URI's FY `2025` 10-K gives equipment-rental revenue percent by fleet type.

| Fleet Type | FY 2025 | FY 2024 |
|---|---:|---:|
| General construction and industrial equipment | `39%` | `40%` |
| Aerial work platforms | `22%` | `23%` |
| General tools and light equipment | `9%` | `9%` |
| Power and HVAC equipment | `11%` | `11%` |
| Trench safety equipment | `5%` | `5%` |
| Fluid solutions equipment | `7%` | `7%` |
| Mobile storage equipment and modular office space | `3%` | `3%` |
| Surface protection mats | `4%` | `2%` |

This is the first category-level mix table that matters for the URI thread.

The key point is not that every category has a separate segment. The key point is that the public source gives a fleet-type revenue mix, while the segment financial table gives only General Rentals versus Specialty.

## What Specialty Includes

The Q2 `2026` 10-Q describes Specialty as renting products, plus setup and other services on rented equipment, including:

- trench safety equipment
- power and HVAC equipment
- fluid solutions equipment
- mobile storage equipment and modular office space
- surface protection mats

The filing describes Specialty customers as construction companies involved in infrastructure projects, municipalities, and industrial companies. The segment primarily operates in the United States and Canada, with a smaller presence in Europe, Australia, and New Zealand.

## What The Category Table Adds

The category table strengthens the Matting/ancillary bridge:

- Surface protection mats rose from `2%` of equipment-rental revenue in FY `2024` to `4%` in FY `2025`.
- Q4 `2025` transcript commentary says Matting project timing was worth about one point of fleet productivity.
- The Q4 `2025` release says specialty margin pressure included depreciation pressure due in part to growth in the Matting business.

This makes Matting category-visible.

It still does not make Matting margin-visible.

## Category Sums

If we group the clearly Specialty-labeled fleet types in the 10-K table:

`Power/HVAC + Trench + Fluid Solutions + Mobile Storage/Modular + Surface Protection Mats`

then FY `2025` sums to:

`11% + 5% + 7% + 3% + 4% = 30%`

FY `2024` sums to:

`11% + 5% + 7% + 3% + 2% = 28%`

This is directionally consistent with Specialty taking share, but it is not the same as the filed Specialty segment share of equipment-rentals revenue. The segment table and fleet-type table can differ because of rounding, definitions, geography, services, acquisitions, and classification.

## Safe Claim

`URI now has category-mix visibility, but not category-margin visibility. The FY2025 10-K discloses equipment-rental revenue by fleet type: Power/HVAC was 11%, Fluid Solutions 7%, Trench Safety 5%, Mobile Storage/modular 3%, and Surface Protection Mats 4%, up from 2% in FY2024. The Q2 2026 10-Q confirms these are core Specialty categories. This supports a cleaner Matting and specialty-mix source trail, but it still does not disclose category gross margin, category OEC, category capex, or category ROIC.`

## Claims Not To Make Yet

Do not say:

- Power/HVAC has a known margin
- Fluid Solutions has a known margin
- Trench Safety has a known margin
- Mobile Storage/modular has a known margin
- Matting/surface protection mats have a known margin
- Surface protection mats caused the full specialty margin decline
- the sum of fleet-type categories exactly equals Specialty segment revenue
- category mix proves category ROIC

## Next Concrete Work

The next URI evidence gates are:

1. Use `capital-flow-uri-fleet-type-revenue-estimate-pass-1.md` for rounded category dollar scale.
2. Find category-level margin, OEC, capex, or asset data.
3. Search older investor days, acquisition materials, and product-line presentations for Specialty subcategory economics.
4. Tie Surface Protection Mats/Yak commentary to purchase accounting, depreciation, and fleet age if disclosed.
5. Build a category matrix that separates revenue mix, productivity mix, margin mix, OEC, capex, and utilization.
