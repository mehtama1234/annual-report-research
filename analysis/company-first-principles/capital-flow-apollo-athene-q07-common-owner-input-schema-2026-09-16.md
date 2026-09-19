# Apollo–Athene Q-07 common-owner cash input schema

Research date: `2026-09-17`

This schema converts the Q-07 parent-receipt question into model-ready fields.
It does not treat consolidated cash, statutory cash, a dividend declaration, or
an intercompany balance as Apollo common-owner cash. Each input must be joined
to the correct legal entity, period, cash account, senior claim, and elimination
boundary before it can enter a common-owner waterfall.

The structured companion is
[the Q-07 input CSV](data/capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.csv).

| Input family | Required model field | Current state | Model use | Exact upgrade document |
| --- | --- | --- | --- | --- |
| Earnings | FRE, SRE, PII and ANI bridge | Observed at Apollo consolidated level | Starting earnings/use surface | Apollo 10-Q and earnings reconciliation |
| Entity | Apollo HoldCo/AGM unrestricted cash | Partial: `$3.412B` summary and `$3.415B` segment context | Parent cash denominator | Parent-only cash ledger and bank statement |
| Source | Athene subsidiary dividend declared and paid | Partial: `$110M` H1 distribution-to-parent frontier; `$375M` Athene common dividends paid | Upstream source candidate | Athene dividend schedule and payment confirmation |
| Receipt | AGM receiving account and dated amount | Searched-negative: Apollo Q2 10-Q and financial supplement do not expose a parent-only June 30 receipt line or AGM receiving account | Apollo parent cash inflow | Bank confirmation, intercompany receipt ledger |
| Elimination | Apollo/Athene intercompany elimination | Missing: no controlled schedule is joined to the receipt frontier; the public boundary is not a substitute for that schedule | Prevents grossing up internal transfers | Consolidation elimination schedule |
| Financing | AHL-to-AGM note draw, repayment, interest, and use | Partial: `$279M` Athene-side receivable within `$500M` facility; Apollo FY2025 parent-only Schedule I independently corroborates a `$227M` AGM payable to AHL against AHL's `$227M` receivable at December 31, 2025; Apollo Q2 provides no parent-only June 30 note line; Athene's Q2 10-Q reports no amounts outstanding under the current or previous external credit facilities at June 30, 2026 | Financing versus distribution classification | Note ledger, borrowing notices, bank confirmations |
| Legal access | Statutory dividend capacity and restrictions | Partial: legal path and constraints observed | Maximum legally available upstream cash | Regulatory dividend filing and solvency schedule |
| Senior claims | Debt, preferred, NCI, policyholder, tax, and regulated-capital claims | Partial: aggregate claims visible | Residual available to common | Entity waterfall and capital-adequacy schedule |
| Fee cash | Athene management-fee payable, settlement, recipient entity | Partial: `$779M` mechanical settlement implication | Fee-entity cash inflow | Related-party settlement schedule and recipient account |
| Parent uses | Dividends, repurchases, taxes, debt service, and HoldCo investment uses | Partial: selected uses visible | Common-owner cash deployment | Parent cash-flow note and use-of-cash ledger |
| Shares | Basic, preferred conversion, RSU, and dilution claims | Observed denominator boundary | Per-share residual | Q2 share-claim and dilution schedule |
| Return | Common-owner residual, payout, repurchase, and per-share value | Not assembled: a `$0M–$110M` attribution frontier exists, but no source-linked parent-to-common-owner waterfall has been assembled | Final common-owner cash/value | Integrated parent-to-common-owner waterfall |

## Promotion rule

The Q-07 common-owner claim is promotion-ready only when a dated source joins
the upstream distribution or fee payment to an AGM receiving account, removes
intercompany eliminations, applies legal availability and senior claims, and
reconciles the residual to the relevant share denominator. The current
`$0M–$110M` attribution frontier remains a sensitivity, not an observed
receipt. The searched-negative receipt and elimination results make the
public-source boundary explicit; they do not imply that no private transfer or
elimination occurred.

## Current boundary and next order

The local evidence supports a qualified map of Apollo earnings, Athene
distributions, HoldCo cash surfaces, intercompany financing, statutory limits,
and common-owner claims. It does not prove that any specific Athene distribution
reached AGM unrestricted cash or became a final common-owner residual.

The [June 26, 2026 credit-agreement purpose perimeter](capital-flow-apollo-athene-2026-credit-agreement-purpose-perimeter-2026-09-17.md)
adds a dated primary-filed AHL/Athene financing control: `$1.750B` of
aggregate commitments, working-capital/lawful-corporate-purpose language, and
specified affiliate/intercompany permissions. It does not establish a draw,
AGM transfer, use-of-proceeds allocation, elimination, or common-owner cash.

Next: obtain the AGM bank/intercompany receipt ledger; join the Athene dividend
schedule; reconcile eliminations; apply debt, preferred, NCI, policyholder,
regulated-capital, tax, and dilution claims; then run the source-linked waterfall.
