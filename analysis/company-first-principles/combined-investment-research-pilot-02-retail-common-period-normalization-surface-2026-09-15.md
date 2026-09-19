# Retail cohort common-period normalization surface — 2026-09-15

This artifact consolidates the current TJX, Target, and Walmart cash screens
into one review surface. It is a denominator control, not a ranking. The
companies report on different fiscal calendars and the inputs include
source-bounded sensitivities; the table therefore shows what is visible and
what still prevents promotion to normalized common-owner cash.

## Controlled common-period surface

| Company / period | Net sales | OCF | Property spending | Cash after property | Support candidate | Cash after support | OCF less 50% property | Inventory / payable signal | Supplier-finance signal | SBC sensitivity | Debt principal | Stacked residual | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TJX / H1 FY2027 | `$29.503B` | `$3.345B` | `$1.159B` | `$2.186B` | `$0.750B` | `$1.436B` | `$2.766B` | `+$0.603B / +$0.470B` | `not populated` | `$0.085B` | `$0.000B` | `$1.351B` | source-bounded residual |
| Target / H1 2026 | `$51.982B` | `$4.519B` | `$2.404B` | `$2.115B` | `$1.364B` | `$0.751B` | `$3.317B` | `not fully populated / +$0.612B` | `$3.200B` | `$0.154B` | `$1.070B` | `($0.473B)` | source-bounded residual |
| Walmart / H1 FY2027 | `$361.784B` | `$19.710B` | `$14.181B` | `$5.529B` | `$4.548B` | `$0.981B` | `$12.619B` | `+$2.660B / +$1.648B` | `$6.400B` | `not separately populated` | `$2.303B` | `($1.322B)` | source-bounded residual |

Definitions:

- `Cash after property` is reported operating cash flow less disclosed
  property spending. It is not normalized owner cash.
- `Support candidate` is a source-bounded temporary tariff, vendor, payable,
  or interchange benefit candidate. It is not a claim that every dollar is
  nonrecurring.
- `OCF less 50% property` is a maintenance/growth allocation sensitivity. It
  does not assert that 50% is the correct split.
- `Stacked residual` is cash after property less the support candidate, SBC
  sensitivity where available, and disclosed debt-principal repayment. It is
  a stress screen and must not be described as reported negative owner cash.

## TJX sensitivity reconciliation

The TJX row contains two intentionally different low-screen constructions in
the surrounding artifacts:

| Screen | Arithmetic | Result | Interpretation |
| --- | --- | ---: | --- |
| Cash-quality low | `$2.186B - $470M` payable-support signal `- $85M` SBC | `$1.631B` | Normalized-cash screen that leaves tariff and interchange treatment unresolved |
| Temporary-support stress | `$2.186B - $750M` tariff/interchange candidate `- $85M` SBC | `$1.351B` | Stress sensitivity that treats the identified `$331M` refund and `$419M` settlement as non-recurring candidates |

The `$470M` payable signal and the `$750M` temporary-support candidate are not
additive deductions. They arise from different measurement layers and may
overlap in timing or economic effect. The cohort surface therefore preserves
both as labeled sensitivities and does not select either as normalized owner
cash.

## What this surface proves

1. The same burden categories can be placed beside each company’s reported
   cash denominator.
2. Support removal and debt/dilution claims can materially change the apparent
   residual: the current stacked screen is `$1.351B` for TJX, `($0.473B)` for
   Target, and `($1.322B)` for Walmart.
3. A 50% property-spending allocation creates a distinct sensitivity from the
   reported cash-after-property line, but it does not resolve maintenance
   versus growth capital.
4. The working-capital and supplier-finance signals are not interchangeable:
   a payable increase, supplier-finance balance, and inventory change can have
   different timing and economic meanings.
5. Attached-service revenue remains outside the positive owner-cash bridge
   until direct costs, collection, working capital, capital, tax, and entity
   allocation are visible.

## What this surface does not prove

- normalized annual owner cash;
- maintenance-capital amounts by store, distribution, or technology;
- lease, tax, shrink, markdown, or service-level cash allocation;
- whether each support candidate is temporary, recurring, or reversed later;
- comparable traffic, transaction, ticket, and inventory-turn economics; or
- a relative investment ranking across the three companies.

The promotion decision remains `hold at reported/illustrative screen` for all
three retailers. The next decisive upgrade is a period-matched roll-forward
that allocates maintenance capital, working capital, leases, taxes, attached
services, and dilution to each legal entity and fiscal period.

Structured rows: [normalization surface CSV](data/combined-investment-research-pilot-02-retail-common-period-normalization-surface-2026-09-15.csv).
Source components: [common-period cash matrix](data/combined-investment-research-pilot-02-retail-common-period-cash-matrix.csv), [margin and working-capital normalization](data/combined-investment-research-pilot-02-retail-margin-working-capital-normalization.csv), [capex sensitivity](data/combined-investment-research-pilot-02-retail-capex-allocation-sensitivity.csv), and [post-financing residual screen](combined-investment-research-pilot-02-retail-post-financing-residual-screen-2026-09-15.md).
