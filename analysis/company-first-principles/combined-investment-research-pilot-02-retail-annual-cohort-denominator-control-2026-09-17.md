# Pilot 02 annual retail cohort denominator control

Research date: `2026-09-17`

This control puts the latest available fiscal-year observations for TJX,
Target, and Walmart on one reported denominator: operating cash flow less
property spending, divided by weighted-average diluted shares. It adds
cash-paid lease and tax context, plus the annual supplier-finance movement
where the filing roll-forward is available.

The result is a comparable reported screen, not normalized common-owner cash.
Lease and tax cash are already reflected in operating cash flow; they are shown
as burden context and are not subtracted a second time. Supplier-finance
balances are also not treated as cash unless the filing supplies a settlement
join.

| Company | Fiscal period | OCF ($M) | Property ($M) | Cash after property ($M) | Diluted shares (M) | Cash after property/share | Lease cash ($M) | Tax cash ($M) | Supplier-finance movement ($M) | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TJX | FY2026 | 6,874 | 1,957 | 4,917 | 1,128.0 | $4.359 | 2,214 | 1,471 | not disclosed in the controlled annual roll-forward | reported-not-normalized |
| Target | FY2025 | 6,562 | 3,727 | 2,835 | 455.6 | $6.223 | 529 | 1,091 | -640 ending-minus-beginning obligation movement | reported-not-normalized |
| Walmart | FY2026 | 41,565 | 26,642 | 14,923 | 8,022.0 | $1.860 | 2,315 | 5,364 | +264 ending-minus-beginning obligation movement | reported-not-normalized |

## What the control establishes

1. All three companies have a fiscal-year-aligned reported cash-after-property
   screen and diluted-share denominator.
2. The per-share figures are mechanically reproducible: `$4.917B / 1,128M`,
   `$2.835B / 455.6M`, and `$14.923B / 8,022M`.
3. Lease cash, income-tax cash, and supplier-finance balances are visible as
   separate burden and timing fields rather than silently mixed into capex or
   operating cash.
4. Target's and Walmart's annual supplier-finance movements are not converted
   into owner cash. The confirmed-invoice roll-forwards do not provide a
   comparable H1 allocation or prove the operating-cash classification needed
   for promotion.

## What remains unresolved

The screen does not identify the maintenance share of capital spending, the
recurring cash cost and collection of attached services, inventory and
markdown normalization, seasonal timing, stock-compensation dilution, or a
common legal-entity owner waterfall. TJX's annual supplier-finance settlement
field is also not populated in the controlled roll-forward.

Accordingly, this artifact improves CA-06 comparability but does not promote
any row to normalized common-owner cash. The next promotion object remains a
same-period maintenance-capital, working-capital settlement, service-cost, or
claim-allocation schedule.

Sources: [annual retail cash per diluted share](combined-investment-research-pilot-02-retail-annual-per-share-cash.md), [annual lease and tax control](combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.md), and [supplier-finance roll-forward](combined-investment-research-pilot-02-retail-supplier-finance-roll-forward-2026-09-16.md).
