# Capital Flow Capital-Intensive Energy Project Denominator Pass 1

## Purpose

This pass starts executing the project-denominator workbench for the capital-intensive energy subthemes.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-energy-project-denominator-pass-1.csv`

The core question is:

`Do external government records confirm that ET and Cheniere are showing up in real physical export systems, not just company narratives?`

## What Was Added

| Item | Count |
|---|---:|
| Denominator rows | `14` |
| Energy Transfer rows | `6` |
| Cheniere rows | `8` |
| Official external source families | `2` |
| Cached federal workbook files | `5` |

## Sources Used

| Source family | Use in this pass |
|---|---|
| EIA petroleum export tables | U.S. HGL, ethane, and propane export denominators for ET's NGL/export-capacity subtheme. |
| DOE Natural Gas Imports and Exports Monthly | Cargo-level LNG export rows by vessel, export point, country, docket, and volume for Cheniere's Sabine Pass and Corpus Christi terminals. |
| Company SEC/source-table passes | The company-source anchors for capex, capacity additions, cargoes, contracts, debt, and funding mix. |

Cached local files:

- `raw/primary-sources/capital-flow/market-denominators/eia/us-ethane-exports-mbpd-monthly.xls`
- `raw/primary-sources/capital-flow/market-denominators/eia/us-propane-exports-mbpd-monthly.xls`
- `raw/primary-sources/capital-flow/market-denominators/eia/us-hgl-exports-mbpd-monthly.xls`
- `raw/primary-sources/capital-flow/market-denominators/doe-lng/us-lng-exports-reexports-details-jan-2016-jun-2026.xlsx`
- `raw/primary-sources/capital-flow/market-denominators/doe-lng/us-natural-gas-imports-exports-summary-jan-2000-jun-2026.xlsx`

## Energy Transfer: NGL Logistics Bottleneck Relief

The ET subtheme is now more concrete:

`ET is not just an energy company in this lane. It is a capital-intensive NGL logistics and export-capacity case.`

Company-source anchors:

- Nederland expansion capacity: `240000 bpd` ethane plus `55000 bpd` LPG
- Lone Star Express incremental takeaway: more than `90000 bpd`
- long-term y-grade transportation/fractionation agreements: about `300000 bpd`
- FY `2025` growth capex: `5.250B USD`
- FY `2026` growth-capex guide: `5.6B-5.9B USD`
- Q2 `2026` NGL exports up `25%` year over year
- Q2 `2026` NGL transportation volumes up `13%` year over year

External denominator evidence:

| Metric | External value | Period | Interpretation |
|---|---:|---|---|
| U.S. ethane exports | `717 kbpd` | May `2026` | Supports the direction of ethane export-capacity expansion. |
| U.S. ethane exports | `579.7 kbpd` average | FY `2025` | Sizes the `240000 bpd` Nederland ethane capacity addition at about `41%` of the 2025 average U.S. export run rate. |
| U.S. propane exports | `1938.2 kbpd` average | Jan-May `2026` | LPG proxy remains high and was up `7.8%` versus Jan-May `2025`. |
| U.S. HGL exports | `3776 kbpd` | May `2026` | Broad NGL/HGL export denominator remains multi-million-barrel-per-day scale. |
| U.S. HGL exports | `3109.6 kbpd` average | FY `2025` | Context for the size of ET's `90000 bpd` Lone Star increment. |

What this lets us say:

`ET's growth-capex and project-capacity story is directionally supported by external export denominators. U.S. ethane, propane, and HGL export markets are large enough, and in visible periods strong enough, to make the bottleneck-relief thesis plausible.`

What it does not let us say:

`The EIA national series do not prove Nederland utilization, Lone Star fill rate, project returns, customer economics, debt use of proceeds, or ET-specific market share.`

The next ET proof layer is narrower:

- PADD 3 or export-district product exports
- Permian/NGL production or movement proxies
- Nederland and Lone Star in-service/project records
- project-level capex allocation
- debt issuance, revolver, maturity, and use-of-proceeds evidence

## Cheniere: LNG Capacity Conversion Into Cargoes

The Cheniere subtheme is now more concrete:

`Cheniere is a contracted LNG capacity-conversion case: capital is funding liquefaction trains and related infrastructure that show up as physical cargoes from Sabine Pass and Corpus Christi.`

Company-source anchors:

- FY `2025` cargoes: `670`
- FY `2025` exported volume: `2424 TBtu`
- Q2 `2026` cargoes: `184`
- H1 `2026` cargoes: `371`
- about `90%` of anticipated SPL/CCL production contracted
- weighted-average remaining contract life around `15` years
- FY `2025` growth capital: `2.6B USD`
- FY `2025` total debt: `23.0B USD`
- Train 6 substantial completion in June `2026`
- Train 7 expected in fall `2026`

External denominator evidence from DOE:

| Metric | External value | Period | Interpretation |
|---|---:|---|---|
| Sabine Pass plus Corpus Christi vessel export rows | `674` cargoes | FY `2025` | Closely reconciles to Cheniere's `670` reported FY cargoes. |
| Sabine Pass plus Corpus Christi vessel export volume | `2316499 MMCF` | FY `2025` | Gives a physical terminal-volume base behind the cargo count. |
| Sabine Pass plus Corpus Christi vessel export rows | `184` cargoes | Q2 `2026` | Exactly matches Cheniere's reported Q2 cargo count. |
| Sabine Pass plus Corpus Christi vessel export rows | `374` cargoes | H1 `2026` | Close to Cheniere's `371` reported H1 cargoes; requires cargo-level reconciliation. |
| Sabine Pass plus Corpus Christi vessel export volume | `640991.63 MMCF` | Q2 `2026` | Physical export volume behind the Q2 cargo count. |
| Cheniere terminal share of U.S. vessel LNG export volume | `40.7%` | June `2026` | Cheniere remains a large piece of the U.S. LNG export denominator. |
| Corpus Christi vessel export volume | `265627.13 MMCF` | Q2 `2026` | Physical terminal output is visible while CCL train progress is being reported. |

What this lets us say:

`Cheniere's company-reported cargo counts are externally visible in DOE cargo-level export records. The strongest check is Q2 2026, where DOE vessel rows for Sabine Pass and Corpus Christi equal the company's 184 reported cargoes.`

What it does not let us say:

`DOE cargo rows do not prove train-level economics, SPA pricing, debt-service coverage, DCF quality, or which exact train produced which cargo.`

The next Cheniere proof layer is narrower:

- cargo-level tanker/date reconciliation
- TBtu-to-MMCF conversion bridge
- destination and docket mapping
- FERC train construction/status records
- SPL/CQP/CCH debt and maturity tables
- SPA volume/duration mapping without assuming undisclosed price terms

## Subthemes Now Visible

| Subtheme | Company | What is being funded | What external data now confirms | Still missing |
|---|---|---|---|---|
| NGL export capacity | ET | Ethane/LPG export loading, docks, pipes, refrigeration, terminal expansion | U.S. ethane/propane/HGL export denominator is large and visibly active. | ET-specific utilization, project cost, customer economics. |
| Permian NGL takeaway | ET | Pipeline/fractionation/y-grade logistics | National HGL denominator supports broad product-flow scale. | Permian-specific movements and Lone Star fill rate. |
| LNG cargo throughput | Cheniere | Liquefaction trains and terminal operations | DOE vessel rows reconcile closely to Cheniere cargo disclosures. | Cargo-level definition differences and heat-content bridge. |
| LNG construction | Cheniere | Corpus Christi Stage 3 and midscale trains | Corpus Christi export volume is visible during the construction-progress period. | Train-specific FERC status and in-service records. |
| Funding stack | ET and Cheniere | Growth capex, revolvers, project debt, parent/entity debt | External physical denominators show assets are tied to real export systems. | Use-of-proceeds, entity-level waterfalls, and project returns. |

## Simple Bottom Line

In simple words:

`Capital is going into the pipes, docks, trains, tanks, and logistics systems that let U.S. hydrocarbons reach global customers. ET is mostly the NGL logistics bottleneck case. Cheniere is the LNG cargo-conversion case. The outside data now confirms the physical export systems are real and measurable, especially for Cheniere cargoes. The remaining hard question is whether the project-level money is earning attractive returns and exactly how the funding stack supports each project.`

## Claim Status

This pass improves CTCS-014, but it should still stay below full `project-and-cash-grade`.

Promote only this narrower claim:

`For ET and Cheniere, source-backed company capex/capacity/cargo claims now have first-pass external physical denominator support from EIA and DOE data.`

Do not promote this broader claim yet:

`Every dollar of growth capex is proven project-return capital with fully known source-of-funds.`

## Next Pass

The next useful pass is:

`capital-flow-capital-intensive-industrial-denominator-pass-1.md`

That should do for URI and Sterling what this pass does for ET and Cheniere:

- URI: rental market size, fleet OEC, utilization/rate/productivity, ABL/securitization and cash conversion
- Sterling: Census construction spending, manufacturing/data-center project denominators, backlog conversion, contract assets/liabilities, and acquisition contribution
