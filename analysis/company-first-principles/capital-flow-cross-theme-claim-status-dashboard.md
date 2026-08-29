# Capital Flow Cross-Theme Claim Status Dashboard

## Purpose

This page creates a single status dashboard for the capital-flow research program.

The operating table is:

`analysis/company-first-principles/data/capital-flow-cross-theme-claim-status-dashboard.csv`

The goal is to make every claim answer the same questions:

- What theme and subtheme does it belong to?
- What is the current status bucket?
- What is the strongest current evidence?
- What does that evidence prove?
- What does it not prove?
- What is the next proof step?
- What overclaim should we avoid?

## Status Buckets

| Bucket | Meaning |
|---|---|
| `queued` | We know the company/theme is high-signal, but source extraction has not yet proved the claim. |
| `announced` | Company or transaction language exists, but legal/financial proof is not yet enough. |
| `filed` | The claim has entered a formal filing, tariff, report, docket, schedule, or source table. |
| `approved` | A regulator, transaction process, or governing document has approved at least part of the claim. |
| `financed` | Financing, funded exposure, balance-sheet allocation, or credit instrument evidence is visible. |
| `under-construction` | Project, capacity, or operating buildout is underway with source-backed milestones. |
| `in-service` | The asset or financing outcome has converted into operating service, realized balance sheet, or completed transaction. |
| `trend-proven` | The metric repeats across periods rather than appearing as a one-period datapoint. |
| `thesis-grade` | Company-source evidence, external denominators, disproof tests, and bounded claims all line up. |

## Claim Dashboard

| ID | Theme | Subtheme | Current Status | Current Grade | Next Status |
|---|---|---|---|---|---|
| CTCS-001 | Private-credit platforms | Direct lending at scale | `financed` | Level 4 official platform and deployment proof | `trend-proven` |
| CTCS-002 | Private-credit platforms | Borrower-level destination proof | `financed` | Level 4 SEC-holder and transaction-role proof | `claim-grade` |
| CTCS-003 | Private-credit platforms | Bank replacement | `approved` | Level 5 for isolated cases; Level 2 for broad claim | `pattern-proven` |
| CTCS-004 | Insurance and retirement capital | Liability-to-credit channel | `financed` | Level 4 platform and balance-sheet proof | `statutory-proven` |
| CTCS-005 | Insurance and retirement capital | Asset quality and risk migration | `announced` | Level 2 partial risk evidence | `risk-grade` |
| CTCS-006 | Power grid and project finance | Customer-backed large-load demand | `filed` | Level 4 for AEP Ohio and Duke ESAs; Level 3 broader lane | `approved` |
| CTCS-007 | Power grid and project finance | Recoverable regulated utility capital | `filed` | Level 3 to Level 4 depending on jurisdiction | `approved` |
| CTCS-008 | Power grid and project finance | Generation procurement | `approved` | Level 4 for Duke Anderson; Level 3 for broader project table | `under-construction` |
| CTCS-009 | Power grid and project finance | Buildout service backlog | `announced` | Level 3 official company-source proof | `cash-proven` |
| CTCS-010 | Power grid and project finance | Midstream and fuel logistics | `financed` | Level 3 official company-source proof | `project-grade` |
| CTCS-011 | Debt refinancing and facilities | Capital-stack change | `filed` | Level 2 packet-derived first-pass event ledger | `credit-agreement-grade` |
| CTCS-012 | Acquisition finance | Deal funding and control | `filed` | Level 2 packet-derived first-pass acquisition ledger | `deal-document-grade` |
| CTCS-013 | Asset-backed finance and securitization | Collateralized operating assets | `filed` | Level 2 packet-derived first-pass asset-backed ledger | `collateral-document-grade` |
| CTCS-014 | Capital-intensive buildout | Growth capex and physical capacity | `filed` | Level 3 source-table-backed first-pass buildout evidence | `project-and-cash-grade` |
| CTCS-015 | Cross-lane governance | Outside denominator proof | `filed` | Level 3 method proof | `thesis-grade` |

## What We Are Saying Now

The research is no longer only asking:

`Where are companies spending money?`

It is asking:

`What has moved from narrative into a document, obligation, financing instrument, regulatory process, funded exposure, project milestone, or operating asset?`

That matters because the same dollar-flow story can sit at very different evidence levels.

Examples:

- Ares platform credit scale is already `financed` evidence because AUM, direct-lending AUM, deployment, and transaction counts are visible.
- Broad bank-displacement language is not thesis-grade because it needs repeated borrower takeout cases and category-matched bank denominators.
- AEP Ohio large-load demand is stronger than generic load commentary because it has a tariff process with study, LOA, ESA, collateral, minimum-demand, and exit-fee mechanics.
- Duke Anderson County generation procurement is stronger than a planning-table row because it has South Carolina PSC docket and approval evidence.
- Contractor backlog is still weaker than utility dockets because backlog still needs funded-award, margin, working-capital, and cash-conversion proof.

## Theme And Subtheme Detail

### Private-Credit Platforms

Current strongest claims:

- platform-scale credit routing is real
- borrower-level destination proof exists for a growing set of operating companies, now normalized into an `83` row Ares borrower holder-expansion table with holder-source taxonomy and a `9` row same-period borrower control
- specific bank-facility takeout can be proven in isolated cases

The main boundary:

`AUM and deployment are not bank replacement.`

The normalized borrower-holder layer now preserves holder vehicle, holder-source taxonomy, capital-channel group, period, instrument, funded fair value, unfunded commitment, transaction context, facility-size status, bank-replacement status, safe claim, and do-not-claim boundary across AeriTek, Atwell, Frontline Road Safety, MAI Capital, Precinmac, Relation Insurance, Sunvair, Valcourt, and Jiffy/PVA. The same-period summary selects one actual holder-dollar reporting period per borrower before summing fair value or commitments. The promoted borrower-level total remains the master-rollup `1.1578648B USD` latest visible funded fair value, not the raw row-level audit sum.

The next proof step:

Build repeated borrower cases with prior bank facility, new lender group, use of proceeds, termination or repayment language, and post-close bank-role checks.

### Insurance And Retirement Capital

Current strongest claims:

- insurer-linked capital is a real source of credit supply
- Apollo/Athene, KKR/Global Atlantic, Brookfield, and Blackstone each show a measurable insurance-linked or insurer-client channel

The main boundary:

`Insurance balance-sheet scale does not prove specific borrower destination.`

The next proof step:

Pull statutory statements, Schedule D, Schedule BA, ratings mix, impairments, affiliated-investment detail, and rating-agency risk overlays.

### Power, Grid, And Project Finance

Current strongest claims:

- some large-load demand has moved into tariff and ESA mechanics
- some utility capital plans have docket and regulatory entry points
- some generation procurement has project-level approval evidence
- midstream and contractor layers are visible capital-absorption channels

The main boundary:

`Do not mix signed load, expected load, late-stage pipeline, under-construction load, approved MW, and in-service MW.`

The next proof step:

Push the AEP/Duke method to operating-company, jurisdiction, docket, project, status, dollars, MW, and recovery mechanism.

### Debt, Acquisition, Asset-Backed, And Buildout Lanes

Current strongest claims:

- refinancing now has a first-pass event ledger with named debt events, amounts, instruments, and next-source requirements
- acquisition finance now has a first-pass acquisition ledger with named deal/context rows, asset-control consequences, and next-source requirements
- asset-backed finance now has a first-pass ledger separating true finance rows from collateral-search rows
- capital-intensive buildout now has a first-pass ledger tying named company rows to backlog, throughput, capacity investment, fleet spend, materials, engineering, energy infrastructure, telecom networks, and regulated replacement assets
- the correct proof packages are defined

The main boundary:

`Filed first-pass evidence is not credit-agreement-grade proof.`

The next proof step:

Start primary-source extraction passes:

- debt footnotes, credit agreements, indentures, repayment language, and maturity schedules for the RFL refinancing-event rows
- deal documents, financing notes, purchase-accounting tables, assumed-debt schedules, and post-close operating metrics for the AFL acquisition-finance rows
- securitization notes, receivables-facility agreements, trust reports, collateral pools, advance rates, retained interests, and loss tables for the ABF asset-backed rows
- growth-versus-maintenance capex, project schedules, capacity additions, utilization, throughput, funded backlog, working-capital bridge, debt/equity funding, rate recovery, and project-return evidence for the CIB buildout rows

The CIB next pass now has a project/cash extraction queue that groups the first-pass rows by proof type: energy infrastructure, materials and fabrication, rental fleet, specialty construction, engineering/project delivery, electrical equipment, telecom capex, gas-utility recovery, and cross-buildout claim governance.

The big-picture remaining-work map now defines the full proof chain for the capital-flow thesis: `capital source -> funding vehicle -> company -> asset/project/backlog -> operating output -> cash/return -> durability -> safe claim`. It converts the broad remaining work into `12` layers: capital source, funding vehicle, destination company, asset/project, use of proceeds, operating conversion, cash/return, durability, outside denominator, disproof tests, claim governance, and scale-up system. This keeps the work from collapsing into one company or one lane: Sterling remains a useful case study, but the real objective is a repeatable capital-flow operating system across companies and sectors.

The promoted-claims and overclaims pass now adds `15` writing-control rows. It separates what the evidence lets us say from what we should not say yet across private credit, BDC borrower exposures, bank replacement, insurer and retirement capital channels, AI/power load, utility recovery, energy infrastructure, URI fleet capex, Sterling backlog, funding-wrapper logic, operating conversion, outside denominators, trend proof, and the `519` company scale-up program.

The first CIB project/cash extraction pass has also started classifying current evidence by status bucket: `capex-visible`, `growth-maintenance-split`, `project-scheduled`, `contracted-or-regulated`, and `cash-converting`. This improves the claim language, but it still does not promote CTCS-014 to full `project-and-cash-grade`.

The CIB priority source manifest now identifies the first `8` source-family pulls needed for Energy Transfer, Cheniere, United Rentals, and Sterling Infrastructure. It also records the current file-availability boundary: source ledgers are present, but the raw priority documents must be rehydrated or retrieved before source-table extraction can be called primary-source proof.

The first CIB priority source-table extraction pass has now rehydrated SEC Q2 `2026` source families for United Rentals and Sterling Infrastructure and extracted `22` source-table rows.

The first CIB energy source-table extraction pass has also rehydrated SEC Q2 `2026` source families for Energy Transfer and Cheniere and extracted `24` source-table rows across midstream cash generation, growth-versus-maintenance capex, NGL export and Permian takeaway capacity, LNG train completion, cargo throughput, capital deployment, and funding mix. This materially strengthens CTCS-014, but the dashboard status remains below full `project-and-cash-grade` until annual/Q4 baselines, source-page/slide citations, project-cost tables, customer/contract terms, debt-facility mapping, and outside denominator checks are complete.

The annual baseline source-table pass now adds `32` FY/Q4 `2025` ET/Cheniere rows. It strengthens the energy subthemes from one-quarter evidence to baseline-plus-update evidence: ET shows a large existing growth-capex program and an explicit Lake Charles LNG suspension/capital-reallocation decision, while Cheniere shows annual LNG cash generation, 670 cargoes, long-duration contracted production, CCL Stage 3 execution, CCL Trains 8/9 construction, a named CPC Taiwan SPA, and a mixed growth-capex/equity/debt/liquidity funding model. CTCS-014 remains below thesis-grade because project cost, customer economics, debt facility mapping, and outside capacity denominators are still missing.

The industrial annual baseline source-table pass adds `36` FY/Q4 `2025` United Rentals/Sterling rows. It separates the two industrial subthemes: URI is a fleet-access capital absorber with annual OEC, fleet productivity, rental capex, used-equipment proceeds, operating cash flow, free cash flow, leverage, and liquidity; STRL is a specialty-construction execution platform with signed backlog, combined backlog, unsigned awards, future-phase opportunities, E-Infrastructure growth, CEC acquisition contribution, operating cash flow, and modest company-level capex. This makes CTCS-014 stronger, but also more bounded: URI fleet capex and STRL backlog are different evidence types and should not be merged into one generic buildout metric.

The project denominator workbench now adds `18` rows that define the next proof tests for ET, Cheniere, United Rentals, and Sterling. The workbench shifts CTCS-014 from source-family restoration into external validation: EIA/DOE/FERC/SEC/rating/industry/Census/project-source checks now have explicit join keys, first metrics to pull, acceptance rules, and disproof signals. CTCS-014 stays at `filed` because the workbench defines the external proof path; it has not yet extracted the external denominator numbers.

The first energy project denominator pass now adds `14` external denominator rows for ET and Cheniere. ET gets EIA support for the NGL/export bottleneck subtheme through U.S. ethane, propane, and HGL export series. Cheniere gets DOE support for the LNG cargo-conversion subtheme, including a clean Q2 `2026` match between Cheniere's `184` reported cargoes and `184` DOE vessel export rows from Sabine Pass and Corpus Christi. CTCS-014 still should not be promoted to full `project-and-cash-grade` because project costs, train-specific FERC status, entity-level debt waterfalls, use-of-proceeds, customer economics, and returns remain open.

The first industrial denominator pass now adds `16` external/context rows for URI and Sterling. URI is tested against machinery/equipment rental revenue and construction-machinery investment denominators. Sterling is tested against Census construction-spending categories and a processed Census/BLS data-center construction series. The result is narrower and more useful than a generic buildout claim: URI is a fleet-access capital absorber, while Sterling is a customer-project execution platform levered to selected mission-critical pockets. CTCS-014 remains below full `project-and-cash-grade` until fleet utilization, OEC mix, backlog roll-forward, contract assets/liabilities, customer funding, project economics, and source-of-funds are extracted.

The first industrial conversion pass now adds `16` rows that join company metrics into conversion tests. URI now has a fleet-capex-to-cash bridge: H1 `2026` operating cash flow was `112.8%` of gross rental capex, net cash rental-equipment investment after proceeds was `2.040B USD`, OEC rose `1.32B USD` from year-end `2025`, and fleet productivity increased `3.4%`. Sterling now has a backlog/cash bridge with acquisition separation: acquisition revenue contribution was `21.5%` of Q2 revenue, CEC/Stone Ridge contributed `2.56B USD` to signed backlog plus unsigned awards, combined backlog was `4.8x` Q2 revenue, and H1 operating cash flow less capex was `258.375M USD`. This strengthens CTCS-014, but it remains below full `project-and-cash-grade` because utilization, project/customer funding, source-of-funds, margins, and contract-asset/liability roll-forwards remain open.

The first project funding map now adds `20` rows across ET, Cheniere, URI, and Sterling. It makes the funding boundary explicit: ET and URI have company cash/facility capacity, Cheniere has a direct equity-funded growth-capex split, and Sterling has company cash conversion plus expanded revolver capacity. This is a real improvement because funding is no longer blank, but CTCS-014 remains below full `project-and-cash-grade` until credit agreements, project-finance tables, debt maturities, use-of-proceeds, customer funding, and project-level return evidence are extracted.

The first credit-agreement and project-finance pass now adds `20` rows across the same four companies. ET now has visible revolver/commercial-paper/refinancing evidence: a `5.00B USD` Five-Year Credit Facility, `1.21B USD` outstanding facility borrowings including `1.12B USD` commercial paper, and `3.00B USD` January `2026` senior notes used to refinance existing indebtedness. Cheniere now has first-pass entity-level debt separation, including `5.027B USD` of SPL debt, `9.550B USD` of CQP debt, `1.750B USD` of long-dated CQP notes issued by Q2 `2026`, and a quantified `75.2%` H1 growth-capex share not identified as equity-funded in the earnings release. URI now has a visible asset-backed/corporate fleet funding stack: `1.414B USD` AR securitization facility balance, `1.666B USD` ABL balance, `971M USD` term loan, and `9.823B USD` senior-note carrying amount. Sterling now has a clearer credit-platform reset: `285.000M USD` term loan at Q2, zero revolver borrowings before the reset, and a July `2026` `1.5B USD` revolving facility, a `10.0x` increase versus the FY2025 revolver. This moves CTCS-014 from funding-map support to credit-stack-visible support, but still not to full `project-and-cash-grade` because borrowing-base detail, covenants, indentures, project waterfalls, customer funding, and asset-level source-and-use schedules remain open.

The credit-document source-locator pass now carries `17` rows that identify the next document layer and selected retrieval results. It records cached local quarterly debt-table support, candidate Item `1.01`/`2.03` 8-Ks, the exact Sterling Exhibit `10.1` SEC URL for the July `2026` Second Amended and Restated Credit Agreement, retrieved URI June `2026` receivables exhibits, retrieved URI July `2025` ABL exhibits, and classification of the URI August `2025` candidate as a secured term-loan amendment. This does not lift CTCS-014 to full borrowing-base or project-finance grade; it makes the remaining evidence gate explicit.

The first filed-credit term-summary pass now adds `20` rows from cached filed 10-Q/10-K debt notes. It moves CTCS-014 from document-locator-only support into `filed-term-summary` support: ET now has a `3.00B USD` January `2026` senior-note coupon/maturity ladder, `1.60B USD` of near-term note redemptions, a `3.01x` Five-Year Credit Facility covenant ratio clue, and `1.75B USD` of July `2026` junior subordinated notes. Cheniere now has separable SPL/CQP/CCH/parent debt layers plus a `29.0B USD` debt-and-interest schedule and `290.6B USD` executed-SPA revenue denominator. URI now has a `14.230B USD` debt-stack ladder, `125.8%` AR collateral-pool-to-borrowing coverage, and a `37.0%` ABL draw-intensity check. Sterling now has a pre/post credit-platform reset: `450M USD` old platform, `285.305M USD` Q2 debt, July `2026` `1.5B USD` revolver, `500M USD` incremental base amount, and a `10 bp` SOFR-adjustment elimination. This strengthens the subthemes, but CTCS-014 still remains below full agreement-term, borrowing-base, covenant, waterfall, and project source-of-funds grade.

The URI borrowing-base fleet-collateral pass now adds `16` rows that join fleet-capital conversion with the secured funding wrapper. URI has `23.8B USD` of Q2 `2026` OEC, H1 operating cash flow equal to `112.8%` of gross rental capex, `2.040B USD` of net cash rental-equipment investment after sale proceeds, `125.8%` AR collateral-pool coverage, `365M USD` of AR excess collateral pool, `37.0%` ABL draw intensity, and `2.999B USD` liquidity. This strengthens the URI part of CTCS-014, but it remains below borrowing-base-grade because advance rates, eligibility rules, reserves, L/Cs, legal availability, asset-class utilization, and growth-versus-replacement capex are still missing.

The URI fleet-capital durability pass now adds `210` rows across Q1 `2024` through Q2 `2026`. It shows repeated rental revenue, positive fleet productivity, positive average-OEC growth, H1 `2026` gross rental capex up `28.9%` year over year, H1 `2026` net fleet cash investment up `43.0%` year over year, H1 `2026` OCF covering `112.8%` of gross rental capex and `162.0%` of net fleet cash investment, AR collateral coverage above `100%` in every extracted period, and ABL draw intensity between `27.7%` and `57.5%`. This moves URI toward `trend-proven` support inside CTCS-014, but not to thesis grade because asset-class returns, growth/replacement split, legal availability, borrowing-base mechanics, and source-of-funds by purchase remain missing.

The URI receivables purchase agreement mechanics pass now adds `20` rows from the actual June `18`, `2026` 8-K and Exhibit `10.1`. It gives URI agreement-term-visible support for the AR securitization wrapper: `1.500B USD` purchase limit, named bank commitments totaling `1.500B USD`, June `18`, `2027` commitment termination date, receivables-only repayment source, reserve formulas, reporting mechanics, termination tests, and true-sale/non-consolidation opinion conditions. This strengthens URI's funding-wrapper proof, but CTCS-014 still remains below full borrowing-base or thesis grade because legal availability, monthly-report inputs, collateral reports, and fleet-return evidence are still missing.

The URI ABL agreement mechanics pass now adds `30` rows from the actual July `11`, `2025` 8-K, Fifth Amended and Restated Credit Agreement, and U.S./Canadian security agreements. It gives URI agreement-term-visible support for the ABL wrapper: `4.500B USD` facility size, July `10`, `2030` maturity, `2.049B USD` drawn and `2.428B USD` available at the reset date, `300M USD` L/C sublimit, `1.0x` springing FCCR tied to low availability, cash-dominion trigger mechanics, and collateral categories that include accounts, inventory, and rental equipment. This closes the ABL agreement-term gap, but CTCS-014 still remains below borrowing-base or thesis grade because current legal availability, advance rates, eligibility cuts, reserves, field exams, fleet utilization, and source-of-funds by fleet purchase remain missing.

The URI ABL borrowing-base definitions pass now adds `32` rows from the July `2025` ABL agreement. It shows the actual formula layer: U.S. borrowing-base value includes `60%` of eligible merchandise and consumables inventory plus eligible rental equipment capped at the lesser of `100%` net book value and `85%` net orderly liquidation value, less reserves; Canadian borrowing-base value uses the same `100%` NBV / `85%` NOLV rental-equipment limiter, less reserves. It also extracts Combined Availability, Suppressed Availability, Borrowing Base Certificate contents, quarterly and conditional monthly reporting, a `1.250B USD` pre-appraisal acquisition/investment adjustment cap, reserve discretion, and inspection/appraisal triggers. This closes the formula-definition gap, but CTCS-014 still remains below live borrowing-base grade because eligible collateral dollars, reserve balances, appraisal values, legal availability, and source-of-funds by fleet purchase are still missing.

The URI ABL borrowing-base certificate source-boundary pass now adds `18` rows. It makes the remaining certificate gap precise: the agreement references an `Exhibit A` certificate form but the filed text does not expose a populated form or live values; it does prove that a May `31`, `2025` Borrowing Base Certificate was delivered to the Agent and Lenders as a closing condition and that closing Combined Availability had to be at least `1.000B USD`. The required missing fields are now mapped: eligible inventory, eligible rental-equipment NBV, eligible rental-equipment NOLV, reserves, outstandings, caps, Combined Borrowing Base, Combined Availability, and Suppressed Availability. This keeps CTCS-014 below live borrowing-base grade while defining the exact source hunt.

The URI ABL public-disclosure proxy bridge now adds `25` rows. It uses Q2 `2026` public filings to bound, but not prove, live availability: cash was `112M USD`, total liquidity was `2.999B USD`, implied ABL plus AR facility availability inside liquidity was `2.887B USD`, gross unused ABL stated capacity was `2.834B USD`, gross unused AR purchase-limit capacity was `86M USD`, and gross unused ABL plus AR stated capacity before constraints was `2.920B USD`. The small `33M USD` difference between gross unused stated capacity and implied facility availability should be treated as constraints, L/Cs, reserves, timing, definitions, or rounding. This gives CTCS-014 a public-disclosure proxy bridge while still keeping it below live borrowing-base grade.

The URI fleet return/utilization proxy pass now adds `31` rows. It uses Q2 `2026` public filings to bound, but not prove, fleet economics: Q2 rental revenue/OEC was `16.2%`, annualized Q2 rental revenue/OEC was `64.7%`, Q2 adjusted EBITDA/OEC was `8.6%`, annualized Q2 adjusted EBITDA/OEC was `34.6%`, H1 OCF covered `112.8%` of gross rental capex, fleet productivity rose `3.4%`, and Q2 used-equipment sales had a `52.9%` OEC recovery rate with a `46.7%` GAAP gross margin. This gives CTCS-014 `fleet-return-proxy-visible` support while still keeping it below asset-level ROIC, true utilization, rate/time/mix split, and growth/replacement capex grade.

The URI owned-rental segment economics pass now adds `40` rows from the filed Q2 `2026` 10-Q. It separates owned-equipment rental revenue from re-rent and ancillary revenue: owned-equipment rentals were `2.991B USD` in Q2 and `5.676B USD` in H1, equal to `77.7%` and `78.1%` of equipment-rentals revenue. It also separates general-rentals and specialty segment economics: specialty was `36.1%` of H1 equipment-rental revenue but `41.1%` of H1 equipment-rentals gross profit, with a `43.1%` H1 gross margin versus `34.8%` for general rentals. This gives CTCS-014 `owned-rental-segment-economics-visible` support while still keeping it below true utilization, rate/time/mix split, segment ROIC, and growth/replacement capex grade.

The URI owned-rental segment trend pass now adds `40` rows. It moves URI's segment evidence from current-period support to trend support: owned-equipment rentals were `80.0%` of FY `2025` equipment-rentals revenue, down from `82.5%` in FY `2023`, while specialty rose from `27.0%` to `33.6%` of annual equipment-rental revenue and from `33.1%` to `38.5%` of annual equipment-rentals gross profit. In H1 `2024` to H1 `2026`, specialty rose from `30.4%` to `36.1%` of equipment-rental revenue and from `37.9%` to `41.1%` of equipment-rentals gross profit. The safe reading is trend-visible specialty share gain, not segment ROIC, because specialty gross margin compressed from `48.9%` in FY `2023` to `43.6%` in FY `2025`.

The URI segment asset-return proxy pass now adds `30` rows. It pairs filed segment equipment-rentals gross profit with filed segment total assets: specialty's annual gross-profit/assets proxy was `30.8%` in FY `2023`, `27.6%` in FY `2024`, and `25.0%` in FY `2025`, versus general rentals at `15.8%`, `15.4%`, and `14.8%`. In H1 `2026`, specialty's annualized gross-profit/average-assets proxy was `26.4%` versus `14.7%` for general rentals. This gives CTCS-014 `segment-asset-return-proxy-visible` support, but keeps it below ROIC, ROA, true utilization, segment OEC, operating-profit return, or growth/replacement capex grade.

The URI specialty margin driver boundary pass now adds `22` rows. It shows that specialty margin pressure is `driver-visible`, not `driver-quantified`: specialty equipment-rentals gross margin compressed from `48.9%` in FY `2023` to `43.6%` in FY `2025`, and from `48.5%` in H1 `2024` to `43.1%` in H1 `2026`; the filed MD&A names ancillary mix, specialty ancillary mix, inflation, normal cost variability, delivery costs, labor and benefits costs, used-equipment pricing normalization, Yak/acquisition mix, and Q2 `2026` specialty margin pressure as relevant drivers or context. This strengthens CTCS-014's operating-driver trail while staying below quantified margin bridge, ROIC, and true utilization grade.

The URI rate/time/mix source-boundary pass now adds `18` rows. It turns the fleet-productivity question into a cleaner proof gate: URI public releases show a bridge from rental revenue growth to average OEC, assumed inflation, aggregate fleet productivity, and ancillary/re-rent contribution, including Q2 `2026` fleet productivity of `3.4%`, inferred ancillary/re-rent contribution of `3.7%`, and H1 `2026` fleet productivity of `2.9%` with inferred ancillary/re-rent contribution of `3.0%`. The boundary is explicit: this is `rate-time-mix-source-boundary-visible`, not rental-rate, time-utilization, or mix quantified.

The URI investor deck fleet-productivity pass now adds `20` rows and caches four official investor presentations. It confirms the deck-level bridge and upgrades the evidence from source-boundary to `investor-deck-aggregate-productivity-bridge-visible`: the Q2 `2026` deck defines fleet productivity as the combined impact of rental rates, time utilization, and mix, then shows Q2 `2026` rental revenue growth of `12.7%` bridging through `7.1%` average OEC growth, `-1.5%` assumed inflation, `3.4%` fleet productivity, `9.0%` owned-equipment rental revenue growth, and `3.7%` ancillary/re-rent contribution. It still does not quantify the internal rate/time/mix split.

The URI transcript rate/time/mix commentary pass now adds `16` rows. It gives the first qualitative internal split: for Q4 `2025`, rate was positive/stable, time was slightly less positive, and mix was the major negative driver because Matting project timing was worth roughly one point of fleet productivity. It also adds Q2 `2025` evidence that about `15M USD` of fleet movement supported high time utilization and efficient capital utilization, and Q2 `2026` evidence that ancillary/re-rent grew nearly `28%`. This strengthens CTCS-014's operating-driver trail while keeping the status below a quantified rate/time/mix split or true utilization proof.

The URI ancillary/Matting margin bridge pass now adds `18` rows. It keeps CTCS-014 honest by separating fleet-productivity mix from ancillary/re-rent margin mix: Matting explains a Q4 `2025` productivity-mix movement, while lower-margin ancillary/re-rent revenue mix explains part of the specialty margin pressure in the Q2 `2026` source trail. Specialty is still gaining revenue and gross-profit share, but its margin compressed from `48.9%` in FY `2023` to `43.6%` in FY `2025` and `43.1%` in H1 `2026`. The status is `ancillary-matting-margin-bridge-visible`, not product-category margin bridge or ROIC proof.

The URI specialty category source-boundary pass now adds `23` rows. It gives CTCS-014 category-mix evidence without overpromoting category economics: FY `2025` equipment-rental revenue by fleet type was Power/HVAC `11%`, Fluid Solutions `7%`, Trench Safety `5%`, Mobile Storage/modular `3%`, and Surface Protection Mats `4%`, up from `2%` in FY `2024`. The named Specialty fleet-type sum rose from `28%` to `30%` of equipment-rental revenue. This is `specialty-category-mix-visible`, not category margin, OEC, capex, utilization, or ROIC proof.

The URI fleet-type revenue estimate pass now adds `33` rows. It translates category mix into approximate dollar scale: FY `2025` Power/HVAC was about `1.519B USD`, Fluid Solutions `0.966B USD`, Trench Safety `0.690B USD`, Mobile Storage/modular `0.414B USD`, and Surface Protection Mats `0.552B USD`. Named Specialty fleet-type estimates sum to about `4.142B USD`, up `0.494B USD` from FY `2024`. This helps size the categories while staying below source-stated product-line revenue, category margin, category OEC, capex, utilization, or ROIC.

The URI category economics matrix pass now adds `20` rows. It turns the remaining URI Specialty work into a category-by-category gap table: revenue scale is visible for the five named Specialty categories, Matting has qualitative productivity and margin-pressure commentary, but category margin, category OEC, category capex, category utilization, and category ROIC are all still not disclosed. The status is `category-economics-matrix-visible`, not category-unit-economics proof.

The URI Yak/Matting acquisition economics pass now adds `25` rows. It gives Matting real acquisition-level numbers: Yak had `353M USD` of 2023 adjusted revenue, `171M USD` of adjusted EBITDA, about `600,000` mats, a `1.100B USD` base purchase price, `1.158B USD` acquisition-date fair value, `127M USD` of acquired rental-equipment fair value, and `828M USD` of goodwill assigned to Specialty. The acquisition was funded with senior notes and ABL drawings. This moves Matting to `yak-acquisition-economics-visible`, while still below ongoing category margin, OEC, capex, utilization, or ROIC.

The URI Yak acquisition funding-chain pass now adds `21` rows. It makes the financing chain explicit: `1.100B USD` of `6 1/8%` senior notes plus ABL drawings funded the acquisition and related fees, the notes equaled `100.0%` of the base purchase price and about `95.0%` of acquisition-date fair value, and ABL balances provide public context without proving the exact Yak draw. This is `yak-acquisition-funding-chain-visible`, not purchase-level source-and-use or ABL allocation proof.

The URI Yak senior-note terms pass now adds `25` rows. It makes the debt instrument itself term-visible: `1.100B USD` of `6.125%` Senior Notes due March `15`, `2034`, estimated net proceeds of `1.090B USD`, senior unsecured guarantees, Truist Bank as trustee, semiannual interest, optional redemption beginning March `15`, `2029`, equity-claw capacity, change-of-control language, and a Yak-specific special mandatory redemption if the acquisition failed to close. This is `yak-senior-note-terms-visible`, not investor allocation or exact ABL allocation proof.

The URI Yak rating context pass now adds `12` rows. S&P headline metadata gives outside credit-market context: the proposed `1.100B USD` senior unsecured notes due `2034` were rated `BB+` with Recovery `4`, an average recovery range of `30%-50%`, and rounded recovery estimate of `35%`. This is `rating-headline-visible`, not full rating rationale, multi-agency confirmation, investor allocation, spread/yield, exact ABL allocation, or Matting ROIC proof.

The URI Yak initial-purchaser source-boundary pass now adds `11` rows. Cravath represented the initial purchasers in the `1.100B USD` high-yield senior notes offering, the transaction closed on March `11`, `2024`, URI described the offering as Rule `144A` / Regulation `S`, and estimated net proceeds of `1.090B USD` were after initial purchasers' discounts, commissions, and estimated fees/expenses. This is `initial-purchaser-role-visible`, not named initial purchasers, investor allocation, pricing spread/yield, exact ABL allocation, or Matting ROIC proof.

The URI Yak bond identifier and market-data boundary pass now adds `17` rows. The SEC indenture gives CUSIPs `911365BR4` and `U91139AK8` and ISINs `US911365BR47` and `USU91139AK85`; public bond-reference pages add FIGI/ticker lookup evidence; Public.com showed a current retail quote snapshot of price `101.97` and yield `5.71%`; and Schwab's SCYB holdings page showed a later `2.225M` face-amount position in CUSIP `911365BR4` as of August `21`, `2026`. This is `bond-identifier-and-market-data-boundary-visible`, not named initial purchasers, original investor allocation, institutional spread tape, exact ABL allocation, or Matting ROIC proof.

The URI Yak public holder crosswalk pass now adds `9` rows. Public ETF/fund/portfolio sources show later positions in CUSIP `911365BR4` / ISIN `US911365BR47` across Schwab `SCYB`, Pacer `PTBD`, Columbia Threadneedle, Fidelity Strategic Advisers, and Federated Core Trust High Yield Bond Portfolio. The captured face/quantity rows total `2.895M USD` face, and the captured value rows total about `4.829041M USD`. This is `later-public-holder-crosswalk-visible`, not original initial purchasers, full holder base, original allocation, institutional spread tape, exact ABL allocation, or Matting ROIC proof.

The URI Yak expanded public holder crosswalk pass now adds `9` rows. Re-opened SEC EDGAR, Natixis/Loomis, Loomis Sayles Global Allocation, and Invesco composition sources show additional later rows for the `6.125%` URI note due March `15`, `2034`. The captured face rows total `43.130M USD` face, and the captured value rows total `44.708177M USD`, with one additional Invesco row showing `0.13%` portfolio weight. This is `expanded-later-public-holder-crosswalk-visible`, not a deduped holder base, original investor allocation, named initial purchasers, institutional spread tape, exact ABL allocation, or Matting ROIC proof.

The URI Yak holder schedule extractor pass now adds `9` candidate rows plus `9` dedupe-scope summary rows. A local extractor recovered United Rentals North America `6.125%` note due March `15`, `2034` rows across American Beacon, Capital Group, Federated Hermes, Fidelity, Jackson, Loomis Sayles, Venerable, and Western Asset sources, extracting a grouped `14.942000M USD` face and `15.018985M USD` value from local HTML, rendered N-PORT, and raw N-PORT XML schedules with source URL, period, CIK, accession, manager-family, fund/vehicle, dedupe-scope, and dedupe-key fields. This is `holder-schedule-dedupe-summary-expanded`, meaning the holder-discovery process is repeatable and has a multi-source grouped output, but it is not a full holder base, deduped manager-family exposure table, original allocation, or pricing tape.

The URI Yak original-pricing source-boundary pass now adds `11` rows. It keeps the original pricing claim honest: coupon, principal, maturity, estimated net proceeds, identifiers, carrying amount, current quote, and later holder marks are visible, but original issue price, original yield, benchmark spread, TRACE issuance tape, offering memorandum, purchase agreement, and pricing supplement were not located. This is `original-pricing-source-boundary-visible`, not original-issue-yield, original-spread, institutional-pricing-tape, named-initial-purchaser, exact ABL allocation, or Matting ROIC proof.

The first funding-type hypothesis map now adds `10` rows explaining why different funding containers may fit different asset types. The working model is `funding type follows asset type`: ET's diversified network can support corporate revolver/commercial-paper/note funding; Cheniere's contracted LNG entities can support entity debt; URI's reusable fleet and receivables can support ABL and securitization; Sterling's backlog/acquisition platform can support a flexible secured revolver; utilities may fund rate-base assets through debt/equity with customer recovery; and contractors may execute customer-funded capital projects while financing working-capital timing. This is hypothesis-grade, not proof-grade: every row includes proof metrics and disproof tests.

The first Sterling agreement-term extraction pass now adds `20` rows from the actual July `2026` Exhibit `10.1` Second Amended and Restated Credit Agreement. Sterling is now `agreement-term-visible` for its credit wrapper: the agreement shows `1.500B USD` revolving commitments, July `2`, `2031` termination date, reborrowable revolving loans, `600M USD` L/C sublimit, `50M USD` swing-line sublimit, SOFR/L/C margins from `1.25%` to `2.00%`, base-rate margins from `0.25%` to `1.00%`, commitment fees from `0.15%` to `0.25%`, broad use-of-proceeds language for refinancing, capex, working capital, permitted acquisitions, general corporate purposes, and existing term-loan prepayment, a `500M USD`/`100%` EBITDA base incremental amount, maximum Total Net Leverage Ratio of `3.50x`, acquisition holiday up to `4.00x`, minimum Interest Coverage Ratio of `3.00x`, subsidiary guarantees, broad personal-property collateral, and Project Specific JV exclusions/investment limits. This supports the funding-container hypothesis for Sterling, but it still does not prove customer-funded backlog, project-level source-of-funds, collateral value, actual availability, draw history, or project returns.

The first Sterling backlog/customer-funding pass now adds `22` rows that test why Sterling's funding type differs from ET, Cheniere, URI, and utilities. Q2 `2026` contract liabilities were `802.601M USD` versus `156.295M USD` of contract assets, creating a `646.306M USD` net contract-liability position and a `5.1x` contract-liability-to-contract-asset ratio. Sterling also had `4.3336B USD` of backlog, `1.28B USD` of unsigned awards, `5.62B USD` of combined backlog, `1.4B USD` of future-phase opportunities, and H1 operating cash flow less capex of `258.375M USD`. This strengthens the explanation that Sterling is a customer-project execution and acquisition platform whose funding need is timing, bonding/L/C support, working capital, capex, and acquisition flexibility. It still does not prove every backlog dollar is funded, signed, margin-accretive, non-cancellable, or tied to a named project-owner source of funds.

The first Sterling funded-backlog and covenant-cushion pass now adds `22` rows that test whether the credit wrapper looks structurally explainable and directionally roomy. The new facility's L/C sublimit is `600.0M USD`, up `8.0x` from the old `75.0M USD` L/C sublimit; total revolver capacity rose `10.0x` from `150.0M USD` to `1.500B USD`; L/C capacity equals `40.0%` of the new revolver; and filings describe bid bonds generally at `5%` to `10%` of bid amount plus performance/payment bonds up to `100%` of construction cost on some contracts. Q2 `2026` total debt was `285.305M USD`, cash was `464.451M USD`, and total debt was only about `0.32x` the FY `2026` adjusted EBITDA guide midpoint of `903.5M USD`, which is directionally far below the `3.50x` standard leverage ceiling. This is not a formal covenant calculation and does not disclose actual post-reset L/C usage, bonded backlog, or compliance-certificate cushion.

The Sterling eight-quarter contract-capital conversion pass now adds `8` rows from Q3 `2024` through Q2 `2026`. RPO rose about `106.0%`, from `2.055081B USD` to `4.233618B USD`; net contract-liability timing rose from `483.795M USD` to `646.306M USD`; quarterly operating cash flow less capex stayed positive in every period; and debt/RPO fell from `15.8%` to `6.7%`. This moves the Sterling claim from single-quarter evidence toward durability evidence, but CTCS-014 still cannot become full project-and-cash-grade until organic/acquired backlog, L/C and surety usage, customer source-of-funds, project margins, and cancellation/conversion history are extracted.

The Sterling acquired-versus-organic backlog pass now adds `18` rows that sharpen the "why" and "how much is organic" question. At Q2 `2026`, CEC and Stone Ridge contributed `1.32B USD` of signed backlog and `1.24B USD` of unsigned awards, or `2.56B USD` of signed-plus-unsigned contribution against `5.62B USD` of combined backlog. The derived non-acquired proxy was about `3.0136B USD` of signed backlog but only about `40.0M USD` of unsigned awards. This keeps the promoted claim honest: Sterling's growth is both organic and acquisition-enabled, and unsigned awards are the weakest and most acquisition-linked bucket.

The Sterling L/C and surety usage boundary pass now adds `19` rows that explain why the funding wrapper needs guarantee capacity while keeping actual usage unpromoted. The new `600.0M USD` L/C sublimit is `8.0x` the old limit and equals `40.0%` of the `1.5B USD` revolver. The agreement defines L/C obligations, `103.0%` cash collateralization mechanics, bonding agreements, and contingent-obligation treatment. The filings show bid, performance, payment, and maintenance-bond requirements plus Travelers surety support, but actual post-reset L/C outstanding and bonded backlog remain missing.

## How To Use This Dashboard

Use this page as the decision layer.

Before writing any broad thesis sentence, find the matching row and ask:

1. Is the status only `queued` or `announced`?
2. Is the evidence company-source only, or externally denominator-tested?
3. Does the claim require legal approval, financing proof, or in-service proof?
4. What is the disproof test?
5. What exact source would move the row one status higher?

## Bottom Line

The current picture is:

`Private-credit and insurance-linked credit channels are the most advanced on financing proof. Power/grid is quickly moving from company-source proof into regulatory and project proof. Debt refinancing, acquisition finance, asset-backed finance, and capital-intensive buildout now have first-pass filed ledgers, but still need agreement, collateral, project, cash-conversion, and outside-denominator proof.`

The next objective is not to make the thesis bigger. It is to move more rows upward:

`queued -> filed -> approved -> financed -> under construction -> in service -> trend-proven -> thesis-grade`
