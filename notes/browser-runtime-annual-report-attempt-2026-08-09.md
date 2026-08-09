# Browser Runtime Annual Report Attempt 2026-08-09

Date: 2026-08-09

Purpose:

- Test whether the three remaining annual-report artifact gaps could be closed from this machine using a real local headless browser runtime instead of shell clients.

What was done:

- Installed Python `playwright` locally into the user site.
- Installed Playwright Chromium locally.
- Downloaded and unpacked Debian runtime libraries into `tmp/deb-libs/` and launched Chromium successfully by setting `LD_LIBRARY_PATH` to the local `libnspr4`, `libnss3`, and `libasound2t64` bundles.
- Verified the browser runtime was real and usable by loading `https://example.com` and reading the page title.

Result:

- The browser runtime itself works from this machine.
- The remaining annual-report artifact gaps still failed because of source- or network-level denial behavior, not because no browser path was attempted.

Observed outcomes:

- Caesars official annual report PDF URL:
  - URL: `https://investor.caesars.com/static-files/c3fbec19-0b97-4be1-8d7a-d706c9820559`
  - Result from local Playwright Chromium: HTTP `403`
  - Returned page title: `Access Denied`
  - Returned body started with `You don't have permission to access`
- T. Rowe Price official annual report PDF URL:
  - URL: `https://investors.troweprice.com/static-files/7c2a040a-0872-4017-b25a-52c92b489983`
  - Result from local Playwright Chromium: no download event within `15s`, and follow-up page navigation did not return a usable PDF before manual interruption
  - This is consistent with the earlier shell-client and prior browser-side failure pattern rather than with a missing source URL
- AnnualReports click paths:
  - Clearwater `https://www.annualreports.com/Click/17231`
  - Caesars `https://www.annualreports.com/Click/26971`
  - Result from local Playwright Chromium: `net::ERR_CONNECTION_REFUSED` for both

Interpretation:

- The workspace now has direct evidence that:
  - `annualreports.com` click-through PDF paths are not reachable from this machine even in a real local browser runtime
  - Caesars' current official IR static-file annual report object is edge-denied from this machine even in a real local browser runtime
  - T. Rowe Price's current official IR static-file annual report object still does not deliver a usable binary from this machine even after a full local browser path was created

Practical conclusion:

- The remaining annual-report gaps for Clearwater Paper, T. Rowe Price, and Caesars are now best treated as machine-local retrieval failures with strong reproduced evidence, not as unresolved source-discovery work.
