# Insight Note Standardization Cutoff

Date: 2026-08-11
Repo: `annual-report-research`

## Packet Inputs Used

- the current `notes/*.md` inventory after the insight-evidence-chain standardization pass
- the repo rule that reusable control, goal, planning, mapping, and status notes should carry `## Packet Inputs Used` and `## Skeptical Reader Test`
- the current verifier-backed note layer that now covers the reusable operating system for lane selection, packet expectations, insight extraction, and archive continuity
- the remaining note inventory, which is now dominated by per-batch handoffs, per-company extension handoffs, raw-offload handoffs, and execution logs
- the practical need to stop high-value standardization work at the point where additional edits would mostly rewrite historical logs rather than strengthen the reusable system

## What Was Standardized

The reusable note layer was standardized to make the archive's operating system auditable.

That includes:

- master goals and instruction notes
- lane runbooks and insight-system notes
- control notes for blind-spot ownership and batch selection
- kickoff briefs and active execution queues
- archive-wide audit, mapping, and integration reviews
- reusable planning, batch-shaping, collection-window, and status notes
- selected reusable handoff notes that still function as enduring operator guidance

The purpose of the two added sections is:

- `Packet Inputs Used`
  - to show what source or control inputs a note is actually built from
- `Skeptical Reader Test`
  - to force each reusable note to state what a careful reader should be able to verify from it

## Deliberate Cutoff

The remaining unstamped note files are mostly historical execution artifacts.

The cutoff is now backed by two machine-readable manifests whose union should cover every current top-level `notes/*.md` file:

- reusable operating notes
- historical handoff and log notes

Direct audit script:

- `bash scripts/audit-note-layer-boundary.sh`
- `bash scripts/audit-note-layer-boundary.sh --write-report notes/note-layer-boundary-audit-2026-08-11.md`

Current report artifact:

- [note-layer-boundary-audit-2026-08-11.md](note-layer-boundary-audit-2026-08-11.md)

The committed report is generated state, not hand-maintained narrative. If the manifests or note inventory change, regenerate it:

- `bash scripts/audit-note-layer-boundary.sh --write-report notes/note-layer-boundary-audit-2026-08-11.md`

Current remaining count at the cutoff:

- total remaining without both sections: `63`
- handoff files: `49`
- log files: `7`
- raw / blob / rclone operational files: `6`
- other: `1`

Machine-readable exclusion list:

- [indexes/historical-note-exclusion-files-2026-08-11.txt](../indexes/historical-note-exclusion-files-2026-08-11.txt)
- [indexes/historical-note-exclusion-categories-2026-08-11.tsv](../indexes/historical-note-exclusion-categories-2026-08-11.tsv)

Those remaining notes are largely:

- per-batch handoffs
- per-company extension handoffs
- raw offload or merge-operation handoffs
- runtime or execution logs

Most of them are valuable as historical evidence, but they are not the main reusable control layer for how the archive should operate going forward.

## Practical Rule Going Forward

If a future note is meant to be reused as part of the archive's operating system, it should include:

- `## Packet Inputs Used`
- `## Skeptical Reader Test`

If a note is mainly a one-time historical handoff or log, adding those sections is optional and should be judged case by case rather than enforced mechanically.

If a historical note eventually grows into a reusable operating note and gains both standardized sections, it should usually be moved from the historical manifest into the reusable manifest rather than left as an ambiguous exclusion.

## Skeptical Reader Test

- Does this note explain why the standardization pass stopped where it did rather than implying the remaining unstamped notes were forgotten?
- Can a skeptical reader tell the difference between the reusable note layer and the historical handoff/log layer?
- Does the cutoff preserve the stronger evidence-chain standard where it matters most without turning every historical operational record into templated prose?
- What future repo state would show that a supposedly reusable note was left outside the standardized layer by mistake?
