import asyncio
from playwright.async_api import async_playwright
async def run(mode):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/index.html'); await pg.wait_for_timeout(1500)
        m0=await pg.evaluate("S.money")
        if mode=='pass':
            await pg.click('#tut [data-t=skip]'); await pg.wait_for_timeout(200); print('btn', await pg.evaluate("document.querySelector('#tut [data-t=skip]').textContent"))
            await pg.click('#tut [data-t=skip]'); await pg.wait_for_timeout(1500)
            await pg.screenshot(path='pass.png')
            print('pass', await pg.evaluate("[S.money, S.goal, S.grad, Object.keys(S.unl).length, document.querySelector('#sheet').innerText.slice(0,40)]"), 'gained', (await pg.evaluate("S.money"))-m0)
        else:
            await pg.evaluate("TUT.on&&tutEnd(); Q.length=0; modalOpen&&closeSheet();"); await pg.wait_for_timeout(600)
            print('locked dock', await pg.evaluate("[...document.querySelectorAll('#dock button.lk')].map(b=>b.dataset.dock)"))
            await pg.screenshot(path='lockdock.png')
            got=0
            setups=["S.stats.fed=1","S.stats.rescued=1","(()=>{const a=S.fish.filter(f=>CORE.isAdult(f)&&f.loc==='tank0'); const m=a.find(f=>f.sex==='m'),f=a.find(f=>f.sex==='f'); CORE.moveTo(S,m.id,'box0'); CORE.moveTo(S,f.id,'box0');})()","S.stats.wc=1","(()=>{const f=S.fish[0]; S.reg[f.id]=[S.fish[1].id,S.fish[2]?S.fish[2].id:1,0]; f.age=Math.max(f.age,7);})()","S.stats.sold=1","S.stats.orders=1","S.boxGoal={0:{color:'gray'}}","S.starter={got:{'blue:m':1}}"]
            for i,sx in enumerate(setups):
                await pg.evaluate(f"Q.length=0; modalOpen&&closeSheet(); {sx}; renderHud();")
                g=await pg.evaluate("(()=>{const g=CORE.goalNow(S); return g&&[g.t,g.ok(S)]})()")
                mb=await pg.evaluate("S.money"); await pg.evaluate("act('goal',{dataset:{}})"); await pg.wait_for_timeout(700)
                ma=await pg.evaluate("S.money"); got+=ma-mb
                print(i+1, g, '+', ma-mb, 'unl', await pg.evaluate("Object.keys(S.unl).join(',')"), '|', await pg.evaluate("document.querySelector('#note').textContent"))
            await pg.screenshot(path='grad.png'); print('total', got, await pg.evaluate("document.querySelector('#sheet').innerText.slice(0,60)"))
        print(errs); await b.close()
async def main():
    await run('walk'); await run('pass')
asyncio.run(main())
