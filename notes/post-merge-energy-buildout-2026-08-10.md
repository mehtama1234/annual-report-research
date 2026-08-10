# Post-Merge Energy Buildout Note

Date: 2026-08-10
Merged into `main`: `3e43ea8a`
Source branch: `parallel/energy-buildout`
Source branch head at merge: `123ffb9d`

## What landed

- The energy and heavy-input batch was merged from `parallel/energy-buildout` into `main`.
- The audited batch count is `80` completed companies and `0` partial companies.
- The branch note remains the primary batch artifact:
  - `notes/energy-buildout-batch-2026-08-10.md`

## Scope of the merged batch

- upstream independents
- oil and gas pipelines and integrated midstream or NGL systems
- oilfield equipment and services
- refining and marketing
- supporting heavy-input comparison lanes across metals, mining, chemicals, fertilizer, uranium, and packaging where those comparisons materially sharpen the commodity-system synthesis

## Important audit conclusions

- Shared repo-wide indexes were intentionally not updated inside the branch workflow; the coherent batch output is the packet tree plus the branch note.
- A direct audit confirmed that all `80` companies counted in the branch note have the full extracted triad on disk:
  - `company-packet.md`
  - `company-profile.md`
  - `source-ledger.md`
- Some thematic comparison bullets mention pre-existing archive packets such as `CF Industries`, `Nutrien`, `Dow`, and `Graphic Packaging`; those are contextual comparisons, not additional completed names from this batch.
- `Civitas Resources` was explicitly rejected as a clean next target because, as of Monday, August 10, 2026, the authoritative source chain did not support a normal standalone `2025` annual-report-plus-latest-three-quarters packet after the `SM Energy` merger closed on `January 30, 2026`.

## Post-merge cleanup

- The `parallel/energy-buildout` worktree was cleaned after merge.
- Removed only the documented untracked leftovers:
  - abandoned `Civitas Resources` raw stub folders
  - duplicate `Tourmaline` `2025-aif.pdf`
  - bad or low-value `MPLX` IR slide and events captures

## Remaining unrelated dirt

- `main` still has unrelated untracked `Walgreens Boots Alliance` raw folders under:
  - `raw/annualreports/healthcare/drug-stores/walgreens-boots-alliance-inc/`
  - `raw/company-ir/healthcare/drug-stores/walgreens-boots-alliance-inc/`
  - `raw/sec/healthcare/drug-stores/walgreens-boots-alliance-inc/`
- Those folders were already present and were not part of the energy merge.
