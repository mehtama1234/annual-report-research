# Magnite programmatic advertising and CTV valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Magnite from an advertising-agencies packet into a company-specific valuation object. It separates CTV from DV+, contribution ex-TAC from gross billings and traffic-acquisition pass-throughs, publisher and buyer relationships, take rates, receivables, AI and agentic tooling, regulatory exposure, acquisitions, debt, and diluted common residual. It does not treat gross revenue, contribution, adjusted EBITDA, CTV growth, free cash flow, or buybacks as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Magnite | Collected independent sell-side advertising cash after publisher supply, buyer demand, traffic-acquisition costs, CTV/DV+ take rates, data and curation, receivables, AI tooling, regulation, acquisitions, debt, and dilution | Platform engineering, supply-path integration, publisher/buyer onboarding, data and measurement, sales, AI/agentic workflow, compliance, acquisitions, working capital, and repurchases | CTV budget slowdown, walled-garden or DSP disintermediation, Google remedies, publisher concentration, take-rate pressure, political-ad volatility, receivable timing, acquisition integration, debt, or dilution | Contribution and CTV growth rise while ex-TAC take rate, publisher retention, buyer demand, receivables, platform cost, regulatory position, or diluted per-share cash deteriorate |

## Current evidence anchors

- Q2 2026 contribution ex-TAC was about `$189.6M`, up `17%`; CTV contribution ex-TAC `$97.1M`, up `36%`; DV+ `$92.5M`, up `2%`; net income `$19.4M`; adjusted EBITDA `$70.6M`; operating cash flow `$57.4M`.
- Q1 2026 contribution ex-TAC was about `$160.9M`, up `10%`; CTV `$82.3M`, up `30%`; DV+ `$78.6M`, down `5%`; adjusted EBITDA `$42.9M`; operating cash flow `$23.3M`.
- FY2025 CTV contribution ex-TAC was about `$304.2M`, up `17%` or `22%` excluding political advertising, and represented `45%` of total contribution ex-TAC.
- Magnite raised FY2026 contribution ex-TAC growth to `13%`–`14%`, adjusted EBITDA growth above `20%`, and adjusted EBITDA margin to at least `37%`; management also guided free-cash-flow growth to the high `40%` range.
- Magnite repurchased or withheld about `5.2M` shares for `$79.2M` in 2025 and authorized a new `$200M` repurchase program; capital returns require SBC, platform investment, debt, and common-residual reconciliation.

## QoE and financial-shenanigans prompts

1. Reconcile gross billings, traffic-acquisition costs, contribution ex-TAC, take rates, publisher payments, buyer collections, credits, makegoods, and receivables.
2. Separate CTV, DV+, audio, display, and video surfaces; political advertising and event timing can distort comparisons and should not be treated as recurring growth.
3. Test publisher and buyer retention, supply-path quality, data/measurement costs, curation, fraud, brand safety, and platform dependence before accepting contribution growth as durable.
4. Keep AI and agentic-product claims tied to realized workflow savings, customer adoption, engineering cost, and regulatory or privacy obligations.
5. Reconcile adjusted EBITDA, operating cash flow, working capital, acquisitions, debt, SBC, share withholding, repurchases, and diluted shares before accepting FCF or buybacks as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what CTV share, contribution ex-TAC, take rate, publisher retention, buyer demand, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether fragmented media remains independent enough to support the intermediary, whether platforms and regulation compress the toll, and whether working capital, AI investment, or debt consume liquidity before ad-market growth reaches common owners.

## Promotion boundary

`magnite-programmatic-ctv-qualified; supplypath-takerate-and-owner-cash-open; no-ranking`

Promotion requires same-entity joins from publisher inventory and buyer demand to ex-TAC collections, take rates, publisher settlement, receivables, retention, fraud and measurement cost, platform investment, regulatory claims, debt, funding, and diluted common residual. Gross revenue, contribution, CTV growth, adjusted EBITDA, FCF, guidance, and buybacks remain diagnostic inputs.

## Sources

- [Magnite company packet](../../extracted/technology/advertising-agencies/magnite-inc/company-packet.md)
- [Magnite source ledger](../../extracted/technology/advertising-agencies/magnite-inc/source-ledger.md)

