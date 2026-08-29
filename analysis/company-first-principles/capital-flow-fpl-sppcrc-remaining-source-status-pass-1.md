# Capital Flow FPL SPPCRC Remaining Source Status Pass 1

## Purpose

This page records the current status of the remaining FPL proof gaps after the category, factor/WACC, final true-up, final factor-order, project-detail, FPL-wide earnings/cash, category-attribution, Distribution Inspection attribution, Distribution Inspection component-extraction, and receipts/financing boundary passes.

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-remaining-source-status-pass-1.csv`

## Short Answer

FPL now has a stronger regulated recovery bridge. The two source classes that were previously blocking the next step have been acquired and extracted:

- Order `PSC-2025-0439-FOF-EI` for the 2026 SPPCRC factor/tariff authorization
- Pankratz testimony with Exhibits AP-1/AP-2 for 2025 project-detail and variance evidence

The remaining blocker is narrower: the Distribution Inspection attribution, component-extraction, and receipts/financing boundary passes now show the proof chain is strong through physical output, capital use, plant additions, recoverable expense, final category recovery, factor-order authority, carrying-charge context, FPL-wide cash context, final equity/debt/depreciation component attribution, aggregate SPPCRC clause revenue, and Form 8A recovery capital-structure support. It still lacks Distribution Inspection category receipts, source-of-funds allocation, and, if needed, AP-1 row-level project IDs.

## Current Source Status

| Need | Status | Current Evidence | Next Action |
|---|---|---|---|
| 2026 SPPCRC factor approval order | extracted | Official PSC PDF for Order `PSC-2025-0439-FOF-EI` has been fetched as Document `15236-2025` and extracted into rows `CFPLFO-001` through `CFPLFO-014`. | Use the extracted order rows as the order-level approval bridge; search only if separate stamped tariff sheets or amended post-rate-case factors are needed. |
| final tariff sheets / factor sheets | order-level-approval-extracted | Order `PSC-2025-0439-FOF-EI` approves revised tariffs reflecting SPPCRC factors and authorizes application during January 2026 through December 2026. | Search PSC tariff attachments only to obtain separately stamped tariff sheets or amended factors after final rate-case disposition. |
| Exhibit AP-1 project-level detail | extracted-summary-visible | Pankratz testimony with Exhibit AP-1 has been fetched as Document `01941-2026` and extracted into physical-output rows `CFPLPD-001` through `CFPLPD-016`. | If project-level asset IDs are needed, parse AP-1 feeder/project rows beyond the summary pages. |
| Exhibit AP-2 variance explanations | extracted-summary-visible | Pankratz testimony and AP-2 variance-driver pages have been fetched and extracted into `CFPLPD-017` and related source-control rows. | Parse AP-1 row-level variance fields only if a category/project variance distribution is needed. |
| earnings/cash conversion | receipts-financing-boundary-partial | Final true-up, order-level factor approval, AP-1/AP-2 physical output, FPL-wide earnings/cash context, a `13` row Distribution Inspection attribution table, a `15` row final Form 7A component extraction, and a `12` row receipts/financing boundary pass are visible. The latest pass confirms aggregate clause revenue, true-up collection/refund mechanics, and Form 8A capital-structure support; category customer-receipt and source-of-funds-allocation gates remain missing. | Find SPPCRC category receipts by rate class, financing-source allocation, later true-up/order workpapers, workpaper notes explaining Form 7E to Form 7A changes, or AP-1 row-level project IDs. |

## Why This Matters

The evidence chain has improved in stages:

1. Category recovery rows: FPL SPPCRC programs have capital-use and recoverable-expense evidence.
2. Factor/WACC rows: the filing exposes customer-factor math and carrying-charge inputs.
3. Final true-up rows: the 2025 period has final true-up evidence, final clause revenue, and final jurisdictional revenue requirements.
4. Final factor-order rows: Order `PSC-2025-0439-FOF-EI` approves the 2026 factor/tariff bridge.
5. Project-detail rows: AP-1/AP-2 adds physical-output summaries and variance controls.
6. FPL-wide earnings/cash rows: Q2 2026 source files expose utility-wide revenue, net income, operating cash flow, capex, receivables, regulatory assets, debt, AFUDC, and regulatory ROE.
7. Category-attribution rows: Distribution Inspection and Transmission Inspection connect output, actual costs, final recovery, factor-order support, WACC context, and FPL-wide cash context.
8. Distribution Inspection attribution rows: the strongest category is tested against output, cost, plant, recovery, factor, cash-context, customer-receipt, category-earnings, and financing-source gates.
9. Distribution Inspection component rows: final Form 7A decomposes the category into equity, debt, and depreciation components.
10. Receipts/financing boundary rows: aggregate clause revenue, true-up collection/refund mechanics, and final Form 8A capital-structure support are visible.
11. Remaining source gap: Distribution Inspection category receipts, source-of-funds allocation, workpaper interpretation, and full project-level row reconciliation remain open.

The current answer is therefore:

`FPL is final-factor-order, physical-output, FPL-wide cash/earnings context, Distribution Inspection component-attribution visible, and recovery capital-structure supported. It is the strongest regulated recovery case in the power/grid pilot, but it is not yet full project-return-grade because Distribution Inspection category receipts, source-of-funds allocation, and full project-level return remain unreconciled.`

## Do Not Claim

- actual customer receipts have been extracted
- SPPCRC category component attribution proves realized cash return
- separately stamped tariff sheets have been extracted
- AP-1 individual feeder/project rows have been fully normalized
- clause revenue equals earnings
- revenue requirement equals IRR
- FPL's storm-protection recovery proves all FPL capital recovery

## Decision

`fpl-remaining-source-status-open - final factor/tariff order, AP exhibit summaries, FPL-wide earnings/cash context, Distribution Inspection attribution, Distribution Inspection component extraction, and receipts/financing boundary extraction are complete; category receipts, source-of-funds allocation, workpaper interpretation, and AP-1 row-level detail are the next required evidence.`
