import os
d=os.path.dirname(os.path.abspath(__file__))
r=lambda f:open(os.path.join(d,f),encoding='utf-8').read()
paths=''.join('<path d="%s"/>'%p for p in r('_src/poland_paths.txt').split('\n') if p.strip())
s=(r('src.html').replace('{{BADGE_STYLE}}',r('_src/badge_style.part').replace('<style>','').replace('</style>','').strip())
   .replace('{{BADGE_LINK}}',r('_src/badge_link.part').strip()).replace('{{LOGO}}',r('_src/logo_inline.svg').strip()).replace('{{POLAND}}',paths))
assert '{{' not in s
open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(s)
print(len(s))
