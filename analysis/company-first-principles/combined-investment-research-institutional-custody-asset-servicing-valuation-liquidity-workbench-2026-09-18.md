# Institutional custody and asset-servicing valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves State Street from institutional-scale evidence into a
company-specific valuation and liquidity object. It separates custody,
administration, securities processing, asset management, FX, securities finance,
net interest income, client assets, bank capital, technology, and operational
risk from benchmark/data vendors, exchanges, and alternative asset managers.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| State Street | Institutional servicing and management fee cash after client retention, fee rates, market/activity sensitivity, technology/control investment, bank liquidity, collateral, capital, and dilution | Custody and fund-administration systems, settlement, cybersecurity, software, client implementation, compensation, regulatory capital, collateral/liquidity, acquisitions, and common capital | Market drawdown, fee compression, client outflow, deposit repricing, NII decline, collateral/counterparty stress, operational failure, remediation, or capital pressure | AUC/A, AUM, fee revenue, EPS, or buybacks rise while fee rates, client retention, control investment, liquidity, tangible capital, or diluted common cash deteriorate |

## Current evidence anchors

- FY2025 total revenue excluding notable items was about `$14.0B`, fee revenue about `$11.0B`; Q2 2026 total revenue was about `$4.0B`, up `17%`, and fee revenue rose `13%`.
- Q2 2026 AUC/A was approximately `$50.7T` and AUM approximately `$5.1T`; these are scale measures, not interchangeable revenue or ownership claims.
- Q2 2026 EPS was `$3.15` and `$3.65` excluding notable items; adjusted operating leverage must be reconciled to technology, cybersecurity, compliance, and capital requirements.
- The institutional bank carries deposits, collateral, liquidity, securities finance, regulatory capital, operational, and counterparty claims in addition to fee-platform economics.
- Client assets are not State Street assets; the cash test is fee-paying activity after servicing cost, control investment, NII/FX/securities-finance normalization, and diluted common claims.

## QoE and financial-shenanigans prompts

1. Separate AUC/A from AUM, market appreciation from net flows, and custody/administration fees from management, FX, securities finance, software, and NII.
2. Track fee rate, wallet share, client retention, concessions, transaction volumes, collateral, and revenue per asset/account.
3. Reconcile adjusted earnings and operating leverage to technology, cybersecurity, operational resilience, remediation, compensation, regulatory capital, and diluted shares.
4. Keep client securities and collateral separate from State Street's own assets, deposits, liquidity, loans, and capital requirements.
5. Stress market levels, client outflows, deposit repricing, NII, collateral calls, counterparty risk, cyber/settlement failure, and client concentration.
6. Treat AUC/A, AUM, EPS, dividends, and buybacks as diagnostic until recurring fee cash survives control and bank-capital requirements.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what custody retention, fee rate,
management flows, transaction activity, technology productivity, regulatory
capital, normalized NII, and cost of capital the valuation requires. The Lyn
Alden-style stress test asks whether market drawdown, rates, collateral demand,
institutional cost-cutting, counterparty stress, and liquidity regulation can
be absorbed without impairing the servicing franchise.

## Promotion boundary

`institutional-custody-asset-servicing-qualified; fee-control-and-common-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from custody/AUM activity to
fee rates, flows, transaction volume, client retention, technology/control
spend, collateral/liquidity, regulatory capital, NII/FX/securities-finance
normalization, and diluted common residual. AUC/A, AUM, fee revenue, EPS, OCF,
and buybacks remain diagnostic inputs.

## Sources

- [State Street deep company page](../deep-company-pages/state-street-corp.md)
- [State Street company packet](../../extracted/financial/asset-management/state-street-corp/company-packet.md)
- [State Street source ledger](../../extracted/financial/asset-management/state-street-corp/source-ledger.md)
