# Thin-Lane Window And Source-Authority Audit

Date baseline: `2026-08-11`
Repo: `annual-report-research`

## Purpose

This note tests one of the exact remaining-work items from the original-goal audit:

- whether thin-lane anchor packets really prove the `2025` annual plus latest-three-reported-quarters standard as of `2026-08-10`
- whether they clearly show AnnualReports as taxonomy only and company IR plus SEC as the authoritative source chain when AnnualReports lags

This is not a repo-wide audit.

It is a targeted audit of thin-lane anchors that matter disproportionately to honest closeout quality.

## Anchors reviewed

- `UnitedHealth Group`
- `HCA Healthcare`
- `Sysco`
- `MetLife`
- `Zebra Technologies`
- `Hewlett Packard Enterprise`
- `Epson`

## Status key

- `proven`: the current packet and ledger explicitly prove both the filing window and the authority rule
- `qualified`: the packet is still usable and mostly authoritative, but the proof relies on fallback methods, partial local capture, or weaker explicitness
- `needs repair`: the current packet contains an internal contradiction, unresolved path problem, or evidence gap large enough that the proof chain is not clean

## Audit results

| Company | Filing-window proof | Source-authority proof | Status | Exact reason |
|---|---|---|---|---|
| `UnitedHealth Group` | explicit `Q2 2026`, `Q1 2026`, `Q4 2025` target window in packet and ledger | explicit note that AnnualReports lagged at `2024` and that IR plus SEC are authoritative | `qualified` | Strong chain, but the ledger also states that no `Q2 2026` `10-Q` was collected locally, so the most recent quarter is proven at release plus `8-K` level rather than filed-quarterly level |
| `HCA Healthcare` | explicit `Q2 2026`, `Q1 2026`, `Q4 2025` target window in packet and ledger | explicit AnnualReports verification plus official IR and SEC chain | `proven` | Cleanest case in this sample: annual report, quarter releases, `8-K` wrappers, and both in-scope `10-Q` filings are all stated clearly |
| `Sysco` | packet states `Q4 FY26`, `Q3 FY26`, `Q2 FY26`; ledger states the same fiscal window | ledger explicitly says AnnualReports lagged at `2024` and that IR plus SEC are authoritative | `needs repair` | The packet claims the `Q4 FY26` release PDF and `8-K` wrapper are on disk, but the raw SEC directory reviewed in this audit only showed files through `2026-q3-*`; the current-quarter completeness claim is therefore internally inconsistent |
| `MetLife` | explicit `2Q26`, `1Q26`, `4Q25` target window in packet and ledger | explicit note that IR binaries were blocked by Cloudflare and that SEC filings plus verified IR URLs are the authoritative local chain | `qualified` | The chain is still authoritative, but direct local IR artifact capture is missing, so proof depends more heavily on SEC plus verified official URLs |
| `Zebra Technologies` | explicit `Q2 2026`, `Q1 2026`, `Q4 2025` target window in packet and ledger | explicit note that AnnualReports lagged and official IR retrieval hit `429`, so SEC-hosted annual and quarterly artifacts carry the proof | `qualified` | Good evidence chain, but official IR pages were not saved locally and the packet depends on SEC-hosted artifacts plus IR verification notes |
| `Hewlett Packard Enterprise` | packet and profile explicitly define fiscal `2025` annual plus `Q2 FY2026`, `Q1 FY2026`, and `Q4 FY2025` | packet-level narrative says IR routing links and SEC chains were saved | `needs repair` | The source-ledger points to a raw chain under `annual-report-research-new-lanes`, but that path was not verifiable in the same clean way during this audit; unlike the other anchors, the current workspace did not expose a clearly inspectable local evidence chain from the ledger itself |
| `Epson` | explicit `Three Months ended June 30, 2026`, `Fiscal Year ended March 31, 2026`, and `Nine Months ended December 31, 2025` target window in packet and ledger | explicit note that AnnualReports lagged and direct retrieval returned `403`, so browser-captured official extracts were used | `qualified` | The company is still well covered, but proof depends on browser-captured official extracts rather than locally downloaded binaries or SEC-hosted equivalents |

## Exact observations

### 1. `UnitedHealth Group` is better than the old handoff implied, but still not a perfect filed-quarter chain.

What is clearly proven:

- the packet states the correct target window: `Q2 2026`, `Q1 2026`, `Q4 2025`
- the ledger explicitly says AnnualReports lagged at `2024`
- the ledger explicitly says the authoritative `2025` chain comes from IR and SEC

What remains weaker:

- the ledger says no `Q2 2026` `10-Q` was collected locally as of `2026-08-08`

Conclusion:

- the packet is real and usable
- the cleanest phrasing is not "fully filed-quarter complete"
- the cleanest phrasing is "current quarter proven through official release, `8-K`, and prepared remarks, but not local `10-Q` capture"

### 2. `HCA Healthcare` is the best proof-standard model in this thin-lane sample.

What is clearly proven:

- annual report PDF is saved locally
- `2025` `10-K` is saved locally
- `Q4 2025`, `Q1 2026`, and `Q2 2026` releases are named explicitly
- both in-scope `10-Q` filings are named explicitly
- the ledger explicitly states that the annual-plus-quarter chain is clean on disk

Conclusion:

- HCA should be treated as the standard for what "proven" looks like in later cleanup work

### 3. `Sysco` currently has a real internal contradiction.

What is clearly proven:

- the intended fiscal window is correct: `Q4 FY26`, `Q3 FY26`, `Q2 FY26`
- AnnualReports lag was recorded explicitly
- the packet correctly frames Sysco as the enabling infrastructure layer under hospitality and participation demand

What is not clean:

- the ledger says the `Q4 FY26` release PDF is saved locally, but the matching local `8-K` wrapper was not present when the ledger was written
- the packet then says the `Q4 FY26` release PDF and `8-K` wrapper are both on disk
- the raw SEC directory reviewed in this audit only showed:
  - `2025-q4-*`
  - `2026-q1-*`
  - `2026-q2-*`
  - `2026-q3-*`
- no `2026-q4-*` file appeared in the reviewed local raw SEC directory

Conclusion:

- Sysco is directionally strong but not audit-clean
- this packet needs either:
  - correction of the packet language if the `Q4 FY26` wrapper is not actually local
  - or restoration of the missing current-quarter files if they exist elsewhere

### 4. `MetLife` is authoritative enough, but only through a fallback route.

What is clearly proven:

- target window is explicit: `2Q26`, `1Q26`, `4Q25`
- AnnualReports lag at `2024` is explicit
- the ledger and IR-link note explicitly explain the Cloudflare block
- the SEC chain for annual and trailing quarters is locally present

What is weaker:

- no clean local IR PDFs were preserved in this workspace

Conclusion:

- MetLife should count as authoritative but qualified
- the main weakness is capture method, not misunderstanding of the period chain

### 5. `Zebra Technologies` is also authoritative through fallback evidence.

What is clearly proven:

- target window is explicit: `Q2 2026`, `Q1 2026`, `Q4 2025`
- AnnualReports lag at `2024` is explicit
- the ledger says official IR retrieval hit `429`
- SEC-hosted annual and quarter artifacts are explicitly named

What is weaker:

- no locally saved official IR pages
- no standalone earnings-release exhibit or transcript artifact

Conclusion:

- Zebra is a good packet
- it is just not the gold-standard "official IR plus SEC plus local binary" version

### 6. `Hewlett Packard Enterprise` is the weakest proof chain in this audit after Sysco.

What is clearly stated:

- the packet and profile define the correct annual anchor and the latest three reported quarters
- the profile says official IR routing links and SEC chains were saved

What is not currently clean:

- the source-ledger points to a raw chain under `annual-report-research-new-lanes`
- during this audit, that raw path was not exposed in the same clear way as the reviewed chains for HCA, MetLife, or Sysco
- the ledger format is older and less explicit about reconciliation notes, authority hierarchy, and missing evidence than the stronger ledgers in this sample

Conclusion:

- HPE is analytically useful, but the evidence-proof layer should be treated as needing repair before using it as a model completion case

### 7. `Epson` is a valid non-U.S. qualified case, not a broken case.

What is clearly proven:

- the packet and ledger define the correct non-U.S. reporting window
- AnnualReports lag is explicit
- the ledger explains why browser-captured official extracts were used instead of direct binary capture

What is weaker:

- proof depends on browser-captured official extracts
- there is no SEC fallback because this is not the core filing path for this issuer

Conclusion:

- Epson is acceptable as a qualified case
- its weaker point is collection method, not the underlying period logic

## What This Audit Changes

This audit improves the original-goal closeout picture in a more exact way:

- it shows that some supposedly "thin" anchors are actually well-proven
- it shows that the problem is not uniformly missing research
- it isolates the exact cases where closure quality still needs repair

In this sample:

- `proven`: `1`
- `qualified but usable`: `4`
- `needs repair`: `2`

## Exact repair queue from this audit

### Highest priority

1. `Sysco`
   - resolve the `Q4 FY26` current-quarter contradiction between packet text, ledger text, and reviewed raw-file presence
2. `Hewlett Packard Enterprise`
   - rebuild or restate the source-ledger proof chain so the authority hierarchy and local-path evidence are inspectable from the current workspace

### Second priority

3. `UnitedHealth Group`
   - clarify in closeout language that the latest quarter is proven through release plus `8-K` plus prepared remarks, not local `10-Q`
4. `MetLife`
   - keep as qualified unless direct IR binaries are later recoverable
5. `Zebra Technologies`
   - keep as qualified unless official IR HTML or binaries are later recoverable
6. `Epson`
   - keep as qualified unless cleaner local official binaries can be saved later

## Bottom line

The original-goal audit was right to say that proof quality was uneven.

But "uneven" does not mean "mostly absent."

In this thin-lane sample:

- `HCA` is already fully proven
- `UnitedHealth`, `MetLife`, `Zebra`, and `Epson` are real and usable, but qualified
- `Sysco` and `HPE` are the two cases where the evidence-proof layer most clearly still needs repair

That is the actual thin-lane proof state as of `2026-08-11`.
