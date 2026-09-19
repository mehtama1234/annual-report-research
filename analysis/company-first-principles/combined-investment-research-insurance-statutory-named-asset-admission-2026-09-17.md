# Insurance statutory named-asset income — next-sector admission

Research date: `2026-09-17`

## Decision

Admit insurance statutory named-asset income as the next capital-flow sector
lane. The initial comparison is:

- **Apollo/Athene:** prototype legal-entity income, proceeds, and named-issuer
  route.
- **KKR/Global Atlantic/Accordia:** comparison route with row-level owned-bond
  interest-received evidence.
- **Blackstone Credit & Insurance, Brookfield Wealth Solutions, BlackRock/HPS,
  Ares, and Carlyle/AlpInvest:** candidate extensions only after a named legal
  entity or borrower/vehicle source is confirmed.

The existing [statutory named-asset selection register](data/capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.csv)
is the structured control. This is an admission, not a platform ranking or a
claim that insurance capital is safe or unsafe.

## Force and control point

The force is the growth of retirement, annuity, insurance, private-credit, and
alternative-investment channels. The control point is not platform AUM. It is
the legal entity that holds liabilities and assets and can be followed from
named security or loan to income, proceeds, liability cost, remittance, and
return.

The chain is:

```text
policyholder / retirement liability
  -> insurer or reinsurer legal entity
  -> Schedule D / BA asset or named loan
  -> investment income, maturity, sale, or repayment
  -> liability cost, credit loss, capital treatment
  -> receipt, trustee/remittance waterfall, and residual return
```

AUM, gross spread earnings, statutory income, and asset proceeds are separate
objects. A named holding without cash, or cash without liability allocation,
does not close the chain.

## Current evidence surface

Apollo/Athene has the strongest local prototype: approximately `$158.619B` of
parsed Schedule D bond base, `$12.733B` statutory net investment income,
`$12.282B` cash-flow net investment income, `$13.601B` collected gross
investment income, `$54.035B` bond sale/maturity/repayment proceeds, and
`$12.676B` mortgage-loan sale/maturity/repayment proceeds. The remaining gap is
the named borrower receipt, liability cost, remittance/waterfall, and
Athene-to-parent allocation.

Accordia provides the strongest comparison row surface: approximately
`$7.318B` owned-bond book value, `$229.508M` owned-bond interest received,
`$156.199M` interest due/accrued, `$605.073M` gross investment income
collected, and `$549.714M` summary net investment income. The comparison still
needs disposal-lot continuity, liability cost, borrower/use, and waterfall.

The other platforms remain intentionally lower priority because the current
repository does not yet have an equally strong public legal-entity Schedule
D/BA route for them.

## QoE and financial-shenanigans tests

1. Do not use AUM as invested assets or invested assets as private credit.
2. Reconcile statutory income with cash-flow income and collected income.
3. Join named holdings to income, maturity, sale, proceeds, gain/loss, and
   impairment rather than inferring cash from fair value.
4. Compare asset income with credited rates, policyholder liabilities,
   reinsurance, funds-held balances, FHLB funding, and other liability costs.
5. Track NAIC designation, rating migration, non-accruals, allowances,
   impairments, affiliated exposure, and capital/RBC treatment.
6. Keep insurer-owned assets, manager-advised SMA assets, BDC holdings, and
   borrower facilities in separate legal perimeters.

These are forensic prompts, not fraud findings. Insurance accounting can be
valid while liability cost, liquidity, and asset-level return remain opaque.

## Damodaran and Lyn Alden handoff

Damodaran valuation requires a liability-adjusted spread, expected credit loss,
capital requirement, reinvestment, duration, and residual cash model. Lyn
Alden-style stress requires rates, surrender/withdrawal behavior, collateral
liquidity, credit spreads, refinancing, funding-agreement access, and the
nominal value of long-duration liabilities.

The platform is not promoted on gross investment income. Promotion requires:

`legal entity -> named asset/CUSIP -> investment amount -> income/proceeds -> liability cost -> remittance/waterfall -> return`

## Promotion consequence

Status: `insurance-statutory-named-asset-admitted; Apollo-and-Accordia-routes-visible; borrower-remittance-and-liability-adjusted-return-open; no-ranking`.

Primary routes: [statutory named-asset next-dig](capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.md),
[asset-quality bridge](capital-flow-insurance-statutory-asset-quality-bridge-pass-1.md),
and the [structured selection register](data/capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.csv).
