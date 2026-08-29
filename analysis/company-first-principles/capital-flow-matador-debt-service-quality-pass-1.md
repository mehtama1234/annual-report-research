# Capital Flow Matador Debt-Service Quality Pass 1

## Purpose

This page executes Matador row `CFDRBUQ-008` from the debt/refinancing bridge upgrade queue:

`Can Matador's borrowing-base bridge be upgraded from source/use visibility to debt-service quality evidence?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-matador-debt-service-quality-pass-1.csv`

The upstream queue is:

`/cluster/capital-flow-debt-refinancing-bridge-upgrade-queue-pass-1.md`

The upstream Matador bridges are:

`/cluster/capital-flow-matador-borrowing-base-use-return-bridge-pass-1.md`

`/cluster/capital-flow-matador-source-specific-use-allocation-pass-1.md`

## Current Answer

`Matador can be upgraded to proxy-grade debt-service quality evidence, but not full financing-quality proof. The Q2 2026 filing and June 10 2026 Eighth Amendment show a 3.25B USD borrowing base, 2.75B USD elected commitments, 939M USD of Credit Agreement borrowings, 53.8M USD of letters of credit, about 1.7572B USD of simple unused elected commitment after letters of credit, current-ratio and debt-to-EBITDA covenant thresholds, binary covenant compliance, 112.344M USD of first-half interest expense, and a 2028-to-2034 note refinancing with visible premium/write-off costs. But the pricing grid, exact SOFR spread, covenant cushion, reserve collateral cushion, cash interest schedule, and asset-level return remain open.`

## Reconciliation

| Step | Amount | Meaning |
|---|---:|---|
| Borrowing base | `3.250B USD` | Reserve-based capacity reaffirmed in the 10-Q and amendment. |
| Elected commitments | `2.750B USD` | Lender-agreed commitment after the June 2026 increase. |
| Credit Agreement borrowings | `939.000M USD` | Drawn main facility balance at June 30 2026. |
| Letters of credit | `53.800M USD` | Ancillary facility usage. |
| Simple unused elected commitment after LCs | `1.7572B USD` | `2.750B - 939.0M - 53.8M`. |
| Simple utilization including LCs | `36.102%` | Borrowings plus LCs divided by elected commitment. |
| First-half interest expense | `112.344M USD` | GAAP interest expense, not cash interest. |
| Interest expense / OCF proxy | `7.981%` | First-half interest expense divided by first-half operating cash flow. |
| 2028 notes retired | `500.000M USD` | Tender plus redemption. |
| 2034 notes issued | `750.000M USD` | New 6.00% senior notes due 2034. |
| Simple annual coupon-dollar change | `10.625M USD` | New annual coupon dollars exceed old annual coupon dollars because principal increased. |

## What Improved

| Area | Prior Bridge | This Pass |
|---|---|---|
| Facility quality | Borrowing base and elected commitment were visible. | This pass adds simple utilization, unused elected commitment after LCs, maturity, covenant thresholds, and binary compliance. |
| Agreement quality | The Eighth Amendment was already evidence for capacity. | This pass uses it as agreement-grade support for commitment increase, lender reallocation, no-default condition, and collateral-coverage mechanics. |
| Debt-service burden | Interest was an open quality question. | First-half interest expense, capitalized interest, and interest/OCF proxy are measured. |
| Note economics | Senior note issuance and 2028 retirement were visible. | The pass calculates old and new simple annual coupon dollars and records premium/write-off costs. |

## Decision

`debt-service-quality-proxy-visible-pricing-cushion-incomplete`

This is an upgrade from:

`aggregate-timing-source-use-reconciliation-visible`

It does not reach:

`full-financing-quality-or-asset-return-proven`

The queue pass test required pricing, covenants, interest, and note economics. The visible local evidence passes at proxy level: covenant thresholds, compliance status, facility headroom, interest burden, note coupon mechanics, issuance cost proxy, premium, and extinguishment loss are visible. It holds on full proof because the actual pricing grid, exact SOFR spread, lender-level commitments, covenant cushion, borrowing-base certificate, reserve value, cash interest, and asset contribution are not yet extracted.

## Remaining Gap

| Gap | Why It Matters | Next Source |
|---|---|---|
| Pricing grid and SOFR spread | Needed to evaluate true facility cost and whether terms improved or worsened. | Full credit agreement pricing grid and amendment schedules. |
| Covenant cushion | Binary compliance does not show how much room Matador had. | Covenant compliance certificate. |
| Reserve collateral cushion | Borrowing base is not reserve value or collateral coverage. | Reserve report, borrowing-base certificate, and collateral schedule. |
| Cash interest | GAAP interest expense and capitalized interest are not cash debt service. | Cash interest disclosure and interest rollforward. |
| Pro forma note economics | Simple coupon math ignores timing, tax, premium, amortization, and use of excess proceeds. | Tender documents, redemption notice, and pro forma interest schedule. |
| Asset contribution | Company-level OCF does not prove the acquired assets or capex generated return. | Asset-area production, LOE, revenue, capex, EBITDA, and cash contribution. |

## Safe Claim

`Matador's Q2 2026 filing and June 10 2026 Eighth Amendment support a bounded debt-service quality proxy: the borrowing base was reaffirmed at 3.25B USD, elected commitments increased to 2.75B USD, borrowings plus letters of credit used about 36.1% of elected commitment, simple unused elected commitment after letters of credit was about 1.7572B USD, covenant thresholds and compliance were visible, first-half interest expense was 112.344M USD, and the 2028-to-2034 note refinancing lowered coupon rate but increased simple annual coupon dollars by about 10.625M USD because new principal was larger. This does not prove pricing improvement, covenant cushion, reserve collateral sufficiency, lender allocation, source-specific use, or asset-level return.`

## Next Work

1. Extract the full pricing grid and applicable SOFR spread.
2. Pull the covenant compliance certificate or exact covenant calculation.
3. Find the borrowing-base certificate and reserve/collateral support.
4. Build a cash interest and pro forma interest schedule.
5. Tie acquired acreage, Cardinal, San Mateo, and development capex to asset-level cash contribution.
