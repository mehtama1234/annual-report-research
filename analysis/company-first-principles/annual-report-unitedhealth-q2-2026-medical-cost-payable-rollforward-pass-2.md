# Annual Report UnitedHealth Q2 2026 Medical-Cost-Payable Roll-Forward Pass 2

## Purpose

This pass tests whether UnitedHealth's Q2 2026 Form 10-Q can move the
healthcare-access case from a scale-and-margin observation toward a
same-period claims-funding and reserve-quality bridge.

## Source and period

- Company: UnitedHealth Group Incorporated (`UNH`)
- Filing: Q2 2026 Form 10-Q
- Period: six months ended June 30, 2026
- Primary source: [SEC Form 10-Q](https://www.sec.gov/Archives/edgar/data/731766/000073176626000197/unh-20260630.htm), Note 4, Medical Costs Payable

## Roll-forward

| Object | Six-month 2026 value | Interpretation |
| --- | ---: | --- |
| Medical costs payable, beginning | `$39.337B` | Opening consolidated medical-cost liability |
| Current-year reported medical costs | `$150.333B` | Current-period cost incurred, not cash paid |
| Prior-year reported medical-cost development | `$(1.250B)` | Favorable prior-year development; do not capitalize as recurring margin |
| Premium-deficiency and loss-contract reserve change | `$(236M)` | Separate reserve movement |
| Total reported medical costs | `$148.847B` | Reconciles to the income statement medical-cost line |
| Medical payments for current year | `$(116.846B)` | Filing-defined medical payments |
| Medical payments for prior years | `$(32.474B)` | Filing-defined settlement of prior-year claims |
| Total medical payments | `$(149.320B)` | Same-period payment outflow disclosed in the liability roll-forward |
| Held-for-sale payable change | `$66M` | Perimeter adjustment, not ordinary recurring claims conversion |
| Medical costs payable, ending | `$38.930B` | Closing consolidated medical-cost liability |
| IBNR component at June 30 | `$26.5B` | Claims incurred but not yet reported |

The arithmetic is:

`39.337 + 148.847 - 149.320 + 0.066 = 38.930` (billions of dollars).

The filing also states that prior-year reserve development was driven by a
favorable respiratory-illness season and other individually insignificant
factors. This makes the `$1.250B` favorable development an observed reserve
movement with a stated operational explanation, not evidence of a durable
underwriting or medical-cost margin.

## What this proves

The Q2 filing now supplies a same-entity, same-period medical-cost-payable
roll-forward. It shows that reported medical costs of `$148.847B` were paired
with `$149.320B` of filing-defined medical payments during the first half of
2026, while the ending liability remained `$38.930B` and included `$26.5B` of
IBNR claims.

This materially improves the UnitedHealth payer-cash diagnostic. It is no
longer limited to MCR, days claims payable, and a point-in-time IBNR balance.

## What remains unproven

- The filing does not label the `$149.320B` line as a complete “claims paid”
  waterfall by payer, provider, Optum business, or legal entity.
- It does not allocate medical payments between UnitedHealthcare and Optum
  Health or show the associated premium/service collections by legal entity.
- It does not provide a complete reserve-development triangle or normalize the
  favorable development across future periods.
- It does not join provider/pharmacy payments, risk-adjustment settlement,
  capital requirements, taxes, subsidiary restrictions, and diluted common
  residual into owner cash.
- The `$66M` held-for-sale adjustment must remain separate from recurring
  medical-cost conversion.

## Decision

`unitedhealth-medical-cost-payable-rollforward-qualified; payer-cash-bridge-open`

The workbench may promote the medical-cost-payable roll-forward as a proven
diagnostic input. It must not promote UnitedHealth to normalized owner cash,
durable margin, better access, or a cross-company ranking.

