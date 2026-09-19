# Walmart H1 FY2027 owner-cash denominator control — 2026-09-15

This memo tightens the Walmart H1 cash denominator by putting the filing's
reinvestment categories, debt principal, share repurchases, and diluted-share
movement in one control surface. It is still a denominator boundary, not a
normalized owner-cash conclusion.

## Filing-backed bridge

Walmart reported H1 operating cash flow of `$19.710B`, capital expenditures of
`$14.181B`, and company-defined free cash flow of `$5.529B`. The filing's
capital-allocation table identifies `$7.659B` of supply-chain, customer-facing,
technology, and other spending; `$3.623B` of store and club remodels;
`$1.087B` of new stores and clubs; and `$1.812B` of international capital
spending. Only the new-store line is a clearly identified growth floor; the
remaining categories cannot be silently treated as maintenance or growth.

The financing statement reports `$2.303B` of debt principal repayment and
`$4.230B` of debt issuance. Walmart also repurchased `$5.104B` of common stock
in H1. Repurchases are a capital-allocation use, not an operating expense, so
they are shown separately rather than subtracted from the owner-cash screen by
default. Diluted weighted-average shares were `7.989B`, versus `8.033B` in the
prior-year H1 period.

## Controlled denominator views

```text
reported cash after property                         $5.529B
less disclosed H1 debt principal repayment           $2.303B
                                                   -------------
post-financing residual screen                       $3.226B

post-financing residual screen                       $3.226B
less H1 common-stock repurchases (separate use)       $5.104B
                                                   -------------
cash after debt and repurchases                      $(1.878B)
```

The second view is not “negative owner cash.” It shows that a cash-after-
property denominator cannot simultaneously be treated as cash available for
debt repayment, repurchases, leases, taxes, attached-service reinvestment, and
all common-owner distributions without an explicit period and priority
waterfall.

## Evidence boundary

| Layer | Status | What remains open |
| --- | --- | --- |
| H1 reported cash after property | `filed-and-reconciled` | Seasonality and working-capital reversal |
| Capex categories | `category-visible` | Maintenance versus growth allocation within supply chain, remodels, technology, and international spending |
| Debt principal | `filed-and-reconciled` | Future maturity, refinancing, and interest burden |
| Share repurchases | `filed-and-reconciled-separate-use` | Whether repurchases are sustainable after normalized operating cash |
| Diluted shares | `filed-and-reconciled` | Future awards, SBC expense/cash dilution, and per-share owner cash |
| Operating leases | `balance-visible-cash-open` | July 31 operating lease obligations total `$16.512B`; H1 lease cash payment is not separately disclosed |
| Income taxes | `provision-visible-cash-paid-open` | H1 tax provision is `$3.141B` on `$15.160B` of pretax income; accrued-tax movement is not cash taxes paid |
| Normalized common-owner cash | `held` | Leases, taxes, supplier finance, attached-service costs, maintenance capital, and annual seasonality |

## September 17 annual category recheck

Walmart's FY2026 annual report provides a historical category control: U.S.
supply chain/customer-facing/technology/other was `$16.468B`, store and club
remodels were `$5.571B`, new stores/clubs including expansions and relocations
were `$1.406B`, and Walmart International was `$3.197B`. The new-store line is
an identified growth floor, but the annual filing still does not disclose the
maintenance share inside the mixed categories. This is a stronger category
observation, not a normalized owner-cash upgrade.

Structured claims: [Walmart H1 denominator CSV](data/combined-investment-research-pilot-02-walmart-h1-owner-cash-denominator-control-2026-09-15.csv).

Primary sources: [Walmart Q2 FY2027 Form 10-Q](https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm) and [Walmart FY2026 annual report](https://stock.walmart.com/_assets/_ef4b3350ef1127ae63b1dd51abb6cf31/walmart/db/950/9988/annual_report/Walmart%2B2026%2BAnnual%2BReport.pdf).
