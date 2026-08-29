# Capital Flow All-Company Triage

## Purpose

This is the first broad scan across the full company-packet universe.

The goal is not to deeply analyze every company. The goal is to rank where deeper capital-flow work is likely to pay off.

Machine-readable table:

`analysis/company-first-principles/data/capital-flow-all-company-triage.csv`

## Current Result

| Metric | Value |
|---|---:|
| Company packets scanned | `519` |
| High-signal rows with score >= 80 | `190` |
| Private-credit/direct-lending primary-lane rows | `7` |
| Companies with existing first-principles analysis | `50` |

## What We Are Finding

The full universe should be triaged before it is deep-dived.

The strongest next candidates are companies where the packet already contains hard numbers plus capital-flow language: debt facilities, refinancing, acquisition finance, rate base, project backlog, private credit, securitization, insurance liabilities, or government support.

This scan converts the `519` company packets into a ranked work queue. It tells us where to pull annual reports, quarterly reports, credit agreements, rating reports, and source-of-funds documents next.

## Top Ranked Candidates

| Rank | Company | Sector | Industry | Score | Primary Lane | Evidence Snippet |
|---:|---|---|---|---:|---|---|
| 1 | Kkr Co. Inc. | Financial | Asset Management | 123 | `private_credit_direct_lending` | The business is not best summarized as only fee-related earnings plus realizations, and not as only a spread-and-retirement-services engine either. |
| 2 | Apollo Global Management Inc. | Financial | Asset Management | 119 | `private_credit_direct_lending` | The model is not just management fees plus realizations; it is management fees plus spread earnings through Athene, backed by origination, retirement services, and insurance-scale balance-sheet sourcing. |
| 3 | Ares Management Corporation | Financial | Asset Management | 119 | `private_credit_direct_lending` | - Full-year `2025` closed with AUM of about `$622.5B`, FPAUM of about `$384.9B`, available capital of about `$156.0B`, gross fundraising of about `$113.2B`, net inflows of about `$107.7B`, capital deployment of about `$145.8B`, fee related earnings of about... |
| 4 | Oneok Inc. | Energy | Oil Gas Pipelines | 116 | `power_grid_and_project_finance` | Management describes the company as a leading midstream operator providing gathering, processing, fractionation, transportation, storage, and marine export services through an approximately `60,000-mile` pipeline network. |
| 5 | Pbf Energy | Energy | Oil Gas Refining Marketing | 113 | `debt_refinancing_and_facilities` | Management said the company reduced gross debt by over `\$1B` during the quarter, including exiting the asset-backed lending facility and refinancing about `\$802M` of `2028` senior notes. |
| 6 | Mastec Inc. | Industrial Goods | Engineering Construction | 113 | `power_grid_and_project_finance` | Industry: Engineering Construction |
| 7 | Plains All American Pipeline Lp | Energy | Oil Gas Pipelines | 112 | `power_grid_and_project_finance` | The official investor profile is explicit that the company owns and operates midstream energy infrastructure and provides logistics services for crude oil, with a network of gathering and transportation systems, terminalling, storage, and related assets acr... |
| 8 | Targa Resources Corp. | Energy | Oil Gas Pipelines | 111 | `power_grid_and_project_finance` | That makes it a more growth-heavy NGL-and-export platform than a narrower gas-transmission name. |
| 9 | Nextera Energy Inc. | Utilities | Electric Utilities | 111 | `power_grid_and_project_finance` | NextEra describes itself as the largest electric power and energy infrastructure company in North America. |
| 10 | Vistra Energy Corp. | Utilities | Other Utilities | 111 | `power_grid_and_project_finance` | It adds an integrated retail-plus-merchant-power platform with competitive generation, hedging, and commodity exposure rather than another primarily regulated transmission-and-distribution utility. |
| 11 | Dycom Industries Inc. | Industrial Goods | Heavy Construction | 109 | `power_grid_and_project_finance` | Industry: Heavy Construction |
| 12 | Abm Industries Inc. | Industrial Goods | Business Services | 108 | `power_grid_and_project_finance` | - It also adds a distinct operating model to the infrastructure thread. |
| 13 | Granite Construction Incorporated | Industrial Goods | General Contractors | 107 | `power_grid_and_project_finance` | # Granite Construction Incorporated Packet |
| 14 | Caci International Inc. | Technology | Information Technology Services | 107 | `power_grid_and_project_finance` | - It also helps the archive close an important gap in the physical-and-digital infrastructure stack. |
| 15 | Constellation Energy Corporation | Utilities | Diversified Utilities | 107 | `power_grid_and_project_finance` | That makes the company one of the clearest direct utility-side reads on how AI and data-center demand are reshaping power value. |
| 16 | Devon Energy Corporation | Energy | Independent Oil Gas | 106 | `debt_refinancing_and_facilities` | - The annual-close evidence chain is unusually useful because it captures the last full standalone Devon state before the Coterra merger changed the scale of the company. |
| 17 | Jacobs Solutions Inc. | Industrial Goods | Engineering Construction | 105 | `capital_intensity_and_capex` | It sits between consulting and construction: not a commodity contractor, but not an application-software platform either. |
| 18 | Dnow Inc. | Industrial Goods | Industrial Supply | 105 | `power_grid_and_project_finance` | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 19 | Duke Energy Corporation | Utilities | Electric Utilities | 104 | `power_grid_and_project_finance` | Duke is a useful third utility because it is a cleaner traditional regulated-utility comparison than NextEra while still showing the same electricity-scarcity and large-load themes now appearing across the archive. |
| 20 | Nrg Energy Inc. | Utilities | Other Utilities | 103 | `power_grid_and_project_finance` | NRG is the right ninth utility because it adds the clearest customer-backed large-load and retail-plus-wholesale platform in the current set. |
| 21 | Matador Resources Co. | Energy | Independent Oil Gas | 102 | `debt_refinancing_and_facilities` | Matador is one of the stronger missing upstream packets because it adds a more infrastructure-shaped version of independent oil and gas exposure. |
| 22 | Blackrock Inc. | Financial | Asset Management | 102 | `private_credit_direct_lending` | - Strategic read: the quarter shows how ETF scale, systematic active, private markets, outsourcing, and acquisition-led capability expansion can all reinforce each other inside one manager. |
| 23 | Blackstone Inc. | Financial | Asset Management | 102 | `private_credit_direct_lending` | Credit, insurance, infrastructure, real estate, private equity, and wealth channels all show up as earnings drivers. |
| 24 | Primoris Services Corporation | Industrial Goods | Heavy Construction | 102 | `power_grid_and_project_finance` | Industry: Heavy Construction |
| 25 | Alliant Energy Corporation | Utilities | Electric Utilities | 102 | `power_grid_and_project_finance` | The more current year-end `2025` corporate fact sheet pegs the customer counts at `1,012,286` electric and `433,344` gas customers, peak-hour demand at `5,465 MW`, total assets at `$25.0B`, construction and acquisition expenditures at `$2,483M`, and employe... |
| 26 | Edison International | Utilities | Electric Utilities | 102 | `power_grid_and_project_finance` | - The annual materials are explicit that this is a high-capex, high-risk, but still regulated-growth utility. |
| 27 | Steel Dynamics Inc. | Basic Materials | Steel Iron | 101 | `capital_intensity_and_capex` | `Commercial Metals` is the rebar, fabrication, recycling, and construction-project system. |
| 28 | Watsco Inc. | Industrial Goods | Electronics Wholesale | 101 | `power_grid_and_project_finance` | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |
| 29 | Eaton Corporation | Industrial Goods | Industrial Electrical Equipment | 101 | `capital_intensity_and_capex` | Eaton gives the industrial set a direct read on electrification infrastructure, power quality, power distribution, data-center buildout, and aerospace demand. |
| 30 | Ferguson Enterprises Inc. | Industrial Goods | Plumbing Hvac Distribution | 101 | `power_grid_and_project_finance` | Assigned CLI 8 sub-lane: wholesale and distribution infrastructure |

## Primary-Lane Distribution

| Lane | Companies |
|---|---:|
| `capital_intensity_and_capex` | 148 |
| `power_grid_and_project_finance` | 125 |
| `acquisition_finance` | 99 |
| `low_signal_general_company` | 82 |
| `debt_refinancing_and_facilities` | 33 |
| `asset_backed_and_securitization` | 13 |
| `insurance_and_retirement_capital` | 11 |
| `private_credit_direct_lending` | 7 |
| `government_and_public_funding` | 1 |

## Top-100 Sector Mix

| Sector | Top-100 Count |
|---|---:|
| Energy | 21 |
| Industrial Goods | 20 |
| Technology | 17 |
| Basic Materials | 12 |
| Utilities | 11 |
| Financial | 7 |
| Real Estate | 3 |
| Healthcare | 3 |
| Services | 3 |
| Industrials | 2 |
| Consumer Goods | 1 |

## Method

Each company is scored from its existing `company-packet.md` plus any matching `company-analysis.md`.

The score rewards:

- capital-flow signal categories
- hard numbers
- dollar-denominated numbers
- source pointers
- existing first-principles analysis

The categories are deliberately broad in this first pass:

- `private_credit_direct_lending`
- `debt_refinancing_and_facilities`
- `acquisition_finance`
- `asset_backed_and_securitization`
- `insurance_and_retirement_capital`
- `power_grid_and_project_finance`
- `capital_intensity_and_capex`
- `government_and_public_funding`

## How To Use This

Do not treat the score as a claim.

Treat it as a work allocator:

`high score -> pull primary reports -> extract real numbers -> derive bounded claim -> add disproof test`

The next best use is to take the top `25` to `50` rows, group them by lane, and build lane-specific evidence queues.

## Current Bottom Line

Yes, it makes sense to track this across all companies, but only as triage first.

This file is the bridge from the hand-built private-credit cases into a repeatable all-company capital-flow research system.
