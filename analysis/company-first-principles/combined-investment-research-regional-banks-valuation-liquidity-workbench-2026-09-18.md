# Regional and commercial banking valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves PNC, Truist, U.S. Bancorp, and Regions Financial from
banking evidence into company-specific valuation objects. It does not apply an
industrial OCF framework to banks: the relevant residual is earnings after
funding, credit losses, securities/liquidity costs, operating investment,
regulatory capital, and the claims of depositors and preferred/common holders.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| PNC | Relationship-bank earnings and excess-capital cash after deposit beta, credit losses, securities/liquidity, fee attachment, acquisition integration, and CET1 requirements | Loan growth, credit reserves, branches/digital, treasury systems, compliance, capital markets, acquisitions, and common capital | Deposit migration, commercial/CRE deterioration, securities marks, acquisition dilution, capital-rule change, or funding spread | ROTCE and fee growth rise while deposits become expensive/unstable, criticized credit, capital consumption, or common value deteriorates |
| Truist | Merger-repair earnings after deposit funding, credit normalization, duplicate-cost removal, legal/controls, and CET1 capital | Systems integration, branch/digital, loan growth, compliance, merger restructuring, debt/preferred claims, and common capital | Merger execution failure, deposit runoff, credit losses, securities marks, legal/control cost, or capital shortfall | Cost saves and EPS rise while deposit quality, credit, controls, capital, or tangible-common recovery weaken |
| U.S. Bancorp | Payments-and-banking earnings after deposit funding, credit losses, fraud/technology, securities, and regulated capital | Payments technology, merchant/treasury systems, loan/securities growth, fraud controls, acquisitions, and capital | Deposit repricing, payment/fraud shock, commercial/consumer loss, securities/liquidity stress, or capital requirement | Fee growth and ROTCE rise while deposit/loan growth outruns capital, credit losses, fraud cost, or diluted common value |
| Regions | Southeast relationship-bank earnings after low-cost deposit retention, credit losses, fee attachment, and capital | Branch/treasury/wealth systems, credit provision, technology, compliance, and common capital | Deposit beta, Southeast CRE/consumer deterioration, reserve release reversal, liquidity, or capital stress | Low deposit cost and fee records persist while charge-offs, criticized loans, capital, or tangible common value deteriorate |

## Current evidence anchors

- PNC FY2025 revenue was `$23.099B`, net interest income `$14.410B`, fee
  income `$7.925B`, year-end loans/deposits `$331.5B`/`$440.9B`, and CET1
  `10.6%`; Q2 2026 CET1 was `9.9%`.
- Truist FY2025 revenue was `$20.319B`, net interest income `$14.423B`, and
  noninterest income `$5.896B`; Q2 2026 CET1 was approximately `10.9%`. FY2025
  included `$156M` severance, `$130M` legal settlement accrual, and `$19M` of
  securities losses.
- U.S. Bancorp FY2025 net revenue was `$28.656B`, provision for credit losses
  `$2.186B`, and ROTCE `18.1%`; Q2 2026 loans rose `7.1%` year over year while
  deposits rose `2.4%`.
- Regions FY2025 earnings were approximately `$2.1B`, Q2 2026 common earnings
  `$549M`, CET1 approximately `10.7%`, and annualized Q2 net charge-offs about
  `42` basis points.

## QoE and financial-shenanigans prompts

1. Normalize net interest income for rate cycle, deposit beta, securities
   repricing, purchase accounting, and wholesale funding.
2. Reconcile loan growth through underwriting, criticized/nonaccrual loans,
   charge-offs, reserves, collateral, and capital consumption.
3. Separate securities marks, AOCI, liquidity facilities, pledged collateral,
   uninsured deposits, and runnable funding from tangible common value.
4. Keep merger savings, severance, legal settlements, securities losses,
   acquisitions, and buybacks separate from durable return on common equity.
5. Test fee growth against client retention, payments volume, fraud/technology
   cost, regulatory capital, and diluted common value.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what sustainable ROTCE, credit loss,
deposit cost, capital ratio, growth, payout, and cost of equity the price
requires. The Lyn Alden-style stress test asks whether deposits remain stable,
collateral values hold, securities liquidity survives, and capital can absorb a
credit or funding shock without forced issuance or common-owner impairment.

## Promotion boundary

`regional-bank-qualified; deposit-credit-capital-open; no-ranking`

Promotion requires same-entity, same-period joins from deposits and loans
through funding cost, credit losses, securities/liquidity, regulatory capital,
legal-entity availability, and diluted common residual. Revenue, NII, ROTCE,
deposits, loan growth, CET1, dividends, and buybacks remain diagnostic inputs,
not industrial owner-cash measures.

## Sources

- [PNC deep company packet](../deep-company-pages/pnc-financial-services-group-inc.md)
- [Truist deep company packet](../deep-company-pages/truist-financial-corp.md)
- [U.S. Bancorp deep company packet](../deep-company-pages/us-bancorp.md)
- [Regions deep company packet](../deep-company-pages/regions-financial-corp.md)
