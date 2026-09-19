# Physical-capacity thesis-breaker register

Research date: `2026-09-17`

## Rule

A thesis breaker is a same-entity, same-period filing, contract, collateral,
or project reconciliation that would weaken the operating or valuation claim.
It is not a forecast, a ratio-only warning, or an allegation of misconduct.
Current proxy evidence does not activate a breaker; it only defines what must
be measured when the decisive source arrives.

## Coverage

| Company | Breakers | Core question |
|---|---:|---|
| United Rentals | 2 | Does fleet access produce lifecycle cash without collateral or funding stress? |
| Equinix | 2 | Does powered/interconnected capacity earn a common-owner return after project and funding claims? |
| Digital Realty | 2 | Does hyperscale development convert backlog into diluted common cash after private capital and debt claims? |

All six rows are `active-qualified`; no breaker is activated.

## Breaker matrix

| ID | Company | Thesis claim | Required observation | Activation condition | Current status |
|---|---|---|---|---|---|
| PCB-URI-01 | United Rentals | Fleet scale and access can support durable lifecycle cash | Populated borrowing-base certificate, eligible equipment, NOLV, reserves, L/C, utilization, replacement capex, and resale recovery | Legal Combined Availability is materially below the public facility proxy, or collateral haircuts/availability cannot support the required fleet funding | active-qualified |
| PCB-URI-02 | United Rentals | Rental operations convert fleet investment into owner cash | Same-period fleet cash, maintenance/replacement split, debt service, leases, taxes, resale proceeds, dilution, and utilization | Replacement and senior claims consume the source-backed rental cash, or used-equipment recovery and utilization fail to support the modeled cycle | active-qualified |
| PCB-EQX-01 | Equinix | Interconnection and powered capacity can earn attractive incremental returns | Project capital, power cost, commencement, stabilized yield, recurring capex, lease-up, JV/VIE funding, debt, and dilution | A project cohort fails to cover total capital and claims after commencement, or parent/JV obligations consume the apparent recurring residual | active-qualified |
| PCB-EQX-02 | Equinix | AFFO/booking strength reflects durable common-owner cash | Same-period AFFO-to-cash bridge, receivables, commitments, recurring-capex definition, and per-share claims | AFFO or bookings growth is accompanied by unresolved recurring-capital, receivable, commitment, or dilution burden that lowers common residual | active-qualified |
| PCB-DLR-01 | Digital Realty | Hyperscale backlog and development can convert into common-owner value | Project cost, MW/powered-shell status, commencement, signed rent, stabilized NOI, development yield, debt, private capital, and partner share | Backlog fails to commence or stabilized yield does not cover development capital, partner/private-capital economics, and project claims | active-qualified |
| PCB-DLR-02 | Digital Realty | FFO and equity-funded growth are durable on a per-share basis | FFO-to-cash bridge, recurring capex, ATM proceeds, OP units, preferred claims, dilution, fund contributions, and lease-up | Common-owner cash per diluted share deteriorates despite FFO/backlog growth because ATM/private capital, preferred, OP-unit, or lease-up claims absorb the economics | active-qualified |

## How to update

1. Attach the exact filing or legal source to the row.
2. Preserve the denominator and period; do not activate on a pooled or
   cross-company ratio.
3. Distinguish a failed operating mechanism from an unavailable document.
4. Carry the result into the Damodaran expectation case and Lyn Alden stress
   case.
5. Update the valuation range and confidence only after the trigger is
   reconciled to common-owner cash or a senior claim.

## QoE controls

- A negative search is not a negative operating result.
- A high AFFO/FFO or facility-availability figure does not clear growth
  capital, collateral, or dilution claims.
- A backlog or booking cancellation is not enough by itself; it must be joined
  to commencement, collection, cost, and funding.
- A resale recovery decline is not enough by itself; it must be joined to
  utilization, fleet age, replacement needs, and debt service.

## Decision

The physical-capacity cohort is `thesis-breakers-defined; active-qualified;
no-breaker-activated`. The register makes the comparison falsifiable while
preserving the current no-ranking decision.

Structured companion: [physical-capacity thesis-breaker table](data/combined-investment-research-physical-capacity-thesis-breaker-register-2026-09-17.csv).

Related: [physical-capacity valuation and liquidity stress workbench](combined-investment-research-physical-capacity-valuation-liquidity-stress-workbench-2026-09-17.md).
