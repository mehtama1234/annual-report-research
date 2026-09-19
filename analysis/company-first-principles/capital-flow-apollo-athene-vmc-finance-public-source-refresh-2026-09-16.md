# Apollo–Athene VMC Finance public-source refresh

Research date: `2026-09-16`

## Question

Can public sources connect Athene's `91836A-AA-4` VMC Finance 2023-PV1
statutory disposal candidate to a defined borrower/collateral system and
return-relevant cash path?

## Result

`evidence-insufficient` for exact Athene settlement, borrower receipt,
collateral cash, liability-adjusted return, or Apollo common-owner cash, with a
limited issuer and asset-class upgrade.

The local Athene Schedule D parser identifies `91836A-AA-4`, VMC Finance
2023-PV1 LLC VMC 2023-PV1 Class A 6.498% due 01/19/40, as a disposal-only
`Paydown` candidate with approximately `$295.311M` of consideration and
`$11.061M` of interest/dividend fields. No year-end holding match is present in
the current parser.

Public deal-data identifies VMC 2023-PV1 as a commercial-mortgage ABS deal
with Varde Partners Inc. as parent. A later SEC-hosted 2026 CMBS collateral
term sheet names VMC 2023-PV1 as a previous securitization for one mortgage in
its new collateral pool. This confirms a commercial-real-estate
securitization context and suggests a loan/property lineage, but neither source
maps Athene's CUSIP to a specific loan, borrower, property, trustee account, or
payment.

## Decision

Promote VMC from an unexplained statutory issuer to a bounded Varde-linked
commercial-mortgage ABS research target. Do not promote the statutory
consideration to a settled Athene receipt, borrower repayment, property cash,
liability-adjusted spread, realized return, or common-owner cash.

## Next documents

Request the VMC 2023-PV1 offering document, mortgage-loan schedule, trustee or
master-servicer remittance reports, paydown/redemption notice, Athene trade and
custodian settlement records, and property-level borrower payment history.
Join principal, interest, servicing fees, losses, reserve releases, insurance
liability cost, and taxes before calculating a return.

## Safe claim

`Public sources place VMC Finance 2023-PV1 in a Varde-linked commercial-
mortgage ABS context and identify a later securitization reference to the
deal. Athene's $295.3M statutory disposal row remains a cash-like paydown
candidate, not proven settlement, borrower cash, collateral cash, or return.`

## Sources

- [VMC Finance LLC VMC 2023-PV1 deal profile](https://finsight.com/deal-68212-vmc-finance-llc-vmc-2023-pv1)
- [SEC-hosted BBCMS 2026-5C40 collateral term sheet](https://www.sec.gov/Archives/edgar/data/2104401/000153949726000066/n5566_x4-ts.htm)

