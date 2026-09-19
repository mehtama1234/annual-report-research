# Apollo/Athene AP Grange settlement next-source package

Research date: `2026-09-18`

## Purpose

The AP Grange public record now establishes an instrument identity and an
issuer-level Q2 call/gain event, but it does not establish Athene's lot-level
settlement, paying-agent remittance, borrower/issuer cash, liability-adjusted
return, or Apollo common-owner cash. This package turns that gap into five
ranked acquisition requests rather than another broad public search.

The machine-readable companion is the [AP Grange source-package CSV](data/capital-flow-apollo-athene-ap-grange-next-source-package-2026-09-18.csv).

## Priority order

1. **Issuer/trustee call notice or paying-agent statement.** Identify the
   affected tranche, payment date, and gross settlement pool.
2. **Athene custody or cash allocation.** Establish whether Athene's
   `G2964#-AA-7` Tranche A and/or `G2964#-AB-5` Tranche B was called, and what
   amount was actually remitted.
3. **Post-call statutory lot chronology.** Reconcile holdings, consideration,
   gain/loss, and counterparty fields without treating statutory consideration
   as a bank receipt.
4. **Apollo wrapper/fund allocation.** Connect the reported approximately
   `$5.0B` credit-strategy redemption to the AP Grange tranche and named legal
   entities, while keeping fund cash separate from parent cash.
5. **After-cost return waterfall.** Obtain asset-level liability cost, tax,
   fees, residual entity cash, upstream distribution, and common-owner claims.

## Promotion rule

Q-08 can move beyond `evidence-insufficient` only when the source set joins:

`issuer call -> exact Athene lot -> paying-agent or bank remittance -> legal-entity cash -> liability/tax burden -> residual return`

The existing public tuple join, the `$673M` gain, the `$5.080B` issuer
concentration change, and independent-holder redemption observations remain
controls around that chain. None is a substitute for the chain itself.

## Stop rule

Do not repeat the broad AP Grange search or promote the public N-2/A, SSGA
N-PORT, KEMI, KKR, Principal, or Brighthouse observations into Athene cash.
Reopen this route only when one of the five source objects or a materially
equivalent transaction-level record becomes available.

## Decision

`settlement-unproven; source-package-ready`
