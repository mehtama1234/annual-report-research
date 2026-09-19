# Current retail quality-of-earnings composite input panel

Research date: `2026-09-16`

## Purpose

This panel advances the [composite QoE input schema](combined-investment-research-quality-of-earnings-composite-input-schema-2026-09-16.md)
for one matched six-month period across TJX, Target, and Walmart. It is an
input panel, not a Beneish score and not a fraud finding. A field is populated
only when the filing supplies a comparable amount and perimeter; an empty field
is retained as missing rather than inferred from a nearby line item.

Amounts are in USD millions unless stated otherwise. Walmart uses net income
attributable to Walmart and diluted shares for the common-owner denominator;
consolidated net income and noncontrolling interest remain separately visible
in the filing.

## Current-period panel

| Company / period | Revenue | Net income | Receivables | Inventory | Accounts payable | Current assets | Net PP&E | D&A | SG&A | Debt/lease claims | SBC | Diluted shares | OCF | Property spending | Input status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| TJX / H1 FY2027 | 29,503 | 2,852 | 665 | 7,862 | 5,024 | 15,329 | 8,567 | 676 | 5,879 | 14,317 debt + lease liabilities | 85 | 1,118 | 3,345 | 1,159 | partial: SG&A and debt/lease are present, but full composite perimeter still needs reconciliation |
| Target / H1 2026 | 51,982 | 2,658 | — | 13,249 | 13,306 | 20,928 | 34,767 | 1,597 | 11,286 | — | 154 | 456.2 | 4,519 | 2,404 | partial: receivables and a clean combined debt/lease claim are not separately disclosed in the extracted statement |
| Walmart / H1 FY2027 | 361,784 | 11,696 attributable | 11,075 | 61,600 | 64,318 | 88,703 | 142,482 | 7,746 | — | 73,755 debt + lease obligations | — | 7,989 | 19,710 | 14,181 | partial: SG&A and SBC are not isolated in the current panel; NCI is separately controlled |

## Interpretation

The panel supports three concrete QoE observations:

1. All three companies show positive reported-period OCF after property
   spending, but that screen remains exposed to inventory, payable, supplier-
   finance, temporary-support, maintenance-capital, lease, tax, and dilution
   adjustments.
2. Target's current earnings and cash panel must remove or separately model the
   `$994M` tariff refund recognized in the six-month filing and the `$3.2B` of
   vendor obligations eligible for early payment. These are disclosed economic
   inputs, not allegations of improper accounting.
3. Walmart's common-owner screen must retain the `$323M` six-month
   noncontrolling-interest deduction from consolidated net income and must not
   treat its company-defined free cash flow as unrestricted owner cash.

The panel therefore changes several composite inputs from globally missing to
current-period observed or partial, but it does not assemble a multi-period
composite score. Promotion still requires fiscal-history alignment, consistent
receivable and SG&A taxonomies, supplier-finance treatment, maintenance versus
growth capital, and a common claim perimeter.

## Primary sources

- [TJX Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm)
- [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm)
- [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm)

Structured rows: [current retail composite input panel CSV](data/combined-investment-research-quality-of-earnings-current-retail-composite-input-panel-2026-09-16.csv).
