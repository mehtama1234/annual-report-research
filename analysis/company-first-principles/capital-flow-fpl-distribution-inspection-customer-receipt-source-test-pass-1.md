# Capital Flow FPL Distribution Inspection Customer Receipt Source Test Pass 1

This page executes cash-return source work-order row `CFCRSWO-002`.

The question is:

`Can FPL Distribution Inspection move from regulated recovery proxy to category customer-receipt and funding-allocation proof using the current local source set?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-distribution-inspection-customer-receipt-source-test-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-cash-return-source-work-order-pass-1.md`

## Short Answer

`No full upgrade yet. FPL Distribution Inspection remains the strongest regulated recovery-to-cash bridge, but current local evidence still does not prove category-specific customer receipts or source-of-funds allocation.`

The local evidence proves the recovery mechanism and category-level revenue-requirement stack. Distribution Inspection links `193199` actual projects, `61.500000M USD` AP-1 actual cost, `38.320627M USD` final expenditures, `22.263219M USD` final additions to plant, `15.942971M USD` final recoverable expense, `10.481240M USD` equity component grossed up for taxes, `2.278910M USD` debt component, and `3.182821M USD` depreciation.

The broader SPPCRC bridge also shows `804.620369M USD` aggregate clause revenue, `65.318726M USD` aggregate true-up collected/refunded, approved `2026` rate-factor authority, Form 8A capital-structure support, and FPL-wide H1 `2026` operating cash/capex/debt context.

That is not the same as Distribution Inspection customer-receipt or funding-source proof. The current local set still lacks billing determinants, rate-class/customer allocation to the category, billed/collected cash by category, and evidence that debt, equity, operating cash, or another source specifically funded Distribution Inspection projects.

## Source-Test Result

| Gate | Result | Meaning |
|---|---|---|
| Physical output | Pass | `193199` Distribution Inspection projects are visible. |
| Category cost/use | Pass | AP-1 cost, final expenditures, and plant additions are visible. |
| Category recovery | Pass | Final `15.942971M USD` recoverable expense is visible. |
| Recovery components | Pass | Equity, debt, and depreciation components are visible. |
| Aggregate clause revenue | Pass with boundary | SPPCRC aggregate revenue is visible, but not category revenue. |
| True-up collection line | Pass with boundary | Aggregate collection/refund mechanics are visible, but not category cash. |
| Rate-factor authority | Pass with boundary | Customer charge authority is visible, but not billed/collected cash. |
| Capital structure | Pass with boundary | Cost-of-capital inputs are visible, but not project funding source. |
| FPL-wide cash context | Pass with boundary | Utility cash/capex/debt context exists, but not Distribution Inspection allocation. |
| Category customer receipts | Hold | No local source proves billed or collected customer cash for Distribution Inspection. |
| Source-of-funds allocation | Hold | No local source proves which financing/cash source funded Distribution Inspection. |
| Full realized return | Hold | Project IRR and earned shareholder return remain unproven. |

## Decision

`customer-receipt-source-test-hold-with-regulated-recovery-proxy`

The work-order row `CFCRSWO-002` is executed from local evidence. The result is not a full promotion. It confirms that FPL Distribution Inspection is the strongest regulated recovery-to-cash bridge in the system and defines the exact source package still needed for category customer-receipt and funding-allocation proof.

## Safe Claim

`FPL Distribution Inspection has strong regulated recovery evidence: 193199 actual projects, 61.500000M USD AP-1 actual cost, 38.320627M USD final expenditures, 22.263219M USD final additions to plant, 15.942971M USD final recoverable expense, equity/debt/depreciation recovery components, aggregate SPPCRC clause revenue, aggregate true-up collection/refund mechanics, approved 2026 factor authority, Form 8A capital-structure support, and FPL-wide cash context. Current local evidence still does not prove Distribution Inspection-specific customer receipts, billing determinant allocation, source-of-funds allocation, project IRR, or earned shareholder return.`

## Next Source Package

1. `2027` SPPCRC actual/estimated filing covering the `2026` factor year.
2. Billing determinant workpapers by rate class.
3. Category allocation workpapers tying customer factors to Distribution Inspection.
4. Customer receipt or revenue ledger support by SPPCRC category.
5. Debt/equity/cash source-of-funds support for Distribution Inspection projects.
6. Project-level return or earned-shareholder-return support.
