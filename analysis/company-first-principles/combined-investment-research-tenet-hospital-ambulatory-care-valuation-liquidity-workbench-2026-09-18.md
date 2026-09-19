# Tenet hospital and ambulatory-care valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Tenet Healthcare from provider-sector evidence into a
company-specific valuation object. It separates hospitals, outpatient care,
USPI ambulatory surgery, payer mix, acuity, supplemental Medicaid programs,
labor, physician alignment, portfolio changes, working capital, debt, and
diluted common residual. It does not treat admissions, adjusted EBITDA,
adjusted free cash flow, net patient revenue, or portfolio growth as normalized
owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Tenet | Acute-care and ambulatory-care cash after payer and patient collections, acuity, labor, physician and facility costs, supplemental-program settlement, surgery-center investment, debt, and dilution | Hospital maintenance and expansion, USPI center development, equipment, labor, physician alignment, working capital, acquisitions, compliance, debt, and SBC replacement | Payer-mix deterioration, exchange or Medicaid funding change, labor inflation, lower acuity or admissions, supplemental-payment timing, facility underperformance, debt refinancing, or dilution | Adjusted EBITDA and ambulatory growth continue while patient collections, payer mix, acuity, labor productivity, supplemental revenue quality, required capex, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net operating revenues were about `$21.310B`, net income available to
  common shareholders about `$1.407B`, and adjusted EBITDA about `$4.566B`.
- At year-end 2025, the hospital segment operated `50` hospitals and `132`
  outpatient facilities; USPI held interests in `533` ambulatory surgery
  centers and `26` surgical hospitals across `37` states.
- Q2 2026 net operating revenues were about `$5.628B`, adjusted EBITDA about
  `$1.304B`, and hospital adjusted EBITDA margin about `18.0%`; the quarter
  included about `$92M` of favorable prior-year Medicaid supplemental revenue.
- Q1 2026 showed lower exchange admissions, unfavorable payer mix, and an
  approximate `$40M` favorable non-recurring CommonSpirit-related revenue
  impact. These items must remain separate from recurring care-delivery cash.

## QoE and financial-shenanigans prompts

1. Reconcile admissions and adjusted admissions to acuity, payer mix, patient
   collections, denial and reserve behavior, supplemental programs, and cash.
2. Separate hospital, outpatient, and USPI economics; test whether ambulatory
   growth reflects durable physician and payer alignment or simply portfolio
   transfer and acquisition accounting.
3. Keep Medicaid supplemental receipts, exchange enrollment, favorable contract
   settlements, and other non-recurring items outside normalized earnings until
   recurrence and settlement are proven.
4. Connect labor, contract staffing, physician arrangements, facility capex,
   equipment, compliance, and service quality to the cash required to maintain
   the network.
5. Treat adjusted FCF, dividends, and repurchases as residual claims only after
   facility reinvestment, working capital, debt, claims, and payer obligations
   are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what same-store volume, acuity,
payer mix, ambulatory conversion, labor productivity, reinvestment rate, and
cost of capital the valuation requires. The Lyn Alden-style stress test asks
whether reimbursement, Medicaid and exchange funding, labor, rates, facility
capital, and patient affordability remain liquid through a provider-cycle
shock without confusing adjusted EBITDA or supplemental revenue with durable
common-owner cash.

## Promotion boundary

`tenet-qualified; hospital-and-ambulatory-cash-open; no-ranking`

Promotion requires same-entity joins from care delivery to patient and payer
collection, acuity and mix, labor and physician settlement, supplemental
program cash, facility and center reinvestment, debt, claims, and diluted
common residual. Admissions, adjusted EBITDA, adjusted FCF, revenue, and
portfolio growth remain diagnostic inputs.

## Sources

- [Tenet company packet](../../extracted/healthcare/medical-care-facilities/tenet-healthcare-corp/company-packet.md)
- [Tenet source ledger](../../extracted/healthcare/medical-care-facilities/tenet-healthcare-corp/source-ledger.md)
