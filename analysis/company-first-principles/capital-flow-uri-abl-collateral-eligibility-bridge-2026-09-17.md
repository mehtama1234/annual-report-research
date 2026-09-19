# URI ABL collateral-eligibility and availability bridge

## Purpose

This pass upgrades the United Rentals industrial-uptime lane from a generic
borrowing-base request to a documented collateral-control model. It joins the
filed ABL agreement to the latest 10-Q, but it does not treat facility capacity
as a populated borrowing-base certificate, free cash, or fleet lifecycle return.
The structured [evidence table](data/capital-flow-uri-abl-collateral-eligibility-bridge-2026-09-17.csv)
preserves each observed field and each missing join.

## What the agreement actually controls

The July 10, 2025 amended and restated ABL agreement identifies United Rentals
(North America), Inc. as borrower, United Rentals, Inc. as Holdings, Bank of
America as agent, and the U.S., Canadian, ROW, European, and ANZ borrower
perimeter. Its definition of a Borrowing Base Certificate requires the
borrowers' agent to calculate both U.S. and Canadian borrowing bases, including
each component and applicable reserves.

The collateral is not simply all rental equipment. Eligible Rental Equipment
must be held for sale or rent, rented as lessor in the ordinary course, or be
specified titled goods. The agreement also requires the equipment to satisfy
location, lien, representation, and regulatory-standards conditions; equipment
that ceases to qualify must be removed from eligibility. The agent can change
eligibility criteria after notice when conditions materially impair collateral
quality.

The resulting control chain is:

`rental fleet -> eligibility filters -> NBV / NOLV and reserves -> U.S. and Canadian borrowing bases -> Combined Availability -> facility draws and covenant triggers`

The agreement defines Combined Availability as the lesser of the maximum
revolver amount and Combined Borrowing Base, less aggregate revolver
outstandings. It requires a quarter-end certificate by the 25th day of the next
month, plus a monthly certificate when availability falls below the stated
65% trigger unless the specified exception is satisfied. The closing condition
also confirms that a May 31, 2025 certificate was delivered and that closing
Combined Availability had to be at least `$1.000B`.

## What the Q2 2026 filing adds

URI's June 30, 2026 10-Q reports `$2.802B` of ABL borrowing capacity net of
letters of credit, `$1.666B` of ABL debt, a 4.7% ABL rate, and `$2.999B` of
total available liquidity including cash and receivables-facility capacity.
It also says specified availability exceeded the required threshold, so the
ABL fixed-charge covenant was not applicable. The filing says seasonal
expenditures caused maximum month-end ABL debt of `$1.677B` to exceed the
`$1.391B` average month-end amount.

These are useful liquidity and seasonality observations, but they are not the
collateral proof. The public filing does not provide the quarter-end eligible
fleet NBV, NOLV appraisal, reserve schedule, letter-of-credit deductions,
Combined Borrowing Base, Suppressed Availability, or source-to-purchase draw
allocation.

## Investment and QoE implication

The key quality-of-earnings risk is denominator substitution: a reader could
mistake `$2.802B` capacity or `$2.999B` liquidity for unencumbered fleet value,
or mistake `$1.666B` debt for the debt actually funding the `$2.720B` of
gross rental-equipment purchases in the broader H1 cash bridge. The agreement
shows why that shortcut is unsafe: eligibility, appraisals, reserves, and
agent judgment sit between fleet ownership and legal availability.

The current conclusion is therefore:

`eligibility-and-reporting-control-visible; populated collateral and lifecycle return unproven`

This is a real cross-sector insight: asset-backed liquidity is a contractual
measurement system, not a balance-sheet ratio. To promote URI, the next object
must contain populated collateral components and a period-matched source-to-
purchase/use bridge. The work should not infer those values from total fleet
NBV, reported liquidity, resale proceeds, or OCF.

## Sources

- [URI July 2025 fifth amended and restated ABL credit agreement](https://www.sec.gov/Archives/edgar/data/1047166/000110465925067406/tm2520569d1_ex10-1.htm)
- [URI Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1067701/000106770126000026/uri-20260630.htm)

