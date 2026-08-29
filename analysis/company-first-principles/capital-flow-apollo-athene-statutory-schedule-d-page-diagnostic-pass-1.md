# Capital Flow Apollo Athene Statutory Schedule D Page Diagnostic Pass 1

## Purpose

This pass converts the Schedule D reconciliation failure into a page-level correction worklist.

It asks:

`Which Athene Schedule D pages have missing or weak book-value parser coverage, and where should the numeric-column correction work start?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-page-diagnostic-pass-1.csv`

The diagnostic script is:

`scripts/reconcile-athene-schedule-d-parser.py`

The upstream reconciliation diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.md`

The high-priority page inspection is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-high-priority-page-inspection-pass-1.md`

## Short Answer

`The page diagnostic creates a 192-row correction worklist across the located Schedule D issuer-credit and ABS ranges after the ABS blank-column parser correction and statutory CUSIP-marker row-start correction. It flags 12 high-priority pages, 26 medium-priority pages, and 154 coverage-visible pages. The remaining worst missing-book pages are concentrated in Schedule D Part 1 Section 2 ABS pages, led by pages 5970, 5971, 5917, 5937, 5939, 5969, 5972, 5927, 5916, 5941, 5962, and 5940.`

## Page Status Summary

| Page Status | Pages |
|---|---:|
| `page-parser-coverage-visible` | `154` |
| `medium-priority-column-correction` | `26` |
| `high-priority-column-correction` | `12` |

## Worst Missing-Book Pages

| Page | Schedule | Parser Rows | Missing Book-Value Rows | Book Coverage | Status |
|---:|---|---:|---:|---:|---|
| `5970` | Schedule D Part 1 Section 2 | `45` | `45` | `0.000000` | high-priority-column-correction |
| `5971` | Schedule D Part 1 Section 2 | `45` | `41` | `0.088889` | high-priority-column-correction |
| `5917` | Schedule D Part 1 Section 2 | `45` | `19` | `0.577778` | high-priority-column-correction |
| `5937` | Schedule D Part 1 Section 2 | `45` | `19` | `0.577778` | high-priority-column-correction |
| `5939` | Schedule D Part 1 Section 2 | `45` | `18` | `0.600000` | high-priority-column-correction |
| `5969` | Schedule D Part 1 Section 2 | `43` | `18` | `0.581395` | high-priority-column-correction |
| `5972` | Schedule D Part 1 Section 2 | `30` | `13` | `0.566667` | high-priority-column-correction |
| `5927` | Schedule D Part 1 Section 2 | `45` | `12` | `0.733333` | high-priority-column-correction |
| `5916` | Schedule D Part 1 Section 2 | `36` | `12` | `0.666667` | high-priority-column-correction |
| `5941` | Schedule D Part 1 Section 2 | `47` | `10` | `0.787234` | high-priority-column-correction |
| `5962` | Schedule D Part 1 Section 2 | `45` | `10` | `0.777778` | high-priority-column-correction |
| `5940` | Schedule D Part 1 Section 2 | `44` | `9` | `0.795455` | high-priority-column-correction |

## What This Means

The reconciliation problem is now actionable.

The prior diagnostic said:

`full-range Schedule D parser visible, but not reconciled`

This page says:

`continue correction with ABS pages 5970, 5971, 5917, 5937, 5939, 5969, 5972, 5927, 5916, 5941, 5962, and 5940`

That is the right next move because the full-range output has high total field coverage, but specific pages show missing or shifted book-value columns.

## Boundary

This is still a parser diagnostic.

It does not prove:

1. final Schedule D totals
2. correct numeric assignment on every page
3. issuer-level income roll-up
4. borrower/originator destination
5. liability-cost spread
6. asset-level cash return

## Decision

`apollo-athene-statutory-schedule-d-page-diagnostic-ready-column-correction-targets`

The next correction pass should start with the high-priority ABS pages and inspect raw PDF text around missing book-value fields.

## Safe Claim

`The Athene Schedule D page diagnostic turns the near-reconciled full-range parser into a page-level correction worklist. After the blank-column and row-start corrections, it identifies 12 high-priority pages and 26 medium-priority pages for numeric-column correction, with the worst gaps concentrated in ABS pages. It does not yet make Schedule D fully reconciled or proof-grade.`

## Next Work

1. Use the high-priority page inspection rows to design blank-column-aware parsing.
2. Compare raw PDF text against parser token positions for missing book-value rows.
3. Add ABS-specific numeric-column correction.
4. Rerun full-range parser and reconciliation diagnostics.
5. Promote only if Section 1 and Section 2 book values reconcile to statutory verification totals.
