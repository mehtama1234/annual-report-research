# Apollo/Athene statutory income population boundary pass 1

Research date: `2026-09-18`

## Source-defined populations

The 2025 statutory statement uses different population definitions:

| Source | Definition | Period/population |
|---|---|---|
| Page 18 | Exhibit of Net Investment Income | Full-year collected and earned category totals |
| Schedule D Part 1 Sections 1–2 | Long-term bonds owned December 31 of current year | Year-end issuer-credit and ABS holdings |
| Schedule D Part 4 | Long-term bonds and stocks sold, redeemed, or otherwise disposed of during current year | Current-year disposed holdings |
| Schedule D Part 5 | Long-term bonds and stocks acquired during year and fully disposed of during current year | Current-year acquired-and-disposed holdings |

## Consequence

The corrected Schedule D Part 1 row population ties the filing's issuer-credit
and ABS interest subtotals exactly: `$1.504450447B` of interest income due and
accrued and `$6.230478121B` of interest received. That removes missing Part 1
rows as the leading explanation for the page-18 comparison.

It does not establish that Part 1 alone should equal page 18. Page 18 is a
full-year exhibit, while Part 1 is a December 31 holdings population. Current-
year disposals, redemptions, maturities, and assets acquired and fully disposed
during the year are separately presented in Parts 4 and 5. Those populations
can carry current-year interest or dividends received fields, but the existing
disposal extraction remains a consideration worklist rather than a
same-definition income reconciliation.

This is a concrete population-boundary explanation, not a quantified allocation
of the `$1.897374415B` difference. The structured source controls are in the
[population-boundary CSV](data/capital-flow-apollo-athene-statutory-income-population-boundary-pass-1.csv).

## Decision

`schedule-d-part1-subtotals-tied; full-year-income-population-join-open`

The next promotion-quality object is a controlled Part 4/Part 5 interest or
dividend subtotal reconciliation to page 18. Until that exists, no portion of
the page-18 difference is assigned to disposed assets, borrower receipts,
liability-adjusted return, or Apollo common-owner cash.
