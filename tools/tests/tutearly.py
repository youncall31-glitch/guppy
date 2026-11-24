import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':360,'height':740},device_scale_factor=2,is_mobile=True,has_touch=True)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/index.html'); await pg.wait_for_timeout(1800)
        shot=lambda n: pg.screenshot(path=f'e{n}.png')
        print('start',await pg.evaluate('TUT.i')); await shot(0); await pg.click('#tut [data-t=next]', timeout=5000); await pg.wait_for_timeout(500); await shot(1)
        await pg.click('#feedBtn'); await pg.wait_for_timeout(900); await shot(2)
        r=await pg.evaluate("(()=>{const e=SW[TUT.mom].el.getBoundingClientRect();return [e.left+e.width/2,e.top+e.height/2]})()")
        await pg.mouse.click(r[0],r[1]); await pg.wait_for_timeout(700); await shot(3)
        await pg.click('#pop [data-a=follow]'); await pg.wait_for_timeout(900); await shot(4)
        await pg.wait_for_timeout(2500); print('early', await pg.evaluate("[TUT.i, S.fish.filter(f=>f.atRisk).length]")); await pg.click('#rescue button', force=True); await pg.wait_for_timeout(1500); await shot(5)
        await pg.wait_for_timeout(5000); await shot(6)
        print('step', await pg.evaluate("[TUT.i, S.fish.filter(f=>f.atRisk).length]"))
        await pg.evaluate("0"); await pg.wait_for_timeout(700); await shot(7)
        for i in range(8):
            if not await pg.evaluate("TUT.on"): break
            await pg.evaluate("(()=>{const e=TS()[TUT.i].el&&TS()[TUT.i].el(); if(e) e.setAttribute('data-tt','1')})()")
            print('i', await pg.evaluate('TUT.i'), await pg.evaluate('TS()[TUT.i].wait'))
            await shot(8+i)
            await pg.click('[data-tt="1"]', timeout=5000, force=True); await pg.evaluate("document.querySelectorAll('[data-tt]').forEach(e=>e.removeAttribute('data-tt'))")
            await pg.wait_for_timeout(600); await shot(20+i); await pg.wait_for_timeout(1800)
        await pg.wait_for_timeout(1500); await pg.evaluate("Q.length=0; modalOpen&&closeSheet()"); await pg.wait_for_timeout(300)
        print('done', await pg.evaluate("[TUT.on,S.tutDone,C.at(S,'nursery').length,S.stats.fed]"), errs)
        await b.close()
asyncio.run(main())
