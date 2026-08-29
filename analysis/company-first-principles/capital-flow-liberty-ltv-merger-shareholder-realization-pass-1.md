# Capital Flow Liberty LTV Merger Shareholder Realization Pass 1

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-011`.

The question is:

`Can Liberty Broadband's holdco restructuring be upgraded from debt/collateral mechanics to LTV, merger funds-flow, and shareholder-realization evidence?`

The evidence table is:

`analysis/company-first-principles/data/capital-flow-liberty-ltv-merger-shareholder-realization-pass-1.csv`

## Short Answer

`Liberty has holdco collateral/liquidity restructuring evidence with LTV context, but not final merger/shareholder realization proof.`

Liberty Broadband is not an operating-return case. It is a holding-company capital-structure case where the money moves through Charter-linked collateral, Charter share monetization, margin-loan debt, a Charter loan, restricted cash, and exchangeable-debenture settlement.

The local evidence supports a boundary upgrade. Liberty had a `5.507B USD` Charter investment, `864M USD` of Margin Loan Facility debt, `359M USD` of Charter Loan Facility debt, `19.1M` Charter shares in collateral accounts, and `2.7B USD` of disclosed collateral-account value. Charter advanced about `359M USD` to repay margin-loan borrowings after an LTV trigger, while Liberty used Margin Loan Facility proceeds and restricted cash to pay `966M USD` including accrued interest to repurchase and retire all outstanding `3.125%` Exchangeable Senior Debentures due `2053`.

That shows how money moved. It does not yet show final shareholder realization. The missing proof is contractual LTV calculation, restricted-cash/source split, merger closing funds-flow, tax outcome, debt repayment or assumption at close, and actual consideration delivered to Liberty holders.

## Money Movement

| Question | Current Answer | Boundary |
|---|---:|---|
| Holdco asset base | `5.507B USD` Charter investment | Carrying value is not market value or shareholder realization. |
| Current debt pressure | `864M USD` Margin Loan Facility | Collateralized debt, not operating return. |
| Charter support loan | `359M USD` Charter Loan Facility | Debt substitution and liquidity support. |
| Debenture cash use | `966M USD` settlement payment including accrued interest | No favorable-settlement proof. |
| Settlement source | Margin Loan Facility proceeds plus restricted cash | Dollar split unavailable. |
| Debt movement | `1.239B USD` borrowings; `1.771B USD` repayments | Aggregate financing movement only. |
| Total debt reduction | `523M USD` decline from Dec. 31 2025 to Jun. 30 2026 | Not an economic gain by itself. |
| Charter monetization | `595M USD` cash from Charter share repurchases | Asset monetization, not final holder realization. |
| Collateral shares | `19.1M` Charter shares in collateral accounts | No contractual LTV certificate. |
| Collateral value | `2.7B USD` disclosed collateral value | No lender haircut or definition proof. |
| Simple collateral ratio | About `32.0%` margin debt / disclosed collateral value | Not contractual LTV. |
| LTV trigger | `50%` support trigger with `30%`/`40%` target context | Actual test calculation missing. |

## Queue Result

`executed-local-boundary-pass-1`

The row can be upgraded from partial-local to executed-local boundary status. The local evidence proves holdco source/use mechanics, collateral context, debenture cash settlement, Charter support-loan mechanics, and asset-monetization context. It does not prove the full target of LTV-certified sufficiency, final merger funds-flow, or shareholder realization.

## What This Proves

The current Liberty answer is:

`Charter-linked holding-company asset base -> pledged Charter-share collateral / margin-loan structure -> Charter support loan + restricted cash / margin-loan proceeds -> debenture retirement and margin-loan repayment -> lower debt stack and transaction-liquidity context`

That is not the same as:

`Liberty shareholder receives final merger cash/value after debt, tax, and transaction mechanics`

## Missing Proof

| Missing proof | Why it matters | Next source |
|---|---|---|
| Contractual LTV | Needed to prove collateral sufficiency and margin-call cushion. | LTV certificate and margin-loan agreement definitions. |
| Restricted-cash split | Needed to separate settlement sources. | Restricted-cash rollforward and treasury funds-flow. |
| Charter loan economics | Needed to determine cost and repayment mechanics. | Charter Loan Facility agreement and interest/payment schedule. |
| Debenture settlement economics | Needed to distinguish principal, accrued interest, premium, tax, and fair-value accounting. | Settlement statement, put notice, fair-value rollforward, and tax note. |
| Merger funds-flow | Needed to know whether debt is repaid, assumed, or rolled at close. | Final Charter/Liberty merger closing statement. |
| Shareholder realization | Needed to move from restructuring to investor outcome. | Final consideration, exchange ratio, tax treatment, and holder proceeds bridge. |

## Safe Claim

`Liberty Broadband has holdco collateral/liquidity restructuring evidence with LTV context. The local evidence shows a 5.507B USD Charter investment, 864M USD of Margin Loan Facility debt, 359M USD of Charter Loan Facility debt, 19.1M Charter shares in collateral accounts, 2.7B USD of disclosed collateral-account value, a simple 32.0% margin-debt/disclosed-collateral ratio, a 50% LTV support trigger, a 359M USD Charter loan advanced to repay margin-loan borrowings, 595M USD of cash from Charter share repurchases, and a 966M USD debenture retirement funded with Margin Loan Facility proceeds and restricted cash. This proves holdco money-movement mechanics, not contractual LTV sufficiency, final merger funds-flow, tax outcome, or shareholder realization.`

## Next Work

1. Pull the margin-loan LTV certificate and agreement definitions.
2. Pull the Charter Loan Facility agreement and repayment terms.
3. Extract restricted-cash rollforward and debenture settlement details.
4. Track final Charter/Liberty merger close documents.
5. Build a shareholder-realization bridge only after final consideration, debt treatment, and tax treatment are visible.
