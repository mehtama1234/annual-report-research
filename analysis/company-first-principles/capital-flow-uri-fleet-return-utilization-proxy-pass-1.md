# Capital Flow URI Fleet Return And Utilization Proxy Pass 1

## Purpose

This pass answers the narrow next URI question:

`Can public Q2 2026 filings tell us whether fleet capital is producing output, cash, and recycling value without pretending we have true asset-level ROIC or utilization?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-fleet-return-utilization-proxy-pass-1.csv`

## Source Boundary

This is not a fleet ROIC schedule.

It uses public disclosures only:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-ex99-earnings-release.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`

The source gives revenue, adjusted EBITDA, fleet productivity, cash flow, fleet capex, OEC, guidance, and used-equipment sale metrics. It does not give asset-level time utilization, rental rate, mix, branch utilization, growth-versus-replacement capex, or fleet ROIC.

## Public Inputs

| Metric | Value | Source |
|---|---:|---|
| Q2 rental revenue | `3.849B USD` | Q2 `2026` earnings release. |
| Q2 adjusted EBITDA | `2.056B USD` | Q2 `2026` earnings release. |
| Q2 adjusted EBITDA margin | `46.6%` | Q2 `2026` earnings release. |
| Q2 fleet productivity | `+3.4%` | Q2 `2026` earnings release. |
| Average OEC YoY increase | `+7.1%` | Q2 `2026` earnings release. |
| OEC | `23.8B USD` | Q2 `2026` extracted source table. |
| H1 operating cash flow | `3.305B USD` | Q2 `2026` earnings release. |
| H1 free cash flow | `1.149B USD` | Q2 `2026` earnings release. |
| H1 gross rental capex | `2.931B USD` | Q2 `2026` earnings release. |
| H1 rental-equipment purchase payments | `2.720B USD` | Q2 `2026` earnings release. |
| H1 rental-equipment sale proceeds | `680M USD` | Q2 `2026` earnings release. |
| Q2 used-equipment sale proceeds | `330M USD` | Q2 `2026` earnings release. |
| Q2 used-equipment GAAP gross margin | `46.7%` | Q2 `2026` earnings release. |
| Q2 used-equipment adjusted gross margin | `47.3%` | Q2 `2026` earnings release. |
| Q2 OEC recovery rate on fleet sold | `52.9%` | Q2 `2026` earnings release. |

## Proxy Bridge

| Bridge | Calculation | Result |
|---|---|---:|
| Q2 rental revenue / OEC | `3.849B / 23.8B` | `16.2%` |
| Annualized Q2 rental revenue / OEC | `3.849B * 4 / 23.8B` | `64.7%` |
| Q2 adjusted EBITDA / OEC | `2.056B / 23.8B` | `8.6%` |
| Annualized Q2 adjusted EBITDA / OEC | `2.056B * 4 / 23.8B` | `34.6%` |
| H1 OCF / H1 gross rental capex | `3.305B / 2.931B` | `112.8%` |
| H1 FCF / OEC | `1.149B / 23.8B` | `4.8%` |
| H1 net rental-equipment cash investment | `2.720B - 680M` | `2.040B USD` |
| H1 net rental-equipment cash investment / OEC | `2.040B / 23.8B` | `8.6%` |
| H1 sale proceeds / H1 purchase payments | `680M / 2.720B` | `25.0%` |
| Implied Q2 OEC of used fleet sold | `330M / 52.9%` | `623.8M USD` |
| Implied Q2 used-equipment GAAP gross profit | `330M * 46.7%` | `154.1M USD` |
| H1 purchase payments / current gross purchases guide midpoint | `2.720B / 5.050B` | `53.9%` |
| H1 net cash investment / current net rental-capex guide midpoint | `2.040B / 3.600B` | `56.7%` |
| H1 OCF / current OCF guide midpoint | `3.305B / 6.250B` | `52.9%` |

## Why This Matters

This makes the URI fleet claim more concrete:

- fleet capital is producing disclosed rental revenue
- fleet productivity is positive and explicitly includes rate, time utilization, and mix
- OEC is growing while revenue and EBITDA remain high
- operating cash flow covers gross rental capex in H1
- used-equipment sales produce a visible recycling channel
- the OEC recovery rate and used-sale gross margin are strong public clues, but not a full life-cycle return model

## Safe Claim

`URI has public proxy support that fleet capital is producing revenue, EBITDA, cash, and recycling output: Q2 rental revenue/OEC was 16.2%, annualized Q2 rental revenue/OEC was 64.7%, Q2 adjusted EBITDA/OEC was 8.6%, annualized Q2 adjusted EBITDA/OEC was 34.6%, H1 OCF covered 112.8% of gross rental capex, fleet productivity rose 3.4%, and Q2 used-equipment sales had a 52.9% OEC recovery rate with a 46.7% GAAP gross margin.`

## Claims Not To Make Yet

Do not say:

- URI fleet ROIC is proven
- asset-level utilization is known
- time utilization, rate, and mix are separately quantified
- all rental revenue is owned-fleet rental revenue
- all fleet capex is growth capex
- used-equipment gross margin proves total life-cycle fleet return
- OEC equals eligible collateral
- the fleet purchases were funded by a specific source

## What This Adds

This adds:

`fleet-return-proxy-visible`

It does not move URI to:

`fleet-ROIC-visible`

or:

`true-utilization-visible`

## Next Concrete Work

The next URI evidence gates are:

1. Find owned-equipment rental revenue separated from re-rent and ancillary revenue.
2. Find management discussion that splits fleet productivity into rate, time utilization, and mix.
3. Find fleet capex split between growth and replacement.
4. Find segment or asset-class OEC, gross margin, age, utilization, and disposal recovery.
5. Reconcile these proxies to a trailing-twelve-month rather than single-quarter annualized denominator.

The first item is now partly addressed by:

`analysis/company-first-principles/capital-flow-uri-owned-rental-segment-economics-pass-1.md`
