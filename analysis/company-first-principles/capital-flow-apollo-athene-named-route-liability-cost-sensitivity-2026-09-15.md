# Apollo–Athene Named-Route Liability-Cost Sensitivity

Research date: `2026-09-17`

## Purpose

Test whether the reconciled named-route book values can support a transparent
liability-cost burden screen without mislabeling a proportional allocation as
observed asset-level funding cost.

## Mechanical screen

The reconciled Schedule D Part 1 Section 1 plus Section 2 bond denominator is
`$158.852395199B`. Athene's H1 2026 reported cost of funds is `$5.749B`.
Allocating that segment cost mechanically by named holding book value gives:

| Route | Holding book value | Share of reconciled bond base | Mechanical cost allocation |
| --- | ---: | ---: | ---: |
| AMAPS `02300A-AA-8` | `$1.917500B` | `1.2071%` | `$69.396M` |
| Concord `20633K-AN-8` | `$215.168M` | `0.1355%` | `$7.787M` |

For orientation only, subtracting those mechanical allocations from the
available holding-side income fields would produce approximately negative
`$20.525M` for AMAPS and negative `$4.474M` for Concord. That subtraction is
not a return claim because the income fields are FY2025 statutory rows while
the cost-of-funds figure is H1 2026 segment reporting.

## What this proves

The named holding denominator is large enough to expose the scale of a
liability-cost burden sensitivity. It also shows why gross holding income
cannot be promoted directly to risk-adjusted asset return.

## Boundary

This is not an observed liability allocation, net spread, ROIC, IRR, or cash
return. It does not account for duration, hedges, policyholder crediting
rates, reserves, capital charges, taxes, credit losses, NCI, preferred claims,
or legal-entity matching.

## Next test

Obtain Athene asset-liability duration and crediting-rate schedules, legal-
entity investment-income exhibits, and named-route funding/custodian records.
Replace the proportional screen with a period-matched liability-cost bridge.

## Safe claim

`A reconciled bond denominator supports a transparent named-route liability-
cost sensitivity, but public evidence still does not allocate Athene funding
cost to AMAPS or Concord at the asset level.`

## Q2 2026 wrapper-denominator refresh — 2026-09-17

The Q2 2026 public packet reports current AMAPS 1 exposure of approximately
`$2.544B`, compared with `$2.550B` at December 31, 2025. Applying the same
mechanical proportional screen to the reconciled `$158.852395199B` bond base
and H1 2026 Athene cost of funds of `$5.749B` gives:

```text
2.544B / 158.852395199B = 1.6015% of the bond base
1.6015% x 5.749B = approximately 92.1M of mechanical cost allocation
```

This is a current-period wrapper-denominator sensitivity, not evidence that
`$92.1M` was the cost incurred by AMAPS 1. The Q2 exposure is not joined to
settled lots, issuer-level income, policyholder crediting, duration, hedges,
or a custodian/trustee cash record. It therefore improves denominator
freshness without changing Q-08's `evidence-insufficient` return grade.
