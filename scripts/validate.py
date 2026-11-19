"""Validate bibliography identity, required evidence, generated parity and local links."""
from pathlib import Path
import collections,hashlib,json,re,subprocess,sys,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
def validate():
 p=json.loads((ROOT/'papers.json').read_text()); errors=[]
 ids=[x['id'] for x in p];keys=[x['citekey'] for x in p]
 for name,values in [('paper IDs',ids),('citekeys',keys)]:
  if len(set(values))!=len(values):errors.append('Duplicate '+name)
 for x in p:
  for k in ['id','title','year','category_id','url','summary','limitations','evidence_level','evidence_url','checked','authors','bibtex']:
   if not x.get(k):errors.append(x['id']+': missing '+k)
  if x['evidence_level'] not in ('abstract','method'):errors.append(x['id']+': invalid level')
  if x['evidence_level']=='method':
   for k in ['method','conditions','evaluation']:
    if not x.get(k):errors.append(x['id']+': missing method-level '+k)
  if x.get('audit_status')=='full_text_checked':
   for k in ['data_split','metrics','evidence_locator','full_text_source','full_text_version','full_text_sha256','full_text_bytes']:
    if not x.get(k):errors.append(x['id']+': missing full-text field '+k)
  if x.get('full_text_sha256') and not re.fullmatch(r'[0-9a-f]{64}',x['full_text_sha256']):errors.append(x['id']+': invalid source hash')
  for key in ['url','evidence_url','code']:
   if x.get(key) and not x[key].startswith('https://'):errors.append(x['id']+': non-HTTPS '+key)
  if x['year']>2026 or x['year']<1900:errors.append(x['id']+': invalid year')
  if x['bibtex'].count('{')!=x['bibtex'].count('}'):errors.append(x['id']+': unbalanced BibTeX')
 bib=(ROOT/'references.bib').read_text();bibkeys=re.findall(r'@\w+\s*\{([^,]+),',bib)
 if sorted(bibkeys)!=sorted(keys):errors.append('BibTeX and catalog identities differ')
 if json.loads((ROOT/'audit.json').read_text())['title_differences_to_review']:errors.append('Unresolved title mismatches')
 # All generated views must be reproducible from retained inputs.
 generated=['papers.json','references.bib','README.md','notes/papers.md','audit.json','docs/papers.js','notes/comparison.md','notes/protocols.md','sources/full_text_inventory.json']
 before={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in generated}
 subprocess.run([sys.executable,str(ROOT/'scripts/build.py')],check=True,stdout=subprocess.DEVNULL)
 for f in generated:
  if hashlib.sha256((ROOT/f).read_bytes()).hexdigest()!=before[f]:errors.append('Stale generated view: '+f)
 for f in ROOT.rglob('*'):
  if f.is_file() and f.suffix in ('.md','.bib','.py','.html','.js'):
   for n,line in enumerate(f.read_text().splitlines(),1):
    if line!=line.rstrip():errors.append(str(f.relative_to(ROOT))+': trailing whitespace at '+str(n))
 coverage=ROOT/'audits/requested100_coverage.json'
 if coverage.exists():
  requested=json.loads(coverage.read_text())['requested_ids']
  actual={x['id'] for x in p if x.get('audit_status')=='full_text_checked'}
  if len(requested)!=100 or set(requested)-actual:errors.append('Requested original100 coverage incomplete')
 checked=0
 for f in ROOT.rglob('*.md'):
  body=f.read_text()
  for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',body):
   if target.startswith(('http:','https:','mailto:')):continue
   path,_,anchor=target.partition('#');dest=(f.parent/urllib.parse.unquote(path)).resolve() if path else f
   if not dest.exists():errors.append(str(f.relative_to(ROOT))+': missing '+target);continue
   if anchor and dest.suffix=='.md':
    text=dest.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',text))
    for h in re.findall(r'^#+ (.+)$',text,re.M):anchors.add(re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-'))
    if anchor not in anchors:errors.append(str(f.relative_to(ROOT))+': missing anchor '+target)
   checked+=1
 report={'papers':len(p),'full_text_checked':sum(x.get('audit_status')=='full_text_checked' for x in p),'method_records':sum(x['evidence_level']=='method' for x in p),'bibtex_entries':len(bibkeys),'internal_links_checked':checked,'deterministic_views':len(generated),'errors':errors}
 print(json.dumps(report,indent=2));return not errors
if __name__=='__main__':sys.exit(0 if validate() else 1)
