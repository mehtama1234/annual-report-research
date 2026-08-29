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

`Not fully. The public Q2 2026 release improves the Antamina bridge because Wheaton reports that Antamina produced 2.3M attributable silver ounces in Q2 2026, up 56% year over year, with the increase primarily driven by the newly acquired BHP Antamina PMPA that raised Wheaton's Antamina silver production share from 33.75% to 67.5% effective April 1, 2026. This upgrades the row from delivery-timing context to actual post-close production evidence. It still does not prove delivered ounces, invoices, settlement cash, realized price, tax allocation, interest allocation, lender waterfall, or IRR/NPV.`

## Production-To-Receipt Bridge

| Gate | Current Evidence | Status | Boundary |
|---|---:|---|---|
| PMPA close and effective date | BHP Antamina PMPA closed/effective April `1`, `2026`; upfront payment was `4.300B USD`. | `named-use-and-effective-date-visible` | Does not prove cash receipt from the stream. |
| First delivery timing | Q1 release said first deliveries under the BHP Antamina PMPA were anticipated at the end of May `2026`. | `delivery-timing-context-visible` | Anticipated delivery is not an actual receipt ledger. |
| Q2 production | Q2 release says Antamina produced `2.3M` attributable silver ounces in Q2 `2026`. | `post-close-production-visible` | Production is not delivered ounces, sold ounces, invoiced cash, or collected cash. |
| BHP PMPA effect | Q2 release says the increase was primarily driven by the newly acquired BHP Antamina PMPA increasing Wheaton's share from `33.75%` to `67.5%` effective April `1`, `2026`. | `pmpa-production-link-visible` | Does not separate BHP PMPA ounces from pre-existing Glencore stream ounces. |
| Stream economics | Local 6-K extraction shows H1 `2026` Antamina revenue `277.563M USD`, cost excluding depletion `55.340M USD`, depletion `51.322M USD`, profit `170.901M USD`, OCF proxy `222.223M USD`, and asset base `4.708329B USD`. | `stream-cash-proxy-visible` | Does not reconcile production to delivered/sold ounces, invoices, realized price, or cash collection. |
| Cash payment formula | BHP/Wheaton deal materials show ongoing payments equal to `20%` of spot/price received and fixed `90%` payable factor. | `cash-cost-formula-visible` | Formula is not applied to actual settlement rows. |
| Debt waterfall | Company debt, term loan, revolver, and Bank of Montreal administrative-agent context are visible. | `debt-channel-context-visible` | No Antamina-specific borrowing notices, repayment schedule, restricted account, or lender payback route. |
| Return model | Mechanical OCF/upfront-payment proxies exist. | `return-proxy-visible` | No full delivery curve, reserve-backed model, tax/interest allocation, IRR, or NPV. |

## What Improved

The important upgrade is narrow:

`first-delivery-timing-context -> post-close-production-visible`

The system can now say the post-close Antamina production contribution appeared in Q2 `2026` and was linked by Wheaton to the BHP PMPA share increase.

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

`Wheaton Antamina now has post-close production evidence: Wheaton reported 2.3M attributable silver ounces from Antamina in Q2 2026 and linked the increase primarily to the newly acquired BHP Antamina PMPA, which raised its Antamina silver production share from 33.75% to 67.5% effective April 1, 2026. This strengthens the named asset cash-return proxy, but it does not prove delivered ounces, sold ounces, invoices, settlement cash, realized price, tax allocation, interest allocation, lender waterfall, IRR, or NPV.`

## Next Source Package

1. Mine-by-mine delivered and sold ounces for Antamina after April `1`, `2026`.
2. BHP PMPA-only ounce separation from the legacy Glencore Antamina stream.
3. Invoice, settlement, or cash receipt support for Antamina silver deliveries.
4. Realized price and ongoing `20%` production payment reconciliation.
5. Term-loan and revolver debt-service allocation to the PMPA funding.
6. Antamina reserve report, mine plan, delivery curve, and PMPA valuation model.
