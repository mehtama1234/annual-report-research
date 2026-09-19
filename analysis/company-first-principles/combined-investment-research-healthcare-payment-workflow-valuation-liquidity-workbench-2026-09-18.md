# Healthcare payment workflow valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Waystar from healthcare-information evidence into a
company-specific valuation and liquidity object. It keeps payment workflow
software separate from hospital operations, managed-care payers, healthcare
distribution, care delivery, and medical devices. The object tests whether
provider and patient workflows convert into common-owner cash after processing
costs, implementation, support, R&D, acquisitions, debt, stock compensation,
and dilution.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Waystar | Healthcare payment and revenue-cycle workflow cash after subscription and volume mix, third-party payment costs, implementation/support, collection, product investment, acquisitions, debt, and diluted common residual | Provider versus patient workflow mix, transaction volume, payment-processing cost, receivables, deferred revenue, capitalized software/PP&E, R&D, SBC, acquisition cohorts, debt, and diluted shares | Provider liquidity, patient collection, payer/reimbursement change, lower transaction volume, processing-cost inflation, acquisition funding, refinancing, and regulatory/privacy exposure | Revenue, NRR, adjusted EBITDA, or EPS rise while patient-payment mix, receivables, Iodine returns, SBC dilution, debt, or cash per diluted share deteriorates |

## Current evidence anchors

- FY2025 revenue was `$1.099B`, operating cash flow was `$309.7M`, and
  property/equipment plus capitalized software spending was `$26.5M`, leaving a
  reported recurring-capital residual of about `$283.2M` before acquisitions and
  capital returns.
- Waystar paid `$629.5M` cash and issued about `$620.8M` of stock for Iodine in
  2025. Iodine contributed only `$31.0M` of 2025 revenue, so acquired revenue,
  retention, cross-sell, integration cost, and incremental cash return remain a
  cohort-return question.
- Provider solutions represented approximately 70% of revenue. Patient-payment
  solutions carry substantially higher third-party costs—about 60% of related
  revenue versus roughly 6%–8% for provider solutions—so gross revenue and
  transaction growth cannot be treated as equivalent cash economics.
- Accounts receivable rose to `$177.0M` from `$145.2M`; current deferred revenue
  was `$67.9M` and long-term deferred revenue `$5.5M`. These balances can support
  cash conversion, but require contract-timing and collection reconciliation.
- At December 31, 2025, cash was `$61.4M`, investment securities `$24.9M`, and
  outstanding debt before issuance costs `$1.481B`, with a major maturity in
  2029. Debt reduction, acquisition funding, and liquidity access remain part of
  the valuation rather than post-analysis details.
- FY2025 adjusted EBITDA was `$462.1M` against GAAP net income of `$112.1M`;
  the adjustment bridge included `$42.1M` SBC, `$21.1M` acquisition/integration
  costs, and `$140.5M` depreciation and amortization. The adjustment gap is a
  per-share and replacement-cost control.

## QoE and financial-shenanigans prompts

1. Split subscription, provider-volume, and patient-payment revenue and match
   each to third-party processing cost, contribution margin, collection, and
   customer retention.
2. Reconcile NRR and transaction growth to organic customer cohorts; do not let
   Iodine or future acquisitions make consolidated growth look organic.
3. Test whether deferred revenue is durable contract funding or merely billing
   timing, and whether the receivables increase is supported by collection.
4. Keep SBC, amortization, acquisition/integration work, debt service, and
   replacement acquisitions in the common-owner bridge even when adjusted EBITDA
   excludes them.
5. Compare debt paydown with acquisition cash and stock issuance. Buybacks or
   adjusted EPS are not evidence of surplus cash while leverage and dilution
   remain unresolved.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what organic provider retention,
patient-payment contribution margin, transaction volume, collection rate,
product investment, acquisition return, debt paydown, and cost of capital the
price requires. The Lyn Alden-style stress test asks whether provider and
patient liquidity, reimbursement policy, healthcare administrative complexity,
processing costs, rates, regulation, and credit access preserve the workflow's
cash conversion in a downturn.

## Promotion boundary

`healthcare-payment-workflow-qualified; mix-acquisition-and-debt-open; no-ranking`

Promotion requires same-entity, same-period joins from workflow volume and
revenue mix to third-party cost, collection, organic retention, product
reinvestment, Iodine/future acquisition return, debt, SBC, diluted shares, and
common-owner residual. Revenue, NRR, adjusted EBITDA, reported OCF, deferred
revenue, and buybacks remain diagnostic inputs.

## Sources

- [Waystar deep-company packet](../deep-company-pages/waystar-holding-corp.md)
- [Waystar company packet](../../extracted/technology/healthcare-information-services/waystar-holding-corp/company-packet.md)
- [Waystar source ledger](../../extracted/technology/healthcare-information-services/waystar-holding-corp/source-ledger.md)

