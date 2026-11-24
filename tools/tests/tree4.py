import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/test_play.html'); await pg.wait_for_timeout(2000)
        gs=["{metal:true,color:'yellow',pat:'cobra',tail:'delta'}","{color:'red',pat:'halfblack',tail:'veil',albino:true}"]
        for n,g in enumerate(gs):
            await pg.evaluate(f"Q.length=0; modalOpen&&closeSheet(); showTree({g})"); await pg.wait_for_timeout(600)
            await pg.evaluate("document.querySelector('.ttree').scrollIntoView({block:'start'})"); await pg.wait_for_timeout(200); await pg.screenshot(path=f'tt{n}.png')
        print(errs); await b.close()
asyncio.run(main())
