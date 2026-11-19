"""Non-destructive publication of this directory to the designated survey repository.
Usage: python scripts/publish.py --checkout /tmp/survey-checkout --push
Requires an existing clean clone; never publishes the parent project or force-pushes.
"""
from pathlib import Path
import argparse,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
DEST='Yutao-Yang/awesome-compositional-human-motion'
def git(dst,*args,capture=False):
 return subprocess.run(['git','-C',str(dst),*args],check=True,text=True,stdout=subprocess.PIPE if capture else None).stdout
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--checkout',required=True,type=Path);ap.add_argument('--push',action='store_true');args=ap.parse_args();dst=args.checkout.resolve()
 if not (dst/'.git').is_dir():sys.exit('Use an existing dedicated clean clone.')
 remote=git(dst,'remote','get-url','origin',capture=True).strip().removesuffix('.git')
 if remote not in ['https://github.com/'+DEST,'git@github.com:'+DEST]:sys.exit('Unexpected remote; refusing publication.')
 if git(dst,'status','--porcelain',capture=True).strip():sys.exit('Checkout is dirty; refusing to overwrite changes.')
 subprocess.run([sys.executable,str(ROOT/'scripts/validate.py')],check=True)
 allowed={'.md','.json','.bib','.py','.html','.js'};copied=[]
 for src in sorted(ROOT.rglob('*')):
  rel=src.relative_to(ROOT)
  if any(part in ('.git','__pycache__') for part in rel.parts):continue
  if src.is_symlink():sys.exit('Refusing symlink: '+str(rel))
  if not src.is_file():continue
  if src.suffix not in allowed and not (rel.parts[0]=='figures' and src.suffix in ('.png','.pptx')) and src.name not in ('.gitignore','.nojekyll'):sys.exit('Unexpected publication file: '+str(rel))
  target=dst/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target);copied.append(rel)
 print('Copied',len(copied),'survey files; no destination files deleted.')
 git(dst,'add','.')
 changed=git(dst,'diff','--cached','--name-only',capture=True).splitlines()
 if not changed:print('Already synchronized.');sys.exit(0)
 if set(changed)-{str(p) for p in copied}:sys.exit('Unexpected staged path; refusing commit.')
 git(dst,'diff','--cached','--check');git(dst,'diff','--cached','--stat')
 branch=git(dst,'symbolic-ref','--short','HEAD',capture=True).strip()
 if branch!='main':sys.exit('Expected main branch; staged files remain reviewable.')
 git(dst,'commit','-m','Curate compositional human motion survey with evidence and clickable map')
 if args.push:git(dst,'push','origin','HEAD:main')
 else:print('Committed locally. Pass --push to publish after review.')
