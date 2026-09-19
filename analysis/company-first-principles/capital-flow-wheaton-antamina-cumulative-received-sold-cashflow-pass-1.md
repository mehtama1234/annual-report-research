# Capital Flow Wheaton Antamina Cumulative Received/Sold Cashflow Pass 1

## Purpose

This pass checks whether Wheaton Antamina can move beyond production-only evidence into cumulative received/sold unit and cash-flow evidence.

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-wheaton-antamina-cumulative-received-sold-cashflow-pass-1.csv`

The upstream production receipt bridge is:

`/cluster/capital-flow-wheaton-antamina-production-receipt-bridge-pass-1.md`

## Question

`Can Wheaton Antamina move closer to named cash proof using the Q2 2026 MD&A mineral-stream table?`

## Short Answer

`Yes, but only at combined-stream proxy level. The Q2 2026 MD&A mineral-stream table reports a named Antamina Glencore/BHP silver row with 67.50% attributable production, 20% production payment, 5.200000B USD of total upfront consideration paid to June 30 2026, 1.171862B USD of cash flow generated to date, 56.718M silver ounces received and sold to date, and 1.412M Q2 2026 PBND. This upgrades Antamina from production-only evidence to combined-stream cumulative received/sold and cash-flow evidence. It still does not isolate BHP PMPA-only delivered ounces, invoices, settlement cash, realized price, tax, interest, lender waterfall, IRR, NPV, or full return.`

## Cumulative Bridge

| Gate | Current Evidence | Status | Boundary |
|---|---:|---|---|
| Named row | MD&A table has `Antamina Glencore/BHP PER 67.50%`. | `combined-stream-row-visible` | Combined row does not isolate BHP PMPA. |
| Upfront denominator | Antamina combined upfront paid to June 30 2026 is `5.200000B USD`. | `combined-upfront-denominator-visible` | Blends legacy Glencore stream and BHP PMPA. |
| Cash flow generated | Antamina combined cash flow generated to date is `1.171862B USD`. | `combined-cash-flow-generated-visible` | Cumulative cash flow is not invoice cash by period. |
| Units received and sold | Antamina combined units received and sold to date are `56.718M` silver ounces. | `combined-received-sold-units-visible` | Does not prove BHP-only deliveries or settlement cash. |
| PBND | Antamina Q2 2026 payable ounces produced but not delivered are `1.412M` silver ounces. | `combined-pbnd-visible` | PBND is a delivery timing gap, not cash. |
| Q2 production and sales | Q2 release reports `2.319M` combined attributable silver ounces produced and `2.063M` sold. | `post-close-production-visible` | Production and sales are not BHP-only settled or collected cash. |
| H1 stream economics | Financial statements show `277.563M USD` revenue and `222.223M USD` OCF proxy. | `stream-economics-visible` | Does not reconcile to invoices or realized price. |
| Cumulative cash-yield proxy | `1.171862B / 5.200000B = 22.536%`. | `derived-combined-cash-yield-proxy` | Not IRR, NPV, after-tax return, or BHP-only return. |
| Unit cash proxy | `1.171862B / 56.718M oz = 20.66 USD/oz`. | `derived-combined-unit-cash-proxy` | Not realized price or delivery settlement detail. |
| Full proof verdict | Strongest proxy improves, but full proof still holds. | `combined-stream-cashflow-visible-bhp-receipt-proof-hold` | BHP-only cash-all-the-way-through remains missing. |

## What Improved

The proof grade moves from:

`post-close-production-visible`

to:

`combined-stream cumulative received/sold and cash-flow generated visible`

That matters because the table reports not only production, but cumulative units received and sold plus cash flow generated for the named Antamina stream.

## What Still Blocks Full Named Cash Proof

The decisive missing source is now narrower:

1. BHP PMPA-only delivered ounces after April 1 2026
2. separation from legacy Glencore Antamina deliveries
3. invoice or settlement cash by delivery
4. realized silver price and 20% production-payment reconciliation
5. cash receipt timing and PBND rollforward
6. debt-service allocation to the BHP PMPA funding
7. Antamina-specific tax and interest allocation
8. reserve-backed delivery curve and IRR/NPV

## Decision

`wheaton-antamina-combined-stream-cashflow-visible-bhp-receipt-proof-hold`

Antamina remains the strongest named asset cash-return proxy in the system. The current upgrade is real but bounded: combined-stream received/sold units and cash flow are visible, while BHP-only delivered-cash proof remains missing.

## Safe Claim

`Wheaton Antamina now has combined-stream cumulative received/sold and cash-flow evidence. The Q2 2026 MD&A mineral-stream table shows Antamina Glencore/BHP at 67.50% attributable production, 5.200000B USD upfront consideration paid to June 30 2026, 1.171862B USD cash flow generated to date, 56.718M silver ounces received and sold to date, and 1.412M Q2 2026 PBND. This strengthens the named cash-return proxy, but it does not prove BHP PMPA-only delivered ounces, invoices, settlement cash, realized price, tax allocation, interest allocation, lender waterfall, IRR, NPV, or full PMPA return.`

## Next Source Package

1. BHP PMPA-only delivery and sales schedule.
2. Legacy Glencore versus BHP Antamina split.
3. Invoice, settlement, and cash receipt records.
4. PBND rollforward from production to delivery to sale.
5. Realized price and production-payment reconciliation.
6. Antamina-specific tax, interest, debt-service, and return model support.
