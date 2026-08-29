# Capital Flow Liberty Debenture Settlement Economics Pass 1

## Purpose

This page executes Liberty Broadband row `CFDRBUQ-011` from the debt/refinancing bridge upgrade queue:

`Can Liberty Broadband's 2053 exchangeable-debenture retirement be upgraded from holdco restructuring evidence to settlement economics?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-liberty-debenture-settlement-economics-pass-1.csv`

The upstream queue is:

`/cluster/capital-flow-debt-refinancing-bridge-upgrade-queue-pass-1.md`

The upstream Liberty bridge is:

`/cluster/capital-flow-liberty-broadband-holdco-restructuring-bridge-pass-1.md`

## Current Answer

`Liberty Broadband can be upgraded to debenture-retirement mechanics visible with funding-source and collateral context, but not to favorable settlement economics or shareholder realization. The Q2 2026 filing shows that holders of the 3.125% Exchangeable Senior Debentures due 2053 had a put right on April 6 2026, all outstanding 2053 debentures were put back and retired, and Liberty paid 966M USD including accrued interest using Margin Loan Facility proceeds and restricted cash. The debt table shows the debentures fell from 956M USD carrying value at December 31 2025 to zero at June 30 2026, while total debt fell from 1.746B USD to 1.223B USD. That debt reduction is internally consistent with the instrument rollforward: a 956M USD debenture retirement partly offset by a 74M USD margin-loan increase and a new 359M USD Charter loan.`

## Reconciliation

| Step | Amount | Meaning |
|---|---:|---|
| 2053 debentures carrying value at Dec. 31 2025 | `956M USD` | Pre-settlement carrying value in the debt table. |
| 2053 debentures carrying value at Jun. 30 2026 | `0M USD` | Debenture obligation retired. |
| Settlement payment including accrued interest | `966M USD` | Cash paid to repurchase the 2053 debentures on April 6 2026. |
| Payment less prior carrying value | `10M USD` | Rough spread, not a clean premium because accrued interest and fair-value accounting are involved. |
| Total debt at Dec. 31 2025 | `1.746B USD` | Starting debt stack. |
| Total debt at Jun. 30 2026 | `1.223B USD` | Ending debt stack. |
| Total debt decrease | `523M USD` | Net balance-sheet debt reduction. |
| Instrument rollforward check | `523M USD` | `956M` debenture retirement less `74M` margin-loan increase less `359M` new Charter loan. |
| Debt borrowings | `1.239B USD` | First-half financing inflows. |
| Debt repayments | `1.771B USD` | First-half financing outflows. |

## What Improved

| Area | Prior Bridge | This Pass |
|---|---|---|
| Debt retirement | The prior bridge showed that Liberty settled a major exchangeable-debenture obligation. | This pass identifies the holder put right, retirement date, `966M USD` payment, and funding-source language. |
| Funding context | The prior bridge showed margin-loan and Charter loan activity. | This pass separates the debenture settlement source language from the Charter loan's LTV-triggered support role. |
| Balance-sheet reconciliation | The prior bridge listed debt balances. | This pass reconciles the instrument movement to the `523M USD` total-debt reduction. |
| Collateral boundary | The prior bridge noted collateralized margin debt. | This pass adds `19.1M` Charter collateral shares, `2.7B USD` disclosed collateral-account value, and the LTV support-trigger language while refusing to call it contractual LTV proof. |

## Decision

`debenture-retirement-mechanics-visible-settlement-economics-incomplete`

This is an upgrade from:

`holdco-collateral-liquidity-restructuring-bridge-visible`

It does not reach:

`settlement-value-creation-or-shareholder-realization-proven`

The queue pass test required debenture retirement economics and funding source. The visible 10-Q evidence passes the retirement-mechanics and funding-source portion: the debentures were put back and retired for `966M USD`, funded with Margin Loan Facility proceeds and restricted cash. It holds on full economics because the filing does not isolate accrued interest, fair-value movement, tax impact, settlement premium, exact restricted-cash/margin-loan split, contractual LTV certificate, or final merger funds-flow.

## Remaining Gap

| Gap | Why It Matters | Next Source |
|---|---|---|
| Accrued-interest split | Needed to distinguish principal, accrued interest, and any premium. | Debenture settlement statement and put notice. |
| Fair-value rollforward | Needed because Liberty accounted for exchangeable debentures at fair value before redemption. | Fair-value reconciliation by instrument. |
| Funding-source split | Needed to separate Margin Loan Facility proceeds from restricted cash. | Treasury funds-flow and restricted-cash rollforward. |
| Contractual LTV calculation | Needed before claiming collateral sufficiency or margin-call cushion. | Margin-loan LTV certificate and agreement definitions. |
| Charter loan repayment mechanics | Needed because the `359M USD` Charter loan is transaction-linked and LTV-triggered. | Charter Loan Facility agreement and merger-close treatment. |
| Final shareholder realization | Needed before treating the restructuring as value delivered to Liberty holders. | Charter/Liberty final merger closing statement and consideration mechanics. |

## Safe Claim

`Liberty Broadband's Q2 2026 filing supports a bounded debenture-retirement mechanics claim: all outstanding 3.125% Exchangeable Senior Debentures due 2053 were put back and retired on April 6 2026, Liberty paid 966M USD including accrued interest using Margin Loan Facility proceeds and restricted cash, total debt fell by 523M USD from December 31 2025 to June 30 2026, and the debt-table instrument rollforward reconciles the debenture retirement against a 74M USD margin-loan increase and a new 359M USD Charter loan. This does not prove favorable settlement economics, collateral sufficiency, final merger value, tax outcome, or shareholder cash realization.`

## Next Work

1. Pull the debenture put notice and settlement statement.
2. Extract fair-value rollforward and accrued-interest detail.
3. Pull the Margin Loan Facility LTV certificate or collateral schedule.
4. Parse the Charter Loan Facility agreement terms and merger-close treatment.
5. Wait for final Charter/Liberty merger closing documents before making shareholder-realization claims.
