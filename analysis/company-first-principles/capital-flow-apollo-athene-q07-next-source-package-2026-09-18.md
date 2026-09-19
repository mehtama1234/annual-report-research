# Apollo–Athene Q-07 next-source package

Research date: `2026-09-18`

## Purpose

Q-07 currently has a qualified upstream-distribution and intercompany-financing
map, but no source-linked AGM receipt, elimination schedule, or unrestricted
common-owner residual. This package ranks the exact records needed to close
that bridge.

The machine-readable companion is the [Q-07 source-package CSV](data/capital-flow-apollo-athene-q07-next-source-package-2026-09-18.csv).

## Priority order

1. **Athene dividend payment confirmation.** Establish payer, recipient,
   amount, date, and statutory availability.
2. **AGM parent-only receipt ledger.** Establish the receiving account and
   unrestricted/restricted cash classification.
3. **Consolidation elimination schedule.** Remove internal transfers and
   separately identify management-fee settlement.
4. **AHL-to-AGM note ledger.** Keep financing, repayment, interest, and use of
   proceeds separate from distributions.
5. **Parent cash-use waterfall.** Apply senior claims, legal availability,
   preferred/NCI/dilution, and common-owner residuals.

## Promotion rule

Q-07 can move beyond `evidence-insufficient` only when the source set joins:

`Athene distribution -> AGM receiving account -> elimination -> legal availability -> senior claims -> common-owner residual`

The current `$0M–$110M` attribution frontier remains sensitivity-only. A
consolidated cash balance, subsidiary dividend declaration, or intercompany
receivable cannot substitute for the dated receipt and elimination join.

## Public-perimeter recheck

The preserved Apollo/Athene Q2 packet was rechecked against the source-side
flows already in the local corpus: Athene reports `$32M` of Q2 and `$110M` of
H1 distributions to parent; AHL reports a `$279M` receivable from AGM at June
30; and the ACRA/ADIP table reports `$301M` of H1 distributions to ADIP. These
are distinct legal-entity routes. The packet still contains no AGM-only
receiving account, dated bank receipt, or controlled elimination schedule.
The `$279M` note balance is not treated as a cash receipt, and the `$301M`
ADIP flow is not added to the Athene-to-parent distribution.

The current Apollo filing also reports `$25.4B` of consolidated unrestricted
cash and `$5.6B` of available facility capacity, with no amounts outstanding
under the Athene credit facilities at June 30, 2026. These are current
liquidity and senior-claim controls only; they do not identify the portion
funded by Athene's distribution or create an AGM-only receipt.

The official Apollo Q2 2026 Form 10-Q also states that AHL's primary cash-flow
source is dividends from subsidiaries and that the insurance subsidiaries'
dividend capacity is legally constrained. This reinforces the legal-entity
availability control, but it is not a bank receipt, payment confirmation, or
parent-only elimination schedule.

Result: `searched-negative-for-public-agm-receipt-and-elimination`; this does
not imply that private treasury records do not exist.

## Stop rule

Do not re-run consolidated Apollo/Athene cash searches that do not expose a
parent-only receiving account or controlled elimination. Reopen this route only
for a bank/intercompany ledger, payment confirmation, Schedule I/cash schedule,
or equivalent legal-entity waterfall.

## Decision

`receipt-unproven; source-package-ready`

## Source recheck

- [Apollo Q2 2026 Form 10-Q](https://ir.apollo.com/sec-filings/content/0001858681-26-000040/apo-20260630.htm)
