# Insurance risk and brokerage valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Chubb, Aon, and Marsh McLennan from insurance and
brokerage evidence into separate valuation objects. It keeps underwriting and
policyholder-liability economics distinct from fee-led brokerage and advisory
cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Chubb | P&C/life underwriting and investment-float earnings after claims, reserve development, catastrophe, reinsurance, asset-liability matching, statutory capital, debt, and dilution | Premium acquisition, claims systems, reserves, reinsurance, invested assets, regulatory capital, life spread, debt, and common capital | Catastrophe, adverse reserve development, reinsurance recoverability, credit losses, rates, restricted cash, or capital requirement | Premium and investment income rise while combined ratio, reserve adequacy, catastrophe load, reinsurance, or common surplus deteriorates |
| Aon | Client-risk and benefits advisory cash after commission/fee collection, talent, acquisitions, pensions, restructuring, debt, and dilution | Advisory technology, analytics, producer talent, receivables, acquisitions, pension, restructuring, and common capital | Client collection, M&A integration, insurance-cycle softness, pension, debt, FX, or fiduciary/legal claims | Organic growth and margin rise while receivables, acquisition return, restructuring, debt, or diluted cash weaken |
| Marsh McLennan | Institutional risk/advisory and reinsurance-placement cash after fee collection, talent, acquisitions, debt, pensions, and dilution | Broker/advisory workforce, analytics, receivables, acquisitions, technology, pensions, debt, and buybacks | Client retention, catastrophe/reinsurance cycle, acquisition integration, talent cost, debt, or regulatory claims | Adjusted margins and fee growth rise while acquisition cash, receivables, talent costs, debt, or common residual deteriorate |

## Current evidence anchors

- Chubb FY2025 net income was `$10.31B`, net premiums written `$54.84B`,
  pre-tax net investment income `$6.5B`, operating cash flow `$12.816B`, and
  long-term debt `$15.728B`; common buybacks were `$3.694B` and dividends
  `$1.505B`. Its reported P&C combined ratio was `85.7%`.
- Aon FY2025 revenue was approximately `$17.2B`, operating cash flow `$3.481B`,
  acquisition cash `$394M`, capex `$263M`, and business-sale gain `$1.201B`.
  H1 2026 OCF was `$986M`, capex `$140M`, and acquisition cash `$322M`.
- Marsh FY2025 OCF was `$5.292B`, PP&E spending `$291M`, acquisition cash
  `$652M`, stock compensation `$394M`, and long-term debt `$19.587B`; its
  residual before financing and capital returns was about `$4.349B`.

## QoE and financial-shenanigans prompts

1. For Chubb, reconcile premiums, claims paid, reserves, adverse development,
   catastrophe losses, reinsurance recoverables, invested assets, and statutory
   capital; insurance OCF is not unrestricted owner cash.
2. For Aon and Marsh, reconcile commission/fee receivables, fiduciary balances,
   producer compensation, pensions, restructuring, acquisitions, and client
   retention.
3. Keep Aon's `$1.201B` business-sale gain and acquisition cash separate from
   recurring advisory cash; keep Marsh's acquisition-heavy history visible.
4. Test investment income for duration, credit, realized gains, and asset-
   liability matching rather than treating float yield as permanent spread.
5. Treat buybacks, dividends, adjusted EBITDA, and reported OCF as residual or
   diagnostic measures until policyholder, statutory, legal, and common claims
   are joined.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what underwriting margin, reserve
adequacy, investment yield, fee growth, acquisition return, capital requirement,
and cost of equity the valuation requires. The Lyn Alden-style stress test asks
whether catastrophe, reserve, credit, reinsurance, rates, client budgets,
talent, and debt shocks can impair cash before capital and policyholder claims
are satisfied.

## Promotion boundary

`insurance-risk-brokerage-qualified; claims-reserves-and-fee-collection-open; no-ranking`

Promotion requires same-entity, same-period joins from premium or client fee
through collection, claims/reserves or producer settlement, reinsurance or
fiduciary obligations, statutory/regulatory capital, debt, legal-entity
availability, and diluted common residual. Premiums, float, combined ratio,
organic growth, reported OCF, dividends, and buybacks remain diagnostic inputs.

## Sources

- [Chubb deep company packet](../deep-company-pages/chubb-limited.md)
- [Aon deep company packet](../deep-company-pages/aon-plc.md)
- [Marsh McLennan deep company packet](../deep-company-pages/marsh-mclennan-companies-inc.md)
