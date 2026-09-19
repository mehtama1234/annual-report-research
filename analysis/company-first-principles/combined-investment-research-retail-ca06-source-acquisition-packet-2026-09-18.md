# Retail CA-06 source-acquisition packet

Research date: `2026-09-18`

## Purpose

This packet converts the CA-06 denominator gaps into document-specific
requests. It does not treat another OCF screen, a period-end obligation, or an
annual burden total as a substitute for a same-period cash or claim schedule.

## Promotion test

A retail company can move beyond `allocation-sensitivity-only` only when a
source joins the legal entity, reporting period, cash or claim object, and
reconciliation path for the relevant burden. The minimum path is:

```text
reported OCF
  -> period-matched working-capital / supplier-finance settlement
  -> maintenance-versus-growth capital
  -> lease and tax cash where applicable
  -> attached-service collection and allocated cost
  -> debt, NCI, SBC, dilution, and common-owner residual
```

No single missing field is silently filled by an annual proxy or a balance-sheet
ending balance.

## Acquisition queue

| Company / period | Document or source object | Required fields | Promotion test |
|---|---|---|---|
| TJX H1 FY2027 / next filing | Supplier-finance note or payment-date roll-forward | confirmed invoices, paid invoices, payment dates, accounts payable, cash-flow classification, vendor-finance settlement | Match the H1 payable movement to actual settlement without deducting it again from OCF |
| TJX H1 FY2027 / next filing | Property-project or capital-spending schedule | store openings, remodels, distribution, technology, maintenance/replacement, project dates and dollars | Separate recurring replacement capital from growth/expansion before owner-cash promotion |
| TJX H1 FY2027 / next filing | Lease/tax and attached-service schedule | cash-paid leases, cash taxes, digital/credit/service collection, labor/technology/fulfillment cost, entity owner | Join the same period and legal entity; do not import annual cash into H1 |
| Target H1 2026 / next filing | Supplier-finance settlement or invoice roll-forward | `$3.2B` eligible obligation lifecycle, invoice dates, Target remittance dates, early-payment activity, AP movement, cash classification | Demonstrate whether any H1 cash effect is already inside OCF and avoid treating the balance as an early payment |
| Target H1 2026 / next filing | Property and equipment project schedule | stores, remodels, supply chain, technology, maintenance/replacement, growth, project-level cash dates | Allocate the `$2.404B` property line into maintenance and growth; do not use the total as either by default |
| Target H1 2026 / next filing | Operating-lease and tax payment schedule | cash paid by period, lease principal/interest classification, cash taxes, entity and payment dates; keep the `$3.733B` ROIC lease-liability denominator and `$1.402B` trailing tax input as noncash/period controls | Match burden to H1 and preserve payments already embedded in OCF; do not substitute ROIC inputs for cash |
| Target H1 2026 / next filing | Attached-service collection/cost schedule | advertising, card profit sharing, marketplace, Circle 360, Shipt, rental; labor, fulfillment, technology, capex, tax and senior claims | Convert reported service revenue into attributable residual cash only after allocated cost and legal-entity ownership are shown |
| Walmart H1 FY2027 / next filing | Supplier-finance payment allocation | `$6.4B` obligation, confirmed/paid invoices, settlement dates, AP movement, cash classification | Join H1 settlement to OCF; do not subtract the obligation or AP movement twice |
| Walmart H1 FY2027 / next filing | Project-level capex / maintenance schedule | `$14.181B` property payments, `$1.087B` new stores, remodels, supply chain, technology, international, replacement | Retain the `$1.087B` new-store amount as a growth floor and allocate the mixed remainder before promotion |
| Walmart H1 FY2027 / next filing | Lease/tax and ecosystem-service schedule | cash-paid leases, taxes, advertising, membership, marketplace, fulfillment, labor, technology, entity allocation | Join recurring burden and service collection to the same period and owner perimeter |

## Current public boundary

The latest checked filings establish the following but do not satisfy the
promotion test:

- Target H1 2026: `$4.519B` OCF, `$2.404B` property spending, `$3.2B`
  eligible supplier-finance obligations, and `$994M` of tariff refunds;
- Walmart H1 FY2027: `$19.710B` OCF, `$14.181B` property payments, `$6.4B`
  eligible supplier-finance obligations, and a `$1.087B` new-store category;
- TJX H1 FY2027: `$3.345B` OCF, `$1.159B` property additions, `$1.147B` of
  operating-lease cash paid, and a `$2.2B–$2.3B` annual capex guide with
  `$222M` of explicit new-store spending; H1 maintenance, supplier-finance,
  tax, and service-cost allocation remain unproven.

The TJX Q2 filing also exposes the H1 common-owner and liquidity perimeter:
`$1.402B` of share repurchases, `$1.000B` of dividends, a planned `$1.000B`
September 2026 note repayment from operating cash, and `$1.5B` of available
credit facilities at August 1. These are cash uses, senior claims, and
liquidity controls—not normalized owner cash—and the actual note repayment or
facility draw remains unobserved.

The September 18 recheck of TJX's official Q2 FY2027 release and call route
adds 23 net Q2 store additions and confirms the 4% FY2028 store-opening plan,
but does not add the missing settlement bank-receipt/legal-payment schedule or
same-period maintenance-versus-growth capex allocation. This is a searched-
negative source refresh for the two promotion objects, not evidence that the
cash or allocation does not exist in controlled workpapers.

Walmart's Q2 FY2027 presentation attributes a `$2.8B` year-over-year increase
in capital expenditures to its omnichannel growth strategy. The Q2 release
also reports growth in advertising, marketplace, store-fulfilled delivery and
membership, and explains that advertising may be recorded in net sales or as a
reduction of cost of sales depending on the arrangement. These are current
growth and accounting-presentation controls, not maintenance, lease/tax,
supplier-finance, or ecosystem-cost allocations.

These are reported or bounded inputs, not normalized common-owner cash. The
current status remains:

`CA-06-partial; Q-04-through-Q-06-qualified; no cross-company ranking`

Target's current public strategy adds a growth-driver boundary: approximately
`$5B` of 2026 investment includes more than `130` remodels and more than `30`
new stores, while the Q2 release says the `$1.4B` quarterly capex amount was
driven primarily by remodels and new stores. This strengthens the conclusion
that the `$2.404B` H1 property line is mixed and not pure maintenance, but it
does not quantify maintenance/replacement spending or permit the annual plan
to be subtracted from H1 OCF. See the [Target capex growth-driver boundary](combined-investment-research-target-q2-2026-capex-growth-driver-boundary-2026-09-18.md).
Target's Q2 operating update further reports `17` new stores in Q2 and `24`
year-to-date. This supplies a period-matched unit-count control for the growth
component, but not a dollar allocation to those stores; it therefore remains a
classification input rather than a maintenance/growth cash split.
The official Q2 call adds that approximately `$2.4B` had been deployed through
H1, up nearly `30%`, across new stores, full-store remodels, supply chain, and
technology. It also attributes higher SG&A to additional field-team hours,
training, incentive compensation, and planned capital-project spending. The
call does not allocate maintenance/replacement dollars or identify the
collection, labor, fulfillment, technology, tax, lease, and remittance burden
of Target's attached services. These are same-period burden and classification
controls, not additional cash to add to OCF or a basis for a normalized owner-
cash deduction.
The Q2 call adds that approximately `$2.4B` was deployed through H1, up nearly
`30%`, as intentional incremental investment in new stores, remodels, supply
chain and technology. It also reports growth in Roundel, Target Plus and
Target Circle 360, but provides no allocated service-cost or cash schedule;
the transcript has no maintenance, lease, or Shipt payment line. This is a
management-call boundary, not a normalized-owner-cash promotion.

The [known-growth-floor frontier](combined-investment-research-retail-known-growth-floor-frontier-2026-09-18.md)
now puts the same-period capex denominator on one controlled surface. TJX's
`$3.345B` H1 OCF less `$1.159B` property additions is `$2.186B`, with a
disclosed `$222M` new-store floor and `$937M` still unallocated. Target's
corresponding screen is `$2.115B` after `$2.404B` property spending, with no
quantified H1 growth floor. Walmart's screen is `$5.529B` after `$14.181B` of
property payments, with a `$1.087B` new-store/expansion/relocation floor and
`$13.094B` mixed remainder. The frontier improves comparability and
falsifiability; it does not call the remainder maintenance, create owner cash,
or close Q-05.

The [H1 attached-services frontier](combined-investment-research-retail-h1-attached-services-frontier-2026-09-18.md)
now aligns Target's `$1.141B` H1 service pool and Walmart's `$3.904B`
consolidated / `$3.855B` segment service-income surfaces with the current
cash screens. The 0–100% columns are hypothetical conversion sensitivities;
they do not create cash, and the pools are already embedded in consolidated
operating results. TD card ownership, Walmart's `$49M` presentation difference,
service costs, capital, tax, and remittance remain explicit.
Walmart's official Q2 call adds same-period normalization context: tariff
refunds were reinvested in price, higher depreciation followed capital
expenditure, self-insurance costs increased, and management expects more than
`$2B` of incremental fuel-related costs for FY2027 plus Vibe integration cost.
These burdens help define the durability test but are not allocated to the H1
membership, advertising, marketplace, or fulfillment pools and must not be
subtracted again from reported OCF without a matched cash schedule.

The [supplier-finance settlement frontier](combined-investment-research-retail-supplier-finance-settlement-frontier-2026-09-18.md)
now places the current Q-04 evidence on the same control surface. Target's
`$3.2B` eligible obligation versus `$3.0B` opening balance and Walmart's
`$6.4B` versus `$6.0B` are period-end obligation changes, not observed cash
settlements. The associated `$612M` and `$1.257B` accounts-payable cash sources
remain inside reported OCF, and no second subtraction is permitted without an
invoice-level waterfall. TJX's missing comparable note remains a source gap,
not a searched-negative.

The [official-HTML lease/tax recheck](combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md#september-18-2026-official-html-recheck)
confirms that Target and Walmart still lack matched H1 cash-paid lease and tax
lines. TJX exposes lease-liability and tax working-capital movements, but those
are not cash-tax evidence. This narrows the searched-negative boundary without
changing CA-06's partial status.

## Source routes and stop rules

### September 18, 2026 targeted public-source refresh

The official Walmart FY2026 annual filing confirms the accounting boundary:
normal repairs and maintenance are expensed as incurred, while major
improvements are capitalized; its capital-allocation table separately reports
supply chain/customer-facing/technology/other, remodels, new stores/clubs,
and international spending. This improves classification but does not
allocate H1 FY2027 maintenance dollars or service-level cash.

Target's official 2025 annual report and 2026 growth-plan materials likewise
describe 2026 capital spending as a mix of store experience/remodels, supply
chain, technology, and new stores, with more than 130 remodels and more than
30 new stores planned. They provide growth and classification controls, not a
period-matched maintenance schedule or attached-service cost/collection
allocation. No checked official source supplied the missing H1 lease/tax cash,
maintenance-dollar split, service-cost allocation, or common-owner residual.

Result: `searched-negative-for-new-promotion-grade-ca06-object`; this is not
evidence that the payments or workpapers do not exist.

The direct interim filing check sharpens the field boundary. Target reports
H1 tax provision and operating-lease liabilities, Walmart reports H1 tax
provision, accrued-income-tax movement, and operating-lease obligations, and
TJX reports H1 changes in income-tax and net-operating-lease liabilities. Those
are accounting and balance-sheet movements, not cash-paid lease or cash-tax
lines. They cannot be promoted into the H1 owner-cash denominator without a
payment schedule or equivalent cash-flow note.

Primary routes are the next quarterly or annual SEC filings, exhibits,
company-provided project schedules, and authorized payment-date or service
allocation schedules. Stop if a source only repeats OCF, a period-end supplier-
finance balance, annual lease/tax cash, store counts, service revenue, or
management's capital-allocation policy without settlement dates and allocated
costs.

## Sources

- [Retail H1 owner-cash denominator handoff](combined-investment-research-retail-h1-owner-cash-denominator-handoff-2026-09-17.md).
- [Retail CA-06 allocation boundary](combined-investment-research-retail-ca06-allocation-boundary-2026-09-17.md).
- [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm).
- [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm).
- [TJX FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm).
- [Target Q2 2026 operating update](https://corporate.target.com/news-features/article/2026/08/q2-2026-earnings).
- [Target Q2 2026 earnings-call transcript](https://corporate.target.com/getmedia/d01cb805-63cb-4150-bae4-8d717f0d9ed3/Q2-2026-Target-Corp-Earnings-Call.pdf).
- [Walmart Q2 FY2027 earnings-call transcript](https://corporate.walmart.com/content/dam/corporate/documents/newsroom/2026/08/20/walmart-releases-q2-fy27-earnings/q2-fy27-earnings-call-transcript.pdf).
- [Walmart FY2026 Form 10-K capital-allocation and repair-accounting sections](https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000055/wmt-20260131.htm/z14q%22s).
- [Target 2025 Form 10-K capital-expenditure plan](https://corporate.target.com/investors/annual/2025-annual-report/10-k-report/10-k-part-ii/item-7-management-s-discussion-and-analysis-of-financial-condition-and-results-of-operations).
