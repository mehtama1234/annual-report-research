# FPL 2026 SPPCRC rate-class factor boundary

Research date: `2026-09-16`

## Purpose

This artifact captures the rate-class factors stated in Florida PSC Order No.
PSC-2025-0439-FOF-EI for the conditional scenario in which the 2025 FPL Rate
Case Settlement is approved. The structured [factor table](data/capital-flow-fpl-2026-sppcrc-rate-class-factor-boundary-2026-09-16.csv)
preserves the factor unit, class grouping, source, and evidence boundary.

## What is now visible

The order provides class-level 2026 SPPCRC factors, including residential
`$0.00995/kWh`, general-service non-demand `$0.00927/kWh`, general-service
demand `$1.80/kW`, large-demand factors from `$0.19/kW` to `$1.81/kW`, and
separate RDC/SDD factors for SST classes. This is direct evidence of the
rate-design output applied to bills during the 2026 period under the stated
scenario.

## What remains unproven

A rate factor is not a billing determinant, invoice, cash receipt, or
Distribution Inspection allocation. To calculate category customer cash, the
research still needs class usage/demand determinants, the program-level
allocation schedule, billed amounts, collection timing, and reconciliation to
FPL's cash or receivable records. The factor table also has a scenario boundary:
the order presents separate factors depending on whether the rate-case
settlement is approved.

## Decision

`rate-class-factor-visible; category-cash-unproven`

This advances Q-11's regulatory chain to:

```text
approved program -> total revenue requirement -> rate-class factor -> bill application
```

It does not complete:

```text
bill determinant -> category billed cash -> collected cash -> source of funds -> return
```

The factor must not be multiplied by an invented usage base or treated as
Distribution Inspection revenue.

## Primary source

[Florida PSC Order No. PSC-2025-0439-FOF-EI](https://www.floridapsc.com/pscfiles/library/filings/2025/15236-2025/15236-2025.pdf),
Issue 7A, pages 11–13, states the conditional 2026 FPL SPPCRC class factors;
Issue 8A states that they apply from the first January 2026 billing cycle
through the last December 2026 billing cycle.
