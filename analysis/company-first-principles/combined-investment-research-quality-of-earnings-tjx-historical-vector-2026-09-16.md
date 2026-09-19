# TJX historical quality-of-earnings input vector

Research date: `2026-09-16`

## Scope and source control

This is the first historical, same-company QoE vector assembled for the
composite screen. It uses TJX fiscal 2024–2026 annual filings, with the
company's own fiscal-year labels preserved. The current-period H1 FY2027
panel remains a separate observation and is not mixed into the annual ratios.

Amounts are USD millions. The working-capital field uses the cash-flow
statement's reported inventory cash use less accounts-payable cash source; it
is not a reconstructed balance-sheet change and is not normalized owner cash.
Debt-and-lease claims include reported operating-lease liabilities and debt
where the annual balance sheet makes the perimeter joinable.

## Historical vector

| Fiscal year | Revenue | Net income | Receivables | Inventory | Accounts payable | Current assets | Net PP&E | D&A | SG&A | Debt + lease claims | SBC | Diluted shares | OCF | Property additions | Equity-investment purchases | Inventory cash use | AP cash source | OCF / NI | Cash after property / NI | Capex / OCF | D&A / PP&E | SBC / NI | Claims / OCF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FY2024 | 54,217 | 4,474 | 529 | 5,965 | 3,862 | 12,664 | 6,571 | 964 | 10,469 | 12,542 | 160 | 1,159 | 6,057 | 1,722 | 0 | 145 | 64 | 1.353822x | 0.968932x | 28.4299% | 14.6705% | 3.5762% | 2.0707x |
| FY2025 | 56,360 | 4,864 | 549 | 6,421 | 4,257 | 12,991 | 7,346 | 1,104 | 10,946 | 12,778 | 183 | 1,142 | 6,116 | 1,918 | 551 | 539 | 448 | 1.257401x | 0.863076x | 31.3604% | 15.0286% | 3.7623% | 2.0893x |
| FY2026 | 60,372 | 5,494 | 602 | 7,297 | 4,575 | 15,202 | 8,220 | 1,247 | 11,515 | 13,489 | 214 | 1,128 | 6,874 | 1,957 | 12 | 724 | 239 | 1.251183x | 0.894976x | 28.4696% | 15.1703% | 3.8952% | 1.9623x |

## Interpretation

- OCF remained above net income in each year, but OCF/NI declined from
  `1.353822x` to `1.251183x`; this is a persistence prompt, not an accusation.
- Cash after property remained positive, while the FY2026 inventory cash use
  less accounts-payable source widened to `$485M`, versus `$91M` in FY2025 and
  `$81M` in FY2024. The cash-flow effect is a timing diagnostic and needs
  inventory-turn and markdown analysis.
- SBC/NI increased across the three years and diluted shares declined. That
  combination requires a per-share cash check rather than treating repurchases
  as proof of value creation.
- The FY2025 `$551M` equity-investment purchase is kept separate from property
  additions; acquisitions and investments cannot be silently treated as
  recurring operating reinvestment.
- TJX states that maintenance and repairs are expensed as incurred, while
  property additions include stores, renovations, offices, distribution, and
  technology. The vector therefore improves historical accrual and cash
  quality, but it does not solve maintenance-versus-growth capital.

## Forensic promotion gate

| Method | What the vector supports | What it does not support | Current treatment |
| --- | --- | --- | --- |
| Sloan-style cash/accrual review | Three annual OCF/NI observations, working-capital cash effects, reinvestment, SBC, and claims | A full persistence regression or normalized owner-cash conclusion | Controlled diagnostic |
| Schilit-style review | Inventory/AP timing, exceptional investment purchases, capitalization boundary, and dilution prompts | A claim that any disclosed item is improper or misleading | Follow-up flags |
| Beneish-style screen | Revenue, receivables, D&A, SG&A, leverage proxy, and sales-growth components are partly visible | Consistent total-assets, gross-margin, expense, and claim taxonomies across the cohort | Not calculated |

The correct conclusion is therefore that TJX has a source-backed historical
earnings-quality diagnostic, not a manipulation score. The next upgrade is to
complete the missing comparable fields and then test whether the warning
signals persist after fiscal-period, accounting-policy, and cash-perimeter
controls.

## Status

`TJX-company-history-partial`. This vector is sufficient for a same-company
three-year diagnostic and a controlled Sloan-style cash/accrual review. It is
not sufficient for a cross-company Beneish score: comparable Target and Walmart
histories, consistent taxonomies, and additional claim/perimeter controls are
still required.

Primary sources: [TJX FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm) and [TJX FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919825000010/tjx-20250201.htm).

Structured rows: [TJX historical vector CSV](data/combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.csv).
