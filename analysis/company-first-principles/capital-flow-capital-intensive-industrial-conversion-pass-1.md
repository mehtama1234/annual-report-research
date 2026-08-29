# Capital Flow Capital-Intensive Industrial Conversion Pass 1

## Purpose

This pass moves from denominator context to conversion proof for United Rentals and Sterling Infrastructure.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-industrial-conversion-pass-1.csv`

The question is:

`Do the company filings show that industrial buildout demand converts into fleet productivity, backlog visibility, cash flow, and funding capacity?`

## What Was Added

| Item | Count |
|---|---:|
| Conversion rows | `16` |
| United Rentals rows | `7` |
| Sterling rows | `9` |
| Derived conversion metrics | `12` |
| Source-defined conversion metrics | `4` |

## Why This Pass Matters

The industrial denominator pass told us where the outside market is broad, weak, or strong.

This pass asks a different question:

`Can the companies actually convert those pockets of demand into economics?`

That means:

- URI must show fleet spend, fleet scale, productivity, cash generation, and liquidity in the same window.
- Sterling must show signed backlog, weaker backlog buckets, acquisition contribution, cash conversion, and funding capacity without mixing them into one number.

## United Rentals: Fleet Spend To Productive Fleet

URI's conversion mechanism is:

`fleet capex -> OEC -> rental revenue -> fleet productivity -> used-equipment recycling -> free cash flow -> liquidity/funding capacity`

### URI Conversion Rows

| Metric | Value | Period | Interpretation |
|---|---:|---|---|
| Operating cash flow as percent of gross rental capex | `112.8%` | H1 `2026` | Operating cash flow exceeded gross rental capex in the period. |
| Net cash rental-equipment investment | `2.040B USD` | H1 `2026` | Cash purchases of rental equipment less sale proceeds. |
| Rental revenue as percent of OEC | `16.2%` quarterly | Q2 `2026` | Simple revenue/OEC productivity proxy, not ROIC. |
| OEC increase since year-end `2025` | `1.32B USD`, or `5.9%` | FY2025 to Q2 `2026` | Fleet scale increased during the active investment window. |
| Fleet productivity increase | `3.4%` | Q2 `2026` | Company-defined metric combining rate, time utilization, and mix. |
| Gross rental capex guide midpoint increase | `9.8%` | FY2026 guide update | Current gross-purchase guide midpoint rose to `5.05B USD` from `4.6B USD`. |
| Total liquidity | `2.999B USD` | Q2 `2026` | Liquidity includes cash plus ABL and accounts receivable securitization facility availability. |

### URI Simple Read

`URI is doing the thing we hoped the evidence would show: it is spending heavily on fleet, growing OEC, producing rental revenue, reporting positive fleet productivity, generating free cash flow, and still carrying explicit liquidity capacity.`

The stronger claim is:

`URI is a source-table-backed and conversion-supported fleet-access capital absorber.`

The boundary is:

`This is still not fleet-return proof. We need utilization, rate, mix, OEC by category, specialty versus general rental, used-equipment recovery, and facility-level funding details.`

## Sterling: Backlog To Execution And Cash

Sterling's conversion mechanism is:

`customer projects -> signed backlog/RPOs -> unsigned awards -> future phases -> revenue -> operating cash flow -> platform funding capacity`

But Sterling has an important complication:

`Acquisition contribution is material.`

### Sterling Conversion Rows

| Metric | Value | Period | Interpretation |
|---|---:|---|---|
| Acquisition revenue contribution as percent of Q2 revenue | `21.5%` | Q2 `2026` | Growth is partly acquired, not purely organic. |
| Combined backlog to Q2 revenue | `4.8x` | Q2 `2026` | The backlog funnel is large relative to current quarterly revenue. |
| Combined backlog to 2026 revenue guide midpoint | `1.38x` | FY2026 guide context | Backlog exceeds the full-year revenue-guide midpoint. |
| CEC and Stone Ridge contribution to signed backlog plus unsigned awards | `2.56B USD` | Q2 `2026` | Acquisition contribution is about `45.6%` of combined backlog. |
| Operating cash flow less capex | `258.375M USD` | H1 `2026` | Sterling generated cash well above company capex. |
| Revolver expansion multiple | `10.0x` | July `2026` | Revolver capacity expanded to `1.5B USD` from `150M USD`. |
| Unsigned awards as percent of combined backlog | `22.8%` | Q2 `2026` | A meaningful share of combined backlog is below signed-backlog status. |
| Future-phase opportunities as percent of visibility to future work | about `20.0%` | Q2 `2026` | Future phases are meaningful but lower-confidence optionality. |

### Sterling Simple Read

`Sterling is a strong execution-capacity story, but the evidence forces discipline. Backlog is large, cash conversion is positive, and funding capacity improved. But acquisition contribution and weaker backlog buckets are large enough that we cannot call the whole funnel organic, signed, funded work.`

The stronger claim is:

`Sterling is a source-table-backed and conversion-supported customer-project execution platform with material acquisition-enabled growth.`

The boundary is:

`This is still not fully funded backlog proof. We need contract assets, contract liabilities, backlog roll-forward, customer project sources, margin durability, and organic/acquired conversion over time.`

## Side-By-Side Conversion Logic

| Company | What Capital Becomes | Best Conversion Evidence | Main Limitation |
|---|---|---|---|
| URI | Owned fleet available for rent | Operating cash flow above gross rental capex, OEC growth, positive fleet productivity, liquidity including ABL/AR securitization capacity | Need utilization, rate, mix, OEC category, and fleet-return detail. |
| Sterling | Customer projects moving through backlog and field execution | Large combined backlog, positive cash flow less company capex, expanded revolver, explicit future-work funnel | Need signed/funded status, customer funding, contract assets/liabilities, and organic/acquired split. |

## What This Adds To The Big Picture

The industrial lane now has three proof layers:

1. Source-table proof:
   `URI and Sterling have exact annual and quarterly source rows.`
2. External denominator proof:
   `URI and Sterling sit inside measurable rental, machinery, construction, and data-center denominators.`
3. Conversion proof:
   `URI and Sterling show different but measurable conversion mechanics.`

In simple words:

`Capital is not just being announced. In URI, it becomes a rental fleet that generates revenue, productivity, and cash. In Sterling, it becomes a layered project funnel that generates revenue and cash, but the funnel must be separated into signed backlog, unsigned awards, future phases, and acquired contribution.`

## Claim Status

This pass strengthens CTCS-014, but it still should not become full `project-and-cash-grade`.

Promote only this narrower claim:

`The industrial buildout lane now has first-pass conversion support: URI shows fleet-capex-to-cash conversion and Sterling shows backlog/cash conversion with acquisition contribution separated.`

Do not promote this broader claim:

`Every dollar of fleet capex or backlog is high-return, organic, funded project capital.`

## Next Pass

The next useful artifact should be:

`capital-flow-capital-intensive-project-funding-map-pass-1.md`

It should connect:

- URI ABL, accounts receivable securitization, debt maturities, and collateral/funding capacity
- Sterling revolver expansion, term-loan payoff, covenant package, and acquisition funding
- ET and Cheniere debt/entity/project finance rows
- the distinction between company funding capacity and customer/project source-of-funds
