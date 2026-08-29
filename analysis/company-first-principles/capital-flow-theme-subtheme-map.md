# Capital Flow Theme And Subtheme Map

## Purpose

This page translates the all-company triage and lane queues into the interpretive layer:

`theme -> subtheme -> company candidates -> capital-flow question -> proof package -> disproof test`

Input tables:

- `analysis/company-first-principles/data/capital-flow-all-company-triage.csv`
- `analysis/company-first-principles/data/capital-flow-lane-candidate-queues.csv`

## Big Finding

The research is no longer only about private credit.

Private credit is an important funding mechanism, but the broader pattern is a capital-routing cycle across several linked lanes:

1. managed private credit and alternative-asset platforms
2. insurance and retirement liability pools
3. power, grid, midstream, and project-finance infrastructure
4. debt refinancing and balance-sheet repair
5. acquisition finance and consolidation
6. asset-backed finance and securitization
7. capital-intensive real-economy buildout

The correct unit of analysis is not just a company.

The better unit is:

`source of money -> routing platform -> funding instrument -> operating destination -> bottleneck -> proof metric`

## Current Quantitative Frame

| Layer | Current Count | What It Means |
|---|---:|---|
| Company packets scanned | `519` | Full current company universe. |
| High-signal all-company triage rows | `190` | Companies with enough capital-flow signal to revisit. |
| Lane-specific candidate rows | `71` | Practical first work queue for primary-source extraction. |
| Explicit private-credit/platform candidates | `7` | KKR, Apollo, Ares, BlackRock, Blackstone, Carlyle, Brookfield. |
| Insurance/managed-care candidates | `4` | UnitedHealth, Cigna, MetLife, Prudential. |
| Power/grid/project-finance candidates | `15` | Utilities, midstream networks, contractors, and infrastructure service companies. |
| Debt/refinancing candidates | `10` | Companies where debt stack, facility change, or refinancing is central. |
| Acquisition-finance candidates | `10` | Companies where M&A may reveal financing flows. |
| Asset-backed/securitization candidates | `10` | Companies where receivables, leases, customer credit, inventory, or collateralized assets may matter. |
| Capital-intensity/capex candidates | `15` | Companies that turn capital into physical capacity, assets, backlog, and operating throughput. |

## Theme 1: Private-Credit Platforms As Capital Routers

### Core Theme

Private-credit platforms are not only lenders.

They are routing systems that gather money from institutions, insurance balance sheets, private wealth, retirement-linked accounts, and public shareholders, then deploy that money into loans, asset-backed finance, infrastructure credit, BDCs, private funds, and sponsor-backed borrowers.

### Subthemes

| Subtheme | Meaning | Companies To Anchor |
|---|---|---|
| Direct lending at scale | Capital is deployed into first-lien, unitranche, delayed-draw, and revolver structures outside traditional syndicated-bank channels. | Ares, KKR, Apollo, Blackstone, Carlyle |
| Insurance-linked credit | Retirement and insurance liabilities become investable spread assets through affiliated or partner insurance platforms. | Apollo/Athene, KKR/Global Atlantic, Brookfield, Blackstone |
| Wealth-channel private markets | Illiquid private assets are packaged for wealth clients and advisor channels. | Blackstone, KKR, Apollo, BlackRock, Ares |
| Public BDC transmission | Publicly listed or registered vehicles translate public/shareholder capital, notes, CLOs, and revolvers into middle-market loans. | ARCC, FSK, GSBD, OBDC |
| Borrower-level proof | The strongest claims come when platform disclosures can be tied to actual borrower rows and facility documents. | Frontline, Precinmac, Valcourt, Sunvair, AeriTek, MAI, Relation |

### Main Question

Where does the managed private-credit capital come from, and which operating borrowers receive it?

### Candidate Queue

| Rank | Company | Primary Evidence Need |
|---:|---|---|
| 1 | KKR | Credit AUM, Global Atlantic linkage, ABF/private-credit deployment, insurance capital bridge. |
| 2 | Apollo | Athene liabilities, direct origination AUM, ABF, spread-related earnings, borrower destinations. |
| 3 | Ares | Direct-lending originations, available capital, BDC/fund schedules, selected borrowers. |
| 4 | BlackRock | HPS/private-credit integration, private-market fundraising, credit platform scale. |
| 5 | Blackstone | Credit and insurance inflows, private-credit deployment, wealth-channel product flow. |
| 6 | Carlyle | Global Credit and AlpInvest/secondaries capital routing. |
| 7 | Brookfield | Oaktree credit, Wealth Solutions, insurance assets, infrastructure-credit bridge. |

### Proof Package

Extract:

- total AUM and fee-paying AUM
- credit AUM
- insurance or retirement AUM
- direct origination volume
- gross deployment
- available capital
- fundraising by channel
- BDC/fund portfolio schedules
- borrower facility size, pricing, maturity, lender group, and use of proceeds

### Disproof Test

The claim weakens if platform growth is mostly mark-to-market or fee-mix expansion rather than funded deployment, if borrower rows cannot be tied to actual facilities, or if bank lenders remain the decisive funding source.

## Theme 2: Insurance And Retirement Liabilities As Capital Supply

### Core Theme

Insurance and retirement businesses create long-duration liability pools.

Those pools need assets that can provide spread, duration, predictable cash flow, and capital-efficient yield. This is why insurance-linked capital keeps showing up near private credit, asset-backed finance, mortgages, infrastructure, and investment-grade origination.

### Subthemes

| Subtheme | Meaning | Companies To Anchor |
|---|---|---|
| Life-insurance spread portfolios | Premium and retirement liabilities are invested into fixed income, private credit, mortgages, and alternatives. | MetLife, Prudential |
| Retirement-risk transfer | Pension and annuity liabilities create large investable pools with duration-matching needs. | MetLife, Prudential, Apollo/Athene |
| Managed-care float and payment timing | Healthcare payers collect premiums and manage claims timing, but this is a different mechanism from life-insurance spread assets. | UnitedHealth, Cigna |
| Asset-manager insurance partnerships | Alternative managers use insurance platforms or insurance clients as durable capital sources. | Apollo, KKR, Brookfield, Blackstone |

### Main Question

How do insurance or retirement liabilities become credit assets, and what quality or risk sits underneath?

### Candidate Queue

| Rank | Company | Primary Evidence Need |
|---:|---|---|
| 1 | UnitedHealth | Premium revenue, medical claims payable, investment assets, operating cash timing, Optum capital needs. |
| 2 | Cigna | Premiums, pharmacy-benefit economics, investment assets, cash conversion, capital return. |
| 3 | MetLife | General account assets, retirement-risk-transfer liabilities, investment spread, credit allocation. |
| 4 | Prudential | Retirement liabilities, general-account invested assets, spread income, credit quality. |

### Proof Package

Extract:

- insurance liabilities
- premiums and deposits
- invested assets
- asset allocation by credit type
- net investment income
- spread income
- statutory capital or RBC if available
- credit quality, impairments, allowance, and ratings distribution

### Disproof Test

The claim weakens if the investment portfolio remains mostly conventional public bonds, if private credit or alternatives are immaterial, or if liability growth does not translate into investment-asset growth.

## Theme 3: Power, Grid, Midstream, And Project Finance

### Core Theme

AI, electrification, reshoring, LNG, and infrastructure demand all turn into physical buildout.

The money has to fund generation, grid, pipelines, substations, fiber routes, construction labor, backup power, and interconnection. This lane is where abstract capital demand becomes visible steel, wires, turbines, pipes, equipment, and regulated assets.

### Subthemes

| Subtheme | Meaning | Companies To Anchor |
|---|---|---|
| Regulated rate-base growth | Utility capex becomes regulated assets funded by customers and capital markets. | NextEra, Duke, Edison, Alliant |
| Merchant and contracted power | Scarce power capacity becomes cash flow through retail, capacity markets, hedging, and customer contracts. | Vistra, NRG, Constellation |
| Midstream infrastructure | Hydrocarbon and NGL logistics require pipelines, fractionation, storage, export, and processing assets. | ONEOK, Plains, Targa |
| Buildout service layer | Contractors and service companies convert funded projects into physical assets. | MasTec, Dycom, Primoris, Granite |
| Digital infrastructure adjacency | Government technology, communications, and uptime demand pull on power and physical networks. | CACI, DNOW, ABM |

### Main Question

Which companies are turning electricity/load growth and infrastructure demand into funded buildout?

### Candidate Queue

| Rank | Company | Primary Evidence Need |
|---:|---|---|
| 1 | ONEOK | Capex, project backlog, leverage, volumes, NGL/export growth, financing plan. |
| 2 | MasTec | Backlog, communications/power pipeline, customer concentration, working-capital funding. |
| 3 | Plains All American | Pipeline/logistics volumes, capex, debt, distributions, asset-sale/reinvestment pattern. |
| 4 | Targa | NGL growth projects, processing/fractionation capex, leverage and funding. |
| 5 | NextEra | FPL rate base, Energy Resources backlog, origination GW, debt/equity financing. |
| 6 | Vistra | generation fleet value, customer/load contracts, FCF, debt, capital returns. |
| 7 | Dycom | telecom/fiber backlog, customer capex dependency, working capital. |
| 8 | ABM | facility/technical-service demand, infrastructure customers, margin and cash conversion. |
| 9 | Granite | public infrastructure backlog, awards, debt and equipment funding. |
| 10 | CACI | funded backlog, defense/IT modernization, contract duration, acquisition funding. |
| 11 | Constellation | nuclear output, PPAs, Calpine integration, data-center/customer power demand. |
| 12 | DNOW | energy/industrial distribution demand, working capital, customer capex. |
| 13 | Duke | capex plan, rate base, rate cases, debt/equity needs. |
| 14 | NRG | retail/generation cash flow, customer growth, acquisition funding, debt. |
| 15 | Primoris | backlog, utility/energy project mix, working capital, capex. |

### Proof Package

Extract:

- capex plan
- funded backlog
- project-level spend
- rate base
- debt and equity issuance
- operating cash flow and free cash flow
- customer contracts or PPAs
- regulatory approvals
- volumes, MW/GW, miles, assets, or capacity additions

### Disproof Test

The claim weakens if backlog is not funded, if capex is maintenance rather than growth, if regulatory recovery is uncertain, or if project delays prevent capital from becoming operating assets.

## Theme 4: Debt Refinancing, Balance-Sheet Repair, And Capital Stack Change

### Core Theme

Refinancing is one of the cleanest places to observe capital flows because documents often state debt amounts, maturity, pricing, facility structure, and repayment.

This lane asks whether companies are repairing balance sheets, extending maturities, replacing facilities, or changing the lender mix.

### Subthemes

| Subtheme | Meaning | Companies To Anchor |
|---|---|---|
| Refinancing and maturity extension | Companies replace near-term debt with new notes or facilities. | PBF, Matador, Coterra, Cenovus |
| Facility exit or repayment | ABL, revolver, or term-loan repayment can reveal lender displacement or balance-sheet repair. | PBF, Liberty Broadband |
| Commodity-cycle balance sheets | Energy companies use cash flow, asset sales, and refinancing to survive cycle volatility. | Devon, CNX, Ovintiv |
| Nontraditional capital stack | Streaming, royalty, or structured financing can substitute for direct asset ownership or debt. | Wheaton Precious Metals |

### Main Question

Where are debt facilities changing the capital stack, maturity wall, or bank/private-credit role?

### Candidate Queue

| Rank | Company | Primary Evidence Need |
|---:|---|---|
| 1 | PBF Energy | Debt reduction, ABL exit, senior notes refinancing, insurance proceeds, liquidity. |
| 2 | Devon Energy | merger-period debt stack, maturity schedule, cash return vs leverage. |
| 3 | Matador | acquisition/development financing, revolver, notes, liquidity. |
| 4 | Liberty Broadband | Charter term loan, margin-loan repayment, transaction structure. |
| 5 | Wheaton Precious Metals | streaming/royalty financing, debt facilities, acquisition funding. |
| 6 | Enhabit | merger close, debt treatment, facility repayment or assumption. |
| 7 | Coterra | pre/post-merger debt stack and liquidity. |
| 8 | CNX | debt maturity, hedging, midstream financing, free cash flow use. |
| 9 | Ovintiv | acquisition/divestiture funding, debt reduction, capital return. |
| 10 | Cenovus | acquisition-scaled integrated energy debt and liquidity. |

### Proof Package

Extract:

- debt principal by instrument
- interest rate and maturity
- revolver capacity and drawn amount
- ABL or borrowing-base details
- repayment or refinancing language
- lender/admin agent if available
- use of proceeds
- post-transaction liquidity

### Disproof Test

The claim weakens if refinancing is routine maturity management with no change in lender source, if proceeds are not traceable, or if documents do not identify what debt was repaid.

## Theme 5: Acquisition Finance And Consolidation

### Core Theme

M&A converts capital into control.

The key is to identify whether acquisitions are funded by cash, debt, equity, private credit, bridge loans, seller notes, or asset sales, and whether the funding changes industry structure.

### Subthemes

| Subtheme | Meaning | Companies To Anchor |
|---|---|---|
| Strategic acquisition finance | Public companies use debt/cash/equity to acquire assets or peers. | Verizon, Sherwin-Williams, Phillips 66 |
| Roll-up infrastructure | Distributors and building-products companies use acquisitions to consolidate fragmented channels. | Core & Main, Lowe's, Packaging Corp., Silgan |
| Resource and materials consolidation | Mining, energy, and materials companies fund acquisitions to secure assets and reserves. | Rio Tinto, Expand Energy |
| Software/platform M&A | Software and digital platforms can use acquisition finance to change scale or capability. | Roblox |

### Main Question

Which M&A deals require financing proof before we claim capital is flowing into consolidation?

### Candidate Queue

| Rank | Company | Primary Evidence Need |
|---:|---|---|
| 1 | Core & Main | acquisition spend, debt funding, integration, waterworks consolidation. |
| 2 | Verizon | transaction financing, debt stack, spectrum/fiber/wireless capital needs. |
| 3 | Sherwin-Williams | Suvinil acquisition funding, debt/cash mix, coatings growth. |
| 4 | Lowe's | Pro/large-project acquisitions or investments, capex and debt mix. |
| 5 | Roblox | acquisition/investment funding, platform capex, cash burn or FCF. |
| 6 | Expand Energy | Southwestern merger debt/equity treatment, synergy and balance sheet. |
| 7 | Rio Tinto | lithium/copper/project acquisition spend, debt/cash funding. |
| 8 | Packaging Corporation of America | capex/acquisition mix, containerboard capacity. |
| 9 | Silgan | acquisition funding, free cash flow, debt paydown. |
| 10 | Phillips 66 | midstream/chemicals/refining capital allocation and acquisitions. |

### Proof Package

Extract:

- transaction value
- cash/debt/equity mix
- financing commitments
- bridge loans or notes
- merger proxy or closing 8-K debt language
- lender group
- use of proceeds
- target debt assumed or repaid

### Disproof Test

The claim weakens if acquisitions are immaterial, funded entirely from existing cash without broader capital-market signal, or not tied to capacity, consolidation, or strategic control.

## Theme 6: Asset-Backed Finance And Securitization

### Core Theme

Some operating companies turn receivables, leases, inventory, equipment, consumer credit, or contractual cash flows into financeable collateral.

This lane is about collateral transformation: operating assets become funding instruments.

### Subthemes

| Subtheme | Meaning | Companies To Anchor |
|---|---|---|
| Consumer receivables | Card or point-of-sale receivables become loan assets and securitization collateral. | Synchrony, Target, Dollar General |
| Inventory and distribution finance | Working capital and inventory finance support wholesale and distribution systems. | MSC Industrial, Global Industrial, Pool, Arrow, Henry Schein |
| Equipment and lease-like assets | Physical devices, fleets, and equipment can support asset-backed or collateralized funding. | Zebra, Honeywell |
| Operating-data collateral | Asset visibility and transaction data can improve credit underwriting or collateral control. | Zebra, Arrow |

### Main Question

Where are receivables, leases, collateral pools, or SPVs converting operations into financeable assets?

### Candidate Queue

| Rank | Company | Primary Evidence Need |
|---:|---|---|
| 1 | Zebra Technologies | financing programs, receivables, leases, working capital, customer-finance exposure. |
| 2 | Target | card receivables, inventory, supplier finance, lease obligations. |
| 3 | MSC Industrial | receivables, inventory, credit facility, customer working-capital cycle. |
| 4 | Global Industrial | receivables/inventory, working-capital funding. |
| 5 | Pool Corp. | seasonal inventory, receivables, revolver, distributor working capital. |
| 6 | Dollar General | inventory, leases, supplier finance, credit facilities. |
| 7 | Honeywell | receivables, customer finance, aerospace/service contracts, spin/separation finance. |
| 8 | Synchrony | loan receivables, securitization, credit losses, funding costs. |
| 9 | Arrow Electronics | inventory/receivables, vendor/customer finance, credit facility. |
| 10 | Henry Schein | receivables, inventory, dental/medical distribution finance. |

### Proof Package

Extract:

- receivables balance
- inventory balance
- customer financing assets
- securitization trust balances
- warehouse lines
- SPV obligations
- advance rates
- charge-offs or credit losses
- retained interests
- revolver usage

### Disproof Test

The claim weakens if assets are ordinary working capital with no financing program, securitization, customer credit, or collateralized funding structure.

## Theme 7: Capital-Intensive Buildout And Operating Throughput

### Core Theme

Capital flows into the real economy through companies that can absorb spend and convert it into assets, backlog, capacity, or throughput.

This lane is less about a specific financial product and more about capital absorption.

### Subthemes

| Subtheme | Meaning | Companies To Anchor |
|---|---|---|
| Engineering and project delivery | Capital needs design, program management, construction, and execution capacity. | Jacobs, AECOM, KBR |
| Materials and fabrication | Funded infrastructure becomes steel, aggregates, cement, fabricated systems, and inputs. | Steel Dynamics, Nucor, Knife River, Reliance |
| Electrical and power equipment | Data centers, grid, industrial automation, and electrification need equipment. | Eaton, Teledyne |
| Energy infrastructure | LNG, pipelines, gas distribution, and midstream assets require large capex. | Energy Transfer, Cheniere, ONE Gas |
| Access and equipment utilization | Projects can rent rather than own expensive machinery and specialty equipment. | United Rentals |
| Specialty construction | Labor and project capacity become the bottleneck between capital and completed assets. | Sterling Infrastructure |

### Main Question

Where is the real economy consuming the most capital, and how is that build funded?

### Candidate Queue

| Rank | Company | Primary Evidence Need |
|---:|---|---|
| 1 | Jacobs | backlog, contract mix, project funding sources, cash conversion. |
| 2 | Steel Dynamics | capex, steel/fabrication demand, cash flow, debt funding. |
| 3 | Eaton | electrical backlog, data-center demand, capex, acquisition funding. |
| 4 | Energy Transfer | pipeline/project capex, debt, distributions, volumes. |
| 5 | Sterling Infrastructure | backlog, project awards, equipment/capex, public/private funding mix. |
| 6 | Teledyne | instrumentation demand, acquisitions, capex, debt. |
| 7 | AECOM | backlog, funded projects, cash conversion, capital-light delivery. |
| 8 | Knife River | aggregates/capex, public infrastructure demand, debt. |
| 9 | Nucor | growth capex, downstream products, balance sheet. |
| 10 | KBR | backlog, government/industrial project funding, cash conversion. |
| 11 | Verizon | capex, debt stack, network investment, spectrum/fiber. |
| 12 | Reliance Steel & Aluminum | working capital, processing capacity, customer demand. |
| 13 | United Rentals | fleet capex, utilization, rental demand, debt funding. |
| 14 | Cheniere | LNG expansion, project debt, liquefaction capacity, contracts. |
| 15 | ONE Gas | regulated capex, rate recovery, gas distribution assets. |

### Proof Package

Extract:

- capex
- backlog
- funded awards
- capacity additions
- revenue conversion
- operating cash flow
- free cash flow
- debt issued or repaid
- project returns
- utilization
- contract duration

### Disproof Test

The claim weakens if backlog is unfunded, if capex is only maintenance, if demand is cyclical rather than structural, or if cash conversion fails despite reported growth.

## Cross-Lane Subthemes

| Cross-Lane Subtheme | Why It Matters | Evidence To Seek |
|---|---|---|
| Capital source mismatch | The original money source may not be the same as the visible lender or issuer. | shareholder base, noteholders, insurance accounts, fund subscriptions, JV members. |
| Bank coexistence | Private credit often sits beside banks rather than replacing them. | agent bank, revolver banks, term-loan lenders, payoff language, treasury/hedging roles. |
| Private vs public market visibility | Much of the real deployment is off public-company income statements. | SEC holder schedules, BDC schedules, fund reports, rating reports, merger proxies. |
| Operating bottleneck capture | The best operating companies may not receive capital directly; they benefit because funded projects need them. | backlog, orders, project awards, utilization, customer capex commentary. |
| Liability-to-asset transformation | Insurance and retirement liabilities can become credit, mortgages, infrastructure, or private assets. | invested assets, asset allocations, spread income, statutory filings. |
| Collateral transformation | Receivables, leases, inventory, and loans can become financeable pools. | securitization notes, SPVs, warehouse lines, receivable sales, credit losses. |

## Detailed Subtheme Workplans

This section turns each theme into the next extraction logic. The point is to keep moving both directions:

1. from a thesis to the documents and numbers that could prove it
2. from numbers in company reports back to the strongest claim they actually support

### 1. Private-Credit Platforms

Working thesis:

Private-credit managers are building pipes that connect retirement/insurance/wealth/institutional money to loans and asset-backed credit that are less visible in bank lending data.

Subtheme detail:

| Subtheme | First Numbers To Pull | Claim We Can Derive If The Numbers Hold | Claim We Should Not Make Yet |
|---|---|---|---|
| Direct lending at scale | credit AUM, deployment, origination, uncalled capital, number of portfolio companies, BDC investments by borrower. | The platform is converting committed capital into direct operating-company credit. | That private credit has replaced banks unless borrower documents show bank payoff or lender displacement. |
| Insurance-linked credit | insurance assets, reserve liabilities, spread-related earnings, fixed-income/private-credit allocation, affiliated manager fees. | Insurance balance sheets are a durable funding source for credit assets. | That all insurance assets are private credit; most may still be investment-grade public fixed income. |
| Wealth-channel private markets | perpetual fund AUM, retail/wealth inflows, subscriptions/redemptions, performance fees, distribution partners. | Wealth channels are becoming a second funding source for private markets. | That retail investors are directly funding specific borrowers unless fund schedules show it. |
| Public BDC transmission | debt, net assets, notes, CLOs, revolvers, portfolio fair value, investment income, borrower rows. | Publicly listed vehicles translate shareholder and debt-market capital into middle-market loan books. | That the end borrower received new money in the period unless the schedule shows originations or facility dates. |
| Borrower-level proof | facility principal, lender identity, maturity, pricing, use of proceeds, sponsor, prior debt repaid. | A specific borrower was funded by a specific private-credit vehicle or lender group. | That the ultimate investor source is known without holder schedules or fund/insurer ownership evidence. |

Best next company passes:

- `Ares`: strongest direct-lending deployment trail and BDC ecosystem.
- `Apollo`: strongest insurance-liability-to-credit bridge through Athene.
- `KKR`: strong insurance and private-credit bridge through Global Atlantic plus credit funds.
- `Blackstone`: important test of credit/insurance/wealth-channel scaling.
- `BlackRock`: important because HPS changes BlackRock from index giant into a larger private-credit allocator.

### 2. Insurance And Retirement Capital

Working thesis:

Insurance and retirement pools are not just passive balance-sheet items; they can be the upstream money source that makes private credit, mortgages, infrastructure credit, and spread investing scale.

Subtheme detail:

| Subtheme | First Numbers To Pull | Claim We Can Derive If The Numbers Hold | Claim We Should Not Make Yet |
|---|---|---|---|
| Life-insurance spread portfolios | general account assets, reserves, net investment income, yield, credit losses, ratings mix. | Insurers are turning policy liabilities into invested credit portfolios. | That risky/private credit dominates unless allocation tables show it. |
| Retirement-risk transfer | pension risk transfer premiums, annuity reserves, separate account/general account split, longevity assumptions. | Corporate pension obligations are moving into insurer-managed investment pools. | That this automatically increases credit risk; asset quality and capital data decide that. |
| Managed-care float | premiums, claims payable, medical-loss ratio, operating cash flow, investment assets. | Managed-care companies generate large timing balances and reinvestable cash, but the mechanism differs from life insurance. | That managed-care float is equivalent to annuity spread capital. |
| Asset-manager insurance partnerships | affiliated insurance AUM, reinsurance agreements, investment-management fees, asset allocation. | Alternative managers are using insurance liabilities as durable capital. | That every asset-manager insurance relationship creates borrower-level private-credit deployment. |

Best next company passes:

- `MetLife` and `Prudential`: pure large-scale life/retirement anchors.
- `UnitedHealth` and `Cigna`: contrast case where cash timing, claims payable, PBM economics, and investment assets matter, but not in the same way as annuity spread portfolios.
- `Apollo/Athene`, `KKR/Global Atlantic`, and `Brookfield Wealth Solutions`: asset-manager-owned or linked insurance systems.

### 3. Power, Grid, Midstream, And Project Finance

Working thesis:

The real-economy destination for a large share of capital is power and infrastructure capacity: generation, transmission, gas/NGL logistics, data-center power, utility rate base, and contractor backlog.

Subtheme detail:

| Subtheme | First Numbers To Pull | Claim We Can Derive If The Numbers Hold | Claim We Should Not Make Yet |
|---|---|---|---|
| Regulated rate-base growth | multi-year capex plan, rate base, rate-case approvals, allowed ROE, debt/equity issuance. | Utilities are converting external capital into regulated assets with customer recovery. | That growth is already earned if approvals or in-service timing are pending. |
| Merchant/contracted power | MW/GW capacity, contracted load, PPAs, capacity revenue, hedging, FCF, debt. | Scarce power is being monetized through contracts, capacity markets, and customer demand. | That AI/data centers are the cause unless customers or contract language tie to that demand. |
| Midstream infrastructure | pipeline miles, volumes, fractionation capacity, export capacity, growth capex, leverage. | Hydrocarbon logistics remain a major capital destination even outside clean-power narratives. | That every project is growth capital; maintenance capex and commodity-cycle exposure must be separated. |
| Buildout service layer | backlog, awards, book-to-bill, customer concentration, working capital, project margins. | Contractors and service firms are where funded projects become physical work. | That backlog equals profit; execution risk and working-capital drag can absorb the upside. |
| Digital infrastructure adjacency | funded backlog, data-center/power/customer references, communications capex, government modernization contracts. | Digital demand creates second-order capital needs in power, fiber, facilities, and technical services. | That every tech-service company is an AI infrastructure beneficiary. |

Best next company passes:

- `NextEra`, `Duke`, `Constellation`, `Vistra`, `NRG`: power generation and utility rate-base proof.
- `ONEOK`, `Targa`, `Plains`: midstream and NGL/export infrastructure proof.
- `MasTec`, `Dycom`, `Primoris`, `Granite`: service-layer backlog proof.

### 4. Refinancing And Capital-Stack Change

Working thesis:

Refinancing is the cleanest evidence lane because debt documents disclose exact principal, maturity, interest rate, collateral, repayment use, lender groups, and liquidity before/after the transaction.

Subtheme detail:

| Subtheme | First Numbers To Pull | Claim We Can Derive If The Numbers Hold | Claim We Should Not Make Yet |
|---|---|---|---|
| Maturity extension | old maturity, new maturity, coupon/spread, principal, fees, covenants. | Capital is being used to move risk through time and reduce near-term default/refinancing pressure. | That the company is healthier if leverage or interest cost worsened. |
| Facility exit/repayment | revolver/ABL drawn amount, payoff amount, termination language, cash source. | A company changed its liquidity structure or removed a lender/facility. | That private credit displaced banks without lender details. |
| Commodity-cycle balance sheets | debt, hedges, reserves, capex, free cash flow, asset sales. | Energy/materials companies use cycle cash flows and capital markets to reshape risk. | That lower debt means less capital need if capex or shareholder returns consume cash. |
| Nontraditional capital stack | streaming deposits, royalty obligations, preferred equity, JV funding, project debt. | Companies can fund assets without ordinary corporate debt. | That these instruments are cheaper or safer without economics and collateral terms. |

Best next company passes:

- `PBF Energy`: ABL exit/refinancing is likely to produce concrete debt-stack evidence.
- `Liberty Broadband`: transaction-linked facility and repayment evidence.
- `Matador`, `Devon`, `Coterra`, `CNX`, `Ovintiv`, `Cenovus`: energy balance-sheet repair and acquisition funding.

### 5. Acquisition Finance

Working thesis:

M&A is a capital-flow event when the transaction documents show where the money came from, what was bought, what debt was assumed or repaid, and how control or capacity changed.

Subtheme detail:

| Subtheme | First Numbers To Pull | Claim We Can Derive If The Numbers Hold | Claim We Should Not Make Yet |
|---|---|---|---|
| Strategic acquisition finance | purchase price, cash/debt/equity mix, bridge commitment, notes, target debt. | Capital is funding control of specific assets, customers, reserves, or capacity. | That the acquisition is accretive or strategic unless post-close performance supports it. |
| Roll-up infrastructure | number of acquired branches/sites, revenue acquired, debt funded, integration costs. | Fragmented industries are being consolidated using balance-sheet and credit-market capacity. | That roll-ups are value-creating without margin/cash conversion evidence. |
| Resource/materials consolidation | reserves/resources acquired, project capex, commodity exposure, financing mix. | Capital is being routed into scarce minerals, energy resources, or production capacity. | That acquisition value equals productive capacity if permitting/execution is uncertain. |
| Software/platform M&A | acquired capabilities, cash paid, stock issued, deferred consideration, integration spend. | Digital platforms are buying capability or scale rather than building every function internally. | That this is a financing story if deal size is immaterial to the balance sheet. |

Best next company passes:

- `Core & Main`: distributor consolidation and water infrastructure.
- `Verizon`: network/spectrum/fiber capital stack and deal financing.
- `Sherwin-Williams`: acquisition funding and coatings expansion.
- `Rio Tinto` and `Expand Energy`: resource consolidation.

### 6. Asset-Backed Finance And Securitization

Working thesis:

Operating assets become capital-market assets when receivables, inventory, leases, loans, or cash-flow pools are pledged, sold, warehoused, or securitized.

Subtheme detail:

| Subtheme | First Numbers To Pull | Claim We Can Derive If The Numbers Hold | Claim We Should Not Make Yet |
|---|---|---|---|
| Consumer receivables | loan receivables, securitized receivables, charge-offs, allowance, funding cost, delinquencies. | Consumer spending can be funded through ABS and bank/nonbank credit channels. | That growth is high quality if credit losses or delinquencies are rising. |
| Inventory/distribution finance | inventory, receivables, payables, revolver borrowing, supplier finance. | Distributors turn working capital into a recurring financing need. | That working capital equals asset-backed finance unless the facility is collateralized or explicitly tied to assets. |
| Equipment/lease-like assets | leased assets, customer finance, residual value, fleet/equipment debt, utilization. | Physical assets can support recurring collateralized funding. | That equipment demand is structural without utilization and order/backlog evidence. |
| Operating-data collateral | tracking systems, payment data, asset visibility, underwriting references. | Data can make collateral easier to monitor and finance. | That data itself is collateral unless documents tie it to credit underwriting or advance rates. |

Best next company passes:

- `Synchrony`: most direct securitization and consumer receivable proof.
- `Target`: card receivable/supplier/inventory finance contrast case.
- `Arrow`, `MSC Industrial`, `Pool`, `Henry Schein`: distributor working-capital proof.

### 7. Capital-Intensive Buildout

Working thesis:

The best operating signal is not always who raises the money. It is often who receives orders because someone else raised the money and now needs equipment, engineering, materials, rental fleets, or project execution.

Subtheme detail:

| Subtheme | First Numbers To Pull | Claim We Can Derive If The Numbers Hold | Claim We Should Not Make Yet |
|---|---|---|---|
| Engineering/project delivery | backlog, funded awards, contract mix, margins, cash conversion. | Infrastructure spending is becoming revenue visibility for project-delivery firms. | That backlog is risk-free revenue. |
| Materials/fabrication | tons shipped, capacity additions, growth capex, utilization, pricing. | Funded construction and industrial demand are pulling through physical inputs. | That price-driven revenue growth means volume growth. |
| Electrical/power equipment | orders, backlog, segment margins, capacity expansion, data-center/grid commentary. | Electrification and power scarcity are visible in equipment demand. | That all electrical growth is AI-driven without customer or end-market proof. |
| Energy infrastructure | project debt, liquefaction capacity, pipeline volumes, contracted volumes, capex. | Energy infrastructure remains a major absorber of capital. | That contracted capacity eliminates execution, rate, or commodity risk. |
| Access/equipment utilization | fleet capex, utilization, rental rates, debt, customer end markets. | Renting equipment is a capital-efficient way for projects to access machinery. | That rental growth proves new construction if replacement and pricing are not separated. |

Best next company passes:

- `Eaton`: electrical equipment demand and backlog.
- `Jacobs`, `AECOM`, `KBR`: funded project delivery.
- `United Rentals`: fleet capex and utilization.
- `Cheniere`, `Energy Transfer`, `ONE Gas`: energy infrastructure.

## Claim Ladder

Use this ladder to avoid overclaiming:

| Claim Level | What We Can Say | Minimum Evidence |
|---|---|---|
| Level 1: signal | A company belongs in a capital-flow lane. | packet keywords, industry fit, hard-number density. |
| Level 2: quantified company exposure | The company has a measurable capital-flow exposure. | annual report or quarterly filing numbers. |
| Level 3: instrument proof | A specific financing instrument moved capital. | note, loan, revolver, securitization, bridge, equity, or project-finance disclosure. |
| Level 4: source-to-use proof | The source of money and use of money can be linked. | proceeds language, lender group, investor vehicle, borrower schedule, transaction documents. |
| Level 5: system claim | A broader industry funding pattern is visible across companies. | repeated Level 3/4 evidence across multiple companies and sectors. |

## Sector Expansion Logic

Tracking all `519` companies is useful, but not all companies deserve the same depth. The better structure is:

1. keep the `519`-company scan as the broad radar
2. use the `190` high-signal rows as the revisit universe
3. use the `71` lane candidates as the primary-source work queue
4. promote companies only when they generate Level 3 or Level 4 evidence
5. compare lanes only after each lane has at least three claim-grade examples

This keeps the research broad enough to catch unexpected capital flows, but disciplined enough that the claims are built from filings, annual reports, quarterly reports, credit schedules, and transaction documents.

## What We Should Keep Doing

The next research sequence should run in two parallel tracks.

Track A: finish the deep private-credit source-of-capital queue because it is already near claim-grade.

Track B: start lane-specific primary-source passes from this theme map:

1. power/grid/project finance: NextEra, Constellation, Duke, ONEOK, Targa
2. debt/refinancing: PBF, Liberty Broadband, Matador
3. acquisition finance: Core & Main, Verizon, Sherwin-Williams
4. asset-backed/securitization: Synchrony, Target, Arrow
5. capital intensity/capex: Eaton, Jacobs, United Rentals, Cheniere
6. insurance/retirement: MetLife, Prudential, UnitedHealth, Cigna

## Current Bottom Line

The big picture is becoming clearer:

capital is flowing toward yield, infrastructure, power, acquisitions, collateralized assets, and physical capacity.

The theme/subtheme map keeps the work honest by forcing every claim into a proof package:

`what money source -> what instrument -> what company or asset -> what operating use -> what number proves it -> what would disprove it`
