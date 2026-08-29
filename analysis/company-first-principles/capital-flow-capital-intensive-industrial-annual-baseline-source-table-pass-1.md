# Capital Flow Capital-Intensive Industrial Annual Baseline Source-Table Pass 1

## Purpose

This pass adds the annual/Q4 baseline beneath the United Rentals and Sterling Infrastructure Q2 `2026` source-table extraction.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-industrial-annual-baseline-source-table-pass-1.csv`

The deeper question is:

`Do rental fleet access and specialty construction backlog show durable annual capital absorption, or were the Q2 2026 rows only one-quarter snapshots?`

## Source Families Restored

| Company | Source Family | Local Source Files | Status |
|---|---|---|---|
| United Rentals | FY/Q4 `2025` SEC 10-K, 8-K, and annual-results exhibit | `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-10k.html`; `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q4-8k.html`; `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q4-ex99-earnings-release.html` | `source-table-extracted` |
| Sterling Infrastructure | FY/Q4 `2025` SEC 10-K, 8-K, annual-results exhibit, and presentation exhibit | `raw/sec/industrial-goods/heavy-construction/sterling-infrastructure-inc/2025-10k.html`; `raw/sec/industrial-goods/heavy-construction/sterling-infrastructure-inc/2025-q4-8k.html`; `raw/sec/industrial-goods/heavy-construction/sterling-infrastructure-inc/2025-q4-ex99-earnings-release.html`; `raw/sec/industrial-goods/heavy-construction/sterling-infrastructure-inc/2025-q4-earnings-presentation.html` | `source-table-extracted` |

## Extraction Summary

| Item | Count |
|---|---:|
| Extraction rows | `36` |
| United Rentals rows | `18` |
| Sterling rows | `18` |
| Companies | `2` |
| Source families | `2` |
| Linked manifest rows upgraded | `CIPSM-006`, `CIPSM-008` |

## What Changed

The Q2 priority source-table pass proved:

`URI and STRL have source-backed current-period metrics.`

This annual baseline pass adds:

`URI and STRL have annual evidence that explains whether the current-period rows are part of a larger operating model.`

The industrial subthemes are different:

- United Rentals is a **fleet-access capital absorption** model.
- Sterling is a **specialty-construction backlog and execution capacity** model.

They should not be collapsed into one generic capex/backlog claim.

## United Rentals Subthemes

### 1. Fleet-Access Revenue

United Rentals' annual-results exhibit and 10-K support:

- Q4 `2025` total revenue of `4.208B USD`
- Q4 `2025` rental revenue of `3.581B USD`
- FY `2025` total revenue of `16.099B USD`
- FY `2025` adjusted EBITDA of `7.328B USD`

Simple claim:

`United Rentals turns physical access to equipment into a large recurring rental-revenue base.`

Boundary:

`Rental revenue includes owned rental revenue, re-rent revenue, and ancillary revenue. The source still needs mix and margin detail before we can judge quality.`

### 2. Fleet Capex And Asset Recycling

The annual baseline is now source-backed:

- FY `2025` gross rental capital expenditures of `4.189B USD`
- FY `2025` cash payments for rental-equipment purchases of `4.149B USD`
- FY `2025` proceeds from rental-equipment sales of `1.413B USD`
- FY `2025` net payments for rental capital expenditures of `2.736B USD`

Simple claim:

`United Rentals is one of the cleanest examples of capital being absorbed into real-economy access: dollars go into fleet, fleet is rented, old fleet is sold, and the company tracks gross-to-net capital.`

Boundary:

`Gross rental capex is not the same as net fleet growth, and net capex is not automatically high-return capital. We still need utilization, age, OEC, mix, and maintenance economics tied together.`

### 3. Fleet Scale And Productivity

The FY `2025` 10-K supports:

- fleet OEC of `22.48B USD`
- `1.095M` equipment units
- fleet age of `49.5` months
- FY `2025` fleet productivity growth of `2.2%`
- Q4 `2025` average OEC growth of `4.5%`

Simple claim:

`The fleet-access model has both scale and productivity metrics, so it can be tested more rigorously than a generic capex number.`

Boundary:

`OEC and unit count mix many asset classes. The next proof layer needs fleet type, time utilization, rate, specialty mix, and proceeds recovery.`

### 4. Cash Conversion And Funding

The annual baseline supports:

- FY `2025` operating cash flow of `5.190B USD`
- FY `2025` free cash flow of `2.181B USD`
- year-end net leverage of `1.9x`
- year-end liquidity of `3.322B USD`
- long-term debt of `12.652B USD`
- 2026 gross rental-capex guidance of `4.3B-4.7B USD`

Simple claim:

`URI is not just consuming capital; it is generating cash while maintaining a large fleet and leverage/liquidity discipline.`

Boundary:

`Free cash flow does not prove the marginal fleet dollar is high-return. The next pass needs fleet returns by category and utilization.`

## Sterling Infrastructure Subthemes

### 1. Specialty Construction Revenue And Profitability

Sterling's FY `2025` annual-results exhibit supports:

- FY `2025` revenue of `2.49B USD`
- FY `2025` adjusted EBITDA of `503.8M USD`
- FY `2025` operating cash flow of `439.988M USD`
- FY `2025` capital expenditures of `77.3M USD`

Simple claim:

`Sterling is not a balance-sheet capex absorber like URI. It is a project execution and backlog conversion company with high operating cash generation relative to its own capex.`

Boundary:

`Sterling's customer projects may be capital-intensive even if Sterling's own capex is modest. We need customer/project funding proof to show what external capital is being executed.`

### 2. Signed Backlog, Combined Backlog, And Future Phases

Sterling's annual baseline supports:

- signed backlog of `3.01B USD`
- CEC contribution to signed backlog of `488.9M USD`
- combined backlog of `3.31B USD`
- unsigned awards of `300.7M USD`
- CEC contribution to unsigned awards of `226.4M USD`
- more than `1.0B USD` of high-probability future-phase work
- a visibility pool approaching `4.5B USD`

Simple claim:

`Sterling's source-backed evidence is mostly visibility into future work, not capex on its own balance sheet.`

Boundary:

`Signed backlog, unsigned awards, combined backlog, and future-phase work are different evidence levels. The visibility pool should not be counted as funded backlog.`

### 3. Mission-Critical E-Infrastructure

Sterling's sources support a clear segment shift:

- Q4 `2025` E-Infrastructure Solutions revenue growth of `123%`
- legacy site-development revenue growth excluding CEC of `67%`
- E-Infrastructure work shifting toward large mission-critical projects
- FY `2025` E-Infrastructure revenue of `1.466777B USD`
- FY `2025` E-Infrastructure operating income of `346.041M USD`

Simple claim:

`Sterling is increasingly a mission-critical site-development/electrical/mechanical execution platform for data centers, semiconductor fabrication, manufacturing, distribution, warehousing, and power generation.`

Boundary:

`Mission-critical exposure is not automatically AI/datacenter purity. The next pass needs project/customer categories and signed/funded status.`

### 4. Acquisition-Enabled Capacity

The 10-K says Sterling acquired CEC Facilities Group on September 1 `2025` for `562M USD`, consisting primarily of `443M USD` cash and `79M USD` common stock, with an earn-out opportunity up to `80M USD`.

Simple claim:

`Part of Sterling's buildout exposure was bought through acquisition, not generated organically.`

Boundary:

`CEC contribution must be separated from same-store demand. Otherwise acquisition capital can be mistaken for organic market acceleration.`

### 5. Funding And Liquidity

Sterling's FY `2025` 10-K supports:

- cash and equivalents of `390.721M USD`
- term loan outstanding borrowings of `292.5M USD`
- revolver capacity of `150M USD`
- no revolver borrowings outstanding at year-end

Simple claim:

`Sterling had meaningful cash and modest company-level leverage relative to the backlog visibility pool, but that does not prove individual customer projects were funded.`

Boundary:

`The real funding question is upstream: who is paying for the data-center, semiconductor, manufacturing, power-generation, and infrastructure projects Sterling executes?`

## Baseline To Q2 Bridge

| Company | Annual Baseline | Q2 2026 Update | What We Learn |
|---|---|---|---|
| United Rentals | FY `2025` gross rental capex `4.189B USD`; operating cash flow `5.190B USD`; free cash flow `2.181B USD`; fleet OEC `22.48B USD`; net leverage `1.9x` | H1 `2026` gross rental capex `2.931B USD`; free cash flow `1.149B USD`; OEC `23.8B USD`; fleet productivity `3.4%` | URI is a durable fleet-access capital absorber, not a one-quarter fleet spend story. |
| Sterling | FY `2025` signed backlog `3.01B USD`; combined backlog `3.31B USD`; future-phase work `>1.0B USD`; operating cash flow `439.988M USD`; CEC purchase price `562M USD` | Q2 `2026` combined backlog `5.62B USD`; future-phase opportunities `1.4B USD`; H1 operating cash flow `328.021M USD`; CEC contribution remains material | STRL is a backlog-visibility and execution-capacity case, with acquisition contribution and future-phase evidence kept separate. |

## What We Are Saying Now

The industrial buildout claim is now stronger and more precise:

`Capital is being absorbed through two different industrial channels. URI turns dollars into rentable fleet access, then tests the fleet through OEC, productivity, equipment sales, operating cash flow, free cash flow, leverage, and liquidity. STRL turns customer-funded construction demand into signed backlog, unsigned awards, future-phase opportunities, segment operating income, and operating cash flow, with CEC adding acquired electrical/mechanical capability.`

The big warning is:

`Do not mix URI fleet capex with STRL backlog as if they were the same thing. URI owns and finances fleet assets. STRL executes customer projects and converts backlog into revenue and cash.`

## Next Required Proof

The next pass should add:

- URI fleet utilization, specialty/re-rent mix, fleet-type returns, used-equipment recovery, and debt maturity/facility draw detail.
- STRL project/customer categories, signed versus unsigned conversion, CEC organic/acquired bridge, contract assets/liabilities, and customer funding sources.
- Outside denominators for U.S. equipment rental fleet, nonresidential construction starts, data-center construction spending, semiconductor/manufacturing construction, and heavy/civil project awards.
