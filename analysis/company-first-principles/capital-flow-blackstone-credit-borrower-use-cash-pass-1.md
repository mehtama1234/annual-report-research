# Capital Flow Blackstone Credit Borrower Use Cash Pass 1

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-015`.

The question is:

`Can Blackstone credit-channel evidence be upgraded from vehicle/source visibility to borrower use, interest income, repayment, and cash-return evidence?`

The evidence table is:

`analysis/company-first-principles/data/capital-flow-blackstone-credit-borrower-use-cash-pass-1.csv`

## Short Answer

`Blackstone has credit and insurance channel scale plus borrower candidate evidence, but borrower-use and cash-return proof remain incomplete.`

Blackstone answers the money-movement question at channel, vehicle, industry, and borrower-candidate level. Capital flows into Blackstone Credit & Insurance, into direct-lending and infrastructure/asset-based strategies, into insurance SMAs and BCRED-like perpetual capital, and into BXSL industry exposures. Separate borrower work identifies Auctane/Stamps.com, Guidehouse, and Medallia as useful private-credit borrower candidates.

The local evidence shows `469.3B USD` of Credit & Insurance AUM, `318.241B USD` of Credit & Insurance fee-earning AUM, `31.0B USD` of quarterly Credit & Insurance inflows, `143.0B USD` of LTM Credit & Insurance inflows, `13.3B USD` of global direct-lending strategy inflows, `1.0B USD` of BCRED equity raised, `9.9B USD` of infrastructure and asset-based credit strategy inflows, `7.5B USD` of insurance SMA inflows, `12.7B USD` of quarterly Credit & Insurance capital deployed, `3.9%` LTM private-credit net return, and `373.242M USD` of Credit & Insurance segment distributable earnings.

The BXSL evidence adds a public vehicle denominator: `13.364295B USD` of portfolio base, with the largest industry destinations including Software at `2.525852B USD`, Health Care Providers & Services at `1.376522B USD`, Professional Services at `1.376522B USD`, Insurance at `1.336430B USD`, and Commercial Services & Supplies at `1.109236B USD`.

The borrower-candidate layer is promising but not complete. Auctane/Stamps.com has a `6.6B USD` transaction value and `2.775B USD` of debt or new capital with Blackstone Credit named among current/private-credit lenders in prior work. Guidehouse has a `5.3B USD` transaction value and `3.075B USD` of debt context. Medallia has a `6.4B USD` transaction value and `1.8B USD` debt context with Blackstone-linked lender/control evidence. Those candidates do not yet prove Blackstone vehicle allocation, borrower cash flow, repayments, or realized return.

## Money Movement

| Question | Current Answer | Boundary |
|---|---:|---|
| Credit/insurance platform | `469.3B USD` AUM | Platform scale, not borrower cash. |
| Fee-earning base | `318.241B USD` | Manager economics, not source/use proof. |
| Current inflows | `31.0B USD` Q2 inflows | Not assigned to vehicles or borrowers. |
| Sustained inflows | `143.0B USD` LTM inflows | No deployment-by-borrower map. |
| Direct lending lane | `13.3B USD` Q2 inflows | Borrower recipients missing. |
| BCRED/perpetual capital | `1.0B USD` equity raised | No funded loan allocation in this pass. |
| Infrastructure/ABF lane | `9.9B USD` Q2 inflows | Collateral and borrower use missing. |
| Insurance client channel | `7.5B USD` insurance SMA inflows | Client capital, not owned insurance liabilities. |
| Deployment | `12.7B USD` quarterly deployed | Deal list and cash returns missing. |
| Private-credit performance | `3.9%` LTM net return | Strategy return, not borrower cash proof. |
| Segment earnings | `373.242M USD` distributable earnings | Manager segment economics. |
| BXSL vehicle denominator | `13.364295B USD` portfolio base | Needs named borrower cash detail. |
| BXSL destinations | Software, healthcare, professional services, insurance, commercial services | Industry map, not use-of-proceeds proof. |
| Borrower candidates | Auctane, Guidehouse, Medallia | Not final Blackstone vehicle/cash return proof. |

## Queue Result

`executed-local-boundary-pass-1`

The row can be upgraded from route-visible-not-local to executed-local boundary status because local evidence now ties Blackstone's credit/insurance channel to strategy inflows, deployment, a public vehicle denominator, industry destinations, and named borrower candidates. It does not pass the full target because borrower-use and cash-return evidence remain incomplete.

## What This Proves

The current Blackstone answer is:

`institutional / wealth / insurer-client capital -> Blackstone Credit & Insurance -> direct lending, insurance SMA, infrastructure and asset-based credit, BCRED, and BXSL-like vehicles -> industry exposures and borrower candidates -> strategy/segment return proxies`

That is not the same as:

`specific vehicle funding -> specific borrower facility -> use of proceeds -> borrower cash flow -> interest/principal repayment -> realized return`

## Missing Proof

| Missing proof | Why it matters | Next source |
|---|---|---|
| Vehicle funding stack | Needed to know whether money came from BXSL, BCRED, SMA, drawdown fund, or insurer client. | BXSL/BCRED filings, N-PORT schedules, SMA holdings, and fund financials. |
| Borrower facility allocation | Needed to know Blackstone's funded amount and tranche. | Credit agreements, lender schedules, and administrative-agent records. |
| Use of proceeds | Needed to connect capital to acquisition, refinancing, growth, dividend, or working-capital use. | Debt commitment letters, merger proxies, payoff letters, and borrower disclosures. |
| Borrower cash flow | Needed to test repayment capacity. | Borrower financials, rating reports, lender presentations, and sponsor updates. |
| Interest income and repayment | Needed for cash-return evidence. | Vehicle interest-income detail, repayment records, non-accrual schedules, and realized gains/losses. |
| Bank role | Needed to prove bank displacement or residual bank participation. | Prior credit agreements, payoff letters, revolvers, agent roles, and ancillary bank services. |

## Safe Claim

`Blackstone has credit and insurance channel scale plus borrower candidate evidence. The local evidence shows 469.3B USD of Credit & Insurance AUM, 318.241B USD of fee-earning AUM, 31.0B USD of Q2 inflows, 143.0B USD of LTM inflows, 13.3B USD of direct-lending inflows, 1.0B USD of BCRED equity raised, 9.9B USD of infrastructure and asset-based credit inflows, 7.5B USD of insurance SMA inflows, 12.7B USD of quarterly deployed capital, 3.9% LTM private-credit net return, 373.242M USD of segment distributable earnings, a 13.364295B USD BXSL portfolio base, industry destination exposure, and borrower candidates including Auctane/Stamps.com, Guidehouse, and Medallia. This supports channel/vehicle/industry/borrower-candidate money-movement language, not borrower-use, interest income, repayment, cash-return, or bank-displacement proof for a specific Blackstone-funded facility.`

## Next Work

1. Extract BXSL and BCRED schedules of investments into named borrower/facility rows.
2. Join Auctane, Guidehouse, and Medallia borrower records to Blackstone vehicle exposure where available.
3. Pull credit agreements, lender schedules, debt commitment letters, and payoff letters.
4. Extract borrower interest income, repayment, non-accrual, and realized gain/loss evidence from vehicle filings.
5. Build a bank-role map distinguishing prior facility payoff from residual revolver, agent, hedging, and ancillary-bank roles.
