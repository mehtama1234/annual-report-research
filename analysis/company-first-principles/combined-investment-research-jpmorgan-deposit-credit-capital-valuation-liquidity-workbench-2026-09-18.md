# JPMorgan deposit, credit, and capital valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves JPMorgan Chase from broad bank evidence into a
company-specific valuation object. It separates deposits, lending, securities,
markets, payments, investment banking, credit losses, net interest income,
capital and liquidity, technology, legal claims, dividends, repurchases, and
diluted common equity. It does not treat deposits, loan growth, net revenue,
EPS, bank operating cash flow, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| JPMorgan Chase | Regulated bank common-equity return after deposit pricing, loan collections, credit losses, securities duration, markets risk, payment infrastructure, operating expense, regulatory capital, liquidity, legal claims, and dilution | Technology, branches and payments, risk systems, loan growth, securities liquidity, talent, regulatory capital, reserves, acquisitions, and SBC replacement | Deposit repricing or runoff, consumer or commercial credit deterioration, rates and securities marks, markets loss, capital-rule change, liquidity event, litigation, debt refinancing, or dilution | Revenue, EPS, deposits, loan growth, or buybacks rise while credit migration, funding cost, liquidity, capital ratios, securities marks, or diluted common residual deteriorate |

## Current evidence anchors

- FY2025 total net revenue was `$182.447B` and net income `$57.048B`; year-end
  assets were `$4.4249T` and deposits `$2.5593T`.
- The current-period packet highlights strong Markets revenue, Payments
  strength, technology investment, and favorable Visa and equity-investment
  effects; these are not all recurring spread or fee cash.
- The bank operates across consumer and community banking, commercial banking,
  payments, markets, investment banking, asset management, and custody; each
  carries different capital, liquidity, and risk denominators.

## QoE and financial-shenanigans prompts

1. Reconcile deposits by pricing, mix, maturity, uninsured share, runoff,
   liquidity, and funding cost rather than treating deposit growth as cash.
2. Test loans and leases through vintage, delinquency, charge-offs, reserves,
   collateral, guarantees, and sector concentration; revenue growth is not
   evidence of credit quality.
3. Separate net interest income, markets, investment banking, payments, and
   investment gains; isolate Visa and equity-investment gains from recurring
   operating return.
4. Connect capital return to CET1 and other regulatory constraints, stress
   liquidity, securities duration, legal claims, technology spend, and reserves.
5. Keep adjusted earnings and capital-return narratives separate from the
   diluted common residual actually available after all regulated claims.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what deposit beta, loan growth,
credit losses, net interest margin, markets normalization, capital ratio,
reinvestment rate, and cost of equity the valuation requires. The Lyn
Alden-style stress test asks whether deposit confidence, rates, commercial and
consumer credit, securities marks, liquidity, regulation, and geopolitical risk
remain solvent through a banking shock without confusing balance-sheet scale
with common-owner cash.

## Promotion boundary

`jpmorgan-qualified; deposit-credit-capital-open; no-ranking`

Promotion requires same-entity joins from deposits and loans to pricing,
collection, credit migration, reserves, securities and liquidity marks,
regulatory capital, funding, claims, dividends, repurchases, and diluted common
equity. Deposits, loan growth, revenue, EPS, and repurchases remain diagnostic.

## Sources

- [JPMorgan company packet](../../extracted/financial/money-center-banks/jpmorgan-chase-co/company-packet.md)
- [JPMorgan source ledger](../../extracted/financial/money-center-banks/jpmorgan-chase-co/source-ledger.md)
