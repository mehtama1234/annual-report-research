# Insulet automated insulin-delivery valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Insulet from medical-device evidence into a
company-specific valuation object. It separates recurring Pods, Omnipod
software and algorithms, reimbursement and pharmacy access, CGM integration,
active-user retention, manufacturing, quality, clinical and regulatory gates,
working capital, debt, and diluted common residual. It does not treat Pods
shipped, active users, revenue, adjusted operating income, operating cash flow,
free cash flow, or guidance as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Insulet | Recurring automated-insulin-delivery cash after Pod and software collections, reimbursement and pharmacy settlement, patient retention, CGM and algorithm integration, factory capacity, quality, clinical investment, debt, and dilution | Pod manufacturing and Costa Rica capacity, software and algorithms, clinical trials, quality systems, reimbursement support, inventory, CGM integrations, regulatory filings, and SBC replacement | Reimbursement denial or pressure, patient churn, product or quality event, supply disruption, FDA or clinical delay, CGM partner change, manufacturing underutilization, debt refinancing, or dilution | Revenue and active users grow while Pod retention, reimbursement collection, manufacturing yield, quality claims, required capacity, clinical spend, or diluted per-share cash deteriorate |

## Current evidence anchors

- Q2 2026 revenue was `$801.7M`, up `23.5%`; Omnipod revenue was `$795.9M`,
  operating income `$129.7M`, and adjusted operating income `$154.5M`.
- Q1 2026 revenue was `$761.7M`, up `33.9%`; Q4 2025 revenue was `$783.8M`,
  gross margin `72.5%`, and operating income `$146.3M`.
- Insulet reported more than `600,000` estimated active users globally at the
  end of 2025 and raised 2026 constant-currency revenue-growth guidance to
  `22%`–`24%` in Q2.
- The model combines recurring disposable Pods with software, smartphone
  control, CGM integration, reimbursement, pharmacy placement, and clinical
  expansion into type 2 diabetes; each layer has separate cash and execution
  gates.

## QoE and financial-shenanigans prompts

1. Reconcile Pods shipped and active users to patient retention, prescription
   persistence, reimbursement approval, pharmacy settlement, returns, and cash.
2. Separate recurring Pod economics from software, algorithm, CGM, Calm, and
   future type 2 expansion; test whether each increases durable contribution
   after clinical, regulatory, and support costs.
3. Connect growth to manufacturing yield, factory capacity, inventory, quality
   events, warranty, recalls, and supply-chain resilience.
4. Keep adjusted operating income, guidance, launch timing, and temporary mix or
   currency effects separate from recurring cash conversion.
5. Treat capital returns as residual claims only after capacity, quality,
   clinical, reimbursement, debt, and regulatory obligations are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what active-user growth, Pod retention,
reimbursement, gross margin, factory utilization, type 2 expansion, clinical
investment, reinvestment rate, and cost of capital the valuation requires. The
Lyn Alden-style stress test asks whether diabetes affordability, payer access,
manufacturing, regulatory timing, supply chains, rates, and partner dependence
remain liquid through a chronic-care or device-quality shock without confusing
recurring revenue with durable owner cash.

## Promotion boundary

`insulet-qualified; automated-delivery-and-consumables-open; no-ranking`

Promotion requires same-entity joins from Pods and software to collection,
reimbursement, retention, manufacturing and quality settlement, clinical and
regulatory reinvestment, debt, claims, and diluted common residual. Pods,
active users, revenue, adjusted income, OCF, FCF, and guidance remain diagnostic.

## Sources

- [Insulet company packet](../../extracted/healthcare/medical-instruments-supplies/insulet-corporation/company-packet.md)
- [Insulet source ledger](../../extracted/healthcare/medical-instruments-supplies/insulet-corporation/source-ledger.md)
