# Medpace clinical-trial infrastructure valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Medpace from a healthcare packet into a company-specific valuation object. It separates trial design, site and patient execution, regulatory coordination, therapeutic expertise, sponsor awards, backlog conversion, employee utilization, study mix, working capital, claims, and diluted common residual. It does not treat awards, backlog, book-to-bill, revenue, EBITDA, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Medpace | Clinical-development workflow cash after study design, patient and site execution, regulatory services, sponsor collections, employee capacity, trial delivery, quality obligations, technology, claims, and dilution | Clinical staff hiring and retention, site and patient payments, trial start-up, technology, global facilities, working capital, contract assets, study-specific costs, compliance, and repurchases | Sponsor budget cuts, trial cancellations, award volatility, backlog slippage, patient/site cost inflation, regulatory or quality failure, employee attrition, receivable aging, or dilution | Revenue and EBITDA grow while net new awards, book-to-bill, backlog conversion, sponsor collections, utilization, study costs, or diluted per-share cash deteriorate |

## Current evidence anchors

- Q2 2026 revenue was about `$707.3M`, net new business awards about `$795.7M`, net book-to-bill `1.13x`, and EBITDA about `$153.4M` or `21.7%` of revenue.
- Q1 2026 revenue was about `$706.6M`, awards about `$618.4M`, and net book-to-bill `0.88x`, demonstrating that award timing can diverge from current-period revenue conversion.
- Q4 2025 revenue was about `$708.5M`, awards about `$736.6M`, net book-to-bill `1.04x`, and EBITDA margin about `22.6%`.
- Backlog was about `$3.0B`; the platform had about `6,300` employees across `46` countries, making capacity and labor execution part of the cash bridge.
- The therapeutic mix includes oncology, cardiology, metabolic disease, endocrinology, CNS, and anti-viral/anti-infective work; sponsor concentration, study cancellations, and protocol mix therefore require company-specific testing.

## QoE and financial-shenanigans prompts

1. Reconcile awards, backlog, book-to-bill, revenue recognition, contract assets, sponsor billings, collections, and cancellations; backlog is not a receivable or owner cash.
2. Test study margin by therapeutic area and phase against employee utilization, site and patient payments, pass-through costs, start-up timing, and protocol amendments.
3. Keep hiring, retention, training, technology, quality, regulatory, and global-facility spending visible as required capacity investment rather than treating an asset-light model as costless.
4. Examine sponsor funding quality and receivable aging when awards rise faster than cash collections, especially during biotech funding or pharma-budget stress.
5. Reconcile EBITDA, operating cash flow, contract liabilities/assets, claims, share repurchases, SBC, and diluted shares before accepting per-share growth as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what award rate, backlog conversion, study margin, employee utilization, cancellation rate, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether sponsor budgets and clinical funding remain available through a biotech financing slowdown, whether site and patient costs absorb cash before collection, and whether regulatory or quality events create liabilities that adjusted earnings understate.

## Promotion boundary

`medpace-clinical-trial-infrastructure-qualified; backlog-and-sponsor-collection-open; no-ranking`

Promotion requires same-entity joins from sponsor awards and backlog to study delivery, billings, collections, site and patient payments, employee capacity, quality and regulatory claims, required reinvestment, funding, and diluted common residual. Awards, backlog, book-to-bill, revenue, EBITDA, guidance, and buybacks remain diagnostic inputs.

## Sources

- [Medpace company packet](../../extracted/healthcare/diagnostic-substances/medpace-holdings-inc/company-packet.md)
- [Medpace source ledger](../../extracted/healthcare/diagnostic-substances/medpace-holdings-inc/source-ledger.md)

