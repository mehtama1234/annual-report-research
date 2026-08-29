# Capital Flow OBDC Schedule Parser Pass

## What This Adds

The OBDC pass turns Blue Owl Capital Corporation's Q2 2026 10-Q schedule into exact industry-dollar evidence.

Local outputs:

- `analysis/company-first-principles/data/capital-flow-obdc-official-industry-subtotals.csv`
- `analysis/company-first-principles/data/capital-flow-obdc-industry-summary.csv`
- `scripts/extract-obdc-schedule.py`

## Reconciliation

| Check | Result |
|---|---:|
| Official subtotal and adjustment rows | `68` |
| Industry summary rows | `30` |
| Total fair value from extracted schedule rows | `14.955049B USD` |
| OBDC reported total investments at fair value | `14.955049B USD` |
| Reconciliation difference | `0.000000B USD` |
| Miscellaneous commitment adjustments | `-8.744M USD` |

The industry summary excludes the miscellaneous debt commitment adjustments from lane ranking, but the subtotal file keeps those adjustment rows so the schedule ties exactly to reported total investment fair value.

## Top OBDC Lanes

| OBDC Reported Industry | Fair Value |
|---|---:|
| Internet software and services | `1.733B USD` |
| Healthcare providers and services | `1.274B USD` |
| Asset based lending and fund finance | `1.111B USD` |
| Insurance | `0.911B USD` |
| Healthcare technology | `0.872B USD` |
| Food and beverage | `0.783B USD` |
| Healthcare equipment and services | `0.720B USD` |
| Buildings and real estate | `0.663B USD` |
| Manufacturing | `0.565B USD` |
| Financial services | `0.560B USD` |

## Claim Upgrade

Before this pass, OBDC only gave breadth evidence: `229` companies across `30` industries.

After this pass, OBDC gives exact schedule-derived lane dollars. That lets us say:

`Blue Owl's BDC loan book independently confirms the same broad private-credit destination pattern seen at ARCC and BXSL: software, healthcare, financial/fund-finance, insurance, commercial services, consumer services, and industrial/support categories.`

## What It Does Not Prove

This still does not prove bank displacement by itself.

It proves destination: where Blue Owl BDC capital sits at quarter end.

The displacement question still needs borrower-level matching:

- sponsor
- transaction purpose
- prior debt source
- current lender group
- bank revolver or administrative-agent role

## Simple Version

OBDC confirms the capital-flow map with exact numbers.

Blue Owl's BDC money is heavily in software, healthcare, fund finance/financial services, insurance, food and beverage, real estate, manufacturing, business services, and materials-related lanes.
