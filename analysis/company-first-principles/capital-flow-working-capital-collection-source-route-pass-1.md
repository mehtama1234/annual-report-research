# Capital Flow Working Capital Collection Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-010`.

It asks:

`Can current local evidence prove that recovery, backlog, project revenue, retainage, receivables, or contract assets have been billed or collected in cash?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-working-capital-collection-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full working-capital collection upgrade yet. FPL has partial aggregate recovery collection mechanics because aggregate SPPCRC clause revenue and true-up collected/refunded lines are visible, but Distribution Inspection-specific receipts are not proven. Sterling and MasTec remain holds: both have useful contract-timing, backlog, revenue, DSO, retainage, or operating-cash proxies, but neither has receivable aging, retainage collection history, customer collection records, or backlog-cohort cash collection in the current local source set.`

## Row Outcomes

| Row | Case | Current Collection Evidence | Collection Result | Remaining Gap |
|---|---|---|---|---|
| `CFWCCSR-001` | FPL Distribution Inspection | 2025 final true-up has `804.620369M USD` aggregate SPPCRC clause revenue and `65.318726M USD` aggregate true-up collected/refunded; 2026 factor authority and Form 8A recovery capital-structure support are visible | Partial aggregate recovery collection proxy | No Distribution Inspection-specific receipts, billing determinants, rate-class allocation, category collection schedule, customer bill support, or source-of-funds allocation |
| `CFWCCSR-002` | Sterling backlog | Q2 `2026` contract liabilities of `802.601M USD`; contract assets of `156.295M USD`; net contract-liability timing of `646.306M USD`; contract asset retainage of `72.8M USD`; contract liability retainage of `197.1M USD`; positive Q2/H1 OCF less capex; RPO/backlog timing evidence | Hold with retainage and contract-timing proxy | No retainage aging, retainage collection history, receivable aging, named owner collections, backlog-cohort cash collection, project margin, bonded backlog, or actual L/C/surety usage |
| `CFWCCSR-003` | MasTec backlog | Q2 `2026` backlog of `21.4B USD`; contract liabilities of `760.912M USD`; Q2 revenue of `4.374B USD`; adjusted EBITDA of `384.2M USD`; H1 OCF of `120.322M USD`; H1 capex of `188.312M USD`; `72` DSO; liquidity and debt context | Hold with DSO and contract-liability proxy | No retainage disclosure, receivable aging, project collection history, backlog-cohort billing, customer collection records, funded-award support, project margin, or source-to-project credit allocation |

## Decision

`working-capital-collection-source-route-hold-with-one-partial`

`CFRMSWO-010` is executed against the current local source set. It produces one partial aggregate collection row and two holds:

- FPL Distribution Inspection: partial aggregate recovery collection proxy.
- Sterling backlog: hold below retainage/receivable collection proof.
- MasTec backlog: hold below receivable aging and backlog-cohort collection proof.

## Safe Claim

`The working-capital collection source-route pass confirms that selected rows have recovery revenue, true-up mechanics, contract timing, retainage, DSO, backlog, revenue, or operating-cash proxy evidence, but the current local evidence does not prove named category receipts, receivable aging, retainage collection, backlog-cohort cash collection, customer collection records, or project-level cash realization across the affected rows.`

## Next Work

1. For FPL, pull billing determinants, category allocation workpapers, rate-class support, customer bill/collection schedules, and later true-up collection evidence.
2. For Sterling, pull retainage aging, receivable aging, collection history, named owner collection schedules, bonded backlog, actual L/C/surety usage, and project margin.
3. For MasTec, pull receivable aging, retainage disclosures, backlog-cohort billing, collection history, customer award funding, project margin, and source-to-project credit allocation.
4. Move next to `CFRMSWO-011` acquisition, refinancing, or merger closing funds-flow.
