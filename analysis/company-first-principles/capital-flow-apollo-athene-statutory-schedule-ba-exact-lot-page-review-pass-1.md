# Apollo/Athene Schedule BA exact-lot page review pass 1

Research date: `2026-09-18`

## Purpose

This pass reviews the four strongest same-identifier continuity screens from
the corrected Schedule BA Part 1, Part 2, and Part 3 coordinate parsers. It
does not treat a book-value tie as proof of a single economic lot, a full
disposal, bank settlement, borrower repayment, or Apollo owner cash.

The structured output is [the exact-lot page-review CSV](data/capital-flow-apollo-athene-statutory-schedule-ba-exact-lot-page-review-pass-1.csv).

## Page-level review

| Identifier | Source continuity | What the source columns show | Classification | Promotion boundary |
|---|---|---|---|---|
| `309601-AE-2` | Part 1 p. 5817 → Part 2 p. 5826 → Part 3 p. 5831; `$4.000M` Part 1 book, `$4.000M` Part 3 book, `$4.000M` consideration | Part 3 disposal-nature column visibly says `Sale`; dates are 10/10/2017 → 09/30/2025; Part 1 income is `$141,883` | Source-column sale with exact book continuity | No bank receipt, settlement account, counterparty remittance, liability release, tax/fee, or parent residual is shown |
| `05565A-DW-0` | Part 1 p. 5819 → Part 2 p. 5827 → Part 3 p. 5832; `$4.499M` Part 1/Part 3 book and consideration | Part 2 visible amount is `$8.999M`, approximately twice the Part 1/Part 3 book; Part 3 nature field is blank; dates are 01/01/2025 → 02/28/2025 | Blank-nature, multi-row-or-multi-lot/transfer candidate | Do not call this a cash sale or use consideration as proceeds without row-level transaction and settlement evidence |
| `539439-BF-5` | Part 1 p. 5819 → Part 2 p. 5828 → Part 3 p. 5833; `$0.800M` Part 1/Part 3 book | Part 3 disposal-nature column visibly says `Sale`; consideration is `$793,592`; realized loss is `$(6,408)`; Part 2 visible amount is `$1.600M` | Source-column sale with exact book continuity, but multiple-lot warning | Consideration is not independently proven bank receipt; the doubled Part 2 amount requires lot interpretation |
| `639057-AT-5` | Part 1 p. 5820 → Part 2 p. 5828 → Part 3 p. 5833; `$6.245M` Part 1/Part 3 book and consideration | Part 2 visible amount is `$12.491M`, approximately twice the Part 1/Part 3 book; Part 3 nature field is blank; dates are 10/08/2025 → 12/01/2025 | Blank-nature, multi-row-or-multi-lot/transfer candidate | Do not call this a cash sale or use consideration as proceeds without row-level transaction and settlement evidence |

## Result

Two candidates have a visible `Sale` marker, and two have a blank disposal-
nature field. All four retain the same statutory limitation: the Schedule BA
consideration field is not a bank statement. The Part 2 amounts that are
approximately twice the Part 1/Part 3 book value are retained as a lot-count or
transfer warning, not forced into a one-lot cash bridge.

This advances the statutory route from quantitative continuity to source-column
classification. It does not promote any candidate to Athene cash return,
borrower repayment, liability-adjusted return, or Apollo common-owner cash.

## Primary evidence

- Athene Annuity and Life Company 2025 statutory statement, Schedule BA Part 1 pages `5817`, `5819`, and `5820`.
- Same statement, Schedule BA Part 2 pages `5826`, `5827`, and `5828`.
- Same statement, Schedule BA Part 3 pages `5831`, `5832`, and `5833`.
- Coordinate-controlled parser outputs: [Part 1](data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv), [Part 2](data/capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-parser-pass-1.csv), and [Part 3](data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv).
