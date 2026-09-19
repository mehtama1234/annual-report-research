# Healthcare distribution valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves McKesson, Cencora, and Cardinal Health from period-labeled
cash and legal-claim diagnostics into company-specific valuation, reinvestment,
liquidity, and thesis-breaker objects. It preserves McKesson's Q1 FY2027,
Cencora's 9M FY2026, and Cardinal's FY2026 periods rather than creating a
cross-company ratio ranking.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| McKesson | Drug-distribution gross profit and collected cash after inventory/receivables funding, Apollo preferred claims, acquisitions, debt, and dilution | Distribution working capital, PP&E/software, acquisitions, specialty/medical-surgical investment, preferred/redemption claims, and repurchases | Payable reversal, receivable/inventory funding, supplier terms, payer/customer concentration, preferred cash, and refinancing | Reported adjusted earnings or repurchases rise while normalized working capital, preferred claims, collections, or common residual deteriorate |
| Cencora | Specialty/distribution cash after working capital, OneOncology and RCA acquisition cohorts, contingent consideration, LIFO/legal items, and dilution | Inventory/receivables, capex, OneOncology/RCA purchase price, contingent consideration, integration, debt, and SBC | Acquisition financing, supplier terms, reimbursement, specialty customer concentration, LIFO volatility, and legal cash | Adjusted EPS/FCF rises while post-close cohort cash, working capital, contingent claims, or diluted residual weakens |
| Cardinal Health | Distribution and specialty workflow cash after acquisitions, opioid/legal payments, debt reduction, CVS concentration, tariff/LIFO effects, and dilution | `$649M` capex, `$1.991B` acquisitions, Solaris consideration, opioid payments, debt, repurchases, and dividends | Customer concentration, legal settlement schedule, working-capital reversal, tariff/refund timing, debt, and refinancing | OCF and capital returns rise while legal claims, acquisition return, normalized CVS working capital, or common residual deteriorates |

## Current evidence anchors

- McKesson Q1 FY2027 OCF was `$(220)M`; receivables/inventory used `$4.448B`,
  payables supplied `$3.773B`, PP&E/software was `$175M`, acquisitions were
  `$23M`, and Apollo preferred capital plus `$2.6B` shareholder returns alter
  the common-owner perimeter.
- Cencora 9M FY2026 OCF was `$1.688B`, capex `$511M`, acquisition cash
  `$4.974B`, adjusted FCF `$1.142B`, and the acquisition screen after capex was
  approximately `$(3.797B)`; OneOncology includes `$752M` contingent
  consideration and a `$1.087B` remeasurement gain.
- Cardinal FY2026 OCF was `$5.174B`, capex `$649M`, acquisitions `$1.991B`,
  and the residual after acquisitions and capex was approximately `$2.534B`.
  After listed repurchases, dividends, and debt reduction, the screen was
  approximately `$32M`; the July 2026 `$374M` opioid payment and future claims
  remain period-separated.

## QoE and financial-shenanigans prompts

1. Use gross profit, rebates, inventory, receivables, supplier terms, and
   collections—not revenue alone—as the distribution denominator.
2. Normalize payable and receivable/inventory timing over comparable quarters;
   a working-capital release is not a permanent cash margin.
3. Keep acquisitions, contingent consideration, amortization, integration,
   LIFO, remeasurement gains, and legal credits/payments in the return hurdle.
4. Separate preferred equity, redeemable NCI, VIEs, held-for-sale entities,
   debt, taxes, and dilution before naming common-owner cash.
5. Treat repurchases and dividends as financing choices, not evidence of
   surplus cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what normalized gross profit,
working-capital rate, acquisition return, legal burden, reinvestment, terminal
growth, and cost of capital the market price requires. The Lyn Alden-style
stress test asks whether liquidity tightening, reimbursement pressure,
drug-price/LIFO volatility, supplier terms, customer concentration, acquisition
financing, and legal settlements can be funded without impairing the common
residual.

## Promotion boundary

`healthcare-distribution-qualified; period/cohort-normalization-open; no-ranking`

Promotion requires same-entity comparable periods, normalized working-capital
settlement, post-close cohort cash, legal/acquisition cash, financing and
preferred/NCI claims, debt, dilution, and a common-owner residual. Adjusted
FCF, OCF, acquisition scale, repurchases, and revenue remain diagnostic inputs.

## Sources

- [Healthcare distribution current-period synthesis](combined-investment-research-healthcare-distribution-current-period-synthesis-2026-09-17.md)
- [Healthcare distribution owner-cash denominator pass](combined-investment-research-healthcare-distribution-owner-cash-denominator-pass-2-2026-09-17.md)
- [McKesson longitudinal cash perimeter](combined-investment-research-mckesson-longitudinal-cash-perimeter-pass-2-2026-09-17.md)
- [Cencora OneOncology return bridge](combined-investment-research-cencora-oneoncology-return-bridge-pass-2-2026-09-17.md)
- [Cardinal Solaris/legal owner-cash pass](combined-investment-research-cardinal-solaris-legal-owner-cash-pass-2-2026-09-17.md)
