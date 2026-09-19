# Apollo/Athene Schedule BA income-category reconciliation pass 1

Research date: `2026-09-18`

## Purpose

This pass makes the Schedule BA income-definition boundary arithmetic and
machine-checkable. It compares the coordinate-controlled Part 1 row-income
total, the page-18 `Other invested assets` collected/earned category, the Part
3 event-income population, and the top-30 income review screen.

The full page-18 category extraction is preserved separately in the [page-18
full-table pass](capital-flow-apollo-athene-statutory-page18-net-investment-income-full-table-pass-1.md)
and its [CSV](data/capital-flow-apollo-athene-statutory-page18-net-investment-income-full-table-pass-1.csv).

The structured output is [the income-category reconciliation CSV](data/capital-flow-apollo-athene-statutory-ba-income-category-reconciliation-pass-1.csv).

## Controlled result

| Test | Result | Safe interpretation |
|---|---:|---|
| Part 1 parsed income vs page-5825 control | `$237.086006M` vs `$237.086005M`; difference `$1` | Row-level statutory control is reconciled |
| Part 1 income minus page-18 `Other invested assets` collected amount | `$422.166225M` arithmetic difference | Perimeter mismatch, not cash shortfall or loss |
| Part 1 income minus page-18 `Other invested assets` earned amount | `$369.290523M` arithmetic difference | Perimeter mismatch, not missing receipt or recurring loss |
| Part 3 event-income population | `$156.037953M` | Event-level fields cannot be added to Part 1 without overlap control |
| Top 30 positive Part 1 rows / parsed Part 1 total | `77.10%` | Review-priority concentration, not a yield ranking |

## Interpretation

The positive Part 1 row-income control and the negative page-18 `Other
invested assets` category are not a simple same-perimeter income bridge. The
source may be using different category boundaries, and the Part 3 event rows
may include income associated with transfers or disposals that overlap the
year-end population. No residual is promoted to a loss, cash gap, or owner
cash.

The correct next proof object is a category roll-forward that explains the
relationship among the page-18 exhibit, Schedule BA Part 1 income, Part 3
event fields, and the legal-entity cash-flow statement. Until that exists:

- `$237.086M` remains a controlled statutory row-income field, not collected
  BA cash;
- `$(185.080M)` and `$(132.205M)` remain page-18 category observations, not
  Schedule BA losses; and
- `$156.038M` remains an event-population field, not additional income to add
  to Part 1.

This closes an arithmetic/documentation gap in the legal-entity bridge without
claiming a named-borrower receipt, asset-level return, liability-adjusted
spread, or Apollo common-owner cash.

## Primary evidence

- Athene Annuity and Life Company 2025 statutory statement, page `18` Exhibit of Net Investment Income and Schedule BA pages `5813–5835`.
- [Part 1 coordinate reconciliation](data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-reconciliation-pass-1.csv).
- [Part 1 income review queue](data/capital-flow-apollo-athene-statutory-schedule-ba-part1-income-review-queue-pass-1.csv).
- [Existing income-category boundary](capital-flow-apollo-athene-statutory-ba-income-category-boundary-pass-1.md).
