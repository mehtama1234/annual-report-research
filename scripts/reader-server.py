#!/usr/bin/env python3
"""Serve the editorial reader: python3 scripts/reader-server.py [port].

Requires Python-Markdown. Uses the research files directly, without a build step.
"""
import json
import csv
import math
import re
import sys
import time
from html.parser import HTMLParser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urljoin, urlparse

import markdown

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = {'deep-company-pages': 'Company', 'first-principles': 'Explanation', 'cross-sector': 'Comparison'}
LEGACY_ROOTS = ('/home/manishmehta/ui-projects/annual-report-research-new-lanes/',
                '/home/manishmehta/ui-projects/annual-report-research/')
MANIFEST = ROOT / 'indexes/raw-blob-offload-manifest-2026-08-10.csv'
with MANIFEST.open(newline='') if MANIFEST.exists() else open('/dev/null') as source:
    ARCHIVED = {row['local_path']: row for row in csv.DictReader(source)}

CATALOG_CACHE = None
CATALOG_CACHE_AT = 0.0
# The archive is intentionally read directly from the research checkout. Keep
# the parsed index warm during a reading session; refresh=1 is available after
# editing source files.
CATALOG_CACHE_SECONDS = 300.0

# The archive filenames remain stable, but the visible labels follow the
# reader's plain-language editorial standard. Apply these at serve time so
# existing cross-links and saved paths continue to work.
TREND_LABELS = {
    b'The AI Infrastructure Toll': b'AI infrastructure: who controls the inputs?',
    b'The Gray Wave Dividend': b'Aging and healthcare demand',
    b'The Affordability Ceiling': b'Consumer demand by budget',
    b'The Private Capital Colonization': b'Credit moving outside banks',
    b'The Grid&#x27;s New Landlords': b'Who pays for new power infrastructure?',
    b'The Cash Harvest': b'When mature businesses return cash',
}


class ArticleLinks(HTMLParser):
    """Resolve local references against the document, including filesystem links."""
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.links = {}
        self.external = 0

    def handle_starttag(self, tag, attrs):
        raw = dict(attrs).get('href')
        if tag != 'a' or not raw or raw.startswith('#'):
            return
        url = urlparse(raw)
        if url.scheme or url.netloc:
            if url.scheme in ('http', 'https'):
                self.external += 1
            return
        name = unquote(url.path)
        for legacy in LEGACY_ROOTS:
            if name.startswith(legacy):
                name = '/' + name[len(legacy):]
                break
        prefix = str(ROOT) + '/'
        if name.startswith(prefix):
            target = Path(name).resolve()
        else:
            resolved = urljoin('/' + str(self.path.relative_to(ROOT)), name)
            target = (ROOT / resolved.lstrip('/')).resolve()
        if target.is_relative_to(ROOT) and '.git' not in target.parts:
            self.links[raw] = {'path': str(target.relative_to(ROOT)),
                               'available': target.is_file() or target.is_dir()}
            archived = ARCHIVED.get(str(target.relative_to(ROOT)), {})
            archive_url = archived.get('drive_url', '')
            if urlparse(archive_url).scheme == 'https':
                self.links[raw]['archive_url'] = archive_url
            ledger = target.parent / 'source-ledger.md'
            if not target.exists() and ledger.is_file():
                self.links[raw]['ledger'] = str(ledger.relative_to(ROOT))


def document(path):
    source = path.read_text()
    title = next((line[2:] for line in source.splitlines() if line.startswith('# ')), path.stem)
    title = re.sub(r' (Full Analysis Memo|Full Forensic Analysis Memo|Deep Dossier)$', '', title, flags=re.I)
    date_match = re.search(r'^(Date(?: baseline)?|As of|Reference date|Research date):\s*`?([^`\n]+)', source, re.I | re.M)
    if not date_match:
        date = 'Not stated'
        date_label = 'Date'
    else:
        raw_date = date_match.group(2).strip()
        iso_date = re.match(r'\d{4}-\d{2}-\d{2}', raw_date)
        date = iso_date.group(0) if iso_date else raw_date.split('.')[0].strip()
        matched_label = date_match.group(1).lower()
        date_label = 'Research date' if matched_label == 'research date' else ('As of' if matched_label == 'as of' else 'Reporting period')
    excerpt = ''
    for paragraph in re.split(r'\n\s*\n', source):
        paragraph = paragraph.strip()
        if len(paragraph) < 100 or paragraph.startswith(('#', '|', '-', '* ', '```', 'Date:', 'Source:', 'Companion', '[')):
            continue
        paragraph = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', paragraph)
        paragraph = re.sub(r'[*`]', '', paragraph)
        paragraph = ' '.join(paragraph.split())
        excerpt = paragraph if len(paragraph) <= 400 else paragraph[:400].rsplit(' ', 1)[0] + '…'
        break
    coverage = []
    coverage_rules = [
        ('Business economics', r'(?im)(?:^#{1,4}[^\n]*(?:business|economics|earns|revenue model|operating model|controls|operating baseline|fee compression|underwriting and investment spread|investment question|what .* buying|what (?:the )?company does|control point|where the economics sit|how to read|revenue engines|what (?:this page|the lane) is for|what the lane covers|who captures)|operating chain)'),
        ('Cash conversion', r'(?i)(?:owner cash|cash conversion|operating cash flow|free cash flow|cash flow|cash per share|distributable cash|cash from operations|cash bridge|cash-after-capex|company-only cash|cash settlement)'),
        ('Risks and accounting tests', r'(?im)(?:forensic|earnings quality|accounting risk|financial engineering|shenanigan|what could go wrong|^#{1,4}[^\n]*(?:balance sheet|capital returns|liquidity|risk|thesis breaker))'),
        ('Valuation', r'(?i)valuation|implied equity value|market value'),
        ('What to check next', r'(?i)(?:next filing|watch next|what would change|what to check next|thesis.break|future filing|falsifier|filing-based|open edge)'),
    ]
    for label, pattern in coverage_rules:
        if re.search(pattern, source):
            coverage.append(label)
    return {'path': str(path.relative_to(ROOT)), 'title': title, 'date': date,
            'date_label': date_label,
            'excerpt': excerpt,
            'kind': FOLDERS.get(path.parent.name, 'Research'),
            'minutes': max(1, math.ceil(len(source.split()) / 220)),
            'coverage': coverage}


def catalog():
    """Return the catalog without reparsing every article on every navigation."""
    global CATALOG_CACHE, CATALOG_CACHE_AT
    now = time.monotonic()
    if CATALOG_CACHE is None or now - CATALOG_CACHE_AT >= CATALOG_CACHE_SECONDS:
        CATALOG_CACHE = [document(p) for folder in FOLDERS for p in sorted((ROOT / 'analysis' / folder).glob('*.md'))]
        CATALOG_CACHE_AT = now
    return CATALOG_CACHE


class Reader(SimpleHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path == '/api/catalog':
            if parse_qs(url.query).get('refresh') == ['1']:
                global CATALOG_CACHE, CATALOG_CACHE_AT
                CATALOG_CACHE = None
                CATALOG_CACHE_AT = 0.0
            self.send_json(catalog())
        elif url.path == '/api/article':
            name = parse_qs(url.query).get('file', [''])[0]
            path = (ROOT / name).resolve()
            if not path.is_relative_to(ROOT) or '.git' in path.parts or path.suffix != '.md' or not path.is_file():
                self.send_error(404, 'Article not found')
                return
            result = document(path)
            renderer = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists'])
            result['html'] = renderer.convert(path.read_text())
            result['toc'] = renderer.toc
            links = ArticleLinks(path)
            links.feed(result['html'])
            result['local_links'] = links.links
            result['source_summary'] = {
                'linked': len(links.links),
                'available': sum(1 for link in links.links.values() if link['available']),
                'archived': sum(1 for link in links.links.values() if link.get('archive_url')),
                'recorded_only': sum(1 for link in links.links.values() if not link['available'] and not link.get('archive_url') and link.get('ledger')),
                'external': links.external,
            }
            self.send_json(result)
        elif url.path.startswith('/site/trends/') and url.path.endswith('.html'):
            self.send_trend_page(url)
        else:
            if url.path in ('/', '/site/index.html', '/site/viewer.html'):
                self.path = '/site/reader.html' + (f'?{url.query}' if url.query else '')
            super().do_GET()

    def send_trend_page(self, url):
        """Serve the standalone trend archive with a return path to the reader."""
        path = (ROOT / unquote(url.path.lstrip('/'))).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file() or path.suffix != '.html':
            self.send_error(404, 'Trend page not found')
            return
        body = path.read_bytes()
        for old, new in TREND_LABELS.items():
            body = body.replace(old, new)
        marker = b'class="reader-return"'
        if marker not in body:
            handoff = (b'<p class="reader-return"><a href="/">'
                       b'\xe2\x86\x90 Company &amp; sector research</a></p>')
            wrapped = body.replace(b'<div class="wrap home">', b'<div class="wrap home">' + handoff, 1)
            if wrapped == body:
                wrapped = body.replace(b'<div class="wrap">', b'<div class="wrap">' + handoff, 1)
            body = wrapped
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, data):
        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    # Build the index before accepting browser requests. This makes the first
    # visible page load use the warm cache instead of holding the reader on a
    # loading message while all archive files are parsed.
    catalog()
    print(f'Research reader: http://localhost:{port}/', flush=True)
    ThreadingHTTPServer(('0.0.0.0', port), partial(Reader, directory=str(ROOT))).serve_forever()
