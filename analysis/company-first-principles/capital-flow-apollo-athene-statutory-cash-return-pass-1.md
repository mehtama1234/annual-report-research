# Capital Flow Apollo/Athene Statutory Cash Return Pass 1

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-013`.

The question is:

`Can Apollo/Athene be upgraded from liability-channel and spread-earnings proxy evidence to statutory asset-income, credit-quality, and cash-return evidence?`

The evidence table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cash-return-pass-1.csv`

## Short Answer

`Apollo/Athene has liability-channel, invested-asset, and spread-earnings evidence, but statutory asset-income and credit-quality proof remain missing.`

Apollo/Athene answers the current money-movement question at channel level. Retirement and insurance-linked inflows move into Athene-related invested assets and Apollo-managed credit/alternative investment lanes. The channel is economically active because spread-related earnings are visible.

The local evidence shows Q2 `2026` retirement-services gross inflows of `22.069B USD`, Athene-attributable inflows of `17.095B USD`, retirement-services net flows of `11.928B USD`, gross invested assets of `413.598B USD`, net invested assets of `314.090B USD`, gross alternative investments of `20.396B USD`, and spread-related earnings of `877M USD`. FY `2025` evidence adds `302.1B USD` of direct-origination AUM, `282.7B USD` of asset-backed-finance AUM, `392.2B USD` of Athene Accounts AUM, `292.414B USD` of year-end net invested assets, `3.5B USD` of net floating-rate assets, `8.6B USD` of capital available to deploy, and liability-stickiness context from `3` to `20` year surrender-charge periods with a `6%` weighted-average base surrender charge.

That is not yet statutory cash-return proof. The missing layer is legal-entity statutory investment schedules: Schedule D/BA holdings, NAIC designations, investment income by asset class, realized gains/losses, impairments, rating migration, RBC/capital treatment, liability cost, and cash receipt evidence.

## Money Movement

| Question | Current Answer | Boundary |
|---|---:|---|
| Liability inflow source | `22.069B USD` Q2 retirement-services gross inflows | Not allocated to assets or borrowers. |
| Athene-attributable inflows | `17.095B USD` | Not statutory asset allocation proof. |
| Net flow source | `11.928B USD` retirement-services net flows | No surrender/outflow stress bridge. |
| Invested-asset base | `413.598B USD` gross invested assets; `314.090B USD` net invested assets | No Schedule D/BA classification. |
| Alternative exposure | `20.396B USD` gross alternative investments | Alternatives do not equal all private credit. |
| Spread proxy | `877M USD` spread-related earnings | Not asset-class income or risk-adjusted spread. |
| Credit manufacturing scale | `302.1B USD` direct-origination AUM; `282.7B USD` ABF AUM | AUM is not statutory ownership or cash return. |
| Athene account scale | `392.2B USD` Athene Accounts AUM | Managed capital, not legal-entity holdings. |
| Annual invested assets | `292.414B USD` FY2025 net invested assets | No income/gain/loss/impairment by asset class. |
| Rate exposure context | `3.5B USD` net floating-rate assets | Rate offset is not credit-quality proof. |
| Deployment capacity | `8.6B USD` capital available to deploy | Future route not identified. |
| Liability durability | `3` to `20` year surrender-charge periods; `6%` weighted-average base surrender charge | Stickiness proxy, not stress outflow proof. |

## Queue Result

`executed-local-boundary-pass-1`

The row can be upgraded from route-visible-not-local to executed-local boundary status because the local evidence supports the channel, asset-base, credit-lane, spread-earnings, rate-exposure, deployment-capacity, and liability-durability pieces of the graph. It does not pass the full statutory target because the statutory asset-income and credit-quality layer is still missing.

## What This Proves

The current Apollo/Athene answer is:

`retirement/insurance inflows -> Athene-related liability channel -> invested assets / Apollo-managed accounts -> direct origination, ABF, alternatives, and credit lanes -> spread-related earnings proxy`

That is not the same as:

`specific statutory liability source -> specific Schedule D/BA asset -> investment income/cash receipt -> realized gain/loss or impairment -> risk-adjusted spread by asset class`

## Missing Proof

| Missing proof | Why it matters | Next source |
|---|---|---|
| Statutory legal-entity holdings | Needed to prove where Athene liabilities are invested by entity. | Athene state statutory annual and quarterly statements. |
| Schedule D/BA asset detail | Needed to classify bonds, loans, alternatives, affiliated assets, and private-credit exposure. | NAIC Schedule D, Schedule BA, and investment schedules. |
| Investment income by asset class | Needed to prove cash/spread outcome rather than AUM scale. | Statutory investment income exhibits and Apollo/Athene investment income notes. |
| Realized gains/losses and impairments | Needed to test asset quality and credit cost. | Realized gain/loss schedules, impairment notes, and credit-loss detail. |
| NAIC designations and rating migration | Needed to test statutory capital quality. | NAIC designation distribution, rating migration, and RBC/capital notes. |
| Liability cost and spread | Needed to calculate spread after policyholder funding cost. | Crediting-rate/liability-cost schedules and ALM disclosures. |
| Borrower or asset destination | Needed to connect the insurance channel to real-economy recipients. | Borrower-level holdings, private placement schedules, rating reports, and credit agreements. |

## Safe Claim

`Apollo/Athene has liability-channel, invested-asset, and spread-earnings evidence. The local evidence shows 22.069B USD of Q2 2026 retirement-services gross inflows, 17.095B USD of Athene-attributable inflows, 11.928B USD of net flows, 413.598B USD of gross invested assets, 314.090B USD of net invested assets, 20.396B USD of gross alternative investments, 877M USD of spread-related earnings, 302.1B USD of direct-origination AUM, 282.7B USD of asset-backed-finance AUM, 392.2B USD of Athene Accounts AUM, 292.414B USD of FY2025 net invested assets, 3.5B USD of net floating-rate assets, 8.6B USD of capital available to deploy, and liability-stickiness context. This supports channel-level money-movement and spread-proxy language, not statutory asset-income, NAIC credit-quality, realized gain/loss, impairment, liability-cost spread, borrower destination, or asset-level cash-return proof.`

## Next Work

1. Pull Athene legal-entity statutory filings.
2. Extract Schedule D and Schedule BA holdings by asset class, issuer, affiliate status, NAIC designation, and book/market value.
3. Extract statutory investment income, realized gains/losses, impairments, and rating migration.
4. Build a liability-cost/spread bridge by statutory entity.
5. Match private-credit or private-placement holdings to borrower/use/cash evidence where public records allow it.
