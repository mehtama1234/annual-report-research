# Private-credit borrower promotion workbench

Research date: `2026-09-17`

## Purpose

This workbench turns the private-credit proof ladder into a promotion test. It
does not treat an insurer's statutory holding, a public wrapper, an arranger
announcement, or a fair-value mark as a funded lender cash flow.

The required chain is:

`lender or insurer legal entity -> instrument and facility -> borrower and use of proceeds -> funded principal -> collateral and senior claims -> borrower cash/debt service -> lender receipt -> repayment/recovery -> liability-adjusted return`

## Promotion matrix

| Route | What is visible | Missing promotion fields | Current grade | Next decisive package |
|---|---|---|---|---|
| KKR / Accordia -> Bear Financing | Accordia statutory row for `2023 Bear Financing L.P.`, CUSIP `90231*-AA-0`, `$202.125M` book, `$17.419M` interest received | Legal issuer resolution, private-placement terms, borrower/use, custodian allocation, repayment, liability/funds-held cost, parent remittance | Statutory issuer/income proxy | Private-placement package, custodian subledger, ALM allocation, repayment or maturity record |
| Apollo / Athene -> Concord | Athene same-CUSIP consideration candidate `$229.053M`; Concord wrapper, public ABS/collateral/use context, timely deal-level interest proxies | Athene trade/custody, trustee remittance, royalty collections, lot continuity, liability cost, parent allocation | Borrower/wrapper/use proxy | Athene custody record, trustee waterfall/remittance, collateral collections, legal-entity cash schedule |
| Ares -> Frontline / Bain | Ares lead-arranger/bookrunner role; Bain acquisition and growth purpose; SEC holder markers with `$198.675M` visible funded fair value and `$54.300M` unfunded commitments; SOFR + `4.75%–5.00%` markers and 2032 maturity cluster | Full facility size, Ares allocation, credit agreement, closing funds flow, collateral, borrower FCF/debt service, interest/principal receipts, payoff/recovery | Acquisition-facility role proxy | Credit agreement, lender allocation, closing funds flow, prior debt payoff, borrower debt-service schedule |

## Field-level status

| Field | Bear Financing | Concord | Frontline |
|---|---|---|---|
| Legal lender/holder entity | partial | partial | partial |
| Named instrument/security | partial; marker unresolved | observed wrapper/CUSIP route | partial instrument marker |
| Borrower legal entity | missing | proxy | observed operating borrower |
| Use of proceeds | missing | proxy | acquisition/growth purpose visible |
| Funded principal | book value only | candidate consideration only | fair value proxy only |
| Lender allocation | missing | missing | missing |
| Collateral and senior claims | missing | public wrapper/collateral context | senior-secured role marker; package missing |
| Borrower cash/debt service | missing | deal-level servicing proxy | missing |
| Lender receipt | statutory interest field only | trustee/receipt open | fair value/commitment only |
| Repayment/recovery | missing | deal-level proxy; Athene lot open | missing |
| Liability/funding cost | missing | policyholder/liability route open | vehicle funding cost open |
| Common-owner residual | missing | missing | missing |
| Promotion status | hold | hold | hold |

## QoE and financial-integrity controls

- Statutory interest is not borrower operating cash.
- Fair value is not funded principal, and an unfunded commitment is not a cash
  outflow.
- An arranger or bookrunner role does not prove that the manager funded the
  entire facility.
- A wrapper's collateral or refinancing description does not prove a specific
  insurer lot, borrower repayment, or trustee remittance.
- Coupon and effective yield are not realized lender return without principal,
  fees, losses, funding cost, timing, and repayment.
- A private-credit facility cannot enter a common-owner return model until the
  legal entity, source of funds, use, senior claims, and receipt route agree.

These are reconciliation controls, not allegations of misconduct.

## Adjacent-route exclusion: Atwell

The local Atwell packet is intentionally not promoted into the Ares/Frontline
route. An Atwell announcement identifies Advent International's March 2026
investment in the engineering, consulting, and construction-services company;
the separately preserved ABF Journal record describes a `$200M` senior credit
facility led by Bank of America. Neither document identifies Ares as lender,
the facility's funded draw, a lender allocation, borrower cash generation, or
repayment.

This is a useful source-integrity control because Atwell appears in the wider
private-credit and infrastructure discovery set. It may support a separate
`BofA-led facility -> Atwell -> infrastructure-services capacity` route, but it
must not be used to fill Ares/Frontline's missing facility size, Ares
allocation, or borrower cash waterfall.

## Decision

The private-credit lane is `qualified; promotion open; no-ranking`. Frontline
is the best public borrower/facility-purpose route; Concord is the best public
wrapper/use route; Bear Financing is the strongest statutory named-asset route.
They should not be pooled into one return comparison until each reaches the
same lender-allocation and cash-waterfall fields.

The machine-readable workbench is in the [private-credit promotion table](data/combined-investment-research-private-credit-promotion-workbench-2026-09-17.csv).

## Related records

- [Private-credit borrower proof ladder](combined-investment-research-private-credit-borrower-proof-ladder-2026-09-17.md)
- [Ares/Frontline primary-source refresh](capital-flow-ares-frontline-primary-source-refresh-2026-09-17.md)
- [Ares/Frontline facility cash-waterfall bridge](capital-flow-ares-frontline-facility-cash-waterfall-bridge-pass-1.md)
- [Apollo/KKR statutory named-asset selection](capital-flow-apollo-kkr-statutory-named-asset-selection-pass-1.md)
