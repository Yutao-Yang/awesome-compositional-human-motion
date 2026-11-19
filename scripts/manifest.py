"""Record the exact public artifact scope after build/validation and before publishing."""
from pathlib import Path
import datetime as dt,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
 dst=ROOT/'sources/content_manifest.json';files=[]
 for p in sorted(ROOT.rglob('*')):
  if not p.is_file() or p==dst or '__pycache__' in p.parts or '.git' in p.parts:continue
  files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 dst.write_text(json.dumps({'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'scope':'Public survey text, bibliography, structured evidence, static viewer and authorized editable diagram with renders','status':'complete_for_listed_files','files':files},ensure_ascii=False,indent=2)+'\n')
 print('Manifest:',len(files),'files;',sum(x['bytes'] for x in files),'bytes')
