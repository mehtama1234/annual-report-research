# Capital Flow ARCC Schedule Parser Pass

## What This Adds

The earlier ARCC evidence used borrower examples and visible schedule tags.

This pass goes deeper by parsing the ARCC Q2 2026 10-Q investment schedule into row-level investment records and industry totals.

The important update: ARCC's official industry subtotal rows were also extracted separately and reconcile to reported total investments fair value.

## Local Data Files

- Row-level parser output: `analysis/company-first-principles/data/capital-flow-arcc-schedule-parser-rows.csv`
- Industry summary: `analysis/company-first-principles/data/capital-flow-arcc-schedule-industry-summary.csv`
- Official industry subtotals: `analysis/company-first-principles/data/capital-flow-arcc-official-industry-subtotals.csv`
- Source filing: `raw/primary-sources/capital-flow/ares-capital/q2-2026/arcc-2026-q2-10q.html`

## Reconciliation Status

There are two evidence levels now.

The row-level parser is useful, but not final. It captures borrower and instrument detail, but it does not fully reconcile.

| Check | Value |
|---|---:|
| Row-level parsed investment rows | `1,379` |
| Row-level parsed fair value | `22.456B USD` |
| Reported non-controlled/non-affiliate fair value | `24.282B USD` |
| Row-level coverage of reported non-controlled/non-affiliate fair value | `92.5%` |

The official industry-subtotal extraction does reconcile.

| Check | Value |
|---|---:|
| Official industry subtotal rows | `24` |
| Official industry subtotal fair value | `29.349B USD` |
| Reported total investments fair value | `29.349B USD` |
| Reconciliation difference | `0.0B USD` |
| Percent of net assets total | `211.32%` |

The right status is:

`official-subtotal-reconciles-to-total-fair-value`

That status applies to the official industry subtotal table. The row-level parser remains `parser-derived-needs-reconciliation` and should be used for borrower discovery, not final totals.

## Official ARCC Industry Lanes

| Industry | Official Fair Value | % Of Net Assets | Share Of Total Fair Value |
|---|---:|---:|---:|
| Software and Services | `6.451B USD` | `46.45%` | `21.98%` |
| Financial Services | `3.936B USD` | `28.34%` | `13.41%` |
| Health Care Equipment and Services | `2.895B USD` | `20.84%` | `9.86%` |
| Commercial and Professional Services | `2.812B USD` | `20.25%` | `9.58%` |
| Consumer Services | `1.972B USD` | `14.20%` | `6.72%` |
| Insurance | `1.571B USD` | `11.31%` | `5.35%` |
| Capital Goods | `1.438B USD` | `10.35%` | `4.90%` |
| Consumer Distribution and Retail | `1.378B USD` | `9.92%` | `4.69%` |
| Investment Funds and Vehicles | `1.181B USD` | `8.50%` | `4.02%` |
| Sports, Media and Entertainment | `1.121B USD` | `8.07%` | `3.82%` |

## What This Changes

Before this pass, ARCC supported the claim mostly through scale and examples:

`ARCC has hundreds of investments, billions of funded loans, mostly senior secured/floating-rate exposure, and named borrowers in software and services lanes.`

After this pass, the claim gets more quantitative and better reconciled:

`ARCC's official Q2 2026 industry subtotals show the largest borrower lanes are software/services, financial services, healthcare equipment/services, commercial/professional services, consumer services, insurance, capital goods, consumer distribution/retail, investment funds/vehicles, and sports/media/entertainment.`

That lines up with the BXSL and OBDC evidence. The same lane pattern keeps appearing:

- software and IT systems
- healthcare services and technology
- commercial/professional services
- consumer and home services
- insurance and financial services
- capital goods and industrial support

## What This Still Does Not Prove

This pass still does not prove bank displacement.

It improves the map of where private-credit dollars are going. It does not yet identify:

- prior lender
- prior debt instrument
- transaction purpose
- sponsor owner
- whether banks were displaced or remained as revolving-credit providers

## Better Claim After This Pass

Old claim:

`Ares private credit is funding real borrowers.`

Better claim:

`ARCC's official Q2 2026 industry subtotal rows show Ares-managed BDC exposure concentrated in software/services, financial services, healthcare equipment/services, commercial/professional services, consumer services, insurance, capital goods, retail/distribution, investment funds/vehicles, and sports/media/entertainment. The industry subtotals reconcile to reported total investment fair value, while the separate row-level parser remains a borrower-discovery tool that still needs reconciliation.`

## Next Parser Fixes

The row-level parser still needs three improvements before promotion:

- reconcile the missing `1.826B USD` against the reported non-controlled/non-affiliate fair value
- separate subtotal rows from investment rows more cleanly
- tie each borrower row back to the reconciled official industry subtotal

## Simple Version

The ARCC industry totals are now reconciled.

The official subtotal read says Ares private-credit exposure is largest in software/services, financial services, healthcare, commercial/professional services, consumer services, insurance, capital goods, and retail/distribution.

Use the official subtotal table for industry totals. Use the row-level parser for finding borrower names to investigate next.
