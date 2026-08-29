# Capital Flow URI ABL Borrowing-Base Definitions Pass 1

## Purpose

This pass answers the next narrow URI question:

`Can we extract how the ABL borrowing base is calculated and monitored, without pretending we have the live certificate?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-abl-borrowing-base-definitions-pass-1.csv`

## Source

This pass uses the actual July `2025` ABL agreement:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-tm2520569d1_ex10-1.htm`

The prior ABL agreement-mechanics pass established the facility size, maturity, disclosed reset-date draw/availability snapshot, pricing, sublimits, springing covenant, cash-dominion trigger, and security-agreement collateral categories.

This pass goes one layer deeper into the borrowing-base formula.

## Formula Mechanics

| Term | Extracted Mechanic | Why It Matters |
|---|---:|---|
| U.S. merchandise and consumables inventory formula | `60%` of value of eligible merchandise and consumables inventory | Inventory receives partial borrowing-base credit. |
| U.S. eligible rental equipment | lesser of `100%` net book value and `85%` net orderly liquidation value | Fleet collateral is capped by both accounting value and liquidation-value appraisal. |
| Canadian eligible rental equipment | lesser of `100%` net book value and `85%` net orderly liquidation value | Canadian borrowing base is also rental-equipment driven. |
| U.S. borrowing base | inventory formula plus rental-equipment formula, less reserves | Headline collateral becomes legal capacity only after formula and reserve deductions. |
| Canadian borrowing base | rental-equipment formula less reserves | Canadian borrowing capacity is separately calculated. |
| Combined borrowing base | U.S. base plus lesser of Canadian base and Canadian maximum revolver amount | Canadian contribution is capped inside combined availability. |
| Combined availability | lesser of maximum revolver amount and combined borrowing base, less aggregate revolver outstandings | Availability is constrained by both facility size and eligible collateral. |
| Suppressed availability | combined borrowing base minus maximum revolver amount | Agreement tracks collateral value above the headline revolver cap. |

## Eligibility Mechanics

Eligible rental equipment is not all fleet at face value.

The agreement excludes or conditions equipment based on:

- balance-sheet classification
- clean ownership and lien status
- location and landlord-control conditions
- negotiable document-of-title control
- excess, obsolete, unsaleable, unrentable, materially damaged, or unfit status
- ordinary-course sale/rental/use status
- first-priority lien status
- material breaches of equipment representations
- regulatory standards

Eligible merchandise and consumables inventory is also bounded. It must generally have good title, avoid material damage/defect, avoid obsolete/unmerchantable/slow-moving status, satisfy security-interest and location requirements, and exclude fuel plus extraneous unboxed inventory.

## Reporting And Control Mechanics

The agreement requires recurring borrowing-base reporting:

- quarterly Borrowing Base Certificates as of each fiscal-quarter end
- due by the `25th` day of the following calendar month
- monthly certificates if daily Combined Availability falls below `65%` of Maximum Revolver Amount on any day, subject to exceptions
- pro forma acquisition/investment borrowing-base adjustments before appraisal capped at `1.250B USD`
- Agent review and adjustment rights using reasonable credit judgment
- reserve-setting rights, subject to notice and anti-duplication limits

The appraisal and inspection mechanics matter because the rental-equipment value limiter is not just book value.

The agreement defines:

- Net Book Value as cost less accumulated depreciation under GAAP
- Net Orderly Liquidation Value as orderly liquidation value, net of estimated liquidation costs and expenses, determined by the most recent appraisal
- Appraisal as a report setting forth NOLV of rental equipment
- baseline inspection limits of once per `12` months absent continuing default
- additional inspection/appraisal rights if Specified Availability is below `20%` of Maximum Revolver Amount for `20` consecutive business days
- borrower consent to use Rouse Asset Services as an appraiser

## What This Adds

This upgrades the URI ABL work from:

`agreement-term-visible`

to:

`borrowing-base-definition-visible`

It still does not make URI borrowing-base-grade.

The difference is important:

- We now know the legal formula and controls.
- We do not yet know the live eligible collateral balances, reserve balances, appraisal values, or current legal availability.

## Safe Claim

`URI's ABL capacity is formula-bound: U.S. borrowing-base value includes 60% of eligible merchandise and consumables inventory plus eligible rental equipment capped at the lesser of 100% net book value and 85% net orderly liquidation value, minus reserves; Canadian borrowing-base value uses the same 100% NBV / 85% NOLV rental-equipment limiter, minus reserves. The agreement also requires recurring Borrowing Base Certificates, permits agent reserve adjustments, and ties NOLV to appraisals.`

## Claims Not To Make Yet

Do not say:

- the current borrowing base is known
- the current legal availability is proven
- eligible rental-equipment dollars are known
- reserve amounts are known
- appraisal values are known
- all OEC is eligible collateral
- the ABL funded specific fleet purchases
- fleet ROIC is proven

## Next Concrete Work

The next URI evidence gates are:

1. Find actual Borrowing Base Certificates or collateral reports.
2. Extract eligible rental equipment, eligible inventory, reserves, and L/C usage if certificates are available.
3. Reconcile Q2 `2026` debt-note availability to agreement-defined Combined Availability.
4. Locate appraisal or rating-agency collateral commentary.
5. Join borrowing-base capacity to fleet utilization, OEC, age, growth/replacement capex, and rental revenue.

The immediate certificate source-boundary pass is:

`analysis/company-first-principles/capital-flow-uri-abl-borrowing-base-certificate-source-boundary-pass-1.md`
