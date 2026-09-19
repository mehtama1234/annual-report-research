# Q2 2026 valuation and liquidity stress matrix

Research date: `2026-09-17`  
Status: `expectation and stress workbench; no ranking`

## Purpose

The latest cash-quality panel identifies what must be normalized before a
valuation can be trusted. This matrix carries the current lanes one step further:
it identifies the correct valuation object, the reinvestment variable, the
liquidity stress, and the filing-based thesis breaker. It is not a comparable
multiple table. The companies have different legal claims, capital cycles,
accounting boundaries, and owner-cash denominators.

## Decision matrix

| Lane | Damodaran-style valuation object | Reinvestment / denominator variable | Lyn Alden-style liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Broad technology — Fortinet / Cloudflare | Forecast recognized revenue, renewal economics, operating margin, reinvestment, and dilution; treat billings/RPO/deferred revenue as visibility inputs | Service delivery, bandwidth/colocation, server replacement, capitalized contract costs, SBC replacement, and tax | Renewal slowdown plus higher infrastructure cost, rates, and inability to fund growth without equity | Deferred revenue or RPO grows while renewal, gross margin, cost-to-serve, and diluted cash conversion deteriorate |
| Basic materials — CF / Sherwin-Williams / West Fraser | Through-cycle commodity or specialty margin, invested capital, maintenance capital, terminal volume, and cost of capital | Sustaining versus transition/project capital, working capital, environmental claims, lease burden, and partner funding | Lower product prices, input inflation, tax/settlement reversal, and tighter project or acquisition financing | Reported cash depends on incident proceeds, tax deposits, partner funding, or margin peaks that reverse without recurring replacement economics |
| Consumer goods — Burlington / Ollie's / Lowe's | Store-level sales and margin durability, reinvestment per store, mature-store returns, and diluted common cash | Inventory funding, markdowns, store openings, property/lease acquisition, distribution, debt maturities, and buybacks | Consumer trade-down without adequate liquidity, inventory aging, refinancing pressure, or supplier-term reversal | Store growth and sales rise while inventory, markdown, lease, and debt claims exhaust cash after replacement spending |
| Ordinary finance — JPMorgan / American Express / Capital One | Loss-adjusted spread, fee retention, credit cost, capital requirement, payout capacity, and long-run growth | Reserve adequacy, charge-offs, funding cost, rewards/marketing, integration, regulatory capital, and dilution | Credit losses rise as funding becomes expensive and capital or liquidity prevents distributions | Reserve release or exceptional gain supports earnings while charge-offs, delinquency, integration, or capital needs rise |
| Energy supply route — Energy Transfer / Cheniere / PBF / Devon | Project or asset cash flow using throughput, cargo, crack spread, production, price, cost, capex, debt, and partner claims | Maintenance/project capex, turnaround, depletion replacement, gas procurement, customer credit, acquisitions, and exchangeable dilution | Commodity/basis shock, project delay, refinancing, counterparty stress, partner/NCI funding withdrawal, or conditional redemption failure | Adjusted EBITDA/DCF, in-transit cargo, refining margin, or acquisition production fails to reconcile to collected cash after claims |
| Integrated oil and gas — ConocoPhillips / Exxon Mobil | Through-cycle price/volume/netback, reserve life, integrated margin, reinvestment rate, and cost of capital | Reserve replacement, development and maintenance capital, royalties, abandonment, working capital, and dilution | Lower crude/gas prices, geopolitical disruption, service-cost inflation, and inability to sustain dividends/buybacks | Production declines while cash returns depend on price peaks, asset sales, deferred replacement, or exceptional/derivative effects |
| Healthcare distribution — McKesson / Cencora / Cardinal | Normalized gross profit, rebate/chargeback economics, working-capital conversion, acquisition returns, and diluted common cash | Receivables, inventory, vendor terms, specialty acquisitions, legal payments, capex, preferred/NCI claims, and debt | Payer/reimbursement pressure, supplier-term reversal, acquisition financing, opioid/legal cash, and restricted segment liquidity | Revenue and adjusted EPS grow while working capital, acquisitions, legal claims, or preferred claims consume common cash |
| Healthcare access/care delivery — UnitedHealth / Cigna / DaVita / Option Care / Addus / BrightSpring / Enhabit | Medical-cost or treatment-margin economics, reimbursement durability, service volume, labor productivity, and normalized cash by legal entity | Claims reserves, provider/service labor, reimbursement lag, quality investment, pharmacy economics, capex, and debt | Medical-cost acceleration, rate cuts, labor shortages, denial/trust backlash, cyber disruption, or payer concentration | Revenue/patient growth and adjusted earnings rise while claims, reimbursement, labor, quality, or collections deteriorate |
| Digital infrastructure — Equinix / Digital Realty | Project-level lease-up, stabilized NOI, power cost, recurring capex, development return, and diluted per-share cash | Development capex, maintenance/recurring capex, leasing commissions, partner/JV capital, ATM equity, debt, and preferred claims | Higher rates, power delays, slower lease commencement, partner withdrawal, refinancing, or equity dependence | Backlog/signed rent grows while projects fail to commence, stabilize, cover recurring capital, or earn the required return |
| Physical-capacity rental — United Rentals / URNA | Cohort-level rental yield, utilization, rate, useful life, resale value, and replacement cost; consolidated FCF is only an input until fleet cohorts are joined to returns | Fleet purchases, equipment-sale proceeds, maintenance, debt collateral, borrowing-base reserves, and parent/subsidiary transfer rights | Stress the `$2.999B` stated liquidity, `$2.802B` ABL capacity, `$1.779B` receivables collateral, fleet resale, and restricted URNA-to-parent availability separately | OCF and reported FCF remain positive while replacement intensity, used-equipment values, borrowing-base eligibility, or legal-entity availability weaken |
| Insurance/statutory — Chubb / Apollo-Athene / Accordia | Underwriting margin or named-asset income after reserve, liability cost, capital, tax, and remittance claims | Claims paid, reserve development, reinsurance/funds-held, statutory capital, credited funding cost, and parent restrictions | Catastrophe, reserve deterioration, reinsurance non-collection, surrender/funding stress, or remittance restrictions | Reported investment or underwriting earnings grow while reserves, liability cost, capital, or legal-entity cash worsen |
| Exchange/information infrastructure — CME / S&P Global | Normalized fee/subscription cash, clearing economics, acquired-cohort return, and diluted common cash | Collateral/legal availability, default-risk capital, intangible replacement, acquisitions, SBC, debt, and dividends | Volume shock, clearing default, collateral calls, regulation, cyber event, refinancing, or acquisition underperformance | Reported FCF or volume rises while collateral needs, acquisition claims, intangible replacement, or dilution consume cash |
| Restaurant franchising — McDonald's / Chipotle | Royalty/fee collection, franchisee health, mature-store economics, company-store margin, and per-share cash | Franchisee support, advertising funds, remodel/technology capex, leases, debt, repurchases, and dividends | Consumer weakness, franchisee distress, labor/food inflation, closures, refinancing, or required system reinvestment | Systemwide sales and royalties rise while franchisee health, collections, support costs, or reinvestment deteriorate |

## How to use the matrix

### Valuation is an expectation test

The valuation object must match the business. A DCF for Cloudflare should not
use RPO as current cash; a materials model should not capitalize litigation or
insurance proceeds as recurring margin; a retail model must distinguish mature
store economics from growth-store spending; a bank model must price losses and
capital rather than apply an industrial FCF multiple; an energy model must
separate contracted capacity from project cash; and an upstream model must
charge the reinvestment required to replace depletion.

For each company, the valuation workbench should show:

1. observed base-period revenue, operating cash, and capital spending;
2. the normalized numerator and every adjustment proposed;
3. maintenance, growth, acquisition, and claim allocations;
4. reinvestment as a function of growth and return on capital;
5. cost of capital and terminal assumptions;
6. price-implied expectations; and
7. the single assumption whose failure most damages value.

Until the normalized numerator is evidenced, a market multiple is an
expectation screen—not a margin of safety or an intrinsic-value conclusion.

### Liquidity is a constraint, not a second growth story

The stress overlay asks whether the company can fund senior claims through a
bad period. It must include debt maturities, revolver or borrowing-base
availability, supplier and customer terms, lease and tax cash, collateral,
regulatory capital, partner contributions, and dilution. Reported cash and
undrawn capacity should be separated from legally available cash.

### Financial shenanigans are falsifiable prompts

The matrix does not label companies fraudulent. It identifies where accounting
or presentation could make the economics appear stronger: deferred revenue,
capitalized contract costs, incident proceeds, tax timing, inventory/payables,
reserve releases, exceptional gains, in-transit recognition, adjusted EBITDA,
derivative timing, asset sales, and buybacks financed by cyclical cash. Each
flag becomes a reconciliation request with a same-entity and same-period
source requirement.

## Named-object stress overlays added this cycle

The latest source work adds four concrete stress inputs to the general
framework:

| Object | Valuation implication | Liquidity implication | Do not promote to |
|---|---|---|---|
| Wheaton / BHP Antamina | Keep BHP entitlement at `30.375%` before the threshold and `20.25%` after it as scenario inputs; allocate debt interest and tax only when the facility schedule is available | Stress silver price, delivery timing, debt service, and the company-level `$650M` Q2 / approximately `$1.4B` H1 OCF context | BHP-specific cash yield or IRR |
| URI / URNA | Value fleet replacement and resale by cohort using utilization, rental rate, useful life, and disposition assumptions; H1 OCF of `$3.305B` less `$2.885B` of rental/non-rental purchases plus `$706M` of equipment-sale proceeds is a reported bridge, not normalized owner cash | Stress the `$2.999B` stated liquidity, `$1.779B` receivables collateral, `$2.802B` ABL capacity, and URNA transfer restrictions; require the missing populated equipment certificate/NOLV schedule before treating borrowing capacity as available | Freely available parent cash, normalized lifecycle return, or a fleet-replacement-adjusted FCF yield |
| PBF refinancing | Keep the completed June 2026 2028-note redemption separate from the issued September 2032 exchangeable financing and still-pending 2030-note redemption; include the conditional `$519.690M` principal-plus-premium floor before accrued interest and model the exchangeable feature as a potential diluted-share claim | Stress gross-to-net proceeds, capped-call cost, accrued interest, fees, cash contribution, ABL availability, post-close liquidity, and settlement; do not reuse June's completed source/use bridge for September | Refinancing NPV, settled September debt reduction, or undiluted common-owner return |
| Chubb carrier | Normalize reserve development and catastrophe exposure before capitalizing operating cash | Stress `$18.453B` reinsurance recoverable for collectibility and modeled `$3.766B` U.S. hurricane PML against capital | Reserve adequacy or unrestricted common cash |

These overlays improve the Damodaran expectation burden and Lyn Alden-style
funding stress without changing the no-ranking status. Each remains a
company- or asset-specific input until the missing receipt, allocation, or
legal-availability document is obtained.

## Promotion boundary

`expectation-screen-qualified; liquidity-stress-open; no-ranking`

The next promotion requires a company-specific schedule joining the selected
valuation numerator to reinvestment, senior claims, liquidity, and diluted
common ownership. A company may be attractive under one scenario and still
fail the evidence gate; the matrix preserves that distinction.

## Source handoff

- [Q2 2026 cross-sector cash-quality control panel](combined-investment-research-q2-2026-cross-sector-cash-quality-control-panel-2026-09-17.md)
- [New-sector valuation expectation register](combined-investment-research-new-sector-valuation-expectation-register-2026-09-17.md)
- [New-sector macro/liquidity register](combined-investment-research-new-sector-macro-liquidity-register-2026-09-17.md)
- [Integrated oil and gas Q2 refresh](combined-investment-research-integrated-oil-gas-q2-2026-cash-quality-refresh-2026-09-17.md)
- [Healthcare distribution current-period synthesis](combined-investment-research-healthcare-distribution-current-period-synthesis-2026-09-17.md)
- [Healthcare access and care-delivery cluster](healthcare-access-care-delivery-cluster-synthesis.md)
- [Digital infrastructure current-period synthesis](combined-investment-research-digital-infrastructure-current-period-synthesis-2026-09-17.md)
- [Insurance brokers/carrier Q2 refresh](combined-investment-research-insurance-brokers-carrier-q2-2026-cash-quality-refresh-2026-09-17.md)
- [Exchange/information infrastructure Q2 refresh](combined-investment-research-exchange-information-infrastructure-q2-2026-cash-quality-refresh-2026-09-17.md)
- [Restaurant current-period refresh](combined-investment-research-restaurant-current-period-refresh-2026-09-17.md)

Decision marker: `q2-2026-valuation-liquidity-stress-matrix-qualified`
