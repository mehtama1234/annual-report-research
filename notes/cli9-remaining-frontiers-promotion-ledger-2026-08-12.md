# CLI9 Remaining Frontiers Promotion Ledger

Date: 2026-08-12

This note converts the dirty `cli9-remaining-frontiers` worktree into an action ledger. The goal is to separate already-integrated history from true local-only work so `main` is not polluted by stale duplicates, raw-blob churn, or delete noise.

## Source worktree

- Worktree: `/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers`
- Branch: `cli9-remaining-frontiers`
- Branch head: `f33ef0de` (`Add Cencora and Quest Diagnostics frontier packets`)
- Dirty state at capture time:
  - `617` modified paths
  - `1471` deleted paths
  - `551` untracked paths

## Already integrated on `main`

These integration branches are already ancestors of `main` and should be treated as settled:

- `cli9-healthcare-integration-2026-08-10` at `14f3db8f`
- `new-lanes-integration-2026-08-10` at `1ffb00e8`
- `apparel-cluster-integration-2026-08-10` at `dfca59bc`
- `energy-buildout-integration-2026-08-10` at `dfca59bc`

Implication:

- The Cencora and Quest packet-side integration is already on `main`.
- The broad new-lanes, apparel, and energy integration passes are already on `main`.
- Do not merge `cli9-remaining-frontiers` wholesale just because it is ahead of `main` on its own branch history.

## Bucket 1: Do Not Promote From This Worktree

These paths appear dirty because the worktree is behind `main` or because raw files were intentionally removed from Git after offload. They should not be re-merged from this worktree.

### 1.1 Integrated Cencora and Quest packet deletions

These deletions are not a valid promotion target:

- `extracted/healthcare/medical-distribution/cencora/`
- `extracted/healthcare/medical-laboratories-research/quest-diagnostics-inc/`

The packet-side versions are already present on `main`.

### 1.2 Cencora and Quest raw deletions

These raw deletions should not be reintroduced into Git:

- `raw/annualreports/healthcare/medical-distribution/cencora/`
- `raw/company-ir/healthcare/medical-distribution/cencora/`
- `raw/sec/healthcare/medical-distribution/cencora/`
- `raw/annualreports/healthcare/medical-laboratories-research/quest-diagnostics-inc/`
- `raw/company-ir/healthcare/medical-laboratories-research/quest-diagnostics-inc/`
- `raw/sec/healthcare/medical-laboratories-research/quest-diagnostics-inc/`

Related pointer already on `main`:

- [notes/cli9-main-cencora-quest-raw-offload-2026-08-10.md](/notes/cli9-main-cencora-quest-raw-offload-2026-08-10.md)

### 1.3 Branch-behind packet trees that already exist on `main`

The following healthcare packet families show up as untracked in the dirty worktree, but equivalent packet trees already exist on `main`. Treat them as branch-staleness artifacts, not missing archive coverage:

- `extracted/healthcare/biotechnology/`
- `extracted/healthcare/diagnostic-substances/`
- `extracted/healthcare/drug-manufacturers-other/`
- `extracted/healthcare/drug-stores/`
- `extracted/healthcare/medical-appliances-equipment/`
- `extracted/healthcare/medical-equipment-wholesale/`
- `extracted/healthcare/specialized-health-services/`
- `extracted/healthcare/medical-distribution/adapthealth-corp/`
- `extracted/healthcare/medical-instruments-supplies/becton-dickinson-and-company/`
- `extracted/healthcare/medical-instruments-supplies/dexcom-inc/`
- `extracted/healthcare/medical-instruments-supplies/henry-schein-inc/`
- `extracted/healthcare/medical-instruments-supplies/insulet-corporation/`
- `extracted/healthcare/medical-instruments-supplies/warby-parker-inc/`
- `extracted/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/`
- `extracted/healthcare/medical-laboratories-research/labcorp-holdings-inc/`
- `extracted/healthcare/medical-laboratories-research/natera-inc/`
- `extracted/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/`

## Bucket 2: Review-Then-Promote Text Work

These are the healthcare text edits in `cli9-remaining-frontiers` that still look like genuine local-only work and deserve review for promotion.

### 2.1 Sector synthesis

- `extracted/healthcare/healthcare-sector-synthesis-2026-08-09.md`

### 2.2 Modified company packets already tracked in the worktree

- `extracted/healthcare/drug-manufacturers-general/johnson-johnson/`
- `extracted/healthcare/drug-manufacturers-general/pfizer-inc/`
- `extracted/healthcare/long-term-care-facilities/brookdale-senior-living-inc/`
- `extracted/healthcare/managed-health-care/unitedhealth-group-inc/`
- `extracted/healthcare/medical-care-facilities/hca-healthcare-inc/`
- `extracted/healthcare/medical-instruments-supplies/abbott-laboratories/`
- `extracted/healthcare/medical-instruments-supplies/baxter-international-inc/`
- `extracted/healthcare/medical-instruments-supplies/boston-scientific-corporation/`
- `extracted/healthcare/medical-instruments-supplies/intuitive-surgical-inc/`
- `extracted/healthcare/medical-instruments-supplies/stryker-corporation/`
- `extracted/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/`

Promotion rule:

- Review these as text-first changes.
- Promote only the packet, profile, ledger, and synthesis files that still improve on `main`.
- Do not carry over matching raw deletions as part of the same move.

### 2.3 Broad index and planning files

These are local-only editorial/control files, not automatic merge candidates:

- `indexes/companies.csv`
- `indexes/coverage-tracker.csv`
- `indexes/pilot-companies.md`
- `indexes/sectors.csv`
- `indexes/theme-tracker.csv`
- `indexes/research-master-map-2026-08-09.md`
- `indexes/prioritized-expansion-queue-2026-08-09.md`
- `indexes/*blind-spot*`
- `indexes/*noncovered*`
- `notes/blind-spot-*`
- `notes/*handoff*`

Promotion rule:

- Curate these at the end of a coherent batch.
- Do not merge the entire index/note surface from this worktree just because it is present.

## Bucket 3: Raw Evidence Eligible For Drive Offload

If the Bucket 2 text edits are kept, the corresponding raw evidence should move to Drive rather than back into Git history.

### 3.1 Modified healthcare raw tied to existing packet revisions

- `raw/annualreports/healthcare/medical-instruments-supplies/abbott-laboratories/`
- `raw/annualreports/healthcare/medical-instruments-supplies/baxter-international-inc/`
- `raw/annualreports/healthcare/medical-instruments-supplies/boston-scientific-corporation/`
- `raw/annualreports/healthcare/medical-instruments-supplies/thermo-fisher-scientific-inc/`
- `raw/company-ir/healthcare/medical-instruments-supplies/baxter-international-inc/`
- `raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/`

Important nuance:

- The worktree shows both deleted legacy Baxter IR PDFs and untracked replacement Baxter IR HTML pages.
- That should be handled as an offload-and-pointer refresh, not as a raw reinsertion into `main`.

### 3.2 Untracked healthcare raw trees that may support future promotion

- `raw/annualreports/healthcare/biotechnology/`
- `raw/annualreports/healthcare/diagnostic-substances/`
- `raw/annualreports/healthcare/drug-manufacturers-other/`
- `raw/annualreports/healthcare/drug-stores/`
- `raw/annualreports/healthcare/medical-appliances-equipment/`
- `raw/annualreports/healthcare/medical-distribution/adapthealth-corp/`
- `raw/annualreports/healthcare/medical-equipment-wholesale/`
- `raw/annualreports/healthcare/medical-instruments-supplies/becton-dickinson-and-company/`
- `raw/annualreports/healthcare/medical-instruments-supplies/dexcom-inc/`
- `raw/annualreports/healthcare/medical-instruments-supplies/henry-schein-inc/`
- `raw/annualreports/healthcare/medical-instruments-supplies/insulet-corporation/`
- `raw/annualreports/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/`
- `raw/annualreports/healthcare/medical-laboratories-research/labcorp-holdings-inc/`
- `raw/annualreports/healthcare/medical-laboratories-research/natera-inc/`
- `raw/annualreports/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/`
- `raw/annualreports/healthcare/specialized-health-services/`
- `raw/company-ir/healthcare/biotechnology/`
- `raw/company-ir/healthcare/diagnostic-substances/`
- `raw/company-ir/healthcare/drug-manufacturers-other/`
- `raw/company-ir/healthcare/drug-stores/`
- `raw/company-ir/healthcare/medical-appliances-equipment/`
- `raw/company-ir/healthcare/medical-distribution/adapthealth-corp/`
- `raw/company-ir/healthcare/medical-equipment-wholesale/`
- `raw/company-ir/healthcare/medical-instruments-supplies/dexcom-inc/`
- `raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/`
- `raw/company-ir/healthcare/medical-instruments-supplies/insulet-corporation/`
- `raw/company-ir/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/`
- `raw/company-ir/healthcare/medical-laboratories-research/labcorp-holdings-inc/`
- `raw/company-ir/healthcare/medical-laboratories-research/natera-inc/`
- `raw/company-ir/healthcare/medical-laboratories-research/quest-diagnostics-incorporated/`
- `raw/company-ir/healthcare/specialized-health-services/`

Offload rule:

- Only offload raw evidence for names whose text packets are still worth keeping after comparison with `main`.
- Skip duplicate evidence for trees already integrated and already supported by existing notes/manifests.

## Recommended Order

1. Ignore the Cencora and Quest delete noise in this worktree.
2. Review the eleven modified healthcare company packet families plus the healthcare sector synthesis.
3. Promote only the text improvements that still beat `main`.
4. Offload any supporting raw evidence for the kept names to Drive and record a pointer note.
5. Leave the huge blind-spot index/note surface for a separate integration pass.

## August 12 review result

The healthcare text-review pass was completed on `2026-08-12`.

Result: no packet or synthesis files from this healthcare salvage set were promoted to `main`.

Why:

- Johnson & Johnson, Pfizer, Brookdale, and HCA only differed by local link rewrites from worktree-specific raw paths to the canonical `annual-report-research/raw/...` paths already used on `main`.
- UnitedHealth was a regression relative to `main`:
  - older date baseline
  - removal of `proven` status language
  - removal of the locally preserved `Q2 2026` `10-Q`
- Stryker pointed at an obsolete sibling workspace path (`annual-report-research-cli8-middle-layer`) rather than improving the canonical source chain.
- Abbott, Baxter, Boston Scientific, Intuitive Surgical, Thermo Fisher, and the healthcare sector synthesis produced no net text diff against `main` in this review pass.

Operational conclusion:

- Treat the healthcare salvage portion of `cli9-remaining-frontiers` as closed for packet promotion.
- Any further value in this worktree is more likely to come from curated raw offload or from the broader blind-spot planning surface, not from direct packet merges.

## Short Version

`cli9-remaining-frontiers` is not a merge candidate. It is a salvage candidate.

- Salvage text improvements selectively.
- Offload supporting raw evidence selectively.
- Do not merge branch-behind duplicates.
- Do not reintroduce raw blobs that were already intentionally moved out of Git.
