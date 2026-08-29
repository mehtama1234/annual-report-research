# Capital Flow Wheaton Antamina Net Cash Return Pass 1

## Purpose

This pass executes upgrade queue row `CFDRBUQ-004`.

The question is:

`Can Wheaton's Antamina PMPA evidence move from gross stream economics to net cash-return evidence after accounting for depletion, tax, and interest?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-wheaton-antamina-net-cash-return-pass-1.csv`

The upstream economics pass is:

`/cluster/capital-flow-wheaton-antamina-pmpa-economics-pass-1.md`

## Current Answer

`Partly. Antamina now has a pre-tax, pre-interest net cash-return proxy. The Q2 2026 filing shows Antamina revenue, cash cost, depletion, profit, operating cash flow, asset carrying value, the 4.300B USD PMPA cash payment, company-level finance costs, company-level income tax expense, and debt-principal denominators. The filing still does not allocate income tax expense or finance costs to Antamina, so full net return, debt-service coverage, IRR, NPV, and lender allocation remain open.`

## Evidence Bridge

| Metric | Value | What It Supports | Boundary |
|---|---:|---|---|
| Antamina PMPA upfront payment | `4.300B USD` | Named use of cash. | Not lender-level allocation. |
| Antamina H1 2026 revenue | `277.563M USD` | Stream-level revenue. | Not after-cost return. |
| Cost of sales excluding depletion | `55.340M USD` | Stream cash-cost support. | Excludes depletion, tax, and finance cost. |
| Antamina depletion | `51.322M USD` | Accounting cost allocation. | Not cash tax or interest. |
| Antamina profit after depletion | `170.901M USD` | Pre-tax, pre-interest accounting profit proxy. | Not after-tax profit. |
| Antamina operating cash flow | `222.223M USD` | Stream-level cash margin before tax and finance allocation. | Not debt-service cash flow. |
| Antamina asset carrying amount | `4.708329B USD` | Asset-base denominator. | Not fair value or NPV. |
| Company finance costs | `32.502M USD` | Company-level financing burden. | Not allocated to Antamina. |
| Company income tax expense | `210.876M USD` | Company-level tax burden. | Not allocated to Antamina. |

## Derived Proxies

| Proxy | Value | Interpretation |
|---|---:|---|
| Cash margin before depletion | `222.223M USD` | Revenue less cost excluding depletion matches reported Antamina operating cash flow. |
| Cash margin before depletion as share of revenue | `80.071%` | Antamina's first-half stream cash-margin proxy is high before depletion, tax, and finance costs. |
| Depletion burden as share of cash margin | `23.095%` | Depletion consumes about one-quarter of first-half cash margin on an accounting basis. |
| Profit after depletion as share of OCF | `76.905%` | The visible stream still has strong pre-tax, pre-interest accounting profit after depletion. |
| First-half OCF / upfront payment | `5.168%` | First-half cash-yield proxy against the 4.300B USD PMPA payment. |
| Annualized OCF / upfront payment | `10.336%` | Mechanical annualization only; not IRR or NPV. |
| First-half profit / upfront payment | `3.974%` | First-half accounting-profit yield proxy after depletion. |
| Annualized profit / upfront payment | `7.949%` | Mechanical annualization only; still before tax and finance cost. |
| Annualized OCF / Antamina assets | `9.439%` | Asset-carrying-value cash-yield proxy. |
| Annualized profit / Antamina assets | `7.260%` | Asset-carrying-value accounting-profit proxy after depletion. |
| Term loan / upfront payment | `34.884%` | The 1.500B USD term loan is material relative to the PMPA payment. |
| Gross bank debt / upfront payment | `45.860%` | Quarter-end bank debt is material relative to the PMPA payment. |

## Decision

`net-cash-return-proxy-visible-tax-interest-allocation-incomplete`

Wheaton passes the next bounded test: Antamina is no longer only a gross stream economics case. The local filings support a pre-tax, pre-interest net cash-return proxy after depletion, plus company-level tax and finance-cost context.

The pass does not support a full net return claim. The missing pieces are Antamina-specific income tax, Antamina-specific interest expense, actual debt-service waterfall, lender allocation, reserve-life support, delivered-ounce schedule, IRR, NPV, and full PMPA return model.

## Safe Claim

`Wheaton's Antamina PMPA now has source-backed pre-tax, pre-interest net cash-return proxy evidence: H1 2026 Antamina revenue of 277.563M USD, cost excluding depletion of 55.340M USD, depletion of 51.322M USD, profit after depletion of 170.901M USD, operating cash flow of 222.223M USD, assets of 4.708329B USD, and a 10.336% mechanical annualized OCF/upfront-payment proxy. The evidence still does not allocate Antamina taxes, interest, debt service, or lender funding.`

## Do Not Claim

- Do not claim Antamina after-tax return.
- Do not claim Antamina interest expense.
- Do not claim debt-service coverage.
- Do not claim the term loan was the exact source for a fixed share of the PMPA payment.
- Do not claim PMPA IRR, NPV, full payback, or reserve-life sufficiency.

## Next Sources

1. Antamina delivered-ounce and cash-receipt schedule.
2. PMPA agreement or detailed contract economics.
3. Antamina reserve and mine-life support.
4. Tax note or jurisdiction schedule that can allocate income tax to Antamina stream income.
5. Term loan and revolver debt-service schedule, borrowing notices, repayment waterfall, and lender allocation.
