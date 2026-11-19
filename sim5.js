const fs=require('fs');const cfg=JSON.parse(process.argv[3]||'{}');
let core=fs.readFileSync(process.argv[2],'utf8').match(/<script id="core">([\s\S]*?)<\/script>/)[1];
if(cfg.curve)core=core.replace('Math.pow(1.6, score(ph) - 3)','Math.pow('+cfg.curve+', score(ph) - 3)');
if(0)core=core.replace('(t.show ? 2 * (1 + addonBonus(t)) : 0)','(t.show ? '+cfg.sm+' * (1 + addonBonus(t)) : 0)');
new Function(core)();const C=globalThis.CORE;Object.assign(C.MKT,cfg.mkt||{});Object.assign(C.SHOW,cfg.show||{});Object.assign(C.UPKEEP,cfg.up||{});
const TH=['forest','iwagumi','jungle'];
function play(style,days){const S=C.newState();S.intro=true;const r=Math.random;const m={tank2:null,show:null,stuck:0,at:{},sold:0,cust:0,ord:0,up:0,shows:0};
for(let d=1;d<=days;d++){const mb=S.money;const ev=C.dayTick(S,r);const inc=ev.find(e=>e.t==='income');m.cust+=inc?inc.amt:0;m.up+=S.lastUpkeep||0;
C.rescue(S);S.tanks.forEach((t,i)=>{if(t.show)return;C.careOf(t);if(t.full<=.5)C.feed(S,i,'flake');if(t.water<45)C.waterChange(S,i)});
while(C.claimGoal(S)){}
for(const c of(style==='casual'?['blue']:['blue','red']))for(const sx of['m','f'])if(!(S.starter&&S.starter.got[c+':'+sx])&&S.money>=30)C.buyStarter(S,c,sx,r);
for(let i=0;i<S.boxes;i++){const b=C.at(S,'box'+i).filter(f=>!f.sep);if(!b.length){const ad=S.fish.filter(f=>C.isAdult(f)&&/^tank/.test(f.loc)&&!S.tanks[+f.loc.slice(4)].show&&!f.preg).sort((a,b)=>C.sellPrice(S,b)-C.sellPrice(S,a));const mm=ad.find(f=>f.sex==='m'),ff=ad.find(f=>f.sex==='f');if(mm&&ff&&ad.filter(f=>f.sex==='m').length>1){C.moveTo(S,mm.id,'box'+i);C.moveTo(S,ff.id,'box'+i)}}}
(S.orders||[]).slice().forEach(o=>{if(C.orderMatches(S,o).length){const x=C.fulfil(S,o.id);if(!x.err)m.ord+=x.o.reward}});
C.at(S,'nursery').filter(C.isAdult).forEach(f=>{if(C.moveTo(S,f.id,'tank'))m.sold+=C.sell(S,f.id)});
// 전시 어항 채우기: 비싼 수컷부터
S.tanks.forEach((t,si)=>{if(!t.show)return;const cand=S.fish.filter(f=>C.isAdult(f)&&!f.preg&&/^tank/.test(f.loc)&&!S.tanks[+f.loc.slice(4)].show).sort((a,b)=>C.sellPrice(S,b)-C.sellPrice(S,a));let n=0;while(C.tankUsed(S,si)<C.tankCap(S,si)&&cand.length>4&&n<2){C.moveTo(S,cand.shift().id,'tank'+si);n++}});
// 판매: 캐주얼은 꽉 찼을 때만, 그리디는 여유 두고 많이
const keep=style==='greedy'?3:2;S.tanks.forEach((t,i)=>{if(t.show)return;const L=C.at(S,'tank'+i).filter(f=>C.isAdult(f)&&!f.preg).sort((a,b)=>C.sellPrice(S,a)-C.sellPrice(S,b));while(C.tankUsed(S,i)>C.tankCap(S,i)-keep&&L.length>4)m.sold+=C.sell(S,L.shift().id)});
if(style==='greedy'){const L=S.fish.filter(f=>C.isAdult(f)&&!f.preg&&/^tank/.test(f.loc)&&!S.tanks[+f.loc.slice(4)].show&&!C.isParent(f)).sort((a,b)=>C.sellPrice(S,b)-C.sellPrice(S,a));L.slice(6).forEach(f=>{if(C.sellPrice(S,f)>=10)m.sold+=C.sell(S,f.id)})}
const k={casual:2,normal:1.3,greedy:1.05}[style];const maxB={casual:2,normal:4,greedy:6}[style];
const bp=C.BREED_PRICE[C.breedCount(S)];if(bp!=null&&C.breedCount(S)<maxB&&S.money>bp*k+30){if(!C.buy(S,'tank')&&C.breedCount(S)===2&&m.tank2==null)m.tank2=d}
const sc=C.showCount(S);if(sc<3){const th=C.THEMES[TH[sc]];if(S.money>th.price*(k)){const c0=S.cur;if(!C.buy(S,'show',TH[sc])){if(m.show==null)m.show=d;m.shows++}S.cur=c0}}
{const si=S.tanks.findIndex(t=>t.show);if(si>=0)for(const a of['bubble','light','back','moon'])if(S.money>C.ADDONS[a].price*2*k){const c0=S.cur;S.cur=si;C.buy(S,'addon',a);S.cur=c0}}
if(d<=40&&S.money<15)m.stuck++;if([30,90,180].includes(d))m.at[d]=Math.round(S.money)}
m.earned=Math.round(S.stats.earned);m.album=Object.keys(S.album).length;m.fish=S.fish.length;return m}
const N=+(cfg.n||24),med=a=>{const s=a.filter(x=>x!=null).sort((x,y)=>x-y);return s.length?Math.round(s[s.length>>1]):'-'};
const out=[];for(const st of['casual','normal','greedy']){const R=Array.from({length:N},()=>play(st,180));const pct=f=>Math.round(100*R.filter(f).length/N)+'%';
out.push(`${st.padEnd(6)} 2nd ${med(R.map(x=>x.tank2))} show ${med(R.map(x=>x.show))}(${pct(x=>x.show!=null)}) stuck ${pct(x=>x.stuck>=3)} $ ${[30,90,180].map(d=>med(R.map(x=>x.at[d]))).join('/')} | 번돈 ${med(R.map(x=>x.earned))} [판매 ${med(R.map(x=>x.sold))} 손님 ${med(R.map(x=>x.cust))} 의뢰 ${med(R.map(x=>x.ord))} 관리비 -${med(R.map(x=>x.up))}] 전시수 ${med(R.map(x=>x.shows))} 사진첩 ${med(R.map(x=>x.album))} 구피 ${med(R.map(x=>x.fish))}`)}
console.log('## '+(cfg.name||JSON.stringify(cfg))+'\n'+out.join('\n'));
