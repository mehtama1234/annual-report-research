# Apollo–Athene Q2 policyholder-liquidity and repo-burden boundary

Research date: `2026-09-15`

This memo adds a company-specific Lyn Alden-style liquidity transmission test
to the Apollo–Athene owner-cash bridge. Apollo's Q2 2026 Form 10-Q reports that
approximately `36%` of Athene's net reserve liabilities were generally
non-surrenderable and approximately `54%` were subject to a surrender penalty.
The same filing reports repurchase-agreement payables of `$3.2B` at June 30,
2026 versus `$6.0B` at December 31, 2025, backed by securities and collateral
with fair values of `$3.4B` and `$6.2B`, respectively.

## Transmission mechanism

```text
rates / market liquidity / collateral values
  -> policyholder surrender and withdrawal behavior
  -> Athene funding and collateral needs
  -> asset sales, repo capacity, and investment-spread pressure
  -> regulated capital and parent-distribution capacity
  -> Apollo common-owner cash
```

The liability percentages do not predict surrender behavior: a penalty or
non-surrenderable contract is a contract feature, not an observed stress test.
Likewise, the repo balances do not prove a funding crisis or a realized loss.
They identify the balance-sheet channels through which a liquidity regime can
reach Athene's cash availability and then the parent-receipt question.

## Evidence boundary

| Q2 2026 observation | What it supports | What it does not prove |
| --- | --- | --- |
| `36%` of net reserve liabilities generally non-surrenderable | A disclosed floor of contract rigidity | Customer behavior, liquidity sufficiency, or distributable surplus |
| `54%` of net reserve liabilities subject to surrender penalty | A disclosed contract-friction measure | Actual surrender rates or cash savings in a stress |
| `$3.2B` repurchase-agreement payables | A current secured-funding obligation | Debt distress, asset-sale loss, or Apollo funding responsibility |
| `$3.4B` collateral fair value against those payables | Current collateral context | Haircut headroom, margin-call terms, or unrestricted cash |
| `$6.0B` / `$6.2B` prior-year payable / collateral comparison | A period-over-period deleveraging observation | Causal attribution to rates, policyholder flows, or investment performance |

## Denominator consequence

Athene operating cash, statutory investment income, and consolidated cash must
remain separate from Apollo common-owner cash. The new observations belong in
the liability, liquidity, and regulated-capital layers of the bridge. They do
not change the unresolved parent-receipt frontier or justify subtracting repo
payables and policyholder liabilities again from a cash-flow line that already
contains their operating effects.

## Next falsifiable test

The next filing should be checked for surrender/withdrawal cash, repo maturity
and haircut terms, collateral calls, statutory capital, realized investment
sales, and any dated dividend or intercompany receipt. A stress conclusion can
be promoted only if those flows are joined by period and legal entity.

Primary source: [Apollo Q2 2026 Form 10-Q](https://ir.apollo.com/sec-filings/content/0001858681-26-000040/0001858681-26-000040.pdf).

Structured extraction: [policyholder-liquidity and repo CSV](data/capital-flow-apollo-athene-q2-policyholder-liquidity-repo-burden-boundary-2026-09-15.csv).
