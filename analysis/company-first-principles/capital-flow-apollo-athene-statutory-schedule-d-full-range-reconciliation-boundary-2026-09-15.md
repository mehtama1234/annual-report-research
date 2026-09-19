# Apollo–Athene Statutory Schedule D Full-Range Reconciliation Boundary

Research date: `2026-09-15`

## Purpose

Promote the existing Athene Schedule D full-range parser output into the
combined investment-research proof chain while preserving the distinction
between portfolio population and reconciled return evidence.

## Evidence

The 2025 Athene statutory statement parser produces `8,648` rows across the
located Schedule D Part 1 Section 1 issuer-credit range and Section 2
asset-backed-security range:

- `3,418` issuer-credit rows
- `5,230` asset-backed-security rows
- `8,648` CUSIPs and maturity-date fields
- `8,258` rows with a populated parsed book/adjusted-carrying-value field

The initial positional parser sums did not reconcile. After the
coupon-decimal/NAIC-marker correction documented in the [reconciliation
upgrade](capital-flow-apollo-athene-statutory-schedule-d-reconciliation-upgrade-2026-09-15.md),
the corrected section totals now reconcile within one dollar. The original
pre-correction diagnostic was:

| Section | Parsed book value | Verification reference | Coverage |
| --- | ---: | ---: | ---: |
| Issuer credit | `$85.338022455B` | `$85.388493720B` | `99.9409%` |
| Asset-backed securities | `$73.855727313B` | `$73.463901477B` | `100.5334%` |

The corrected totals are `$85,388,493,721` versus `$85,388,493,720` for
issuer credit and `$73,463,901,478` versus `$73,463,901,477` for ABS.

## What this proves

The legal-entity portfolio can now be examined at full-range CUSIP population
scale rather than only through selected named rows, with section totals
reconciled by the corrected parser. The output supports
prioritizing issuer, wrapper, ABS, and private-credit routes for the next
income, proceeds, impairment, and liability-cost joins.

## Boundary

This is a population and reconciliation boundary, not final statutory return
proof. The parser still uses dense-PDF positional numeric fields; missing or
shifted book-value columns and page/row boundaries remain unresolved. The
output therefore does not prove final Schedule D totals, borrower destination,
asset-level cash receipts, liability-cost spread, or Apollo common-owner cash.

## Next test

Correct blank-column and row-boundary handling, rerun the full-range parser,
reconcile both sections to statutory verification totals, then join named
holdings to investment income, disposals, impairments, liability funding cost,
and realized cash.

## Safe claim

`Athene's full located Schedule D ranges now provide 8,648 normalized legal-
entity rows and approach the two section-level statutory book-value references;
the population is source-routed and useful for prioritization, but remains
below reconciled asset-level return proof.`
