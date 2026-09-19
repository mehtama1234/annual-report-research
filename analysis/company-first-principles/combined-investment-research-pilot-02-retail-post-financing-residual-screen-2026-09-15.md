# Pilot 02 retail post-financing residual screen — 2026-09-15

This screen adds disclosed H1 debt-principal repayment to the retail cash
frontier. It is a residual screen, not normalized owner cash: support
recurrence, maintenance capital, leases, taxes, service costs, inventory
seasonality, dilution, and future refinancing remain unresolved.

## Formula

```text
post-financing residual screen = OCF − property spending
  − support-removal assumption
  − SBC sensitivity
  − disclosed debt-principal repayment
```

The debt column uses actual financing-statement repayments where disclosed. A
zero for TJX means no separate H1 debt-principal repayment row was populated in
the reviewed cash-flow statement; it does not mean TJX has no debt obligation.
Debt issuance is shown separately in the source boundary and is not treated as
owner cash.

| Company / period | Cash after property | Support candidate | SBC sensitivity | Debt principal repayment | Reported residual | Support-removed residual | Support+SBC residual | Support+SBC+debt residual |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TJX / H1 FY2027 | `$2.186B` | `$750M` | `$85M` | `$0M` | `$2.186B` | `$1.436B` | `$1.351B` | `$1.351B` |
| Target / H1 2026 | `$2.115B` | `$1.364B` | `$154M` | `$1.070B` | `$2.115B` | `$751M` | `$597M` | `-$473M` |
| Walmart / H1 FY2027 | `$5.529B` | `$4.548B` | `NA` | `$2.303B` | `$5.529B` | `$981M` | `NA` | `-$1.322B` |

The Target and Walmart debt repayments are actual H1 financing cash outflows;
they are not allocations of all debt to the retail operating period. The
negative lower corners are useful precisely because they show that stacking
source-bounded burden candidates can exhaust a reported cash-after-property
screen. They must not be read as reported negative owner cash.

## Promotion boundary

This screen improves the owner-cash bridge by making senior financing claims
visible beside working-capital and support sensitivities. It does not select a
maintenance share, prove support nonrecurrence, allocate attached-service costs,
or normalize the annual period. Status: `source-bounded post-financing
residual; normalized owner cash unresolved`.

Structured result: [post-financing residual CSV](data/combined-investment-research-pilot-02-retail-post-financing-residual-screen-2026-09-15.csv).

Primary sources: [TJX Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm), [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm), and [Walmart Q2 FY2027 Form 10-Q](https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm).
