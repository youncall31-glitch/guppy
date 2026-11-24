import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/test_play.html'); await pg.wait_for_timeout(2000)
        await pg.evaluate("Q.length=0; modalOpen&&closeSheet(); showTree({metal:true,color:'yellow',pat:'cobra',tail:'delta'})"); await pg.wait_for_timeout(500)
        await pg.screenshot(path='tp_a.png')
        await pg.click('[data-a=treepair] >> nth=0'); await pg.wait_for_timeout(600); await pg.screenshot(path='tp_b.png')
        await pg.click('[data-a=tpsel] >> nth=0'); await pg.wait_for_timeout(300)
        n = await pg.evaluate("[...document.querySelectorAll('[data-a=tpsel]')].findIndex(e=>S.fish.find(f=>f.id==e.dataset.id).sex==='f')")
        await pg.click(f'[data-a=tpsel] >> nth={n}'); await pg.wait_for_timeout(400)
        await pg.evaluate("document.querySelector('.pcard.best')?.scrollIntoView({block:'center'})"); await pg.wait_for_timeout(200); await pg.screenshot(path='tp_c.png')
        await pg.click('.pcard.best [data-a=tpput] >> nth=1'); await pg.wait_for_timeout(600); await pg.screenshot(path='tp_d.png')
        print(await pg.evaluate("[JSON.stringify(S.treeBox), boxPar(1).map(f=>f.sex), JSON.stringify((S.boxGoal||{})[1]||null)]"))
        # old mark flow
        await pg.evaluate("closeSheet(); const f=S.fish.find(x=>CORE.isAdult(x)&&!CORE.isParent(x)); showOld(f.id); window._oid=f.id")
        await pg.wait_for_timeout(400); await pg.evaluate("closeSheet(); render()"); await pg.wait_for_timeout(400)
        print(await pg.evaluate("[S.fish.find(f=>f.id===_oid).oldMark, JSON.stringify(nextAction())]"))
        print(errs); await b.close()
asyncio.run(main())
