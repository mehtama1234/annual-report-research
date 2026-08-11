# Legacy Root Reference Audit

Date: 2026-08-11

## Purpose

This note records the remaining footprint of the retired repo root:

`/home/manishmehta/ui-projects/annual-report-research-new-lanes`

The goal is to prove that live navigation has been normalized and that the remaining references are now either:

- raw-evidence provenance pointers
- explicit historical offload notes

## Audit result

As of `2026-08-11`, the remaining markdown footprint is:

- files still containing the retired repo root: `555`
- files where the remaining reference is specifically a `.../raw/...` provenance path: `553`
- files where the remaining reference is historical or non-raw: `2`

The remaining non-raw historical files are:

- `notes/new-lanes-raw-blob-offload-2026-08-10.md`
- `notes/legacy-root-reference-audit-2026-08-11.md`

Those notes intentionally preserve historical naming context:

- source worktree: `/home/manishmehta/ui-projects/annual-report-research-new-lanes`
- source raw tree: `/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw`

## Interpretation

This means the current repo boundary is now clear:

- live docs, sector briefs, sector syntheses, and framework pages should use the current `annual-report-research` repo root
- packet-level evidence links may still carry legacy raw provenance paths because the heavy `raw/**` payload was offloaded from remote `main`
- historical offload notes may still name the old worktree because they are documenting what happened, not offering live navigation

## How to verify

Run:

```bash
bash scripts/audit-legacy-root-references.sh
```

That script prints:

- total markdown files still mentioning the retired root
- the subset that are raw-evidence files
- the residual historical or non-raw files
- the heaviest raw-evidence files by frequency of retained provenance links

## How to resolve raw evidence

If a remaining packet or source-ledger link points into the retired raw workspace, resolve it through:

```bash
python3 scripts/resolve-offloaded-raw-path.py 'raw/.../file.ext'
```

Supporting references:

- `notes/raw-evidence-link-policy-2026-08-11.md`
- `notes/raw-blob-offload-readme-2026-08-10.md`
- `indexes/raw-blob-offload-manifest-2026-08-10.csv`

## Why this is enough for now

Mass-rewriting hundreds of packet-level raw citations would create high-noise churn across the evidence layer without improving provenance.

The archive now has a cleaner split:

- navigation uses the current repo root
- provenance resolves through the offload manifest and Drive pointers
