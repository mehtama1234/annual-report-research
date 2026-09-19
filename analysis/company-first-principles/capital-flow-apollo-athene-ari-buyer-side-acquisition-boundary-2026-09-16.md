# Apollo–Athene ARI buyer-side acquisition boundary

Research date: `2026-09-16`

## Question

Does Athene's Q2 2026 filing join the ARI seller-side disposal to a buyer-side
asset acquisition, and does that join prove borrower cash collections or a
realized return?

## Source route

| Source | Route | Period / date | Role |
| --- | --- | --- | --- |
| Athene Holding Ltd. Form 10-Q | [SEC filing](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm) | Quarter ended June 30, 2026 | Buyer-side acquisition and commercial-mortgage balance |
| Apollo Commercial Real Estate Finance Form 10-Q | [SEC filing](https://www.sec.gov/Archives/edgar/data/1467760/000119312526342628/ari-20260630.htm) | Quarter ended June 30, 2026 | Seller-side consideration and closing boundary |

## Observations

| Observation | Amount / date | Evidence grade | Boundary |
| --- | ---: | --- | --- |
| Athene purchase of ARI commercial-mortgage portfolio, including accrued interest | Approximately `$8.7B`; completed April 24, 2026 | `reported-buyer-acquisition` | Aggregate consideration is not a loan-level payment ledger |
| ARI sale description | Approximately `$8.6B` cash consideration, subject to purchase-agreement adjustments | `reported-seller-consideration` | Seller and buyer descriptions are retained as separate reported perimeters |
| Athene commercial-mortgage balance | `$39.071B` at December 31, 2025 to `$48.291B` at June 30, 2026; increase `$9.220B` | `reported-aggregate-balance` | Directionally consistent with a material acquisition, but not ARI-attributed |
| ARI post-close seller status | Zero seller commercial loans after the transaction, except for the named Chicago Hotel Loan that repaid after closing | `reported-seller-boundary` | Does not identify Athene borrower receipts or collateral proceeds |
| Athene commercial-mortgage portfolio and stressed subset | `$48.372B` commercial mortgage loans; `$1.802B` under development; `$1.027B` unpaid principal 90 days past due and/or non-accrual with `$695M` fair value | `reported-buyer-credit-boundary` | Portfolio-level figures are not ARI-attributed and do not establish post-close cash collections |

## Reconciliation result

The two filings establish a stronger transaction perimeter:

```text
ARI seller portfolio
  -> April 24 closing
  -> approximately $8.6B seller cash consideration
  -> Athene buyer disclosure of approximately $8.7B purchase
  -> Athene aggregate commercial-mortgage balance increase
```

This is a buyer-side acquisition boundary, not a complete cash loop. The
`$8.6B` and `$8.7B` figures should not be forced to equality because the filings
describe different reporting perimeters, accrued interest, and contractual
adjustments. The `$9.220B` balance increase is not a substitute for the
purchase ledger.

Athene's credit table makes the buyer-side return test more concrete: the
portfolio has a visible stressed subset, but the filing does not identify
which loans came from ARI, how much principal or interest was collected after
closing, or how the fair-value marks map to borrower-level outcomes.

## What remains unproven

This artifact does not prove:

- the Athene bank account that paid the consideration;
- the loan-level allocation of the acquired portfolio;
- borrower principal, interest, or collateral collections after closing;
- realized losses, fees, or liability funding costs attributable to the ARI
  loans; or
- any transfer from Athene to Apollo or cash available to Apollo common owners.

## Q-09 consequence

Q-09 remains `partial-upgrade` / `evidence-insufficient`. The buyer-side
acquisition and aggregate balance perimeter is now source-backed, while the
next decisive evidence remains an Athene investment schedule, borrower or
trustee remittance, loan-level collection report, or a subsequent filing that
joins the acquired assets to cash receipts and return attribution.
