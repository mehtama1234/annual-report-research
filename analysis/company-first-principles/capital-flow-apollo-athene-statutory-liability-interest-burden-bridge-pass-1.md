# Apollo/Athene statutory liability-interest burden bridge pass 1

Research date: `2026-09-18`

## Source-controlled same-period burden

Athene's 2025 Summary of Operations reports:

- `$12.732699320B` of net investment income; and
- `$5.890696798B` of “Interest and adjustments on contract or deposit-type
  contract funds.”

The second line is a real legal-entity, same-period liability-side burden
observation. It is materially stronger than using a different-period management
cost-of-funds figure as if it were the statutory asset-level cost.

## Bounded screens

| Screen | Calculation | Result | Status |
|---|---:|---:|---|
| Net investment income less contract/deposit interest adjustments | `$12.732699320B - $5.890696798B` | `$6.842002522B` | bounded liability-burden screen |
| Reconciled page-18 collected bond income less contract/deposit interest adjustments | `$8.127852536B - $5.890696798B` | `$2.237155738B` | bounded bond-versus-liability screen |
| Gross collected investment income less contract/deposit interest adjustments | `$13.601183683B - $5.890696798B` | `$7.710486885B` | bounded gross-income screen |

The structured calculations are in the [liability-interest burden CSV](data/capital-flow-apollo-athene-statutory-liability-interest-burden-bridge-pass-1.csv).

## Boundary

These are not final spreads or owner cash. Line 17 does not by itself disclose
product-level credited rates, reserve duration, surrender behavior, hedging,
reinsurance allocation, investment expenses, taxes, credit losses, capital
charges, preferred/NCI claims, or the legal-entity-to-Apollo residual. The
bond-versus-liability screen also compares a reconciled collected bond category
with a liability expense/adjustment line, so it is a directional burden screen,
not a full accounting spread.

## Decision

`same-period-liability-interest-line-visible; normalized-spread-and-owner-cash-open`

The next promotion-quality evidence is Exhibit 5/7 or an equivalent liability
workpaper that allocates the `$5.890696798B` line by reserve/deposit block and
credited-rate mechanics, followed by legal-entity expenses and capital claims.
