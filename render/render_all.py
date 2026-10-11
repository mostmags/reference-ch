"""Router + renderer: turns all 48 Chase guide JSONs into HTML-blueprint screenshots."""
import json, os, subprocess, time, importlib
import chase_ui as C
from desktop import d_web, d_ur, d_brand, d_fee_table, d_locator, d_bizweb, IS_DESKTOP
importlib.reload(C)

PACKS="/Users/amanmaan/Documents/TOOLS/Screenshot Automator/cashgen-pipeline/chase-research-packs"
GUIDES="/Users/amanmaan/Documents/TOOLS/Screenshot Automator/cashgen-pipeline/guides"

# ---------- generic extra templates ----------

def t_more(highlight=None):
    rows=[("Profile &amp; settings","&#128100;"),("Alerts &amp; messages","&#128276;"),
          ("Chase Credit Journey","&#128200;"),("Contact us","&#128172;"),
          ("Find a branch or ATM","&#128205;"),("Documents","&#128196;")]
    h=""
    out=[f'<div class="content w"><div style="padding:14px 20px 0"><h1 class="s">More</h1></div><div class="rows" style="margin-top:4px">']
    for n,i in rows:
        c=""
        if highlight and highlight.lower().replace("&","&") in n.lower():
            c=" hl"; b="<b>"+n+"</b>"+'<div class="sub" style="color:#8a6d00">TAP HERE</div>'
        else:
            b=n
        out.append(f'<div class="row{c}"><span class="ico">{i}</span><div class="g">{b}</div><span class="chev">&rsaquo;</span></div>')
    out.append('</div></div>')
    return C.sb()+C.nav("More","")+ "".join(out) + C.tabbar(4) + C.sb() + '<div class="hi"></div>'

def t_profile():
    return C.sb() + C.nav("Profile &amp; Settings","","Sign out",border=True) + f'''
<div class="content w">
  <div style="display:flex;align-items:center;gap:12px;padding:16px 18px;border-bottom:1px solid var(--line)">
    <span style="width:44px;height:44px;border-radius:50%;background:#E8F1FF;color:var(--blue);display:flex;align-items:center;justify-content:center;font-weight:700">JA</span>
    <div><div style="font-size:16px;font-weight:600">Jordan Avery</div><div style="font-size:12.5px;color:var(--ink2)">Last sign in: Oct 10, 2026</div></div>
  </div>
  <div class="rows" style="margin-top:12px">
    <div class="row"><span class="ico">&#128274;</span><div class="g">Security &amp; privacy</div><span class="chev">&rsaquo;</span></div>
    <div class="row hl"><span class="ico">&#128100;</span><div class="g"><b>Personal details</b><div class="sub" style="color:#8a6d00">TAP HERE</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#9919;</span><div class="g">Sign-in preferences</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#9878;</span><div class="g">Account settings</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#128276;</span><div class="g">Alerts &amp; messages</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#128172;</span><div class="g">Help &amp; support</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#128196;</span><div class="g">Document manager</div><span class="chev">&rsaquo;</span></div>
  </div>
  <div style="display:flex;justify-content:space-between;padding:12px 20px;font-size:13.5px"><span class="lnk">Give us feedback &rsaquo;</span><span class="lnk">Legal information &rsaquo;</span></div>
</div>{C.sb()}<div class="hi"></div>'''

def t_contact():
    return C.sb() + C.nav("Contact us") + f'''
<div class="content w">
  <div class="rows" style="margin-top:12px">
    <div class="row" style="align-items:flex-start;min-height:64px"><div class="g"><b>Call us</b><div class="sub">Personal Banking: 1-800-935-9935, 24/7</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="align-items:flex-start;min-height:64px"><div class="g"><b>Secure message center</b><div class="sub">Sign in to send a secure message</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="align-items:flex-start;min-height:64px"><div class="g"><b>Chase Digital Assistant</b><div class="sub">Chat with us in the app</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="align-items:flex-start;min-height:64px"><div class="g"><b>Find a branch or ATM</b><div class="sub">Get in-person support</div></div><span class="chev">&rsaquo;</span></div>
  </div>
  <p class="body" style="font-size:12.5px;margin:14px 18px">Calling us about your account is the fastest way to reach a representative. Have your account or card details ready.</p>
</div>{C.tabbar(4)}{C.sb()}<div class="hi"></div>'''

def t_app_info(title, paras, cta=None):
    ps="".join(f'<p class="body" style="margin-bottom:12px;font-size:14px">{p}</p>' for p in paras)
    c=f'<div class="bbtns"><div class="btn" style="margin:0">{cta}</div></div>' if cta else ""
    return C.sb()+C.nav(title)+f'<div class="content w"><div style="padding:18px 20px 0">{ps}</div></div>{c}{C.sb()}<div class="hi"></div>'

def t_app_list(title, rows, highlight=None, tab=0):
    r=""
    for x in rows:
        hl=' hl' if highlight and highlight.lower() in x.lower() else ''
        b=f'<b>{x}</b>' if hl else x
        s='<div class="sub" style="color:#8a6d00">TAP HERE</div>' if hl else ''
        r+=f'<div class="row{hl}"><div class="g">{b}{s}</div><span class="chev">&rsaquo;</span></div>'
    return C.sb()+C.nav(title)+f'<div class="content w"><div class="rows" style="margin-top:12px">{r}</div></div>{C.tabbar(tab)}{C.sb()}<div class="hi"></div>'

def t_app_form(title, fields, btn="Save", note=None):
    f="".join(f'<div class="lbl">{a}</div><div class="field" style="{"color:#c6c9cd" if v.startswith("(") else ""}">{v}</div>' for a,v in fields)
    n=f'<p class="body" style="font-size:12.5px;margin:12px 20px 0">{note}</p>' if note else ""
    return C.sb()+C.nav(title)+f'<div class="content w"><div style="padding:16px 20px 0">{f}</div>{n}</div><div class="bbtns"><div class="btn" style="margin:0">{btn}</div></div>{C.sb()}<div class="hi"></div>'

def t_web(title, crumb, body, cta=None):
    c=f'<div style="margin:22px 40px 0;background:var(--blue);color:#fff;display:inline-block;padding:13px 28px;border-radius:4px;font-weight:600;font-size:15px">{cta}</div>' if cta else ""
    return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;overflow:hidden">
  <div style="background:#F6F6F6;border-bottom:1px solid var(--line);padding:10px 40px;display:flex;align-items:center;gap:14px">
    <span style="font-weight:700;font-size:17px;letter-spacing:.5px">CHASE <span style="display:inline-block;width:16px;height:16px;background:var(--brand);border-radius:3px;vertical-align:-2px"></span></span>
    <span style="color:#0060F0;font-weight:600;font-size:14px;margin-left:auto">Sign in</span>
  </div>
  <div style="padding:14px 40px 0;font-size:12.5px;color:var(--ink2)">{crumb}</div>
  <div style="padding:8px 40px 0;font-size:30px;font-weight:300">{title}</div>
  <div style="padding:14px 40px 0;font-size:14.5px;line-height:1.6;color:#3c4043;max-width:700px">{body}</div>
  {c}
</div>{C.sb()}<div class="hi"></div>'''

def t_ur(stage="signin", highlight=None):
    if stage=="signin":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="background:#F6F6F6;border-bottom:1px solid var(--line);padding:10px 40px;display:flex;align-items:center;gap:14px">
    <span style="font-weight:700;font-size:17px">CHASE <span style="display:inline-block;width:16px;height:16px;background:var(--brand);border-radius:3px;vertical-align:-2px"></span></span>
    <span style="margin-left:auto;font-size:13px;color:var(--ink2)">Easy to sign in &mdash; not enrolled? <span class="lnk">Sign up now</span></span>
  </div>
  <div style="max-width:420px;margin:40px auto 0;padding:0 20px">
    <div style="font-size:26px;font-weight:300">Sign in</div>
    <div class="lbl">Username</div><div class="field">jordan.avery4821</div>
    <div class="lbl">Password</div><div class="field" style="letter-spacing:2px">&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;</div>
    <div style="margin-top:16px;background:var(--blue);color:#fff;border-radius:4px;height:46px;display:flex;align-items:center;justify-content:center;font-weight:600">Sign in</div>
    <div style="margin-top:12px;text-align:center"><span class="lnk" style="font-size:13.5px">Forgot username/password?</span></div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage in ("home","home_menu"):
        menu = '''<div style="position:absolute;top:150px;right:40px;width:250px;background:#fff;border:1px solid var(--line);border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.15);z-index:49;padding:6px 0">
        <div style="padding:10px 16px;font-size:14px">Book travel</div>
        <div style="padding:10px 16px;font-size:14px">Points details</div>
        <div class="hl" style="padding:10px 16px;font-size:14px"><b>Transfer points to partners</b><div style="font-size:11px;color:#8a6d00;font-weight:400">TAP HERE</div></div>
        <div style="padding:10px 16px;font-size:14px">Combine points</div></div>''' if stage=="home_menu" else ""
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="background:linear-gradient(120deg,#0B57C2,#0846A8);color:#fff;padding:18px 40px;display:flex;align-items:center;gap:14px">
    <span style="font-weight:700;font-size:16px">CHASE <span style="display:inline-block;width:14px;height:14px;background:#fff;border-radius:3px;vertical-align:-2px"></span></span>
    <span style="margin-left:auto;font-size:13.5px;background:rgba(255,255,255,.15);border-radius:4px;padding:8px 14px;font-weight:600">Travel &#9662;</span>
  </div>
  <div style="padding:24px 40px 0">
    <div style="font-size:15px;color:var(--ink2)">Ultimate Rewards&reg; points balance</div>
    <div style="font-size:42px;font-weight:300;margin-top:4px">85,000</div>
    <div style="display:flex;gap:12px;margin-top:20px">
      <div style="flex:1;border:1px solid var(--line);border-radius:8px;padding:16px"><b style="font-size:14.5px">Book travel</b><div style="font-size:12.5px;color:var(--ink2);margin-top:4px">Flights, hotels, cars and more</div></div>
      <div style="flex:1;border:1px solid var(--line);border-radius:8px;padding:16px"><b style="font-size:14.5px">Transfer points</b><div style="font-size:12.5px;color:var(--ink2);margin-top:4px">Send points to airline and hotel partners</div></div>
      <div style="flex:1;border:1px solid var(--line);border-radius:8px;padding:16px"><b style="font-size:14.5px">Redeem for cash back</b><div style="font-size:12.5px;color:var(--ink2);margin-top:4px">Statement credit or deposit</div></div>
    </div>
  </div>{menu}
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="partners":
        hl=highlight or "United Airlines MileagePlus"
        airlines=["United Airlines MileagePlus","British Airways Club","Aeroplan (Air Canada)","Flying Blue (Air France-KLM)","Iberia Club","JetBlue TrueBlue","KrisFlyer (Singapore)","AerClub (Aer Lingus)","Rapid Rewards (Southwest)","Virgin Atlantic Flying Club"]
        hotels=["World of Hyatt","Marriott Bonvoy","IHG One Rewards","Wyndham Rewards"]
        ar="".join(f'<div style="display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--line);font-size:13.5px{";outline:3px solid #FFB300;outline-offset:-3px" if a==hl else ""}"><span style="width:26px;height:26px;border-radius:50%;background:#E8F1FF;flex:none"></span><span style="flex:1">{a}</span><b style="font-size:12px;color:var(--ink2)">1:1</b></div>' for a in airlines)
        hr="".join(f'<div style="display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--line);font-size:13.5px{";outline:3px solid #FFB300;outline-offset:-3px" if h==hl else ""}"><span style="width:26px;height:26px;border-radius:6px;background:#E8F1FF;flex:none"></span><span style="flex:1">{h}</span><b style="font-size:12px;color:var(--ink2)">1:1</b></div>' for h in hotels)
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;overflow:hidden">
  <div style="background:linear-gradient(120deg,#0B57C2,#0846A8);color:#fff;padding:14px 40px;font-weight:600">Transfer points to travel partners</div>
  <div style="padding:16px 40px 0;font-size:14px;font-weight:600">AIRLINE PARTNERS</div>
  <div style="margin:10px 40px 0;border:1px solid var(--line);border-radius:8px;overflow:hidden">{ar}</div>
  <div style="padding:16px 40px 0;font-size:14px;font-weight:600">HOTEL PARTNERS</div>
  <div style="margin:10px 40px 0;border:1px solid var(--line);border-radius:8px;overflow:hidden">{hr}</div>
  <div style="margin:12px 40px;font-size:11.5px;color:var(--ink2)">Points transfer in increments of 1,000. Transfers are final and cannot be reversed.</div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="transfer":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="background:linear-gradient(120deg,#0B57C2,#0846A8);color:#fff;padding:14px 40px;font-weight:600">Transfer to United Airlines MileagePlus</div>
  <div style="max-width:560px;margin:24px auto 0;padding:0 20px">
    <div style="border:1px solid var(--line);border-radius:8px;padding:18px">
      <div class="lbl" style="margin-top:0">Frequent flyer number</div><div class="field">JH48219</div>
      <div class="lbl">Points to transfer</div><div class="field" style="font-size:20px;font-weight:600;color:var(--ink)">50,000</div>
      <div style="font-size:11.5px;color:var(--ink2);margin-top:6px">In increments of 1,000 points. 1:1 transfer ratio. Transfers are final.</div>
      <div style="margin-top:14px;font-size:13px;color:var(--ink2)">Recipient: <b style="color:var(--ink)">JORDAN AVERY</b> (name must match your program account)</div>
    </div>
    <div style="margin-top:16px;background:var(--blue);color:#fff;border-radius:4px;height:46px;display:flex;align-items:center;justify-content:center;font-weight:600">Transfer points</div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="done":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="max-width:560px;margin:50px auto 0;text-align:center;padding:0 20px">
    <div class="green-check" style="margin:0 auto"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
    <div style="font-size:24px;font-weight:300;margin-top:14px">Your transfer is submitted</div>
    <p class="body" style="margin-top:10px">50,000 Ultimate Rewards&reg; points to <b>United Airlines MileagePlus</b>. Most transfers process by the next business day, but may take up to 7 business days. Transfers are final.</p>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    return t_ur("home")

def t_brand(brand, title, body, cta="Search flights"):
    brand_colors={"BA":"#075AAA","United":"#0B2C71","Aeroplan":"#C8102E","Hyatt":"#B22517","Coinbase":"#0052FF","Plaid":"#111333","PriorityPass":"#1B2A4A","Atmos":"#0B3D5C"}
    c=brand_colors.get(brand,"#333")
    return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="background:{c};color:#fff;padding:16px 40px;font-weight:700;font-size:18px">{brand}</div>
  <div style="padding:22px 40px 0;max-width:760px">
    <div style="font-size:26px;font-weight:600">{title}</div>
    <div style="margin-top:14px;display:flex;gap:10px">
      <div style="flex:1.4"><div class="lbl" style="margin-top:0">From - To</div><div class="field" style="justify-content:space-between"><span>New York (JFK) - Los Angeles (LAX)</span><span>&#8644;</span></div></div>
      <div style="flex:1"><div class="lbl" style="margin-top:0">Dates</div><div class="field">Nov 12 - Nov 19</div></div>
    </div>
    <div style="margin-top:16px;background:{c};color:#fff;display:inline-block;padding:12px 26px;border-radius:4px;font-weight:600;font-size:14.5px">{cta}</div>
    <p class="body" style="margin-top:18px;font-size:13.5px">{body}</p>
  </div>
</div>{C.sb()}<div class="hi"></div>'''

def t_coinbase(stage="link"):
    if stage=="link":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#fff">
  <div style="background:#fff;border-bottom:1px solid var(--line);padding:12px 24px;font-weight:700;color:#0052FF;font-size:17px">coinbase</div>
  <div style="padding:26px 24px 0;max-width:520px;margin:0 auto">
    <div style="font-size:22px;font-weight:600">Link your bank account</div>
    <p class="body" style="font-size:13.5px;margin-top:8px">Select your bank to connect securely with Plaid.</p>
    <div style="margin-top:16px;border:1px solid var(--line);border-radius:10px;overflow:hidden">
      <div class="hl" style="display:flex;align-items:center;gap:12px;padding:13px 16px;border-bottom:1px solid var(--line);font-size:15px"><span style="width:30px;height:30px;border-radius:6px;background:var(--brand);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px">C</span><b>Chase</b><span style="margin-left:auto;color:var(--ink3)">&rsaquo;</span></div>
      <div style="display:flex;align-items:center;gap:12px;padding:13px 16px;border-bottom:1px solid var(--line);font-size:15px;color:var(--ink2)"><span style="width:30px;height:30px;border-radius:6px;background:#F0F2F5"></span>Bank of America</div>
      <div style="display:flex;align-items:center;gap:12px;padding:13px 16px;font-size:15px;color:var(--ink2)"><span style="width:30px;height:30px;border-radius:6px;background:#F0F2F5"></span>Wells Fargo</div>
    </div>
    <div style="font-size:11.5px;color:var(--ink2);margin-top:12px">By continuing you agree to the Plaid Terms of Use and Privacy Policy.</div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="accounts":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#fff">
  <div style="background:#111333;color:#fff;padding:12px 24px;font-weight:700;font-size:16px">Plaid</div>
  <div style="padding:24px 24px 0;max-width:520px;margin:0 auto">
    <div style="font-size:19px;font-weight:600">Choose your account</div>
    <div style="margin-top:14px;border:1px solid var(--line);border-radius:10px;overflow:hidden">
      <div class="hl" style="display:flex;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--line);font-size:14.5px"><span><b>TOTAL CHECKING</b> (&hellip;4821)</span><b>$2,436.19</b></div>
      <div style="display:flex;justify-content:space-between;padding:14px 16px;font-size:14.5px;color:var(--ink2)"><span>360 Performance Savings (&hellip;8535)</span><span>$8,160.30</span></div>
    </div>
    <div style="margin-top:18px;background:#111333;color:#fff;border-radius:6px;height:46px;display:flex;align-items:center;justify-content:center;font-weight:600">Continue</div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    # buy flow
    return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#0A0B0D"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#0A0B0D;color:#fff">
  <div style="background:#0A0B0D;border-bottom:1px solid #23262d;padding:12px 24px;font-weight:700;color:#fff;font-size:17px">coinbase</div>
  <div style="padding:26px 24px 0;max-width:520px;margin:0 auto">
    <div style="font-size:13px;color:#9aa4b2">Buy</div>
    <div style="display:flex;align-items:baseline;gap:10px;margin-top:6px"><span style="font-size:44px;font-weight:600">$100</span><span style="font-size:17px;color:#9aa4b2">&#8776; 0.0015 BTC</span></div>
    <div style="margin-top:16px;border:1px solid #23262d;border-radius:10px;padding:14px 16px;font-size:14px">
      <div style="display:flex;justify-content:space-between;padding:5px 0"><span style="color:#9aa4b2">Pay with</span><span>Chase &bull;&bull;&bull;&bull;4821</span></div>
      <div style="display:flex;justify-content:space-between;padding:5px 0"><span style="color:#9aa4b2">Fee</span><span>$2.99</span></div>
      <div style="display:flex;justify-content:space-between;padding:5px 0"><span style="color:#9aa4b2">Total</span><b>$102.99</b></div>
    </div>
    <div style="margin-top:18px;background:#0052FF;border-radius:8px;height:48px;display:flex;align-items:center;justify-content:center;font-weight:600">Preview Buy</div>
  </div>
</div><div class="hi lt"></div>{C.sb(True)}'''

def t_wallet(stage="device"):
    if stage=="device":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#fff;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif">
  <div style="display:flex;justify-content:space-between;padding:12px 18px;border-bottom:1px solid var(--line);color:#007AFF"><span>Cancel</span><b>Add Card</b><b>Next</b></div>
  <div style="text-align:center;padding:22px 20px 0;font-size:21px;font-weight:600">Add to Wallet</div>
  <div style="text-align:center;font-size:13.5px;color:#6d6d72;padding:6px 44px 0">Select the device to add your Chase debit card to.</div>
  <div style="margin:24px 24px 0;border:1px solid var(--line);border-radius:12px;overflow:hidden;font-size:15px">
    <div class="hl" style="display:flex;justify-content:space-between;padding:15px 16px;border-bottom:1px solid var(--line)"><span>&#63743; iPhone</span><span style="color:#007AFF">&#10003;</span></div>
    <div style="display:flex;justify-content:space-between;padding:15px 16px;color:var(--ink2)"><span>&#63743; Apple Watch</span><span>Add</span></div>
  </div>
  <div style="margin:20px 24px;background:#007AFF;color:#fff;border-radius:11px;height:48px;display:flex;align-items:center;justify-content:center;font-weight:600">Continue</div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="adding":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#fff;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif">
  <div style="display:flex;justify-content:space-between;padding:12px 18px;border-bottom:1px solid var(--line);color:#007AFF"><span>Cancel</span><b>Adding Card</b><span style="opacity:.4">Next</span></div>
  <div style="text-align:center;padding:70px 30px 0">
    <div style="width:56px;height:56px;border:4px solid #E5E5EA;border-top-color:#007AFF;border-radius:50%;margin:0 auto"></div>
    <div style="font-size:17px;font-weight:600;margin-top:22px">Adding Card&hellip;</div>
    <div style="font-size:13.5px;color:#6d6d72;margin-top:8px">Contacting Chase to set up your card. This may take a moment.</div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="terms":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#fff;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif">
  <div style="display:flex;justify-content:space-between;padding:12px 18px;border-bottom:1px solid var(--line);color:#007AFF"><span>Cancel</span><b>Terms and Conditions</b><b>Agree</b></div>
  <div style="padding:18px 22px 0;font-size:13px;line-height:1.55;color:#3c4043">
    <b style="font-size:15px;color:#000">Apple Pay&trade; Terms and Conditions</b>
    <p style="margin-top:10px">These terms apply when you add an eligible Chase card to Apple Pay. Your card remains subject to your cardholder agreement.</p>
    <p style="margin-top:8px">A device account number is created and stored securely on your device. Your actual card number is not stored on your device or shared with merchants.</p>
    <p style="margin-top:8px">You may remove your card from Apple Pay at any time. We may suspend your use of Apple Pay if we suspect fraud or a violation of these terms.</p>
    <p style="margin-top:8px;color:#8e8e93">(Scroll continues)</p>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="default":
        return C.sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#fff;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif">
  <div style="text-align:center;padding:14px 18px;border-bottom:1px solid var(--line);font-size:17px;font-weight:600">Default Card</div>
  <div style="text-align:center;color:#6d6d72;font-size:13.5px;padding:22px 44px 0">Use your Chase debit card as the default card when you pay with Apple Pay.</div>
  <div style="width:240px;height:150px;border-radius:13px;background:linear-gradient(135deg,#0B57C2,#0846A8);margin:26px auto 0;position:relative">
    <span style="position:absolute;left:14px;top:12px;color:#fff;font-weight:700;font-size:12px">CHASE</span>
    <span style="position:absolute;left:14px;bottom:34px;color:rgba(255,255,255,.9);font-size:9.5px;letter-spacing:1px">JORDAN AVERY</span>
    <span style="position:absolute;left:14px;bottom:14px;color:#fff;font-size:12px;letter-spacing:2px">&bull;&bull;&bull;&bull; 4821</span>
  </div>
  <div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:18px 18px 0 0;padding:18px 20px 40px;box-shadow:0 -8px 30px rgba(0,0,0,.15)">
    <div style="background:#007AFF;color:#fff;border-radius:11px;height:48px;display:flex;align-items:center;justify-content:center;font-weight:600">Use as Default Card</div>
    <div class="hl" style="margin-top:12px;background:#fff;border:1px solid #d1d1d6;color:#1a1a1a;border-radius:11px;height:48px;display:flex;align-items:center;justify-content:center;font-weight:600">Not Now</div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="linked":
        return C.sb() + C.nav("Chase Debit Card (&hellip;4821)") + f'''
<div class="content w" style="background:#fff">
  <div style="display:flex;align-items:center;gap:14px;margin:20px 20px 0;border:1px solid var(--line);border-radius:12px;padding:14px 16px">
    <span style="width:64px;height:42px;border-radius:7px;background:linear-gradient(135deg,#0B57C2,#0846A8);flex:none"></span>
    <div style="flex:1"><b style="font-size:15px">DEBIT/ATM CARD (&hellip;2208)</b><div style="font-size:12.5px;color:var(--ink2)">Expires 08/29</div></div>
    <span style="display:inline-flex;align-items:center;gap:5px;background:#E5F5EA;color:#1B7A3E;border-radius:14px;padding:6px 12px;font-size:12.5px;font-weight:600">&#10003; Linked</span>
  </div>
  <div style="margin:16px 20px;background:#E8F1FF;border-radius:10px;padding:12px 14px;font-size:13px;line-height:1.5">Your card is ready for Apple Pay. Pay in stores, online and in merchant apps with your iPhone.</div>
  <div style="margin:0 20px;font-size:13.5px"><span class="lnk">Manage digital wallets &rsaquo;</span></div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''
    return t_wallet("device")

def t_digital_wallets():
    return C.sb() + C.nav("Digital wallets") + f'''
<div class="content w">
  <div style="padding:14px 20px 0"><p class="body" style="font-size:13.5px">Add your eligible Chase cards to a digital wallet and pay from your phone in stores, in apps and online.</p></div>
  <div class="rows" style="margin-top:10px">
    <div class="row hl" style="min-height:64px"><span style="font-size:20px;font-weight:600;margin-right:10px">&#63743; Pay</span><div class="g"><div class="sub">Pay with your iPhone</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="min-height:64px"><span style="width:30px;height:30px;border-radius:8px;background:#003087;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-style:italic;margin-right:12px">P</span><div class="g">PayPal<div class="sub">Pay with PayPal</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="min-height:64px"><span style="width:30px;height:30px;border-radius:50%;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;margin-right:12px">pay</span><div class="g">Paze<div class="sub">Pay at checkout online</div></div><span class="chev">&rsaquo;</span></div>
  </div>
  <div style="padding:14px 20px;font-size:12px;color:var(--ink2)">Apple Pay is available on compatible iPhone and Apple Watch devices. <span class="lnk">Learn more</span></div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''

def t_wallet_link():
    return C.sb() + C.nav("Apple Pay") + f'''
<div class="content w">
  <div style="padding:14px 20px 0"><p class="body" style="font-size:13.5px">Select the eligible card you'd like to add to Apple Pay.</p></div>
  <div style="margin:12px 16px;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:14px 16px">
    <div style="display:flex;align-items:center;gap:12px">
      <span style="width:56px;height:36px;border-radius:6px;background:linear-gradient(135deg,#0B57C2,#0846A8);flex:none"></span>
      <div><div style="font-size:14.5px;font-weight:600">Chase Debit Card</div><div style="font-size:12px;color:var(--ink2)">Total Checking (&hellip;4821) &middot; Debit</div></div>
    </div>
    <div class="hl" style="text-align:right;margin-top:10px"><span class="lnk" style="font-size:14.5px">Add to Apple Wallet</span></div>
  </div>
  <div style="margin:12px 16px;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:14px 16px">
    <div style="display:flex;align-items:center;gap:12px">
      <span style="width:56px;height:36px;border-radius:6px;background:linear-gradient(135deg,#232529,#0E1013);flex:none"></span>
      <div><div style="font-size:14.5px;font-weight:600">Freedom Unlimited</div><div style="font-size:12px;color:var(--ink2)">Credit card (&hellip;7710) &middot; Visa Signature&reg;</div></div>
    </div>
    <div style="text-align:right;margin-top:10px"><span class="lnk" style="font-size:14.5px">Add to Apple Wallet</span></div>
  </div>
  <div style="padding:10px 20px;font-size:12px;color:var(--ink2)">Your card number isn't shared with merchants and isn't stored on your device.</div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''

def t_settings_lang(stage=0):
    # Apple Settings screens
    def apple_nav(t):
        return f'<div style="display:flex;justify-content:space-between;padding:12px 18px;border-bottom:1px solid var(--line);color:#007AFF"><span>&#8249; Settings</span><b>{t}</b><span></span></div>'
    if stage==0:
        rows=["Wi-Fi","Bluetooth","Mobile Data","General &#9654;","Control Centre","Display &amp; Brightness","Home Screen","Accessibility","Wallpaper"]
        r="".join(f'<div style="display:flex;align-items:center;gap:12px;padding:13px 16px;border-bottom:1px solid var(--line);font-size:15.5px">{x}</div>' for x in rows)
        return C.sb()+f'''<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#F2F2F7"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#F2F2F7;font-family:-apple-system,'Helvetica Neue',sans-serif">
  <div style="text-align:center;padding:10px 0;font-size:20px;font-weight:600">Settings</div>
  <div style="margin:8px 16px;background:#fff;border-radius:10px;overflow:hidden">{r}</div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage==1:
        return C.sb()+f'''<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#F2F2F7"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#F2F2F7;font-family:-apple-system,'Helvetica Neue',sans-serif">
  {apple_nav("General")}
  <div style="margin:16px 16px 0;background:#fff;border-radius:10px;overflow:hidden">
    <div class="hl" style="display:flex;justify-content:space-between;padding:13px 16px;border-bottom:1px solid var(--line);font-size:15.5px"><span>Language &amp; Region</span><span style="color:var(--ink3)">English &rsaquo;</span></div>
    <div style="display:flex;justify-content:space-between;padding:13px 16px;border-bottom:1px solid var(--line);font-size:15.5px"><span>Date &amp; Time</span><span style="color:var(--ink3)">&rsaquo;</span></div>
    <div style="display:flex;justify-content:space-between;padding:13px 16px;font-size:15.5px"><span>Keyboard</span><span style="color:var(--ink3)">&rsaquo;</span></div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage==2:
        return C.sb()+f'''<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#F2F2F7"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#F2F2F7;font-family:-apple-system,'Helvetica Neue',sans-serif">
  {apple_nav("Language &amp; Region")}
  <div style="margin:16px 16px 0;background:#fff;border-radius:10px;overflow:hidden;font-size:15.5px">
    <div style="padding:13px 16px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between"><span>Preferred Language Order</span></div>
    <div style="padding:13px 16px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between"><span>&#9776; English</span></div>
    <div style="padding:13px 16px;display:flex;justify-content:space-between"><span style="color:#007AFF;font-weight:600">Add Language&hellip;</span></div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage==3:
        langs=["English (US)","Espa&ntilde;ol","Fran&ccedil;ais (France)","Deutsch","&#26085;&#26412;&#35486;","&#20013;&#25991; (&#31616;&#20307;)"]
        l="".join(f'<div style="padding:13px 16px;border-bottom:1px solid var(--line);font-size:15.5px">{x}</div>' for x in langs)
        return C.sb()+f'''<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#F2F2F7"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;background:#F2F2F7;font-family:-apple-system,'Helvetica Neue',sans-serif">
  {apple_nav("Add Language")}
  <div style="margin:16px 16px 0;background:#fff;border-radius:10px;padding:11px 14px;font-size:15px;color:var(--ink2)">&#9906; Search</div>
  <div style="margin:12px 16px 0;background:#fff;border-radius:10px;overflow:hidden">{l}</div>
</div>{C.sb()}<div class="hi"></div>'''
    return t_settings_lang(0)

def t_creditjourney(stage=0):
    if stage==0:
        return t_more("Credit Journey")
    if stage==1:
        return C.sb()+C.nav("Plan &amp; track") + f'''
<div class="content w">
  <div class="rows" style="margin-top:12px">
    <div class="row hl"><span class="ico">&#128200;</span><div class="g"><b>Free credit score</b><div class="sub" style="color:#8a6d00">TAP HERE &mdash; Chase Credit Journey&reg;</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#128176;</span><div class="g">Budgets</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#128197;</span><div class="g">Snapshots</div><span class="chev">&rsaquo;</span></div>
  </div>
</div>{C.tabbar(2)}{C.sb()}<div class="hi"></div>'''
    if stage==2:
        return C.sb()+C.nav("Chase Credit Journey&reg;") + f'''
<div class="content w">
  <div style="margin:16px 18px 0;background:#fff;border-radius:14px;box-shadow:0 1px 3px rgba(0,0,0,.08);padding:20px;text-align:center">
    <div style="font-size:13px;color:var(--ink2)">Your VantageScore&reg; 3.0 by Experian&trade;</div>
    <div style="font-size:52px;font-weight:600;margin-top:6px">720</div>
    <div style="font-size:13px;color:var(--ink2)">GOOD &nbsp;&middot;&nbsp; 300-850 range</div>
    <div style="height:10px;border-radius:6px;margin:16px 10px 0;background:linear-gradient(90deg,#E06F00,#E8C400,#2CA853)"></div>
    <div style="display:flex;justify-content:center;margin-top:10px"><span style="background:#E8F1FF;color:var(--blue);border-radius:14px;padding:6px 14px;font-size:12.5px;font-weight:600">Free &middot; won't impact your credit</span></div>
  </div>
  <div class="rows">
    <div class="row"><div class="g">Score factors</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g">Score simulator</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g">Alerts</div><span class="chev">&rsaquo;</span></div>
  </div>
</div>{C.tabbar(4)}{C.sb()}<div class="hi"></div>'''
    return t_creditjourney(0)

def t_stored_cards(stage=0):
    if stage==0:
        return C.sb()+C.nav("Stored cards") + f'''
<div class="content w">
  <div style="padding:14px 20px 0"><p class="body" style="font-size:13.5px">See places you've saved your card info online. Tap a business for details.</p></div>
  <div class="rows" style="margin-top:8px">
    <div class="row"><span class="ico">&#128722;</span><div class="g"><b>Smashburger</b><div class="sub">Card saved 3 months ago</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#127869;</span><div class="g"><b>Kiwi Kar Lube &amp; Repa</b><div class="sub">Card saved 5 months ago</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span class="ico">&#127915;</span><div class="g"><b>Streamflix</b><div class="sub">Recurring subscription &middot; monthly</div></div><span class="chev">&rsaquo;</span></div>
  </div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''
    return C.sb()+C.nav("Smashburger") + f'''
<div class="content w">
  <div style="margin:14px 18px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:14px 16px;font-size:13.5px">
    <div style="display:flex;justify-content:space-between;padding:6px 0"><span style="color:var(--ink2)">Card</span><b>Freedom Unlimited (&hellip;7710)</b></div>
    <div style="display:flex;justify-content:space-between;padding:6px 0"><span style="color:var(--ink2)">First saved</span><span>Jul 2026</span></div>
    <div style="display:flex;justify-content:space-between;padding:6px 0"><span style="color:var(--ink2)">Last used</span><span>Sep 28, 2026</span></div>
  </div>
  <div class="sec">CHARGE HISTORY</div>
  <div class="rows">
    <div class="row" style="align-items:flex-start"><div class="g">SMASHBURGER #2214</div><div style="text-align:right"><b>$14.85</b><div class="sub">Sep 28, 2026</div></div></div>
    <div class="row" style="align-items:flex-start"><div class="g">SMASHBURGER #1988</div><div style="text-align:right"><b>$11.20</b><div class="sub">Aug 24, 2026</div></div></div>
  </div>
  <div style="padding:14px 20px;font-size:13px">To manage or cancel this subscription, contact the merchant directly.</div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''

def t_zelle(stage="home"):
    if stage=="home":
        return C.sb()+C.nav("Pay bills &amp; send money with Zelle&reg;","") + f'''
<div class="content w">
  <div class="tabs"><div class="on">Pay</div><div>Payments due</div></div>
  <div style="display:flex;align-items:center;gap:10px;margin:12px 16px 0">
    <div style="flex:1;border:1px solid var(--line);border-radius:20px;height:38px;display:flex;align-items:center;padding:0 13px;font-size:13px;color:var(--ink2)">&#9906; Search your recipients</div>
    <span class="lnk" style="font-size:13.5px;font-weight:600">&#8853; Add</span>
  </div>
  <div class="sec">YOUR RECIPIENTS</div>
  <div class="rows" style="margin-top:2px">
    <div class="row"><span style="width:34px;height:34px;border-radius:50%;background:#E8F1FF;display:flex;align-items:center;justify-content:center;margin-right:12px;font-size:13px;font-weight:600">JD</span><div class="g"><b>Joe Doe</b><div class="sub">Registered with Zelle&reg;</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row"><span style="width:34px;height:34px;border-radius:50%;background:#E8F1FF;display:flex;align-items:center;justify-content:center;margin-right:12px;font-size:13px;font-weight:600">MB</span><div class="g"><b>Mike Barrett</b><div class="sub">Not registered with Zelle&reg;</div></div><span class="chev">&rsaquo;</span></div>
  </div>
  <div style="padding:14px 20px;font-size:13px;color:#3c4043">Need to send money to someone you know? Add your trusted recipients' U.S. mobile number or email address to send money. <span class="lnk">Add a recipient &rsaquo;</span></div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    if stage=="pending":
        return C.sb()+C.nav("Zelle&reg; Activity","") + f'''
<div class="content w">
  <div class="tabs"><div class="on">Activity</div><div>Scheduled</div></div>
  <div style="margin:14px 16px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:14px 16px">
    <div style="display:flex;align-items:center;gap:12px">
      <span style="width:38px;height:38px;border-radius:50%;background:#E8F1FF;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600">MB</span>
      <div style="flex:1"><b style="font-size:15px">Mike Barrett</b><div style="font-size:12.5px;color:var(--ink2)">Pending &middot; not enrolled with Zelle&reg;</div></div>
      <b style="font-size:16px">$25.00</b>
    </div>
    <div style="display:flex;gap:10px;margin-top:14px">
      <div class="hl" style="flex:1;border:1px solid var(--blue);color:var(--blue);border-radius:8px;height:42px;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600">Cancel This Payment</div>
    </div>
    <p class="body" style="font-size:11.5px;margin-top:10px">You can only cancel a payment if the person you sent money to hasn't yet enrolled with Zelle&reg;.</p>
  </div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    if stage=="cancel_ok":
        return C.sb()+C.nav("Zelle&reg; Activity") + f'''
<div class="content w">
  <div class="green-check" style="margin-top:30px"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:20px;font-weight:600;margin-top:12px">Your payment was canceled</div>
  <div style="text-align:center;font-size:13.5px;color:var(--ink2);margin-top:6px">$25.00 to Mike Barrett &middot; the money is back in TOTAL CHECKING (&hellip;4821)</div>
  <div class="bbtns"><div class="btn" style="margin:0">Done</div></div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    if stage=="welcome":
        return C.sb()+C.nav("Set Up Zelle&reg;", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:22px 20px 0">
    <div style="width:60px;height:60px;border-radius:50%;border:2px solid #6C1FD6;color:#6C1FD6;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px">zelle<sup>&reg;</sup></div>
    <div style="font-size:21px;font-weight:600">Welcome to Zelle&reg;</div>
    <p class="body" style="margin-top:8px">Set up your account to start sending and receiving money today.</p>
    <p class="body" style="font-size:12.5px;margin-top:10px"><b>Important:</b> First time receiving money from someone at another bank? It may take 1 to 2 business days for the money to arrive.</p>
  </div>
  <div style="margin:14px 20px 0;font-size:12.5px"><span class="lnk">Zelle&reg; Service Agreement and Privacy Notice &rsaquo;</span></div>
  <div style="display:flex;gap:10px;margin:12px 20px 0;align-items:flex-start"><span style="width:19px;height:19px;border-radius:4px;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;flex:none">&#10003;</span><span style="font-size:12.5px">I agree to the Zelle&reg; Service Agreement and Privacy Notice.</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="code":
        boxes="".join('<i style="width:36px;height:44px;border:1.5px solid #b9bcc2;border-radius:7px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:600;font-style:normal"></i>' for _ in range(8))
        return C.sb()+C.nav("Verify", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:24px 20px 0">
    <div style="width:52px;height:52px;border-radius:12px;background:#E8F1FF;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;font-size:22px">&#128274;</div>
    <div style="font-size:19px;font-weight:600">We texted you a one-time code</div>
    <div style="font-size:13px;color:var(--ink2);margin-top:6px">Enter your one-time code.</div>
    <div style="display:flex;gap:7px;justify-content:center;margin:20px 0 0">{boxes}</div>
    <div style="font-size:13px;margin-top:16px">Didn't receive it? <span class="lnk">Get another code &rsaquo;</span></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="ok":
        return C.sb()+C.nav("Confirmation") + f'''
<div class="content w" style="background:#fff">
  <div class="green-check"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:21px;font-weight:600;margin-top:12px">You're all set!</div>
  <div style="text-align:center;font-size:13px;color:var(--ink2);margin-top:6px">Now you can send and request money using</div>
  <div style="text-align:center;font-size:14px;font-weight:600;margin-top:8px">JORDAN AVERY<br><span style="font-weight:400;color:var(--ink2);font-size:12.5px">Mobile &bull;&bull;&bull; &bull;&bull;&bull; 4821 &middot; CHECKING (&hellip;4821)</span></div>
  <div class="rows" style="margin-top:16px">
    <div class="row"><div class="g">Show the Zelle&reg; QR code</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g"><b>Add more Zelle&reg; IDs</b><div class="sub">You can add 1 U.S. mobile number and up to 4 emails.</div></div><span class="chev">&rsaquo;</span></div>
  </div>
  <div class="bbtns" style="bottom:20px"><div class="btn" style="margin:0">Send or request money</div><div class="btn gray" style="margin:10px 16px">Done</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="safe":
        return C.sb()+C.nav("Stay Safe from Scams") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:20px 24px 0"><div style="width:54px;height:54px;border-radius:12px;background:linear-gradient(135deg,#2B5BD7,#173B8C);margin:0 auto 12px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px">&#128737;</div>
  <div style="font-size:19px;font-weight:600;line-height:1.35">For your protection, we don't let you pay someone you've indicated that you only know through social media.</div></div>
  <div style="margin:16px 20px 0;font-size:12.5px;color:var(--ink2)">Based on JPMorganChase internal data, a significant number of Zelle&reg; scam claims involve contact with scammers on social media.</div>
  <div style="margin:14px 20px 0;background:#EFEFFF;border-radius:10px;padding:12px 14px;font-size:12.5px;line-height:1.55"><b>Here are tips to help you avoid scams:</b>
  <div style="margin-top:6px">&bull; Be cautious if a buyer wants you to put money upfront for anything.</div>
  <div style="margin-top:4px">&bull; Don't buy anything without seeing it in person.</div>
  <div style="margin-top:4px">&bull; If someone pressures you to act fast, slow down.</div></div>
  <div style="margin:14px 20px 0;font-size:12.5px">I acknowledge that I've read the above.</div>
  <div class="bbtns"><div class="btn" style="margin:0">Got it</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="add":
        return C.sb()+C.nav("Add Recipient", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0">
    <div class="lbl" style="margin-top:0">Recipient Name</div><div class="field">Name</div>
    <div style="display:flex;gap:14px;margin:12px 0 0;font-size:13px"><span class="lnk">&#128241; Add from phone contacts</span><span class="lnk">&#9635; Scan QR code</span></div>
    <div style="font-size:12.5px;font-weight:600;color:var(--ink2);margin:16px 0 2px">Enter at least 1 of the below:</div>
    <div class="lbl">Recipient's mobile number</div><div class="field" style="color:#c6c9cd">e.g. 5555555555</div>
    <div class="lbl">Recipient's email address</div><div class="field" style="color:#c6c9cd">example: email@domain.com</div>
    <div class="lbl">Recipient's Zelle&reg; tag <span style="font-weight:400">(available for businesses)</span></div><div class="field" style="color:#c6c9cd">e.g. business-zelle-tag.co</div>
  </div>
  <div style="margin:12px 20px 0;font-size:11.5px;color:var(--ink2)">Chase doesn't provide a process for you to request or recall a Zelle&reg; payment from the recipient. Zelle&reg; payments are like paying with cash &mdash; make sure you trust who you're sending to.</div>
  <div class="bbtns"><div class="btn" style="margin:0">Add Recipient</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="amount":
        return C.sb()+C.nav("Enter Amount", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="display:flex;align-items:center;gap:12px;padding:14px 20px;border-bottom:1px solid var(--line)">
    <span style="width:40px;height:40px;border-radius:50%;background:#E8F1FF;display:flex;align-items:center;justify-content:center;font-weight:600">JD</span>
    <div style="flex:1"><b style="font-size:15px">Joe Doe</b><div style="font-size:12px;color:var(--ink2)">Registered as: personal account &middot; Zelle&reg; ID active since Apr 2026</div></div>
  </div>
  <div style="text-align:center;margin-top:18px"><div style="font-size:12.5px;color:var(--ink2)">Amount</div>
  <div style="font-size:34px;font-weight:600;margin-top:4px">$0<span style="color:#c6c9cd">.00</span></div>
  <div style="font-size:12px;color:var(--ink2);margin-top:8px">Today's limit for this recipient is $500.00 &nbsp;<span class="lnk">Learn more &rsaquo;</span></div></div>
  <div style="margin:16px 20px 0;font-size:13.5px">
    <div class="lbl" style="margin-top:0">Message to recipient <span style="font-weight:400">(required)</span></div><div class="field" style="color:#c6c9cd">What's this for? <span style="margin-left:auto;font-size:11px">146 characters remaining</span></div>
    <div style="padding:11px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Pay from</div><div style="margin-top:3px"><b>TOTAL CHECKING (&hellip;4821)</b> <span style="color:var(--ink2);font-size:12px">$2,436.19</span> &#9662;</div></div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:11px 0;border-bottom:1px solid var(--line)"><div><div style="font-size:12px;color:var(--ink2)">Send on</div><div style="margin-top:3px">Today &#9662;</div></div></div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:11px 0"><span style="font-size:13.5px">Repeat payment</span><span style="width:40px;height:24px;border-radius:12px;background:#d5d8dc;position:relative"><span style="position:absolute;top:2px;left:2px;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.2)"></span></span></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Review &amp; send</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="confirm":
        return C.sb()+C.nav("Confirmation") + f'''
<div class="content w" style="background:#fff">
  <div class="green-check"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:20px;font-weight:600;margin-top:12px;line-height:1.35">We're sending your money now.<br>Mike Barrett will get it in a few minutes.</div>
  <div style="text-align:center;font-size:30px;font-weight:600;margin-top:12px">$5.00</div>
  <div style="text-align:center;font-size:12.5px;color:var(--ink2);margin-top:6px">Joe Doe &middot; Registered as: personal account</div>
  <div style="margin:18px 20px 0;background:#EFEFFF;border-radius:10px;padding:12px 14px;font-size:12.5px;line-height:1.5">Set up a Siri shortcut, such as "Pay Joe," to save time when sending money. <span class="lnk">Add to Siri &#63743;</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Done</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="qr":
        return C.sb()+C.nav("Scan Or Share Code","") + f'''
<div class="content w">
  <div class="tabs"><div>Scan</div><div class="on">My code</div></div>
  <div style="text-align:center;padding:18px 20px 0">
    <div style="font-size:14px;font-weight:600">JORDAN AVERY</div>
    <div style="font-size:12px;color:var(--ink2);margin-top:2px">TOTAL CHECKING (&hellip;4821)</div>
    <div style="width:170px;height:170px;margin:16px auto 0;background:
      repeating-linear-gradient(0deg,#1a1a1a 0 6px,#fff 6px 12px),
      repeating-linear-gradient(90deg,#1a1a1a 0 6px,#fff 6px 12px);background-blend-mode:multiply;border-radius:10px"></div>
    <div style="margin-top:14px"><span style="font-weight:700;color:#6C1FD6;font-style:italic">zelle</span><sup>&reg;</sup></div>
    <div style="font-size:12px;color:var(--ink2);margin-top:8px">Tap code to hide personal info</div>
    <div style="display:flex;gap:26px;justify-content:center;margin-top:12px;color:var(--blue);font-size:15px">&#9993; &#128247; &#128279;</div>
  </div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    return t_zelle("home")

def t_dispute(stage="options"):
    if stage=="details":
        items=[("ZELLE PAYMENT TO BEIBE JPMPW6Z3XKAK","Jun 30, 2026","-$5.00","$61.50"),
               ("KIWI KAR LUBE &amp; REPA THE WOODLANDS TX (6/29)","Jul 01, 2026","-$18.50","$61.50"),
               ("ATM CASH DEPOSIT 06/29 1010 THE WOODLANDS PKWY","Jun 25, 2026","$50.00","$80.00")]
        rows="".join(f'<div style="display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid var(--line);font-size:12.5px"><span style="flex:1;padding-right:10px">{n}<div style="color:var(--ink2);font-size:11.5px;margin-top:2px">{d}</div></span><span style="text-align:right"><b>{a}</b><div style="color:var(--ink2);font-size:11.5px">{b}</div></span></div>' for n,d,a,b in items)
        return C.sb()+C.nav("TOTAL CHECKING (&hellip;4821)") + f'''
<div class="content w">
  <div style="padding:12px 18px 0;font-size:15.5px;font-weight:600">See all transactions</div>
  <div style="margin:6px 16px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:6px 16px">{rows}</div>
  <div style="margin:14px 16px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:14px 16px">
    <div style="font-size:14px;line-height:1.45"><b>Having a problem with this transaction?</b> Let's look into it.</div>
    <div class="hl" style="margin-top:8px;text-align:right"><span class="lnk" style="font-size:14px">Report a problem</span></div>
  </div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''
    if stage=="options":
        opts=["I returned or canceled a one-time purchase and haven't received a credit.",
              "I never received the product or service or received it late.",
              "I'm dissatisfied with the quality of the product or service I received.",
              "I was charged a higher amount than expected.",
              "I made this purchase, but it was paid for more than once.",
              "I did not make this purchase."]
        o="".join(f'<div style="display:flex;gap:12px;padding:13px 0;border-bottom:1px solid var(--line);font-size:13.5px;line-height:1.45"><span style="width:19px;height:19px;border-radius:50%;border:2px solid #b9bcc2;flex:none;margin-top:2px"></span><span style="flex:1">{x}{"<div style=\'font-size:12px;color:#BF2155;margin-top:4px\'>If you didn\'t authorize this purchase, you can lock or cancel your card to prevent more suspicious activity.</div>" if "did not make" in x else ""}</span></div>' for x in opts)
        return C.sb()+C.nav("Report a Problem", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0"><h1 class="s" style="font-size:21px">What doesn't look right with this transaction?</h1>
  <p class="body" style="font-size:13px">Choose the scenario that best describes what happened.</p></div>
  <div style="margin:8px 20px 0">{o}</div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="sure":
        return C.sb()+C.nav("Report a Problem") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0"><h1 class="s" style="font-size:21px">Are you sure this option best fits your situation?</h1></div>
  <div style="margin:6px 20px 0;font-size:13.5px;line-height:1.55">
    <b>Choose this option if:</b>
    <div style="margin-top:5px">&bull; You canceled or returned a one-time purchase and you haven't received a refund. Keep in mind, some refunds may show up on your statement under a different merchant name.</div>
    <div style="margin-top:12px"><b>Choose a different option if:</b></div>
    <div style="margin-top:5px">&bull; You returned merchandise that's defective or not as you expected.</div>
  </div>
  <div class="bbtns" style="bottom:20px"><div class="btn" style="margin:0">Yes, I'm sure</div><div style="text-align:center;margin-top:10px"><span class="lnk" style="font-size:14px">Go back</span></div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="call":
        return C.sb()+C.nav("Report a Problem") + f'''
<div class="content w" style="background:#fff">
  <div style="margin:20px 18px 0;background:#FDEEEA;border:1px solid #F5C9BE;border-radius:10px;padding:14px 16px;font-size:14px;line-height:1.55;color:#8C2F17">&#9888; Please call us at <b>1-866-564-2262</b> to complete your claim.</div>
  <div class="bbtns"><div class="btn" style="margin:0">Done</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    return t_dispute("options")

def t_pin():
    return C.sb()+C.nav("Get a new PIN", action="Close") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0">
    <h1 class="s" style="font-size:21px">Need a new PIN?</h1>
    <p class="body" style="font-size:13.5px">Tell us your card number and we'll create a new PIN for you. You should receive it in the mail in 5 to 7 business days. To set your own PIN, visit a Chase branch.</p>
  </div>
  <div class="sec" style="padding-left:20px">Account</div>
  <div style="margin:0 20px;font-size:14px;font-weight:600;border-bottom:1px solid var(--line);padding-bottom:9px">TOTAL CHECKING (&hellip;4821)</div>
  <div style="margin:14px 20px 0">
    <div class="lbl" style="margin-top:0">Debit/ATM card number</div>
    <div class="field" style="justify-content:space-between"><span>16-digit card number</span><span style="color:var(--blue);font-size:13px">Show</span></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Request PIN</div></div>
</div>{C.sb()}<div class="hi"></div>'''

def t_secpriv():
    return C.sb()+C.nav("Security &amp; Privacy Center") + f'''
<div class="content w">
  <div style="margin:12px 16px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:14px 16px">
    <div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:15px">Report fraud</b><span style="background:var(--blue);color:#fff;border-radius:5px;padding:7px 13px;font-size:12.5px;font-weight:600">Contact us</span></div>
    <div style="font-size:12.5px;color:var(--ink2);margin-top:5px">Help protect your accounts and flag suspicious activity.</div>
  </div>
  <div class="sec">QUICK ACTIONS</div>
  <div style="display:flex;gap:8px;padding:0 16px">
    <div style="flex:1;background:#fff;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:12px 6px;font-size:11.5px;font-weight:600;text-align:center"><span style="color:var(--blue);font-size:17px;display:block;margin-bottom:5px">&#128274;</span>Lock/unlock card</div>
    <div style="flex:1;background:#fff;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:12px 6px;font-size:11.5px;font-weight:600;text-align:center"><span style="color:var(--blue);font-size:17px;display:block;margin-bottom:5px">&#128179;</span>Replace a card</div>
    <div style="flex:1;background:#fff;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:12px 6px;font-size:11.5px;font-weight:600;text-align:center"><span style="color:var(--blue);font-size:17px;display:block;margin-bottom:5px">&#8226;&bull;&bull;&bull;</span>Request a new PIN</div>
  </div>
  <div class="sec">ENHANCE YOUR SECURITY</div>
  <div style="margin:0 16px;font-size:13px;color:var(--ink2);padding:0 2px 6px">Here are some ways you can make your accounts more secure.</div>
  <div class="rows">
    <div class="row" style="align-items:flex-start"><div class="g"><b>Manage the passkeys and security keys associated with your profile.</b></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="align-items:flex-start"><div class="g"><b>Enable 2-step verification for extra security at sign-in.</b></div><span class="chev">&rsaquo;</span></div>
  </div>
</div>{C.tabbar(4)}{C.sb()}<div class="hi"></div>'''

def t_twofa():
    return C.sb()+C.nav("Extra Security at Sign In") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0"><h1 class="s" style="font-size:22px">Update Your Settings</h1>
  <p class="body" style="font-size:13.5px">Customize your sign in experience. You can update these choices any time.</p></div>
  <div style="margin:14px 20px 0;font-size:14px;font-weight:600">Security Settings</div>
  <div style="margin:8px 20px 0;border-top:1px solid var(--line)">
    <div style="display:flex;align-items:center;gap:12px;padding:14px 0;border-bottom:1px solid var(--line)">
      <div style="flex:1;font-size:14px">Use 2-Step verification every time you sign in on a browser</div>
      <span style="width:42px;height:25px;border-radius:13px;background:var(--blue);position:relative;flex:none"><span style="position:absolute;top:2px;right:2px;width:21px;height:21px;border-radius:50%;background:#fff"></span></span>
    </div>
    <div style="display:flex;align-items:center;gap:12px;padding:14px 0;border-bottom:1px solid var(--line)">
      <div style="flex:1;font-size:14px">Receive one-time codes by email</div>
      <span style="width:42px;height:25px;border-radius:13px;background:#d5d8dc;position:relative;flex:none"><span style="position:absolute;top:2px;left:2px;width:21px;height:21px;border-radius:50%;background:#fff"></span></span>
    </div>
  </div>
  <div style="margin:16px 20px 0;font-size:13.5px;color:var(--blue);font-weight:600">&#9654; How Extra Security at Sign In protects you</div>
</div>{C.sb()}<div class="hi"></div>'''

def t_password():
    return C.sb()+C.nav("Password") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0"><p class="body" style="font-size:13px">Make sure your password is unique to this account. Keep it different from the ones you use on other sites or apps and it's pointless.</p></div>
  <div style="margin:8px 20px 0">
    <div class="lbl" style="margin-top:0">Current</div><div class="field" style="letter-spacing:2px">&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;</div>
    <div class="lbl">New</div><div class="field" style="color:#c6c9cd">Enter new password</div>
    <div class="lbl">Confirm</div><div class="field" style="color:#c6c9cd">Confirm new password</div>
  </div>
  <div style="margin:14px 20px 0;font-size:13.5px;color:var(--blue);font-weight:600">&#9654; Password help</div>
  <div class="bbtns"><div class="btn" style="margin:0">Save</div></div>
</div>{C.sb()}<div class="hi"></div>'''

def t_ext(stage="find"):
    if stage=="find":
        banks=["Bank of America","Wells Fargo","Navy Federal Credit Union","TD Bank","Ally Bank","Citibank","Capital One","USAA"]
        r="".join(f'<div style="display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--line);font-size:14.5px"><span style="width:30px;height:30px;border-radius:50%;background:#E8F1FF;flex:none"></span><div style="flex:1"><b>{b}</b><div style="font-size:11px;color:var(--ink2)">www.{b.split()[0].lower()}.com</div></div><span class="chev">&rsaquo;</span></div>' for b in banks)
        return C.sb()+C.nav("Add an external account", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 18px 0"><div style="font-size:18px;font-weight:600">Find your external financial institution</div>
  <div style="font-size:12px;color:var(--ink2);margin-top:3px">Bank or credit union name</div>
  <div class="field" style="margin-top:6px">&#9906; Search for an institution</div></div>
  <div style="margin:12px 16px 0;border:1px solid var(--line);border-radius:10px;overflow:hidden">{r}</div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    if stage=="how":
        return C.sb()+C.nav("Add an external account", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 18px 0;font-size:17px;font-weight:600;line-height:1.35">Choose how you want to add your checking or savings account</div>
  <div style="margin:12px 18px 0;font-size:12px;color:var(--ink2)">Choose an option</div>
  <div style="margin:8px 18px 0;border:1.5px solid var(--blue);border-radius:12px;padding:12px 14px">
    <div style="display:flex;gap:10px"><span style="width:18px;height:18px;border-radius:50%;border:6px solid var(--blue);flex:none"></span><div><b style="font-size:14.5px">Sign in to Capital One</b><div style="font-size:12px;color:var(--ink2);margin-top:2px">Use your bank's username and password to add your account.</div></div></div>
  </div>
  <div style="margin:10px 18px 0;border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:flex;gap:10px"><span style="width:18px;height:18px;border-radius:50%;border:2px solid #b9bcc2;flex:none"></span><div><b style="font-size:14.5px">Fill in your account info yourself</b><div style="font-size:12px;color:var(--ink2);margin-top:2px">Add using your account and routing numbers.</div></div></div>
  <div style="margin:14px 18px 0;font-size:12.5px;color:var(--ink2)"><b style="color:var(--ink)">Data you'll share</b> We collect, use and retain only what is necessary: <span class="lnk">Account details</span></div>
  <div style="margin:10px 18px 0;font-size:12.5px;color:var(--ink2)"><b style="color:var(--ink)">Terms and conditions</b> Review our terms and conditions to learn how we partner with Yodlee, our data access provider. <span style="color:var(--ok)">&#10003; You accepted our terms and conditions.</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    if stage=="select":
        rows=[("360 Performance Savings (&hellip;8535)","SAVINGS"),("360 Performance Savings (&hellip;0759)","SAVINGS"),("Quicksilver (&hellip;7017)","CREDIT CARD")]
        r="".join(f'<div style="display:flex;align-items:center;gap:12px;padding:13px 16px;border-bottom:1px solid var(--line);font-size:13.5px"><span style="width:19px;height:19px;border:2px solid #b9bcc2;border-radius:4px;flex:none"></span><div><b>{a}</b><div style="font-size:11px;color:var(--ink2)">{b}</div></div></div>' for a,b in rows)
        return C.sb()+f'''<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--line)"><span style="color:var(--ink2)">&#10005;</span><span style="background:#EDEFF2;border-radius:6px;padding:6px 12px;font-size:13px;color:var(--ink2)">&#128279; consent.capitalone.com</span></div>
  <div style="padding:16px 18px 0;font-size:16px;font-weight:600">Choose an account to connect</div>
  <div style="margin:12px 18px 0;border:1px solid var(--line);border-radius:10px;overflow:hidden">{r}</div>
  <div style="display:flex;gap:10px;margin:16px 18px 0"><div style="flex:1;border:1px solid var(--line);border-radius:6px;height:44px;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:14px">Back</div><div style="flex:1;background:var(--blue);color:#fff;border-radius:6px;height:44px;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:14px">Continue</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage=="nickname":
        return C.sb()+C.nav("Add an external account", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 18px 0;font-size:17px;font-weight:600;line-height:1.35">Choose an account you'd like to add.</div>
  <div style="margin:12px 18px 0;font-size:12.5px;color:var(--ink2);line-height:1.5">Balance transfer checks, as well as some money market accounts and savings accounts, may not be eligible for external money transfers. Please ask your financial institution if you're not sure if your account is eligible.</div>
  <div class="sec" style="padding-left:0">Capital One</div>
  <div style="margin:0 18px;font-size:13.5px">
    <div style="padding:8px 0;border-bottom:1px solid var(--line)"><b>360 Performance Savings (&hellip;8535)</b></div>
    <div class="lbl" style="margin-top:10px">Account nickname</div>
    <div class="field">360 Performance Savings</div>
    <div style="font-size:11.5px;color:var(--ink2);margin-top:5px">6 of 32 characters remaining. Fill in a nickname, so you can easily identify your account.</div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    if stage=="ok":
        return C.sb()+C.nav("Manage External Accounts") + f'''
<div class="content w">
  <div style="margin:14px 16px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:16px;text-align:center">
    <div class="green-check" style="margin:0 auto;width:52px;height:52px"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
    <b style="font-size:16px;display:block;margin-top:10px">You have verified and added this external account</b>
    <div style="font-size:12.5px;color:var(--ink2);margin-top:5px">Routing number &bull;&bull;&bull;&bull;&bull;8535 &middot; Status: Active &middot; Confirmation #C448217903</div>
  </div>
  <div class="sec">MY EXTERNAL ACCOUNTS (1)</div>
  <div class="rows"><div class="row"><div class="g"><b>360 Performance Savings</b><div class="sub">Personal SAVING&hellip;8535</div></div><span class="chev">&rsaquo;</span></div></div>
  <div style="padding:4px 16px 0"><div class="btn" style="margin:0">Add an external account</div></div>
</div>{C.tabbar(1)}{C.sb()}<div class="hi"></div>'''
    return t_ext("find")

def t_payct(title, body, cta=None, rows=None):
    r=""
    if rows:
        r='<div class="rows">'+''.join(f'<div class="row"><div class="g">{a}<div class="sub">{b}</div></div><span class="chev">&rsaquo;</span></div>' for a,b in rows)+'</div>'
    c=f'<div style="padding:4px 16px 0"><div class="btn" style="margin:0">{cta}</div></div>' if cta else ""
    return C.sb()+C.nav(title)+f'<div class="content w"><div style="padding:14px 20px 0">{body}</div></div>{r}{c}{C.sb()}<div class="hi"></div>'

def t_autopay(stage=0):
    if stage==0:
        return C.sb()+C.nav("Freedom Unlimited (&hellip;7710)") + f'''
<div class="content w">
  <div style="padding:12px 20px 0"><div style="font-size:31px;font-weight:600">$418.77</div><div style="font-size:12.5px;color:var(--ink2);margin-top:2px">Current balance</div></div>
  <div class="rows" style="margin-top:10px"><div class="row"><div class="g">See statements</div><span class="chev">&rsaquo;</span></div><div class="row"><div class="g">Show details</div><span class="chev">&rsaquo;</span></div></div>
  <div style="margin:10px 16px;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:14px 16px">
    <div style="display:flex;justify-content:space-between;align-items:center"><div><b style="font-size:14.5px">Automatic payments</b><div style="font-size:12px;color:var(--ink2)">On &middot; Auto pay full balance</div></div><span class="lnk" style="font-size:14px">Manage</span></div>
  </div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''
    if stage==1:
        return C.sb()+C.nav("Automatic payments") + f'''
<div class="content w">
  <div style="margin:14px 16px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:16px;font-size:13.5px">
    <div style="display:flex;padding:6px 0"><span style="width:130px;color:var(--ink2)">Payment type</span><span>Auto pay full balance</span></div>
    <div style="display:flex;padding:6px 0"><span style="width:130px;color:var(--ink2)">Pay from</span><span>TOTAL CHECKING (&hellip;4821)</span></div>
    <div style="display:flex;padding:6px 0"><span style="width:130px;color:var(--ink2)">Send on</span><span>Due date each month</span></div>
  </div>
  <div class="bbtns" style="bottom:20px"><div class="btn" style="margin:0">Edit</div><div style="text-align:center;margin-top:10px"><span class="lnk" style="font-size:14px">Turn automatic payments off</span></div></div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage==2:
        return C.sb()+C.nav("Automatic payments") + f'''
<div class="content w">
  <div class="green-check" style="margin-top:36px"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:20px;font-weight:600;margin-top:12px">Automatic payments turned off</div>
  <div style="text-align:center;font-size:13.5px;color:var(--ink2);margin-top:6px">You'll need to pay your balance manually each month.</div>
  <div class="bbtns"><div class="btn" style="margin:0">Done</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    return t_autopay(0)

def t_loan(stage=0):
    if stage==0:
        return C.sb()+C.nav("Freedom Unlimited (&hellip;7710)") + f'''
<div class="content w">
  <div style="padding:12px 20px 0"><div style="font-size:31px;font-weight:600">$418.77</div><div style="font-size:12.5px;color:var(--ink2);margin-top:2px">Current balance</div></div>
  <div class="rows" style="margin-top:10px">
    <div class="row hl"><div class="g"><b>Pay over time</b><div class="sub" style="color:#8a6d00">TAP HERE</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g">My Chase Loan</div><span class="chev">&rsaquo;</span></div>
  </div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''
    if stage==1:
        return C.sb()+C.nav("My Chase Loan") + f'''
<div class="content w">
  <div style="margin:14px 16px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:16px">
    <div style="font-size:15.5px;font-weight:600">Your available loan offer</div>
    <div style="font-size:29px;font-weight:600;margin-top:6px">Up to $4,000.00</div>
    <div style="font-size:12.5px;color:var(--ink2);margin-top:5px">No application or credit check needed &middot; funds in 1-2 business days &middot; fixed monthly payments at a lower APR than cash advances</div>
  </div>
  <div style="padding:4px 16px 0"><div class="btn" style="margin:0">Request a loan</div></div>
</div>{C.tabbar(0)}{C.sb()}<div class="hi"></div>'''
    if stage==2:
        return C.sb()+C.nav("My Chase Loan") + f'''
<div class="content w" style="background:#fff">
  <div style="margin:14px 20px 0">
    <div class="lbl" style="margin-top:0">Request amount</div><div class="field" style="font-size:20px;font-weight:600;color:var(--ink)">$2,000.00</div>
    <div class="lbl">Purpose</div><div class="field" style="justify-content:space-between"><span>Debt consolidation</span><span>&#9662;</span></div>
    <div class="lbl">Monthly payment plan</div>
    <div style="border:1.5px solid var(--blue);border-radius:10px;padding:12px 14px;font-size:13.5px"><b>12 months &middot; $174.15/mo</b><div style="font-size:12px;color:var(--ink2);margin-top:3px">16.49% APR &middot; total $2,089.80</div></div>
    <div style="border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:13.5px;margin-top:10px"><b>24 months &middot; $99.20/mo</b><div style="font-size:12px;color:var(--ink2);margin-top:3px">16.49% APR &middot; total $2,380.80</div></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Continue</div></div>
</div>{C.sb()}<div class="hi"></div>'''
    return t_loan(0)

def t_trade(stage=0):
    if stage==0:
        return C.sb()+C.nav("Trade") + f'''
<div class="content w" style="background:#fff">
  <div style="margin:14px 20px 0">
    <div class="lbl" style="margin-top:0">Symbol</div><div class="field" style="justify-content:space-between"><span><b>VOO</b> &middot; Vanguard S&amp;P 500 ETF</span><span>&#9662;</span></div>
    <div style="display:flex;background:#EDEFF2;border-radius:8px;padding:3px;margin-top:14px">
      <div style="flex:1;text-align:center;padding:8px 0;font-size:13.5px;color:var(--ink2);border-radius:6px">Shares</div>
      <div class="hl" style="flex:1;text-align:center;padding:8px 0;font-size:13.5px;font-weight:600;background:#fff;border-radius:6px;box-shadow:0 1px 3px rgba(0,0,0,.12)">Dollars</div>
    </div>
    <div class="lbl">Amount in dollars</div><div class="field" style="font-size:22px;font-weight:600;color:var(--ink)">$25.00</div>
    <div style="font-size:11.5px;color:var(--ink2);margin-top:6px">Fractional shares start with $5, regardless of the share price. Market order.</div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{C.tabbar(4)}{C.sb()}<div class="hi"></div>'''
    if stage==1:
        return C.sb()+C.nav("Preview") + f'''
<div class="content w" style="background:#fff">
  <div style="margin:14px 20px 0;font-size:13.5px">
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Order</span><b>Buy VOO</b></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Amount</span><span>$25.00 &middot; market</span></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Estimated shares</span><span>0.04386</span></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Commission</span><span>$0.00</span></div>
    <div style="display:flex;padding:8px 0"><span style="width:130px;color:var(--ink2)">Settlement</span><span>Nov 14, 2026</span></div>
  </div>
  <p class="body" style="font-size:11.5px;margin:10px 20px 0">Fractional share positions cannot be transferred and may not carry voting rights.</p>
  <div class="bbtns"><div class="btn" style="margin:0">Submit order</div></div>
</div>{C.tabbar(4)}{C.sb()}<div class="hi"></div>'''
    return t_trade(0)

def t_bizweb(stage=0):
    def bh(t):
        return f'''<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0;overflow:hidden">
  <div style="background:#0D2E6B;color:#fff;padding:13px 40px;display:flex;align-items:center;gap:12px;font-size:15px"><b style="font-size:15px">CHASE for Business</b><span style="margin-left:auto">&#128100; Jordan Avery</span></div>
  <div style="padding:20px 40px 0;font-size:26px;font-weight:300">{t}</div>'''
    if stage==0:
        return C.sb()+bh("Profile and settings")+'''
  <div style="margin:18px 40px 0;border:1px solid var(--line);border-radius:8px;overflow:hidden;font-size:14.5px;max-width:640px">
    <div style="padding:13px 16px;border-bottom:1px solid var(--line)">Personal details</div>
    <div style="padding:13px 16px;border-bottom:1px solid var(--line)">Alerts</div>
    <div class="hl" style="padding:13px 16px;border-bottom:1px solid var(--line)"><b>Account settings</b><div style="font-size:11px;color:#8a6d00;font-weight:600">TAP HERE</div></div>
    <div style="padding:13px 16px">Security preferences</div>
  </div>
</div>'''+C.sb()+'<div class="hi"></div>'
    if stage==1:
        return C.sb()+bh("Account settings")+'''
  <div style="margin:18px 40px 0;border:1px solid var(--line);border-radius:8px;overflow:hidden;font-size:14.5px;max-width:640px">
    <div style="padding:13px 16px;border-bottom:1px solid var(--line)">Account display preferences</div>
    <div class="hl" style="padding:13px 16px;border-bottom:1px solid var(--line)"><b>Manage linked accounts</b><div style="font-size:11px;color:#8a6d00;font-weight:600">TAP HERE</div></div>
    <div style="padding:13px 16px">Authorized signers</div>
  </div>
</div>'''+C.sb()+'<div class="hi"></div>'
    if stage==2:
        return C.sb()+bh("Manage linked accounts")+'''
  <div style="margin:18px 40px 0;max-width:640px;font-size:14.5px">
    <p style="color:#3c4043;font-size:14px">Choose how your accounts appear when you sign in.</p>
    <div style="margin-top:14px;border:1.5px solid var(--blue);border-radius:8px;padding:14px 16px"><b>Show my accounts</b><div style="font-size:12.5px;color:var(--ink2);margin-top:3px">Personal and business accounts appear together in one profile.</div></div>
    <div style="margin-top:10px;border:1px solid var(--line);border-radius:8px;padding:14px 16px">Link a business relationship</div>
    <div style="margin-top:16px;background:var(--blue);color:#fff;display:inline-block;padding:12px 26px;border-radius:4px;font-weight:600;font-size:14.5px">Continue</div>
  </div>
</div>'''+C.sb()+'<div class="hi"></div>'
    if stage==3:
        return C.sb()+bh("Accounts linked")+f'''
  <div style="margin:18px 40px 0;max-width:640px;background:#EFF6EF;border:1px solid #BFE3C6;border-radius:8px;padding:16px;font-size:14.5px">
    <b>&#10003; Your business relationship was linked.</b>
    <div style="margin-top:6px;font-size:13px;color:#2E5E36">CHASE BUSINESS COMPLETE CHECKING (&hellip;3117) now appears with your personal accounts in Chase Mobile and on chase.com.</div>
  </div>
</div>'''+C.sb()+'<div class="hi"></div>'
    return t_bizweb(0)

def t_fee_table():
    body='''<p>Chase Total Checking&reg; has a <b>$15 Monthly Service Fee</b> OR <b>$0</b> with any one of the following, each monthly statement period:</p>
<table style="width:100%;border-collapse:collapse;margin-top:14px;font-size:14px">
<tr style="background:#F0F4FA"><td style="padding:10px 12px;border:1px solid var(--line)"><b>$500 or more</b> in qualifying electronic deposits (direct deposits)</td></tr>
<tr><td style="padding:10px 12px;border:1px solid var(--line)"><b>$1,500 or more</b> balance at the beginning of each day</td></tr>
<tr style="background:#F0F4FA"><td style="padding:10px 12px;border:1px solid var(--line)"><b>$5,000 or more</b> average beginning day balance (this account alone or with linked qualifying deposits/investments)</td></tr>
<tr><td style="padding:10px 12px;border:1px solid var(--line)">Link a <b>qualifying Chase checking account</b></td></tr>
</table>
<p style="margin-top:12px">The most popular option: set up <b>qualifying direct deposits of $500+</b>.</p>'''
    return t_web("Chase Total Checking&reg; fees","Chase &rsaquo; Checking &rsaquo; Chase Total Checking&reg;",body)

def t_locator(stage=0):
    if stage==0:
        return C.sb()+f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="background:#F6F6F6;border-bottom:1px solid var(--line);padding:12px 40px;display:flex;align-items:center;gap:14px"><span style="font-weight:700;font-size:17px">CHASE <span style="display:inline-block;width:16px;height:16px;background:var(--brand);border-radius:3px;vertical-align:-2px"></span></span><span style="margin-left:auto;font-size:13px;color:var(--ink2)">Find a branch or ATM</span></div>
  <div style="padding:26px 40px 0;max-width:640px">
    <div style="font-size:26px;font-weight:300">Schedule a meeting</div>
    <p style="font-size:14px;color:#3c4043;margin-top:8px">Meet with a banker or J.P. Morgan advisor &mdash; in person or virtually.</p>
    <div class="lbl">City or ZIP code</div><div class="field" style="max-width:380px">77002</div>
    <div style="margin-top:14px;display:flex;gap:10px"><div style="flex:1;max-width:190px;border:1px solid var(--line);border-radius:4px;height:44px;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:14px">Branch</div><div style="flex:1;max-width:190px;border:1px solid var(--line);border-radius:4px;height:44px;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:14px;color:var(--ink2)">ATM</div></div>
    <div style="margin-top:16px;background:var(--blue);color:#fff;display:inline-block;padding:12px 28px;border-radius:4px;font-weight:600;font-size:14.5px">Search</div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    if stage==1:
        return C.sb()+f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#fff"></div>
<div style="position:absolute;top:47px;left:0;right:0;bottom:0">
  <div style="background:#F6F6F6;border-bottom:1px solid var(--line);padding:12px 40px;font-weight:700;font-size:16px">Branches near 77002</div>
  <div style="margin:18px 40px 0;border:1px solid var(--line);border-radius:8px;overflow:hidden;font-size:14px;max-width:640px">
    <div class="hl" style="padding:14px 16px;border-bottom:1px solid var(--line)"><b>Chase &mdash; Houston Main</b><div style="font-size:12.5px;color:var(--ink2);margin-top:3px">712 Main St, Houston, TX 77002 &middot; 0.4 mi</div><div style="font-size:12.5px;color:var(--blue);margin-top:3px">Schedule a meeting &rsaquo;</div></div>
    <div style="padding:14px 16px;border-bottom:1px solid var(--line)"><b>Chase &mdash; Capitol Street</b><div style="font-size:12.5px;color:var(--ink2);margin-top:3px">1018 Congress Ave, Houston, TX 77002 &middot; 0.8 mi</div></div>
    <div style="padding:14px 16px"><b>Chase &mdash; Bayou Place</b><div style="font-size:12.5px;color:var(--ink2);margin-top:3px">500 Texas St, Houston, TX 77002 &middot; 1.1 mi</div></div>
  </div>
</div>{C.sb()}<div class="hi"></div>'''
    return t_locator(0)
