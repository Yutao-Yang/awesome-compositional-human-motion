"""Keep bibliographic citations concise without redistributing source abstracts."""
import re
def strip_abstract(bib):
 while True:
  m=re.search(r'^\s*abstract\s*=\s*',bib,re.I|re.M)
  if not m:return bib
  i=m.end();start=i
  if i>=len(bib):return bib
  if bib[i]=='{':
   depth=1;i+=1
   while i<len(bib) and depth:
    if bib[i]=='\\':i+=2;continue
    if bib[i]=='{':depth+=1
    elif bib[i]=='}':depth-=1
    i+=1
  elif bib[i]=='"':
   i+=1
   while i<len(bib):
    if bib[i]=='\\':i+=2;continue
    if bib[i]=='"':i+=1;break
    i+=1
  else:
   while i<len(bib) and bib[i]!=',':i+=1
  while i<len(bib) and bib[i] in ' \t':i+=1
  if i<len(bib) and bib[i]==',':i+=1
  if i<len(bib) and bib[i]=='\n':i+=1
  bib=bib[:m.start()]+bib[i:]
