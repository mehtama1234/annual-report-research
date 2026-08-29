# Capital Flow All-Company Scale-Up Operating Model

## Purpose

This page answers the scale question directly:

`Should we track capital flows across the whole company universe, across sectors, and then across subthemes?`

Yes, but not as one flat spreadsheet.

The right system is:

`all-company radar -> lane queue -> theme/subtheme evidence program -> primary-source extraction -> claim-grade dashboard -> disproof loop`

The machine-readable file is:

`analysis/company-first-principles/data/capital-flow-all-company-scale-up-operating-model.csv`

## Current Base

| Layer | Current Evidence |
|---|---:|
| Company packets scanned | `519` |
| High-signal rows with score >= 80 | `190` |
| Lane candidate rows selected | `71` |
| Theme evidence programs | `12` |
| Power/grid AEP-Duke regulatory extraction rows | `9` |

The broad map already says the research should scale. The deeper question is how to scale without losing proof quality.

## Visible Operating-Model Row Anchors

| Row Range | Focus |
|---|---|
| ACSU-001 to ACSU-002 | Universe radar and lane queue governance |
| ACSU-003 to ACSU-004 | Private-credit platform and borrower proof |
| ACSU-005 to ACSU-006 | Insurance/retirement capital and managed-care cash timing |
| ACSU-007 to ACSU-010 | Power/grid/project-finance demand, recovery, generation, and service backlog |
| ACSU-011 to ACSU-014 | Refinancing, acquisition finance, asset-backed finance, and capital-intensive buildout |

## Simple Answer

We should track all `519` companies, but at different depths.

| Depth | Coverage | Purpose |
|---|---|---|
| Level 0 | all `519` companies | keep a capital-flow radar so nothing important is invisible |
| Level 1 | `190` high-signal rows | rank where annual reports, quarterly reports, and outside data should be pulled |
| Level 2 | `71` lane candidates | run lane-specific extraction instead of generic summaries |
| Level 3 | top companies inside each lane | build claim-grade tables with real numbers and source links |
| Level 4 | only the strongest or most uncertain claims | reconcile company numbers against external denominators and disproof tests |

This keeps the system broad enough to discover new patterns and narrow enough to avoid pretending every company deserves the same amount of work.

The first explicit batch-refresh design is now:

`/cluster/capital-flow-519-company-batch-evidence-refresh-pass-1.md`

It takes the completed URI, Sterling, AEP/Duke, Cheniere, Atwell, and insurance bridges and turns them into repeatable lane-specific extraction gates.

## Theme And Subtheme Structure

### Theme 1: Private-Credit Platforms

Core question:

`Where does managed private-credit capital come from, and which operating borrowers receive it?`

Subthemes:

- direct lending at scale
- BDC and fund vehicle transmission
- borrower-level facility proof
- bank replacement versus bank coexistence
- source-of-capital proof from insurance, wealth, pensions, or institutional channels

Main companies:

`Ares; Apollo; KKR; Blackstone; BlackRock; Carlyle; Brookfield`

What we need to extract:

- AUM and FPAUM
- credit AUM
- direct-lending AUM
- fundraising
- deployment
- originations
- available capital
- BDC/fund schedule fair value
- borrower facility size
- use of proceeds
- lender role

Claim-grade output:

`Private-credit platform source-to-destination table.`

Disproof test:

If we only have AUM and deployment, we can prove scale but not bank replacement. Bank replacement requires borrower documents showing repayment, termination, amendment, lender change, or use-of-proceeds language.

### Theme 2: Insurance And Retirement Capital

Core question:

`How do long-duration liabilities become credit and private-asset capital?`

Subthemes:

- annuity and retirement spread assets
- alternative-manager insurance channels
- affiliated asset-management relationships
- Schedule D and Schedule BA asset quality
- managed-care cash timing as a contrast case

Main companies:

`Athene/Apollo; Global Atlantic/KKR; Brookfield Wealth Solutions; MetLife; Prudential; UnitedHealth; Cigna`

What we need to extract:

- reserves
- policyholder liabilities
- premiums and deposits
- invested assets
- net investment income
- spread income
- capital and surplus
- ratings mix
- affiliated investments
- statutory portfolio schedules

Claim-grade output:

`Liability-to-asset bridge showing whether insurance and retirement liabilities are becoming durable credit supply.`

Disproof test:

Insurance asset scale does not prove destination. We need portfolio schedules, affiliated-investment disclosures, private-placement data, or manager disclosures to tie the liability pool to actual asset destinations.

### Theme 3: Power, Grid, And Project Finance

Core question:

`Which companies are turning electricity demand, data-center load, and reliability needs into funded infrastructure?`

Subthemes:

- customer-backed large-load demand
- recoverable regulated utility capital
- generation procurement and capacity additions
- gas and midstream support infrastructure
- contractor and service-layer backlog
- external denominator reconciliation

Main companies:

`AEP; Duke; NextEra; Exelon; Constellation; Vistra; NRG; ONEOK; Targa; Plains; Energy Transfer; MasTec; Dycom; Primoris; Granite`

What we need to extract:

- contracted MW/GW
- expected load additions
- tariff obligations
- study fees
- collateral
- minimum demand
- capex plans
- rate base
- allowed ROE
- project cost
- approved MW
- under-construction MW
- backlog
- book-to-bill
- cash conversion

Claim-grade output:

`Demand-to-capex-to-recovery map by company, operating subsidiary, jurisdiction, docket, asset bucket, and status.`

Disproof test:

Load-growth commentary is weak if it does not tie to tariff, customer contract, interconnection queue, resource plan, capital plan, commission order, or actual project spend.

### Theme 4: Debt Refinancing And Facilities

Core question:

`Where is the capital stack changing through refinancings, revolvers, asset-based facilities, private placements, and maturity extensions?`

Subthemes:

- maturity-wall relief
- ABL exits or expansions
- revolver capacity changes
- private-placement debt
- lender mix and collateral changes
- refinancing used for growth versus refinancing used for survival

Main companies:

`PBF; Liberty Broadband; Devon; Matador; Coterra; CNX; Ovintiv; Cenovus; Enhabit; Wheaton`

What we need to extract:

- old debt amount
- new debt amount
- maturity
- interest rate or spread
- collateral
- lender or administrative agent
- use of proceeds
- repayment language
- covenant changes

Claim-grade output:

`Refinancing event ledger with before/after capital-stack effects.`

Disproof test:

A refinancing is not automatically growth funding. It may only extend maturities, reduce interest cost, repay existing debt, or preserve liquidity.

### Theme 5: Acquisition Finance

Core question:

`Which consolidation stories are backed by financing commitments and real balance-sheet movement?`

Subthemes:

- debt-financed strategic acquisitions
- sponsor-backed acquisition finance
- stock-and-cash mix
- assumed debt and refinancing
- bridge-to-bond structures
- acquisition capex and integration spend

Main companies:

`Core & Main; Verizon; Sherwin-Williams; Lowe's; Roblox; Expand Energy; Rio Tinto; Packaging Corporation of America; Silgan; Phillips 66`

What we need to extract:

- transaction value
- cash consideration
- stock consideration
- assumed debt
- financing commitments
- bridge loan amount
- lender group
- sponsor equity
- debt issuance
- use of proceeds

Claim-grade output:

`Deal funding proof table.`

Disproof test:

Deal value alone does not tell us who funded the transaction or whether new money entered the system. We need financing documents or debt issuance proof.

### Theme 6: Asset-Backed Finance And Securitization

Core question:

`Where are receivables, leases, inventory, loans, or other operating assets being turned into financeable collateral?`

Subthemes:

- receivables securitization
- warehouse facilities
- inventory-backed borrowing
- lease-backed finance
- consumer-credit ABS
- distributor working-capital funding

Main companies:

`Synchrony; Zebra; Target; MSC Industrial; Global Industrial; Pool; Dollar General; Honeywell; Arrow; Henry Schein`

What we need to extract:

- collateral pool
- receivables balance
- warehouse size
- note balance
- advance rate
- retained interest
- credit losses
- inventory balance
- lender or noteholder structure

Claim-grade output:

`Asset-backed funding extraction pass.`

Disproof test:

Working capital assets are not securitization evidence unless there is a facility, note, collateral pledge, sale, or retained-interest disclosure.

### Theme 7: Capital-Intensive Buildout

Core question:

`Where is the real economy consuming the most incremental capital, and how is that build funded?`

Subthemes:

- growth capex versus maintenance capex
- capacity additions
- throughput expansion
- project backlog
- industrial electrification
- materials and construction pull-through
- operating cash flow versus debt/equity funding

Main companies:

`Jacobs; Steel Dynamics; Eaton; Energy Transfer; Sterling Infrastructure; Teledyne; AECOM; Knife River; Nucor; KBR; Verizon; Reliance Steel; United Rentals; Cheniere; ONE Gas`

What we need to extract:

- total capex
- growth capex
- maintenance capex
- backlog
- capacity added
- utilization
- throughput
- operating cash flow
- debt issuance
- equity issuance
- project return language

Claim-grade output:

`Capital absorption scorecard.`

Disproof test:

High capex can be replacement, inflation, or compliance spend. The growth claim needs capacity, throughput, return, or customer-demand evidence.

## Cross-Sector Tracking Logic

The same theme can show up in many sectors, but the proof package changes.

| Sector | Likely Capital-Flow Role | Proof Package |
|---|---|---|
| Financial | capital source, vehicle, lender, insurer, asset manager | AUM, liabilities, portfolio schedules, deployment, originations, statutory assets |
| Utilities | regulated capital destination | capex, rate base, customer load, dockets, commission orders, recovery mechanisms |
| Energy | physical infrastructure and refinancing | growth capex, projects, volumes, debt, contracts, midstream capacity |
| Industrial Goods | buildout service and equipment layer | backlog, awards, capex, customer concentration, working capital, margins |
| Technology | data-center, connectivity, automation, or software-control layer | capex, infrastructure contracts, customer obligations, deferred revenue, financing needs |
| Healthcare | cash timing, consolidation, services infrastructure | claims payable, premiums, acquisitions, capex, receivables, working capital |
| Consumer Goods and Services | demand channel, inventory/receivables funding, store/logistics capex | capex, inventory, receivables, leases, securitization, supplier finance |
| Basic Materials | upstream capacity and construction inputs | capex, capacity additions, volumes, project economics, debt funding |
| Real Estate | asset ownership, development, financing cost | development spend, debt maturity, occupancy, cap rates, secured debt |

This is why we should track all companies, but not with one universal metric. A utility MW claim, a BDC borrower position, a retailer receivables facility, and a steel mill capacity project are all capital-flow evidence, but they are not the same kind of evidence.

## End-To-End Research Questions

The next deep questions should be:

1. `Where is the marginal dollar actually going: credit assets, grid assets, energy infrastructure, industrial capacity, acquisitions, or working-capital collateral?`
2. `Who supplies the money: banks, private-credit funds, insurers, public markets, customers, governments, or retained cash flow?`
3. `What turns a narrative into spend: contract, tariff, docket, debt agreement, order, asset schedule, backlog, or acquisition close?`
4. `What is only announced, what is approved, what is financed, what is under construction, and what is in service?`
5. `Which claims survive when company disclosures are reconciled against external denominators?`

## Operating Rules

### Rule 1: Keep Full Coverage, But Vary Depth

Every company gets a lane and score. Only high-signal companies get source extraction. Only claim-critical rows get outside denominator work.

### Rule 2: Do Not Mix Status Buckets

Do not combine:

- expected load
- signed load
- studied load
- approved capacity
- under-construction capacity
- in-service capacity
- announced capex
- approved capex
- recoverable capex

unless the source definitions prove comparability.

### Rule 3: Every Claim Needs A Disproof Test

Examples:

- Private credit: could this be bank coexistence rather than bank replacement?
- Utility capex: is this approved and recoverable, or only planned?
- Backlog: is it funded and profitable, or cancellable and cash-consuming?
- Acquisition finance: is deal value visible but financing invisible?
- Capex: is this growth, maintenance, inflation, or compliance?

### Rule 4: Derived Claims Must Come From The Tables

The claim should be written after the extraction row exists.

Acceptable direction:

`row -> normalized metric -> bounded claim -> source gap -> next extraction`

Weak direction:

`interesting macro story -> cherry-picked company number`

### Rule 5: The Unit Of Analysis Changes By Theme

| Theme | Best Unit |
|---|---|
| Private credit | platform -> vehicle -> borrower -> loan |
| Insurance | insurer -> liability pool -> invested asset class -> destination |
| Utilities | parent -> operating company -> jurisdiction -> docket -> project/load bucket |
| Midstream | company -> project -> contracted capacity/volume -> funding |
| Contractor backlog | company -> segment -> award/backlog -> owner capex link |
| Debt refinancing | issuer -> old instrument -> new instrument -> use of proceeds |
| Acquisition finance | buyer -> target -> transaction -> financing source |
| Asset-backed finance | issuer -> collateral pool -> facility/note -> credit performance |

## Next Work Order

1. Keep the all-company triage as the radar layer.
2. Expand `71` lane candidates into document-acquisition queues.
3. Continue the AEP/Duke regulatory extraction until final orders and cost-recovery treatment are captured.
4. Start one parallel private-credit scale pass for Blackstone, BlackRock, Carlyle, and Brookfield.
5. Start one insurance statutory-source queue for MetLife and Prudential.
6. Start one refinancing event ledger for PBF, Liberty Broadband, Devon, Matador, and Coterra.
7. Build a claim dashboard that marks every claim as `announced`, `filed`, `approved`, `financed`, `under construction`, or `in service`.

## Bottom Line

The big-picture answer is:

`Yes, track the whole company universe, but use it as a radar. The real analysis should deepen by theme and subtheme, because each capital-flow mechanism needs a different proof package. The goal is not to say every company is part of the same story. The goal is to find where money is actually being sourced, committed, financed, regulated, spent, and converted into assets.`
