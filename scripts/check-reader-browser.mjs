// Exercise the running reader in Chromium without external browser libraries.
// CHROME_BIN=/path/to/chrome node scripts/check-reader-browser.mjs
import {spawn} from 'node:child_process';
import {mkdtemp, writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createServer} from 'node:net';
const profile=await mkdtemp(join(tmpdir(),'research-reader-browser-'));
const port=await new Promise((resolve,reject)=>{const s=createServer();s.once('error',reject);s.listen(0,'127.0.0.1',()=>{const p=s.address().port;s.close(()=>resolve(p));});});
const browser=spawn(process.env.CHROME_BIN||'/home/mehtama1/.cache/ms-playwright/chromium-1140/chrome-linux/chrome',[
  '--headless','--no-sandbox','--disable-gpu',`--remote-debugging-port=${port}`,`--user-data-dir=${profile}`,'about:blank'
],{stdio:['ignore','ignore','pipe']});
let socket;
let completed=false;
try{
  const endpoint=await (async()=>{const deadline=Date.now()+20000;while(Date.now()<deadline){try{const version=await(await fetch(`http://127.0.0.1:${port}/json/version`)).json();if(version.webSocketDebuggerUrl)return version.webSocketDebuggerUrl;}catch{}await new Promise(r=>setTimeout(r,100));}throw Error('Browser startup timed out');})();
  const url=new URL(endpoint);const targets=await(await fetch(`http://${url.host}/json`)).json();
  socket=new WebSocket(targets.find(t=>t.type==='page').webSocketDebuggerUrl);
  await new Promise((r,j)=>{socket.onopen=r;socket.onerror=j;});
  let id=0;const pending=new Map();
  socket.onmessage=e=>{const m=JSON.parse(e.data);if(pending.has(m.id)){const {resolve,reject,timer}=pending.get(m.id);clearTimeout(timer);pending.delete(m.id);m.error?reject(Error(m.error.message)):resolve(m.result);}};
  const send=(method,params={},timeout=20000)=>new Promise((resolve,reject)=>{const key=++id;const timer=setTimeout(()=>{pending.delete(key);reject(Error(method+' timed out'));},timeout);pending.set(key,{resolve,reject,timer});socket.send(JSON.stringify({id:key,method,params}));});
  const capture=async name=>{try{const shot=await send('Page.captureScreenshot',{format:'png'},5000);await writeFile(join(profile,name+'.png'),Buffer.from(shot.data,'base64'));}catch(error){console.log('Screenshot skipped: '+name+' ('+error.message+')');}};
  const evaluate=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
  async function open(path,width,height){
    await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:width<500});
    await send('Page.navigate',{url:'http://localhost:8765/'+path});
    const articleRoute=path.includes('?file=');
    // The first catalog build reads the complete archive. Allow that cold
    // start, while keeping the subsequent readiness poll fast.
    for(let i=0;i<300;i++){
      const ready=articleRoute
        ? await evaluate("location.search.includes('file=') && !!document.querySelector('.reading article h1') && !!document.querySelector('.article-meta')")
        : await evaluate("!location.search.includes('file=') && !!document.querySelector('#results') && !!document.querySelector('.library-stats')");
      if(ready)break;
      await new Promise(r=>setTimeout(r,100));
    }
    const loaded=articleRoute
      ? await evaluate("location.search.includes('file=') && !!document.querySelector('.reading article h1') && !!document.querySelector('.article-meta')")
      : await evaluate("!location.search.includes('file=') && !!document.querySelector('#results') && !!document.querySelector('.library-stats')");
    if(!loaded)throw Error('Reader did not load: '+path);
    if(await evaluate("!!document.querySelector('.error')"))throw Error('Reader error');
    await new Promise(r=>setTimeout(r,150));
    const layout=await evaluate('({viewport:innerWidth,width:document.documentElement.scrollWidth,title:document.title})');
    if(layout.width>layout.viewport+1)throw Error('Horizontal overflow: '+JSON.stringify(layout));
    return layout;
  }
  for(const [name,path,width,height]of [
    ['desktop','',1440,1000],['mobile','',390,844],
    ['article','?file=analysis/first-principles/restaurant-occasion-franchisee-health-and-owner-cash.md',390,844],
    ['comparison','?file=analysis/cross-sector/ai-physical-capacity-to-owner-cash-forensic-synthesis-2026-09-14.md',390,844]
  ]){
    const layout=await open(path,width,height);
    await capture(name);
    console.log(name,JSON.stringify(layout));
  }
  await open('site/viewer.html?file=analysis/deep-company-pages/the-cigna-group.md',390,844);
  const legacyArticle=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',route:location.pathname+location.search})`);
  if(!legacyArticle.title.includes('The Cigna Group')||!legacyArticle.route.includes('/site/viewer.html?file='))throw Error('Legacy viewer query handoff failed: '+JSON.stringify(legacyArticle));
  console.log('Legacy viewer query handoff passed.');
  const articleLanguage=await evaluate(`({status:document.querySelector('.source-status')?.textContent||'',coverage:document.querySelector('.coverage-status')?.textContent||'',terms:document.querySelector('.term-note a')?.getAttribute('href')||'',definitions:!!document.querySelector('#financial-terms'),readingPath:document.querySelector('.article-reading-path')?.textContent||'',sourceLink:document.querySelector('.reading a')?.textContent||'',sourceLabel:document.querySelector('.source-status a')?.getAttribute('aria-label')||'',relatedCompanyLinks:document.querySelectorAll('.related a[href*="deep-company-pages"]').length})`);
  if(!articleLanguage.status.includes('Where the evidence comes from')||articleLanguage.status.includes('local references'))throw Error('Reader-facing evidence language failed: '+JSON.stringify(articleLanguage));
  if(!articleLanguage.coverage.includes('Questions this page addresses'))throw Error('Coverage summary failed: '+JSON.stringify(articleLanguage));
  if(!articleLanguage.sourceLabel.startsWith('Open source file for '))throw Error('Source link accessibility label failed: '+JSON.stringify(articleLanguage));
  if(articleLanguage.terms!=='#financial-terms'||!articleLanguage.definitions)throw Error('Definitions handoff failed: '+JSON.stringify(articleLanguage));
  if(!articleLanguage.readingPath.includes('Read the claim')||!articleLanguage.readingPath.includes('future filing'))throw Error('Article reading path failed: '+JSON.stringify(articleLanguage));
  await evaluate(`document.querySelector('.term-note a').click()`);
  if(!(await evaluate(`document.querySelector('#financial-terms').open`)))throw Error('Definitions did not open from handoff link');
  if(articleLanguage.relatedCompanyLinks<5)throw Error('Comparison article handoff failed: '+JSON.stringify(articleLanguage));
  await open('?file=analysis/cross-sector/financial-intermediation-to-owner-cash-forensic-synthesis-2026-09-14.md#alternative-capital-comparison-fee-platform-insurance-spread-and-carry',390,844);
  const privateCapitalAnchor=await evaluate(`(()=>{const h=document.querySelector('#alternative-capital-comparison-fee-platform-insurance-spread-and-carry');return {hash:location.hash,title:h?.textContent||'',top:h?.getBoundingClientRect().top||null}})()`);
  if(!privateCapitalAnchor.hash.includes('alternative-capital-comparison')||!privateCapitalAnchor.title.includes('Alternative-capital comparison')||privateCapitalAnchor.top===null||privateCapitalAnchor.top>120)throw Error('Private-capital comparison anchor failed: '+JSON.stringify(privateCapitalAnchor));
  console.log('Private-capital comparison anchor passed.');
  await open('?file=analysis/cross-sector/regulated-wires-versus-large-load-forensic-comparison-2026-09-14.md#3-demand-visibility-versus-recovery-visibility',390,844);
  const energyAnchor=await evaluate(`(()=>{const h=document.getElementById('3-demand-visibility-versus-recovery-visibility');return {hash:location.hash,title:h?.textContent||'',top:h?.getBoundingClientRect().top||null}})()`);
  if(!energyAnchor.hash.includes('3-demand-visibility-versus-recovery-visibility')||!energyAnchor.title.includes('Demand visibility versus recovery visibility')||energyAnchor.top===null||energyAnchor.top>120)throw Error('Energy comparison anchor failed: '+JSON.stringify(energyAnchor));
  console.log('Energy comparison anchor passed.');
  await open('?file=analysis/cross-sector/power-demand-to-owner-cash-forensic-synthesis-2026-09-13.md',390,844);
  const powerBridge=await evaluate(`(()=>{const h=[...document.querySelectorAll('.reading article h2')].find(x=>x.textContent.includes('Initial comparable filing bridge'));const children=h?[...h.parentElement.children]:[];const wrap=h?children.slice(children.indexOf(h)+1).find(x=>x.querySelector?.('table')):null;const table=wrap?.querySelector('table');return {heading:!!h,rows:table?.querySelectorAll('tbody tr').length||0,companyLinks:table?.querySelectorAll('a[href*="deep-company-pages"]').length||0,language:document.querySelector('.reading article')?.textContent.includes('not a ranking')||false}})()`);
  if(!powerBridge.heading||powerBridge.rows<8||powerBridge.companyLinks<8||!powerBridge.language)throw Error('Power-demand filing bridge failed: '+JSON.stringify(powerBridge));
  console.log('Power-demand filing bridge passed.');
  await open('?file=analysis/deep-company-pages/brookdale-senior-living-inc.md',390,844);
  const researchDate=await evaluate(`({label:document.querySelector('.article-facts p:last-child .label')?.textContent||'',value:document.querySelector('.article-facts p:last-child strong')?.textContent||''})`);
  if(researchDate.label!=='Research date'||researchDate.value!=='2026-09-14')throw Error('Research-date label failed: '+JSON.stringify(researchDate));
  await open('?file=analysis/deep-company-pages/asml-holding-nv.md',390,844);
  const externalOnly=await evaluate(`({status:document.querySelector('.source-status')?.textContent||'',sourceLinks:[...document.querySelectorAll('.reading article a[href^="http"]')].length})`);
  if(!externalOnly.status.includes('external filing')||!externalOnly.status.includes('not stored in this checkout')||externalOnly.sourceLinks<3)throw Error('External-only source boundary failed: '+JSON.stringify(externalOnly));
  console.log('External-only source boundary passed.');
  await open('?file=analysis/deep-company-pages/ge-vernova-inc.md',390,844);
  const geExternalOnly=await evaluate(`({status:document.querySelector('.source-status')?.textContent||'',sourceLinks:[...document.querySelectorAll('.reading article a[href^="http"]')].length})`);
  if(!geExternalOnly.status.includes('external filing')||!geExternalOnly.status.includes('not stored in this checkout')||geExternalOnly.sourceLinks<4)throw Error('GE Vernova external-only source boundary failed: '+JSON.stringify(geExternalOnly));
  console.log('GE Vernova external-only source boundary passed.');
  await open('?file=analysis/deep-company-pages/the-cigna-group.md',390,844);
  const cignaComparison=await evaluate(`(()=>{const link=[...document.querySelectorAll('.reading article a')].find(a=>a.textContent.includes('UnitedHealth Group comparative dossier'));const article=document.querySelector('.reading article')?.textContent||'';return {href:link?.getAttribute('href')||'',text:link?.textContent||'',article}})()`);
  if(!cignaComparison.text||!cignaComparison.href.includes('unitedhealth-group-inc.md')||!cignaComparison.article.includes('shareholder cash')||cignaComparison.article.includes('common-owner cash'))throw Error('Cigna comparative dossier or language handoff failed: '+JSON.stringify(cignaComparison));
  console.log('Cigna comparative dossier link passed.');
  await open('?file=analysis/deep-company-pages/unitedhealth-group-inc.md',390,844);
  const unitedhealthDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.reading article a').length})`);
  if(!unitedhealthDossier.title.includes('UnitedHealth')||!unitedhealthDossier.article.includes('medical costs')||!unitedhealthDossier.article.includes('Optum')||!unitedhealthDossier.article.includes('Damodaran')||!unitedhealthDossier.article.includes('Lyn Alden')||unitedhealthDossier.sourceLinks<1)throw Error('UnitedHealth dossier handoff failed: '+JSON.stringify(unitedhealthDossier));
  console.log('UnitedHealth dossier passed.');
  await open('?file=analysis/deep-company-pages/williams-sonoma-inc.md',390,844);
  const williamsDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.source-status a').length})`);
  if(!williamsDossier.title.includes('Williams-Sonoma')||!williamsDossier.article.includes('inventory')||!williamsDossier.article.includes('Damodaran')||!williamsDossier.article.includes('Lyn Alden')||williamsDossier.sourceLinks<1)throw Error('Williams-Sonoma dossier handoff failed: '+JSON.stringify(williamsDossier));
  console.log('Williams-Sonoma dossier passed.');
  await open('?file=analysis/deep-company-pages/doubleverify-holdings-inc.md',390,844);
  const doubleverifyDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.source-status a').length})`);
  if(!doubleverifyDossier.title.includes('DoubleVerify')||!doubleverifyDossier.article.includes('merger')||!doubleverifyDossier.article.includes('Damodaran')||!doubleverifyDossier.article.includes('Lyn Alden')||doubleverifyDossier.sourceLinks<1)throw Error('DoubleVerify dossier handoff failed: '+JSON.stringify(doubleverifyDossier));
  console.log('DoubleVerify dossier passed.');
  await open('?file=analysis/deep-company-pages/aptar-group-inc.md',390,844);
  const aptarDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.source-status a').length})`);
  if(!aptarDossier.title.includes('AptarGroup')||!aptarDossier.article.includes('Pharma')||!aptarDossier.article.includes('Damodaran')||!aptarDossier.article.includes('Lyn Alden')||aptarDossier.sourceLinks<1)throw Error('AptarGroup dossier handoff failed: '+JSON.stringify(aptarDossier));
  console.log('AptarGroup dossier passed.');
  await open('?file=analysis/deep-company-pages/campbell-soup-company.md',390,844);
  const campbellDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.source-status a').length})`);
  if(!campbellDossier.title.includes("Campbell's")||!campbellDossier.article.includes('Meals & Beverages')||!campbellDossier.article.includes('Damodaran')||!campbellDossier.article.includes('Lyn Alden')||campbellDossier.sourceLinks<1)throw Error('Campbell dossier handoff failed: '+JSON.stringify(campbellDossier));
  console.log('Campbell dossier passed.');
  await open('?file=analysis/deep-company-pages/colgate-palmolive-co.md',390,844);
  const colgateDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.source-status a').length})`);
  if(!colgateDossier.title.includes('Colgate-Palmolive')||!colgateDossier.article.includes('Hill')||!colgateDossier.article.includes('Damodaran')||!colgateDossier.article.includes('Lyn Alden')||colgateDossier.sourceLinks<1)throw Error('Colgate-Palmolive dossier handoff failed: '+JSON.stringify(colgateDossier));
  console.log('Colgate-Palmolive dossier passed.');
  await open('?file=analysis/deep-company-pages/the-tjx-companies-inc.md',390,844);
  const tjxDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.source-status a').length})`);
  if(!tjxDossier.title.includes('TJX')||!tjxDossier.article.includes('inventory')||!tjxDossier.article.includes('Damodaran')||!tjxDossier.article.includes('Lyn Alden')||tjxDossier.sourceLinks<1)throw Error('TJX dossier handoff failed: '+JSON.stringify(tjxDossier));
  console.log('TJX dossier passed.');
  await open('?file=analysis/cross-sector/off-price-value-discovery-and-retail-cash-comparison-2026-09-15.md',390,844);
  const tjxComparison=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',companyLink:[...document.querySelectorAll('.reading article a')].find(a=>a.textContent.includes('TJX deep company dossier'))?.getAttribute('href')||'',targetLink:[...document.querySelectorAll('.reading article a')].find(a=>a.textContent.includes('Target deep company dossier'))?.getAttribute('href')||'',walmartLink:[...document.querySelectorAll('.reading article a')].find(a=>a.textContent.includes('Walmart deep company dossier'))?.getAttribute('href')||''})`);
  if(!tjxComparison.title.includes('Retail formats')||!tjxComparison.article.includes('Target')||!tjxComparison.article.includes('Walmart')||!tjxComparison.companyLink.includes('the-tjx-companies-inc.md')||!tjxComparison.targetLink.includes('target-corporation.md')||!tjxComparison.walmartLink.includes('walmart-inc.md'))throw Error('Retail comparison handoff failed: '+JSON.stringify(tjxComparison));
  console.log('TJX comparison handoff passed.');
  await open('?file=analysis/deep-company-pages/astrana-health-inc.md',390,844);
  const astranaDossier=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||'',sourceLinks:document.querySelectorAll('.source-status a').length})`);
  if(!astranaDossier.title.includes('Astrana')||!astranaDossier.article.includes('delegated-risk')||!astranaDossier.article.includes('Damodaran')||!astranaDossier.article.includes('Lyn Alden')||astranaDossier.sourceLinks<1)throw Error('Astrana dossier handoff failed: '+JSON.stringify(astranaDossier));
  console.log('Astrana dossier passed.');
  await open('?file=analysis/cross-sector/healthcare-middle-layer-provider-network-and-product-flow-comparison-2026-09-15.md',390,844);
  const astranaComparison=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',companyLink:[...document.querySelectorAll('.reading article a')].find(a=>a.textContent.includes('Astrana deep company dossier'))?.getAttribute('href')||''})`);
  if(!astranaComparison.title.includes('Healthcare middle layers')||!astranaComparison.companyLink.includes('astrana-health-inc.md'))throw Error('Astrana comparison handoff failed: '+JSON.stringify(astranaComparison));
  console.log('Astrana comparison handoff passed.');
  await open('',1440,1000);
  const methodLink=await evaluate(`({text:document.querySelector('.method-link a')?.textContent||'',href:document.querySelector('.method-link a')?.getAttribute('href')||''})`);
  if(!methodLink.text.includes('How to read the research')||!methodLink.href.includes('combined-end-to-end-forensic-research-system-2026-09-13.md'))throw Error('Research-method handoff failed: '+JSON.stringify(methodLink));
  await open('?file=analysis/cross-sector/combined-end-to-end-forensic-research-system-2026-09-13.md',390,844);
  const methodArticle=await evaluate(`({title:document.querySelector('.reading article h1')?.textContent||'',article:document.querySelector('.reading article')?.textContent||''})`);
  if(!methodArticle.title||!methodArticle.article.includes('cash conversion')||!methodArticle.article.includes('future filing'))throw Error('Research-method article failed: '+JSON.stringify(methodArticle));
  console.log('Research-method handoff passed.');
  await open('',1440,1000);
  const integratedReview=await evaluate(`(()=>{const section=document.querySelector('#investment-research');const hrefs=[...section?.querySelectorAll('a')||[]].map(a=>a.getAttribute('href')||'');const method=document.querySelector('.method-brief')?.textContent||'';return {heading:section?.querySelector('h2')?.textContent||'',cards:section?.querySelectorAll('.investment-research-grid article').length||0,gateCount:method.includes('226 checked evidence gates'),required:['combined-investment-research-current-synthesis.md','combined-investment-research-pilot-01-wheaton-antamina.md','combined-investment-research-pilot-02-affordability-value.md','combined-investment-research-pilot-03-apollo-athene.md','combined-investment-research-completion-audit.md','combined-investment-research-deliverable-audit.md','combined-investment-research-reviewers-guide.md','combined-investment-research-cross-sector-comparison-2026-09-16.md','capital-flow-apollo-athene-q2-parent-receipt-refresh-2026-09-16.md','combined-investment-research-pilot-02-retail-capex-public-source-refresh-2026-09-16.md','combined-investment-research-pilot-02-retail-attached-services-public-source-refresh-2026-09-16.md','combined-investment-research-force-to-company-atlas-2026-09-15.md','combined-investment-research-pilot-02-target-q2-management-call-control-point-upgrade-2026-09-15.md','capital-flow-apollo-athene-fee-rollforward-boundary-2026-09-15.md','capital-flow-apollo-athene-ari-q2-seller-cash-debt-waterfall-upgrade-2026-09-15.md','capital-flow-apollo-athene-ari-q2-cash-flow-reconciliation-2026-09-15.md','capital-flow-apollo-q2-xbrl-parent-receipt-boundary-2026-09-15.md','capital-flow-apollo-athene-q2-adip-related-party-flow-upgrade-2026-09-15.md','capital-flow-apollo-athene-q2-policyholder-liquidity-repo-burden-boundary-2026-09-15.md','capital-flow-apollo-q2-fund-distributions-to-company-boundary-2026-09-15.md','combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.md','combined-investment-research-pilot-02-tjx-forward-capex-category-boundary-2026-09-15.md','capital-flow-apollo-athene-intercompany-note-balance-movement-boundary-2026-09-15.md','capital-flow-wheaton-antamina-bhp-fy2026-annual-report-boundary-2026-09-16.md','capital-flow-wheaton-antamina-investor-day-forward-profile-boundary-2026-09-16.md','capital-flow-wheaton-antamina-dual-pmpa-threshold-reconciliation-2026-09-16.md','capital-flow-apollo-athene-broadcom-anthropic-whco-guarantee-boundary-2026-09-16.md','capital-flow-apollo-broadcom-capital-solutions-fee-timing-boundary-2026-09-16.md','capital-flow-apollo-athene-ari-closing-payment-mechanics-boundary-2026-09-16.md','capital-flow-apollo-athene-ari-post-close-proof-search-boundary-2026-09-16.md','capital-flow-apollo-athene-ari-cash-perimeter-delta-boundary-2026-09-16.md','combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.md','combined-investment-research-through-cycle-retail-panel-diagnostic-2026-09-16.md','combined-investment-research-through-cycle-retail-within-company-diagnostic-2026-09-16.md','combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.md'].every(name=>hrefs.some(href=>href.includes(name)))}})()`);
  if(!integratedReview.heading.includes('Integrated investment research')||integratedReview.cards<6||!integratedReview.gateCount||!integratedReview.required)throw Error('Integrated investment-research review path failed: '+JSON.stringify(integratedReview));
  const latestReviewDocs=await evaluate(`(()=>[...document.querySelector('#investment-research .investment-research-footer')?.querySelectorAll('a')||[]].map(a=>a.getAttribute('href')||'').filter(href=>href.includes('combined-investment-research-thesis-breaker-register.md')||href.includes('combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md')||href.includes('capital-flow-apollo-athene-concord-public-document-acquisition-attempt-pass-1.md')||href.includes('capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.md')||href.includes('capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.md')||href.includes('capital-flow-apollo-athene-corporate-structure-presentation-boundary-2026-09-16.md')||href.includes('capital-flow-retail-owner-cash-input-schema-2026-09-16.md')).length)()`);
  if(latestReviewDocs!==7)throw Error('Latest investment-research review documents handoff failed: '+latestReviewDocs);
  console.log('Latest investment-research review documents handoff passed.');
  const ariAumLink=await evaluate(`(()=>[...document.querySelector('#investment-research')?.querySelectorAll('a')||[]].some(a=>(a.getAttribute('href')||'').includes('capital-flow-apollo-athene-ari-aum-outflow-boundary-2026-09-16.md')))()`);
  if(!ariAumLink)throw Error('ARI AUM outflow reader handoff failed.');
  console.log('ARI AUM outflow reader handoff passed.');
  console.log('Integrated investment-research review path passed.');
  await open('',1440,1000);
  const comparisonHandoff=await evaluate(`(()=>{const order=['#themes','#comparisons','#watchlist','#library'].map(s=>document.querySelector(s)?.getBoundingClientRect().top||-1);return {section:!!document.querySelector('#comparisons'),cohorts:document.querySelectorAll('.cohort').length,companyLinks:document.querySelectorAll('.cohort a[href*="deep-company-pages"]').length,filters:document.querySelectorAll('.cohort-filters button').length,watchlist:document.querySelectorAll('#watchlist article').length,watchLinks:document.querySelectorAll('#watchlist a').length,legend:!!document.querySelector('.coverage-legend'),stats:document.querySelector('.library-stats')?.textContent||'',findingLink:document.querySelector('.library-stats a[href="#findings-heading"]')?.textContent||'',findingTitles:[...document.querySelectorAll('.findings-grid h3')].map(x=>x.textContent).join(' | '),states:document.querySelectorAll('#research-state article').length,industrialState:document.querySelector('#research-state a[href*="backlog-visibility-to-cash-realization"]')?.textContent||'',industrialTheme:document.querySelector('.theme h2')&&[...document.querySelectorAll('.theme h2')].find(x=>x.textContent.includes('Infrastructure, backlog'))?.textContent||'',industrialThemeLinks:['fastenal-company','ww-grainger-inc','ferguson-enterprises-inc','core-main-inc','avnet-inc','sysco-corp','us-foods-holding-corp','mastec-inc'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean),softwareState:document.querySelector('#research-state a[href*="software-control-and-ai-capital-conversion"]')?.textContent||'',softwareTheme:document.querySelector('.theme h2')&&[...document.querySelectorAll('.theme h2')].find(x=>x.textContent.includes('Software, data'))?.textContent||'',aiThemeLinks:['micron-technology-inc','marvell-technology-inc','intel-corporation','broadcom-inc','cisco-systems-inc','dell-technologies-inc'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean),securityThemeLinks:['crowdstrike-holdings-inc','palo-alto-networks-inc','zscaler-inc','f5-inc'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean),paymentThemeLinks:['affirm-holdings-inc','uber-technologies-inc','doordash-inc','booking-holdings-inc','wayfair-inc'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean),financialThemeLinks:['blackstone-inc','kkr-co-inc','ares-management-corporation','blackrock-inc','state-street-corp'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean),healthcareThemeLinks:['the-cigna-group','hca-healthcare-inc','davita-inc','cencora-inc','addus-homecare-corporation','adapthealth-corp'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean),intelKlaCard:!!document.querySelector('.cohort a[href*="intel-versus-kla"]'),valuationBoundary:document.querySelector('.valuation-boundary')?.textContent||'',valuationCards:document.querySelectorAll('.valuation-boundary-grid article').length,energyStateLink:document.querySelector('#research-state a[href*="power-demand-to-owner-cash"]')?.textContent||'',powerDemandCard:document.querySelector('.cohort a[href*="power-demand-to-owner-cash"]')?.textContent||'',order}})()`);
  if(!comparisonHandoff.stats.includes('236 company studies'))throw Error('Homepage catalog count is stale: '+comparisonHandoff.stats);
  if(!comparisonHandoff.section||comparisonHandoff.cohorts<1||comparisonHandoff.companyLinks<5||comparisonHandoff.filters<4||comparisonHandoff.watchlist<4||comparisonHandoff.watchLinks<4||!comparisonHandoff.legend||!comparisonHandoff.stats.includes('140 comparisons')||comparisonHandoff.findingLink!=='Read five findings'||!comparisonHandoff.findingTitles.includes('AI backlog')||!comparisonHandoff.findingTitles.includes('Recurring security')||!comparisonHandoff.findingTitles.includes('Strategic manufacturing')||!comparisonHandoff.findingTitles.includes('Payer scale')||!comparisonHandoff.findingTitles.includes('Three retail formats')||comparisonHandoff.states<7||comparisonHandoff.industrialState!=='Industrial capacity and backlog'||comparisonHandoff.industrialTheme!=='Infrastructure, backlog & field execution'||!comparisonHandoff.industrialThemeLinks||comparisonHandoff.softwareState!=='Software and workflow control'||comparisonHandoff.softwareTheme!=='Software, data & recurring workflows'||!comparisonHandoff.aiThemeLinks||!comparisonHandoff.securityThemeLinks||!comparisonHandoff.paymentThemeLinks||!comparisonHandoff.financialThemeLinks||!comparisonHandoff.healthcareThemeLinks||!comparisonHandoff.intelKlaCard||comparisonHandoff.valuationCards!==3||!comparisonHandoff.valuationBoundary.includes('224 source-linked rows')||!comparisonHandoff.valuationBoundary.includes('payers')||!comparisonHandoff.valuationBoundary.includes('Not a price target')||comparisonHandoff.energyStateLink!=='Energy and infrastructure'||comparisonHandoff.powerDemandCard!=='Power demand: recovery, control points and execution'||comparisonHandoff.order.some((v,i,a)=>v<0||(i&&v<=a[i-1])))throw Error('Homepage comparison handoff failed: '+JSON.stringify(comparisonHandoff));
  comparisonHandoff.stats=comparisonHandoff.stats.replace('236 company studies','231 company studies');
  const staplesHandoff=await evaluate(`({company:!!document.querySelector('.theme a[href*="general-mills-inc"]'),comparison:!!document.querySelector('.theme a[href*="affordability-engineering-and-value-reinvestment-comparison-2026-08-11.md"]')})`);
  if(!staplesHandoff.company||!staplesHandoff.comparison)throw Error('General Mills editorial handoff failed: '+JSON.stringify(staplesHandoff));
  console.log('General Mills editorial handoff passed.');
  const campbellHandoff=await evaluate(`({company:!!document.querySelector('.theme a[href*="campbell-soup-company"]'),text:document.querySelector('.theme a[href*="campbell-soup-company"]')?.textContent||''})`);
  if(!campbellHandoff.company||campbellHandoff.text!=="Campbell's")throw Error('Campbell editorial handoff failed: '+JSON.stringify(campbellHandoff));
  console.log('Campbell editorial handoff passed.');
  const colgateHandoff=await evaluate(`({company:!!document.querySelector('.theme a[href*="colgate-palmolive-co"]'),text:document.querySelector('.theme a[href*="colgate-palmolive-co"]')?.textContent||''})`);
  if(!colgateHandoff.company||colgateHandoff.text!=='Colgate-Palmolive')throw Error('Colgate editorial handoff failed: '+JSON.stringify(colgateHandoff));
  console.log('Colgate editorial handoff passed.');
  const plainTrendTitles=await evaluate(`(()=>[...document.querySelectorAll('.trend-bridge strong')].map(x=>x.textContent))()`);
  if(plainTrendTitles.some(x=>/Gray Wave|Cash Harvest|New Landlords|Private Capital Colonization|AI Infrastructure Toll/.test(x))||!plainTrendTitles.includes('Aging and healthcare demand')||!plainTrendTitles.includes('Credit moving outside banks'))throw Error('Homepage trend labels are not plain-language: '+JSON.stringify(plainTrendTitles));
  await evaluate(`document.querySelector('[data-cohort-lane="Healthcare and aging"]').click()`);
  const healthcareFilter=await evaluate(`({pressed:document.querySelector('[data-cohort-lane="Healthcare and aging"]').getAttribute('aria-pressed'),shown:[...document.querySelectorAll('.cohort')].filter(x=>!x.hidden).length,health:[...document.querySelectorAll('.cohort')].filter(x=>!x.hidden&&x.dataset.cohortLane==='Healthcare and aging').length})`);
  if(healthcareFilter.pressed!=='true'||healthcareFilter.shown!==healthcareFilter.health||!healthcareFilter.health||!(await evaluate(`location.search.includes('lane=Healthcare+and+aging')`)))throw Error('Comparison lane filter failed: '+JSON.stringify(healthcareFilter));
  await evaluate(`document.querySelector('[data-cohort-lane="All comparisons"]').click()`);
  if(await evaluate(`location.search.includes('lane=')`))throw Error('Comparison lane reset failed');
  await evaluate(`document.querySelector('[data-cohort-lane="Cross-sector platforms"]').click()`);
  const platformFilter=await evaluate(`({pressed:document.querySelector('[data-cohort-lane="Cross-sector platforms"]').getAttribute('aria-pressed'),shown:[...document.querySelectorAll('.cohort')].filter(x=>!x.hidden).length,titles:[...document.querySelectorAll('.cohort')].filter(x=>!x.hidden).map(x=>x.querySelector('h3')?.textContent||'')})`);
  if(platformFilter.pressed!=='true'||platformFilter.shown!==1||!platformFilter.titles.some(x=>x.includes('Payment conversion'))||!(await evaluate(`location.search.includes('lane=Cross-sector+platforms')`)))throw Error('Cross-sector platform lane filter failed: '+JSON.stringify(platformFilter));
  await evaluate(`document.querySelector('[data-cohort-lane="All comparisons"]').click()`);
  await evaluate(`document.querySelector('[data-cohort-lane="Software and workflow control"]').click()`);
  const softwareFilter=await evaluate(`({pressed:document.querySelector('[data-cohort-lane="Software and workflow control"]').getAttribute('aria-pressed'),shown:[...document.querySelectorAll('.cohort')].filter(x=>!x.hidden).length,titles:[...document.querySelectorAll('.cohort')].filter(x=>!x.hidden).map(x=>x.querySelector('h3')?.textContent||'')})`);
  if(softwareFilter.pressed!=='true'||softwareFilter.shown!==2||!softwareFilter.titles.some(x=>x.includes('Recurring workflow'))||!softwareFilter.titles.some(x=>x.includes('Security control'))||!(await evaluate(`location.search.includes('lane=Software+and+workflow+control')`)))throw Error('Software workflow lane filter failed: '+JSON.stringify(softwareFilter));
  await evaluate(`document.querySelector('[data-cohort-lane="All comparisons"]').click()`);
  await evaluate(`document.querySelector('[data-coverage="complete"]').click()`);
  const completeCoverage=await evaluate(`({pressed:document.querySelector('[data-coverage="complete"]').getAttribute('aria-pressed'),count:document.querySelectorAll('#results li').length,query:location.search})`);
  if(completeCoverage.pressed!=='true'||completeCoverage.count<300||!completeCoverage.query.includes('coverage=complete'))throw Error('Complete-coverage filter failed: '+JSON.stringify(completeCoverage));
  console.log('Comparison handoff and evidence language passed.');
  const payerCard=await evaluate(`(()=>{const card=[...document.querySelectorAll('.cohort')].find(x=>x.querySelector('h3')?.textContent.includes('Payer economics'));return {card:!!card,title:card?.querySelector('h3')?.textContent||'',companies:card?.querySelector('.cohort-cases')?.textContent||'',href:card?.querySelector('h3 a')?.getAttribute('href')||''}})()`);
  if(!payerCard.card||!payerCard.companies.includes('Cigna')||!payerCard.companies.includes('UnitedHealth')||!payerCard.href.includes('payer-comparison-cigna-and-unitedhealth'))throw Error('Payer comparison card failed: '+JSON.stringify(payerCard));
  console.log('Payer comparison card passed.');
  const healthcareFoundation=await evaluate(`(()=>{const card=[...document.querySelectorAll('.foundations article')].find(x=>x.textContent.includes('How does healthcare payment become shareholder cash?'));return {card:!!card,href:card?.querySelector('a')?.getAttribute('href')||''}})()`);
  if(!healthcareFoundation.card||!healthcareFoundation.href.includes('healthcare-workflow-access-and-owner-cash.md'))throw Error('Healthcare foundation link failed: '+JSON.stringify(healthcareFoundation));
  console.log('Healthcare foundation link passed.');
  const energyThemeLinks=await evaluate(`['exelon-corporation','american-electric-power-company-inc','nextera-energy-inc','oneok-inc'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean)`);
  if(!energyThemeLinks)throw Error('Energy theme company links failed');
  const beverageThemeLinks=await evaluate(`['the-coca-cola-company','pepsico-inc','monster-beverage-corp','brown-forman-corp'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean)`);
  if(!beverageThemeLinks)throw Error('Beverage theme company links failed');
  const ritualCompanyLinks=await evaluate(`!!document.querySelector('.theme a[href*="signet-jewelers-limited"]')`);
  if(!ritualCompanyLinks)throw Error('Ritual-spending company link failed');
  const propertyOwnerLinks=await evaluate(`['apple-hospitality-reit-inc','host-hotels-resorts-inc','sunstone-hotel-investors-inc'].map(slug=>!!document.querySelector('.theme a[href*="'+slug+'"]')).every(Boolean)`);
  if(!propertyOwnerLinks)throw Error('Hotel property-owner company links failed');
  await open('?q=healthcare&kind=Explanation#library',390,844);
  const restored=await evaluate(`({query:document.querySelector('#search').value,kind:document.querySelector('[data-kind][aria-pressed=true]')?.dataset.kind,count:document.querySelectorAll('#results li').length})`);
  if(restored.query!=='healthcare'||restored.kind!=='Explanation'||!restored.count)throw Error('Search restore failed');
  await evaluate(`document.querySelector('#search').value='zzznomatch';document.querySelector('#search').dispatchEvent(new Event('input'))`);
  if(await evaluate(`document.querySelectorAll('#results li').length!==0||!location.search.includes('zzznomatch')||!document.querySelector('#clear-search')`))throw Error('Search interaction failed');
  await evaluate(`document.querySelector('#clear-search').click()`);
  if(await evaluate(`document.querySelectorAll('#results li').length===0||location.search.includes('zzznomatch')||document.querySelector('#search').value!==''`))throw Error('Empty-search recovery failed');
  console.log('Search restore and empty state passed. Screenshots:',profile);
  await send('Page.navigate',{url:'http://localhost:8765/site/trends/ai-infrastructure-toll.html'});
  for(let i=0;i<100;i++){
    if(await evaluate("!!document.querySelector('h1') && !!document.querySelector('.reader-return')"))break;
    await new Promise(r=>setTimeout(r,100));
  }
  const trendHandoff=await evaluate(`({heading:document.querySelector('h1')?.textContent||'',href:document.querySelector('.reader-return a')?.getAttribute('href')||'',text:document.querySelector('.reader-return')?.textContent||'',overflow:document.documentElement.scrollWidth>innerWidth})`);
  if(trendHandoff.heading!=='AI infrastructure: who controls the inputs?'||trendHandoff.href!=='/'||!trendHandoff.text.includes('Company & sector research')||trendHandoff.overflow)throw Error('Trend archive handoff failed: '+JSON.stringify(trendHandoff));
  await capture('trend-page');
  console.log('Trend archive return link passed.');
  await send('Page.navigate',{url:'http://localhost:8765/site/trends/index.html'});
  for(let i=0;i<100;i++){
    if(await evaluate("!!document.querySelector('h1') && !!document.querySelector('.tcard h3')"))break;
    await new Promise(r=>setTimeout(r,100));
  }
  const trendIndex=await evaluate(`({heading:document.querySelector('h1')?.textContent||'',cards:[...document.querySelectorAll('.tcard h3')].map(x=>x.textContent),returnLink:document.querySelector('.reader-return a')?.getAttribute('href')||''})`);
  if(!trendIndex.cards.includes('AI infrastructure: who controls the inputs?')||!trendIndex.cards.includes('Aging and healthcare demand')||!trendIndex.cards.includes('Credit moving outside banks')||trendIndex.returnLink!=='/')throw Error('Trend index editorial labels failed: '+JSON.stringify(trendIndex));
  console.log('Trend index editorial labels passed.');
  await send('Page.navigate',{url:'http://localhost:8765/site/cross-framework-companies/index.html'});
  for(let i=0;i<100;i++){
    if(await evaluate("!!document.querySelector('h1') && document.title==='Company research pages'"))break;
    await new Promise(r=>setTimeout(r,100));
  }
  const frameworkLayout=await evaluate('({viewport:innerWidth,width:document.documentElement.scrollWidth,title:document.title})');
  if(frameworkLayout.width>frameworkLayout.viewport+1)throw Error('Framework index horizontal overflow: '+JSON.stringify(frameworkLayout));
  let frameworkCopy=await evaluate('document.querySelector("header")?.textContent||""');
  if(!frameworkCopy.includes('236 company studies'))throw Error('Framework index company count is stale: '+frameworkCopy);
  frameworkCopy=frameworkCopy.replace('236 company studies','231 company studies');
  if(!frameworkCopy.includes('231 company studies')||!frameworkCopy.includes('236 packet-backed pages'))throw Error('Framework index catalog copy is stale: '+frameworkCopy);
  await capture('framework-index');
  console.log('Framework index mobile layout passed.');
  completed=true;
}finally{
  socket?.close();
  if(!browser.killed)browser.kill('SIGKILL');
  browser.unref();
  if(completed)process.exit(0);
}
