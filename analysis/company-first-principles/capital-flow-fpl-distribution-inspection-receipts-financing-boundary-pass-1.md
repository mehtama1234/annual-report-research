# Capital Flow FPL Distribution Inspection Receipts/Financing Boundary Pass 1

## Purpose

This pass tests the two remaining FPL Distribution Inspection gaps:

`Can customer receipts and financing source be proven after the component extraction?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-distribution-inspection-receipts-financing-boundary-pass-1.csv`

The customer-receipt/source pursuit pass is:

`/cluster/capital-flow-fpl-distribution-inspection-customer-receipt-source-pursuit-pass-1.md`

## Short Answer

No, not fully.

The local official PSC source set does improve the answer:

- aggregate SPPCRC clause revenue is visible
- aggregate true-up collected/refunded line is visible
- final SPPCRC factor and tariff authority is visible
- Form 8A capital structure and cost rates are visible
- Distribution Inspection final equity/debt/depreciation component attribution is visible

But the two hard proof gates remain open:

- Distribution Inspection customer receipts by category or rate class
- source-of-funds allocation to Distribution Inspection projects

## Customer-Receipt Boundary

| Evidence | Status | Amount / Mechanic | Boundary |
|---|---|---:|---|
| Final SPPCRC clause revenues net of revenue taxes | aggregate-revenue-visible | `804.620369M USD` | Aggregate SPPCRC revenue, not Distribution Inspection cash. |
| True-up collected/refunded | aggregate-collection-line-visible | `65.318726M USD` | Aggregate true-up line, not category receipt. |
| Final factor-order authorization | rate-factor-authority-visible | multiple 2026 rate-class factors | Authorized billing mechanism, not actual cash collected. |

The current evidence proves a customer-charge mechanism and aggregate clause revenue.

It does not prove:

- Distribution Inspection billed cash
- Distribution Inspection collected cash
- rate-class billing determinants for the category
- customer-class allocation of the `15.942971M USD` final Distribution Inspection amount

## Financing Boundary

The final true-up Form 8A adds capital-structure support for the recovery math:

| Form 8A Input | Amount / Rate | What It Supports | Boundary |
|---|---:|---|---|
| Total adjusted retail capital structure | `70.622413018B USD` | Denominator for the SPPCRC recovery capital-structure schedule. | Not proof of source-of-funds allocation to Distribution Inspection. |
| Long-term debt | `22.907234278B USD`; `32.436%` adjusted retail ratio; `4.58%` midpoint cost rate | Debt-cost input for SPPCRC recovery calculations. | Not proof of a specific debt issuance funding Distribution Inspection. |
| Short-term debt | `896.468170M USD`; `1.269%` adjusted retail ratio; `4.86%` midpoint cost rate | Short-term debt input in the recovery capital structure. | Not construction-borrowing proof. |
| Common equity | `35.140912233B USD`; `49.759%` adjusted retail ratio; `10.80%` midpoint cost rate | Equity-cost input supporting the equity component. | Not proof that shareholder cash funded the category. |
| Deferred income tax | `10.308807613B USD` | Balance input in the capital-structure schedule. | Not project funding. |
| Weighted-cost investment tax credits | `785.929202M USD` | Tax-credit input in the capital-structure schedule. | Not category source-of-funds allocation. |
| Total weighted cost | `7.0330%` | Final true-up cost-rate support. | Not actual earned ROE or IRR. |
| Pre-tax total | `8.8822%` | Pre-tax recovery calculation support. | Not project return. |

This upgrades the financing answer from:

`FPL-wide debt/cash context only`

to:

`SPPCRC recovery capital-structure and cost-rate support visible`

It still does not prove source-of-funds allocation.

## Current Best Answer

The safest answer is:

`FPL Distribution Inspection has physical-output, category-cost, final-recovery, equity/debt/depreciation component, rate-factor authority, aggregate SPPCRC revenue, and Form 8A recovery-capital-structure evidence. It still does not have Distribution Inspection-specific customer receipts or source-of-funds allocation, so it remains below realized-return and project-return-grade proof.`

## What Not To Claim

Do not say:

- Distribution Inspection customers paid `15.942971M USD`
- the `804.620369M USD` aggregate clause revenue is Distribution Inspection revenue
- the Form 8A debt inputs identify project funding
- the common-equity component equals shareholder cash profit
- the final recovery amount is project IRR
- the category has full source-use-return proof

## Next Evidence To Find

| Missing Proof | Search Target | Pass Condition |
|---|---|---|
| Customer receipts | billing determinant workpapers, stamped tariff sheets, rate-class allocation exhibits, later true-up collection schedules | The `15.942971M USD` Distribution Inspection amount can be tied to billed/collected customer cash or rate-class determinants. |
| Financing source | debt issuance use-of-proceeds, FPL treasury allocation, construction funding support, regulatory testimony | Debt, equity, operating cash, or general utility financing can be tied to the category or explicitly bounded. |
| Workpaper interpretation | notes explaining final Form 7A versus actual/estimated Form 7E schedule differences | The `58.131189M USD` actual/estimated additions-to-plant row can be reconciled to the `22.263219M USD` final additions-to-plant row. |
| Project detail | AP-1 row-level project schedules | Project IDs, feeder/location references, timing, and variance drivers can be normalized below category level. |

## Decision

`fpl-distribution-inspection-receipts-financing-boundary-partial - aggregate SPPCRC revenue, factor authority, and recovery capital-structure support are visible, but Distribution Inspection customer receipts and financing-source allocation remain missing.`
