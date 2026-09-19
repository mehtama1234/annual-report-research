# Wheaton–Antamina reserve-constrained delivery ceiling — 2026-09-15

This artifact advances Q-02 by joining the disclosed BHP-interest Proven and
Probable reserve quantity to the public production-profile proxies. It is a
mechanical reserve ceiling, not a mine-plan forecast or a BHP-PMPA settlement
ledger.

## Source-anchored inputs

- BHP-interest P&P contained silver reserves: `65.7M oz`.
- PMPA payable factor: `90%`.
- Mechanical reserve-payable ceiling: `59.13M oz`.
- Initial PMPA stream threshold: `100M delivered oz`.
- Public production proxies: `6.0M oz/year` for the first-five-year profile,
  `5.4M oz/year` for the first-ten-year profile, and `5.588M oz` FY2026
  BHP-interest production.

## Reserve-constrained duration screen

| Production proxy | Payable production/year at 90% | Full years within 59.13M payable oz | Partial next year | Mechanical reserve duration | Gap to 100M threshold |
| ---: | ---: | ---: | ---: | ---: | ---: |
| `6.000M oz/year` | `5.400M oz` | `10` | `0.950` | `10.95 years` | `40.87M oz` |
| `5.400M oz/year` | `4.860M oz` | `12` | `0.167` | `12.17 years` | `40.87M oz` |
| `5.588M oz/year` | `5.029M oz` | `11` | `0.757` | `11.76 years` | `40.87M oz` |

```text
reserve-payable ceiling = 65.7M contained oz × 90% = 59.13M oz
payable production/year = production proxy × 90%
mechanical duration = 59.13M oz ÷ payable production/year
```

## Interpretation boundary

Under these constant-rate proxies, the currently disclosed P&P quantity does
not reach the `100M`-ounce initial PMPA step-down threshold. That is not a
conclusion that the contract will never reach the threshold: reserves can
convert, production can change, payable recovery can differ, and the PMPA
threshold counts actual delivered credits rather than contained reserve
ounces. The calculation also does not model mine sequencing, depletion,
metallurgical recovery, payability deductions, settlement timing, or the
post-reserve life-of-mine tail.

The safe upgrade is therefore `reserve-constrained delivery ceiling confirmed`,
not `reserve-backed delivery curve proven`. The valuation workbench must keep
the threshold step-down and the reserve ceiling as separate assumptions.

## Proof-grade result

| Gate | Result |
| --- | --- |
| P&P reserve quantity | Proven as a transaction-material input |
| Mechanical payable conversion | Proven as arithmetic sensitivity |
| Reserve-constrained duration ceiling | Qualified mechanical screen |
| Annual life-of-mine delivery curve | Not proven |
| BHP-PMPA settlement quantity and cash | Not proven |

Sources: [BHP reserve-quantity boundary](capital-flow-wheaton-antamina-bhp-reserve-quantity-boundary-upgrade-2026-09-15.md), [production-profile boundary](capital-flow-wheaton-antamina-production-profile-boundary-upgrade-2026-09-15.md), and [BHP annual delivery-curve proxy](capital-flow-wheaton-antamina-bhp-annual-delivery-curve-proxy-2026-09-15.md).
