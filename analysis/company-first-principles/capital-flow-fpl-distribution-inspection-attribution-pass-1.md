# Capital Flow FPL Distribution Inspection Attribution Pass 1

## Purpose

This page tests the next hard question from the FPL SPPCRC work:

`Can Distribution Inspection be traced end to end from physical work and capital cost into recovery, customer cash, category earnings, and financing source?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-distribution-inspection-attribution-pass-1.csv`

The component extraction pass is:

`/cluster/capital-flow-fpl-distribution-inspection-component-extraction-pass-1.md`

The receipts/financing boundary pass is:

`/cluster/capital-flow-fpl-distribution-inspection-receipts-financing-boundary-pass-1.md`

## Short Answer

Not fully.

Distribution Inspection is the strongest current FPL category because the public record now lines up:

- `193199` actual Distribution Inspection projects
- `61.500000M USD` AP-1 actual capital costs
- `38.500000M USD` Form 7E annual expenditures
- `58.131189M USD` Form 7E additions to plant
- `16.835584M USD` Form 7E total system recoverable expenses
- `15.942971M USD` final category recovery / revenue requirement
- final SPPCRC factor-order and tariff authorization for 2026
- SPPCRC WACC / pre-tax weighted-cost context
- final Form 7A equity, debt, and depreciation components
- Form 8A capital structure and cost-rate support
- FPL-wide operating revenue, net income, capex, debt, AFUDC, PP&E, operating cash flow, and regulatory ROE context

That is enough for category-output-recovery-with-component-attribution.

It is still not enough for realized return proof because two decisive pieces remain missing:

- Distribution Inspection customer receipts by rate class
- Distribution Inspection financing source

## Current Proof Chain

| Gate | Status | Evidence | What It Allows | Boundary |
|---|---|---|---|---|
| Physical output | pass-bridge | AP-1 lists `193199` actual Distribution Inspection projects. | Same-period operating output is visible. | Not project-level return. |
| Capital use | pass-bridge | Form 7E lists `38.500000M USD` expenditures; AP-1 lists `61.500000M USD` actual capital costs. | Category capital use is visible. | Schedule definitions still need reconciliation. |
| Plant addition | pass-bridge | Form 7E lists `58.131189M USD` additions to plant. | Capital use connects to utility plant. | Not net rate base or asset-by-asset support. |
| Recoverable expense | pass-bridge | Form 7E lists `16.835584M USD` total system recoverable expenses. | Category recovery math is visible. | Not customer cash or category earnings. |
| Final category recovery | pass-bridge | Forms 6A and 7A list `15.942971M USD` final Distribution Inspection amount. | Final category revenue requirement is visible. | Not profit or IRR. |
| Aggregate SPPCRC recovery | pass-bridge | Final Form 2A lists `804.620369M USD` clause revenues and `729.233535M USD` total jurisdictional revenue requirements. | Distribution Inspection sits inside a final SPPCRC recovery pool. | Aggregate clause revenue is not category receipts. |
| Customer-charge authority | pass-bridge | Order `PSC-2025-0439-FOF-EI` approves SPPCRC amounts, tariffs, and 2026 factors. | Billing mechanism is authorized. | Authorized factors are not actual cash collected. |
| Allowed-return input | pass-bridge | SPPCRC WACC rows and settlement ROE/capital-structure context are visible. | Cost-of-capital inputs are present. | Not actual earned ROE. |
| FPL-wide cash context | pass-context | Q2/H1 2026 FPL revenue, net income, capex, operating cash flow, PP&E, debt, AFUDC, and regulatory ROE are visible. | Utility-wide absorption capacity and earnings context are visible. | Not SPPCRC category attribution. |
| Customer receipts | missing | No Distribution Inspection-specific receipts by rate class are extracted. | No cash-collection claim yet. | Do not say customers paid this category amount. |
| Category earnings components | pass-component-bridge | Final Form 7A decomposes `15.942971M USD` into `10.481240M USD` equity component grossed up for taxes, `2.278910M USD` debt component, and `3.182821M USD` depreciation expense. | Category recovery composition is visible. | Regulatory components are not cash receipts or shareholder IRR. |
| Financing support | partial-context | Final Form 8A discloses SPPCRC capital structure and cost rates, including long-term debt, short-term debt, common equity, deferred taxes, tax credits, `7.0330%` total weighted cost, and `8.8822%` pre-tax total. | Recovery capital-structure support is visible. | Source-of-funds allocation remains unproven. |

## Derived Attribution Metrics

| Metric | Value | Interpretation |
|---|---:|---|
| AP-1 actual cost per project | `318.32 USD` | `61.500000M USD` divided by `193199` projects. |
| Form 7E plant additions per AP-1 project | `300.89 USD` | `58.131189M USD` divided by `193199` projects. |
| Form 7E recoverable expense per AP-1 project | `87.14 USD` | `16.835584M USD` divided by `193199` projects. |
| Final revenue requirement per AP-1 project | `82.52 USD` | `15.942971M USD` divided by `193199` projects. |
| Final equity component per AP-1 project | `54.25 USD` | `10.481240M USD` divided by `193199` projects. |
| Final debt component per AP-1 project | `11.80 USD` | `2.278910M USD` divided by `193199` projects. |
| Final depreciation per AP-1 project | `16.47 USD` | `3.182821M USD` divided by `193199` projects. |
| Final recovery as share of AP-1 actual cost | `25.92%` | Shows recovery-period revenue requirement is much smaller than same-period AP-1 actual cost. |
| Plant additions as share of AP-1 actual cost | `94.52%` | Shows plant additions are close to, but not identical with, AP-1 actual cost. |
| Distribution Inspection final amount as share of final SPPCRC revenue requirements | `2.19%` | Distribution Inspection is a small share of the full final SPPCRC recovery pool. |
| Distribution Inspection final amount as share of final capital revenue requirements | `2.66%` | Distribution Inspection is a small share of final SPPCRC capital revenue requirements. |
| AP-1 actual cost as share of H1 2026 FPL capex | `1.06%` | Useful context only; periods and scopes differ. |
| Equity plus debt components as share of final recoverable expense | `80.04%` | Final Form 7A recovery is mostly return/carrying-cost components, not depreciation. |

## What We Can Say

The safe evidence-backed answer is:

`FPL Distribution Inspection can now be traced from same-period physical work and category capital cost into plant additions, recoverable expense, final category revenue requirement, final SPPCRC factor-order authorization, cost-of-capital inputs, final equity/debt/depreciation components, Form 8A capital-structure support, aggregate SPPCRC clause revenue, and FPL-wide cash/earnings context. The evidence supports category-output-recovery-with-component-and-capital-structure-attribution, not realized-return proof.`

## What We Cannot Say

Do not claim:

- Distribution Inspection generated `15.942971M USD` of cash receipts
- customers actually paid the Distribution Inspection final amount by category
- the final equity component equals shareholder profit or IRR
- the category earned FPL's reported `11.7%` regulatory ROE
- FPL debt funded these projects
- the category has project-level IRR proof

## Next Evidence To Find

The next source search should look for:

| Missing Piece | Needed Source Class | Pass Condition |
|---|---|---|
| Customer receipts | stamped tariff sheets, billing determinant workpapers, later true-up collection schedules, rate-class allocation exhibits | Distribution Inspection recovery can be tied to billed/collected amounts or rate-class determinants. |
| Category earnings interpretation | SPPCRC workpapers and notes explaining return/carrying-charge formulas, taxes, and final-vs-actual/estimated changes | The visible equity, debt, and depreciation components can be interpreted without overstating them as cash or IRR. |
| Financing source | debt issuance use-of-proceeds, treasury policy, construction-work-in-progress support, or explicit general-utility-funding language | Category capital use can be tied to a funding source or explicitly bounded as general utility financing. |
| Project granularity | AP-1 underlying project rows or workpapers | Project IDs, locations, timing, and variance drivers can be normalized below category level. |

## Decision

`fpl-distribution-inspection-attribution-partial-upgraded - Distribution Inspection is the best current FPL source-use-output-recovery case and now has visible equity, debt, depreciation, aggregate revenue, factor authority, and Form 8A capital-structure support, but the available public evidence still fails the customer-receipt and source-of-funds-allocation tests required for realized return proof.`
