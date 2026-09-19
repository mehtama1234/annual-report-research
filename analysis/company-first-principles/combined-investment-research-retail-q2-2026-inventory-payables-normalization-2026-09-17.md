# Retail Q2 2026 inventory/payables normalization

## Purpose and period control

This pass tests Q-04 using the latest official interim filings: TJX and Target
as of August 1, 2026 and Walmart as of July 31, 2026, compared with each
company's fiscal-year opening balance. It does not treat the mechanical balance
movement as an additional deduction from operating cash flow.

## Balance-sheet and cash-flow bridge

| Company | Inventory opening → ending | Inventory balance change | Inventory cash-flow change | Payables opening → ending | Payables balance change | Payables cash-flow change | Mechanical inventory less payable change |
|---|---:|---:|---:|---:|---:|---:|---:|
| TJX | $7.297B → $7.862B | +$565M | $(603)M | $4.575B → $5.024B | +$449M | +$470M | $116M use |
| Target | $12.304B → $13.249B | +$945M | $(945)M | $12.622B → $13.306B | +$684M | +$612M | $261M use |
| Walmart | $58.851B → $61.600B | +$2.749B | $(2.660)B | $63.061B → $64.318B | +$1.257B | +$1.648B | $1.492B use |

The mechanical signal is calculated from ending balance changes: inventory
increase less accounts-payable increase. The cash-flow columns are the amounts
reported in each statement of cash flows. They are close but not identical
because of timing, foreign exchange, acquisitions, other operating accounts,
classification, and period-specific reconciliation items.

## Quality-of-earnings interpretation

All three retailers increased inventory and payables over the period. That can
be ordinary seasonal or growth funding, not evidence of manipulation. Walmart
specifically attributes part of the OCF change to the timing of inventory
receipts. The proper test is reversal: subsequent filings should show whether
inventory converts to sales and cash without disproportionate markdowns, while
payables remain within ordinary supplier terms.

The bridge does not support subtracting `$116M`, `$261M`, or `$1.492B` again
from OCF. Doing so would double-count operating working capital already
reflected in the cash-flow statement. Nor does a payable increase prove
supplier finance; that requires the supplier-finance obligation and settlement
schedule.

## Promotion consequence

This improves Q-04's same-period normalization surface but does not close it.
The remaining promotion objects are gross margin/price-volume-mix, markdown and
shrink, supplier-finance settlement, receivable and other operating-account
reconciliation, seasonality, and normalized common-owner cash after capex,
leases, taxes, services, debt, and dilution.

Sources: [TJX Q2 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm), [Target Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm), and [Walmart Q2 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm).

Decision marker: `retail-q2-2026-inventory-payables-normalization-qualified`
