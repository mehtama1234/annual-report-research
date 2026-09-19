# Reproducibility gap — RH and Wayfair evidence chains

Date: `2026-09-14`

## Packet Inputs Used

- [RH company packet](../extracted/services/home-furnishing-stores/rh/company-packet.md)
- [RH source ledger](../extracted/services/home-furnishing-stores/rh/source-ledger.md)
- [Wayfair company packet](../extracted/services/home-furnishing-stores/wayfair-inc/company-packet.md)
- [Wayfair source ledger](../extracted/services/home-furnishing-stores/wayfair-inc/source-ledger.md)
- `indexes/raw-blob-offload-manifest-2026-08-10.csv`
- `scripts/resolve-offloaded-raw-path.py`

## Finding

The RH and Wayfair packets preserve source identity, filing dates, official
source URLs, and extracted operating facts. Their source ledgers originally
displayed legacy absolute paths under
`/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/`.
That older worktree is not present in the current environment.

The core SEC annual, continuity-quarter, and latest-quarter artifacts listed
below have now been restored locally under the documented `raw/sec/...`
identity: RH FY2025 10-K, Q3 FY25 10-Q/8-K, and Q1 FY26 10-Q; Wayfair FY2025
10-K, Q3 FY25 10-Q, Q4 FY25 8-K, Q1 FY26 10-Q/8-K, and Q2 2026 10-Q/8-K. Their
source URLs, byte counts, and SHA-256 digests are recorded in
[`rh-wayfair-restored-artifacts-2026-09-14.tsv`](rh-wayfair-restored-artifacts-2026-09-14.tsv).

The raw-path resolver was tested against representative filings:

```text
python3 scripts/resolve-offloaded-raw-path.py 'raw/sec/services/home-furnishing-stores/rh/2025-10k.html'
python3 scripts/resolve-offloaded-raw-path.py 'raw/sec/services/home-furnishing-stores/wayfair-inc/2026-q2-10q.html'
```

The legacy resolver paths remain absent from the offload manifest because the
restored files are now ordinary local evidence under `raw/sec/...`, not Drive
offloads. The corresponding IR PDFs, remaining SEC exhibits and wrappers, and
earnings-call transcripts remain absent from the current checkout. The reader
can now recover the core SEC filing artifacts locally, while the remaining
source chain is still explicitly qualified.

## External recovery routes added

The following official routes remain recorded as a fallback for the artifacts
that are not locally restored. They let a reader recover the authoritative
filing directly from SEC EDGAR while the remaining local-artifact gap stays
visible.

| Company | Filing or source route | Official URL |
|---|---|---|
| RH | SEC submissions index | [CIK0001528849 submissions](https://data.sec.gov/submissions/CIK0001528849.json) |
| RH | FY2025 Form 10-K | [RH 2025 10-K filing](https://www.sec.gov/Archives/edgar/data/1528849/000110465926037992/rh-20260131x10k.htm) |
| RH | Latest Q2 FY2027 Form 10-Q | [RH Q2 FY2027 10-Q filing](https://www.sec.gov/Archives/edgar/data/1528849/000110465926106764/rh-20260801x10q.htm) |
| RH | Investor-relations entry point | [RH investor relations](https://investor.rh.com/) |
| Wayfair | SEC submissions index | [CIK0001616707 submissions](https://data.sec.gov/submissions/CIK0001616707.json) |
| Wayfair | FY2025 Form 10-K | [Wayfair 2025 10-K filing](https://www.sec.gov/Archives/edgar/data/1616707/000161670726000027/w-20251231.htm) |
| Wayfair | Q2 2026 Form 10-Q | [Wayfair Q2 2026 10-Q filing](https://www.sec.gov/Archives/edgar/data/1616707/000161670726000150/w-20260630.htm) |
| Wayfair | Investor-relations entry point | [Wayfair investor relations](https://investor.wayfair.com/) |

These links remain direct source routes for the un-restored material. The
restored filing paths and checksums are recorded separately in the TSV noted
above.

## Effect on conclusions

The RH and Wayfair dossiers remain useful qualified analyses because their
claims are explicitly attributed to the preserved company packets and source
ledgers. The restored SEC filings now support local recovery of the core
annual, continuity-quarter, and latest-quarter evidence. The dossiers should still not be described as
fully reproducible for the entire source chain until the remaining IR,
wrapper/exhibit, and transcript artifacts are restored or explicitly recorded
as externally recoverable.

No valuation precision is added because of this gap. The dossiers retain
explicit exclusions where a synchronized market snapshot, scenario row, or
direct raw artifact is unavailable.

## Required recovery action

For each remaining RH and Wayfair source-ledger row, confirm one of the following:

1. the raw artifact is restored under the documented `raw/...` identity and
   added to the offload manifest with its checksum and Drive pointer; or
2. the official SEC or IR URL is preserved as a direct external source and the
   packet clearly labels the evidence as externally recoverable rather than
   locally recoverable.

Until that action is complete, keep the affected company conclusions at a
qualified evidence grade and keep the remaining gap visible in future handoffs.

## Skeptical Reader Test

- Can the reader distinguish a source identity from a file that is locally
  recoverable?
- Can the reader verify the restored filing artifacts by local path and
  SHA-256 digest?
- Can the reader see the exact resolver test and the manifest result?
- Does the gap reduce confidence in reproducibility without erasing the
  packet-backed analysis?
- Is the recovery action concrete and testable?

## Insight-System Maintenance

Use these checks after restoring or re-registering either evidence chain:

- `python3 scripts/resolve-offloaded-raw-path.py 'raw/sec/services/home-furnishing-stores/rh/2025-10k.html'`
- `python3 scripts/resolve-offloaded-raw-path.py 'raw/sec/services/home-furnishing-stores/wayfair-inc/2026-q2-10q.html'`
- `bash scripts/audit-legacy-root-references.sh`
- `bash scripts/verify-insight-system.sh`
