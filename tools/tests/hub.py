import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/index.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("""TUT.on&&tutEnd(); S.unl=null; Q.length=0; modalOpen&&closeSheet(); S.divOffered=1; S.money=999; for(let i=0;i<8;i++)CORE.buyFounder(S,i%2?'m':'f',false,Math.random); S.fish.forEach(f=>{f.age=Math.max(f.age,8); f.preg=0}); const a=S.fish.find(f=>f.sex==='m'&&f.loc==='tank0'&&!f.nick), c=S.fish.find(f=>f.sex==='f'&&f.loc==='tank0'&&!f.nick); for(let i=0;i<3;i++){S.fish.push(Object.assign({},a,{id:S.nextId++,nick:null})); S.fish.push(Object.assign({},c,{id:S.nextId++,nick:null}));} const o=S.fish[S.fish.length-1]; o.age=o.life*.8; S.fish[3].line={...S.fish[3].line, sword:3}; render();""")
        await pg.wait_for_timeout(900); await pg.evaluate("modalOpen&&closeSheet(); Q.length=0; showFishes()"); await pg.wait_for_timeout(400)
        await pg.screenshot(path='hub0.png')
        await pg.evaluate("act('sellhub',{dataset:{}})"); await pg.wait_for_timeout(400); await pg.screenshot(path='hub1.png')
        print(await pg.evaluate("[...document.querySelectorAll('.sgp')].map(s=>s.querySelector('.shh b').textContent+' | '+(s.querySelector('[data-a=hubsell]')||{}).textContent)"))
        n0=await pg.evaluate("S.fish.length"); await pg.evaluate("act('hubsell', document.querySelector('[data-a=hubsell][data-k=dup]'))"); await pg.wait_for_timeout(400)
        print('sold dup', n0, await pg.evaluate("S.fish.length"), await pg.evaluate("document.querySelector('#toast').textContent"))
        await pg.screenshot(path='hub2.png'); print(errs); await b.close()
asyncio.run(main())
