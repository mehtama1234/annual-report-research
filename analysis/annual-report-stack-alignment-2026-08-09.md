# Annual Report Stack Alignment

Date baseline: 2026-08-09

## Purpose

This note records how the current `annual-report-research/` workspace fits with the two adjacent projects already on disk:

- `/home/manishmehta/ui-projects/ibis-industries/`
- `/home/manishmehta/projects/Misc/ui-projects/strategy-under-a-force/`

The goal is to keep the annual-report archive as the evidence layer that feeds those larger synthesis systems rather than letting all three projects drift into parallel taxonomies.

## What each project is doing

### `annual-report-research/`

- Company-level evidence archive for public companies
- Focused on `2025` annual reports and annual filings plus the latest `2026` quarter chain, pulling in late `2025` only when needed for the trailing-three-quarter window
- Organized into:
  - `raw/`
  - `extracted/`
  - `analysis/`
  - `indexes/`

This is the cleanest source-of-truth layer for company packets, quarter windows, and dated filing evidence.

### `ibis-industries/`

The repo README and framework files show that `ibis-industries/` is the broader industry and economy interpretation layer:

- full `1,491`-industry US corpus
- force layer
- theme layer
- operator layer
- company layer

Its strongest top-level frames are:

- industrial trends
- consumer trends
- cultural and social trends
- societal and institutional trends
- operator and business-model lenses

Its major force buckets include:

- `the-compute-super-cycle`
- `atoms-strike-back`
- `the-real-estate-reckoning`
- `the-health-reckoning`
- `the-channel-shift`
- `the-graying-market`
- `the-compliance-tax`
- `money-gets-unbundled`

### `strategy-under-a-force/`

The adjacent project under `projects/Misc/ui-projects/strategy-under-a-force/` is not a raw filing archive. It is a narrative and dossier layer organized around force-specific pages such as:

- `the-compute-buildout`
- `the-admin-burden-economy`
- `real-estate-is-the-moat`
- `passive-investing`
- `the-great-rebuild`
- `value-migration`
- `the-loyalty-economy`

This makes it a downstream interpretation surface, not a substitute for the annual-report collection workspace.

## Current alignment

The annual-report archive is already lining up well with the stronger `ibis-industries` frames.

### Industrial and infrastructure alignment

The current annual-report sectors most directly support:

- `physical-reindustrialization-and-infrastructure`
- `machine-intelligence-and-compute-buildout`
- `space-housing-and-local-friction`

The clearest evidence chains already in the archive are:

- Utilities:
  - AEP
  - NextEra
  - Duke
  - Alliant
  - Exelon
  - Consolidated Edison
  - Vistra
  - Constellation
  - NRG
- Industrial Goods:
  - Caterpillar
  - Honeywell
  - Eaton
  - Trane
  - Northrop
  - Union Pacific
  - Waste Management
  - ABM
- Real Estate:
  - Prologis
  - Equinix
  - Digital Realty
  - AvalonBay
  - CBRE
  - JLL

Those names form the company-evidence bridge from:

- `the-compute-super-cycle`
- `atoms-strike-back`
- `the-real-estate-reckoning`
- `the-great-consolidation`

down into actual annual reports, `10-K`s, `10-Q`s, earnings releases, and transcripts.

### Consumer and cultural alignment

The annual-report archive also already supports the `ibis-industries` consumer and cultural stack:

- `barbelled-consumer-america`
- `experience-status-and-community`
- `wellness-recodes-daily-life`

The current consumer-goods and services coverage gives live company evidence for:

- affordability versus premium split
- health and wellness demand shifts
- service-density and route-density economics
- trust-sensitive everyday categories

This is the cleaner company-evidence layer beneath broader force language like:

- `the-hollow-middle`
- `the-channel-shift`
- `the-health-reckoning`
- `the-experience-economy`

### Institutional and operating-infrastructure alignment

The strongest cross-project overlap right now is around institutional and operating complexity.

`annual-report-research/analysis/themes/` already includes theme memos such as:

- `institutional-operating-infrastructure`
- `regulation-trust-and-sovereignty-risk`
- `capital-intensity-and-investment-concentration`

Those themes map closely onto both:

- `ibis-industries` forces like `the-compliance-tax`, `money-gets-unbundled`, and `the-ai-rewiring`
- `strategy-under-a-force` pages like `the-admin-burden-economy`, `the-compute-buildout`, and `real-estate-is-the-moat`

## What is now clear

1. `annual-report-research/` should remain the evidence and packetization system.
2. `ibis-industries/` should remain the full-economy and force-map system.
3. `strategy-under-a-force/` should remain the narrative and dossier surface built on top of the force logic.

That division is coherent.

## Where the annual-report archive is strongest

The archive is strongest where named public-company evidence is the missing link between macro force language and investable operators:

- utilities and power scarcity
- industrial electrification and cooling
- logistics and data-center real estate
- financial scale and intermediation
- healthcare policy and operating friction
- consumer affordability versus premium resilience

## Best next integration moves

1. Keep expanding annual-report coverage in sectors that sharpen already-proven force maps rather than chasing disconnected names.
2. Prioritize companies that fill a missing business-model contrast inside an existing force, the same way NRG improved the utilities set.
3. Use the annual-report sector briefs as the upstream evidence source for future refreshes in:
   - `ibis-industries/theme-briefs/`
   - `ibis-industries/forces/`
   - `projects/Misc/ui-projects/strategy-under-a-force/`

## Highest-value next company gaps from this perspective

- Utilities:
  - a more stressed conventional-generation or fuel-concentrated utility
  - or a more purely regulated gas or hydro utility
- Consumer:
  - a cleaner live-experience or status-through-experience public-company set
- Cultural:
  - a more explicit loneliness, community, or identity-driven demand cluster
- Institutional:
  - more admin-burden and compliance-heavy operators beyond the current healthcare and services base

## Working conclusion

The annual-report workspace is not redundant with the other two projects. It is the disciplined source layer they were missing.

The practical rule should be:

- collect here
- interpret there
- keep the taxonomy bridges explicit
