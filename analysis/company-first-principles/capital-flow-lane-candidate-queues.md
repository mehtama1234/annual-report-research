# Capital Flow Lane Candidate Queues

## Purpose

This converts the all-company triage into lane-specific primary-source work queues.

Machine-readable table:

`analysis/company-first-principles/data/capital-flow-lane-candidate-queues.csv`

## Current Result

| Metric | Value |
|---|---:|
| Source company universe | `519` |
| Lane queue rows selected | `71` |
| Lanes with selected rows | `7` |

## Lane Summary

| Lane | Universe Rows | Selected Queue Rows |
|---|---:|---:|
| `private_credit_direct_lending` | 7 | 7 |
| `insurance_and_retirement_capital` | 11 | 4 |
| `power_grid_and_project_finance` | 125 | 15 |
| `debt_refinancing_and_facilities` | 33 | 10 |
| `acquisition_finance` | 99 | 10 |
| `asset_backed_and_securitization` | 13 | 10 |
| `capital_intensity_and_capex` | 148 | 15 |
| `government_and_public_funding` | 1 | 0 |

## What This Means

The private-credit work remains important, but it is only one lane.

The broader map now needs parallel queues for:

- capital-intensive buildout
- power/grid/project finance
- acquisition finance
- refinancing and debt facilities
- insurance/retirement capital
- asset-backed and securitization structures
- government/public funding

Each lane has a different proof package. A private-credit claim needs lender and vehicle evidence. A utility buildout claim needs rate-base, capex, backlog, regulatory recovery, and financing-plan evidence. An acquisition-finance claim needs transaction value, credit agreement, lender group, and use-of-proceeds evidence.

## Lane Queues

## Private Credit Direct Lending

Question: `Where does the managed private-credit capital come from, and which operating borrowers receive it?`

Numbers to extract:

`AUM/FPAUM, credit AUM, fundraising, deployment, direct-lending originations, BDC/fund schedules, borrower examples, facility-size proof.`

| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |
|---:|---:|---|---|---|---:|---|
| 1 | 1 | Kkr Co. Inc. | Financial | Asset Management | 123 | The business is not best summarized as only fee-related earnings plus realizations, and not as only a spread-and-retirement-services engine either. |
| 2 | 2 | Apollo Global Management Inc. | Financial | Asset Management | 119 | The model is not just management fees plus realizations; it is management fees plus spread earnings through Athene, backed by origination, retirement services, and insurance-scale balance-sheet sourcing. |
| 3 | 3 | Ares Management Corporation | Financial | Asset Management | 119 | - Full-year `2025` closed with AUM of about `$622.5B`, FPAUM of about `$384.9B`, available capital of about `$156.0B`, gross fundraising of about `$113.2B`, net inflows of about `$107.7B`, capital deployment of about `$145.8B`, fee related earnings of about... |
| 4 | 22 | Blackrock Inc. | Financial | Asset Management | 102 | - Strategic read: the quarter shows how ETF scale, systematic active, private markets, outsourcing, and acquisition-led capability expansion can all reinforce each other inside one manager. |
| 5 | 23 | Blackstone Inc. | Financial | Asset Management | 102 | Credit, insurance, infrastructure, real estate, private equity, and wealth channels all show up as earnings drivers. |
| 6 | 94 | The Carlyle Group Inc. | Financial | Asset Management | 90 | The recurring stack here is fee-related earnings, fundraising, carry monetization, and a broad segment mix across Global Private Equity, Global Credit, and Carlyle AlpInvest. |
| 7 | 221 | Brookfield Corporation | Financial | Asset Management | 78 | - Compared with Markel, Brookfield is the more global, capital-markets-oriented allocator; compared with the brokers, it is much more capital intensive but also more exposed to secular infrastructure, insurance-float, and private-capital growth. |

## Insurance And Retirement Capital

Question: `How do insurance or retirement liabilities become credit assets, and what quality/risk sits underneath?`

Numbers to extract:

`Insurance liabilities, invested assets, credit allocation, reinsurance structure, statutory schedules, credit quality, asset-manager linkage.`

| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |
|---:|---:|---|---|---|---:|---|
| 1 | 67 | Unitedhealth Group Inc. | Healthcare | Managed Health Care | 95 | healthcare, leadership refresh, AI and cybersecurity investment, Alegeus acquisition plans, Optum UK divestiture, and more direct attention to prior authorization and transparency. |
| 2 | 82 | The Cigna Group | Healthcare | Managed Health Care | 93 | The scarce position is trusted employer and pharmacy-benefit infrastructure. |
| 3 | 138 | Metlife Inc. | Financial | Life Insurance | 84 | MetLife gives CLI 6 the large-scale life-insurance and retirement-risk-transfer model, where earnings depend on underwriting, spread income, investment results, longevity and morbidity assumptions, and disciplined capital return rather than on loan growth o... |
| 4 | 222 | Prudential Financial Inc. | Financial | Life Insurance | 78 | Prudential gives CLI 6 the missing second pure life-insurance and retirement-risk-transfer anchor against `MetLife`, which matters because it lets the archive compare the trust-and-liability-management layer across two real large-scale insurers instead of i... |

## Power Grid And Project Finance

Question: `Which companies are turning electricity/load growth into funded infrastructure buildout?`

Numbers to extract:

`Capex plan, rate base, project backlog, customer/load contracts, financing plan, debt/equity issuance, regulatory recovery.`

| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |
|---:|---:|---|---|---|---:|---|
| 1 | 4 | Oneok Inc. | Energy | Oil Gas Pipelines | 116 | Management describes the company as a leading midstream operator providing gathering, processing, fractionation, transportation, storage, and marine export services through an approximately `60,000-mile` pipeline network. |
| 2 | 6 | Mastec Inc. | Industrial Goods | Engineering Construction | 113 | Industry: Engineering Construction |
| 3 | 7 | Plains All American Pipeline Lp | Energy | Oil Gas Pipelines | 112 | The official investor profile is explicit that the company owns and operates midstream energy infrastructure and provides logistics services for crude oil, with a network of gathering and transportation systems, terminalling, storage, and related assets acr... |
| 4 | 8 | Targa Resources Corp. | Energy | Oil Gas Pipelines | 111 | That makes it a more growth-heavy NGL-and-export platform than a narrower gas-transmission name. |
| 5 | 9 | Nextera Energy Inc. | Utilities | Electric Utilities | 111 | NextEra describes itself as the largest electric power and energy infrastructure company in North America. |
| 6 | 10 | Vistra Energy Corp. | Utilities | Other Utilities | 111 | It adds an integrated retail-plus-merchant-power platform with competitive generation, hedging, and commodity exposure rather than another primarily regulated transmission-and-distribution utility. |
| 7 | 11 | Dycom Industries Inc. | Industrial Goods | Heavy Construction | 109 | Industry: Heavy Construction |
| 8 | 12 | Abm Industries Inc. | Industrial Goods | Business Services | 108 | - It also adds a distinct operating model to the infrastructure thread. |
| 9 | 13 | Granite Construction Incorporated | Industrial Goods | General Contractors | 107 | # Granite Construction Incorporated Packet |
| 10 | 14 | Caci International Inc. | Technology | Information Technology Services | 107 | - It also helps the archive close an important gap in the physical-and-digital infrastructure stack. |
| 11 | 15 | Constellation Energy Corporation | Utilities | Diversified Utilities | 107 | That makes the company one of the clearest direct utility-side reads on how AI and data-center demand are reshaping power value. |
| 12 | 18 | Dnow Inc. | Industrial Goods | Industrial Supply | 105 | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 13 | 19 | Duke Energy Corporation | Utilities | Electric Utilities | 104 | Duke is a useful third utility because it is a cleaner traditional regulated-utility comparison than NextEra while still showing the same electricity-scarcity and large-load themes now appearing across the archive. |
| 14 | 20 | Nrg Energy Inc. | Utilities | Other Utilities | 103 | NRG is the right ninth utility because it adds the clearest customer-backed large-load and retail-plus-wholesale platform in the current set. |
| 15 | 24 | Primoris Services Corporation | Industrial Goods | Heavy Construction | 102 | Industry: Heavy Construction |

## Debt Refinancing And Facilities

Question: `Where are debt facilities changing the capital stack, maturity wall, or bank/private-credit role?`

Numbers to extract:

`Debt table, credit facility size, maturity ladder, lender/admin agent, pricing, use of proceeds, refinancing or repayment language.`

| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |
|---:|---:|---|---|---|---:|---|
| 1 | 5 | Pbf Energy | Energy | Oil Gas Refining Marketing | 113 | Management said the company reduced gross debt by over `\$1B` during the quarter, including exiting the asset-backed lending facility and refinancing about `\$802M` of `2028` senior notes. |
| 2 | 16 | Devon Energy Corporation | Energy | Independent Oil Gas | 106 | - The annual-close evidence chain is unusually useful because it captures the last full standalone Devon state before the Coterra merger changed the scale of the company. |
| 3 | 21 | Matador Resources Co. | Energy | Independent Oil Gas | 102 | Matador is one of the stronger missing upstream packets because it adds a more infrastructure-shaped version of independent oil and gas exposure. |
| 4 | 31 | Liberty Broadband Corporation | Technology | Diversified Communication Services | 101 | On May 12, 2026, Charter advanced a term loan of approximately `$359M` to Liberty Broadband to repay part of the margin-loan borrowings |
| 5 | 40 | Wheaton Precious Metals Corp. | Basic Materials | Gold | 99 | Wheaton added the `Jervois` stream in Australia, the `Spanish Mountain` royalty, and the `Cipango` royalty in Japan, showing how the model keeps growing through deal origination rather than direct mine construction ownership. |
| 6 | 48 | Enhabit Inc. | Healthcare | Specialized Health Services | 98 | Coverage note: the standalone quarter chain ends at `Q1 2026` because the Kinderhook merger closed on `2026-05-15`. |
| 7 | 51 | Coterra Energy Inc. | Energy | Independent Oil Gas | 97 | - The `2025` filings make clear that this was still a real scale independent before the merger endpoint. |
| 8 | 72 | Cnx Resources | Energy | Independent Oil Gas | 94 | The annual filing emphasizes held-by-production acreage, midstream infrastructure ownership, large data advantages, and low-cost operations as structural advantages. |
| 9 | 79 | Ovintiv Inc. | Energy | Independent Oil Gas | 93 | Purchases of `311.8 MMBOE` were primarily from the Montney acquisition and Permian properties with oil and liquids-rich potential, while sales of `156.6 MMBOE` were primarily tied to the Uinta divestiture. |
| 10 | 80 | Cenovus Energy Inc. | Energy | Oil Gas Refining Marketing | 93 | Cenovus is one of the clearest missing packets for the acquisition-scaled Canadian integrated heavy-oil system. |

## Acquisition Finance

Question: `Which M&A deals require financing proof before we claim capital is flowing into consolidation?`

Numbers to extract:

`Transaction value, sponsor, financing commitments, credit agreement, merger proxy, use of proceeds, lender group, prior debt treatment.`

| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |
|---:|---:|---|---|---|---:|---|
| 1 | 74 | Core Main Inc. | Industrial Goods | Building Materials Wholesale | 94 | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 2 | 100 | Verizon Communications Inc. | Technology | Long Distance Carriers | 90 | Verizon is a core communications-and-access packet because it shows the mobile-first side of household and enterprise connectivity more directly than Charter or Comcast while still carrying the scale, regulation, and capital intensity of national telecom in... |
| 3 | 119 | The Sherwin Williams Company | Basic Materials | Specialty Chemicals | 86 | Management highlighted double-digit Protective & Marine growth, mid-single-digit commercial growth, a return to mid-single-digit residential repaint growth, and continued weakness in new residential, while the Suvinil acquisition remained a visible but mana... |
| 4 | 135 | Lowes Companies Inc. | Consumer Goods | Home Improvement Stores | 84 | The company still lives inside consumer demand, but the real engine increasingly runs through Pro relationships, larger-project categories, delivery infrastructure, home services, and loyalty-linked workflow. |
| 5 | 145 | Roblox Corp. | Technology | Internet Software Services | 84 | The `2025` annual report does not read like a normal software packet centered on seats, contracts, or pure infrastructure. |
| 6 | 148 | Expand Energy Corporation | Energy | Independent Oil Gas | 83 | after the Southwestern merger. |
| 7 | 161 | Rio Tinto PLC | Basic Materials | Industrial Metals Minerals | 81 | The `2025` release highlights Oyu Tolgoi completion, Simandou first ore shipment, Western Range start-up, and additional lithium construction progress. |
| 8 | 165 | Packaging Corporation Of America | Consumer Goods | Packaging Containers | 81 | Packaging Corporation of America is the cleanest current extension for the behind-the-shelf consumer infrastructure lane because it adds a second corrugated-and-containerboard throughput peer beside `International Paper`, but it does so from a more concentr... |
| 9 | 166 | Silgan Holdings | Consumer Goods | Packaging Containers | 81 | - Guidance read: Silgan confirmed `2026` free cash flow guidance of about `$450M`, expected capital expenditures of about `$310M`, and guided `Q3 2026` adjusted EPS to `$1.21` to `$1.31`. |
| 10 | 167 | Phillips 66 | Energy | Oil Gas Refining Marketing | 81 | It is about how Midstream, Chemicals, Refining, Marketing and Specialties, and Renewable Fuels sit inside one capital-allocation and infrastructure system. |

## Asset Backed And Securitization

Question: `Where are receivables, leases, collateral pools, or SPVs converting operations into financeable assets?`

Numbers to extract:

`Collateral pool, warehouse/securitization size, advance rate, lender or noteholder structure, retained interests, credit losses.`

| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |
|---:|---:|---|---|---|---:|---|
| 1 | 84 | Zebra Technologies Corp. | Technology | Computer Peripherals | 93 | By reframing the business around `Connected Frontline` and `Asset Visibility and Automation`, Zebra effectively discloses itself as workflow infrastructure rather than as a collection of peripheral devices. |
| 2 | 114 | Target Corp. | Services | Discount Variety Stores | 87 | - Operating posture: non-merchandise sales increased `24.6%`; first-quarter operating income was `$1.1B`; GAAP and adjusted EPS were `$1.71`; and capital expenditures increased `31%` to `$1.0B`. |
| 3 | 142 | Msc Industrial Direct Co. Inc. | Industrial Goods | Industrial Supply | 84 | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 4 | 153 | Global Industrial Company | Industrial Goods | Wholesale Other | 82 | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 5 | 154 | Pool Corp. | Industrial Goods | Wholesale Other | 82 | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 6 | 156 | Dollar General Corporation | Services | Discount Variety Stores | 82 | The customer may not want to drive far, buy in bulk, or spend enough to make a warehouse or large grocery trip efficient. |
| 7 | 169 | Honeywell International Inc. | Industrial Goods | Aerospace Defense Products Services | 81 | Caterpillar is about heavy equipment, power generation, and physical infrastructure throughput. |
| 8 | 185 | Synchrony Financial | Financial | Credit Services | 80 | Results: net earnings were `$885M`, diluted EPS were `$2.59`, purchase volume increased `8%` to `$49.8B`, and loan receivables increased `2%` to `$102.2B`. |
| 9 | 190 | Arrow Electronics Inc. | Technology | Electronics Wholesale | 80 | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 10 | 238 | Henry Schein Inc. | Healthcare | Medical Instruments Supplies | 75 | - Structural themes: Q1 shows that the company’s moat is not only in the warehouse. |

## Capital Intensity And Capex

Question: `Where is the real economy consuming the most capital, and how is that build funded?`

Numbers to extract:

`Capex/backlog, funding mix, operating cash flow, debt issuance, equity issuance, project returns, capacity additions.`

| Lane Rank | Overall Rank | Company | Sector | Industry | Score | Evidence Snippet |
|---:|---:|---|---|---|---:|---|
| 1 | 17 | Jacobs Solutions Inc. | Industrial Goods | Engineering Construction | 105 | It sits between consulting and construction: not a commodity contractor, but not an application-software platform either. |
| 2 | 27 | Steel Dynamics Inc. | Basic Materials | Steel Iron | 101 | `Commercial Metals` is the rebar, fabrication, recycling, and construction-project system. |
| 3 | 29 | Eaton Corporation | Industrial Goods | Industrial Electrical Equipment | 101 | Eaton gives the industrial set a direct read on electrification infrastructure, power quality, power distribution, data-center buildout, and aerospace demand. |
| 4 | 34 | Energy Transfer Lp | Energy | Oil Gas Pipelines | 100 | The system now includes approximately `140,000` miles of pipeline and associated infrastructure across `44` states, with earnings exposure spanning natural gas midstream, intrastate and interstate transportation and storage, crude and refined-product logist... |
| 5 | 36 | Sterling Infrastructure Inc. | Industrial Goods | Heavy Construction | 100 | # Sterling Infrastructure, Inc. |
| 6 | 38 | Teledyne Technologies Inc. | Technology | Scientific Technical Instruments | 100 | - That makes it one of the best comparison names for showing that the infrastructure stack behind AI and advanced electronics is not only compute and communications. |
| 7 | 52 | Aecom | Industrial Goods | Engineering Construction | 97 | Industry: Engineering Construction |
| 8 | 58 | Knife River Corporation | Basic Materials | General Building Materials | 96 | Knife River is the best follow-on to Vulcan in this archive because it adds a second heavy-materials and infrastructure-buildout read, but with a more explicit mix of aggregates, downstream materials, and contracting pull-through. |
| 9 | 59 | Nucor Corporation | Basic Materials | Steel Iron | 96 | - The annual evidence suggests that Nucor is trying to become less cyclical at the margin, not by escaping steel, but by moving further into value-added products, fabricated systems, contract business, and end markets with stronger structural demand such as... |
| 10 | 75 | Kbr Inc. | Industrial Goods | Engineering Construction | 94 | Industry: Engineering & Construction |
| 11 | 87 | Verizon Communications Inc. | Services | Telecom Services Domestic | 92 | Verizon ended `2025` with `$131.1B` of total unsecured debt and `$110.1B` of net unsecured debt while still spending `$17.0B` on capital expenditures. |
| 12 | 93 | Reliance Steel Aluminum Co. | Basic Materials | Steel Iron | 90 | It also includes the infrastructure that moves, cuts, processes, and supplies metal into end markets. |
| 13 | 98 | United Rentals Inc. | Industrial Goods | Rental Leasing Services | 90 | United Rentals is the right rental-and-leasing flagship for this batch because it captures the access model behind physical infrastructure growth: customers do not need to own everything if they can rent scale, specialty capability, logistics, and service f... |
| 14 | 105 | Cheniere Energy Inc. | Energy | Oil Gas Pipelines | 88 | Cheniere adds a distinct energy-infrastructure packet because it sits at the LNG conversion and export chokepoint rather than at the wellhead or the refinery gate. |
| 15 | 110 | One Gas Inc. | Utilities | Gas Utilities | 88 | That matters because this frontier is supposed to show how physical infrastructure still shapes the wider system, and gas distribution remains one of the clearest examples of a capital-intensive, regulated network whose economics depend on reliability, cust... |

## Government And Public Funding

Question: `Where is public money lowering private capital cost or directly funding capacity?`

Numbers to extract:

`Grant/tax-credit/loan-program amount, program authority, project link, timing, conditions, private co-funding.`

_No rows selected in this lane._


## Current Bottom Line

The next research system should not run one generic extraction across every company.

It should run lane-specific extraction passes against this queue, because each capital-flow mechanism has different proof requirements and different disproof tests.
