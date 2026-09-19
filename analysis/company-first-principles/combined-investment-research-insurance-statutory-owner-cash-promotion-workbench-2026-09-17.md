# Insurance statutory named-asset owner-cash promotion workbench

## Purpose

This workbench is the next promotion object for the insurance statutory lane.
It consolidates the Apollo/Athene and KKR/Global Atlantic/Accordia proof ladder
without treating statutory income, asset proceeds, or platform AUM as common-
owner cash. The model is designed to show exactly which evidence exists and
which missing document blocks a return conclusion.

## Formula

`liability-adjusted common-owner return = named asset income + realized proceeds - credit losses/impairments - liability funding cost - reinsurance/funds-held claims - taxes/fees - capital requirement - remittance and parent claims`

The legal entity is the unit of analysis. A platform can manage assets without
owning the insurance liability, receiving the asset cash, or retaining the
residual return.

## Current observed surfaces

| Route | Observed asset/income surface | Strongest current proof | Open owner-cash boundary |
|---|---:|---|---|
| Apollo/Athene | `$158.619B` parsed Schedule D bond base; `$12.733B` statutory NII; `$12.282B` cash-flow NII; `$13.601B` collected gross investment income; `$54.035B` bond proceeds; `$12.676B` mortgage-loan proceeds | Legal-entity income and proceeds bridge plus AP Aristotle, AMAPS, Concord, Eliant, AA Infrastructure, and MF1 named rows | Named borrower receipt, liability cost, trustee/remittance waterfall, Athene allocation, and parent common residual |
| KKR/Global Atlantic/Accordia | `$7.318B` owned-bond book; `$229.508M` interest received; `$156.199M` interest due; `$605.073M` gross investment income collected; `$549.714M` summary NII | Row-level owned-bond interest and selected same-CUSIP disposal candidates | Disposal continuity, borrower/use, liability spread, reinsurance/funds-held route, and remittance |

## Promotion gates

| Gate | Required evidence | Apollo/Athene | Accordia |
|---|---|---|---|
| Legal entity | Insurer/reinsurer statutory entity and ownership | Observed | Observed |
| Named asset | CUSIP/issuer/wrapper and book value | Observed for selected rows | Observed for selected rows |
| Income | Interest/dividend/investment income row and period | Observed | Observed |
| Proceeds | Maturity, sale, repayment, or settlement amount | Candidate/partially reconciled | Selected disposal candidates |
| Receipt | Bank, custodian, trustee, or remittance evidence | Open | Open |
| Liability cost | Credited rate, funds-held, reinsurance, funding agreement, or policy liability allocation | Open | Open |
| Credit/perimeter | NAIC designation, impairment, non-accrual, affiliate, and capital treatment | Partially observed | Partially observed |
| Owner allocation | Subsidiary-to-parent dividend, fee, NCI/preferred, and common residual | Open | Open |
| Return | After-cost, after-loss, after-capital return calculation | Open | Open |

## Priority proof sequence

1. **Apollo/Athene first wave:** AP Aristotle, AMAPS, and Concord.
2. **Apollo/Athene second wave:** Eliant, AA Infrastructure, and MF1.
3. **Accordia comparison:** resolve private-marker `90231*-AA-0`, then Intel,
   Orange, Wells Fargo, and Los Angeles Community College District.
4. **Liability bridge:** attach credited rates, funds-held balances, reinsurance,
   policyholder liability cost, and capital/RBC treatment to the strongest rows.
5. **Cash route:** seek trustee, custodian, borrower payoff, maturity, or
   remittance evidence before labeling consideration as received cash.
6. **Owner return:** calculate only after taxes, fees, impairment, liability
   cost, capital, and parent claims are visible.

## Financial-shenanigans and QoE controls

- Do not use AUM as invested assets or invested assets as private credit.
- Do not use statutory interest received as borrower-level cash without a
  settlement route.
- Do not use disposal consideration as settlement without lot continuity and
  payment evidence.
- Do not use realized gain/loss as return without taxes, fees, impairment,
  liability cost, and capital treatment.
- Do not use a wrapper or issuer name as proof of ultimate borrower, collateral,
  or use of proceeds.
- Track non-accruals, allowances, impairments, NAIC migration, affiliated
  exposure, reinsurance, and funds-held balances.

These are forensic controls, not allegations of misconduct.

## Decision

The insurance statutory lane is `qualified; proof ladder visible; promotion
open; no-ranking`. Apollo/Athene remains the lead proof chase and Accordia the
comparison. Neither route can be promoted to liability-adjusted common-owner
return until one named asset closes the chain from legal entity through receipt,
liability cost, remittance, and after-cost return.

## Sources

- [Insurance statutory named-asset admission](combined-investment-research-insurance-statutory-named-asset-admission-2026-09-17.md)
- [Insurance statutory evidence panel](combined-investment-research-insurance-statutory-named-asset-evidence-panel-2026-09-17.md)
- [Insurance named-asset proof ladder](combined-investment-research-insurance-named-asset-proof-ladder-2026-09-17.md)
- [Apollo/KKR statutory named-asset selection](capital-flow-apollo-kkr-statutory-named-asset-selection-pass-1.md)
