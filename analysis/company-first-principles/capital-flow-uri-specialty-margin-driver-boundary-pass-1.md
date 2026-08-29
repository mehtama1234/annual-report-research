# Capital Flow URI Specialty Margin Driver Boundary Pass 1

## Purpose

This pass answers the next narrow URI question:

`Do URI's filings explain why specialty margin compressed, or do we only see the margin numbers?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-specialty-margin-driver-boundary-pass-1.csv`

## Source Boundary

This uses filed MD&A and segment tables from:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2024-10k-10k.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-10k-10k.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q2-10q.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`

This pass is:

`driver-visible`

It is not:

`driver-quantified`

The filings name margin-pressure drivers, but they do not give a full basis-point or dollar bridge by driver.

## Margin Compression

| Metric | Start | End | Change |
|---|---:|---:|---:|
| Specialty equipment-rentals gross margin, FY2023 to FY2025 | `48.9%` | `43.6%` | `-5.3 pts` |
| Specialty equipment-rentals gross margin, H1 2024 to H1 2026 | `48.5%` | `43.1%` | `-5.4 pts` |

This confirms the margin pressure seen in the segment trend and asset proxy passes.

## Named Drivers In The Filings

| Driver | Source Context | What It Supports |
|---|---|---|
| Higher ancillary revenue mix | FY2024 10-K and FY2025 10-K MD&A | Ancillary revenues generate lower margins than owned equipment rentals. |
| Specialty ancillary mix | FY2025 10-K MD&A | The filing specifically ties a higher proportion of 2025 specialty revenue from ancillary revenues to margin pressure. |
| Inflation | FY2024 10-K, FY2025 10-K, Q2 2025 10-Q | Inflation is a recurring named cost-pressure driver. |
| Normal cost variability | FY2024 10-K, FY2025 10-K, Q2 2025 10-Q | Normal cost variability is repeatedly named with inflation. |
| Delivery costs | Q2 2025 10-Q | Delivery is named as a particular cost-pressure area. |
| Labor and benefits costs | Q2 2025 10-Q | Labor/benefits is named as a particular cost-pressure area. |
| Used-equipment pricing normalization | FY2024 10-K and Q2 2025 10-Q | This affects used-equipment sale margin, not necessarily specialty rental margin. |
| Yak acquisition / mix | FY2025 10-K and Q2 2025 10-Q | Yak affects growth/productivity context and likely specialty mix, but the filings do not isolate margin contribution. |
| Specialty margin offset in Q2 2026 | Q2 2026 10-Q | General rentals margin improved, partially offset by decreased specialty margin. |

## What This Adds

This changes the specialty margin interpretation from:

`margin compression observed`

to:

`margin compression observed and driver-visible`

It still does not become:

`margin bridge quantified`

or:

`specialty ROIC deterioration proven`

## Safe Claim

`URI's filings make specialty margin pressure driver-visible, not driver-quantified. Specialty equipment-rentals gross margin compressed from 48.9% in FY2023 to 43.6% in FY2025 and from 48.5% in H1 2024 to 43.1% in H1 2026. The filings name higher ancillary mix, inflation, normal cost variability, delivery costs, labor and benefits costs, used-equipment pricing normalization, and Yak/acquisition mix as relevant parts of the margin and growth context, while Q2 2026 again identifies specialty margin pressure as an offset to general-rentals improvement.`

## Claims Not To Make Yet

Do not say:

- the filing quantifies each driver's basis-point impact
- specialty ROIC deterioration is proven
- Yak caused the margin compression
- ancillary mix alone explains the margin compression
- used-equipment normalization explains specialty rental margin
- specialty has become a weak segment
- true utilization or rate/mix is known

## Next Concrete Work

The next URI evidence gates are:

1. Download and extract the investor deck/transcript source family identified in `capital-flow-uri-rate-time-mix-source-boundary-pass-1.md`.
2. Find specialty category mix around surface protection mats, power/HVAC, trench, fluid solutions, storage, and modular.
3. Find segment OEC or rental-fleet assets.
4. Find operating-profit or EBITDA by segment.
5. Find growth-versus-replacement capex.
