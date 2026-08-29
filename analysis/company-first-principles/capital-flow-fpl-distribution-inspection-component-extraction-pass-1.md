# Capital Flow FPL Distribution Inspection Component Extraction Pass 1

## Purpose

This pass extracts the detailed Distribution Inspection revenue-requirement components from FPL's SPPCRC schedules.

It answers the narrowed question:

`Does the public SPPCRC record split Distribution Inspection recovery into return/carrying-cost and depreciation components?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-distribution-inspection-component-extraction-pass-1.csv`

The receipts/financing boundary pass is:

`/cluster/capital-flow-fpl-distribution-inspection-receipts-financing-boundary-pass-1.md`

## Short Answer

Yes.

The final 2025 Form 7A schedule for `601 - Distribution Inspection Program` decomposes the `15.942971M USD` final total system recoverable expense into:

| Component | Amount | Share Of Final Recoverable Expense | Per AP-1 Project |
|---|---:|---:|---:|
| Equity component grossed up for taxes | `10.481240M USD` | `65.74%` | `54.25 USD` |
| Debt component | `2.278910M USD` | `14.29%` | `11.80 USD` |
| Depreciation expense | `3.182821M USD` | `19.96%` | `16.47 USD` |
| Total system recoverable expenses | `15.942971M USD` | `100.00%` | `82.52 USD` |

Equity plus debt components total `12.760150M USD`, or `80.04%` of the final Distribution Inspection recoverable expense.

This materially improves the FPL answer: category earnings/carrying-charge components are now visible for Distribution Inspection.

The receipts/financing boundary pass adds aggregate clause-revenue, factor-authority, and Form 8A capital-structure support. It still does not prove Distribution Inspection customer receipts or source-of-funds allocation.

## Final 2025 Form 7A Distribution Inspection Components

| Metric | Final 2025 Value | Evidence |
|---|---:|---|
| Expenditures | `38.320627M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Additions to plant | `22.263219M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Plant-in-service / depreciation base ending balance | `116.409865M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Accumulated depreciation ending balance | `9.167688M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| CWIP non-interest-bearing ending balance | `54.994892M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Net investment ending balance | `162.237069M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Equity component grossed up for taxes | `10.481240M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Debt component | `2.278910M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Depreciation expense | `3.182821M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |
| Total system recoverable expenses | `15.942971M USD` | Form 7A, PDF page 18 / Exhibit ALE-1 page 11 |

## Actual/Estimated Comparator

The earlier 2025 actual/estimated Form 7E schedule provides a comparator:

| Metric | Actual/Estimated Value | Final Value | Final Minus Actual/Estimated |
|---|---:|---:|---:|
| Expenditures | `38.500000M USD` | `38.320627M USD` | `-0.179373M USD` |
| Additions to plant | `58.131189M USD` | `22.263219M USD` | `-35.867970M USD` |
| Equity component grossed up for taxes | `10.692874M USD` | `10.481240M USD` | `-0.211634M USD` |
| Debt component | `2.328484M USD` | `2.278910M USD` | `-0.049574M USD` |
| Depreciation expense | `3.814226M USD` | `3.182821M USD` | `-0.631405M USD` |
| Total system recoverable expenses | `16.835584M USD` | `15.942971M USD` | `-0.892613M USD` |

The largest schedule-definition change is additions to plant, which falls from `58.131189M USD` actual/estimated to `22.263219M USD` final. That difference should not be interpreted as a return signal until the underlying workpaper definition is checked.

## What This Lets Us Say

The stronger answer is:

`FPL's final 2025 SPPCRC Form 7A schedule decomposes Distribution Inspection's 15.942971M USD final recoverable expense into a 10.481240M USD equity component grossed up for taxes, a 2.278910M USD debt component, and 3.182821M USD of depreciation expense. This upgrades Distribution Inspection from category-output-recovery bridge evidence to category-output-recovery-with-component-attribution evidence.`

## What It Still Does Not Say

Do not claim:

- the equity component was collected in cash from customers by category
- the debt component identifies a specific debt issuance or lender
- the equity component equals shareholder profit or IRR
- the category earned FPL's reported `11.7%` regulatory ROE
- the additions-to-plant decline is an economic loss or disallowance
- customer receipts have been proven

## Remaining Hard Questions

| Missing Piece | Current Status | Needed Source |
|---|---|---|
| Customer receipts | still missing | rate-class billing determinants, stamped tariff sheets, collection schedules, later true-up workpapers |
| Financing source | still missing | debt issuance use-of-proceeds, treasury allocation, regulatory capital structure support, or explicit general-funding boundary |
| Project-level asset detail | still missing | AP-1 row-level workpapers or project schedules |
| Final source interpretation | partial | workpaper notes explaining the Form 7E to Form 7A additions-to-plant change |

## Decision

`fpl-distribution-inspection-component-attribution-visible - the final SPPCRC schedule exposes Distribution Inspection return/carrying-cost and depreciation components, but customer-receipt and financing-source proof remain missing.`
