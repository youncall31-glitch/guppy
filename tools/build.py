# index.html → show_demo.html, test_play.html 다시 만들기 (저장소 루트에서 python3 tools/build.py)
import re
idx=open('index.html').read()
m=re.search(r"if \(fresh \|\| !S\.intro\) \{.*?cloudInit\(\);",idx,re.S); assert m
old=open('show_demo.html').read()
a=old.index('/* ---------- 전시 어항 데모'); b=old.index('setTimeout(demo, 300);')+len('setTimeout(demo, 300);')
open('show_demo.html','w').write((idx[:m.start()]+old[a:b]+idx[m.end():]).replace("const KEY = 'guppy-tycoon-v1'","const KEY = 'guppy-show-demo'"))
open('test_play.html','w').write((idx[:m.start()]+open('test_block.js').read()+idx[m.end():]).replace("const KEY = 'guppy-tycoon-v1'","const KEY = 'guppy-test-play'"))
for f in ['index','show_demo','test_play']:
    for i,x in enumerate(re.findall(r'<script[^>]*>(.*?)</script>',open(f+'.html').read(),re.S)):open(f'/tmp/chk_{f}{i}.js','w').write(x)
print('built · 이제 for j in /tmp/chk_*.js; do node --check $j; done')
