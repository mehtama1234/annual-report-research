# Post-Merge Energy Buildout Note

Date: 2026-08-10
Merged into `main`: `3e43ea8a`
Source branch: `parallel/energy-buildout`
Source branch head at merge: `123ffb9d`

## Packet Inputs Used

- the merged branch note that remains the primary artifact for the energy and heavy-input batch
- the post-merge audit of completed-company count, partial-company count, and extracted triad presence on disk
- the cleanup log documenting which leftover raw artifacts were intentionally removed and which unrelated dirt remained on `main`
- the branch-level scope description that defines what actually landed in the merge
- the repo rule that post-merge notes should state both what is now on `main` and what was intentionally left outside the merge

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

## Insight-System Maintenance

When you need to confirm that this post-merge energy note, the main batch artifact, and the broader continuation stack still line up before using it as the merge-state reference, use:

- `bash scripts/run-insight-audit-stack.sh`
- `bash scripts/refresh-note-layer-boundary.sh`
- `bash scripts/audit-audit-stack-terminology.sh`
- `bash scripts/audit-maintenance-doc-stack.sh`
- `bash scripts/audit-continuation-mode-links.sh`
- `bash scripts/audit-remaining-brief-links.sh`
- `bash scripts/audit-remaining-stack-links.sh`
- `bash scripts/audit-browser-review-links.sh`
- `bash scripts/verify-insight-system.sh`

## Skeptical Reader Test

- Does this post-merge note make clear what landed on `main`, what was audited, and what remained intentionally outside the merge?
- Can a skeptical reader tell the difference between energy-batch artifacts and unrelated dirt already present on `main`?
- Does the note provide enough detail to trust the post-merge cleanup without rereading the source branch from scratch?
- What missing merge or audit detail would make the post-merge state hard to verify?
