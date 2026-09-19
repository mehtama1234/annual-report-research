# Internal link audit — 2026-09-14

Command:

```bash
python3 scripts/check-internal-links.py
```

The checker scans Markdown links under `analysis/`, ignores web URLs and
anchors, resolves repository-root paths, and understands the older archive
roots used by the research notes.

Current result:

- 2,333 internal links scanned.
- 191 links do not resolve in the current checkout.
- 191 point to the retired `/cluster/` publication workspace.
- The eight older relative source-file references in financial company pages
  were relinked to the available company evidence packets, with labels changed
  so the reader does not mistake a packet for the original Form 10-K.

This is a reproducibility boundary, not a claim that the research conclusions
are false. The reader marks unavailable local references and preserves an
archive or source-ledger handoff when one exists. The retired `/cluster/`
links belong to historical scaffolding and should be repaired only when that
older page is part of a current reading path.

## Packet Inputs Used

- all Markdown files under `analysis/`;
- repository-root and legacy-root resolution rules in
  `scripts/check-internal-links.py`; and
- the current archive manifest and source-ledger locations.

## Skeptical Reader Test

- Can a reader tell which unresolved links are retired historical scaffolding?
- Does the checker preserve direct external URLs and anchors rather than
  misclassifying them as broken local files?
- Do new dossiers link to a local packet, a source ledger, an archive route, or
  an explicit evidence boundary?

## Insight-System Maintenance

Run:

```text
python3 scripts/check-internal-links.py
```

Review any new unresolved path individually before changing a current research
link or classifying it as retired historical material.

The repository control check is `bash scripts/verify-insight-system.sh`.
