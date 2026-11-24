import asyncio, json
from playwright.async_api import async_playwright
st=open('/home/claude/ustate/s.txt').read().strip()[len('GUPPY-STATE '):]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=2); await ctx.add_init_script("localStorage.setItem('guppy-tycoon-v1', "+json.dumps(st)+")"); pg=await ctx.new_page()
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///home/claude/guppy/index.html'); await pg.wait_for_timeout(1500)
        await pg.evaluate("Q.length=0; modalOpen&&closeSheet()")
        goals=[{'color':'blue','tail':'veil','pat':'grass'},{'color':'yellow','pat':'halfblack','tail':'delta'},{'metal':True,'color':'yellow','pat':'cobra'},{'color':'red','pat':'grass'},{'albino':True,'color':'yellow','pat':'cobra'}]
        for g in goals:
            r=await pg.evaluate("g=>{const t0=performance.now(); const B=CORE.goalBlock(S,g); const r=CORE.planFor(S,g,1); const T=CORE.planTwo(S,g,1,3); const U=CORE.planThree(S,g,1,2); return [Math.round(performance.now()-t0), B, (r.opts||[]).map(c=>Math.round(c.p*100)), T.map(t=>Math.round(t.p*100)), U.map(t=>Math.round(t.p*100))]}", g)
            print(json.dumps(g), r)
        await pg.evaluate("UI.pregOk=1; S.boxGoal=S.boxGoal||{}; S.boxGoal[1]={albino:true,color:'yellow',pat:'cobra'}; act('autopair',{dataset:{id:'1'}})")
        await pg.wait_for_timeout(3000); await pg.screenshot(path='p3a.png', full_page=False)
        await pg.evaluate("document.querySelector('#modal .in, #sheet')?.scrollBy?.(0,600)"); 
        k = await pg.evaluate("UI.pp && UI.pp.all.findIndex(c=>c.gen===3)")
        print('gen3 idx', k)
        if k is not None and k>=0:
            await pg.evaluate(f"act('planpick',{{dataset:{{v:'{k}'}}}})"); await pg.wait_for_timeout(500)
            print(await pg.evaluate("JSON.stringify(S.boxPlan)"))
            for st_ in range(2):
                await pg.evaluate("for(let d=0;d<22;d++){CORE.dayTick(S,Math.random); S.fish.forEach(f=>f.atRisk=false)} S.money=9999; render(); showBox(1)"); await pg.wait_for_timeout(400)
                await pg.evaluate("UI.pregOk=1; act('plan2',{dataset:{id:'1'}})"); await pg.wait_for_timeout(400)
                print(st_, await pg.evaluate("[JSON.stringify(S.boxPlan), JSON.stringify(S.boxGoal[1]||null), document.querySelector('#toast')?.textContent]"))
            await pg.screenshot(path='p3b.png')
        print(errs); await b.close()
asyncio.run(main())
