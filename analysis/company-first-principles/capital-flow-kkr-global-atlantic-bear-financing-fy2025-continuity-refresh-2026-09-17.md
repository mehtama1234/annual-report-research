# Capital Flow KKR Global Atlantic Bear Financing FY2025 Continuity Refresh

Research date: `2026-09-17`

## Purpose

This pass checks the official FY2025 Accordia annual statement after the FY2024
credit-agreement refresh. It tests whether the Bear Financing legal-entity and
instrument observation persists into the next statutory period.

## FY2025 result

The FY2025 statement repeats the January 5, 2024 credit-agreement disclosure:
Accordia committed to issue a `$245,000,000` senior loan to 2023 Bear Financing
L.P., and both entities are indirect KKR subsidiaries.

Schedule D page `239` repeats the matching row:

| Field | FY2024 | FY2025 |
|---|---:|---:|
| CUSIP / issuer | `90231*-AA-0` / `2023 BEAR FINANCING L.P.` | same |
| Book-adjusted carrying value | `$202.125M` | `$202.125M` |
| Fair value | `$202.7718M` | `$202.145213M` |
| Stated rate | `8.500%` | `8.500%` |
| Effective rate | `8.612%` | `6.999%` |
| Interest due/accrued | `$6.585906M` | `$6.585906M` |
| Interest received | `$11.604153M` | `$17.419245M` |
| Acquired / maturity date | `01/05/2024` / `01/05/2039` | same |

## Interpretation

The repeated issuer, CUSIP, book value, acquired date, maturity, and stated rate
provide a useful period-continuity control. The fair-value and effective-rate
changes are observations that require accounting and market-context review;
they are not realized gains or a cash-return calculation.

The increase in the statutory interest-received field from `$11.604153M` to
`$17.419245M` is not by itself a coupon cash settlement ledger. It could reflect
period length, collection timing, accrued-versus-received classification, or
other statutory presentation. The filing does not provide a loan-level bank
statement, draw ledger, repayment schedule, or liability-cost allocation.

## QoE / financial-integrity controls

- Same CUSIP and book value across periods support continuity, not settlement.
- Interest-received growth must not be treated as yield expansion without a
  period-matched denominator and cash/accrual reconciliation.
- Effective-rate movement must not be treated as realized return.
- The `$245M` commitment must not be added to the `$202.125M` Schedule D book
  value.

These are reconciliation prompts, not manipulation findings.

## Safe claim

`The official FY2025 Accordia annual statement independently repeats the $245M Bear Financing credit-agreement and KKR-affiliate disclosure and the matching CUSIP 90231*-AA-0 / 2023 Bear Financing L.P. row. Book value remains $202.125M; interest received rises from $11.604153M in FY2024 to $17.419245M in FY2025, while fair value and effective-rate fields change. This proves period continuity and statutory income observability, not draw, bank settlement, borrower use, liability-adjusted spread, repayment, or KKR owner cash.`

## Decision

`bear-financing-fy2025-statutory-continuity-visible; cash-accrual-draw-and-return-open`

## Primary source

[Global Atlantic / Accordia FY2025 annual statement](https://www.globalatlantic.com/content/dam/global-atlantic/investors/financial-statements/annual-and-quarterly-statements/accordia-4q-2025-quarterly-statements.pdf)
