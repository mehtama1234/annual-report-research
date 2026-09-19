# AI systems distribution and financing valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Dell Technologies from AI-demand evidence into a
company-specific valuation and liquidity perimeter. It keeps customer-facing
system integration, servers, storage, networking, services, financing
receivables, operating leases, supplier terms, inventory, warranty, debt, and
diluted common-owner cash separate from NVIDIA's architecture/software control
point and from generic cloud economics.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Dell AI systems distribution and financing | Collected systems, services, and support cash after component procurement, AI-server margin, inventory, financing receivables, operating leases, customer credit, warranty, debt funding, SBC, and dilution | Memory/GPU/component purchases, inventory, deployment/support labor, customer financing originations, operating-lease assets, receivables, capex, debt funding, acquisitions, SBC replacement, and repurchases | AI-capex pause, customer concentration, lower server margins, memory shortages, receivable charge-offs, residual-value losses, higher funding costs, backlog cancellation, or supplier/liquidity stress | AI orders and backlog rise while shipments, margin, collections, financing-receivable quality, services, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2026 revenue was `$113.5B`, operating cash flow `$11.185B`, reported free
  cash flow `$8.555B`, and adjusted free cash flow `$11.508B`.
- Financing receivables were `$14.280B` and equipment under operating leases
  `$2.459B` at FY2026 year-end. The adjusted cash measure adds back the cash
  impact of these financing-related assets; that is a financing-risk question,
  not automatically free cash.
- Q2 FY2027 AI orders were `$60.9B`, AI-server revenue `$16.4B`, and ending AI
  backlog `$95B`; quarterly operating cash flow was `$2.225B` while adjusted
  free cash flow was `$8.149B`, including a `$6.667B` financing-receivable
  adjustment.
- FY2026 Infrastructure Solutions Group operating margin was `11.7%`, down
  `110` basis points as AI-optimized-server mix increased. A larger backlog can
  therefore increase capital and credit exposure without proportionate margin.
- One customer represented `12%` of FY2026 consolidated revenue. Financing
  originations were `$11.9B`, and reported principal charge-offs were `0.2%`;
  those figures require stress against weaker customers, higher rates, and
  slower equipment resale.

## QoE and financial-shenanigans prompts

1. Reconcile AI orders and backlog to shipment, acceptance, revenue, gross and
   operating margin, inventory, receivables, supplier commitments, and cash
   collection. Backlog is visibility, not profit or owner cash.
2. Keep reported OCF and adjusted FCF side by side. Test whether adjusted FCF
   grows because operations improved or because financing receivables and
   operating-lease assets were excluded from the cash burden.
3. Underwrite Dell Financial Services as a credit portfolio: originations,
   customer concentration, charge-offs, residual values, funding cost, debt
   maturities, and cash recovery after default.
4. Track AI-server margin after scarce-memory/component cost, expedited
   logistics, warranty, deployment, support, and customer concessions. Revenue
   mix can grow while economic margin declines.
5. Reconcile inventory, supplier terms, financing receivables, operating leases,
   SBC, repurchases, dividends, and diluted shares before treating the hardware
   cycle as durable common-owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what AI-server volume, margin,
services attachment, financing spread, receivable loss rate, reinvestment rate,
and cost of capital the valuation requires after separating operating cash from
customer-financing cash. A durable systems relationship must earn enough margin
to pay for working capital, credit, support, and replacement capital.

The Lyn Alden-style stress test asks whether customers can finance AI deployment
through higher rates, weaker model economics, memory shortages, trade limits,
lower equipment residuals, or a data-center spending pause. Liquidity passes only
when financing receivables, debt, inventory, supplier claims, leases, and
diluted common residual remain visible at the legal entity.

## Promotion boundary

`ai-systems-distribution-qualified; financing-receivable-and-margin-open; no-ranking`

Promotion requires same-entity, same-period joins from AI orders and backlog to
shipment acceptance, margin, customer collection, inventory and supplier
settlement, financing-receivable performance, operating-lease cash, services
renewal, debt funding, SBC replacement, and diluted common residual. Orders,
backlog, adjusted FCF, OCF, revenue, and repurchases remain diagnostic inputs.

## Sources

- [Dell company packet](../deep-company-pages/dell-technologies-inc.md)
- [Dell FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1571996/000157199626000008/dell-20260130.htm)
- [Dell FY2027 Q2 results](https://investors.dell.com/news-releases/news-release-details/dell-technologies-delivers-second-quarter-fiscal-2027-financial)
- [Next-execution handoff](combined-investment-research-next-execution-handoff-2026-09-17.md)

