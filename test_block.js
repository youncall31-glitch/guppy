/* ---------- 테스트판: 새로고침할 때마다 '튜토리얼·수습을 마친 직후 + 돈 넉넉' 상태로 새로 시작 (저장 안 함) ---------- */
function testStart() {
  if (modalOpen) closeSheet();
  for (const k in SW) delete SW[k];
  const R = Math.random;
  S = C.newState(); S.intro = true; S.tutDone = true; S.tankV2 = 1; S.apV = 1; S.firstPaid = true; S.speed = 1; S.att = { last: new Date().toISOString().slice(0, 10), n: 1 };
  S.unl = null; S.goal = C.AP_N; S.grad = 1; S.divOffered = 1; S.tips = { boxes: 1, orders: 1 }; S.coach = { boxes: 1, boost: 1, known: 1, pan: 1 }; S.txSeen = {}; S.upTold = 1; S.seenBoxBirth = 1;
  S.money = 99999; S.fish = [];
  C.buy(S, 'tank'); S.boxes = 3;
  ['red', 'yellow'].forEach(c => ['m', 'f'].forEach(x => C.buyStarter(S, c, x, R)));
  for (let i = 0; i < 6; i++) C.buyFounder(S, i % 2 ? 'f' : 'm', false, R);
  for (let i = 0; i < 4; i++) C.buyFounder(S, i % 2 ? 'f' : 'm', true, R);
  S.fish.forEach((f, i) => { f.age = 8 + (i % 6) * 2; f.loc = 'tank' + (i % 2); });
  for (let d = 0; d < 6; d++) { C.dayTick(S, R); S.fish.forEach(f => { f.atRisk = false; }); }   // 며칠 지나 새끼·의뢰가 생긴 상태
  S.fish.forEach(f => { if (C.isAdult(f)) C.revealCheck(S, f, []); });
  S.money = 3000; S.cur = 0; S.clock = 0; S.log = []; rosterSig = ''; VIEW.z = 1; VIEW.cx = 0; layout(); render();
  setTimeout(() => { Q.length = 0; if (modalOpen) closeSheet(); toast('🧪 테스트판 · 새로고침하면 늘 이 상태로 다시 시작해요 (저장 안 됨)'); }, 600);
}
setTimeout(testStart, 300);
