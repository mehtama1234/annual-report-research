# Apollo–Athene Apollo Debt Solutions BDC public-source refresh

Research date: `2026-09-16`

## Question

Can public sources identify Athene's `03770D-AC-7` disposal candidate as an
exact Apollo Debt Solutions BDC debt instrument and connect it to a return-
relevant issuer and funding perimeter?

## Result

`partial-upgrade` for exact instrument identity, issuer, trustee, principal,
coupon, and maturity; `evidence-insufficient` for Athene settlement, borrower
repayment, liability-adjusted return, or Apollo common-owner cash.

The local Athene Schedule D parser identifies `03770D-AC-7`, Apollo Debt
Solutions BDC Senior Unsecured 6.700% due 07/29/31, as a disposal-only market-
sale or counterparty-cash candidate with approximately `$215.832M` of
consideration and `$8.587M` of interest/dividend fields on March 4, 2025.

The SEC-filed second supplemental indenture independently confirms the exact
CUSIP `03770DAC7`, the Apollo Debt Solutions BDC issuer, the 6.700% coupon,
July 29, 2031 maturity, a `$600M` initial principal amount, and U.S. Bank
Trust Company as trustee. This upgrades the route from a parser description to
an exact public debt instrument and issuer obligation.

Apollo's public BDC prospectus provides the broader credit-portfolio and
funding context. The note is a debt claim against Apollo Debt Solutions BDC,
not a direct claim on a named underlying borrower. Athene's statutory row is
classified as `Various` and is disposal-only, so the public record does not
show whether Athene sold the note to a particular counterparty, how the sale
price was settled, or how the BDC used or received funds from any underlying
borrower.

The companion [coupon-carry sensitivity](capital-flow-apollo-athene-apollo-debt-solutions-coupon-carry-sensitivity-2026-09-16.md)
uses the `$600M` issue size, `6.700%` coupon, and `$215.832M` statutory
consideration only to show a par-equivalent gross annual carry proxy of
approximately `$14.461M`. It is an illustrative return input, not observed
Athene income or a realized, liability-cost-adjusted return.

The [issuer cash/return bridge](capital-flow-apollo-athene-apollo-debt-solutions-issuer-cash-return-bridge-2026-09-16.md)
now adds Q2 2026 structured-fact observations for issuer-wide gross investment
income (`$1.153510B`), net investment income (`$599.045M`), borrowing interest
expense (`$323.289M`), quarter-end cash (`$857.638M`), and debt face amount
(`$16.568B`), plus `$312.890M` of cash interest paid. These constrain the issuer perimeter but do not allocate income,
cash, or funding cost to Athene's candidate note.

## Decision

Promote Apollo Debt Solutions BDC to an exact instrument-level Apollo credit
route. Do not promote the `$215.8M` statutory consideration to borrower
repayment, BDC cash receipt, Athene settled cash, liability-adjusted spread,
realized IRR/NPV, or Apollo common-owner cash.

## Next documents

Request Athene's trade confirmation and custodian settlement ledger, the BDC
note offering/closing records, trustee payment history, BDC quarterly debt and
portfolio schedules, and any counterparty or transfer records. Reconcile
principal, accrued interest, sale price, BDC funding cost, portfolio income,
losses, distributions, and the residual available to Apollo owners.

## Safe claim

`The SEC indenture confirms that Athene's 03770D-AC-7 row names a $600M Apollo
Debt Solutions BDC 6.700% senior note due July 29, 2031, with U.S. Bank Trust as
trustee. The $215.8M Athene disposal is an exact instrument-level market-sale
candidate, not proven borrower repayment, Athene settlement, liability-
adjusted return, or Apollo common-owner cash.`

## Sources

- [SEC second supplemental indenture](https://www.sec.gov/Archives/edgar/data/1837532/000119312524187649/d849659dex42.htm)
- [Apollo Debt Solutions BDC prospectus](https://www.apollo.com/content/dam/apolloaem/documents/fund-documents/ads-prospectus.pdf)
