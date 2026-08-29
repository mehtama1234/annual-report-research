# Capital Flow FPL Distribution Inspection Customer Receipt/Source Acquisition Pass 1

## Purpose

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-002`.

It asks:

`Can FPL Distribution Inspection move from regulated recovery proxy to category customer-receipt and source-of-funds allocation proof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-distribution-inspection-customer-receipt-source-acquisition-pass-1.csv`

The upstream pursuit page is:

`/cluster/capital-flow-fpl-distribution-inspection-customer-receipt-source-pursuit-pass-1.md`

The upstream end-to-end graph queue is:

`/cluster/capital-flow-end-to-end-graph-upgrade-queue-pass-1.md`

## Current Answer

`No full upgrade. FPL Distribution Inspection is now an executed local boundary case: output, category cost, plant additions, final recovery, equity/debt/depreciation components, aggregate SPPCRC clause revenue, true-up mechanics, approved rate-factor authority, Form 8A recovery capital structure, and FPL-wide cash context are visible. Category customer receipts and source-of-funds allocation are still not proven.`

## Money Movement Chain

| Link | Current Evidence | Status |
|---|---:|---|
| Regulated activity | `193199` actual Distribution Inspection projects | visible |
| Category cost | `61.500000M USD` AP-1 actual cost | visible |
| Final expenditures | `38.320627M USD` Form 7A final expenditures | visible |
| Plant additions | `22.263219M USD` Form 7A final additions to plant | visible |
| Final recovery | `15.942971M USD` final Distribution Inspection recoverable amount | visible |
| Recovery components | `10.481240M USD` equity component, `2.278910M USD` debt component, `3.182821M USD` depreciation | visible |
| Aggregate customer recovery pool | `804.620369M USD` final SPPCRC clause revenue | aggregate only |
| Aggregate true-up cycle | `65.318726M USD` true-up collected/refunded line | aggregate only |
| Customer charge authority | 2026 PSC-approved SPPCRC factors and tariff authority | mechanism visible |
| Recovery capital structure | `70.622413018B USD` adjusted retail capital structure and `8.8822%` pre-tax total | calculation support |
| FPL-wide cash context | `5388M USD` H1 operating cash flow, `5780M USD` H1 capex, `30188M USD` long-term debt | company context |

## What This Proves

The FPL row now has a strong regulated-recovery bridge:

`utility spending -> named storm-protection category -> physical inspection output -> plant/recovery schedules -> component attribution -> approved rate mechanism -> aggregate clause revenue and true-up cycle`

That is a real money-movement answer, but it is still not a final cash-realization answer.

## Remaining Hard Gates

| Gate | Status | Required Source |
|---|---|---|
| Distribution Inspection customer receipts | missing | Billing determinant workpapers, rate-class allocation schedules, category collection schedules, or later true-up support. |
| Distribution Inspection funding source | missing | Debt use-of-proceeds, FPL treasury allocation, construction funding records, or regulatory testimony tying funding to the category. |
| Project return | missing | Project IDs, asset-level in-service timing, depreciation base, cash collections, tax, and financing allocation. |
| Earned shareholder return | missing | Evidence that regulatory revenue-requirement components translated into earned cash return for the category. |

## Decision

`fpl-distribution-inspection-customer-receipt-source-acquisition-executed-local-time-gated-boundary`

The row improves from route-ready to executed local boundary status. It does not reach full category customer-receipt or source-of-funds proof.

## Safe Claim

`FPL Distribution Inspection shows regulated money movement from utility storm-protection activity into approved recovery mechanics and aggregate customer-recovery cash proxy. The evidence supports output, cost, plant addition, final recovery, component attribution, factor authority, aggregate SPPCRC revenue, true-up mechanics, capital-structure support, and FPL-wide cash context. It does not prove Distribution Inspection-specific customer receipts, source-of-funds allocation, project IRR, or earned shareholder return.`

## Next Work

1. Re-check the `2027` SPPCRC actual/estimated true-up route when it exists.
2. Search for billing determinant workpapers and category allocation schedules.
3. Search for debt use-of-proceeds, treasury allocation, construction funding, or testimony that explicitly bounds the funding source.
4. Keep the graph row below full cash-realization proof until category receipts and funding allocation are source-visible.
