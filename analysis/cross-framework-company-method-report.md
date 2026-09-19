# Cross-Framework Company Method Report

Updated on: 2026-09-15

## Summary

- Source roster rows: 243
- Unique company pages: 238
- Company data files: 238
- Deep exemplar pages: 2
- Detailed first-principles pages: 2
- Packet-backed pages: 236
- Roster-workbench pages: 0
- Damodaran use cases: 12
- Lyn Alden methods: 6
- Other framework methods: 6

## Method Sources

- Damodaran method library: `/home/mehtama1/git-repo/aswath-damodaran-courses-concepts-research/analysis/damodaran-method-library.json`
- Lyn Alden source: https://www.lynalden.com/april-2024-newsletter/
- Lyn Alden source: https://www.lynalden.com/august-2022-newsletter/
- Lyn Alden source: https://www.lynalden.com/fiscal-and-monetary-policy/
- Lyn Alden source: https://www.lynalden.com/june-2026-newsletter/
- Lyn Alden source: https://www.lynalden.com/newsletter-archives/
- Lyn Alden source: https://www.lynalden.com/reshoring/

## Status Tiers

### `detailed-first-principles`

- `mcdonalds-corporation`: McDonald's Corporation (MCD)
- `chipotle-mexican-grill`: Chipotle Mexican Grill, Inc. (CMG)

### `packet-backed`

- `baxter-international-inc`: Baxter International Inc. (BAX)
- `us-foods-holding-corp`: US Foods Holding Corp. (USFD)
- `herc-holdings-inc`: Herc Holdings Inc. (HRI)
- `pool-corp`: Pool Corp. (POOL)
- `global-industrial-company`: Global Industrial Company (GIC)
- `henry-schein-inc`: Henry Schein, Inc. (HSIC)
- `intuitive-surgical-inc`: Intuitive Surgical, Inc. (ISRG)
- `accendra-health-inc`: Accendra Health, Inc. (ACH)
- `astrana-health-inc`: Astrana Health, Inc. (ASTH)
- `adt-inc`: ADT Inc. (ADT)
- `the-geo-group`: The GEO Group, Inc. (GEO)
- `motorola-solutions-inc`: Motorola Solutions, Inc. (MSI)
- `alcoa-corporation`: Alcoa Corporation (AA)
- `dow-inc`: Dow Inc. (DOW)
- `reliance-steel-aluminum-co`: Reliance, Inc. (RS)
- `west-fraser-timber-co-ltd`: West Fraser Timber Co. Ltd. (WFG)
- `clearwater-paper-corp`: Clearwater Paper Corp (CLW)
- `cf-industries-holdings-inc`: CF Industries Holdings, Inc. (CF)
- `the-sherwin-williams-company`: The Sherwin-Williams Company (SHW)
- `builders-firstsource-inc`: Builders FirstSource, Inc. (BLDR)
- ...and 216 more

### `roster-workbench`

- none

## Sector Coverage

- Basic Materials: 13 companies
- Consumer Goods: 43 companies
- Financial: 17 companies
- Healthcare: 21 companies
- Industrial Goods: 47 companies
- Real Estate: 6 companies
- Retail: 3 companies
- Services: 45 companies
- Technology: 29 companies
- Utilities: 14 companies

## Deep Exemplar Standard

The first finished pair is McDonald's and Chipotle. These pages set the repeatable UX and analysis template for the rest of the roster:

- clear company conclusion and investor conclusion
- framework-specific method routing
- annual and quarterly evidence table
- business-model mechanism table
- explicit thesis breakers
- next filing watchlist
- peer comparison bridge

## Release Gate

Run:

```bash
python3 scripts/build-cross-framework-company-pages.py
python3 scripts/verify-cross-framework-company-pages.py
```

The verifier checks registry/page/data parity, framework route coverage,
status-tier validity, and packet-derived annual/quarter/signal content
where local company packets exist.
