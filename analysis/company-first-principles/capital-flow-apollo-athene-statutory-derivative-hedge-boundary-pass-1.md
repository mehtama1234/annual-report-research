# Apollo/Athene statutory derivative and hedge boundary pass 1

Research date: `2026-09-18`

## Source-controlled hedge evidence

Athene's 2025 statutory notes identify a liability-linked hedge architecture:

- fixed indexed and index-linked annuities use OTC options, call options,
  call spreads, variance swaps, and futures to hedge interest credited from
  index movements;
- swaptions hedge interest-rate exposure associated with minimum crediting
  rates;
- interest-rate swaps alter exposure arising from asset/liability mismatches;
- futures-related margin changes can enter Summary of Operations through
  investment income; and
- derivative cash flows are reported through miscellaneous cash-flow lines.

Page 55 quantifies `$2.482135218B` of gross derivative assets, including
`$2.479627050B` admitted and `$2.508168M` nonadmitted. The same page reports
`$2.623563M` of aggregate deferred interest and `$112.792182M` of cumulative
PIK interest in current principal balances.

## Interpretation

This is a real hedge and accounting-mechanism upgrade to the liability-burden
bridge. It shows why subtracting the statutory line 17 from net investment
income cannot be called a normalized spread without accounting for indexed
crediting, rate mismatch hedges, derivative income recognition, and accrued or
PIK components.

The quantified derivative amounts are scale controls only. They do not tell us
the annual premium, cash settlement, realized/unrealized gain or loss,
effectiveness, product allocation, or whether the hedge protects individual
versus group annuities.

Structured values are in the [derivative hedge boundary CSV](data/capital-flow-apollo-athene-statutory-derivative-hedge-boundary-pass-1.csv).

## Decision

`liability-linked-hedge-mechanism-and-derivative-scale-visible; quantified-hedge-cost-and-owner-cash-open`

The next source is the Schedule DB derivative detail plus the related statutory
cash-flow, investment-income, and liability/product allocation workpaper.
