# Wildfire-liability regulated-utility valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Edison International from regulated rate-base growth into
a company-specific catastrophe-liability, recovery, financing, affordability,
and diluted-value test. It is distinct from ordinary utility rate-base analysis:
prudent grid investment does not eliminate wildfire claims, insurance gaps,
regulatory delay, or equity-access risk. Core EPS, rate base, capex, dividends,
and regulatory assets are not normalized common-owner cash by themselves.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Edison International / Southern California Edison | Common value after placed-in-service grid investment, allowed return, wildfire claims, insurance and Wildfire Fund recovery, regulatory lag/assets, debt, preferred claims, affordability, and dilution | Distribution/transmission hardening, vegetation management, automation, resilience, generation/load growth, maintenance, claims funding, insurance, and financing access | Severe wildfire, uninsured loss, Wildfire Fund insufficiency, regulatory disallowance/delay, insurance renewal, credit downgrade, equity issuance, or affordability constraint | Core EPS and rate base rise while wildfire claims, regulatory assets, insurance receivables, debt, preferred obligations, or diluted per-share value deteriorate |

## Current evidence anchors

- FY2025 rate base was `$48.206B`, capital expenditures `$6.729B`, core
  earnings `$2.520B`, and core EPS `$6.55`; the 2026–2030 capital plan was
  `$38–41B`.
- Q2 FY2026 GAAP EPS was `$1.39`, core EPS `$1.54`, and 2026 core EPS guidance
  was reaffirmed at `$5.90–$6.20`.
- At June 30, 2026, Edison reported `$808M` of wildfire-related claims and
  `$805M` of long-term insurance receivables. It also reported current and
  long-term regulatory assets of `$2.855B` and `$12.966B`.
- Current debt, short-term debt, and current long-term debt were approximately
  `$2.479B`, `$1.521B`, and `$3.797B`; recovery balances are claims on future
  collection, not cash already available to common owners.

## QoE and financial-shenanigans prompts

1. Reconcile core earnings to GAAP earnings, wildfire claims, insurance,
   settlements, taxes, Wildfire Fund expense, and other excluded items across
   several years; recurring catastrophe costs are not automatically non-core.
2. Separate capex into maintenance, resilience, load growth, generation,
   transmission, distribution, and placed-in-service rate-base additions.
3. Track wildfire claims paid, accrued claims, insurance recoveries, receivables,
   deductibles, self-insured retention, co-insurance, and Wildfire Fund recovery.
4. Reconcile regulatory assets and securitization proceeds to approved recovery,
   collection timing, disallowance risk, and customer bill impact.
5. Test capital-plan returns after construction cost, regulatory lag, financing,
   safety benefit, affordability, and risk reduction—not capex alone.
6. Charge debt, preferred claims, interest, equity issuance, parent/SCE cash,
   noncontrolling claims, dividends, and diluted shares before promotion.
7. Review incentives for rate-base/core-EPS growth that exclude wildfire,
   insurance, storms, settlements, or regulatory items that recur operationally.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what placed-in-service rate base,
allowed return, resilience spending, regulatory recovery, claims burden,
financing cost, and cost of equity the market price requires. The Lyn Alden-
style stress test asks whether a catastrophe can create simultaneous claims,
legal, insurance, credit, regulatory, and affordability pressure before cash is
recovered.

## Promotion boundary

`wildfire-liability-utility-qualified; recovery-and-catastrophe-liquidity-open; no-ranking`

Promotion requires same-period joins from capex to placed-in-service recovery,
earned return, wildfire claims, insurance/Wildfire Fund cash, regulatory assets,
debt, preferred obligations, customer affordability, and diluted common
residual. Core EPS, rate base, capex, dividends, and regulatory assets remain
diagnostic inputs.

## Sources

- [Edison deep company page](../deep-company-pages/edison-international.md)
- [Edison company packet](../../extracted/utilities/electric-utilities/edison-international/company-packet.md)
- [Edison source ledger](../../extracted/utilities/electric-utilities/edison-international/source-ledger.md)
