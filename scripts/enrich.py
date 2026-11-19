"""Fetch small official bibliographic records. No PDFs, credentials or environments.
Run only when adding papers: python scripts/enrich.py
Existing successes are reused; failures remain explicit in sources/metadata.json.
"""
from pathlib import Path
import concurrent.futures as cf
import datetime as dt
import html
from html.parser import HTMLParser
import json,re,time,urllib.request
ROOT=Path(__file__).resolve().parents[1]
class Metadata(HTMLParser):
 def __init__(self): super().__init__(); self.meta={}; self.text=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='meta' and d.get('name','').startswith('citation_'): self.meta.setdefault(d['name'],[]).append(d.get('content',''))
 def handle_data(self,data): self.text.append(data)
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'CompositionalHumanMotionSurvey/1.0 (bibliography verification)'})
 with urllib.request.urlopen(req,timeout=35) as r: return r.read().decode('utf-8','replace')
def field(bib,key):
 m=re.search(r'\b'+key+r'\s*=\s*\{',bib,re.I)
 if not m:return None
 i=m.end(); depth=1; j=i
 while j<len(bib) and depth:
  if bib[j]=='{':depth+=1
  if bib[j]=='}':depth-=1
  j+=1
 return bib[i:j-1]
def fetch(url):
 out={'url':url,'checked_utc':dt.datetime.now(dt.timezone.utc).isoformat()}
 try:
  ar=re.search(r'arxiv.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})',url)
  if ar:
   u='https://arxiv.org/bibtex/'+ar[1]; bib=get(u)
   if not bib.lstrip().startswith('@'):raise ValueError('Official endpoint did not return BibTeX')
   out.update(status='ok',metadata_url=u,bibtex=bib,title=field(bib,'title'),authors=(field(bib,'author') or '').split(' and '),year=int(field(bib,'year')),arxiv=ar[1])
  else:
   landing=url
   if 'openaccess.thecvf.com/' in url and '/papers/' in url and url.endswith('.pdf'):
    landing=url.replace('/papers/','/html/').removesuffix('.pdf')+'.html'
   elif url.endswith('.pdf'):
    out.update(status='metadata_unavailable',error='PDF identity retained; no HTML bibliography endpoint configured');return out
   s=get(landing); parser=Metadata();parser.feed(s); m=parser.meta
   out.update(status='ok',metadata_url=landing,meta=m)
   if m.get('citation_title'):out['title']=m['citation_title'][0]
   if m.get('citation_author'):out['authors']=m['citation_author']
   date=(m.get('citation_publication_date') or m.get('citation_date') or [''])[0]
   if re.search(r'\d{4}',date):out['year']=int(re.search(r'\d{4}',date)[0])
   # CVF, PMLR and author project pages expose an official citation block.
   text='\n'.join(parser.text); bm=re.search(r'@(?:inproceedings|article|misc|InProceedings)\s*\{',text,re.I)
   if bm:
    start=bm.start();i=text.index('{',start)+1;depth=1
    while i<len(text) and depth:
     if text[i]=='{':depth+=1
     if text[i]=='}':depth-=1
     i+=1
    bib=text[start:i];out['bibtex']=bib
    if not out.get('title'):out['title']=field(bib,'title')
    if not out.get('authors') and field(bib,'author'):out['authors']=field(bib,'author').split(' and ')
    if not out.get('year') and (field(bib,'year') or '').isdigit():out['year']=int(field(bib,'year'))
  return out
 except Exception as e:out.update(status='error',error=type(e).__name__+': '+str(e));return out
if __name__=='__main__':
 dst=ROOT/'sources/metadata.json';dst.parent.mkdir(exist_ok=True)
 old=json.loads(dst.read_text()) if dst.exists() else {}
 urls=sorted({p['url'] for f in (ROOT/'intake').glob('*.json') for p in json.loads(f.read_text())})
 todo=[u for u in urls if old.get(u,{}).get('status')!='ok']
 with cf.ThreadPoolExecutor(max_workers=4) as pool:
  for out in pool.map(fetch,todo):old[out['url']]=out;print(out['status'],out['url'],flush=True)
 dst.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
 print('metadata records',len(old),'errors',sum(x['status']!='ok' for x in old.values()))
