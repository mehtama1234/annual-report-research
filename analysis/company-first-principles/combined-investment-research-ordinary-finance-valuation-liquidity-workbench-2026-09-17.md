# Ordinary finance valuation and liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench converts the Q2 2026 ordinary-finance refresh into
business-specific valuation objects, loss and capital burdens, liquidity
stresses, and filing-based thesis breakers. It does not apply an industrial
FCF multiple to banks or rank JPMorgan, American Express, and Capital One.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/capital denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| JPMorgan | Normalized net interest income, fee/markets revenue, credit losses, operating expense, capital requirement, and common payout capacity | Deposit funding cost, loan growth, technology/regulatory expense, reserves, CET1, preferred claims, and dilution | Deposit outflow or beta, credit-cycle loss, market shock, collateral call, regulatory capital demand, or funding spread | Visa-share/exceptional gain or reserve build supports earnings while charge-offs, funding cost, or CET1 pressure rises |
| American Express | Membership/fee retention, billed-business conversion, merchant economics, rewards, service margin, credit losses, and common earnings | Rewards and benefits, marketing, funding, reserve/charge-off burden, SBC, technology, and capital | Consumer stress, higher write-offs, reserve reversal, funding-cost pressure, merchant/fee regulation, or member attrition | Billed business grows while fee retention weakens, rewards cost rises, write-offs increase, or reserve release masks credit deterioration |
| Capital One | Loss-adjusted card/auto spread, deposit funding, Discover network economics, integration-adjusted expense, capital generation, and diluted common return | Credit reserves, net charge-offs, deposit beta, integration and purchase accounting, regulatory capital, rewards, and dilution | Unemployment/consumer loss, deposit competition, Discover integration failure, capital shortfall, liquidity spread, or refinancing | Pre-provision earnings and allowance release rise while net charge-offs, integration cash, funding cost, or CET1 burden worsens |

## Current evidence anchors

- JPMorgan reported Q2 net income of `$21.2B`, revenue of `$57.3B`, average
  loans of `$1.5T`, average deposits of `$2.7T`, credit costs of `$2.5B`, net
  charge-offs of `$2.4B`, a `$149M` net reserve build, and standard CET1 of
  `14.1%`. The `$4.55B` pretax Visa-share gain is not recurring spread or fee
  income.
- American Express reported Q2 billed business of `$455.8B`, revenue net of
  interest expense of `$19.637B`, credit-loss provision of `$1.084B`, Q2 net
  income of `$3.110B`, H1 credit-loss provision of `$2.336B`, and H1 SBC of
  `$358M`. Lower provision alongside higher write-offs requires a reserve
  roll-forward rather than a simple earnings upgrade.
- Capital One reported Q2 net revenue of `$15.9B`, loans held for investment
  of `$457.2B`, deposits of `$484.3B`, provision of `$2.980B`, net charge-offs
  of `$3.642B`, a `$662M` allowance release, NIM of `8.01%`, and CET1 of
  `13.7%`. Q2 also included `$494M` acquisition amortization, `$298M`
  Discover integration, and `$96M` Brex integration pre-tax adjustments.

## QoE and financial-shenanigans prompts

1. Remove JPMorgan's Visa-share gain from recurring earnings and test whether
   net interest income, fee income, credit costs, and capital support the same
   payout capacity.
2. Reconcile American Express reserve release, write-offs, billed business,
   fee-paying members, rewards, and funding cost before treating spending growth
   as durable common economics.
3. Separate Capital One's allowance release and pre-provision earnings from
   net charge-offs, Discover integration cash, deposit funding, and CET1 needs.
4. Treat CET1 as a distribution constraint and reinvestment requirement, not
   as excess cash available to shareholders.
5. Do not compare bank net income or pre-provision earnings to industrial OCF;
   the economic numerator is loss-adjusted earnings after required capital.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what spread, fee retention, credit
cost, capital ratio, and payout growth the market price requires. The
Lyn Alden-style stress test asks whether deposits, funding, collateral,
regulatory capital, and common distributions survive a higher-rate,
unemployment, inflation, consumer-loss, or market-volatility regime.

The key distinction is that liquidity is partly a confidence-and-funding
system, not merely a cash balance. A bank can report large deposits and
capital while still facing a distribution constraint, rising funding beta,
collateral pressure, or a requirement to retain earnings.

## Promotion boundary

`ordinary-finance-qualified; loss-and-capital-normalization-open; no-ranking`

Promotion requires same-period loss curves, reserve roll-forwards, funding
cost, capital requirements, integration/rewards expense, and diluted common
distribution capacity. Billed business, deposits, loans, pre-provision
earnings, reserve releases, and exceptional gains remain diagnostic inputs,
not normalized owner cash.

## Sources

- [Ordinary finance Q2 2026 credit-quality refresh](combined-investment-research-ordinary-finance-q2-2026-credit-quality-refresh-2026-09-17.md)
- [JPMorgan Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm)
- [American Express Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/4962/000000496226000322/axp-20260630.htm)
- [Capital One Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/927628/000092762826000089/cof-20260630.htm)

