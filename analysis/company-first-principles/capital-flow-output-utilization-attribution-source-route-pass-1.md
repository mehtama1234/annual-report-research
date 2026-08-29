# Capital Flow Output Utilization Attribution Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-008`.

It asks:

`Can current local evidence assign physical output or utilization to the funded asset, project, route, fleet, or reserve base rather than leaving output at aggregate company level?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-output-utilization-attribution-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full physical output and utilization attribution upgrade yet. Cheniere, United Rentals, and Energy Transfer have useful partial attribution proxies: terminal cargo reconciliation, company-fleet OEC/productivity, and named capacity plus volume-growth evidence. Matador and Plains remain holds because current local evidence does not assign production, throughput, utilization, or billing volume to the relevant asset-area, borrowing base, route, or Cactus III asset.`

## Row Outcomes

| Row | Case | Current Output / Utilization Evidence | Attribution Result | Remaining Gap |
|---|---|---|---|---|
| `CFOUASR-001` | Cheniere LNG | FY `2025` company cargoes of `670` versus DOE vessel rows of `674`; Q2 `2026` company and DOE cargoes both `184`; Q2 DOE terminal volume of `640991.63 MMCF`; Sabine Pass and Corpus Christi terminal output and Corpus Christi Stage 3 milestone context | Partial terminal-cargo attribution proxy | No cargo-to-train mapping, train output, cargo-to-contract assignment, terminal-to-entity revenue, train margin, or debt-service/return link |
| `CFOUASR-002` | United Rentals fleet | Q2 `2026` OEC of `23.8B USD`; H1 `2026` rental-equipment purchase payments of `2.720B USD`; H1 gross rental capex of `2.931B USD`; H1 sale proceeds of `680M USD`; Q2 owned-equipment rentals of `2.991B USD`; Q2 rental revenue/OEC of `16.2%`; Q2 adjusted EBITDA/OEC of `8.6%`; positive fleet productivity evidence | Partial company-fleet output and utilization proxy | No fleet-class OEC, true utilization, rate/time/mix, growth versus replacement capex, source-to-purchase allocation, legal borrowing-base availability, or ROIC |
| `CFOUASR-003` | Energy Transfer projects | Nederland `240000 bpd` ethane capacity, Nederland `55000 bpd` LPG capacity, Lone Star Express more than `90000 bpd` incremental NGL takeaway, about `300000 bpd` long-term y-grade agreement context, Q2 `2026` NGL transportation growth of `13%`, and NGL export growth of `25%` | Partial named-capacity and volume-growth proxy | No named-project utilization, route throughput, shipper-volume assignment, tariff or fee billing volume, project revenue, project EBITDA/DCF, or project return |
| `CFOUASR-004` | Matador borrowing base | Q2 `2026` average production of `215631 BOE/d`, Q2 oil production of `11.476MMbbl`, Q2 gas production of `48.9Bcf`, Q2 revenue of `1.186392B USD`, development capex of `745.343M USD`, acquisition use of `1.228834B USD`, BLM Acquisition context, and borrowing-base context | Hold with company production context but no asset-area attribution | No asset-area production, reserve values, well-level output, BLM production contribution, LOE/cash margin, borrowing-base collateral output, or asset-level cash return |
| `CFOUASR-005` | Plains tariff route | Texas RRC tariff `TX 3.6.0`, effective `2026-07-01`, Karnes County to Cactus III/Hobson route, `178.98` cents per barrel base rate, negotiated-rate and term-agreement mechanics, and Cactus III capacity above `600000 bpd` | Hold with tariff-route context but no route throughput attribution | No committed volume, billed barrels, route throughput, utilization, shipper identity, realized route revenue, committed/uncommitted split, Cactus III contribution, or debt-service/return link |

## Decision

`output-utilization-attribution-source-route-hold-with-partials`

`CFRMSWO-008` is executed against the current local source set. It produces three partial output/utilization attribution proxies and two holds:

- Cheniere: partial terminal-cargo attribution proxy.
- United Rentals: partial company-fleet output and utilization proxy.
- Energy Transfer: partial named-capacity and volume-growth proxy.
- Matador: hold below asset-area production attribution.
- Plains: hold below route throughput attribution.

## Safe Claim

`The output utilization attribution source-route pass confirms that some affected rows have visible physical output, fleet output, capacity, or company volume-growth evidence, but the current local evidence does not prove full asset/project/route-level output attribution, utilization, revenue, cash contribution, or return across the affected rows.`

## Next Work

1. For Cheniere, pull cargo-to-train mapping, terminal-to-entity revenue support, cargo-to-contract assignment, train margin, and debt-service/return support.
2. For United Rentals, pull fleet-class OEC, utilization, rate/time/mix, growth/replacement capex, borrowing-base certificates, source-to-purchase allocation, and ROIC support.
3. For Energy Transfer, pull project utilization, route throughput, shipper-volume assignment, tariff/fee billing volume, project revenue, and project EBITDA/DCF.
4. For Matador, pull reserve reports, asset-area production, BLM contribution, well-level output, LOE/cash margin, and borrowing-base collateral support.
5. For Plains, pull committed-volume schedules, tariff billing records, route throughput, utilization, realized route revenue, Cactus III contribution, and debt-service/return support.
6. Move next to `CFRMSWO-009` collateral, borrowing-base, and availability certificates.
