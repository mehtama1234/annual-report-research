# Alnylam RNAi therapeutics and franchise valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Alnylam from a biotechnology packet into a company-specific valuation object. It separates TTR and rare-franchise product collections from diagnosis, reimbursement, label expansion, partner economics, launch cost, pipeline trials, manufacturing, royalty obligations, debt, claims, and diluted common residual. It does not treat product revenue, prescriptions, guidance, milestones, adjusted earnings, or buybacks as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Alnylam | Risk-adjusted commercial RNAi cash after AMVUTTRA/TTR adoption, rare-disease products, diagnosis, reimbursement, partner and royalty economics, launch infrastructure, clinical trials, manufacturing, debt, and dilution | Pipeline trials, regulatory submissions, launch and medical affairs, manufacturing and supply, patient identification, reimbursement support, R&D, royalties, partner obligations, and repurchases | ATTR-CM launch or reimbursement slowdown, TTR concentration, label or safety issue, competing therapy, trial failure, partner economics, pricing pressure, manufacturing constraint, debt, or dilution | TTR product revenue rises while diagnosis, reimbursement, net price, persistence, pipeline return, partner/royalty burden, or diluted per-share cash deteriorate |

## Current evidence anchors

- Q2 2026 TTR revenue was about `$1.03B`; AMVUTTRA contributed about `$1.012B` and ONPATTRO about `$18M`; rare-franchise revenue from GIVLAARI and OXLUMO was about `$142M`.
- Q1 2026 global net product revenue was about `$1.036B`, up `121%`, and total TTR revenue about `$910M`, up `153%`.
- FY2025 global net product revenue was about `$2.987B`, up `81%`, and the company reached GAAP and non-GAAP profitability for the year.
- Management lowered TTR product-sales guidance after early ATTR-CM launch learnings while maintaining a long-term TTR and pipeline strategy; guidance change is therefore a live quality-of-growth signal.
- The company’s value is concentrated in the TTR franchise even as RNAi pipeline readouts and Alnylam 2030 expansion create future optionality; current commercial cash and future optionality must remain separate.

## QoE and financial-shenanigans prompts

1. Reconcile gross product sales to net product revenue, rebates, chargebacks, returns, payer mix, collections, persistence, and patient access; launch revenue is not automatically durable cash.
2. Separate AMVUTTRA and ONPATTRO from GIVLAARI/OXLUMO, collaborations, royalties, and milestone economics so one franchise cannot mask the rest of the platform.
3. Test ATTR-CM diagnosis, physician adoption, reimbursement, treatment sequencing, label expansion, and competition against the TTR forecast rather than accepting headline growth.
4. Keep clinical-trial, manufacturing, regulatory, medical-affairs, patient-identification, and launch-support spending visible as required reinvestment.
5. Reconcile partner obligations, royalty streams, debt, SBC, share count, milestone receipts, and repurchases before accepting adjusted earnings or profitability as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what diagnosis rate, treatment persistence, net price, TTR franchise life, pipeline probability, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether specialty reimbursement and patient access can support a concentrated franchise through launch friction, competitive entry, trial setbacks, pricing pressure, and funding or dilution needs.

## Promotion boundary

`alnylam-rnai-franchise-qualified; ttr-concentration-and-pipeline-cash-open; no-ranking`

Promotion requires same-entity joins from product demand to reimbursement, collection, persistence, manufacturing, partner and royalty settlement, trial and launch reinvestment, claims, funding, and diluted common residual. Product revenue, prescriptions, guidance, milestones, adjusted earnings, profitability, and buybacks remain diagnostic inputs.

## Sources

- [Alnylam company packet](../../extracted/healthcare/biotechnology/alnylam-pharmaceuticals-inc/company-packet.md)
- [Alnylam source ledger](../../extracted/healthcare/biotechnology/alnylam-pharmaceuticals-inc/source-ledger.md)

