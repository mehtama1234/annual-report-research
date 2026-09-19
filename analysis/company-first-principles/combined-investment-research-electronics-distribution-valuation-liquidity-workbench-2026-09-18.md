# Electronics distribution valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Avnet into a company-specific electronics-distribution
and component-availability valuation/liquidity object. It keeps semiconductor
distribution separate from industrial procurement, semiconductor manufacturing,
electronic test, and networking control. The object tests sales and gross
spread after inventory, receivables, supplier terms, obsolescence, price
erosion, warehouses, design support, technology, debt, taxes, and diluted
common claims.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Avnet | Component-availability and design-support cash after inventory velocity, customer collection, supplier settlement, warehouse/freight/service labor, obsolescence, capex, debt, taxes, and diluted common residual | Electronic Components versus Farnell mix, inventory days, receivables, payables, supplier return rights, reserves, design/programming/testing, warehouses, technology, debt, and SBC | Semiconductor/industrial cycle, inventory aging/price erosion, supplier allocation or terms, customer credit, regional/trade/FX, debt/refinancing, and thin-margin compression | Sales, gross margin, adjusted EPS, inventory days, or OCF rise while growth funding, reserves, supplier protection, collection, debt, or per-share residual deteriorate |

## Current evidence anchors

- FY2025 sales were `$22.2008B`, gross margin `10.7%`, operating margin `2.3%`,
  and diluted EPS `$2.75`; the weak cycle makes working-capital and financing
  burden visible despite the large revenue base.
- Q2 FY2026 sales were `$6.319B`, up `11.6%`, with OCF `$208M`; inventory fell
  `$126M` to about `$5.2945B` and receivables were about `$5.2428B`.
- Q3 FY2026 sales were `$7.1198B`, up `34%`; about `$800M` of sales growth used
  `$54M` of operating cash. Inventory days were `77`, then fell to `71` in Q4;
  FY2026 inventory days were `81`, down 18 days year over year.
- Electronic Components represented about `93.5%` of FY2025 sales and Farnell
  about `6.5%`; they have different inventory turns, customer mix, and service
  economics and should not be valued as one identical channel.
- Franchised supplier agreements provide inventory-return or obsolescence/price
  protection in some circumstances, but eligibility, timing, product coverage,
  and historical utilization require verification.

## QoE and financial-shenanigans prompts

1. Separate product volume, price/mix, supplier rebates, freight, regional mix,
   and gross-margin recovery from inventory-cycle effects.
2. Reconcile sales growth to inventory, receivables, payables, supplier terms,
   and operating cash; do not treat inventory decline as permanent cash if it
   reflects understocking or destocking.
3. Test supplier return rights, aging, reserves, write-downs, price erosion,
   allocation, and concentration against actual recoveries.
4. Measure Farnell and design/programming/testing attachment after technical
   labor, systems, warehouse, and service cost.
5. Keep adjusted EPS, buybacks, debt, SBC, and revenue targets separate from
   normalized common-owner cash in a thin-margin financing model.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what cycle-normalized sales, gross
margin, inventory days, receivable collection, vendor terms, service attachment,
debt cost, and cost of capital the price requires. The Lyn Alden-style stress
test asks whether industrial production, automotive, defense, communications,
data-center demand, supplier allocation, rates, trade, FX, and customer credit
preserve liquidity through an inventory correction.

## Promotion boundary

`electronics-distribution-qualified; inventory-velocity-and-supplier-protection-open; no-ranking`

Promotion requires same-entity, same-period joins from component demand and
sales to inventory aging, supplier settlement/return rights, receivable
collection, service cost, capex, debt, taxes, diluted shares, and common-owner
residual. Sales, gross margin, adjusted EPS, inventory days, OCF, FCF,
dividends, and buybacks remain diagnostic inputs.

## Sources

- [Avnet deep-company packet](../deep-company-pages/avnet-inc.md)
- [Avnet company packet](../../extracted/technology/electronics-wholesale/avnet-inc/company-packet.md)

