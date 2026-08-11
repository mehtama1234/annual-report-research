# Raw Evidence Link Policy

Date: 2026-08-11

## Packet Inputs Used

- the remote-`main` storage model that keeps extracted research, notes, indexes, and analysis in Git while offloading heavy `raw/**` payloads
- `notes/raw-blob-offload-readme-2026-08-10.md`
- `indexes/raw-blob-offload-manifest-2026-08-10.csv`
- `indexes/raw-blob-offload-summary-2026-08-10.tsv`
- the current packet, profile, and source-ledger layer where raw provenance must stay auditable even when the raw files are not locally present

## Purpose

This note explains how to read packet evidence links now that heavy `raw/**` payloads have been offloaded from remote `main`.

The goal is to preserve source provenance without pretending that every raw artifact still lives as a local file inside the Git checkout.

## Current state

- Live navigation and synthesis documents now point at the current `annual-report-research` repo.
- The remaining legacy-root references are concentrated in company packets, company profiles, and source ledgers that cite `raw/**` evidence.
- Those evidence links are not ordinary repo-navigation links anymore. They are provenance pointers into the raw-offload system.

## Why the raw links were not mass-rewritten

- Remote `main` intentionally does not carry the heavy `raw/**` payload.
- The offloaded files now live in Google Drive tar archives documented by:
  - `notes/raw-blob-offload-readme-2026-08-10.md`
  - `indexes/raw-blob-offload-manifest-2026-08-10.csv`
  - `indexes/raw-blob-offload-summary-2026-08-10.tsv`
- Blindly replacing every packet-level raw citation with a different string would create a large, noisy rewrite across hundreds of evidence files and would make local provenance harder to audit.

## Reader rule

Treat remaining raw-link references in packets, profiles, and source ledgers as evidence identities, not as guaranteed on-disk paths inside remote `main`.

If you need the actual offloaded location, resolve the raw path through the manifest.

## Resolver

Use:

```bash
python3 scripts/resolve-offloaded-raw-path.py 'raw/sec/healthcare/medical-distribution/cencora/2026-q2-10q.html'
```

Or, if you only need the Drive URL:

```bash
python3 scripts/resolve-offloaded-raw-path.py --url-only 'raw/sec/healthcare/medical-distribution/cencora/2026-q2-10q.html'
```

The resolver also accepts absolute raw paths copied from legacy packet links, as long as they resolve to a `raw/...` location.

## What the resolver returns

- `local_path`
- `drive_url`
- `bytes`
- `sha256`
- `source_family`
- `sector`
- `industry`
- `company_slug`
- `as_of_date`
- `offloaded_by_commit`
- `notes`

This makes the packet evidence layer auditable without restoring the full raw tree into Git.

## Practical interpretation

- `analysis/`, sector briefs, sector syntheses, and theme/framework pages should use current repo links.
- `extracted/.../company-packet.md`, `company-profile.md`, and `source-ledger.md` may still carry raw provenance pointers that must be resolved through the manifest.
- historical offload notes may still mention prior repo/worktree names because they document how the offload happened, not how current live navigation should work.

## Next-step standard

For future packets created after this policy note:

- keep the evidence chain explicit
- prefer current-repo links for live extracted and analysis documents
- when raw evidence is offloaded, ensure the manifest contains the raw path and Drive pointer
- prefer resolver-based provenance over ad hoc path rewrites

## Insight-System Maintenance

When you need to confirm that the raw-evidence provenance rule, offload manifest model, and legacy-root boundary still line up before relying on this policy note, use:

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

- Does this note make it clear that remaining packet-level raw links are provenance pointers rather than guaranteed local files on remote `main`?
- Can a skeptical reader find the exact manifest, resolver, and Drive-pointer path needed to recover a cited raw artifact?
- Does the policy explain why the repo kept raw provenance stable instead of performing a high-noise rewrite across hundreds of packet files?
- What future raw-offload change would require updating this policy note, the manifest, or the resolver behavior?
