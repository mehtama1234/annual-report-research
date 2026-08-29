# Capital Flow URI Yak Holder Schedule Extractor Pass 1

## Purpose

This pass starts the repeatable extraction path for URI's Yak senior-note holder schedules.

It answers:

`Can we turn the manual URI Yak holder search into a local extractor that recovers source rows by instrument description or identifier?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-holder-schedule-extractor-pass-1.csv`

The grouped dedupe-scope table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-holder-schedule-dedupe-summary-pass-1.csv`

The extractor is:

`scripts/extract-uri-yak-holder-schedules.py`

## Source Boundary

This pass uses local SEC holder-schedule files under:

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec`

The current run includes SEC EDGAR / N-PORT local sources for American Beacon, Capital Group, Federated Hermes, Fidelity, Jackson, Loomis Sayles, Venerable, and Western Asset:

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/calamos-nport-cgw8-2026-03.html`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/federated-hermes-institutional-high-yield-2025-nport.html`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/fidelity-qtly-6540-2025-05.html`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/fidelity-qtly-6541-2025-11.html`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/nport-1982467-primary-doc.xml`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/nport-863520-primary-doc.xml`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/nport-917469-2025-06.html`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/venerable-high-yield-2024q4-nport.txt`

`raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/venerable-high-yield-2025q1-nport.txt`

The raw fetch initially returned an SEC automated-tool block page. Re-fetching with a declared user agent and decompression produced the actual filing. That matters because the extractor must prove source integrity before promoting rows.

## Extractor Result

The extractor recovered `9` candidate holder rows from local SEC holder-schedule files and now attaches source and dedupe metadata.

| Source | Metadata | Row Type | Matched Row | Extracted Amount |
|---|---|---|---|---:|
| Capital Group U.S. Multi-Sector Income ETF SEC EDGAR portfolio | CIK `1870117`; accession `000141036826054719`; period March `31`, `2026`; manager family `Capital Group` | `html-table-row-fragment` | United Rentals (North America), Inc. `6.125%`, `3/15/2034` | `2.510000M` face; `2.545000M USD` value |
| Federated Hermes Institutional High Yield Bond Fund SEC EDGAR portfolio | CIK `925723`; accession `000114554925019417`; period January `31`, `2025`; manager family `Federated Hermes` | `html-table-row-fragment` | United Rentals North America, Inc., Sr. Unsecd. Note, 144A, `6.125%`, `3/15/2034` | `5.650000M` face; `5.666272M USD` value |
| Fidelity SAI Sustainable Core Plus Bond Fund SEC EDGAR portfolio | CIK `35315`; accession `000175272425176732`; period May `31`, `2025`; manager family `Fidelity` | `html-table-row-fragment` | United Rentals North America Inc `6.125%`, `3/15/2034` | `0.010000M` face; `0.010136M USD` value |
| Fidelity Sustainable Core Plus Bond Fund SEC EDGAR portfolio | CIK `35315`; accession `000003540226000486`; period November `30`, `2025`; manager family `Fidelity` | `html-table-row-fragment` | United Rentals North America Inc `6.125%`, `3/15/2034` | `0.007000M` face; `0.007311M USD` value |
| Jackson Credit Opportunities Fund SEC rendered N-PORT source | CIK `1982467`; accession `000119312526244833`; period March `31`, `2026`; manager family `Jackson` | `rendered-nport-investment-window` | CUSIP `911365BR4`; ISIN `US911365BR47`; United Rentals North America | `0.395000M` face; `0.399637M USD` value |
| Western Asset Total Return Unconstrained Fund SEC rendered N-PORT source | CIK `863520`; accession `000094040025005171`; period August `29`, `2025`; manager family `Western Asset` | `rendered-nport-investment-window` | CUSIP `911365BR4`; ISIN `US911365BR47`; United Rentals North America | `0.210000M` face; `0.217776M USD` value |
| Loomis Sayles Institutional High Income Fund SEC EDGAR portfolio | CIK `917469`; accession `000175272425211983`; period June `30`, `2025`; manager family `Loomis Sayles` | `html-table-row-fragment` | United Rentals North America, Inc., `6.125%`, `3/15/2034` | `0.045000M` face; `0.046351M USD` value |
| American Beacon NIS Core Plus Bond Fund raw N-PORT filing | CIK `809593`; accession `000175272424293276`; period October `31`, `2024`; manager family `American Beacon` | `nport-xml-investment-block` | CUSIP `911365BR4`; ISIN `US911365BR47`; United Rentals North America | `0.015000M` face; `0.015101M USD` value |
| Venerable High Yield Fund raw N-PORT filing | CIK `1995745`; accession `000175272425116428`; period March `31`, `2025`; manager family `Venerable` | `nport-xml-investment-block` | CUSIP `911365BR4`; ISIN `US911365BR47`; United Rentals North America | `6.100000M` face; `6.111401M USD` value |

The extracted rows total `14.942000M USD` face and `15.018985M USD` value. They are later holder traces and do not replace the broader manual expanded holder crosswalk.

The current dedupe scopes are fund/vehicle-period scopes, for example:

`Federated Hermes|Federated Hermes Institutional High Yield Bond Fund|January 31 2025`

## Dedupe-Scope Summary

The grouped output has `9` rows:

| Dedupe Scope | Candidate Rows | Unique Dedupe Keys | Grouped Face | Grouped Value | Boundary |
|---|---:|---:|---:|---:|---|
| `American Beacon|American Beacon NIS Core Plus Bond Fund|October 31 2024` | `1` | `1` | `0.015000M` | `0.015101M USD` | Fund-period grouping only; not broad manager-family dedupe. |
| `Capital Group|Capital Group U.S. Multi-Sector Income ETF|March 31 2026` | `1` | `1` | `2.510000M` | `2.545000M USD` | Fund-period grouping only; source table reports amounts in thousands. |
| `Federated Hermes|Federated Hermes Institutional High Yield Bond Fund|January 31 2025` | `1` | `1` | `5.650000M` | `5.666272M USD` | Fund-period grouping only; not broad manager-family dedupe. |
| `Fidelity|Fidelity SAI Sustainable Core Plus Bond Fund|May 31 2025` | `1` | `1` | `0.010000M` | `0.010136M USD` | Fund-period grouping only; not broad manager-family dedupe. |
| `Fidelity|Fidelity Sustainable Core Plus Bond Fund|November 30 2025` | `1` | `1` | `0.007000M` | `0.007311M USD` | Fund-period grouping only; not broad manager-family dedupe. |
| `Jackson|Jackson Credit Opportunities Fund|March 31 2026` | `1` | `1` | `0.395000M` | `0.399637M USD` | Fund-period grouping only; not broad manager-family dedupe. |
| `Loomis Sayles|Loomis Sayles Institutional High Income Fund|June 30 2025` | `1` | `1` | `0.045000M` | `0.046351M USD` | Fund-period grouping only; not broad manager-family dedupe. |
| `Venerable|Venerable High Yield Fund|March 31 2025` | `1` | `1` | `6.100000M` | `6.111401M USD` | Fund-period grouping only; not broad manager-family dedupe. |
| `Western Asset|Western Asset Total Return Unconstrained Fund|August 29 2025` | `1` | `1` | `0.210000M` | `0.217776M USD` | Fund-period grouping only; not broad manager-family dedupe. |

This is the first split between:

- raw candidate rows
- dedupe-scope grouped rows
- future manager-family or unique-holder totals

## What This Adds

This does not add a new holder total. It adds process proof:

`local source file -> extractor -> candidate holder row -> source metadata -> dedupe key -> grouped dedupe-scope output`

That is the next step toward scaling the holder work. We can now add more local HTML, rendered N-PORT, and raw N-PORT XML schedules and rerun the extractor rather than relying only on manual browser searches. The new columns also force future totals to state whether they are row sums, manager-family sums, fund-level sums, or true unique-holder estimates.

## Safe Claim

`URI's Yak note holder-discovery path is now holder-schedule-dedupe-summary-expanded: a local extractor recovered 9 United Rentals North America 6.125% note due March 15 2034 candidate rows from local HTML, rendered N-PORT, and raw N-PORT XML schedules, extracting 14.942000M USD face and 15.018985M USD value while attaching source URL, period, CIK, accession, manager-family, fund/vehicle, dedupe-scope, and dedupe-key fields. It also emits 9 grouped dedupe-scope summary rows. This is process evidence for repeatable holder discovery and future dedupe, not a full holder base, not original issuance allocation, and not deduped manager-family exposure.`

## Claims Not To Make Yet

Do not say:

- the extractor has searched all N-PORT filings
- the extractor has produced a full holder base
- candidate rows are all unique holders
- dedupe-scope summary rows equal manager-family unique exposure
- the extracted SEC row proves initial-purchaser status
- the process identifies original deal pricing, yield, spread, or order-book allocation

## Next Concrete Work

1. Add a manager-family grouping output after enough repeated manager/fund-period rows exist to make cross-period dedupe meaningful.
2. Add more locally fetched SEC N-PORT and fund holdings schedules to the source set.
3. Split source-specific amount-scaling rules into testable metadata fixtures if additional `(000)` schedule formats appear.
4. Extend the extractor to PDF/table sources only after HTML, rendered N-PORT, and raw XML extraction remain stable.
