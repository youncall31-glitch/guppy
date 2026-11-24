from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    e=[];pg.on('pageerror',lambda x:e.append(str(x)))
    pg.goto('file:///home/claude/guppy/test_play.html');pg.wait_for_timeout(2500)
    r=pg.evaluate("""(()=>{Q.length=0;if(modalOpen)closeSheet();
      const g={metal:true,color:'yellow',pat:'cobra',tail:'delta'};
      const A=S.fish.filter(C.isAdult);
      // fill 3 boxes with recommended pairs
      const out=[];
      for(let i=0;i<3;i++){const M=A.filter(f=>f.sex==='m'&&!f.loc.startsWith('box')),F=A.filter(f=>f.sex==='f'&&!f.loc.startsWith('box'));if(!M.length||!F.length)break;placePair(i,M[0],F[0]);S.treeBox=S.treeBox||{};S.treeBox[i]=g;}
      const m0=S.money, f0=S.fish.length; let born=0,kept=0,adopt=0,coins=0,hits=0,run=0;
      for(let d=0;d<30;d++){const ev=C.dayTick(S,Math.random);run+=S.lastBoxRun||0;ev.filter(x=>x.t==='birth'&&x.where==='box').forEach(x=>{born+=x.n;kept+=x.kept;adopt+=x.adopt||0;coins+=x.coins||0;hits+=x.hit||0;});}
      return {born,kept,adopt,coins,hits,run,done:S.boxDone,fish:[f0,S.fish.length],money:[m0,S.money]};})()""")
    print(r)
    pg.evaluate("render();showBox(0)");pg.wait_for_timeout(500);pg.screenshot(path='sb.png')
    print(e)
