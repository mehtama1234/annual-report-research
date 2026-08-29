# Capital Flow KKR Global Atlantic Borrower Allocation Pass 1

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-014`.

The question is:

`Can KKR / Global Atlantic be upgraded from source-route visibility to statutory vehicle, borrower allocation, and cash/spread outcome evidence?`

The evidence table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-borrower-allocation-pass-1.csv`

## Short Answer

`KKR/Global Atlantic has insurance balance-sheet, asset-income, and credit-quality proxy evidence, but statutory vehicle-to-borrower allocation remains unproven.`

KKR/Global Atlantic is stronger than a pure AUM/channel case because the local `10-Q` extraction includes insurance investments, policy liabilities, investment income by broad asset class, loan allowances, past-due/foreclosure mortgage loans, LTV buckets, and FHLB pledged-asset context.

The evidence shows `220B USD` of Global Atlantic AUM, `164B USD` of Global Atlantic credit AUM, `62B USD` of Ivy and sponsored reinsurance vehicle AUM, `189.204380B USD` of insurance investments, `205.499130B USD` of insurance policy liabilities, `88.056662B USD` of insurance AFS fixed maturity securities, `48.754106B USD` of insurance mortgage and other loan receivables net, `4.028186B USD` of six-month insurance net investment income, `3.351757B USD` of six-month fixed-maturity investment income, and `1.541995B USD` of six-month mortgage/other loan investment income.

The risk side is proxy-visible too: `671.094M USD` of mortgage and other loan allowance for credit losses, `296.4M USD` of mortgage loans 90 days or more past due or in foreclosure and classified as non-income producing, `21.958570B USD` of commercial mortgage loans at LTV `70%` or less, `507.010M USD` of commercial mortgage loans above `90%` LTV, and `9.2B USD` of FHLB funding-agreement pledged assets.

That still does not prove statutory vehicle-to-borrower allocation. The missing layer is statutory legal-entity holdings, Schedule D/BA, NAIC designations, borrower/facility schedules, use of proceeds, cash receipts, repayment performance, and liability-cost spread.

## Money Movement

| Question | Current Answer | Boundary |
|---|---:|---|
| Insurance platform scale | `220B USD` Global Atlantic AUM | AUM is not statutory holdings. |
| Credit channel scale | `164B USD` Global Atlantic credit AUM | Not automatically private credit or borrower-level exposure. |
| Reinsurance vehicle scale | `62B USD` Ivy/sponsored reinsurance vehicle AUM | No vehicle-to-borrower allocation. |
| Insurance investment base | `189.204380B USD` insurance investments | No Schedule D/BA detail. |
| Liability base | `205.499130B USD` insurance policy liabilities | No liability-cost or duration bridge. |
| Fixed maturity exposure | `88.056662B USD` AFS fixed maturities | No NAIC/rating schedule in this pass. |
| Loan exposure | `48.754106B USD` mortgage and other loan receivables net | No borrower/use allocation. |
| Net investment income | `4.028186B USD` six-month insurance NII | Not risk-adjusted spread. |
| Fixed maturity income | `3.351757B USD` six-month income | Broad asset-class income only. |
| Loan income | `1.541995B USD` six-month income | Not borrower cash receipts. |
| Loan allowance | `671.094M USD` | Credit-risk proxy, not full stress result. |
| Past-due/foreclosure loans | `296.4M USD` | Risk signal, not portfolio-wide safety proof. |
| LTV buckets | `21.958570B USD` at 70% or less; `507.010M USD` above 90% | No borrower/property-level collateral proof. |
| FHLB pledged assets | `9.2B USD` | Bank-adjacent funding remains relevant. |

## Queue Result

`executed-local-boundary-pass-1`

The row can be upgraded from route-visible-not-local to executed-local boundary status because the local 10-Q extraction gives asset-class income and credit-quality proxy evidence. It does not pass the full target because statutory vehicle-to-borrower allocation and liability-cost/cash-return proof remain missing.

## What This Proves

The current KKR/Global Atlantic answer is:

`insurance/reinsurance capital + policy liabilities -> Global Atlantic insurance investment base -> fixed maturities, mortgage/other loans, real assets, and other insurance investments -> investment income + credit allowance/past-due/LTV risk proxies`

That is not the same as:

`specific statutory vehicle -> specific borrower/facility -> use of proceeds -> borrower cash repayment -> liability-cost-adjusted spread`

## Missing Proof

| Missing proof | Why it matters | Next source |
|---|---|---|
| Statutory legal-entity schedules | Needed to locate assets by insurer entity. | Global Atlantic statutory annual/quarterly statements. |
| Schedule D/BA holdings | Needed to identify fixed maturities, alternatives, affiliated assets, and issuer-level exposure. | NAIC Schedule D, Schedule BA, and investment schedules. |
| NAIC/rating distribution | Needed for statutory credit-quality grade. | NAIC designations, ratings, and migration schedules. |
| Borrower/facility allocation | Needed to trace insurance capital to real-economy borrowers or assets. | Private placement schedules, borrower loan schedules, rating reports, and credit agreements. |
| Cash receipt and repayment | Needed to move from income accrual/proxy to cash return. | Cash-interest, principal repayment, non-accrual, and charge-off schedules. |
| Liability-cost spread | Needed to evaluate economics after policyholder funding cost. | Crediting-rate, policy liability cost, funds-withheld, and ALM schedules. |
| Bank-adjacent funding economics | Needed because FHLB pledged assets complicate bank-displacement claims. | FHLB funding agreements, collateral files, and liability terms. |

## Safe Claim

`KKR/Global Atlantic has insurance balance-sheet, asset-income, and credit-quality proxy evidence. The local evidence shows 220B USD of Global Atlantic AUM, 164B USD of credit AUM, 62B USD of Ivy and sponsored reinsurance vehicle AUM, 189.204380B USD of insurance investments, 205.499130B USD of insurance policy liabilities, 88.056662B USD of AFS fixed maturity securities, 48.754106B USD of mortgage and other loan receivables net, 4.028186B USD of six-month insurance net investment income, 3.351757B USD of six-month fixed-maturity investment income, 1.541995B USD of six-month mortgage/other loan investment income, 671.094M USD of mortgage and other loan allowance for credit losses, 296.4M USD of past-due/foreclosure non-income-producing mortgage loans, LTV bucket evidence, and 9.2B USD of FHLB pledged assets. This supports insurance balance-sheet and asset-class-income proxy language, not statutory vehicle-to-borrower allocation, borrower use/cash proof, liability-cost spread, or final asset-level return proof.`

## Next Work

1. Pull Global Atlantic statutory filings by legal entity.
2. Extract Schedule D and Schedule BA holdings, NAIC designations, and affiliate exposure.
3. Build asset-income and realized gain/loss tables by statutory asset class.
4. Join loan exposure to property type, geography, LTV, non-accrual, and charge-off data.
5. Search for borrower/facility documents where private placement or loan records are public.
