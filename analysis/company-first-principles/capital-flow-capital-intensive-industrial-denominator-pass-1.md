# Capital Flow Capital-Intensive Industrial Denominator Pass 1

## Purpose

This pass starts executing the industrial side of the project-denominator workbench for United Rentals and Sterling Infrastructure.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-industrial-denominator-pass-1.csv`

The core question is:

`Do outside market, construction, and services denominators support the source-backed company story, or are URI and Sterling isolated company wins?`

## What Was Added

| Item | Count |
|---|---:|
| Industrial denominator rows | `16` |
| United Rentals rows | `6` |
| Sterling rows | `10` |
| Official external source families | `3` |
| Processed Census-derived source families | `1` |
| Cached denominator files | `8` |

## Sources Used

| Source family | Use in this pass |
|---|---|
| Census Quarterly Services Survey via FRED | URI broad machinery/equipment rental revenue denominator. |
| BEA private fixed investment via FRED | URI construction-machinery investment denominator. |
| Census construction spending via FRED and Census release | Sterling nonresidential, manufacturing, office, communication, and total construction denominators. |
| OWID processed Census/BLS data-center construction series | Data-center construction subtheme sizing where raw Census data-center subcategory is not yet cached. |
| Company SEC filings and exhibits | Company anchors for URI fleet capex/OEC/cash conversion and Sterling backlog/acquisition/funding/cash conversion. |

Cached local files:

- `raw/primary-sources/capital-flow/market-denominators/fred/rev5324taxabl144qnsa.csv`
- `raw/primary-sources/capital-flow/market-denominators/fred/c269rc1a027nbea.csv`
- `raw/primary-sources/capital-flow/market-denominators/fred/tlmfgcons.csv`
- `raw/primary-sources/capital-flow/market-denominators/fred/tlnrescons.csv`
- `raw/primary-sources/capital-flow/market-denominators/fred/pnrescons.csv`
- `raw/primary-sources/capital-flow/market-denominators/fred/tlofcons.csv`
- `raw/primary-sources/capital-flow/market-denominators/fred/prcmucons.csv`
- `raw/primary-sources/capital-flow/market-denominators/census-construction/monthly-spending-data-center-us-owid-census-derived.csv`

## United Rentals: Fleet-Access Capital Absorption

URI's subtheme is:

`Customers want access to heavy project capacity without owning every asset. URI absorbs the fleet capital, manages utilization, rents the fleet, sells older equipment, and converts the system into cash.`

Company-source anchors:

- FY `2025` revenue: `16.099B USD`
- FY `2025` gross rental capex: `4.189B USD`
- FY `2025` rental-equipment purchases: `4.149B USD`
- FY `2025` rental-equipment sale proceeds: `1.413B USD`
- FY `2025` net rental capex: `2.736B USD`
- FY `2025` fleet OEC: `22.48B USD`
- FY `2025` equipment units: `1.095M`
- FY `2025` fleet age: `49.5` months
- FY `2025` operating cash flow: `5.190B USD`
- FY `2025` free cash flow: `2.181B USD`
- Q2 `2026` OEC: `23.8B USD`
- H1 `2026` gross rental capex: `2.931B USD`

External denominator evidence:

| Metric | External value | Period | Interpretation |
|---|---:|---|---|
| NAICS `5324` machinery/equipment rental and leasing revenue | `27471M USD` | Q1 `2026` | Broad rental-services denominator, up `6.8%` versus Q1 `2025`. |
| NAICS `5324` trailing-four-quarter revenue | `115007M USD` | Q2 `2025`-Q1 `2026` | URI FY `2025` revenue is about `14.0%` of this broad denominator. |
| U.S. private fixed investment in construction machinery | `64.723B USD` | `2025` | URI FY `2025` gross rental capex is about `6.5%` of this economy-wide construction-machinery investment denominator. |
| URI H1 `2026` gross rental capex versus guide midpoint | `65.1%` | H1 `2026` | URI had already spent about two-thirds of the `4.5B USD` midpoint of its 2026 gross-rental-capex guide by midyear. |

What this lets us say:

`URI is not just a company with a big capex number. It is a large fleet-capital platform inside a measurable machinery/equipment rental market. The outside denominators support the idea that rental access is a real capital-flow lane, while URI's own filings show the fleet spend is paired with OEC, productivity, cash flow, leverage, and liquidity metrics.`

What it does not let us say:

`The external denominators do not prove marginal fleet returns, utilization by asset class, specialty mix economics, customer project exposure, or asset-backed funding.`

The next URI proof layer is narrower:

- OEC by general rental versus specialty
- utilization, rate, mix, and fleet-productivity bridge
- used-equipment margin and recovery
- debt maturity table and facility capacity
- peer comparison against Ashtead/Sunbelt, Herc, and other rental platforms
- QSS update for Q2 `2026` detailed NAICS `5324`

## Sterling: Customer-Project Execution And Backlog Conversion

Sterling's subtheme is different:

`Sterling is not primarily absorbing capital on its own balance sheet. It is converting customer-funded construction demand into backlog, signed work, future-phase visibility, field execution, and cash.`

Company-source anchors:

- FY `2025` revenue: `2.49B USD`
- FY `2025` adjusted EBITDA: `503.8M USD`
- FY `2025` operating cash flow: `439.988M USD`
- FY `2025` capex: `77.3M USD`
- FY `2025` signed backlog: `3.01B USD`
- FY `2025` combined backlog: `3.31B USD`
- FY `2025` future-phase work: more than `1.0B USD`
- Q2 `2026` backlog: `4.33B USD`
- Q2 `2026` combined backlog: `5.62B USD`
- Q2 `2026` future-phase opportunities: `1.4B USD`
- Q2 `2026` visibility to future work: more than `7B USD`
- CEC and Stone Ridge contribution to signed backlog: `1.32B USD`
- CEC and Stone Ridge contribution to unsigned awards: `1.24B USD`
- July `2026` expanded revolver: `1.5B USD`, maturity July `2031`

External denominator evidence:

| Metric | External value | Period | Interpretation |
|---|---:|---|---|
| Total construction spending | `2166.5B USD` SAAR | June `2026` | Huge denominator, but down `3.2%` year over year. |
| Private nonresidential construction | `745339M USD` SAAR | June `2026` | Down `4.7%` year over year, so broad private nonresidential is not uniformly strong. |
| Total nonresidential construction | `1277174M USD` SAAR | June `2026` | Down `2.1%` year over year but roughly flat from January. |
| Manufacturing construction | `172674M USD` SAAR | June `2026` | Still large, but down `21.4%` year over year. |
| Office construction | `132750M USD` SAAR | June `2026` | Up `12.5%` year over year, consistent with data-center strength inside office. |
| Private communication construction | `28401M USD` SAAR | June `2026` | Up `3.2%` year over year, a secondary infrastructure denominator. |
| Private data-center construction | `4.356776304B USD` monthly real dollars | June `2026` | Up `44.3%` year over year; H1 `2026` was about `25.4%` above H1 `2025`. |

What this lets us say:

`Sterling's strong backlog is not simply broad construction beta. The broad construction and manufacturing denominators are weak or mixed, while data-center/office-related construction is strong. That supports a narrower claim: Sterling is levered to selected mission-critical pockets, not to the whole construction market.`

What it does not let us say:

`The denominators do not prove Sterling's specific customer projects are funded, non-cancellable, profitable, or organic. Acquisition contribution is material and must be separated from same-store demand.`

The next Sterling proof layer is narrower:

- signed backlog roll-forward
- unsigned award conversion
- future-phase conversion
- organic versus acquired backlog
- contract assets and liabilities
- project-reserve and working-capital movement
- customer/project evidence for data centers, semiconductor, manufacturing, power, and distribution sites

## The Important Subtheme Split

| Subtheme | Company | What is being funded | What external data now confirms | Still missing |
|---|---|---|---|---|
| Fleet-access capital absorption | URI | Rental fleet, branch logistics, used-equipment recycling, maintenance, fleet availability | Broad machinery/equipment rental revenue and construction-machinery investment are large measurable denominators. | Fleet-level returns, utilization, rate, mix, funding stack. |
| Customer-project execution | Sterling | Site work, electrical/mechanical integration, civil execution, project labor, backlog conversion | Construction denominators show a mixed broad market and a strong data-center pocket. | Project/customer funding, backlog conversion, margins, organic/acquired split. |
| Mission-critical buildout | Sterling | Data centers, semiconductor/manufacturing, power, distribution/warehousing | Data-center construction is growing sharply while manufacturing is weaker. | Which Sterling backlog dollars map to which category. |
| Funding capacity | URI and Sterling | Debt, liquidity, revolvers, operating cash flow | Company filings show cash conversion and funding capacity. | Ultimate source-of-funds and project-level return proof. |

## What We Are Saying Now

In simple words:

`The industrial buildout story has two channels. URI is where capital gets turned into rentable equipment capacity. Sterling is where other people's capital projects become backlog and field execution. The denominators say the broad market is not uniformly booming: construction is mixed, manufacturing construction is down, but data-center-related construction is strong. That makes the best claim narrower and more useful: capital is moving into selected bottleneck pockets, and the winners are companies that can convert those pockets into fleet utilization, backlog, and cash.`

## Claim Status

This pass improves CTCS-014, but it still should remain below full `project-and-cash-grade`.

Promote only this narrower claim:

`URI and Sterling now have first-pass external denominator context: URI against machinery/equipment rental and construction-machinery investment, Sterling against construction-spending categories and data-center construction.`

Do not promote this broader claim yet:

`All URI fleet capex and all Sterling backlog represent fully funded, high-return, organic project capital.`

## Next Pass

The next useful pass is a company-specific conversion pass:

`capital-flow-capital-intensive-industrial-conversion-pass-1.md`

That should extract:

- URI OEC roll-forward, utilization/rate/mix, used-equipment margin, debt maturities, and facility capacity
- Sterling backlog roll-forward, contract assets/liabilities, acquired-versus-organic contribution, project reserves, and customer/project source links
