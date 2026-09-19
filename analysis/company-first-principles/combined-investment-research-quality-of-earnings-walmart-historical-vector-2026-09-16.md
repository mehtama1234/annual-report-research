# Walmart historical quality-of-earnings input vector

Research date: `2026-09-16`

## Scope and source control

This is the third same-company annual QoE vector for the retail cohort. It
uses Walmart fiscal 2024–2026 annual filings and keeps two earnings bases
visible: consolidated net income is the starting point of the cash-flow
statement, while net income attributable to Walmart is the denominator for
common-owner cash conversion. Noncontrolling interest is not silently folded
into the common-owner result.

Amounts are USD millions. Walmart's own free-cash-flow convention is
operating cash flow less payments for property and equipment; acquisitions
and strategic-investment disposals are shown separately and are not hidden in
that property-only measure. Supplier-finance obligations are also shown
separately because Walmart says they are generally classified in accounts
payable and operating cash flow.

## Historical vector

| Fiscal year | Total revenue | Consolidated NI | Attributable NI | NCI | Receivables | Inventory | Accounts payable | Current assets | Net PP&E | D&A | OSG&A | Debt + lease claims | SBC | Diluted shares | OCF | Property additions | Acquisitions | Strategic investment disposals | Inventory cash effect | AP cash effect | Supplier finance obligations | OCF / attributable NI | Cash after property / attributable NI | Capex / OCF | D&A / PP&E | SBC / attributable NI | Claims / OCF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FY2024 | 648,125 | 16,270 | 15,511 | 759 | 8,796 | 54,892 | 56,812 | 76,877 | 110,810 | 11,853 | 130,971 | 51,321 | 2,093 | 8,108 | 35,726 | 20,606 | 9 | — | 2,017 | 2,515 | — | 2.303269x | 0.974792x | 57.6779% | 10.6967% | 13.4936% | 1.4365x |
| FY2025 | 680,985 | 20,157 | 19,436 | 721 | 9,975 | 56,435 | 58,666 | 79,458 | 119,993 | 12,973 | 139,884 | 60,114 | 2,769 | 8,081 | 36,443 | 23,783 | 1,896 | 4,080 | -2,755 | 3,228 | 5,725 | 1.875026x | 0.651369x | 65.2608% | 10.8115% | 14.2468% | 1.6495x |
| FY2026 | 713,163 | 22,270 | 21,893 | 377 | 11,172 | 58,851 | 63,061 | 84,874 | 136,083 | 14,203 | 147,943 | 67,095 | 3,603 | 8,022 | 41,565 | 26,642 | 53 | 927 | -1,443 | 1,611 | 5,989 | 1.898552x | 0.681633x | 64.0972% | 10.4370% | 16.4573% | 1.6142x |

## Interpretation

- Attributable OCF/NI declined from `2.303269x` in FY2024 to `1.898552x` in
  FY2026, while property-only cash after capex remained positive but below
  one times attributable earnings in FY2026. This is a cash-conversion and
  capital-intensity prompt, not a manipulation conclusion.
- Inventory was a use of cash in FY2025 and FY2026, while accounts payable was
  a source. The working-capital pair must be read together with supplier
  finance, which ended at `$5.989 billion` in FY2026 and is generally included
  in accounts payable.
- SBC rose from `$2.093 billion` to `$3.603 billion`, and the SBC/attributable
  NI ratio rose from `13.4936%` to `16.4573%`. That is a dilution and
  owner-claim input for the common-owner bridge, not proof that reported
  earnings are fictitious.
- Claims include short-term borrowings, current and long-term debt, and
  current and long-term operating and finance lease obligations. Supplier
  finance is displayed separately and is not double-counted in that total.
- Walmart's OSG&A presentation is not a direct equivalent of the SG&A fields
  in the TJX and Target vectors. The three histories are therefore comparable
  for cash, working-capital, capex, claims, and dilution diagnostics, but not
  as a mechanically interchangeable margin line.

## Forensic promotion gate

| Method | What the vector supports | What it does not support | Current treatment |
| --- | --- | --- | --- |
| Sloan-style cash/accrual review | Three annual attributable OCF/NI, working-capital, supplier-finance, reinvestment, SBC, NCI, and claim observations | A common-owner persistence estimate that ignores NCI, supplier finance, or the property-only cash convention | Controlled diagnostic |
| Schilit-style financial-shenanigans review | Supplier-finance presentation, acquisitions/disposals, OSG&A classification, capital intensity, and dilution prompts | A conclusion that payable classification or supplier finance is improper without settlement evidence | Follow-up flags |
| Beneish-style screen | Revenue, receivables, inventory, D&A, leverage proxy, and growth inputs are visible | OSG&A is not a directly equivalent SG&A field, and the cohort still lacks fully aligned claims and transaction taxonomies | Not calculated |

Walmart's vector is therefore strong for cash, claim, and dilution diagnostics,
but its scale and presentation differences must remain visible before any
cross-company composite is attempted.

## Status

`Walmart-company-history-partial`. This completes the third controlled annual
retail history and strengthens the quality-of-earnings overlay. It does not
complete a cross-company Beneish score or establish fraud; several fields
still require taxonomy normalization and the broader composite remains
explicitly unassembled.

Primary sources: [Walmart FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm) and [Walmart FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/wmt-20250131.htm).

Structured rows: [Walmart historical vector CSV](data/combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.csv).
