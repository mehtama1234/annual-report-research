# Apollo/Athene Schedule BA income-category boundary pass 1

## Controlled observations

| source object | collected/current-year amount | earned/current-year amount | safe interpretation |
|---|---:|---:|---|
| Schedule BA Part 1 coordinate rows, page-5825 control | `$237,086,006` parsed vs `$237,086,005` control | not separately presented | Part 1 row-level investment-income column reconciles within `$1` |
| Exhibit of Net Investment Income, page 18, “Other invested assets” | `$(185,080,219)` | `$(132,204,517)` | Broader statutory category reports negative collected and earned income |
| Schedule BA Part 3 coordinate rows | `$156,037,953` investment-income column | not separately presented | Disposal-event population includes income fields, but cannot be added to Part 1 as recurring income without event/perimeter matching |

## Boundary

The positive Part 1 row-control amount and the negative page-18 “Other invested
assets” category do not reconcile as a simple same-perimeter income bridge.
Possible explanations include the page-18 category perimeter, income from
disposed/transferred assets, valuation or alternative-investment accounting,
classification differences, and the distinction between row-level Schedule BA
income fields and the exhibit’s collected/earned presentation. The current
evidence does not identify which explanation dominates.

Accordingly:

1. Do not use `$237.086M` as collected BA cash.
2. Do not use `$(185.080M)` or `$(132.205M)` as a Schedule BA loss without the category roll-forward.
3. Do not add Part 1 and Part 3 income; Part 3 rows are event-level and may overlap the year’s holdings or dispositions.
4. Keep the legal-entity cash bridge at its aggregate statutory level until the income exhibit, BA populations, and disposed/transferred lots are reconciled.

This is a decisive quality-of-earnings boundary for the insurance route: the
asset denominator is controlled, but income definition and cash attribution are
not yet joined at the named-asset level.

The [Part 1 income review queue](capital-flow-apollo-athene-statutory-schedule-ba-part1-income-review-queue-pass-1.md) prioritizes the top 30 positive row-level income fields. They contribute `$182.801M`, or `77.10%` of the parsed Part 1 income total. Several are blank-identifier alternative/loan rows, and some have income with zero or unusual book-value fields, so the queue is a source-review order—not a yield ranking.
Eleven of the top 30 identifiers/rows have a visible Part 3 event; only five
carry an exact coordinate-column `Sale` signal. This is a useful income-to-event
screen, but it does not prove that the income was collected, that the event is
the same lot, or that disposal consideration reached Athene cash.

The underlying controls are in the [Schedule BA parser pass](capital-flow-apollo-athene-statutory-schedule-ba-full-range-parser-pass-1.md) and the [legal-entity income/cash bridge](capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.md).
