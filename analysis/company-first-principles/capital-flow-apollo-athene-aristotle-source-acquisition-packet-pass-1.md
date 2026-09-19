# Capital Flow Apollo Athene AP Aristotle Source-Acquisition Packet Pass 1

Research date: `2026-09-17`

## Purpose

This packet converts the AP Aristotle mixed-row resolution into an executable
source-acquisition queue. It is the next step after the [mixed-row resolution
pass](capital-flow-apollo-athene-aristotle-mixed-row-resolution-pass-1.md).

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-aristotle-source-acquisition-packet-pass-1.csv`

The question is:

`What documents would promote AP Aristotle from a statutory cash-like candidate to a documented settlement, borrower-use, Athene-allocation, liability-cost, and return chain?`

## Current evidence boundary

Athene's statutory rows identify CUSIP `00264#-AB-3` as AP Aristotle Holdings
LLC and show a year-end holding context with `28.317574M USD` of received
interest. The disposal parser separates two cash-like consideration
candidates—`250.704550M USD` labeled `Paydown` and `525.327798M USD` labeled
`Various`—for a combined `776.032348M USD`. A separate `6.588486M USD`
Interest Capitalization / Tax Free Exchange row remains a noncash or transfer
hold, with `38.433K USD` of associated interest/dividends.

The safe route is:

`Athene statutory holding -> AP Aristotle note -> paydown / counterparty event -> settlement evidence -> borrower or issuer use -> Athene allocation -> liability cost -> return`

Only the first link and a statutory cash-like consideration candidate are
currently visible. The route is not full cash proof.

## Acquisition queue and promotion gates

| Priority | Document family | Why it matters | Minimum promotion test | Current status |
|---:|---|---|---|---|
| 1 | Athene raw holding and disposal rows | Locks the exact lot, date, issuer text, transaction label, consideration, and interest fields. | CUSIP, date, lot/position identifier, and consideration reconcile to the selected `Paydown` and `Various` rows without mixing the tax-free exchange. | local row evidence visible; lot continuity open |
| 2 | AP Aristotle note purchase agreement, offering document, or private-placement term sheet | Establishes the legal instrument, issuer, coupon, maturity, principal terms, and financing counterparties. | The document identifies CUSIP `00264#-AB-3` or an unambiguous successor/old-security mapping and explains the relevant paydown or transfer. | source request required |
| 3 | Paydown, repayment, redemption, or settlement notice | Tests whether the `250.704550M USD` Paydown was settled cash and identifies the paying agent, date, principal, accrued interest, fees, and counterparty. | Notice plus settlement ledger or bank/custodian record agrees to principal and date. | not located in public perimeter |
| 4 | `Various` transaction support | Resolves whether the `525.327798M USD` row was a sale, maturity, repayment, transfer, or another counterparty event. | Transaction label, consideration, date, counterparty, and accounting treatment are explicit; noncash transfers are excluded. | classification candidate only |
| 5 | Borrower / issuer use-of-proceeds support | Connects financing proceeds to an operating, refinancing, or portfolio use. | Legal use-of-proceeds language or a populated funds-flow / payoff ledger ties the transaction to a stated use. | not located |
| 6 | Athene allocation, custodian statement, and trade ticket | Proves that statutory consideration became Athene-side settled cash or a defined asset movement. | CUSIP, date, quantity/principal, settlement amount, and receiving account/custodian agree to the statutory row. | not located |
| 7 | Liability-cost and ALM allocation support | Converts gross interest or proceeds into an asset-level spread after policyholder/funding cost, expenses, hedges, and credit-loss treatment. | Period-matched allocation identifies the AP Aristotle exposure and separately shows gross income, liability cost, other burden, and residual spread. | not located |
| 8 | Return model and residual allocation | Tests owner-level economics without assigning insurer cash to Apollo or common owners. | Cash flows, dates, taxes, losses, liability cost, legal-entity boundaries, and residual allocation are explicit; IRR/NPV/ROIC is reproducible. | not promotable |

## Promotion rule

Promote only this bounded statement:

`AP Aristotle has 776.032348M USD of statutory cash-like consideration candidates across a Paydown row and a Various row, while 6.588486M USD tied to Interest Capitalization / Tax Free Exchange remains outside the cash bucket.`

The `Various` row must not be called a sale, maturity, or repayment until
transaction support identifies the event. The tax-free-exchange row must not
be added to cash-like consideration. The `28.317574M USD` received-interest
field must not be treated as AP Aristotle-only cash until allocation and scope
are reconciled. No amount may be assigned to Apollo parent cash or common-owner
residual cash.

## Source-search result and next action

The existing public search refresh found older AP Aristotle borrower-name
analogs but did not locate the current Athene instrument, a paydown settlement,
or an Athene receipt record. That is a bounded `searched-negative` result for
the checked public perimeter, not evidence that the transaction did not occur.

The next request should go to Athene investment accounting/custody, Apollo
insurance-asset-management transaction files, the paying agent or counterparty,
and the relevant private-placement or rating repository. If any of the first
six document families is obtained, rerun the row promotion test before
expanding to valuation.

## Safe claim

`AP Aristotle is source-request-ready. The Athene statutory packet supports a 776.032348M USD cash-like consideration candidate, separated from a 6.588486M USD tax-free-exchange/noncash hold. The packet defines the exact documents needed to prove lot continuity, settlement, issuer use, Athene receipt/allocation, liability-cost-adjusted spread, and final return. None of those downstream claims is promoted yet.`

## Decision

`apollo-athene-aristotle-source-acquisition-packet-ready-settlement-and-allocation-hold`
