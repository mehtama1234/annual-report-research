# Capital Flow FPL SPPCRC Category Attribution Bridge Pass 1

## Purpose

This page tests the next attribution question:

`Can one FPL SPPCRC category be lined up from output and cost to final recovery, factor authorization, WACC context, and FPL-wide cash/earnings context?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-category-attribution-bridge-pass-1.csv`

The deeper Distribution Inspection attribution pass is:

`/cluster/capital-flow-fpl-distribution-inspection-attribution-pass-1.md`

The Distribution Inspection component extraction pass is:

`/cluster/capital-flow-fpl-distribution-inspection-component-extraction-pass-1.md`

## Short Answer

Yes, as a category bridge. No, not as realized return proof.

Distribution Inspection and Transmission Inspection are now the best FPL category-attribution candidates because each has:

- 2025 actual/estimated capital-use rows
- 2025 final category revenue-requirement rows
- AP-1 actual project counts
- AP-1 actual capital costs
- final factor-order and tariff authorization
- WACC/carrying-charge context
- FPL-wide earnings, cash-flow, capex, debt, regulatory ROE, and asset-base context

The missing link is now narrower after the Distribution Inspection component extraction: SPPCRC category recovery has been decomposed into equity, debt, and depreciation components for Distribution Inspection, but customer receipts, financing source, and project-level return remain open.

## Category Bridge

| Category | Output | Actual Cost | Final Recovery / Revenue Requirement | Derived Unit Metric | Status |
|---|---:|---:|---:|---:|---|
| Distribution Inspection | `193199 projects` | `61.500000M USD` | `15.942971M USD` | `82.52 USD final revenue requirement per project` | category-output-recovery bridge visible; attribution open |
| Transmission Inspection | `84056 projects` | `66.300000M USD` | `23.595154M USD` | `280.71 USD final revenue requirement per project` | category-output-recovery bridge visible; attribution open |
| Distribution Vegetation Management | `18597 miles` | `108.700000M USD` | not extracted as final category row | `5845.03 USD actual cost per mile` | output/cost visible; final category attribution open |
| Transmission Vegetation Management | `9610 miles` | `17.600000M USD` | not extracted as final category row | `1831.43 USD actual cost per mile` | output/cost visible; final category attribution open |
| Distribution Feeder Hardening | physical unit not normalized | not normalized | `335.693443M USD` | not calculated | category recovery visible; output-unit missing |

## What This Says

The strongest category answer is:

`FPL's Distribution Inspection and Transmission Inspection categories can now be traced from actual 2025 physical project counts and actual costs to final category revenue-requirement rows, with final factor-order authorization and FPL-wide cash/earnings context.`

That is materially stronger than a general statement that FPL has a rate case, a storm-protection plan, or high capex.

## What This Does Not Say

Do not use this page to claim:

- the final category revenue requirement equals customer cash collected
- the derived per-project metric is project profit
- SPPCRC category recovery equals shareholder earnings
- FPL debt funded these specific projects
- the category has project-level IRR proof
- every AP-1 feeder/project row is normalized

## Why Distribution Inspection Is The Cleanest Next Target

Distribution Inspection is the cleanest next target because the chain already has:

| Chain Step | Evidence |
|---|---|
| capital use | Form 7E annual expenditures of `38.500000M USD` |
| plant addition | Form 7E additions to plant of `58.131189M USD` |
| recoverable expense | Form 7E total system recoverable expenses of `16.835584M USD` |
| final category recovery | Form 6A final amount of `15.942971M USD` |
| physical output | AP-1 actual project count of `193199` |
| actual cost | AP-1 actual capital costs of `61.500000M USD` |
| customer charge authorization | Order `PSC-2025-0439-FOF-EI` factor/tariff authorization |
| carrying-charge context | SPPCRC WACC and pre-tax weighted-cost rows |
| utility cash context | FPL-wide H1 2026 operating cash flow of `5388M USD` and FPL capex of `5780M USD` |

The next proof has now been attempted in the Distribution Inspection attribution pass. Its target chain is:

`project count -> actual cost -> plant addition -> depreciation/tax/AFUDC/return -> revenue requirement -> rate-class collections -> FPL cash/earnings`

The result is attribution-partial-upgraded: output, cost, plant addition, recoverable expense, final category recovery, factor-order authority, carrying-charge context, FPL-wide cash context, and Distribution Inspection equity/debt/depreciation component attribution are visible, while customer receipts and financing source remain missing.

## Current Answer

The current answer is:

`FPL has reached category-output-recovery-with-component-attribution status for Distribution Inspection and category-output-recovery bridge status for Transmission Inspection. That proves a real regulated recovery mechanism with physical work behind it. It still does not prove realized SPPCRC category return because customer receipts and financing source are not reconciled.`

## Decision

`fpl-category-attribution-bridge-visible - Distribution Inspection and Transmission Inspection are ready for a final attribution attempt, while vegetation and feeder hardening need additional category or AP-1 row-level extraction before they can support the same claim.`
