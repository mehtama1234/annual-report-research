# Pilot 02 retail interim lease-and-tax search boundary

Research date: `2026-09-16`

## Purpose

Test the latest interim filings for dedicated cash-paid operating-lease and
cash-tax lines that could be matched to the current H1 retail cash screens.

## Result

The checked H1/Q2 filings expose TJX H1 operating-lease cash paid of `$1.147B`,
but do not expose a matched TJX cash-tax line or comparable cash-paid lease/tax
schedule for Target or Walmart. They also expose operating cash flow and
related balance/provision observations—for example, TJX reports H1 operating
cash flow of `$3.345B`, a `$5M` increase in net operating lease liabilities,
and a `$64M` deferred-tax provision; Target reports H1 operating cash flow of
`$4.519B` and an `$835M` tax provision; Walmart reports H1 operating cash flow
of `$19.710B`, a `$(211M)` accrued-income-tax change, and a `$3.141B` tax
provision. None of the provisions or balance movements is substituted for
cash taxes paid, and Target/Walmart annual lease cash is not substituted for
H1 cash lease payments.

| Company | Interim period | Dedicated cash lease line | Dedicated cash tax line | Result |
| --- | --- | --- | --- | --- |
| TJX | Twenty-six weeks ended August 1, 2026 | `$1.147B` operating cash paid | Not located in checked 10-Q HTML | `lease-cash-visible; tax-cash-searched-negative` |
| Target | Six months ended August 1, 2026 | Not located in checked 10-Q HTML | Not located in checked 10-Q HTML | `searched-negative` |
| Walmart | Six months ended July 31, 2026 | Not located in checked 10-Q HTML | Not located in checked 10-Q HTML | `searched-negative` |

This is a public-disclosure boundary, not evidence that the companies made no
lease or tax payments. The annual cash-paid observations therefore remain
useful calibration controls, but they cannot be carried into the current H1
denominator as if they were matched-period data.

## Annual calibration controls

The latest annual filings provide the following source-backed benchmarks for
the missing fields: TJX FY2026 reports `$2.214B` of operating-lease cash paid
and `$1.471B` of income taxes paid; Target FY2025 reports `$529M` and
`$1.091B`, respectively; Walmart FY2026 reports `$2.315B` and `$5.364B`,
respectively. These figures are useful for scale and accounting-treatment
calibration only. They are not substituted into the H1 denominator because
the fiscal periods and cash timing do not match the current interim screens.

| Company | Annual period | Operating-lease cash paid | Income taxes paid | Source boundary |
| --- | --- | ---: | ---: | --- |
| TJX | FY2026 ended January 31, 2026 | `$2.214B` | `$1.471B` | Annual benchmark; not an H1 input |
| Target | FY2025 ended January 31, 2026 | `$529M` | `$1.091B` | Annual benchmark; not an H1 input |
| Walmart | FY2026 ended January 31, 2026 | `$2.315B` | `$5.364B` | Annual benchmark; not an H1 input |

## Consequence for CA-06

The H1 cash-after-property screens remain source-bounded. Do not annualize or
allocate the annual lease/tax values into H1 without a disclosed interim cash
line or a reproducible cash-flow reconstruction. The next upgrade is the next
quarterly or annual filing, plus any supplemental cash-flow disclosure that
provides matched-period cash taxes and lease payments.

## Primary sources

- [TJX Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm)
- [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm)
- [Walmart Q2 FY2027 Form 10-Q](https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm)
- [TJX FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
- [Target FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm)
- [Walmart FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm)

Structured result: [interim lease-and-tax search CSV](data/combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.csv).

## September 18, 2026 official-HTML recheck

The SEC-hosted Q2 HTML for all three companies was rechecked against the
specific missing-object question. Target's six-month cash-flow statement
reports `$4.519B` of OCF and `$2.404B` of property spending, plus noncash lease
origination disclosures of `$84M` operating-lease assets and `$18M` finance-
lease assets; it does not provide a cash-paid lease or cash-tax line. Its ROIC
note reports `$3.733B` of operating-lease liabilities and trailing taxes, but
those are classification/annual context, not H1 cash.

Walmart's six-month cash-flow statement reports `$19.710B` of OCF and
`$14.181B` of property payments, with a `$(211)M` accrued-income-tax change;
the checked HTML does not provide a dedicated cash-tax or cash-paid operating-
lease schedule. The accrued-tax movement is not substituted for taxes paid.

TJX's six-month statement reports `$3.345B` of OCF and `$1.159B` of property
additions, a `$5M` increase in net operating-lease liabilities, `$(60)M` of
income taxes recoverable, and `$190M` of income taxes payable. These are
working-capital or liability movements, not a dedicated cash-tax line. The
recheck therefore adds no promotion-ready H1 lease/tax cash object:

`TJX lease cash visible from the prior packet; Target/Walmart lease and tax cash searched-negative; all H1 tax movements noncash/working-capital controls`

This confirms the existing stop rule: annual lease/tax cash and balance-sheet
movements cannot be inserted into the H1 owner-cash denominator without a
matched cash schedule.

## September 18, 2026 inline-XBRL tag recheck

The SEC-hosted inline-XBRL HTML was also searched for dedicated matched-period
cash facts, not only visible table labels. Neither Target nor Walmart exposed
`PaymentsOfIncomeTaxes`, `OperatingLeasePayments`, or an equivalent dedicated
H1 cash-payment fact. The filings do expose tax-provision and accrued-tax or
working-capital fields, which remain controls rather than cash-payment
evidence. This strengthens the searched-negative classification without
implying that no cash payments occurred.

Sources: [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm) and [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm).

Structured tag-level result: [inline-XBRL search ledger](data/combined-investment-research-pilot-02-retail-interim-inline-xbrl-search-2026-09-18.csv).

## September 18, 2026 ordinary-language phrase recheck

The same SEC-hosted HTML filings were searched for the ordinary-language
phrase `cash paid` and nearby lease-liability disclosures. No additional
matched-period cash-payment schedule was exposed. Target's filing provides
operating-lease liabilities, noncash leased-asset additions, and a trailing-
twelve-month ROIC framework that adds operating-lease interest; Walmart's
filing provides accrued-income-tax movements, operating-lease balances, and
property payments. These are classification and burden controls, not H1 cash
taxes or operating-lease payments. The expanded phrase search strengthens the
searched-negative boundary but does not prove that no such payments occurred.
