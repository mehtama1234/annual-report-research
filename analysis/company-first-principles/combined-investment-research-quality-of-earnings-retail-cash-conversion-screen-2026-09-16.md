# Retail quality-of-earnings cash-conversion screen

Research date: 2026-09-16

## Purpose and boundary

This is the assembled cash-quality component of the [quality-of-earnings and
financial-shenanigans overlay](combined-investment-research-quality-of-earnings-financial-shenanigans-overlay-2026-09-16.md).
It uses the existing 18-row FY2020-FY2026 retail bridge to compare operating
cash flow with property spending and the resulting cash-after-property screen.

The screen is not a Beneish score, an accrual estimate, or a normalized
owner-cash result. It cannot identify earnings manipulation because the source
panel does not provide a complete, comparable net-income, receivable, payable,
inventory, stock-compensation, acquisition, lease, tax, or service-cost vector
for every company-period.

## Definitions

- capex_intensity = property or capex spending / operating cash flow;
- cash_after_property_conversion = cash after property spending / operating
  cash flow; and
- negative_cash_after_property = a diagnostic flag when the mechanical screen
  is below zero.

These ratios describe cash burden and conversion. They do not identify why a
period changed, and they do not permit annual lease or tax cash to be
subtracted again from operating cash flow.

## Result

The panel contains 18 company-period observations. Target FY2022 is the only
negative cash-after-property observation in the current bridge: operating cash
flow was $4.018B against $5.528B of property spending, producing a
-$1.510B mechanical screen. That is a useful stress flag, not proof of
earnings manipulation. Walmart's cash-after-property conversion declined from
71.5% in FY2021 to 35.9% in FY2026, while TJX's FY2026 conversion was
71.5%; scale, investment cycle, working capital, and fiscal-period alignment
remain confounds.

The result is therefore a cash-quality diagnostic: repeated deterioration or a
cash screen that diverges from earnings would trigger the next accrual and
working-capital tests, not a fraud conclusion.

Structured rows: [retail cash-conversion screen CSV](data/combined-investment-research-quality-of-earnings-retail-cash-conversion-screen-2026-09-16.csv).

Primary source bridge: [longitudinal retail bridge](data/combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv).
