# Capital Flow Wheaton Antamina Production Receipt Bridge Pass 1

## Purpose

This pass executes the next Wheaton pull from the top-three named cash source acquisition packet:

`Wheaton delivered-ounce schedule and Antamina PMPA receipt support.`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-wheaton-antamina-production-receipt-bridge-pass-1.csv`

The upstream packet is:

`/cluster/capital-flow-top-three-named-cash-source-acquisition-packet-pass-1.md`

## Question

`Can Wheaton Antamina move from named PMPA use and stream economics to delivered-ounce receipt proof?`

## Short Answer

`Not fully. The public Q2 2026 filing improves the Antamina bridge because Wheaton's operating table reports 2.319M combined attributable silver ounces produced and 2.063M sold in Q2 2026; its GEO bridge separately identifies an 837,000 silver-ounce-equivalent production increase, primarily driven by the newly acquired BHP Antamina PMPA that raised Wheaton's Antamina share from 33.75% to 67.5% effective April 1, 2026. This upgrades the row from delivery-timing context to actual post-close production and sales evidence. It still does not prove BHP-only delivered ounces, invoices, settlement cash, realized price, tax allocation, interest allocation, lender waterfall, or IRR/NPV.`

## Production-To-Receipt Bridge

| Gate | Current Evidence | Status | Boundary |
|---|---:|---|---|
| PMPA close and effective date | BHP Antamina PMPA closed/effective April `1`, `2026`; upfront payment was `4.300B USD`. | `named-use-and-effective-date-visible` | Does not prove cash receipt from the stream. |
| First delivery timing | Q1 release said first deliveries under the BHP Antamina PMPA were anticipated at the end of May `2026`. | `delivery-timing-context-visible` | Anticipated delivery is not an actual receipt ledger. |
| Q2 production and sales | Q2 filing reports `2.319M` combined attributable silver ounces produced and `2.063M` sold; the GEO bridge reports an `837,000` silver-ounce-equivalent production increase. | `post-close-production-visible` | Production and sales are not BHP-only delivered ounces, invoiced cash, or collected cash. |
| BHP PMPA effect | Q2 release says the increase was primarily driven by the newly acquired BHP Antamina PMPA increasing Wheaton's share from `33.75%` to `67.5%` effective April `1`, `2026`. | `pmpa-production-link-visible` | Does not separate BHP PMPA ounces from pre-existing Glencore stream ounces. |
| Stream economics | Local Q2 2026 6-K extraction shows Q2 Antamina revenue `150.549M USD`, cost excluding depletion `28.510M USD`, depletion `44.716M USD`, profit `77.323M USD`, OCF proxy `122.039M USD`, and asset base `4.708329B USD`; the same filing shows H1 revenue `277.563M USD`, profit `170.901M USD`, and OCF proxy `222.223M USD`. | `stream-cash-proxy-visible` | These are combined Antamina stream-segment amounts, not BHP-only settlement cash; they do not reconcile production to delivered/sold ounces, invoices, realized price, or collection. |
| Revenue-recognition bridge | Wheaton's Q2 accounting policy says precious-metal credit revenue is recognized when the credits are sold and control transfers to the customer; concentrate sales use provisional assays/prices and final settlement based on recovered ounces, smelter weights, assays, and the quotation period. | `sale-recognition-mechanism-visible` | The policy identifies the accounting event and settlement inputs but does not identify which portion of Q2 Antamina revenue came from BHP credits, the BHP invoice, or cash collection. |
| Cash payment formula | BHP/Wheaton deal materials show ongoing payments equal to `20%` of spot/price received and fixed `90%` payable factor. | `cash-cost-formula-visible` | Formula is not applied to actual settlement rows. |
| Debt waterfall | Company debt, term loan, revolver, and Bank of Montreal administrative-agent context are visible. | `debt-channel-context-visible` | No Antamina-specific borrowing notices, repayment schedule, restricted account, or lender payback route. |
| Return model | Mechanical OCF/upfront-payment proxies exist. | `return-proxy-visible` | No full delivery curve, reserve-backed model, tax/interest allocation, IRR, or NPV. |

## What Improved

The important upgrade is narrow:

`first-delivery-timing-context -> post-close-production-visible`

The system can now say the post-close Antamina production contribution appeared in Q2 `2026` and was linked by Wheaton to the BHP PMPA share increase. It can also anchor the combined stream's Q2 accounting and operating-cash proxy to the same post-close reporting period, without promoting those amounts to BHP-only receipts.

## What Still Blocks Delivered-Cash Proof

Full delivered-cash proof still requires:

1. delivered-ounce schedule for the BHP Antamina PMPA
2. separation of BHP PMPA ounces from the existing Glencore Antamina stream
3. sold-ounce schedule and realized price
4. invoice or settlement support
5. cash collection and ongoing `20%` payment reconciliation
6. Antamina-specific tax and interest allocation
7. debt-service waterfall and lender payback support
8. reserve-backed delivery curve and IRR/NPV

## Decision

`wheaton-antamina-post-close-production-visible-receipt-proof-hold`

Wheaton Antamina improves again, but the row remains below named cash receipt proof. Production is a stronger output bridge than timing language, not a cash receipt ledger.

## Safe Claim

`Wheaton Antamina now has post-close production and sales evidence: Wheaton's Q2 operating table reports 2.319M combined attributable silver ounces produced and 2.063M sold, while the GEO bridge reports an 837,000 silver-ounce-equivalent production increase primarily driven by the newly acquired BHP Antamina PMPA, which raised its Antamina share from 33.75% to 67.5% effective April 1, 2026. This strengthens the named asset cash-return proxy, but it does not prove BHP-only delivered ounces, invoices, settlement cash, realized price, tax allocation, interest allocation, lender waterfall, IRR, or NPV.`

The Q2 filing also reports `150.549M USD` of Antamina stream revenue, `77.323M USD` of profit, and `122.039M USD` of operating cash flow for the quarter, with `4.708329B USD` of Antamina stream assets at June 30, 2026. Wheaton's accounting policy says precious-metal credit revenue is recognized when credits are sold and control transfers to the customer, while concentrate final settlement uses recovered ounces, smelter weights, assays, and the quotation period. These facts improve the event-chain definition, but the reported Antamina amounts remain combined-stream accounting and do not identify BHP-only metal credits, invoice, or cash collection.

## September 18, 2026 official Q2-release recheck

The official [Q2 results release](https://www.wheatonpm.com/news/news-details/2026/Wheaton-Precious-Metals-Announces-Second-Quarter-2026-Results-and-Record-Year-to-Date-Production-Revenue-Earnings-and-Cash-Flow/default.aspx) adds a useful same-period control without
closing the BHP allocation gap. It states that the April 1 `$1.500B` Term
Loan was drawn and that the Term Loan, a revolver draw, and cash on hand were
used to fund the BHP Antamina PMPA. At June 30, Wheaton reported approximately
`$100M` of cash and `$2.0B` outstanding under the Term Loan and Revolving
Credit Facility. It also breaks the Q2 net upfront mineral-stream payments
into `$4.5B` total, including `$4.3B` for BHP Antamina and smaller payments for
Koné, Spanish Mountain, Jervois, and Cipango.

The same release reports `2.3M` attributable silver ounces from Antamina in
Q2 and attributes the increase to the BHP PMPA, which raised Wheaton's share
from `33.75%` to `67.5%` effective April 1. These are stronger contemporaneous
source/use and output controls, but they remain corporate funding and
combined-stream observations. The release still does not provide a BHP-only
metal-credit issuance, invoice, sale/receivable, bank collection, or
facility-specific repayment/allocation record. The promotion boundary remains
`post-close combined production visible; BHP-specific receipt and financed
return unproven`.

## Next Source Package

1. Mine-by-mine delivered and sold ounces for Antamina after April `1`, `2026`.
2. BHP PMPA-only ounce separation from the legacy Glencore Antamina stream.
3. Invoice, settlement, or cash receipt support for Antamina silver deliveries.
4. Realized price and ongoing `20%` production payment reconciliation.
5. Term-loan and revolver debt-service allocation to the PMPA funding.
6. Antamina reserve report, mine plan, delivery curve, and PMPA valuation model.
