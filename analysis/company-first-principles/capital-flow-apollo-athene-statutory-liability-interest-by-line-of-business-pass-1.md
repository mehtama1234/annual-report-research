# Apollo/Athene statutory liability-interest allocation by line of business pass 1

Research date: `2026-09-18`

## What the filing adds

The 2025 Athene statutory statement exposes the same liability-side line at
three useful levels:

- Summary of Operations / Analysis of Operations by Lines of Business summary,
  page 8: `$5.890696798B` of “Interest and adjustments on contract or
  deposit-type contract funds”;
- Individual Annuities, page 11: `$5.882288174B`; and
- Group Annuities, page 12: `$8.408625M`.

The two business-line values sum to `$5.890696799B`, one dollar above the
summary line. The one-dollar difference is retained as a source/extraction
control rather than silently normalized.

Exhibit 7, page 31, separately reports `$2.649832829B` of “Investment earnings
credited to the account” across deposit-type contract categories. It also
reports a year-end deposit-type balance of `$64.424636640B` before reinsurance
and `$64.259784362B` after reinsurance.

## Interpretation

This upgrades the earlier same-period burden screen from a single summary line
to a business-line allocation control. The visible burden is overwhelmingly
associated with individual annuities (`99.8573%` using the summary denominator)
with a small group-annuities component (`0.1427%`). The percentages do not sum
to exactly 100% because of the one-dollar source difference and are shown only
as orientation.

Exhibit 7 is a separate control. “Investment earnings credited” is not
automatically equivalent to Summary of Operations line 17: line 17 includes
interest and adjustments, while Exhibit 7 is a deposit-type-contract account
roll-forward. The two should not be netted or substituted without a formal
accounting bridge.

## Boundary

The packet still does not provide product/block-level credited rates, reserve
duration, surrender behavior, hedge allocation, investment expenses, taxes,
credit losses, capital charges, or legal-entity-to-Apollo residual cash. The
allocation therefore remains a liability burden control, not a normalized
spread, distributable cash, return, or owner-cash conclusion.

Structured values are in the [line-of-business allocation CSV](data/capital-flow-apollo-athene-statutory-liability-interest-by-line-of-business-pass-1.csv).

## Decision

`business-line-liability-allocation-visible; product-level-spread-and-owner-cash-open`

The next promotion-quality object is a product/reserve-block workpaper or
equivalent source that reconciles credited rates and liability costs to the
individual- and group-annuity totals, followed by a full legal-entity expense,
hedge, tax, capital, and common-owner bridge.
