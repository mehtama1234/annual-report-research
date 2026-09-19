# FPL SPPCRC rate-class determinant boundary

## Purpose

This pass tests whether the public Florida PSC record exposes the denominator
that converts an approved FPL Storm Protection Plan Cost Recovery Clause
(SPPCRC) factor into a class-level billed amount. It uses FPL's public 2026
projection Form 5P / related Form 4P schedules in the May 1, 2025 filing and
preserves the filing's scenario: the July 11, 2025 alternative in which the
2025 Rate Case Settlement is not approved. The structured [determinant
table](data/capital-flow-fpl-sppcrc-rate-class-determinant-boundary-2026-09-16.csv)
keeps blank billing-kW fields blank rather than imputing them.

## What the source exposes

The Form 5P schedule provides, by rate-class grouping, projected sales at meter
(kWh), projected billed kW at meter where the rate class uses a demand factor,
total SPPCRC cost, demand/customer-related cost components, and the resulting
factor. Form 4P provides the allocation percentages and demand framework behind
the schedule. The total projected sales denominator is `128,430,086,092 kWh`.

This is a material upgrade over a factor-only observation:

`approved total requirement -> class allocation -> projected kWh / billed kW -> factor`

It still is not a collection ledger. The schedules are projections, not actual
meter reads, invoices, receipts, cash application, or a Distribution Inspection
sub-ledger. The total SPPCRC cost also includes programs beyond Distribution
Inspection. Therefore the determinant table cannot be multiplied by a factor and
called Distribution Inspection cash, and it cannot establish the source of
funds or a return on the specific program.

The same May 1, 2025 testimony also makes the recovery formula visible. FPL
states that projected capital revenue requirements include debt and equity
return grossed up for income taxes on average monthly net investment, including
construction work in progress, plus depreciation and amortization; the
identified recoverable costs are allocated to retail customers using separation
factors. The filing reports `$859.244393M` of total jurisdictional 2026 revenue
requirements. This is regulatory recovery mechanics and an aggregate
denominator, not a Distribution-Inspection-specific customer receipt or
common-owner return.

## Evidence classification

- `public-projection-denominator-visible`: class-level projected sales and/or
  billed-kW denominator is visible in the filed schedule.
- `not-category-cash`: the denominator and factor remain aggregate SPPCRC
  projection inputs rather than Distribution Inspection collections.
- `not-actual-collection`: no actual bill, cash receipt, remittance, or
  settlement join is established.

This moves Q-11 from a rate-class-factor boundary to a rate-class-determinant
boundary, but it does not promote Q-11 to owner cash or return evidence.

## Next falsifiable upgrade

Obtain a non-confidential 2026 actual/estimated or final true-up Form 5P / Form
1E–8E workpaper with actual class determinants and a Distribution Inspection
program allocation; then reconcile the resulting billed amount to FPL's
category-specific receivable/collection ledger. A successful promotion would
require the same period, program scope, rate-class determinant, billed amount,
collected cash, and source-of-funds treatment to join without an allocation
assumption.

## Source

- [FPL May 1, 2025 filing, including Form 5P and related Form 4P schedules](https://www.floridapsc.com/library/FILINGS/2025/03306-2025/03306-2025.pdf)
- [Florida PSC final order PSC-2025-0439-FOF-EI](https://www.floridapsc.com/pscfiles/library/filings/2025/15236-2025/15236-2025.pdf) — confirms the alternative schedule is the non-settlement scenario and separately states the approved conditional factors.
