# Bank of America deposit, credit, and capital valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Bank of America from a money-center-bank packet into a bank-specific valuation object. It separates deposit funding, loan and lease growth, net interest income, markets and fee businesses, credit losses, securities duration, liquidity, capital ratios, regulatory constraints, technology investment, capital return, and diluted common equity. It does not treat bank operating cash flow, revenue, EPS, deposits, loan growth, or buybacks as normalized owner cash without a bank capital and asset-quality bridge.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Bank of America | Risk-adjusted common equity earnings after deposit pricing, loan and lease growth, net interest income, fee and markets revenue, provision, securities marks, regulatory capital, technology, legal claims, and dilution | Credit provisioning, reserve build, risk-weighted assets, liquidity buffer, securities portfolio, branches and technology, deposit franchise investment, regulatory capital, and common repurchases | Deposit runoff or repricing, credit deterioration, commercial/card losses, rates and securities marks, liquidity stress, capital-rule change, legal/regulatory claims, funding costs, or dilution | EPS and capital returns rise while deposit beta, credit losses, reserve adequacy, securities/liquidity marks, risk-weighted assets, or diluted common equity deteriorate |

## Current evidence anchors

- FY2025 revenue was about `$113.1B`, net income about `$30.5B`, and diluted EPS `$3.81`.
- Average 2025 deposits were about `$1.98T`, reaching about `$2.02T` at year-end; average loans and leases were about `$1.14T`, reaching about `$1.19T` at year-end.
- Q2 2026 revenue was about `$31.6B`, net income about `$9.1B`, diluted EPS `$1.21`, and FTE net interest income about `$16.0B`.
- Q2 provision for credit losses was about `$1.4B`, net charge-off ratio `0.47%`, and card delinquency trends improved year over year for a fifth consecutive quarter.
- BAC returned more than `$30B` in 2025 and about `$8B` in Q2 2026; capital return must be tested against regulatory capital, reserve needs, deposit stability, and diluted share count.

## QoE and financial-shenanigans prompts

1. Reconcile average and ending deposits, deposit mix, beta, uninsured or concentrated funding, loan growth, credit migration, and net interest income; balances alone do not prove franchise economics.
2. Test provision expense, charge-offs, delinquency, reserve coverage, card and commercial exposure, and criticized assets across the cycle.
3. Separate securities duration and marks, liquidity buffers, wholesale funding, collateral, regulatory capital, and stress-test constraints from reported earnings.
4. Keep Markets, investment banking, wealth, card, consumer, and commercial fee income distinct from spread income and credit risk.
5. Reconcile CET1 and other capital ratios, tangible common equity, legal/regulatory claims, technology spending, dividends, repurchases, SBC, and diluted shares before treating EPS growth as common-owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what deposit franchise, loan growth, net interest margin, fee mix, credit cost, capital requirement, payout ratio, and cost of equity the valuation requires. The Lyn Alden-style stress test asks whether deposits remain stable through rate and confidence shocks, whether credit losses and securities duration consume capital, and whether regulatory liquidity constraints prevent reported earnings from becoming distributable common cash.

## Promotion boundary

`bank-of-america-deposit-credit-qualified; capital-and-asset-quality-open; no-ranking`

Promotion requires same-entity joins from deposits and loans to pricing, collections, credit migration, reserves, securities and liquidity marks, regulatory capital, funding, legal claims, dividends, repurchases, and diluted common equity. Deposits, loan growth, revenue, EPS, bank OCF, guidance, and buybacks remain diagnostic inputs.

## Sources

- [Bank of America company packet](../../extracted/financial/money-center-banks/bank-of-america-corporation/company-packet.md)
- [Bank of America source ledger](../../extracted/financial/money-center-banks/bank-of-america-corporation/source-ledger.md)

