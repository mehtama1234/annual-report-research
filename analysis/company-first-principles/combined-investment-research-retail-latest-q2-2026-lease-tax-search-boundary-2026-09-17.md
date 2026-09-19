# Retail latest Q2 2026 lease-and-tax search boundary

## Result

The latest official interim filings were checked for a same-period cash-paid
lease and income-tax schedule for TJX, Target, and Walmart. The result is
`searched-negative-for-public-interim-payment-lines`, not evidence that the
payments were zero or did not occur.

| Company | Latest filing | Visible controls | Missing payment object |
|---|---|---|---|
| TJX | [Q2 FY2027 Form 10-Q, 26 weeks ended August 1, 2026](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm) | OCF $3.345B; property additions $1.159B; inventory $7.862B; accounts payable $5.024B; operating-lease liabilities $11.446B; income-tax provision $887M; net operating-lease-liability change +$5M; H1 operating-lease cash paid $1.147B | H1 cash-paid income-tax total, maintenance/growth allocation, service-cost allocation, and supplier-finance settlement remain open |
| Target | [Q2 2026 Form 10-Q, six months ended August 1, 2026](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm) | OCF $4.519B; property expenditures $2.404B; inventory $13.249B; accounts payable $13.306B; noncurrent operating-lease liabilities $3.332B; noncash operating-lease additions $84M; tax provision $835M; TTM ROIC table includes $3.733B of lease liabilities and $172M hypothetical lease interest | Supplemental section presents noncash lease additions and a TTM ROIC denominator adjustment, but no H1 cash-paid lease or cash-paid income-tax total |
| Walmart | [Q2 FY2027 Form 10-Q, six months ended July 31, 2026](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm) | OCF $19.710B; property payments $14.181B; inventory cash-flow change $(2.660)B; accounts-payable change +$1.648B; operating-lease obligations $16.512B; tax provision $3.141B; accrued-income-tax change $(211)M | Interim filing does not present cash-paid operating-lease or cash-paid income-tax totals |

## Denominator implication

Lease liabilities, lease expense, tax provision, accrued-tax movement, and
cash-paid taxes are different objects. They cannot be substituted for one
another, and annual cash-paid amounts cannot be inserted into the H1 owner-cash
denominator without period matching. The visible operating-cash-flow changes
also must not be deducted again from OCF.

This boundary therefore records TJX's matched H1 operating-lease burden while
preserving the searched-negative result for cash-paid income taxes at TJX and
both lease and tax payment lines at Target and Walmart. Target's ROIC lease
liability and hypothetical-interest adjustment is a denominator diagnostic, not
an H1 cash payment. It does not close the
retail promotion gate. The remaining requirements are a matched
maintenance/growth capital allocation, service-cost and collection allocation,
supplier-finance settlement, and diluted common-owner residual.

Decision marker: `retail-latest-q2-2026-lease-tax-search-negative-boundary`
