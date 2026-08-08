# Next Steps

## Immediate pilot

Pick 3 to 5 sectors first, then collect a small but complete company set before scaling.

Collection window for this phase:

- annual reports: `2025`
- quarterlies: latest three reported quarters available as of `2026-08-08`
- in many cases: `2026 Q2`, `2026 Q1`, and `2025 Q4`

Suggested pilot sectors:

1. Technology
2. Financial
3. Consumer Goods
4. Healthcare
5. Industrial Goods

## Collection sequence per company

1. Create company row in `indexes/companies.csv`
2. Create raw folder path by sector / industry / company
3. Save company profile from AnnualReports.com
4. Save the `2025` annual report
5. Save the corresponding `2025` annual filing
6. Save the last three quarterly earnings releases in scope
7. Save the last three quarterly filings in scope
8. Save latest call transcript if available
9. Fill `templates/company-packet.md`
10. Update sector and theme trackers

## Raw folder convention

```text
raw/
  annualreports/<sector>/<industry>/<company>/
  company-ir/<sector>/<industry>/<company>/
  sec/<sector>/<industry>/<company>/
  earnings-calls/<sector>/<industry>/<company>/
```

## Naming convention

- Use lowercase kebab-case for sector, industry, and company folder names.
- Prefix dated files with the reporting period when possible.
- Prefer `2026-q2-earnings-release.pdf` over generic filenames.
