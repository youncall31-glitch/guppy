from playwright.sync_api import sync_playwright
st=open('/home/claude/ustate/s.txt').read().strip()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    import json
    pg.add_init_script("if(!sessionStorage.x){localStorage.setItem('guppy-tycoon-v1',%s);sessionStorage.x=1}"%json.dumps(st.replace('GUPPY-STATE ','',1)))
    pg.goto('file:///home/claude/guppy/index.html');pg.wait_for_timeout(1500)
    pg.screenshot(path='dA_s.png');pg.evaluate('closeSheet()');pg.wait_for_timeout(400);pg.screenshot(path='dA0.png')
    pg.evaluate("document.querySelector('#menuBtn').click()");pg.wait_for_timeout(400);pg.screenshot(path='dA1.png')
    pg.evaluate("closeSheet&&closeSheet()");pg.wait_for_timeout(300)
    pg.evaluate("showAlbum()");pg.wait_for_timeout(400);pg.screenshot(path='dA2.png')
    pg.evaluate("showEntry(document.querySelector('.cell.no').dataset.id)");pg.wait_for_timeout(400);pg.screenshot(path='dA3.png')
    pg.evaluate("closeSheet();showShop&&showShop()");pg.wait_for_timeout(400);pg.screenshot(path='dA4.png')
    print(errs)
    b.close()
