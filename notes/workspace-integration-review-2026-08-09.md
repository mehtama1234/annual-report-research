# Workspace Integration Review

Date: 2026-08-09

## Scope reviewed

- `/home/manishmehta/ui-projects/annual-report-research`
- `/home/manishmehta/ui-projects/ibis-industries`
- `/home/manishmehta/projects` for overlapping annual-report or industry-research workspaces

## What exists now

### 1. Annual report research is the evidence repository

`annual-report-research` is now the cleanest source-of-truth workspace for:

- `2025` annual reports and annual filings
- `2026` quarterlies plus the needed late-`2025` trailing quarter
- normalized company packets
- sector briefs and theme memos

The repo structure is disciplined:

- `raw/` for evidence
- `extracted/` for normalized company-level packets
- `analysis/` for sector and theme synthesis
- `indexes/` for coverage and taxonomy control

This is the right base layer for any downstream sector, industry, or theme product.

### 2. IBIS industries is the broad industry synthesis layer

`ibis-industries` already contains:

- `briefs_full.json`
- `trends_full_raw.json`
- a large set of rendered force pages under `forces/`
- operator outputs such as `operator_playbooks.json`

That project is broader and more horizontal than the annual-report repo. It is built around industry writeups and force-pattern synthesis, not around auditable company evidence chains.

### 3. No second comparable annual-report workspace was found under `/home/manishmehta/projects`

A scan of `/home/manishmehta/projects` did not surface another active company-earnings / annual-report archive comparable to `annual-report-research`.

The adjacent path referenced in the README does exist:

- `/home/manishmehta/projects/Misc/ui-projects/strategy-under-a-force/`

That workspace is a force-driven narrative layer with many subprojects such as `the-compute-buildout`, `the-admin-burden-economy`, `value-migration`, `the-energy-transition`, and `real-estate-is-the-moat`. It is not a second filing archive.

## Structural comparison

### Annual-report-research strengths

- auditable raw-source separation
- company-by-company coverage tracking
- sector and industry taxonomy tied to named firms
- better support for claims like "what changed in 2025 and the last three quarters"

### IBIS-industries strengths

- wider industry surface area
- better cross-industry packaging for theme exploration
- already has force frameworks that map well to cultural, consumer, industrial, and technological narratives

### Current gap between them

The two projects are complementary, but not yet mechanically linked.

Today:

- `annual-report-research` knows which specific companies prove a theme
- `ibis-industries` knows how to express broader industry and force narratives

What is still missing is a stable bridge that says:

- which annual-report companies should map into which IBIS force pages
- which annual-report theme memos should refine or correct the current force narratives
- which company packets are the best evidence packets for each force

## Best current mapping

The strongest immediate alignments are:

- `analysis/themes/technology-ai-platform-initial-theme-memo.md`
  -> `ibis-industries/forces/the-ai-rewiring/`
- `analysis/themes/financial-asset-management-flows-and-fee-rate-pressure-initial-theme-memo.md`
  -> `ibis-industries/forces/money-gets-unbundled/`
- `analysis/themes/financial-alternative-manager-fees-and-realizations-initial-theme-memo.md`
  -> `ibis-industries/forces/money-gets-unbundled/`
- `analysis/themes/financial-market-infrastructure-and-risk-transfer-initial-theme-memo.md`
  -> `ibis-industries/forces/money-gets-unbundled/`
- `analysis/themes/industrial-automation-and-infrastructure-initial-theme-memo.md`
  -> `ibis-industries/forces/atoms-strike-back/` and `ibis-industries/forces/the-electrification/`
- `analysis/themes/cultural-value-trust-and-automation-initial-theme-memo.md`
  -> `ibis-industries/forces/the-channel-shift/`, `the-experience-economy/`, and `the-ai-rewiring/`
- `analysis/themes/healthcare-policy-and-portfolio-initial-theme-memo.md`
  -> `ibis-industries/forces/the-health-reckoning/` and `the-pricing-power-collapse/`
- `analysis/themes/regulation-trust-and-sovereignty-risk-initial-theme-memo.md`
  -> `ibis-industries/forces/the-compliance-tax/` and `the-breach-economy/`

## Recommended next steps

1. Treat `annual-report-research` as the only evidence base for public-company proof points from `2025` and `2026`.

2. Keep using the bridge indexes already inside `annual-report-research`, especially:

   - `indexes/force-map.csv`

   With columns such as:

   - `force_slug`
   - `theme_memo`
   - `sector`
   - `industry`
   - `company`
   - `why_it_belongs`
   - `priority`

3. For each major IBIS force, nominate `3-8` anchor public companies from the annual-report archive.

4. Use the annual-report theme memos to tighten IBIS force pages where the current narrative is too generic and not grounded in named company evidence.

5. Keep annual-report collection separate from force-page writing.
   The current separation is good engineering and should not be collapsed into one repo.

## Practical conclusion

The repo layout is directionally correct.

- `annual-report-research` should remain the evidence and company-packet system.
- `ibis-industries` should remain the wide industry and force narrative system.
- The next useful piece is a small bridge layer, not a merger.

That bridge already exists in early form, and tightening it is the fastest path to making sector, industrial, consumer, cultural, and other recurring themes more explicit across both workspaces.
