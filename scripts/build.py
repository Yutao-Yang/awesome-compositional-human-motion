"""Build deterministic public survey views from auditable intake records (stdlib only)."""
from pathlib import Path
import collections,datetime as dt,difflib,html,json,re
from bibtex_fields import strip_abstract
ROOT=Path(__file__).resolve().parents[1]
CATS={
 'classics':'Classical motion composition', 'temporal':'Temporal composition & long sequences',
 'spatial':'Body-part & semantic composition','editing':'Motion editing & in-betweening',
 'backbones':'Generative backbones & representations','objects':'Human-object & articulated interaction',
 'scenes':'Human-scene interaction & planning','people':'Multi-person & collaborative interaction',
 'datasets':'Datasets & compositional evaluation','physics':'Physics-based character control',
 'humanoids':'Humanoid transfer & loco-manipulation','audio':'Audio, dance & gesture composition',
 'surveys':'Surveys & field maps','video':'Adjacent: compositional human video'}
OVERRIDES={}
for cat,ids in {
 'classics':'motion-graphs interactive-motion-examples motion-annotations parametric-motion-graphs',
 'temporal':'teach priormdm diffcollage multi-act-2022 st2m amd-autoregressive flowmdm stmc t2lm dart motion-mamba prism timelinecontrol',
 'spatial':'finemogen fusion sinc amd-anatomical parco mixermdm frankenmotion demogen coma energymogen salad',
 'editing':'omnicontrol gmd dno rg-dno motionclip motionfix motionclr motionlab mmm bamm',
 'backbones':'remodiffuse momask actor temos mdm mld t2m-gpt tmr',
 'objects':'procigen dechoi omomo chois cg-hoi interdiff himo goal saga imos interact pami trace interactmove hoifhli primhoi sk-hoi duethoi cosmi',
 'scenes':'unihsi interactagent coins samp dimos scenediffuser circle trumans occupancy pigraphs world2hosi',
 'people':'intermask intergen remos freemotion inter-x core4d hhoi-text',
 'datasets':'finemotion vimogen-mbench motionmillion best-automated-metric parahome amass babel kitml humanml3d grab behave intercap motionx instructmotion robomocap hiphi mocapact',
 'physics':'intermimic physdiff simdiff deepmimic amp ase diffmimic phc pulse maskedmimic closd mhc maskadapt',
 'humanoids':'exbody beyondmimic gmr weave intermimicgen grail',
 'audio':'cfgcomposer edge lodge emage finedance moco',
 'surveys':'interaction-survey generative-survey text-motion-overview video-motion-survey',
 'video':'realis-motion',
}.items():
 for i in ids.split():OVERRIDES[i]=cat

def group(p):
 if p['id'] in OVERRIDES:return OVERRIDES[p['id']]
 c=p['category'].lower()
 if any(s in c for s in ['style','retarget','representation','backbone']):return 'backbones'
 if any(s in c for s in ['editing','in-between']):return 'editing'
 if any(s in c for s in ['spatial','part','semantic','decompos','model composition']):return 'spatial'
 return 'temporal'
def identity(p):
 m=re.search(r'arxiv.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})',p['url'])
 return m[1] if m else re.sub(r'[^a-z0-9]','',p['title'].lower())
def clean_title(s):return s.replace('{','').replace('}','').replace('\\&','&').strip()
def dump(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def run():
 previous_keys={p['id']:p['citekey'] for p in json.loads((ROOT/'papers.json').read_text())} if (ROOT/'papers.json').exists() else {}
 records={};duplicates=[]
 for file in sorted((ROOT/'intake').glob('*.json'),key=lambda f:(f.name.startswith('deep_batch'),f.name)):
  for raw in json.loads(file.read_text()):
   p=dict(raw); key=next((k for k,v in records.items() if v['id']==p['id']),identity(p));p['intake_sources']=[file.name]
   p['tags']=[p['category']];p['category_id']=group(p)
   if key in records:
    old=records[key]
    if 'arxiv.org/abs/' in p['url'] and 'arxiv.org/abs/' not in old['url']:old['url']=p['url']
    duplicates.append({'identity':key,'ids':[old['id'],p['id']],'intake':file.name})
    old['intake_sources']+=p['intake_sources'];old['tags']=sorted(set(old['tags']+p['tags']))
    for f in ['method','conditions','evaluation','evidence_locator','publication_note','year_basis','venue','code','data_split','metrics','full_text_source','audit_status','version_note','source_receipt','full_text_version','full_text_sha256','full_text_bytes','title_note','code_note','code_evidence_url','project_url']:
     if p.get(f):old[f]=p[f]
    if p.get('evidence_level')=='method':old['evidence_level']='method';old['evidence_url']=p['evidence_url']
    if p.get('audit_status')=='full_text_checked':
     old['summary']=p['summary'];old['limitations']=p['limitations'];old['checked']=p['checked']
     if p.get('bibliographic_correction'):old['title']=p['title']
    elif p['limitations'] not in old['limitations']:old['limitations']+=' '+p['limitations']
   else:records[key]=p
 metadata=json.loads((ROOT/'sources/metadata.json').read_text())
 releases={x['id']:x for x in json.loads((ROOT/'sources/release_links.json').read_text())} if (ROOT/'sources/release_links.json').exists() else {}
 mismatches=[];bib=[];no_bib=[]
 for key,p in records.items():
  m=metadata.get(p['url'],{});release=releases.get(p['id'],{})
  if not p.get('code') and release.get('code_http_status')==200:p['code']=release['code'];p['code_evidence_url']=release['source']
  if len(release.get('project_candidates',[]))==1:p['project_url']=release['project_candidates'][0]
  p['submitted_title']=p['title'];p['submitted_year']=p['year']
  if m.get('title'):
   title=clean_title(m['title']);ratio=difflib.SequenceMatcher(None,re.sub(r'\W','',p['title'].lower()),re.sub(r'\W','',title.lower())).ratio()
   if ratio<.75:mismatches.append({'id':p['id'],'intake_title':p['title'],'official_title':title,'similarity':round(ratio,3)})
   p['title']=title
  if m.get('authors'):p['authors']=m['authors']
  if m.get('year'):p['year']=m['year']
  p['bibliography_source']=m.get('metadata_url',p['url'])
  p['bibliography_status']=('primary-transcribed' if m.get('origin')=='manually_transcribed_primary_source' else 'official') if m.get('bibtex') else 'curated'
  if m.get('arxiv'):p['arxiv']=m['arxiv'];p['first_preprint_year']=int('20'+m['arxiv'][:2])
  if p['id']=='coma':
   p['venue']='AAAI 2026';p['publication_note']='AAAI 40(11), 9206–9214; DOI 10.1609/aaai.v40i11.37878. Published author list differs from the arXiv record; bibliography below cites the arXiv version.'
   p['publication_url']='https://ojs.aaai.org/index.php/AAAI/article/view/37878'
  v=re.search(r'content/(CVPR|ICCV|WACV)(20\d{2})(W)?/',p['url']+' '+p['evidence_url'])
  if v and not p.get('venue'):p['venue']=v[1]+(' Workshops' if v[3] else '')+' '+v[2]
  if p.get('year_basis'):
   p['publication_note']=(p.get('publication_note','')+' '+p['year_basis']).strip()
   first=re.search(r'(?:preprint.*?)(20\d{2})',p['year_basis'])
   if first:p.setdefault('first_preprint_year',int(first[1]))
  p['display_year']=p.get('first_preprint_year',p['year'])
  # Stable, documented citekeys rather than changing author-derived endpoint keys.
  p['citekey']=previous_keys.get(p['id'],p['id'].replace('-','')+str(p['year']))
  base_axes={'classics':['temporal'],'temporal':['temporal'],'spatial':['spatial','semantic'],'editing':['editing'],'backbones':['representation'],'objects':['object-contact'],'scenes':['scene-state'],'people':['multi-person'],'datasets':['data'],'physics':['physical-skill'],'humanoids':['embodiment','physical-skill'],'audio':['cross-modal'],'surveys':['taxonomy'],'video':['cross-modal','appearance-motion']}
  p['composition_axes']=base_axes[p['category_id']].copy()
  if p['id'] in ('sinc','cosmi'):p['composition_axes']+=['data','spatial']
  if p['id'] in ('stmc','frankenmotion','timelinecontrol','himo'):p['composition_axes']+=['temporal','spatial']
  if p['id'] in ('world2hosi','hoifhli','primhoi','weave'):p['composition_axes']+=['temporal','object-contact','scene-state']
  p['composition_axes']=sorted(set(p['composition_axes']))
  if m.get('bibtex'):
   b=re.sub(r'(@\w+\s*\{)[^,]+',lambda q:q[1]+p['citekey'],m['bibtex'],count=1)
  else:
   no_bib.append(p['id'])
   fields={'title':'{'+p['title']+'}','year':str(p['year']),'url':p['url'],'note':'Curated minimal record; verify publication-specific metadata before submission'}
   if p.get('authors'):fields['author']=' and '.join(p['authors'])
   b='@misc{'+p['citekey']+',\n'+''.join('  '+k+' = {'+v+'},\n' for k,v in fields.items())+'}\n'
  b=strip_abstract(b)
  b='\n'.join(line.rstrip() for line in b.splitlines())+'\n'
  p['bibtex']=b;bib.append(b.strip())
 papers=sorted(records.values(),key=lambda p:(list(CATS).index(p['category_id']),-p['display_year'],p['title']))
 dump(ROOT/'papers.json',papers)
 dump(ROOT/'sources/full_text_inventory.json',[{k:p[k] for k in ['id','full_text_source','full_text_version','full_text_sha256','full_text_bytes','evidence_locator','checked'] if k in p} for p in papers if p.get('audit_status')=='full_text_checked'])
 (ROOT/'references.bib').write_text('% Official-source records where available; stable survey citekeys.\n% arXiv versions are cited as preprints, not silently relabeled as proceedings.\n\n'+'\n\n'.join(bib)+'\n')
 counts=collections.Counter(p['category_id'] for p in papers);levels=collections.Counter(p['evidence_level'] for p in papers)
 fulltext=sum(p.get('audit_status')=='full_text_checked' for p in papers)
 report={'full_text_checked':fulltext,'date':'2026-11-19','papers':len(papers),'evidence':dict(levels),'categories':dict(counts),'duplicates_merged':duplicates,'title_differences_to_review':mismatches,'minimal_bibliographies':no_bib,'external_reproduction':False}
 dump(ROOT/'audit.json',report)
 matrix=['# Method-level comparison matrix','','Input contracts are not interchangeable. These are targeted reading notes, not reproduced scores. Each title links to a fuller audit card.','','| Paper | Composition axes | Inputs checked | Mechanism | Evaluation checked |','|---|---|---|---|---|']
 for p in papers:
  if p['evidence_level']!='method':continue
  cells=[f"[{p['id']}](papers.md#{p['id']})",', '.join(p['composition_axes']),p.get('conditions','Pending'),p.get('method','Pending'),p.get('evaluation','Pending')]
  matrix.append('| '+' | '.join(str(c).replace('|','/').replace('\n',' ') for c in cells)+' |')
 (ROOT/'notes/comparison.md').write_text('\n'.join(matrix)+'\n')
 protocols=['# Data splits and evaluation protocols','','Only explicitly reported splits are stated. Missing details and non-applicable splits are distinguished. Source locators point into the audited full text.','','| Paper | Data and split | Metrics | Source locator | Reading scope |','|---|---|---|---|---|']
 for p in papers:
  cells=[f"[{p['id']}](papers.md#{p['id']})",p.get('data_split','Earlier targeted reading; structured split audit pending.'),p.get('metrics','See evaluation in the earlier targeted audit.'),p.get('evidence_locator','Not recorded in earlier pass'),p.get('audit_status','targeted_method_reading')]
  protocols.append('| '+' | '.join(str(c).replace('|','/').replace('\n',' ') for c in cells)+' |')
 (ROOT/'notes/protocols.md').write_text('\n'.join(protocols)+'\n')
 # README: graph gives overview, ordinary Markdown links remain reliable on GitHub.
 lines=['# Compositional Human Motion & Interaction','',
 '**A living paper survey of temporal, spatial, semantic, interaction and skill composition for digital humans.**','',
 '从经典动作拼接到生成模型、交互与具身执行，按“组合了什么、依赖哪些条件、验证了什么”组织。','',
 f'Last audit: **2026-11-19** · **{len(papers)} unique papers** · **{fulltext} full-text checks / {levels["method"]-fulltext} earlier targeted method readings / {levels["abstract"]} abstract-only records** · No external method reproduced.','',
 '[Interactive clickable map](https://yutao-yang.github.io/awesome-compositional-human-motion/) · [All audit cards](notes/papers.md) · [Comparison matrix](notes/comparison.md) · [Data & metrics](notes/protocols.md) · [Benchmarks](notes/benchmarks.md) · [中文阅读指南](notes/reading-guide.zh.md) · [BibTeX](references.bib) · [JSON](papers.json) · [Search & inclusion protocol](SEARCH_PROTOCOL.md) · [Maintenance](CONTRIBUTING.md)','',
 '> Breadth-first, evidence-labelled curation; not a claim of all-field completeness. Full-text checks include methods, input conditions, split and metrics; earlier targeted method readings are separately labelled. Neither means reproduction. Displayed years use the first preprint where known; venue and cited-version bibliography years are separate.','',
 '## Research map','',
 'The diagram is a visual overview. Every category and paper in the directory below is a normal clickable link; the interactive map also offers search, evidence filters and expandable paper cards.','',
 '[![Academic taxonomy drawn as editable PowerPoint shapes](figures/taxonomy-overview.png)](https://yutao-yang.github.io/awesome-compositional-human-motion/)','','[Download editable PowerPoint](figures/compositional-human-motion-taxonomy.pptx) · [Five detailed branch diagrams](figures/README.md)','','<details>','<summary>Text-source taxonomy (Mermaid)</summary>','','```mermaid','mindmap','  root((Compositional Human Motion))']
 branches={'Motion composition':['classics','temporal','spatial','editing','backbones'],'Interaction composition':['objects','scenes','people'],'Data and execution':['datasets','physics','humanoids'],'Related fields':['audio','surveys','video']}
 for label,cats in branches.items():
  lines+=['    '+label]
  for c in cats:lines+=['      '+CATS[c].replace('&','and')]
 lines+=['```','','</details>','','## Clickable directory','']
 for c in CATS:
  lines+=[f'- [{CATS[c]}](#{c}) — {counts[c]} papers']
 lines+=['','## How to read the evidence','',
 '- **Abstract**: identity and task-level claims checked against a primary source; detailed protocol remains to be audited.',
 '- **Full text checked**: read the primary methods and experiments, including input contract, data/split, named metrics and limitations. See exact source locators.',
 '- **Earlier targeted method reading**: targeted method/conditions/evaluation reading from the previous release; not yet the same structured audit as the new full-text round.',
 '- **Curator boundary**: limitations distinguish comparison scope from authors’ claims; they do not assert an untested method failure.',
 '- **Official code link**: points to an author-linked repository; availability is not installation, licensing or reproducibility verification.','',
 'A long sequence is not automatically compositional generalization. Report unseen source pairings, unseen semantic skill pairings and state-dependent task chains separately.','']
 cards=['# Paper audit cards','','Checked: 2026-11-19. Evidence levels describe reading, not reproduction. Curator boundaries are comparison guidance.','']
 for c,label in CATS.items():
  lines += [f'<a id="{c}"></a>',f'## {label}','','| Paper | First public / venue | Why it belongs | Evidence | Links |','|---|---|---|---|---|']
  for p in (p for p in papers if p['category_id']==c):
   links=f'[Paper]({p["url"]}) · [Audit](notes/papers.md#{p["id"]})'
   if p.get('code'):links+=f' · [Code]({p["code"]})'
   summary=p['summary'].replace('|','/').replace('\n',' ')
   lines += [f'| **{p["id"]}** — {p["title"]} | {p["display_year"]}'+ (' / '+p['venue'] if p.get('venue') else '')+f' | {summary} | {p.get("audit_status",p["evidence_level"])} | {links} |']
   cards += [f'<a id="{p["id"]}"></a>',f'## {p["title"]}','',f'**{p["id"]} · {p["display_year"]} · {label} · {p["evidence_level"]}**','',f'[Primary source]({p["url"]}) · [Evidence]({p["evidence_url"]}) · Citekey: `{p["citekey"]}`','']
   if p.get('authors'):cards+=['**Authors of cited version:** '+ '; '.join(p['authors'])+'.','']
   for f,l in [('summary','Contribution / composition'),('method','Mechanism'),('conditions','Input contract'),('data_split','Data and split'),('metrics','Evaluation metrics'),('evaluation','Evaluation checked'),('full_text_source','Full-text source'),('audit_status','Reading status'),('version_note','Full-text version note'),('full_text_version','Inspected version'),('full_text_sha256','Full-text SHA256'),('code_note','Repository scope'),('evidence_locator','Source locator'),('limitations','Scope / curator boundary'),('publication_note','Publication / version note')]:
    if p.get(f):cards+=['**'+l+':** '+str(p[f]),'']
   cards+=['**Composition axes:** '+', '.join(p['composition_axes'])+'.','', '**Metadata:** '+p['bibliography_status']+'; [source]('+p['bibliography_source']+'); checked '+p['checked']+'.','']
  lines+=['']
 lines+=['## Citation and reuse','','Use [references.bib](references.bib) for the exact cited version. Some older author pages only support a minimal curated record; these are explicitly flagged in [audit.json](audit.json). Verify venue-specific formatting before submission. No paper PDFs, datasets or weights are mirrored.','',
 '## Contributing','','See [CONTRIBUTING.md](CONTRIBUTING.md). Keep primary-source provenance, preserve negative and unknown evidence, and rebuild generated views from the structured records.','']
 (ROOT/'README.md').write_text('\n'.join(lines));(ROOT/'notes/papers.md').write_text('\n'.join(cards))
 # Shared embedded data works when opened locally as well as on GitHub Pages.
 payload=json.dumps(papers,ensure_ascii=False).replace('<','\\u003c')
 (ROOT/'docs/papers.js').write_text('window.SURVEY_PAPERS='+payload+';\nwindow.SURVEY_CATEGORIES='+json.dumps(CATS)+';\n')
 print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
