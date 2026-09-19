# Retail quality-of-earnings comparability bridge

Research date: `2026-09-16`

## Purpose

This bridge is the promotion control between the three same-company annual
QoE vectors and any cohort-level financial-shenanigans or accrual screen. It
does not calculate a Beneish score. It records whether each field is observed,
partial, or missing under the same company-period, denominator, accounting,
and legal-entity rules.

The structured [comparability CSV](data/combined-investment-research-quality-of-earnings-retail-comparability-bridge-2026-09-16.csv)
is the field-level source of truth.

The structured rows mark the cohort-level composite as `not-promotable` until
the missing and partial joins below are resolved.

## What is comparable now

- All nine rows use annual primary filings and a property-only cash screen:
  operating cash flow less property additions. This supports directional
  same-period cash diagnostics across TJX, Target, and Walmart.
- Revenue, earnings, inventory, accounts payable, current assets, PP&E, D&A,
  SBC, diluted shares, and operating cash are directly observed for the
  selected annual rows, subject to the company-specific earnings basis.
- The earnings basis is explicit: TJX and Target use net income attributable
  to common owners; Walmart uses net income attributable to Walmart while
  retaining consolidated income and NCI in its source vector.
- Fiscal calendars are preserved rather than silently aligning January 31,
  February 1, and February 3 year ends as if they were identical periods.

## What is not yet promotable

- Target does not separately disclose trade receivables in the consolidated
  balance sheet; “other current assets” is not substituted.
- Walmart reports OSG&A, not a directly equivalent SG&A line to the TJX and
  Target fields. It remains a partial expense-taxonomy join.
- Claims are not a single interchangeable liability field: Target's current
  operating-lease perimeter is incomplete, Walmart's debt-plus-lease claims
  coexist with separately disclosed supplier-finance obligations, and TJX's
  lease presentation requires its own boundary.
- Transaction fields are not identical across the cohort. Walmart's
  acquisitions and strategic-investment disposals are visible, while the
  selected TJX and Target vectors do not yet carry the same complete
  transaction taxonomy.
- “Comparable diagnostic” means the row can support a bounded cash and burden
  comparison. It does not mean the row is eligible for a composite accrual
  score.

## Method-level promotion gate

| Method | Cohort-level evidence | Blocking comparability issue | Current treatment |
| --- | --- | --- | --- |
| Sloan-style cash/accrual review | Nine annual vectors plus the 18-row cash-conversion panel support OCF, earnings, working-capital, reinvestment, SBC, and claim diagnostics | Target receivables, fiscal-period alignment, and claim/perimeter differences prevent one persistence estimate for the cohort | Directional diagnostics only |
| Schilit-style financial-shenanigans review | Inventory/payables timing, supplier finance, temporary support, capex classification, attached services, gift-card timing, and dilution prompts are visible | Cost, collection, tax, and legal-entity allocation is not consistently joined by company and period | Source-review flags only |
| Beneish-style composite | Several component families are present in the annual vectors | Target receivables, Walmart OSG&A, total-asset/gross-margin requirements, transactions, and claim taxonomies are not fully comparable | Not calculated |

The cohort therefore supports a falsifier-oriented review order, not a single
manipulation score or cross-company ranking. A warning advances only when the
same entity, period, accounting taxonomy, and cash/claim perimeter are joined.

## Promotion rule

The cohort may use the nine rows for directional cash-conversion, capex,
working-capital, SBC, dilution, and claim diagnostics. It may not publish a
single cross-company Beneish-style or composite accrual result until the
receivable, expense, lease/claim, transaction, fiscal-calendar, and legal-
entity joins are all sourced and independently checked. An unusual ratio
remains a follow-up prompt, never a fraud conclusion by itself.

Status: `retail-cohort-comparability-partial`.

Primary annual sources are the TJX FY2025/FY2026 filings, Target FY2024/FY2025
filings, and Walmart FY2025/FY2026 filings linked in the structured rows.
