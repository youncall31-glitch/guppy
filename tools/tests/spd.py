import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.goto('file:///home/claude/guppy/test_play.html'); await pg.wait_for_timeout(4000)
        r = await pg.evaluate("""new Promise(res=>{const out=[]; const t0=performance.now(); const iv=setInterval(()=>{Object.values(SW).filter(s=>s.adult&&s.el).forEach(s=>out.push(Math.hypot(s.vx,s.vy)/(120*(s.sz||.3)))); if(performance.now()-t0>20000){clearInterval(iv); res(out)}},100)})""")
        import statistics
        r=sorted(r); q=lambda p: round(r[int(len(r)*p)],2)
        print('n',len(r),'BL/s p25/50/75/90/97:',q(.25),q(.5),q(.75),q(.9),q(.97),'still<0.3:',round(sum(1 for x in r if x<.3)/len(r),2),'>2:',round(sum(1 for x in r if x>2)/len(r),2))
        await b.close()
asyncio.run(main())
