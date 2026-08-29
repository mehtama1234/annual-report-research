# Capital Flow 519-Company Money Movement Map Pass 1

## Purpose

This page takes the non-queued rows from the `35` company cash-realization source table and asks the direct money-path question:

`Who is investing where, how is the money moving, from where, and into what?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-519-company-money-movement-map-pass-1.csv`

The upstream source-status table is:

`/cluster/capital-flow-519-company-cash-realization-source-table-pass-1.md`

The denominator control pass is:

`/cluster/capital-flow-519-company-denominator-control-pass-1.md`

## Current Answer

`The first money-movement map covers the 16 non-queued companies in the 35-company pilot. It shows four visible routing patterns: platform/insurance/private-credit capital into borrower or credit-channel exposure; regulated or contracted infrastructure capital into recovery, tariff, output, or backlog channels; corporate debt and treasury capital into refinancing, capex, acquisitions, or liquidity; and streaming capital into PMPA production rights. The map is source-visible but bounded: it identifies channels and destinations, not final asset-level cash-return proof.`

## Movement Patterns

| Pattern | Companies | What Is Visible | Boundary |
|---|---:|---|---|
| Platform, insurance, and private-credit channel | `4` | KKR, Apollo, Ares, and Blackstone show insurance, retirement, credit-vehicle, or borrower-holder channels. | Source/use/cash allocation to named borrowers or assets remains open. |
| Infrastructure, tariff, regulated recovery, and backlog channel | `7` | ONEOK, MasTec, Plains, Targa, NextEra/FPL, Energy Transfer, and Sterling show capex, backlog, tariff, recovery, output, or cash-proxy paths. | Project-level funding, customer receipts, or project EBITDA remains open. |
| Debt, refinancing, and treasury channel | `4` | PBF, Devon, Matador, and Liberty Broadband show debt, cash, OCF, proceeds, repayments, or collateral/liquidity denominators. | Dollar-level source/use allocation and return economics remain open. |
| Streaming/PMPA channel | `1` | Wheaton shows debt/cash denominators and Antamina PMPA funding context. | Stream-level cash receipts, tax, interest, and full PMPA return remain open. |

## Best Current Money Paths

| Company | From Where | How It Moves | Into What | Cash Channel Visible | Missing Proof |
|---|---|---|---|---|---|
| KKR | Insurance liabilities and credit vehicles | Platform and vehicle channel into private-credit holdings | Borrower/credit exposure | Platform and holder-channel signals | Borrower source/use/cash allocation |
| Apollo | Retirement/Athene inflows and invested assets | Liability-to-asset channel | Credit and alternative-investment portfolio | Spread-related earnings and inflow proxy | Asset-level statutory income and return |
| Ares | BDC and private-credit vehicles | Holder vehicles report named borrower exposure | AeriTek, Frontline, MAI, Sunvair, Valcourt exposure | Borrower fair-value/commitment destination evidence | Facility use and borrower cash generation |
| Blackstone | Credit vehicles and platform capital | Vehicle/source-stack channel | Private-credit investments | Vehicle/channel source stack | Specific borrower use and cash return |
| ONEOK | Corporate cash/debt capacity and growth capex | Midstream capex deployment | Pipelines and expansion capacity | Adjusted EBITDA and output proxy | Named-project financing and cash return |
| MasTec | Customer awards, backlog, working capital, credit | Backlog execution into revenue | Infrastructure project backlog | Revenue, EBITDA, OCF, contract-liability proxy | Owner funding, retainage, and project cash collection |
| Plains | Tariff-supported shipper payments | Published tariff route and rate | Pipeline transportation route | Route/rate evidence | Committed volumes and realized revenue |
| Targa | Liquidity, EBITDA proxy, growth capex | Capex into named projects | NGL trains, processing plants, expansions | Project output and EBITDA proxy | Project sources, contracts, and contribution |
| NextEra/FPL | Regulated recovery mechanism and capital structure | Clause recovery and true-up mechanics | Distribution Inspection / SPPCRC category | Aggregate recovery and component evidence | Category customer receipts and funding allocation |
| PBF | Notes, cash, OCF, liquidity | Refinancing and liquidity support | Refinery capex, turnaround, debt repayment | Debt/cash/OCF denominators | Refinancing value and refinery-level recurring cash |
| Devon | OCF, debt stack, merger consideration | Treasury allocation | Capex, acquisition, debt repayment, dividends, buybacks | Debt/cash/OCF and capital-return denominators | Dollar-level allocation and full-cycle return |
| Matador | OCF, secured/unsecured debt, borrowing base | Credit facility and notes support uses | Development capex, acquisitions, reserve-backed assets | Debt issuance/repayment and cash-flow denominators | Source-specific allocation and asset cash return |
| Liberty Broadband | Charter stake, debt proceeds, liquidity | Holdco collateral and restructuring mechanics | Debt retirement and collateral/liquidity structure | Debt movement and collateral bridge | LTV sufficiency and shareholder realization |
| Wheaton | Bank debt, revolver, term loan, OCF | Upfront PMPA payment | Antamina production rights | Operating cash, debt movement, stream economics proxy | Delivery cash receipts and full PMPA return |
| Energy Transfer | DCF, EBITDA, debt, revolver, growth capex | Company capital stack into projects | Midstream/export expansion | Company-level funding, output, capex, cash generation | Project contracts and project EBITDA bridge |
| Sterling | Backlog/RPO, contract liabilities, OCF, credit wrapper | Awards and credit capacity support execution | Infrastructure project backlog | Backlog, OCF less capex, revolver/L/C capacity | Funded/bonded backlog, margin, collection |

## Decision

`519-company-money-movement-map-ready`

The first money-movement map is now available for the 16 non-queued pilot rows. It should be used as an answer map and extraction guide, not as final proof of cash realization.

## Safe Claim

`The current 35-company pilot has 16 non-queued money-movement rows. The strongest visible paths are insurance/credit channels, borrower-holder destinations, regulated recovery, tariffs, backlog execution, midstream capex/output, debt/refinancing denominators, and Wheaton's Antamina PMPA funding context. These show where money appears to move and what it enters; they do not yet prove full asset-level cash return.`

## Next Work

1. Convert the five debt/refinancing rows from denominator visibility into explicit source/use/cash allocation where the local upgrade passes already have enough detail.
2. Pursue customer receipt and project contribution evidence for FPL, Energy Transfer, Sterling, ONEOK, Targa, MasTec, and Plains.
3. For KKR, Apollo, Ares, and Blackstone, prioritize statutory schedules, vehicle funding stacks, borrower facility documents, and borrower cash evidence.
