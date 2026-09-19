# Apollo–Athene statutory small parenthetical gain/loss boundary

Research date: `2026-09-15`

The selected Eliant Invest Holding LP B Schedule D disposal row provides a
useful parser boundary for the statutory return lane.

## Observed row

The raw Schedule D Part 4 extraction for CUSIP `28655*-AA-7` shows a
`$356.444966M` consideration-like sequence, a `$205.615636M` book-value-like
field, and a small parenthetical `(18)` appearing in the row. The page-specific
interpretation pass preserves that `(18)` as a candidate `-$18` gain/loss while
keeping the larger consideration fields separately identified.

## Safe interpretation

This is not a realized-return promotion. The raw PDF text and parser output
show that a small parenthetical token exists, but the full Schedule D column
geometry, lot continuity, settlement account, borrower receipt, liability-cost
allocation, and asset-level return are still not joined. The row therefore
advances from “parser missed or shifted a small value” to “small token visible,
column semantics held pending full page reconciliation.”

| Field | Current safe reading |
| --- | --- |
| Consideration-like amount | `$356.444966M` candidate, confirmed by the selected schedule-layout pass |
| Book-value-like amount | `$205.615636M` candidate |
| Small parenthetical | `-$18` candidate gain/loss token |
| Cash-like status | Consideration-safe candidate, not settled receipt proof |
| Return status | Not promoted |

## What remains open

- full Part 4 column reconciliation and page geometry;
- lot-level continuity between holding and disposal;
- settled receipt or custodian remittance;
- borrower, collateral, and use-of-proceeds cash;
- period-matched liability cost and capital burden; and
- Athene/Apollo allocation and final return.

Source artifacts: [raw text inspection](data/capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-pass-1.csv)
and [page-specific column interpretation](data/capital-flow-apollo-athene-statutory-cusip-column-interpretation-pass-1.csv).
