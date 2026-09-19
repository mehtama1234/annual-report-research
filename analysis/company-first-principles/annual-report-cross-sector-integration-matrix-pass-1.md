# Annual Report Cross-Sector Integration Matrix Pass 1

Research date: `2026-09-17`

## Purpose

The eight undercovered-theme essays now provide article-grade breadth. This
matrix is the integration layer: it forces every theme to answer the same
end-to-end questions while preserving the denominator and evidence standard
that belongs to that business.

The matrix does not rank sectors or turn an annual-report observation into an
investment recommendation. It connects:

```text
force -> control point -> payer/funder -> burden carrier -> operating denominator
     -> QoE / financial-shenanigans control -> owner cash -> valuation object
     -> macro/liquidity route -> proof-grade breaker
```

The structured companion is [the integration CSV](data/annual-report-cross-sector-integration-matrix-pass-1.csv).

The matrix is checked by `python3 scripts/verify-annual-report-cross-sector-integration.py`.

## The integrated surface

| Theme | Force / human pressure | Control point | Payer or funder | Burden carrier | Operating denominator | QoE / financial-shenanigans control | Owner-cash and valuation object | Macro / liquidity route | Current proof grade and decisive breaker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Services and cultural consumption | Time scarcity, relief, status, travel, attention, escape | Repeatable capture of time, place, habit, and convenience | Households, employers, advertisers, travelers | Labor, leases, food/input costs, franchisees, integration | Same-unit demand, labor hours, occupancy/traffic, maintenance and lease burden | Price versus volume, promotions, franchise economics, capitalized pre-opening or “one-time” costs | Common-owner cash after maintenance, leases, taxes, and dilution; normalized service cash multiple | Employment, real wages, credit, travel and discretionary liquidity | `Article-ready / cash open`; break with multi-period traffic and collections weakness after normalized labor and occupancy cost |
| Consumer goods and household identity | Need for normalcy, cleanliness, safety, identity, and small control under pressure | Brand trust, shelf availability, assortment, and repeat routine | Households, retailers, distributors, supplier credit | Input costs, inventory, trade spend, private label, advertising | Units, price/mix, repeat purchase, inventory turns, gross-to-net and working capital | Price/mix masking volume decline, channel stuffing, inventory build, promotional capitalization, acquisition mix | Diluted cash after sustaining brand investment, inventory funding, taxes, and buyback/SBC effects; normalized brand cash | Inflation, real income, household credit, retailer inventory cycles | `Article-ready / cash open`; break with volume/market-share loss, inventory unwind, or gross-margin reversal not explained by mix |
| Basic materials and input scarcity | Buildout demand and physical bottlenecks | Low-cost reserve, processing asset, logistics, or scarce capacity | Industrial buyers, builders, farmers, distributors | Energy, sustaining capex, geology, permitting, transport, environmental obligations | Realized price net of freight, cost curve, sustaining volume, reserve life, working capital | Spot-price peak mistaken for durable economics, reserve/cost revisions, capitalized stripping or project costs, working-capital reversal | Through-cycle cash after sustaining capex, reclamation, taxes, debt, and dilution; reserve/project NPV | Manufacturing cycle, construction, food costs, rates, inventory and commodity liquidity | `Article-ready / through-cycle open`; break with cost-curve migration, reserve deterioration, or cash failing after sustaining spend |
| Real estate and scarce locations | Shelter, care, delivery, connectivity, travel, and site scarcity | Irreplaceable site, zoning, power, tower, lease, or logistics node | Tenants, guests, operators, partners, debt and equity capital | Property capex, power, taxes, insurance, vacancy, debt and partners | Occupancy/lease-up, rent spread, same-property NOI, recurring capex, debt service | AFFO/FFO perimeter, straight-line rent, development capitalization, JV/VIE and partner claims, dilution | Property/project cash after recurring capex, debt, partner/preferred claims, taxes, and dilution; project NPV/IRR | Rates, credit spreads, refinancing, construction finance, power availability | `Article-ready / project cash open`; break with lease-up delay, rent loss, capex escalation, or funding dilution overwhelming project return |
| Broad technology control points | Digital dependence, identity, security, compute, storage, and workflow complexity | Permissioning, network enforcement, process control, installed software/hardware | Enterprises, governments, developers, network and semiconductor customers | R&D, support, compute/power, channel, cybersecurity, SBC and obsolescence | Retention, utilization, service attach, backlog conversion, gross margin, R&D and capex intensity | ARR/RPO/bookings versus recognized cash, deferred revenue, factoring, capitalization, SBC, acquisition and restructuring normalization | Diluted owner cash after R&D, true maintenance capex, SBC, working capital, and debt; cycle-normalized FCF/earnings | Enterprise budgets, semiconductor capex, rates, AI infrastructure financing, risk appetite | `Article-ready / cycle-normalized cash open`; break with retention/utilization decay, factoring unwind, or reinvestment/SBC consuming distributable cash |
| Healthcare care infrastructure | Aging, chronic disease, access friction, staffing and reimbursement constraint | Device, site, lab, distributor, drug route, or care-coordination workflow | Patients, payers, government programs, providers, manufacturers | Clinicians and caregivers, inventory, receivables, regulation, litigation, capital and labor | Procedures/visits, utilization, reimbursement, payer mix, staffing, inventory and collections | Acquired revenue versus acquired return, adjusted charges, lease/securitization perimeter, payer timing, legal and restructuring cash | Common-owner cash after labor, working capital, maintenance capex, legal cash, leases, taxes and dilution; cohort/provider return | Employment and wages, public reimbursement, medical inflation, credit and demographic demand | `Article-ready / entity and cohort cash open`; break with reimbursement compression, labor failure, cohort losses, or receivable deterioration |
| Energy affordability and supply route | Energy cost flowing into transport, food, rent, goods and industry | Production, decline management, refining, storage, pipeline/LNG route, or service capacity | Households, utilities, industrial users, exporters, contract counterparties, lenders | Commodity volatility, depletion, sustaining capex, turnaround, inventory, debt and environmental obligations | Realized price, throughput, crack/spread, decline rate, utilization, maintenance capex and working capital | Hedging/perimeter, inventory timing, peak margin, reserve depletion, capitalized costs, non-GAAP cash and acquisition mix | Cash after maintenance capex, hedges, taxes, debt, abandonment and dilution; through-cycle asset/project return | Inflation, rates, dollar/liquidity, commodity inventories, trade and capex cycle | `Article-ready / through-cycle open`; break with decline/turnaround cost, spread normalization, or maintenance spend erasing cash |
| Ordinary finance and credit | Household/business need for liquidity, payment, savings, insurance and risk transfer | Deposit franchise, payment rail, underwriting, distribution, or capital allocation | Depositors, card users, borrowers, policyholders, institutional funders | Credit losses, funding cost, capital requirements, fraud, duration, regulation and policyholders | Net interest income after losses/funding, fee retention, delinquencies, deposits, capital and reserve adequacy | Reserve releases, charge-off timing, receivable securitization, fair value, capitalization, deposit mix, one-time gains | Unrestricted common earnings/cash after losses, capital, funding, claims and dilution; normalized ROE/FCFE | Central-bank liquidity, yield curve, unemployment, household leverage, credit spreads | `Article-ready / loss-normalized open`; break with worsening vintages, deposit runoff, funding-cost pressure, or capital need exceeding distributions |
| Affordability and substitution | Inflation and household trade-down without abandoning all routines | Assortment, price architecture, inventory discovery, and channel access | Households, vendors, card/consumer credit, advertisers and members | Inventory, markdowns, labor, leases, supplier finance, services and taxes | Comparable sales, units/transactions, inventory turns, gross margin, OCF-to-capex and dilution | Support reversal, supplier-finance normalization, attached-service perimeter, lease/tax burden and adjusted EPS | Common-owner cash after normalized working capital, maintenance capex, leases, taxes, support and dilution; expectation-based equity value | Real wages, CPI, consumer credit, employment, retailer inventory and rates | `Qualified pilot / cash gate open`; break with normalized demand and cash failing across common periods |
| Scarce physical assets and contractual control | Long-lived production, permitting and reserve scarcity | Contractual entitlement to a named output or receipt | Operator, stream/royalty buyer, industrial purchaser, lender | Operator labor/capex/permitting; buyer funding, taxes and counterparty settlement | Payable/attributable output, sold volume, price, reserve-backed delivery and funding cost | Production versus sales, reserve proxy versus payable curve, acquisition funding, debt allocation, receipt and tax perimeter | Contract-level cash after funding, taxes, debt and dilution; asset NPV/IRR | Metals cycle, real rates, dollar, mine capex and counterparty liquidity | `Qualified pilot / settlement open`; break with named credit issuance, sale/receivable, bank receipt, or reserve-backed delivery failure |
| Institutional capital and financial intermediation | Savings, premiums, credit and investment demand moving through legal wrappers | Origination, asset selection, insurance spread, borrower/facility and entity transfer | Policyholders, depositors, institutional investors, borrowers and parent capital | Regulated entities, borrowers, reinsurers, funding providers, NCI/preferred holders and common owners | Spread after liability/funding cost, credit losses, statutory capital, fees, remittance and dilution | Fair value versus funded principal, wrapper versus lender role, statutory income versus cash, related-party elimination, reserve and acquisition accounting | Named-asset or facility cash after liability cost, capital, claims, fees and entity allocation; liability-adjusted return | Rates, liquidity, credit spreads, collateral values, fiscal/money creation and refinancing | `Qualified pilot / receipt and residual open`; break with failed borrower collections, liability-adjusted spread, or unrestricted parent residual |
| Power grid and permissioned capital | Reliability, electrification and large-load demand under public oversight | Rate base, tariff/recovery category, interconnection, named project or customer obligation | Ratepayers, approved customer recovery, contracts, debt, equity and NCI | Construction, fuel, regulatory timing, financing, storm risk and customers | Billed/collected revenue, paid capex, CWIP, in-service assets, recovery balance and capital allocation | Approved recovery versus receipts, AFUDC/CWIP, category attribution, customer deposits, project approval and shared ownership | Common-owner cash after paid maintenance/growth capex, financing, taxes, regulatory timing and dilution; project return | Rates, inflation, load growth, fiscal policy, power prices, transmission and financing liquidity | `Qualified route / collections open`; break with billed-to-collected weakness or project return failing after funding and customer burden |

## How to use the matrix

The matrix is a routing tool, not a scorecard. A theme can be compelling at
the social level and still fail the investment test. The next source should be
selected from the rightmost column, and should close the named same-period,
same-entity join wherever possible.

Three discipline rules follow:

1. **Do not pool denominators.** A utility recovery, distributor cash cycle,
   insurer spread, REIT project, device cohort, and materials reserve require
   different cash definitions.
2. **Treat QoE and financial-shenanigans diagnostics as reconciliation prompts.**
   A margin gap, adjusted charge, reserve movement, supplier-finance balance,
   factoring line, or unusual working-capital result is not a fraud finding by
   itself.
3. **Do not promote a theme because the macro route is plausible.** Damodaran
   expectation work identifies the operating and reinvestment assumptions in
   the price; the Lyn Alden route identifies liquidity and regime transmission.
   Neither substitutes for collection, legal-entity, liability, or common-owner
   cash proof.

## Synthesis conclusion

Across the full sector set, the recurring pattern is not “growth” in the
abstract. It is the conversion of pressure into dependable capacity: time into
service, income pressure into assortment, raw material into usable production,
site scarcity into access, digital complexity into control, medical need into
care, molecules into energy, and promises into funded credit.

That is the larger picture. The strongest candidate businesses sit at a
control point, but the investment conclusion still depends on who bears the
burden and whether the remaining cash reaches common owners after the correct
reinvestment, funding, legal, and dilution claims. The current evidence
supports a broad, connected research map; it does not yet support a pooled
cross-sector ranking.
