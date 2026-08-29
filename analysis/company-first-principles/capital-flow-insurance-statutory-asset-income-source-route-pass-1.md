# Capital Flow Insurance Statutory Asset Income Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-006`.

It asks:

`Can current local evidence tie insurance or retirement liability capital to statutory legal-entity holdings, Schedule D/BA assets, investment income, realized gains/losses, impairments, NAIC designations, and liability-cost spread?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-insurance-statutory-asset-income-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No statutory asset-income upgrade yet. Apollo/Athene and KKR/Global Atlantic both show large insurance or retirement liability channels, invested-asset bases, and income/spread proxies. KKR/Global Atlantic has the stronger current 10-Q asset-income and credit-quality proxy. But neither row has statutory legal-entity Schedule D/BA holdings, NAIC designations, realized gain/loss and impairment schedules, or liability-cost spread proof in the current local source set.`

## Row Outcomes

| Row | Case | Current Statutory/Asset-Income Evidence | Statutory Result | Remaining Gap |
|---|---|---|---|---|
| `CFISAISR-001` | Apollo/Athene insurance channel | Q2 `2026` retirement-services gross inflows of `22.069B USD`, Athene-attributable inflows of `17.095B USD`, net flows of `11.928B USD`, gross invested assets of `413.598B USD`, net invested assets of `314.090B USD`, gross alternative investments of `20.396B USD`, spread-related earnings of `877M USD`, FY `2025` Athene Accounts AUM of `392.2B USD`, direct-origination AUM of `302.1B USD`, asset-backed-finance AUM of `282.7B USD`, and net floating-rate assets of `3.5B USD` | Hold with liability-channel and spread-earnings proxy | No Athene legal-entity statutory statements, Schedule D/BA holdings, statutory investment-income exhibit, realized gain/loss schedule, impairment detail, NAIC designation distribution, RBC/capital treatment, liability-cost schedule, or borrower destination |
| `CFISAISR-002` | KKR / Global Atlantic channel | Global Atlantic AUM of `220B USD`, credit AUM of `164B USD`, Ivy/sponsored reinsurance vehicle AUM of `62B USD`, insurance investments of `189.204380B USD`, insurance policy liabilities of `205.499130B USD`, AFS fixed maturities of `88.056662B USD`, mortgage and other loan receivables net of `48.754106B USD`, six-month insurance net investment income of `4.028186B USD`, six-month fixed-maturity income of `3.351757B USD`, six-month mortgage/other-loan income of `1.541995B USD`, allowance of `671.094M USD`, past-due/foreclosure mortgage loans of `296.4M USD`, LTV bucket evidence, and FHLB pledged assets of `9.2B USD` | Hold with public-company asset-income and credit-quality proxy | No Global Atlantic statutory legal-entity statements, Schedule D/BA issuer holdings, NAIC designation distribution, statutory realized gain/loss and impairment schedule, asset-by-asset income, borrower/facility allocation, FHLB liability economics, or liability-cost spread |

## Decision

`insurance-statutory-asset-income-source-route-hold`

`CFRMSWO-006` is executed against the current local source set. It produces two holds:

- Apollo/Athene: liability-channel, invested-asset, direct-origination, ABF, alternatives, and spread-earnings proxy, but no statutory legal-entity asset-income proof.
- KKR/Global Atlantic: public-company insurance investment base, asset-class income, LTV, allowance, past-due, and FHLB pledged-asset proxy, but no statutory Schedule D/BA or liability-cost spread proof.

## Safe Claim

`The insurance statutory asset-income source-route pass confirms that Apollo/Athene and KKR/Global Atlantic are large insurance or retirement capital channels with visible invested-asset and income proxies, but current local evidence does not prove statutory legal-entity holdings, Schedule D/BA asset income, realized gains/losses, impairments, NAIC credit quality, liability-cost spread, borrower destination, or asset-level cash return.`

## Next Work

1. Pull Athene and Global Atlantic statutory annual and quarterly statements by legal entity.
2. Extract Schedule D and Schedule BA holdings by issuer, CUSIP, asset type, affiliate status, NAIC designation, book value, fair value, and unrealized gain/loss.
3. Extract statutory investment-income exhibits, realized gain/loss schedules, impairment schedules, and credit-loss detail by statutory entity and asset class.
4. Build liability-cost and spread bridges using crediting-rate, policyholder liability, funds-withheld, FHLB funding-agreement, and ALM disclosures.
5. Join private-placement, loan, mortgage, and alternative-asset rows to borrower/facility documents where public evidence exists.
6. Move next to `CFRMSWO-007` contract pricing, customer obligation, and tenor evidence.
