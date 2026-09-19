# Pilot 01 Antamina Scenario Workbench

Date: 2026-09-16

This is an illustrative Damodaran-style expectation-burden screen for the
[Wheaton–Antamina pilot](combined-investment-research-pilot-01-wheaton-antamina.md).
It is not a source-backed fair-value conclusion because the public record does
not disclose a BHP-PMPA-only delivery curve, settlement ledger, Antamina tax
allocation, or debt-service waterfall.

The structured outputs are in
[combined-investment-research-pilot-01-antamina-scenario-workbench.csv](data/combined-investment-research-pilot-01-antamina-scenario-workbench.csv).

## Inputs that are source anchored

- Initial upfront payment: `4.300B USD`.
- Payable factor: `90%`.
- Initial BHP stream: equivalent to BHP's `33.75%` of payable silver until
  `100M` ounces have been delivered, then `22.5%` for life of mine. The model
  expresses the step-down as `66.666667%` of the initial stream.
- Ongoing payment: `20%` of spot silver price for delivered ounces.
- BHP reported `5.588M` ounces of payable Antamina silver production for FY2026
  on its `33.75%` share basis. This is now the latest full-year counterparty
  production denominator. BHP reported `5.4M` ounces on its share basis in
  calendar 2025. Wheaton's September 16, 2026 Corporate Presentation adds a
  management forward profile of approximately `6.0 Moz` per year for the first
  five years and `5.4 Moz` for the first ten years. The base and bull cases now
  use those labeled profile windows; they remain management-profile inputs,
  not reserve-backed forecasts or settled receipts.
- Wheaton's transaction materials report `65.7M` contained silver ounces of
  BHP-interest Proven and Probable Mineral Reserves. A mechanical `90%`
  equivalent is `59.13M` ounces, below the `100M`-ounce initial step-down
  threshold. This is a reserve-quantity boundary, not a delivery forecast;
  contained ounces, payable ounces, and metal credits are not interchangeable.

## Calculation

For each modeled year:

```text
cash before corporate burden
  = BHP-share production
  × payable factor
  × spot price
  × (1 - stream payment percentage)

illustrative owner-cash proxy
  = cash before corporate burden
  × (1 - burden haircut)
```

The model applies the initial stream share until the 100M-ounce threshold,
then applies the life-of-mine share. The reserve-quantity screen means the
threshold should not be assumed to occur within currently disclosed P&P
reserves without an explicit production and recovery schedule. It discounts the modeled cash flows to
the upfront payment date and calculates an undistributed, unlevered IRR
screen. It does not include terminal value, working capital, corporate debt
repayment, taxes as actually allocated, or a reserve-backed tail beyond the
modeled horizon.

## Result and interpretation

| Scenario | Modeled cash / year before step-down | NPV at stated discount rate | IRR | Reading |
| --- | ---: | ---: | ---: | --- |
| Bear | `56.7M USD` | `-3,951.6M USD` | `-26.2%` | The price is not supported by low price, volume, and short-duration assumptions. |
| Base | `186.6M USD` | `-2,661.0M USD` | `-3.2%` | The disclosed 5.4 Moz first-ten-year profile followed by the contractual step-down still does not recover the upfront payment at $60/oz after the burden haircut. |
| Bull | `330.5M USD` | `-1,514.2M USD` | `1.5%` | Even the disclosed 6.0 Moz first-five-year profile at $90/oz remains below a 7% discounted screen after the modeled step-down and burden haircut. |

The result is an expectation-burden finding, not a claim that the transaction
is uneconomic. The combined Glencore/BHP stream table reports historical cash
flow generated for the combined asset, while this screen isolates only the
incremental BHP stream and intentionally refuses to allocate legacy-stream
cash to the BHP purchase.

### FY2026 production calibration

BHP's FY2026 production table reports `5.588M` payable silver ounces for its
`33.75%` Antamina interest. At the contractual `90%` payable factor, the
mechanical equivalent is `5.0292M` ounces before any question of actual
Wheaton delivery, metal-credit timing, or the `100M`-ounce threshold. For
orientation only, applying the workbench's base `$60/oz` price and `20%`
ongoing payment would produce `$241.402M` of pre-burden stream cash before
any step-down. This is a calibration calculation, not a reported cash flow:
it omits quotation-period price, delivery timing, taxes, debt service, and the
missing BHP-PMPA settlement ledger. The bear/base/bull valuation rows remain
unchanged and continue to use their explicitly labeled forward profiles.

Source: [BHP FY2026 public-filing boundary](capital-flow-wheaton-antamina-bhp-fy2026-annual-report-boundary-2026-09-16.md), which distinguishes the preserved Form 6-K results artifact from the official Form 20-F route.

## What would upgrade the model

1. BHP-PMPA-only delivered and sold ounces by quarter.
2. Realized price and settlement cash by delivery period.
3. A reserve-backed Antamina production and delivery curve that reconciles the
   `65.7M` BHP-interest P&P reserve quantity with payable recovery and the
   `100M`-ounce contractual threshold.
4. Antamina-specific tax and interest allocation.
5. Wheaton debt-service and lender-waterfall evidence.
6. A separate combined-stream model that allocates legacy Glencore economics.
