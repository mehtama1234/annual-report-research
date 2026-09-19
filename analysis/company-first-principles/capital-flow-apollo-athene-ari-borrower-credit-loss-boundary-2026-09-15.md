# Apollo–Athene ARI Borrower and Credit-Loss Boundary

Research date: `2026-09-15`

This upgrade executes the credit-quality portion of queue item `Q-09` using
ARI's Q2 2026 Form 10-Q. It strengthens the transaction's repayment and loss
boundary, but it does not create a borrower-level Athene collection ledger.

Primary source:

[ARI Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1467760/000119312526342628/ari-20260630.htm)

## What the filing adds

ARI states that it sold its commercial real-estate loan portfolio to Athene on
April 24, 2026 for approximately `$8.6B`, based on `99.7%` of total loan
commitments subject to adjustments. The sale excluded loans repaid before
closing and one Chicago Hotel Loan with a `$46M` principal balance that repaid
after closing.

The filing says there were no outstanding loans as of June 30, 2026 and no CECL
allowance remained at that date. It also discloses the credit-cost path around
the transaction:

- `$335.0M` of specific CECL allowance was written off for loans included in
  the asset sale;
- `$2.6M` net realized loss arose from the discount on the asset sale versus
  loan cost basis; and
- `$1.5M` of specific CECL allowance was written off on the discounted Chicago
  Hotel Loan repayment, with another `$1.5M` reversed.

These facts show that the seller-side exit was not a clean face-value cash
event: the portfolio had recognized credit reserves and a sale discount. They
also prove repayment/exit at the ARI entity level, not the performance of the
portfolio after Athene acquired it.

## Proof-grade result

| Gate | Result | Boundary |
| --- | --- | --- |
| Seller loan balance after closing | Proven | ARI had no outstanding loans at June 30; Athene's post-close asset balance is not shown here |
| Named borrower repayment | Partially proven | The `$46M` Chicago Hotel Loan repaid after closing; individual portfolio borrower repayments remain undisclosed |
| Credit-loss recognition | Proven | `$335M` CECL write-off and Chicago-loan allowance activity are visible |
| Sale-price quality | Proven at seller level | `$2.6M` net realized loss from discount to cost basis is visible |
| Athene borrower cash collection | Not proven | The ARI filing does not show Athene's subsequent principal, interest, collateral, or loss collections |
| Apollo return allocation | Not proven | No Apollo HoldCo receipt or common-owner residual is joined |

## Updated safe claim

`ARI's Q2 2026 filing confirms the completed approximately $8.6B cash sale to
Athene, the post-close zero-loan seller balance, the $46M Chicago Hotel Loan
repayment, a $335M specific CECL write-off on transferred loans, and a $2.6M
sale discount loss. This upgrades the seller-side repayment and credit-loss
boundary. It does not prove Athene's post-close borrower cash collections,
collateral realization, loan-level returns, Apollo parent receipt, or common-
owner cash.`

## Next gate

The remaining Q-09 requirement is Athene's post-close investment schedule or
borrower/trustee data showing principal receipts, interest collections,
modifications, impairments, collateral proceeds, and allocation of those cash
flows after the transfer.

