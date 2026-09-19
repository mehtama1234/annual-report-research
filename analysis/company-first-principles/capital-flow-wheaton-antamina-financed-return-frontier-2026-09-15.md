# Wheaton–Antamina financed-return frontier — 2026-09-15

This screen translates the latest company-level financing evidence into a
bounded burden adjustment for the Antamina operating-cash-flow proxy. It is a
financed-return frontier, not an Antamina-specific IRR or NPV: Wheaton does not
allocate its term loan, revolver interest, or tax expense to the PMPA in the
public filing.

## Source-anchored inputs

| Input | Value | Boundary |
| --- | ---: | --- |
| Antamina H1 2026 operating-cash-flow proxy | `$222.223M` | Stream-level, before corporate tax and finance allocation |
| Mechanical annualized proxy | `$444.446M` | H1 multiplied by two; not a forecast |
| PMPA upfront payment | `$4.300B` | Named BHP Antamina purchase price |
| Company term loan plus revolver balance | `$1.972B` | Corporate debt balance, not PMPA-assigned debt |
| Current SOFR plus disclosed margins | `3.62% + 1.00%–2.05%` term loan; `3.62% + 1.10%–2.15%` RCF | Mechanical annualized interest screen before fees, timing, amortization, and tax |

## Mechanical frontier

| Case | Annual company-level interest screen | Annualized Antamina OCF proxy less screen | Cash / upfront payment | Simple payback proxy |
| --- | ---: | ---: | ---: | ---: |
| Lower burden | `$91.578M` | `$352.868M` | `8.206%` | `12.19 years` |
| Higher burden | `$112.284M` | `$332.162M` | `7.725%` | `12.95 years` |

The arithmetic is:

```text
annualized Antamina OCF proxy = 222.223M × 2 = 444.446M
financed cash frontier = 444.446M − company-level interest screen
cash / upfront payment = financed cash frontier ÷ 4,300M
simple payback = 4,300M ÷ financed cash frontier
```

## Interpretation

The screen shows that applying the current full disclosed company-debt
interest range to the annualized Antamina cash proxy lowers the mechanical
cash yield from `10.336%` before financing to approximately `7.725%–8.206%`.
That is useful as a burden frontier: it identifies the scale of financing
drag that a fully financed model must absorb before taxes, debt principal,
delivery timing, and reserve-life uncertainty.

It does not establish that all `$91.578M–$112.284M` belongs to Antamina, that
the H1 OCF proxy repeats for a full year, or that the remaining cash is
available after tax and lender claims. The result therefore cannot be called
PMPA IRR, NPV, debt-service coverage, or common-owner cash.

## Upgrade consequence

Q-03 now has a source-backed company-level financed-return frontier in addition
to the unlevered scenario workbench. Full asset-level financed return still
requires an Antamina debt allocation, actual payment dates, principal
amortization or repayment waterfall, tax allocation, BHP-only delivered-ounce
curve, and realized settlement cash.

## Sources

- [Wheaton–Antamina company-burden boundary](capital-flow-wheaton-antamina-company-burden-boundary-upgrade-2026-09-15.md)
- [Wheaton–Antamina financing terms and SOFR sensitivity](capital-flow-wheaton-antamina-financing-terms-boundary-upgrade-2026-09-15.md)
- [Wheaton–Antamina net-cash-return pass](capital-flow-wheaton-antamina-net-cash-return-pass-1.md)
