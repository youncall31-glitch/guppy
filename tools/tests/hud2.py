import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/index.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("TUT.on&&tutEnd(); S.unl=null; S.divOffered=1; Q.length=0; modalOpen&&closeSheet(); S.money=9999; C.buy(S,'tank'); C.buy(S,'show','cave'); S.orders=[CORE.makeOrder(S,Math.random)]; render()")
        await pg.wait_for_timeout(1500); await pg.evaluate("Q.length=0; modalOpen&&closeSheet()"); await pg.wait_for_timeout(400)
        await pg.screenshot(path='m1.png')
        await pg.click('#menuBtn'); await pg.wait_for_timeout(300); await pg.screenshot(path='m2.png')
        await pg.click('#menu [data-a=decomode]'); await pg.wait_for_timeout(500); await pg.screenshot(path='m3.png')
        print('deco', await pg.evaluate("DECO_MODE"), 'menu open', await pg.evaluate("$('#menu').classList.contains('on')"))
        await pg.click('#decoBtn'); await pg.wait_for_timeout(300)
        await pg.click('#shelf [data-a=tnext]'); await pg.wait_for_timeout(300); await pg.click('#shelf [data-a=tnext]'); await pg.wait_for_timeout(1200); await pg.screenshot(path='m4.png')
        print('cur', await pg.evaluate("S.cur"))
        await pg.click('#menuBtn'); await pg.wait_for_timeout(200); await pg.mouse.click(200,500); await pg.wait_for_timeout(200)
        print('closed by outside tap', not await pg.evaluate("$('#menu').classList.contains('on')"), errs)
        await b.close()
asyncio.run(main())
