# Apollo/Athene Schedule D interest subtotal control pass 1

Research date: `2026-09-18`

## Result

The corrected Schedule D row parser now ties the filing's own subtotal rows for
both interest fields. This is stronger than an aggregate sum derived only from
the parser output.

| Schedule D scope | Interest income due/accrued | Interest received during year | Source control |
|---|---:|---:|---|
| Issuer-credit obligations | `$888.305222M` | `$3.006747015B` | Page 5911 subtotal |
| Asset-backed securities | `$616.145225M` | `$3.223731106B` | Page 6027 subtotal |
| Combined | `$1.504450447B` | `$6.230478121B` | Sum of filing subtotals |

The parser-to-source differences are zero for all four fields and for the
combined totals. The structured control is in the [subtotal-control CSV](data/capital-flow-apollo-athene-statutory-schedule-d-interest-subtotal-control-pass-1.csv).

## Consequence for the page-18 residual

This closes one possible explanation for the prior difference: the corrected
Schedule D population is not shown to be missing a large issuer-credit or ABS
subtotal population. The remaining comparison is still not a same-definition
reconciliation. Page 18 is the Exhibit of Net Investment Income, with gross
category collected and earned columns and footnote adjustments; Schedule D is
a holding-level table with separate due/accrued and received-interest fields.

Accordingly:

- `$6.230478121B` is a filing-controlled Schedule D received-interest total.
- `$8.127852536B` is a filing-controlled page-18 collected bond-category total.
- The `$1.897374415B` difference remains a page-18/Schedule D definition and
  perimeter diagnostic.
- No amount is promoted to a borrower receipt, remittance, liability-adjusted
  return, or Apollo common-owner cash.

## Decision

`schedule-d-interest-fields-subtotal-tied; page18-definition-join-open`

The next promotion-quality object remains a same-definition statutory workpaper
or accounting reconciliation that maps the page-18 bond categories and
footnote adjustments to the Schedule D fields. The current control is strong
enough to stop treating the residual as a parser-coverage problem.
