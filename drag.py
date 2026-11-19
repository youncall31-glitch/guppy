import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2,has_touch=False)
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/index.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("TUT.on&&tutEnd(); Q.length=0; modalOpen&&closeSheet(); S.divOffered=1; S.speed=0; S.money=9999; CORE.buy(S,'tank'); S.tanks.forEach(t=>{CORE.careOf(t); t.full=3}); render();")
        await pg.wait_for_timeout(1200); await pg.evaluate("modalOpen&&closeSheet(); Q.length=0;")
        # 수컷을 집어서 암컷 위에
        await pg.evaluate("(()=>{const m=S.fish.find(x=>x.sex==='m'), f=S.fish.find(x=>x.sex==='f'); window._m=SW[m.id]; window._f=SW[f.id]; _f.hold=true; _m.hold=true;})()")
        await pg.wait_for_timeout(300)
        def scr(s): return pg.evaluate(f"(()=>{{const r={s}.el.getBoundingClientRect(); return [r.x+r.width/2, r.y+r.height/2]}})()")
        mx,my=await scr('_m'); fx,fy=await scr('_f')
        await pg.evaluate("_m.hold=false")
        await pg.mouse.move(mx,my); await pg.mouse.down(); await pg.wait_for_timeout(600)
        print('drag on', await pg.evaluate("!!DRAG"))
        for i in range(1,11): await pg.mouse.move(mx+(fx-mx)*i/10, my+(fy-my)*i/10); await pg.wait_for_timeout(40)
        await pg.wait_for_timeout(400); print('target', await pg.evaluate("DRAG&&DRAG.tgt===_f.f.id"))
        await pg.screenshot(path='drag1.png')
        await pg.mouse.up(); await pg.wait_for_timeout(500)
        print(await pg.evaluate("[S.fish.filter(x=>x.loc==='box0').length, document.querySelector('#toast')&&document.querySelector('#toast').textContent]"))
        # 두 번째: 암컷(이제 어항엔 없음) 대신 새 구피를 ▶ 로
        await pg.evaluate("(()=>{const r=CORE.buyFounder(S,'m',false,Math.random); render(); })()"); await pg.wait_for_timeout(900)
        await pg.evaluate("(()=>{const f=S.fish.find(x=>x.loc==='tank0'&&CORE.isAdult(x)); window._n=SW[f.id]; window._nid=f.id; _n.hold=true;})()"); await pg.wait_for_timeout(200)
        nx,ny=await scr('_n'); await pg.evaluate("_n.hold=false")
        ar=await pg.evaluate("(()=>{const r=document.querySelector('[data-a=tnext]').getBoundingClientRect(); return [r.x+r.width/2,r.y+r.height/2]})()")
        await pg.mouse.move(nx,ny); await pg.mouse.down(); await pg.wait_for_timeout(600)
        for i in range(1,11): await pg.mouse.move(nx+(ar[0]-nx)*i/10, ny+(ar[1]-ny)*i/10); await pg.wait_for_timeout(40)
        await pg.mouse.up(); await pg.wait_for_timeout(400)
        print(await pg.evaluate("[S.fish.find(x=>x.id===_nid).loc, document.querySelector('#toast').textContent]"))
        print(errs); await b.close()
asyncio.run(main())
