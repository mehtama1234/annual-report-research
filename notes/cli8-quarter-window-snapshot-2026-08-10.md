# CLI 8 Quarter Window Snapshot

Date baseline: 2026-08-10

This note captures the current filing chronology observed from saved SEC submissions JSON and the current AnnualReports.com state for the selected CLI 8 slate.

## Packet Inputs Used

- saved SEC submissions chronology for each selected CLI 8 company
- saved AnnualReports company pages and observed sector or industry labels as of `2026-08-10`
- the repo requirement to preserve exact fiscal labels and filing chronology when quarter windows are non-standard
- the branch need to distinguish taxonomy confirmation from authoritative filing coverage when AnnualReports lags
- the packet-writing requirement that chronology cautions should be documented before company drafting starts

## Filing-window summary

### Ferguson plc / Ferguson Enterprises Inc.

- AnnualReports page saved locally:
  - `raw/annualreports/industrial-goods/general-building-materials/ferguson-plc/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - still shows `2024 Annual Report`
  - sector / industry labels are `Industrial Goods / Industrial Electrical Equipment`
- Current SEC registrant is `Ferguson Enterprises Inc.` under CIK `0002011641`, not the stale insider CIK originally guessed
- Observed current filing chain:
  - `2025-09-26` `10-K` for fiscal year ended `2025-07-31`
  - `2025-12-09` `10-Q` for quarter ended `2025-10-31`
  - `2026-05-05` `10-Q` for quarter ended `2026-03-31`
  - `2026-07-13` `8-K` current update that appears to be the latest reported quarter signal before a later filing pass
- Packet caution:
  - Ferguson changed fiscal-year structure after the 2025 year-end, so quarter labels need to be written carefully and explicitly.

### WESCO International Inc.

- AnnualReports page saved locally:
  - `raw/annualreports/industrial-goods/industrial-equipment-components/wesco-international-inc/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - still shows `2024 Annual Report and Form 10K`
  - sector / industry labels are `Industrial Goods / Industrial Equipment Wholesale`
- Observed current filing chain:
  - `2026-02-13` `10-K` for year ended `2025-12-31`
  - `2026-04-30` `10-Q` for quarter ended `2026-03-31`
  - `2026-07-30` `10-Q` for quarter ended `2026-06-30`
- Target trailing-quarter set:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`

### W.W. Grainger, Inc.

- AnnualReports page saved locally:
  - `raw/annualreports/industrial-goods/industrial-equipment-components/ww-grainger-inc/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - still shows `2024 Annual Report and Form 10K`
  - sector / industry labels are `Industrial Goods / Industrial Equipment Wholesale`
- Observed current filing chain:
  - `2026-02-19` `10-K` for year ended `2025-12-31`
  - `2026-05-07` `10-Q` for quarter ended `2026-03-31`
  - `2026-08-04` `10-Q` for quarter ended `2026-06-30`
- Target trailing-quarter set:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`

### McKesson Corporation

- AnnualReports page saved locally:
  - `raw/annualreports/healthcare/drug-stores/mckesson-corporation/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - still shows `2024 Annual Report and Form 10K`
  - sector / industry labels are `Services / Drugs Wholesale`
- Observed current filing chain:
  - `2025-11-06` `10-Q` for quarter ended `2025-09-30`
  - `2026-02-04` `10-Q` for quarter ended `2025-12-31`
  - `2026-05-08` `10-K` for year ended `2026-03-31`
  - `2026-08-05` `10-Q` for quarter ended `2026-06-30`
- Target trailing-quarter set:
  - `FY2027 Q1`
  - `FY2026 Q4`
  - `FY2026 Q3`

### Cencora, Inc.

- AnnualReports page saved locally:
  - `raw/annualreports/healthcare/drug-stores/cencora-inc/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - older-report view still tops out at `2024`
  - sector / industry labels are `Healthcare / Drug Delivery`
- Observed current filing chain:
  - `2026-02-04` `10-Q` for quarter ended `2025-12-31`
  - `2026-05-06` `10-Q` for quarter ended `2026-03-31`
  - `2026-08-05` `10-Q` for quarter ended `2026-06-30`
- Target trailing-quarter set:
  - `FY2026 Q3`
  - `FY2026 Q2`
  - `FY2026 Q1`

### Sysco Corporation

- AnnualReports page saved locally:
  - `raw/annualreports/services/retail-grocery-stores/sysco-corp/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - page still emphasizes older archived reports and lags the current annual chain
  - sector / industry labels are `Consumer Goods / Food Wholesale`
- Observed current filing chain:
  - `2025-10-29` `10-Q` for quarter ended `2025-09-27`
  - `2026-01-28` `10-Q` for quarter ended `2025-12-27`
  - `2026-04-29` `10-Q` for quarter ended `2026-03-28`
  - `2026-08-04` `8-K` for the latest reported quarter
- Target trailing-quarter set:
  - `FY2026 Q4`
  - `FY2026 Q3`
  - `FY2026 Q2`
- Packet caution:
  - the latest quarter appears through earnings-release timing before the annual filing is locally collected, so the annual-plus-quarter chain needs special care.

### United Rentals, Inc.

- AnnualReports page saved locally:
  - `raw/annualreports/industrial-goods/business-services/united-rentals-inc/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - still shows `2024 Annual Report and Form 10K`
  - sector / industry labels are `Industrial Goods / Rental & Leasing Services`
- Observed current filing chain:
  - `2026-01-28` `10-K` for year ended `2025-12-31`
  - `2026-04-22` `10-Q` for quarter ended `2026-03-31`
  - `2026-07-22` `10-Q` for quarter ended `2026-06-30`
- Target trailing-quarter set:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`

### Hyatt Hotels Corporation

- AnnualReports page saved locally:
  - `raw/annualreports/services/lodging/hyatt-hotels-corporation/company-page.html`
- AnnualReports state as of `2026-08-10`:
  - still shows `2024 Annual Report and Form 10K`
  - sector / industry labels are `Consumer Goods / Lodging`
- Observed current filing chain:
  - `2026-02-13` `10-K` for year ended `2025-12-31`
  - `2026-04-30` `10-Q` for quarter ended `2026-03-31`
  - `2026-07-30` `10-Q` for quarter ended `2026-06-30`
- Target trailing-quarter set:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`

## Cross-cutting observations

- AnnualReports lag is real across most of this frontier and should be written up as part of the handoff.
- The archive should preserve odd AnnualReports labels when they appear, because they reveal taxonomy mismatch:
- Ferguson as `Industrial Electrical Equipment`
- Cencora as `Drug Delivery`
- Hyatt as `Consumer Goods / Lodging`
- The branch already has enough evidence to start packet drafting from saved AnnualReports pages plus saved SEC chronology, even before all annual and quarterly filing bodies are downloaded.

## Skeptical Reader Test

- Does this note preserve the exact filing-window evidence needed to keep quarter labels honest for each CLI 8 company?
- Can a skeptical reader tell when AnnualReports is being used for taxonomy only and when SEC chronology is carrying the authoritative date chain?
- Does the note surface the unusual taxonomy labels and fiscal-structure issues that could distort later packet drafting?
- What missing chronology detail would weaken confidence in the target trailing-quarter set for a company?
