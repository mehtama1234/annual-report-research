# Shopify Inc. SEC Source Links

Verification date: 2026-08-10

## Authoritative filing URLs used for verification

- SEC filing chain landing reference: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1594805&type=&dateb=&owner=exclude&count=40`
- Form 10-K for year ended `2025-12-31`: `https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm`
- Q1 2026 10-Q HTML: `https://shopifyinvestors.gcs-web.com/node/12536/html`
- Q2 2026 10-Q HTML: `https://shopifyinvestors.gcs-web.com/node/12611/html`

## Shell collection limitation

- Direct shell fetches to SEC endpoints from this environment on `2026-08-10` returned the SEC automated-tool block page rather than the filing content
- Because of that limitation, the packet relies on:
  - the verified SEC filing URLs above,
  - the company-hosted `10-Q` PDFs collected locally,
  - the official company IR results pages and press-release PDFs,
  - and the SEC `10-K` content verified through browser access during the run

## Practical implication

- This folder preserves the authoritative SEC URL chain and the access limitation rather than storing misleading block-page artifacts
