# Healthcare Frontier Collection Status

Date: 2026-08-10
Branch: `cli4-healthcare-frontier-batch`

## Batch objective

The current healthcare-frontier flagship set is:

- `Regeneron Pharmaceuticals, Inc.`
- `Labcorp Holdings Inc.`
- `Teva Pharmaceutical Industries Ltd.`
- `West Pharmaceutical Services, Inc.`
- `Option Care Health, Inc.`

This set is intended to cover:

- Biotechnology
- Diagnostic Substances
- Drug Manufacturers - Other
- Drug Delivery
- Drug Related Products
- Drugs - Generic
- Medical Laboratories & Research
- Specialized Health Services

## Collection window

For every company in this batch, the target evidence window is:

- `2025` annual report
- latest three reported quarters as of `2026-08-10`

For these calendar-year reporters, the expected quarter chain is:

- `Q2 2026`
- `Q1 2026`
- `Q4 2025`

## Current raw evidence status

### Regeneron Pharmaceuticals, Inc.

Lane role:

- biotechnology
- franchise concentration
- pipeline and label-expansion dependence

Raw evidence currently saved:

- AnnualReports company page HTML
- `2025` annual-report PDF
- SEC submissions JSON
- `2025` `10-K`
- `Q4 2025` `8-K`
- `Q1 2026` `10-Q`
- `Q1 2026` `8-K`
- `Q2 2026` `10-Q`
- `Q2 2026` `8-K`

Current raw status:

- materially source-complete for packet drafting

### Labcorp Holdings Inc.

Lane role:

- diagnostic substances
- medical laboratories and research infrastructure
- testing and biopharma-services operating leverage

Raw evidence currently saved:

- AnnualReports company page HTML
- `2025` annual-report PDF
- SEC submissions JSON
- `2025` `10-K`
- `Q4 2025` `8-K`
- `Q1 2026` `10-Q`
- `Q1 2026` `8-K`
- `Q2 2026` `10-Q`
- `Q2 2026` `8-K`

Current raw status:

- materially source-complete for packet drafting

### Teva Pharmaceutical Industries Ltd.

Lane role:

- drugs-generic
- drug-manufacturers-other
- branded-plus-generic portfolio transition

Raw evidence currently saved:

- AnnualReports company page HTML
- `2025` annual-report PDF
- SEC submissions JSON
- `2025` `10-K`
- `Q4 2025` `8-K`
- `Q1 2026` `10-Q`
- `Q1 2026` `8-K`
- `Q2 2026` `10-Q`
- `Q2 2026` `8-K`

Current raw status:

- materially source-complete for packet drafting

### West Pharmaceutical Services, Inc.

Lane role:

- drug delivery
- drug-related products
- sterile packaging and injectable-therapy physical infrastructure

Raw evidence currently saved:

- AnnualReports company page HTML
- SEC submissions JSON
- `2025` `10-K`
- `Q4 2025` `8-K`
- `Q1 2026` `10-Q`
- `Q1 2026` `8-K`
- `Q2 2026` `10-Q`
- `Q2 2026` `8-K`

Current raw status:

- SEC chain is complete for packet drafting
- official IR-hosted `2025` annual-report PDF still needs a successful local fetch

### Option Care Health, Inc.

Lane role:

- specialized health services
- recurring infusion and alternate-site care complexity
- home-based and ambulatory treatment infrastructure

Raw evidence currently saved:

- AnnualReports company page HTML
- `2025` annual-report PDF
- SEC submissions JSON
- `2025` `10-K`
- `Q4 2025` `8-K`
- `Q1 2026` `10-Q`
- `Q1 2026` `8-K`
- `Q2 2026` `10-Q`
- `Q2 2026` `8-K`

Current raw status:

- materially source-complete for packet drafting

## Interpretation targets for the packet-writing pass

The packet and memo pass should explicitly pull out:

- consumer and patient behavior around treatment adherence, convenience, trust, affordability, and site-of-care choice
- cultural and societal pressure from chronic disease burden, specialty treatment growth, aging, and home-based care normalization
- industrial pressure from reimbursement, pipeline concentration, patent exposure, sterile manufacturing complexity, diagnostic dependence, and labor intensity
- repeated higher-order patterns such as franchise and IP monetization, recurring care complexity, diagnostic-infrastructure dependence, and the physical delivery layer behind modern therapy economics

## Current drafting status

Completed file chains now exist for:

- `Regeneron Pharmaceuticals, Inc.`
- `Labcorp Holdings Inc.`
- `Teva Pharmaceutical Industries Ltd.`
- `Option Care Health, Inc.`

Completed with one remaining raw-artifact gap:

- `West Pharmaceutical Services, Inc.` has a completed packet, profile, source ledger, and IR link file, but the official IR-hosted `2025` annual-report PDF still has not been saved locally after repeated fetch attempts

Cross-company interpretation now exists in:

- `analysis/themes/healthcare-frontier-recurring-care-and-therapy-infrastructure-2026-08-10.md`

## Immediate next actions

1. Treat `Regeneron`, `Labcorp`, `Teva`, and `Option Care` as completed for the current healthcare batch.
2. Treat `West Pharmaceutical Services, Inc.` as partial unless the missing official `2025` annual-report PDF is fetched locally.
3. Decide whether to integrate shared indexes as one coherent healthcare batch or hand the batch back for separate integration.
4. Commit the branch snapshot and hand off with completed companies, partial companies, lane summary, and next recommended names.
