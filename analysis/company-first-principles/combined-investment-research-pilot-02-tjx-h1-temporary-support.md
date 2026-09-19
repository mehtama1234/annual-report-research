# TJX H1 FY2027 temporary-support bridge

Research date: `2026-09-15`

This artifact isolates identifiable H1 FY2027 support from TJX's reported
`$2.186B` cash-after-property bridge. It is a sensitivity input, not a claim
that every dollar should be subtracted from owner cash.

## Source-backed support

| Item | Amount | Treatment | Boundary |
| --- | ---: | --- | --- |
| IEEPA tariff refunds received | `$331M` | Cash-support candidate | Refund was received and recognized in cost of sales; additional refunds were not recorded as a receivable at August 1, 2026 |
| Related incentive and discretionary-bonus accrual | `$112M` | Expense offset, not cash receipt | It reduces the tariff benefit but its eventual cash payment timing is unresolved |
| Net tariff pretax benefit | `$219M` | Earnings-support candidate | Company-reported net benefit after the `$112M` accrual |
| Credit-card interchange settlement | `$419M` net accounting gain (`$470M` gross gain less `$51M` legal expense) | Non-recurring support sensitivity; cash amount not separately quantified in the H1 statement | Amounts related to the settlement were received during the quarter ended May 2, 2026, but the filing does not isolate the bank receipt, legal-payment timing, or tax |
| Combined temporary-support screen | `$750M` mechanical screen | Derived sensitivity only, not observed cash | `$331M` tariff refund plus `$419M` net settlement gain; do not present this as a proven H1 owner-cash deduction |

## H1 reported-cash sensitivity

TJX reported `$3.345B` of H1 operating cash flow and `$1.159B` of property
additions, or `$2.186B` cash after property. A simple source-bounded screen is:

```text
reported cash after property                         2,186M
- identified temporary cash-support candidate          750M
- share-based compensation                              85M
= low screen cash                                     1,351M

reported cash after property                         2,186M
- share-based compensation                              85M
= base screen cash                                    2,101M

high screen: reported cash after property             2,186M
```

The low case is intentionally mechanical. The tariff refund may offset a
genuine cost that would otherwise recur, the settlement is clearly non-
recurring, and stock compensation is a claim/dilution issue rather than a
straight cash subtraction. The screen therefore exposes sensitivity rather
than declaring `$1.351B` to be owner cash.

## Primary sources

- [TJX Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm)
- [TJX Q2 FY2027 earnings release and adjusted results](https://investor.tjx.com/node/21536/html)
