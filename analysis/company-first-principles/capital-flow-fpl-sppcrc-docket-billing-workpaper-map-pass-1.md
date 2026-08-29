# Capital Flow FPL SPPCRC Docket Billing Workpaper Map Pass 1

## Purpose

This pass executes the first ranked target from:

`/cluster/capital-flow-power-grid-customer-contract-receipt-workbench-pass-1.md`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-docket-billing-workpaper-map-pass-1.csv`

The question is:

`Which FPL SPPCRC docket filings and workpaper families could contain the billing determinants, category allocation, and receipt support needed to prove Distribution Inspection customer cash?`

## Short Answer

The answer is now narrowed to a `10` row docket/workpaper map.

FPL remains the strongest public receipt route in the power/grid/data-center theme because the local evidence already shows:

- a current public SPPCRC docket route
- a current petition route
- project/program support
- factor and workpaper support
- amended factor support
- aggregate clause revenue
- projected billing-base proxy evidence
- final true-up baseline evidence
- Distribution Inspection category recovery
- discovery and response routes

But the decisive proof is still missing:

`Distribution Inspection-specific billing determinants, billed revenue, collected customer cash, category allocation ledger, source-of-funds schedule, and earned-return model.`

## What This Pass Adds

The prior work said:

`Find FPL billing determinants and receipt support.`

This pass turns that into a filing-family map:

| Priority | Source Family | Why It Matters | Current Status |
|---:|---|---|---|
| 1 | Current docket inventory | Controls all public source routing. | `docket_route_visible` |
| 2 | Petition control | Anchors the 2026 actual/estimated and 2027 projected factor filing family. | `petition_route_visible` |
| 3 | Project/program support | Shows where Distribution Inspection project/cost/output support should sit. | `program_support_visible` |
| 4 | Factor/workpaper route | Main route to rate-class billing determinants and factor math. | `factor_calculation_visible` |
| 5 | Amended factor route | Controls corrected Form 4P/Form 5P factor basis. | `amended_factor_visible` |
| 6 | Aggregate clause revenue | Shows customer-revenue proxy for the whole SPPCRC. | `aggregate_revenue_visible` |
| 7 | Final true-up baseline | Back-tests the actual/final recovery mechanics. | `final_trueup_visible` |
| 8 | Distribution Inspection category | Shows the category cost/recovery side of the chain. | `category_recovery_visible` |
| 9 | Discovery and response route | Best route for non-confidential billing/receipt support if it exists. | `discovery_response_route_visible` |
| 10 | Named cash proof verdict | Keeps the strict hold boundary. | `hold_with_current_docket_route_visible` |

## Current Proof Chain

The FPL chain currently looks like this:

`Distribution Inspection costs and plant additions -> SPPCRC category recovery -> factor/rate-class calculation route -> aggregate SPPCRC clause revenue -> final true-up mechanics`

That is strong recovery evidence.

It is still not the full cash chain:

`Distribution Inspection costs -> category allocation -> rate-class billing determinants -> billed customer dollars -> collected cash -> regulatory subaccount -> source/use financing -> earned return`

## Key Existing Numbers

| Evidence | Amount / Marker | Meaning |
|---|---:|---|
| 2025 final SPPCRC clause revenue | `804.620369M USD` | Aggregate clause revenue, not category cash. |
| 2026 actual/estimated SPPCRC clause revenue route | `1.000979763B USD` | Aggregate current docket revenue route, not Distribution Inspection cash. |
| 2025 final SPPCRC revenue requirements | `729.233535M USD` | Final revenue requirement baseline. |
| 2025 true-up collected/refunded line | `65.318726M USD` | Mechanism line, not bank receipt proof. |
| 2025 final over-recovery including interest | `16.579976M USD` | True-up carried into later factor period. |
| Distribution Inspection final amount | `15.942971M USD` | Category final recovery evidence. |
| Distribution Inspection 2025 expenditures | `38.500000M USD` | Category capital-use evidence. |
| Distribution Inspection 2025 additions to plant | `58.131189M USD` | Category plant-addition evidence. |
| Distribution Inspection 2026 projected expenditures | `45.400000M USD` | Forward category capital-use evidence. |

## What Would Promote FPL

FPL Distribution Inspection can move from recovery proxy to customer-cash proof only if a source joins:

1. Distribution Inspection category recovery
2. SPPCRC factor or tariff rate
3. billing determinants by rate class and period
4. billed customer revenue
5. collected customer cash or a reliable receipt ledger
6. allocation method tying customer revenue to Distribution Inspection
7. source-of-funds or regulatory subaccount support
8. earned-return support

The most likely places are:

| Source Route | Target Fields |
|---|---|
| DN `02560-2026` Epperson/ALE factor workpapers | Form 4P/Form 5P rate-class billing bases and factors. |
| DN `03227-2026` amended ALE factor workpapers | Corrected Form 4P/Form 5P factor basis. |
| DN `02559-2026` Pankratz/AP exhibits | Program/category cost, output, and Distribution Inspection support. |
| 2025 final true-up Epperson filing | Final clause revenue, true-up, category recovery, and baseline schema. |
| Staff and Panama City discovery routes | Possible non-confidential schedules, receipt workpapers, or allocation responses. |

## Next Concrete Extraction

The next artifact should be:

`capital-flow-fpl-sppcrc-form-4p-5p-billing-base-extraction-pass-1.md`

The follow-through extraction is:

`/cluster/capital-flow-fpl-sppcrc-form-4p-5p-billing-base-extraction-pass-1.md`

It should extract:

| Field | Why It Matters |
|---|---|
| Rate class | Separates residential, commercial, industrial, and demand classes. |
| Projected sales at meter | Base for energy factor billing. |
| Projected billed kW | Base for demand factor billing. |
| SPP factor | Converts billing base to billed charge estimate. |
| Energy-related cost | Shows class allocation for energy billing. |
| Demand/customer-related cost | Shows class allocation for demand/customer billing. |
| Total SPPCRC cost by class | Reconciles the factor table to the total recovery pool. |
| Amended factor difference | Prevents using superseded factor rows. |
| Reconciliation to Form 2 revenue | Tests whether factor math can bridge to aggregate clause revenue. |

## Safe Claim

`FPL has the strongest public customer-cash route in the power/grid/data-center theme. The local evidence identifies a current SPPCRC docket, petition, program support, factor workpapers, amended factor support, aggregate clause revenue, final true-up baseline, Distribution Inspection category recovery, and discovery routes. It still does not prove Distribution Inspection-specific billing determinants, billed revenue, collected customer cash, category allocation, source-of-funds, or earned return.`

## Decision

`fpl-sppcrc-docket-billing-workpaper-map-ready-form-4p-5p-extraction`
