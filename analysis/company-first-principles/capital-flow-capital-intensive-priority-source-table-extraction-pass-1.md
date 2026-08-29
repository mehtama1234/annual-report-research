# Capital Flow Capital-Intensive Priority Source-Table Extraction Pass 1

## Purpose

This pass starts the true source-table layer for the capital-intensive buildout work.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-priority-source-table-extraction-pass-1.csv`

The prior manifest found that the source ledgers existed but the raw priority files were missing from this checkout. This pass rehydrates the first two priority Q2 source families from SEC:

- United Rentals Q2 `2026`: `10-Q`, `8-K`, earnings-release exhibit
- Sterling Infrastructure Q2 `2026`: `10-Q`, `8-K`, earnings-release exhibit, presentation exhibit

## Rehydrated Sources

| Company | Restored Files | What They Add |
|---|---|---|
| United Rentals | `2026-q2-10q.html`; `2026-q2-8k.html`; `2026-q2-ex99-earnings-release.html` | Filed and furnished source support for revenue, rental revenue, adjusted EBITDA, fleet productivity, free cash flow, gross rental capex, rental-equipment purchases, used-equipment proceeds, OEC, leverage, and liquidity. |
| Sterling Infrastructure | `strl-20260630.htm`; `strl-20260803.htm`; `2026-q2-ex99-earnings-release.html`; `2026-q2-earnings-presentation.html` | Filed and furnished source support for revenue, acquisition contribution, adjusted EBITDA, RPOs, MSAs, backlog, unsigned awards, combined backlog, operating cash flow, capex, revolver structure, future-phase opportunities, and visibility-to-future-work framing. |

## Extraction Summary

| Company | Rows | Strongest Source-Table Evidence | Status Impact |
|---|---:|---|---|
| United Rentals | `9` | `2.931B USD` year-to-date gross rental capex; `1.149B USD` free cash flow; `23.8B USD` OEC; `3.4%` fleet productivity; `1.8x` net leverage; `2.999B USD` liquidity | Moves URI from packet-level `cash-converting` toward source-table-backed cash conversion. |
| Sterling Infrastructure | `13` | `4.23B USD` RPOs; `100.0M USD` MSAs; `4.33B USD` total backlog; `1.28B USD` unsigned awards; `5.62B USD` combined backlog; `1.4B USD` future-phase opportunities; `328.021M USD` H1 operating cash flow | Moves STRL from packet-level `contracted-or-regulated` toward source-table-backed backlog and partial cash-conversion proof. |

Total rows: `22`

CSV row ID range:

`CIPSTE-001` through `CIPSTE-022`

## What We Can Now Say

### United Rentals

The safe claim is now stronger:

`United Rentals is a source-table-backed fleet-access capital absorber. The Q2 2026 SEC exhibit and 10-Q show rental revenue, fleet productivity, gross rental capex, rental-equipment purchases, free cash flow, OEC, leverage, and liquidity in the same reporting window.`

The boundary remains:

`This is not yet full fleet-return proof. OEC, fleet age, utilization, used-equipment proceeds, gross-to-net capex, and specialty/re-rent mix still need to be joined into one roll-forward.`

### Sterling Infrastructure

The safe claim is now stronger:

`Sterling is a source-table-backed specialty-construction backlog case. The Q2 2026 10-Q separates RPOs, MSAs, backlog, unsigned awards, and combined backlog, while the presentation separately identifies future-phase opportunities.`

The boundary remains:

`Combined backlog and future-phase opportunities are not the same as signed backlog, funded work, revenue, cash, or guaranteed margin. Acquisition contribution is material and must be separated from organic demand.`

## Why This Matters For The Big Picture

This is the pattern we need across the whole capital-flow project:

`packet claim -> source ID -> restored filing/exhibit -> exact metric label -> value -> status bucket -> safe claim -> missing proof`

The work is now moving in both directions:

- from the capital-flow thesis to the exact source tables that could prove or disprove it
- from the source-table metrics back to narrower claims the evidence actually supports

## Next Priority Pulls

The next source rehydration targets remain:

1. Energy Transfer Q2 `2026` source chain for growth/maintenance capex, DCF, throughput, and project capacity.
2. Cheniere Q2 `2026` source chain for LNG cargoes, Stage 3 train status, DCF, and capital deployment.
3. United Rentals annual/Q4 `2025` source chain for full-year fleet-capex and cash-conversion roll-forward.
4. Sterling annual/Q4 `2025` source chain for CEC contribution, year-end backlog, and E-Infrastructure mix.

## Bottom Line

We now have the first source-table-backed proof that the buildout theme is more than narrative:

- United Rentals shows capital absorbed into rental fleet and converted through rental revenue, fleet productivity, cash flow, and leverage management.
- Sterling shows capital absorbed into construction execution capacity through RPOs, backlog, unsigned awards, future-phase opportunities, and operating cash flow.

But the status stays bounded:

`Source-table-backed first pass, not thesis-grade.`
