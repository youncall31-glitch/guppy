import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/index.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("TUT.on&&tutEnd(); S.unl=null; Q.length=0; modalOpen&&closeSheet(); S.divOffered=1; S.stats.fed=1; S.stats.rescued=1; render();")
        await pg.wait_for_timeout(800)
        for gi in [4,5,6]:
            await pg.evaluate(f"Q.length=0; modalOpen&&closeSheet(); S.goal={gi}; renderHud();"); await pg.wait_for_timeout(400)
            r=await pg.evaluate("(()=>{const g=CORE.goalNow(S); const ok=g.ok(S); act('goal',{dataset:{}}); return [g.t, ok, modalOpen, document.querySelector('#sheet').innerText.slice(0,60)]})()")
            await pg.wait_for_timeout(700)
            print(gi, r, await pg.evaluate("[!!document.querySelector('.flash'), document.querySelector('#note').textContent, document.querySelector('#toast').textContent]"))
            await pg.screenshot(path=f'go{gi}.png')
        print(errs); await b.close()
asyncio.run(main())
