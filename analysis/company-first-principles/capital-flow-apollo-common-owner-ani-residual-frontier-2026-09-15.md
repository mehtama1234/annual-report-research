# Apollo common-owner ANI-to-cash residual frontier

Research date: `2026-09-15`

## Purpose

Apollo's reported H1 adjusted net income provides an earnings numerator, while
the parent-use artifact identifies disclosed common, repurchase, and preferred
cash uses. This frontier shows how much of the selected parent-use burden
would remain under explicit 0%, 50%, and 100% conversion assumptions. It is a
cash-conversion sensitivity, not a reported free-cash-flow calculation.

## Frontier ($ millions)

```text
H1 adjusted net income                                      2,522
selected H1 parent uses:
  common dividends                                           654
  common-stock repurchases                                    729
  preferred dividends                                          49
selected parent uses                                        1,432
```

| Assumed H1 ANI cash conversion | Implied cash-equivalent pool | Less selected parent uses | Mechanical residual | Interpretation |
| ---: | ---: | ---: | ---: | --- |
| `0%` | `$0M` | `$1.432B` | `($1.432B)` | No ANI conversion; uses require other sources or existing cash |
| `50%` | `$1.261B` | `$1.432B` | `($171M)` | Half conversion still does not cover selected uses |
| `100%` | `$2.522B` | `$1.432B` | `$1.090B` | Full conversion leaves a mechanical surplus before other claims |

The calculation is deliberately narrow:

```text
assumed cash-equivalent ANI
  - common dividends paid
  - common-stock repurchases paid
  - preferred dividends paid
  = mechanical residual frontier
```

## What this proves

- The selected H1 parent uses total `$1.432B` and are source-backed cash uses.
- Even full ANI conversion is an assumption, not an observed cash receipt.
- The cash-conversion assumption materially changes the residual from
  `($1.432B)` to `$1.090B`.
- The frontier makes the missing cash-quality bridge measurable rather than
  silently equating adjusted earnings with owner cash.

## What this does not prove

- Fee-entity collections or Athene-to-AGM receipts;
- regulated, restricted, policyholder, VIE, NCI, or preferred cash availability;
- debt, tax, compensation, acquisition, capital-retention, or working-capital
  requirements beyond the selected uses;
- whether the H1 parent uses were funded by H1 ANI, existing cash, debt, or
  subsidiary distributions; or
- a positive common-owner residual.

Proof grade: `mechanical earnings-to-selected-use frontier confirmed; actual
common-owner cash conversion and residual unresolved`.

Sources: [Apollo primary-source upgrade](capital-flow-apollo-athene-primary-source-upgrade-2026-09-15.md) and [Apollo parent-use coverage frontier](capital-flow-apollo-athene-parent-use-coverage-frontier-2026-09-15.md).
