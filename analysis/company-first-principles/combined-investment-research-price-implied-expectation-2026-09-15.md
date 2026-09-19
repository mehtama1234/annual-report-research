# Combined investment research price-implied expectation bridge

Observation date: `2026-09-15`

This memo reverses the illustrative valuation screens. It asks what operating
cash or separated earnings the dated market snapshot would require at the
stated multiples. It is an expectations audit, not an intrinsic-value claim.
The calculations are structured in the [price-implied CSV](data/combined-investment-research-price-implied-expectation-2026-09-15.csv).

## Retail market-implied cash

| Company | Market value | Stated multiple | Implied cash | Existing base cash | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Target | `$71.129B` | `18x / 24x / 30x` | `$3.952B / $2.964B / $2.371B` | `$3.000B` at `24x` | Near the base screen, but not normalized owner cash |
| Walmart | `$867.608B` | `30x / 38x / 45x` | `$28.920B / $22.832B / $19.280B` | `$18.000B` at `38x` | Base multiple requires about `$4.832B` more annual cash than the illustrative base case |

Implied cash is simply market value divided by the selected multiple. It does
not assume that the company can produce the implied cash; it identifies the
burden that the normalized-cash work must prove or reject. Target remains
exposed to tariff, payable, supplier-finance, capex, service, lease, and
dilution normalization. Walmart must justify its higher expectation through
advertising, membership, fulfillment, automation, maintenance capital, and
working-capital conversion.

### Promotion-status cross-check

The `Target $3.000B` and `Walmart $18.000B` values shown as “existing base
cash” are illustrative base inputs from the valuation workbench, not observed
H1 2026/H1 FY2027 owner cash. The latest common-period reported cash-after-
property/capex screens are `$2.115B` for Target and `$5.529B` for Walmart, and
the [owner-cash promotion matrix](combined-investment-research-owner-cash-promotion-matrix-2026-09-15.md)
holds both at reported or illustrative status. The price-implied bridge is
therefore an expectation substitution test, not a promotion of the workbench
base case into normalized owner cash.

## Apollo separated-earnings expectation

Apollo's base SOTP assumptions are `2.8B USD` normalized FRE at `22x`, `3.2B
USD` normalized SRE at `6x`, `3.0B USD` principal/performance value, and a
negative `10.0B USD` common-claims/capital haircut. Against the `$77.803B`
market snapshot:

- Holding base SRE, principal value, and haircut constant requires about
  `$2.982B` normalized FRE rather than `$2.800B`.
- Holding base FRE, principal value, and haircut constant requires about
  `$3.867B` normalized SRE rather than `$3.200B`.
- Holding base FRE, SRE, and haircut constant requires about `$7.003B` of
  principal/performance value rather than `$3.000B`.

These are substitution tests, not forecasts. Each combination still requires
proof after capital, credit, liability, NCI, preferred, tax, dilution, and
parent-cash constraints.

## Wheaton–Antamina boundary

Wheaton's `$67.812B` market capitalization cannot be mechanically translated
into an Antamina-specific implied cash figure because the public record does
not disclose a clean segment equity-value allocation or a market price for the
BHP PMPA alone. The correct expectation test remains transaction-level:
compare the `$4.300B` upfront payment with the BHP-only delivery, price,
payment, tax, interest, and debt-service schedule. The Antamina workbench is
an expectation-burden screen, not a market-implied value.

## Status

`price-implied-expectation-explicit-qualified`: the market snapshot is now
reversed into denominator-specific required cash or separated earnings, with
the Wheaton non-identifiability boundary preserved. Normalized owner cash,
realized SRE/FRE, and Antamina delivery economics remain unresolved.

Sources: [September 16 market snapshot](combined-investment-research-market-snapshot-2026-09-16.md), [retail valuation workbench](data/combined-investment-research-pilot-02-retail-valuation-workbench.csv), [Apollo SOTP workbench](data/combined-investment-research-pilot-03-apollo-sotp-workbench.csv), and [Antamina workbench](data/combined-investment-research-pilot-01-antamina-scenario-workbench.csv).
