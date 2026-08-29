# Capital Flow Capital-Intensive Energy Source-Table Extraction Pass 1

## Purpose

This pass deepens the capital-intensive buildout work for the energy infrastructure subtheme.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-energy-source-table-extraction-pass-1.csv`

The question is:

`When capital flows into energy infrastructure, can we tie the dollars to cash generation, physical capacity, throughput, contracted demand, project timing, and funding evidence?`

## Source Families Restored

| Company | Source Family | Local Source Files | Status |
|---|---|---|---|
| Energy Transfer | Q2 `2026` SEC 10-Q, 8-K, and earnings-release exhibit | `raw/sec/energy/oil-gas-pipelines/energy-transfer-lp/2026-q2-10q.html`; `raw/sec/energy/oil-gas-pipelines/energy-transfer-lp/2026-q2-8k.html`; `raw/sec/energy/oil-gas-pipelines/energy-transfer-lp/2026-q2-ex99-earnings-release.html` | `source-table-extracted` |
| Cheniere | Q2 `2026` SEC 10-Q, 8-K, and earnings-release exhibit | `raw/sec/energy/oil-gas-pipelines/cheniere-energy-inc/2026-q2-10q.html`; `raw/sec/energy/oil-gas-pipelines/cheniere-energy-inc/2026-q2-8k.html`; `raw/sec/energy/oil-gas-pipelines/cheniere-energy-inc/2026-q2-ex99-earnings-release.html` | `source-table-extracted` |

## Extraction Summary

| Item | Count |
|---|---:|
| Extraction rows | `24` |
| Energy Transfer rows | `13` |
| Cheniere rows | `11` |
| Companies | `2` |
| Source families | `2` |
| Source files used | `4` |
| Linked manifest rows upgraded | `CIPSM-001`, `CIPSM-003` |

## Energy Subthemes

### 1. Midstream Cash Generation

Energy Transfer gives the clearest midstream cash-generation example.

The Q2 `2026` release supports:

- adjusted EBITDA of `5.07B USD`
- DCF attributable to partners, as adjusted, of `2.59B USD`
- full-year adjusted EBITDA guidance raised to `18.8B-19.1B USD`

Simple claim:

`Energy Transfer is not just announcing projects. It is generating current cash while funding growth capex.`

Boundary:

`Adjusted EBITDA and DCF are company-level metrics. They do not prove individual project returns.`

### 2. Growth Versus Maintenance Capex

Energy Transfer is useful because the release separates expansion spend from sustaining spend.

The Q2 `2026` source supports:

- Q2 growth capex of `1.10B USD`
- Q2 maintenance capex of `307M USD`
- FY `2026` growth-capex guidance of `5.6B-5.9B USD`

Simple claim:

`A large part of the visible capital flow is expansion capital, not only keeping old assets running.`

Boundary:

`The Q2 release does not allocate the entire 1.10B USD to named assets, so the project-level capital bridge still needs the 10-Q and project schedule.`

### 3. NGL Export And Permian Takeaway Capacity

The ET subtheme is not generic energy. It is mostly export-linked NGL logistics and Permian takeaway.

The source supports:

- NGL transportation volumes up `13%` year over year
- NGL exports up `25%` year over year
- Nederland ethane export capacity addition of `240000 bpd`
- Nederland LPG capacity addition of `55000 bpd`
- Lone Star Express incremental Permian NGL takeaway capacity of more than `90000 bpd`
- long-term transportation/fractionation agreements for about `300000 bpd` on y-grade assets extending into the `2030s`

Simple claim:

`The money is going into pipes, docks, refrigeration, fractionation, and export capacity that turns Permian production into contracted Gulf Coast logistics volume.`

Boundary:

`Capacity, subscriptions, and contract volume are stronger than narrative demand, but they still need customer names, pricing, minimum-volume terms, project cost, and return evidence.`

### 4. LNG Train Completion And Cargo Throughput

Cheniere gives the cleanest LNG conversion example: liquefaction capacity becomes cargoes, EBITDA, and DCF.

The Q2 `2026` source supports:

- revenue of `5.73B USD`
- consolidated adjusted EBITDA of `1.80B USD`
- DCF of `1.17B USD`
- `184` LNG cargoes exported in Q2
- `371` LNG cargoes exported in H1
- FY `2026` production forecast tightened upward to `53-54 mtpa`
- Corpus Christi Stage 3 Midscale Train 6 reached substantial completion in June `2026`
- Midscale Train 7 first LNG expected imminently and substantial completion expected in fall `2026`

Simple claim:

`Cheniere shows the conversion chain from construction to liquefaction capacity to cargo throughput to cash generation.`

Boundary:

`Cargo count and company-level DCF do not prove train-level project return without contract mix, debt service, capacity payments, and project cost.`

### 5. Capital Deployment And Funding Mix

Cheniere also gives a funding/subtheme bridge.

The Q2 `2026` release supports:

- capital deployed under the capital allocation plan of `884M USD` in Q2 and `2.1B USD` in H1
- Q2 growth capital invested of about `1.1B USD`
- Q2 equity-funded growth capital of about `219M USD`
- H1 growth capital invested of about `2.1B USD`
- H1 equity-funded growth capital of about `520M USD`
- H1 consolidated long-term debt repayment of about `253M USD`
- long-term debt of `22.632B USD` at June 30 `2026` in the 10-Q

Simple claim:

`The funding story is mixed: Cheniere is funding growth, returning capital, repaying debt, and carrying a large project-finance-heavy debt base at the same time.`

Boundary:

`The capital-deployment total mixes buybacks, dividends, growth capex, and debt repayment. It should not be treated as pure infrastructure investment.`

### 6. Project Maturity

The two companies sit at different points in the physical-buildout chain.

| Company | Project Evidence | Status Read |
|---|---|---|
| Energy Transfer | Nederland expansion announced and fully subscribed; Lone Star Express upgrades completed; y-grade agreements signed into the `2030s` | `contracted-capacity` and partial `in-service-capacity` |
| Cheniere | Midscale Train 6 substantially complete; Train 7 moving from commissioning toward fall `2026` substantial completion; CCL Trains 8 and 9 under construction | `in-service-milestone` and `under-construction` |

Simple claim:

`Energy Transfer currently reads as logistics-capacity expansion backed by throughput and contracts. Cheniere reads as liquefaction-capacity conversion backed by train milestones and cargoes.`

Boundary:

`Neither company is yet fully project-and-cash-grade in this research system until project cost, debt facility, customer contract, capacity, operating output, and cash conversion are reconciled in one row.`

## What This Adds To The Big Picture

The capital-intensive buildout theme now has a stronger energy spine.

Before this pass, the energy rows were mostly packet-grade:

`high-signal company + named projects + headline capex/cash metrics`

After this pass, they are closer to primary-source project/cash evidence:

`SEC source family + exact metric label + value + subtheme + safe claim + boundary + next source`

The emerging message is:

`Capital is flowing into energy infrastructure where physical bottlenecks are visible: LNG trains, NGL export terminals, pipeline takeaway, docks, refrigeration, fractionation, and contracted logistics capacity. The strongest evidence is when the same source family shows capex, operating throughput, contracts, liquidity/debt, and cash generation in the same reporting window.`

## Claims Promoted

| Claim | Status After This Pass | Why |
|---|---|---|
| ET is funding energy-infrastructure growth capex | `source-table-supported` | Q2 growth capex, maintenance capex, FY growth-capex guide, EBITDA, DCF, liquidity, and debt context are extracted. |
| ET NGL export/takeaway buildout is tied to physical capacity | `source-table-supported` | Nederland, Lone Star Express, and y-grade contracted-capacity metrics are extracted. |
| Cheniere LNG expansion is converting into operating capacity | `source-table-supported` | Train 6 substantial completion, Train 7 timing, CCL Stage 3 capacity status, and cargo counts are extracted. |
| Cheniere funding mix is observable but not simple | `source-table-supported-with-boundary` | Growth capex, equity funding, capital return, debt repayment, and long-term debt are visible but mixed. |

## Claims Not Yet Promoted

| Claim | Why Not Yet |
|---|---|
| ET projects are individually high-return | Need project cost, tariff/contract economics, utilization, and incremental EBITDA. |
| Cheniere each-train economics are proven | Need train-level capex, SPA mix, debt service, and capacity payment mapping. |
| Energy infrastructure capital flow is thesis-grade across the sector | Need annual/Q4 baselines, peer rows, outside denominators, and repeated-period tracking. |
| Private credit or insurance capital directly funded these named energy projects | Need lender/facility source-of-funds proof. Current rows prove company/project funding context, not ultimate capital source. |

## Next Extraction Pass

The next energy pass should extract:

- ET annual/Q4 `2025` baseline capex, EBITDA, DCF, debt maturity, and Lake Charles LNG language
- Cheniere FY/Q4 `2025` baseline capacity, cargo, capital allocation, and debt/project-finance tables
- project-level cost schedules for Nederland, Lone Star Express, CCL Stage 3, CCL Trains 8/9, and SPL Expansion Phase 1
- contract/customer evidence where public
- outside denominator checks for U.S. LNG export capacity, NGL export capacity, Gulf Coast fractionation, and Permian takeaway
