# Capital Flow Power/Grid Pilot Official Source Discovery Pass 1

## Purpose

This page turns the priority-1 source-availability gap into official source routes.

The question is:

`Can we identify official public source URLs for the raw filings, releases, presentations, supplements, and regulatory materials needed to upgrade the first five-company pilot?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-power-grid-pilot-official-source-discovery-pass-1.csv`

## Short Answer

Yes. The current workspace does not have the raw files mounted locally, but official online routes now exist for the main Q2 2026 source packages.

This pass adds `14` source-discovery rows:

| Company | Discovered Official Sources | Current Status |
|---|---:|---|
| ONEOK | `2` | official routes found; direct PDF links still need asset resolution |
| MasTec | `3` | official hub, presentation PDF, and 10-Q filing page found |
| Plains | `3` | official hub, earnings presentation PDF, and earnings release PDF found |
| Targa | `2` | official hub and earnings supplement PDF found |
| NextEra | `4` | official hub, presentation PDF, release PDF, and remarks PDF found |

## What This Changes

The prior source-availability audit said the priority-1 raw artifacts were not mounted in the current repo. That remains true.

This pass adds the next missing layer: official web routes that can be fetched, opened, or used as browser-backed evidence sources.

The immediate next step is to run the acquisition workflow against these source URLs, then extract fields into priority-1 result rows.

The source acquisition result is now:

`/cluster/capital-flow-power-grid-pilot-source-acquisition-results-pass-1.md`

It confirms that `10` official source artifacts were fetched locally and are ready for parsing.

The priority-1 metric extraction pass is now:

`/cluster/capital-flow-power-grid-pilot-priority1-metric-extraction-pass-1.md`

It extracts `30` metric rows from the acquired source package.

## Source Discovery By Company

| Company | Best Immediate Source | Why |
|---|---|---|
| ONEOK | Q2 2026 earnings release page and 2026 financial reports page | official confirmation of Q2 slots and current quarter financial/volume context |
| MasTec | Q2 2026 earnings presentation PDF | segment results, backlog by segment, cash flow, leverage, liquidity, and guidance are already visible in the official PDF |
| Plains | Q2 2026 earnings release and presentation PDFs | Cactus III, growth capital, debt reduction, crude transition, and leverage are the core upgrade fields |
| Targa | Q2 2026 earnings supplement PDF | volume denominators and segment operating-margin bridge are visible in the official supplement |
| NextEra | Q2 2026 release and presentation PDFs | FPL capital/recovery proxy and Energy Resources backlog/origination fields are available from official materials |

## Decision

`official-source-routes-discovered - the first five-company pilot now has official source URLs for the next acquisition and extraction pass.`

## Safe Claim

`The priority-1 upgrade program has official public source routes for the main Q2 2026 evidence packages, but those documents still need to be locally acquired and extracted before any project-return, backlog-quality, tariff/contract durability, or recovery-grade promotion is allowed.`

## Claims Not To Make Yet

Do not say:

- source discovery equals source extraction
- official source routes mean the raw files are already local
- the priority-1 tasks have been promoted
- the discovered documents necessarily contain every requested project-return field
- FPL regulatory dockets or Plains tariff/shipper contracts are fully discovered
