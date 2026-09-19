# Target historical quality-of-earnings input vector

Research date: `2026-09-16`

## Scope and source control

This is the second same-company annual QoE vector for the retail cohort. It
uses Target fiscal 2023–2025 annual filings and preserves the 53-week fiscal
2023 boundary. Target does not separately disclose trade receivables in the
consolidated statement of financial position, so the receivables field remains
missing rather than treating “other current assets” as receivables.

Amounts are USD millions. Inventory and accounts-payable cash effects retain
the signs shown in the cash-flow statement: positive means a source of cash and
negative means a use. Target's debt-plus-lease claim ratio includes current and
long-term debt plus disclosed noncurrent operating-lease liabilities; current
operating-lease cash and liability components are not separately isolated in
the statement and therefore remain a perimeter limitation.

## Historical vector

| Fiscal year | Revenue | Net income | Receivables | Inventory | Accounts payable | Current assets | Net PP&E | D&A | SG&A | Debt + disclosed lease claims | SBC | Diluted shares | OCF | Property additions | Inventory cash effect | AP cash effect | OCF / NI | Cash after property / NI | Capex / OCF | D&A / PP&E | SBC / NI | Claims / OCF |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FY2023 | 107,412 | 4,138 | — | 11,886 | 12,098 | 17,498 | 33,096 | 2,801 | 21,462 | 19,317 | 251 | 462.8 | 8,621 | 4,806 | 1,613 | -1,216 | 2.083374x | 0.921943x | 55.7476% | 8.4633% | 6.0657% | 2.2407x |
| FY2024 | 106,566 | 4,091 | — | 12,740 | 13,053 | 19,454 | 33,022 | 2,981 | 21,969 | 19,522 | 304 | 461.8 | 7,367 | 2,891 | -854 | 1,008 | 1.800782x | 1.094109x | 39.2426% | 9.0273% | 7.4309% | 2.6499x |
| FY2025 | 104,780 | 3,705 | — | 12,304 | 12,622 | 20,005 | 33,749 | 3,134 | 21,535 | 19,918 | 281 | 455.6 | 6,562 | 3,727 | 436 | -501 | 1.771120x | 0.765182x | 56.7967% | 9.2862% | 7.5843% | 3.0354x |

## Interpretation

- OCF/NI declined from `2.083374x` in FY2023 to `1.771120x` in FY2025,
  while claims/OCF rose to `3.0354x`. This is a quality-of-earnings and
  balance-sheet burden prompt, not a manipulation conclusion.
- Cash after property remained positive but fell sharply relative to earnings
  in FY2025. The change must be read alongside Target's rebuilding capex,
  inventory, supplier-finance obligations, and margin-support items.
- The inventory and accounts-payable cash effects reverse direction across the
  period, which is precisely why a single-period cash conversion ratio cannot
  be treated as recurring owner cash.
- Target's 2025 filing separately identifies advertising, credit-card profit
  sharing, marketplace, membership, and other revenue. Those streams remain
  outside normalized owner cash until costs, working capital, capital, tax, and
  collection are allocated.

## Forensic promotion gate

| Method | What the vector supports | What it does not support | Current treatment |
| --- | --- | --- | --- |
| Sloan-style cash/accrual review | Three annual OCF/NI, working-capital, reinvestment, SBC, and claim observations | A complete receivables-based accrual history because Target does not separately disclose trade receivables | Controlled diagnostic with a missing-field boundary |
| Schilit-style financial-shenanigans review | Inventory/AP reversals, margin-support and attached-service prompts, capitalization, supplier-finance, and dilution review | A claim that Target's disclosed support or service streams are improper | Follow-up flags |
| Beneish-style screen | Revenue growth, inventory, D&A, SG&A, leverage proxy, and sales-growth inputs are partly visible | Receivables and fully comparable cohort taxonomies | Not calculated |

Target is therefore useful as a controlled stress history and a high-priority
follow-up, but its missing receivables field is a hard stop for a full
Beneish-style screen.

## Status

`Target-company-history-partial`. This vector supports a controlled
same-company annual diagnostic and creates a second comparable history for the
retail cohort. It does not complete a cross-company Beneish score because
receivables and certain lease/perimeter fields remain unavailable or
non-comparable, and Walmart's annual vector is still outstanding.

Primary sources: [Target FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm) and [Target FY2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741925000018/tgt-20250201.htm).

Structured rows: [Target historical vector CSV](data/combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.csv).
