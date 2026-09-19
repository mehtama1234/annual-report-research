# Apollo–Athene SVF II Finco public-search refresh

Research date: `2026-09-16`

## Question

Does the public filing record convert Athene's same-CUSIP SVF II Finco rows—especially `G7741@-AC-4`—into borrower paydown cash, a settlement record, or a realized return?

## Result

`evidence-insufficient` for cash-loop or return promotion.

The SEC-hosted 2025 Athene Holding Ltd. Form 10-K confirms the legal-entity
perimeter and reports `SVF II Finco Cayman LP` as a 2025 investment
concentration of `$2.186B`. Its statutory Schedule D parser output identifies
three same-issuer CUSIPs at year-end:

| CUSIP | Description | Year-end book value | Year-end fair value | Disposal consideration candidate | Disposal type |
| --- | --- | ---: | ---: | ---: | --- |
| `G7741@-AC-4` | SVF II Finco (Cayman) LP | `$1,292.266M` | `$1,292.266M` | `$2,089.548M` headline; `$50.751M` selected cash-like | Mixed paydown / tax-free exchange |
| `G7741@-AD-2` | SVF II Finco (Cayman) LP | `$691.911M` | `$691.911M` | `$19.047M` | Paydown |
| `G7741@-AE-0` | SVF II Finco II B3 Upsize | `$201.276M` | `$201.408M` | `$31.592M` | Apollo Global Securities, LLC |

The [structured search record](data/capital-flow-apollo-athene-svf-ii-finco-public-search-refresh-2026-09-16.csv)
and [row-composition boundary](capital-flow-apollo-athene-svf-ii-finco-row-composition-boundary-2026-09-16.md)
preserve the source rows and classification logic.

The three year-end fair-value rows sum to approximately `$2.1856B`, which
rounds to the `$2.186B` concentration disclosed by Athene. This is a useful
issuer/denominator cross-check. The AC-4 `$2.089548B` headline is an aggregate
of five disposal rows: the detailed parser classifies `$50.751M` as selected
paydown-like cash candidates and `$2.038797B` as tax-free-exchange/transfer
holds. Neither bucket establishes a bank settlement, a borrower repayment, or
cash available to Athene or Apollo.

The filing also contains no executed settlement statement, custodian receipt,
borrower notice, collateral-paydown schedule, trustee remittance, lot-level
continuity, liability-cost allocation, or realized-return calculation for the
SVF II Finco route. The public search found independent insurer statutory
references to SVF II Finco and related CUSIPs, but those observations are
cross-checks of the wrapper name and instrument identifiers, not evidence of
Athene's receipt or borrower economics.

## Decision

The SVF II Finco route is promoted from a raw high-dollar same-CUSIP candidate
to a named issuer and concentration-reconciled proof target. It is not
promoted to `promotion-ready` for borrower cash, settlement, liability-
adjusted return, or Apollo common-owner cash.

## Required next documents

Prioritize the SVF II Finco note purchase/refinancing documents, paydown or
redemption notice, trade confirmation, custodian settlement ledger, borrower
payoff record, trustee report, and Athene investment-income/realized-gain
support. The decisive join is CUSIP + lot + settlement date + receiving
account + borrower/collateral ledger + liability/funding allocation.

## Safe claim

`Athene's 2025 public filing confirms a $2.186B SVF II Finco concentration and
three same-issuer statutory rows that reconcile to that rounded amount. The
AC-4 row has a $2.090B aggregate consideration field, but only $50.751M is
currently classified as selected cash-like paydown candidates and $2.039B as
tax-free-exchange/transfer holds; public evidence does not prove settlement
cash, borrower repayment, or realized return.`

## Sources

- [Athene 2025 Form 10-K filing directory](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000013)
- [Athene 2025 concentration table](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000013/R68.htm)
- [Arch Mortgage Insurance Company 2025 annual statement search lead](https://s205.q4cdn.com/950744987/files/doc_downloads/Arch-Mortgage-Insurance-Company-Annual-Statement-2025.pdf)
- [Unum 2025 annual statement search lead](https://s201.q4cdn.com/630564768/files/doc_downloads/2026/03/62235_54_L_2025_O_M_1_0_NA_PI.pdf)
