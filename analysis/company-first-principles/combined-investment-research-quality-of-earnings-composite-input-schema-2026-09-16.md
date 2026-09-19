# Quality-of-earnings composite input schema

Research date: 2026-09-16

## Purpose

This schema defines the minimum comparable inputs required before the
cross-pilot QoE overlay can calculate a Beneish-style or other composite
accrual screen. It is an input-control artifact, not a score and not an
allegation of accounting manipulation.

The structured [composite input CSV](data/combined-investment-research-quality-of-earnings-composite-input-schema-2026-09-16.csv)
is the field-level source of truth. observed means the value exists for the
selected company-period; partial means it exists only for a subset or as a
non-comparable proxy; and missing means the current longitudinal panel cannot
support the field without a new extraction.

## Required comparable families

The proposed screen needs period-matched revenue, net income, receivables,
inventory, current assets, property and equipment, depreciation, SG&A, debt,
operating cash flow, stock compensation, acquisitions, and diluted shares.
Each row also needs an accounting-policy and source-period check. A ratio is
not promotable when the company changes fiscal alignment, classification, or
discloses only a consolidated proxy for a legal-entity question.

The current 18-row retail bridge supplies operating cash flow, property
spending, and cash-after-property. The nine-row annual TJX/Target/Walmart
vectors also supply much of the income-statement and balance-sheet vector,
including net income, inventory, payables, current assets, PP&E, D&A, claims,
SBC, and diluted shares. The annual cohort still has material comparability
boundaries: Target does not separately disclose trade receivables, Walmart's
OSG&A is not identical to TJX/Target SG&A, claims and lease perimeters differ,
and the full 18-row longitudinal vector is not assembled. Therefore the
composite screen remains not-assembled; the [retail cash-conversion screen](combined-investment-research-quality-of-earnings-retail-cash-conversion-screen-2026-09-16.md)
and the [retail comparability bridge](combined-investment-research-quality-of-earnings-retail-comparability-bridge-2026-09-16.md)
are the highest-confidence interim components.

## Promotion rule

Do not calculate or publish a composite score until every required field is
period-aligned, sourced, and classified as reported or transparently derived.
When the field set is incomplete, publish the missing-field map and component
diagnostics only. Even a complete score would be a screening signal requiring
filing review, not proof of fraud or misstatement.
