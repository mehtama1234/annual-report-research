# Capital Flow Power/Grid Pilot Source Acquisition Results Pass 1

## Purpose

This page records the first successful acquisition run for the five-company power/grid pilot.

The question is:

`Did the official Q2 2026 source routes for ONEOK, MasTec, Plains, Targa, and NextEra produce local files that can feed priority-1 extraction?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-power-grid-pilot-source-acquisition-results-pass-1.csv`

## Short Answer

Yes. The acquisition run fetched `10` official source artifacts:

| Company | Files Fetched | Types | Current Status |
|---|---:|---|---|
| ONEOK | `2` | HTML pages | fetched, not yet parsed |
| MasTec | `2` | PDF and HTML page | fetched, not yet parsed |
| Plains | `2` | PDFs | fetched, not yet parsed |
| Targa | `1` | PDF | fetched, not yet parsed |
| NextEra | `3` | PDFs | fetched, not yet parsed |

Every fetched file has nonzero bytes and a valid HTML or PDF header. The acquisition bottleneck is cleared for these ten rows.

The priority-1 metric extraction pass is now:

`/cluster/capital-flow-power-grid-pilot-priority1-metric-extraction-pass-1.md`

It parses the acquired source package into `30` metric rows and records which promotion tests pass or fail.

The second-pass gap closure is:

`/cluster/capital-flow-power-grid-pilot-gap-closure-and-metric-pass-2.md`

It adds four newly resolved source artifacts and `12` additional ONEOK/MasTec metric rows.

## Local Source Files

| Company | Local Files |
|---|---|
| ONEOK | `raw/primary-sources/capital-flow/power-grid-pilot/oneok/q2-2026/oneok-2026-financial-reports-page.html`; `raw/primary-sources/capital-flow/power-grid-pilot/oneok/q2-2026/oneok-2026-q2-earnings-release-page.html` |
| MasTec | `raw/primary-sources/capital-flow/power-grid-pilot/mastec/q2-2026/mastec-2026-q2-earnings-presentation.pdf`; `raw/primary-sources/capital-flow/power-grid-pilot/mastec/q2-2026/mastec-2026-q2-10q-filing-page.html` |
| Plains | `raw/primary-sources/capital-flow/power-grid-pilot/plains/q2-2026/plains-2026-q2-earnings-presentation.pdf`; `raw/primary-sources/capital-flow/power-grid-pilot/plains/q2-2026/plains-2026-q2-earnings-release.pdf` |
| Targa | `raw/primary-sources/capital-flow/power-grid-pilot/targa/q2-2026/targa-2026-q2-earnings-supplement.pdf` |
| NextEra | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/q2-2026/nextera-2026-q2-earnings-presentation.pdf`; `raw/primary-sources/capital-flow/power-grid-pilot/nextera/q2-2026/nextera-2026-q2-earnings-release.pdf`; `raw/primary-sources/capital-flow/power-grid-pilot/nextera/q2-2026/nextera-2026-q2-prepared-remarks.pdf` |

## What This Answers

The previous availability audit found that the raw source files were not mounted in the current workspace. This pass fixes that for the main official Q2 2026 evidence package.

The acquired source set is enough to begin priority-1 extraction for:

- ONEOK capex, guidance, adjusted EBITDA, volume growth, and source-document discovery
- MasTec backlog, segment results, cash flow, leverage, liquidity, and 10-Q filing resolution
- Plains Cactus III, growth capital, debt reduction, adjusted EBITDA, leverage, and free cash flow
- Targa volume denominators, operating-margin bridge, growth capital, maintenance capital, and business mix
- NextEra FPL capex, regulatory capital employed, Energy Resources backlog, placed-in-service projects, large-load interest, and management risk framing

## What This Still Does Not Prove

This is acquisition evidence, not by itself extraction evidence.

The follow-through metric extraction pass now parses the downloaded PDFs and HTML pages into metric rows, but the following limits remain:

- ONEOK still needs direct financial-table/presentation asset resolution if the HTML pages do not contain all tables.
- MasTec's 10-Q page still needs filing-document resolution or SEC source extraction.
- Plains still needs shipper/tariff evidence beyond the company PDFs.
- Targa still needs project-level contribution and utilization tests, not only aggregate volume charts.
- NextEra still needs FPL docket/order/rider proof for recovery-grade claims.

## Decision

`pilot-source-acquisition-complete - ten official Q2 2026 source files were fetched locally and are ready for parsing into priority-1 extraction rows.`

## Safe Claim

`The first power/grid/project-finance pilot now has locally acquired official Q2 2026 source artifacts for ONEOK, MasTec, Plains, Targa, and NextEra. These files support the next extraction pass, but they do not by themselves promote any company to project-return, backlog-quality, tariff/contract durability, or recovery-grade evidence.`

## Claims Not To Make Yet

Do not say:

- downloaded file equals extracted metric
- the acquired source set proves project-level returns
- company PDFs replace missing tariff, shipper, PPA, or regulatory docket evidence
- the global download log preserves all ten single-source fetches, because the current fetcher overwrites the log on each filtered run
