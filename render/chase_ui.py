"""Chase Mobile iOS — HTML blueprint templates built from verified 4K frames.
Every screen function returns the inner HTML of a 393x852 design-space `.app` div.
Rendered at 2x (786x1704) by the renderer. Data persona: Jordan Avery."""

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--blue:#0060F0;--brand:#0846A8;--ok:#2CA853;--ink:#1a1a1a;--ink2:#5f6368;--ink3:#9aa0a6;
      --bg:#F6F6F6;--line:#e3e3e3}
body{background:#555}
.shot{width:786px;height:1704px;background:#fff;position:relative;overflow:hidden}
.app{transform:scale(2);transform-origin:top left;width:393px;height:852px;position:relative;background:#fff;
     font-family:"Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif;color:var(--ink)}
.sb{position:absolute;top:0;left:0;right:0;height:47px;display:flex;align-items:center;justify-content:space-between;
    padding:0 22px 0 26px;font-weight:600;font-size:14px;z-index:50}
.sb .r{display:flex;align-items:center;gap:5px}
.sig{display:flex;align-items:flex-end;gap:1.5px}
.sig i{width:2.5px;background:currentColor;border-radius:1px;display:block}
.batt{width:20px;height:10px;border:1px solid currentColor;border-radius:3px;position:relative;opacity:.9}
.batt::after{content:"";position:absolute;inset:1px 4px 1px 1px;background:currentColor;border-radius:1px}
.batt::before{content:"";position:absolute;right:-3px;top:2.5px;width:2px;height:4px;background:currentColor;border-radius:1px}
.hi{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:126px;height:5px;border-radius:3px;background:#1a1a1a;opacity:.85;z-index:60}
.hi.lt{background:#fff}
.nav{position:absolute;top:47px;left:0;right:0;height:52px;display:flex;align-items:center;justify-content:center;
     border-bottom:1px solid var(--line);background:#fff;z-index:40}
.nav .bk{position:absolute;left:12px;display:flex;align-items:center;gap:4px;font-size:16px;color:var(--ink)}
.nav .t{font-size:16px;font-weight:600}
.nav .act{position:absolute;right:16px;font-size:16px;font-weight:600;color:var(--blue)}
.content{position:absolute;top:99px;bottom:0;left:0;right:0;overflow:hidden;background:var(--bg)}
.content.w{background:#fff}
h1.s{font-size:24px;font-weight:600;margin-bottom:12px}
.body{font-size:14.5px;line-height:1.5;color:#3c4043}
.rows{background:#fff;border-radius:12px;margin:10px 16px;box-shadow:0 1px 3px rgba(0,0,0,.07);overflow:hidden}
.row{display:flex;align-items:center;min-height:54px;padding:0 16px;border-bottom:1px solid var(--line);font-size:15.5px}
.row:last-child{border-bottom:none}
.row .g{flex:1}
.row .sub{font-size:12.5px;color:var(--ink2);margin-top:2px}
.row .chev{color:var(--ink3);font-size:17px;margin-left:8px}
.row .ico{width:24px;margin-right:12px;color:var(--blue);font-size:18px;text-align:center}
.sec{padding:20px 18px 6px;font-size:12.5px;font-weight:600;color:var(--ink2);letter-spacing:.4px}
.btn{display:flex;align-items:center;justify-content:center;width:calc(100% - 32px);margin:14px 16px;background:var(--blue);color:#fff;border:none;border-radius:6px;
     height:50px;font-size:16px;font-weight:600;font-family:inherit;text-align:center}
.btn.gray{background:#e9e9e9;color:#7c7c7c}
.btn.pill{border-radius:25px}
.lnk{color:var(--blue);font-weight:600}
.hl{outline:3px solid #FFB300;outline-offset:-3px;border-radius:10px}
.green-check{width:64px;height:64px;border-radius:50%;background:var(--ok);margin:26px auto 0;display:flex;align-items:center;justify-content:center}
.field{border:1px solid #b9bcc2;border-radius:8px;height:48px;display:flex;align-items:center;padding:0 12px;font-size:15px;background:#fff;color:var(--ink2)}
.lbl{font-size:12px;color:var(--ink2);margin:14px 0 5px}
.tabs{display:flex;border-bottom:1px solid var(--line);background:#fff}
.tabs div{flex:1;text-align:center;padding:13px 0;font-size:14.5px;font-weight:600;color:var(--ink2)}
.tabs div.on{color:var(--ink);border-bottom:3px solid var(--blue)}
.tnb{position:absolute;left:0;right:0;bottom:0;height:80px;background:#fff;border-top:1px solid var(--line);display:flex;padding:7px 2px 0;z-index:45}
.tnb .tb{flex:1;text-align:center;font-size:10px;color:#5f6368}
.tnb .tb svg{display:block;margin:0 auto 3px;stroke:#5f6368;fill:none}
.tnb .tb.on{color:var(--blue)}
.tnb .tb.on svg{stroke:var(--blue);fill:#E8F1FF}
.bbtns{position:absolute;left:0;right:0;bottom:34px;padding:10px 16px;z-index:48}
"""

def sb(dark=False):
    c = "#ffffff" if dark else "#1a1a1a"
    cell = ('<svg width="19" height="12" viewBox="0 0 19 12" fill="'+c+'">'
            '<rect x="0" y="7.5" width="3.4" height="4.5" rx="0.9"/>'
            '<rect x="5" y="5" width="3.4" height="7" rx="0.9"/>'
            '<rect x="10" y="2.5" width="3.4" height="9.5" rx="0.9"/>'
            '<rect x="15" y="0" width="3.4" height="12" rx="0.9"/></svg>')
    wifi = ('<svg width="17" height="12" viewBox="0 0 17 12" fill="none" stroke="'+c+'" stroke-width="1.9" stroke-linecap="round">'
            '<path d="M1.5 3.8C3.6 1.9 6 .9 8.5.9s4.9 1 7 2.9"/>'
            '<path d="M4 6.7c1.3-1.2 2.8-1.8 4.5-1.8s3.2.6 4.5 1.8"/>'
            '<path d="M6.6 9.5c.6-.55 1.2-.8 1.9-.8s1.3.25 1.9.8"/>'
            '<circle cx="8.5" cy="11" r="0.9" fill="'+c+'" stroke="none"/></svg>')
    batt = ('<svg width="27" height="13" viewBox="0 0 27 13">'
            '<rect x="0.5" y="0.5" width="22" height="12" rx="3.5" fill="none" stroke="'+c+'" stroke-opacity="0.4"/>'
            '<rect x="2" y="2" width="16" height="9" rx="2" fill="'+c+'"/>'
            '<path d="M24.5 4.5v4c1.3-.3 2-1.1 2-2s-.7-1.7-2-2z" fill="'+c+'" fill-opacity="0.5"/></svg>')
    return ('<div class="sb" style="color:'+c+'"><span style="font-size:16px;letter-spacing:.2px">12:01</span>'
            '<span class="r">'+cell+wifi+batt+'</span></div>')

def logo(size=30, color="#0B4DA2"):
    return ('<svg width="'+str(size)+'" height="'+str(size)+'" viewBox="0 0 100 100">'
            '<path fill="'+color+'" fill-rule="evenodd" d="'
            'M34 0 H66 L100 34 V66 L66 100 H34 L0 66 V34 Z '
            'M34 34 H66 V66 H34 Z"/></svg>')

def back():
    return '<svg width="11" height="18" viewBox="0 0 12 20" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M10 2 3 10l7 8"/></svg>'

def nav(title, backlabel="Back", action=None, border=True):
    a = f'<span class="act">{action}</span>' if action else ""
    b = f'<span class="bk">{back()} {backlabel}</span>' if backlabel else ""
    bd = "border-bottom:1px solid var(--line);" if border else ""
    return f'<div class="nav" style="{bd}">{b}<span class="t">{title}</span>{a}</div>'

def tabbar(active=0):
    W="#5f6368"; B="#0060F0"
    def svg(paths, fill=False, color=None):
        c=color or W
        f=c if fill else "none"
        return '<svg width="23" height="23" viewBox="0 0 24 24" fill="'+f+'" stroke="'+c+'" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+paths+'</svg>'
    icons=[
      svg('<rect x="3.2" y="5" width="17.6" height="14.5" rx="3"/><path d="M3.2 9.6h17.6"/><path d="M6.4 15.4h5"/>', True if active==0 else False),
      svg('<path d="M12 14.6a2.4 2.4 0 1 0 0-4.8 2.4 2.4 0 0 0 0 4.8z"/><path d="M12 8.2v1.6M12 14.2v1.6"/><path d="M20.2 12a8.2 8.2 0 0 1-1.2 4.3M3.8 12c0-1.6.5-3.1 1.3-4.3"/><path d="M18.6 6.2l.3 3-3-.2M5.4 17.8l-.3-3 3 .2"/>'),
      svg('<rect x="4.5" y="3.5" width="15" height="17" rx="2.4"/><path d="M8.5 8h7M8.5 11.6h4.6M12.6 15.4l2.6 2.6 3.4-3.4"/>'),
      svg('<path d="M12 3.4l2.7 5.4 6 .9-4.3 4.2 1 6-5.4-2.8-5.4 2.8 1-6L3.3 9.7l6-.9z"/>'),
      svg('<path d="M4 7h16M4 12h16M4 17h16"/>')]
    labels=["Accounts","Pay &amp; transfer","Plan &amp; track","Benefits &amp; travel","More"]
    out=['<div class="tnb">']
    for i,(ic,lb) in enumerate(zip(icons,labels)):
        on=" on" if i==active else ""
        out.append('<div class="tb'+on+'">'+ic+lb+'</div>')
    out.append('</div>')
    return "".join(out)

def acct_card(name="TOTAL CHECKING (&hellip;4821)", bal="$2,436.19", cap="Available balance", swatch="linear-gradient(135deg,#0B57C2,#0060F0)", meta=True):
    m = ('<div style="font-size:12px;color:var(--ink2);margin-top:9px;padding-top:9px;border-top:1px solid var(--line);display:flex;gap:14px">'
         f'<span>Present balance {bal}</span><span>&bull;&bull;&bull;&bull; 4821</span></div>') if meta else ""
    return (f'<div style="background:#fff;border-radius:13px;margin:0 20px 12px;padding:15px 16px;color:var(--ink);box-shadow:0 8px 20px rgba(0,0,0,.14)">'
            f'<div style="font-size:15.5px;font-weight:600;display:flex;align-items:center;gap:9px">'
            f'<span style="width:25px;height:25px;border-radius:6px;background:{swatch};flex:none"></span>{name}<span style="margin-left:auto;color:var(--ink3)">&rsaquo;</span></div>'
            f'<div style="font-size:27px;font-weight:600;margin-top:5px">{bal}</div>'
            f'<div style="font-size:12px;color:var(--ink2);margin-top:2px">{cap}</div>{m}</div>')

# ---------------- templates (each returns .app inner html) ----------------

def t_home(extra=""):
    g="#3c4043"
    return sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#F7F8FA"></div>
<div style="position:absolute;top:50px;left:0;right:0;padding:6px 18px 0">
  <div style="display:flex;align-items:center">
    <span style="color:{g};display:flex;gap:12px">
      <svg width="24" height="22" viewBox="0 0 26 24" fill="none" stroke="{g}" stroke-width="1.7"><path d="M2 5.5A3.5 3.5 0 0 1 5.5 2h8A3.5 3.5 0 0 1 17 5.5v5a3.5 3.5 0 0 1-3.5 3.5H8l-4 3.6V14"/><path d="M20 8h1.6A3.4 3.4 0 0 1 25 11.4v4.2a3.4 3.4 0 0 1-3.4 3.4h-.6v3l-3.4-3"/></svg>
      <svg width="25" height="22" viewBox="0 0 27 24" fill="none" stroke="{g}" stroke-width="1.7"><rect x="1.5" y="5" width="19" height="13.5" rx="2.6"/><path d="M5.5 5V3.6A2.1 2.1 0 0 1 7.6 1.5h14.3a2.1 2.1 0 0 1 2.1 2.1v10.2a2.1 2.1 0 0 1-2.1 2.1"/><path d="M11 13.6h5M13.5 11.1v5" stroke-linecap="round"/></svg>
    </span>
    <span style="margin:0 auto">{logo(34)}</span>
    <span style="color:{g}"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{g}" stroke-width="1.6"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="9.6" r="3.1"/><path d="M5.8 19.4c1-3 3.3-4.6 6.2-4.6s5.2 1.6 6.2 4.6"/></svg></span>
  </div>
  <div style="font-size:32px;font-weight:700;color:var(--ink);margin-top:22px;letter-spacing:-.3px">Good evening</div>
  <div style="font-size:15.5px;color:var(--ink);margin-top:6px">October 11, 2026</div>
  <div style="display:flex;gap:10px;margin-top:18px;overflow:hidden">
    <div style="flex:none;width:86px;height:46px;background:#fff;border-radius:23px;box-shadow:0 1px 4px rgba(0,0,0,.10);display:flex;align-items:center;justify-content:center;font-size:23px;color:var(--blue);font-weight:300">+</div>
    <div style="flex:none;height:46px;background:#fff;border-radius:23px;box-shadow:0 1px 4px rgba(0,0,0,.10);display:flex;align-items:center;font-size:15px;color:var(--blue);font-weight:600;padding:0 20px">Pay bills</div>
    <div style="flex:none;height:46px;background:#fff;border-radius:23px;box-shadow:0 1px 4px rgba(0,0,0,.10);display:flex;align-items:center;font-size:15px;color:var(--blue);font-weight:600;padding:0 18px">See bill activity</div>
    <div style="flex:none;height:46px;background:#fff;border-radius:23px;box-shadow:0 1px 4px rgba(0,0,0,.10);display:flex;align-items:center;font-size:15px;color:var(--blue);font-weight:600;padding:0 16px">Credit Journey</div>
  </div>
  <div style="margin-top:20px;background:#fff;border-radius:16px;box-shadow:0 2px 8px rgba(0,0,0,.07);padding:16px;display:flex;align-items:center;gap:14px">
    <span style="width:50px;height:50px;border-radius:50%;background:#E3F0FD;display:flex;align-items:center;justify-content:center;font-size:24px;flex:none">&#127942;</span>
    <div style="flex:1">
      <div style="display:flex;align-items:center;gap:8px"><b style="font-size:17.5px">Snapshot</b><span style="background:#F1F2F4;color:var(--ink2);border-radius:12px;padding:3px 10px;font-size:12.5px">30 sec read</span></div>
      <div style="font-size:15.5px;color:var(--ink);margin-top:5px;line-height:1.35">You recently earned <b>161 Amazon Rewards points</b>.</div>
    </div>
    <span style="color:var(--ink2);font-size:18px">&rsaquo;</span>
  </div>
  <div style="display:flex;align-items:center;margin:24px 2px 12px">
    <span style="font-size:23px;font-weight:700;color:var(--ink)">Accounts</span>
    <span style="margin-left:auto;width:32px;height:32px;border-radius:50%;border:1.5px solid #8a9099;display:flex;align-items:center;justify-content:center;color:#3c4043;font-weight:700;letter-spacing:1px;font-size:12px">&hellip;</span>
  </div>
  <div style="background:linear-gradient(90deg,#1B449C,#153680);border-radius:12px 12px 0 0;padding:15px 18px;color:#fff;font-size:16.5px;font-weight:600">Bank accounts (1)</div>
  <div style="background:#fff;border-radius:0 0 12px 12px;padding:15px 18px 17px;box-shadow:0 2px 8px rgba(0,0,0,.05)">
    <div style="font-size:15.5px;font-weight:700;color:#0A2E6E">TOTAL CHECKING (&hellip;4821) &rsaquo;</div>
    <div style="text-align:right;margin-top:6px">
      <div style="font-size:28px;color:var(--ink)">$2,436.19</div>
      <div style="font-size:14px;color:var(--ink2)">Available balance</div>
    </div>
  </div>
  <div style="background:linear-gradient(90deg,#1B449C,#153680);border-radius:12px 12px 0 0;padding:15px 18px;color:#fff;font-size:16.5px;font-weight:600;margin-top:14px">Credit cards (1)</div>
  <div style="background:#fff;border-radius:0 0 12px 12px;padding:15px 18px 15px;box-shadow:0 2px 8px rgba(0,0,0,.05)">
    <div style="font-size:15.5px;font-weight:700;color:#0A2E6E">CREDIT CARD (&hellip;7710) &rsaquo;</div>
    <div style="display:flex;align-items:flex-end;margin-top:10px">
      <div style="width:96px;height:60px;border-radius:7px;background:linear-gradient(135deg,#1A1D24,#0B0D12 65%);position:relative;box-shadow:0 2px 6px rgba(0,0,0,.3)">
        <span style="position:absolute;left:7px;top:6px;color:#00A8E0;font-weight:700;font-size:9px;letter-spacing:.3px">Chase Freedom</span>
        <span style="position:absolute;right:7px;bottom:6px;color:#fff;font-weight:700;font-size:9px;font-style:italic">VISA</span>
      </div>
      <div style="flex:1;text-align:right">
        <div style="font-size:28px;color:var(--ink)">$418.77</div>
        <div style="font-size:14px;color:var(--ink2)">Current balance</div>
      </div>
    </div>
    <div style="display:flex;gap:8px;margin-top:10px;font-size:14px;color:var(--ink);line-height:1.35"><span style="color:var(--ok);font-weight:700">&#10003;</span><span>You've scheduled your automatic payment for <b>Oct 12, 2026</b>.</span></div>
  </div>
  <div style="margin-top:14px;background:#fff;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.05)">
    <div class="row" style="border:none;border-radius:12px"><div class="g" style="font-size:15.5px;font-weight:600">Link external accounts</div><span class="chev">&rsaquo;</span></div>
  </div>
  <div style="margin:16px 0 10px;border:1.5px solid var(--blue);border-radius:26px;height:48px;display:flex;align-items:center;justify-content:center;gap:6px;color:var(--blue);font-size:15.5px;font-weight:600"><span style="font-size:19px;font-weight:400">+</span> Open an account</div>
</div>
{extra}{tabbar(0)}{sb()}<div class="hi"></div>'''.replace("{sb()}", sb())

def t_account(highlight="manage", txn=False):
    txn_items = txn if isinstance(txn,list) else [
      ("ATM CASH DEPOSIT 06/29 1010 THE WOODLANDS PKWY THE WOODLANDS TX","Jun 25, 2026","$50.00"),
      ("KIWI KAR LUBE &amp; REPA THE WOODLANDS TX (6/29)","Jul 01, 2026","-$18.50"),
      ("REMOTE ONLINE DEPOSIT #1","Jun 30, 2026","$30.00")]
    tx=""
    if txn:
        rows="".join(f'<div style="display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid var(--line);font-size:12.5px"><span style="flex:1;padding-right:10px">{n}<div style="color:var(--ink2);font-size:11.5px;margin-top:2px">{d}</div></span><span style="text-align:right"><b>{a}</b></span></div>' for n,d,a in txn_items)
        tx=f'''
  <div style="margin:0 16px;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:4px 16px 2px">{rows}</div>
  <div style="display:flex;gap:10px;margin:12px 16px 0"><span class="lnk" style="font-size:13px;border:1px solid var(--line);border-radius:16px;padding:7px 14px;background:#fff">See statements</span><span class="lnk" style="font-size:13px;border:1px solid var(--line);border-radius:16px;padding:7px 14px;background:#fff">See all transactions</span></div>'''
    hl=" hl" if highlight=="manage" else ""
    return sb() + f'''
<div style="position:absolute;top:0;left:0;right:0;bottom:0;background:#E9EEF6"></div>
<div style="position:absolute;top:50px;left:0;right:0;bottom:0;overflow:hidden">
  <div style="padding:6px 14px 0;color:#3c4043;font-size:22px">{back()}</div>
  <div style="padding:2px 16px 0;font-size:31px;font-weight:700;color:var(--ink)">TOTAL CHECKING (&hellip;4821)</div>
  <div style="margin:12px 14px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.06);padding:14px 16px">
    <div style="text-align:right">
      <div style="font-size:29px;color:var(--ink)">$2,436.19</div>
      <div style="font-size:13.5px;color:var(--ink2);margin-top:1px">Available balance</div>
    </div>
    <div style="font-size:17px;font-weight:700;margin-top:14px">Account details</div>
    <div style="display:flex;justify-content:space-between;font-size:14.5px;padding:10px 0;border-bottom:1px solid var(--line)"><span>Available balance</span><span>$2,436.19 <span style="color:var(--blue)">&#9432;</span></span></div>
    <div style="display:flex;justify-content:space-between;font-size:14.5px;padding:10px 0"><span>Present balance</span><span>$2,436.19 <span style="color:var(--blue)">&#9432;</span></span></div>
  </div>
  <div style="text-align:center;margin:10px 0 4px"><span style="display:inline-block;background:#fff;border:1.5px solid var(--blue);color:var(--blue);border-radius:22px;padding:10px 22px;font-size:15.5px;font-weight:600">Show details &#9662;</span></div>
  <div style="display:flex;justify-content:space-around;margin:14px 10px 0">
    <div style="text-align:center"><div style="width:58px;height:58px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.08);margin:0 auto 6px;display:flex;align-items:center;justify-content:center"><span style="width:34px;height:22px;border-radius:4px;background:linear-gradient(135deg,#1557A5,#0A2E6E)"></span></div><span style="color:var(--blue);font-weight:600;font-size:14px">Pay</span></div>
    <div style="text-align:center"><div style="width:58px;height:58px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.08);margin:0 auto 6px;display:flex;align-items:center;justify-content:center;color:var(--blue);font-size:20px">&#8644;</div><span style="color:var(--blue);font-weight:600;font-size:14px">Transfer</span></div>
    <div style="text-align:center"><div style="width:58px;height:58px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.08);margin:0 auto 6px;display:flex;align-items:center;justify-content:center;color:var(--blue);font-size:20px">&#8943;</div><span style="color:var(--blue);font-weight:600;font-size:14px">More</span></div>
  </div>
  <div style="margin:16px 14px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.06);padding:12px 16px">
    <div style="font-size:16px;font-weight:700">Action list</div>
    <div style="display:flex;align-items:center;gap:10px;padding:10px 0 2px"><span style="color:var(--blue);font-size:16px">&#128203;</span><span style="flex:1;font-size:14.5px">Finish setting up your new account</span><span class="chev" style="color:var(--ink3)">&rsaquo;</span></div>
  </div>
  <div style="margin:12px 14px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.06);padding:13px 16px">
    <div class="row" style="border:none;padding:0;min-height:40px"><div class="g{hl}"><b style="font-size:16px">Manage account</b><div class="sub" style="font-size:13px;color:#5f6368">Access tools &amp; services for your account</div></div><span class="chev">&rsaquo;</span></div>
  </div>
  <div style="margin:12px 14px 0;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.06);padding:13px 16px">
    <div class="row" style="border:none;padding:0;min-height:30px"><div class="g"><b style="font-size:16px">See all transactions</b></div><span class="chev">&rsaquo;</span></div>{tx}
  </div>
</div>{tabbar(0)}{sb()}<div class="hi"></div>'''

def t_manage(highlight=None):
    rows1 = ["Track your card","Add card to digital wallets","Activate your card","Manage PIN"]
    rows2 = ["Stop payment on a check","Overdraft protection","Debit card coverage","Order checks and deposit slips","Set up direct deposit form"]
    def r(n): 
        h = ' hl' if highlight and highlight.lower() in n.lower() else ''
        b = '<b>'+n+'</b>' if h else n
        s = '<div class="sub" style="color:#8a6d00">TAP HERE</div>' if h else ''
        return f'<div class="row{h}"><div class="g">{b}{s}</div><span class="chev">&rsaquo;</span></div>'
    tri = ''.join(f'<div style="flex:1;background:#fff;border-radius:10px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:12px 6px;font-size:11.5px;font-weight:600;text-align:center;min-height:64px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px"><span style="color:var(--blue);font-size:17px">{i}</span>{n}</div>'
      for i,n in [("&#128274;","Lock &amp; unlock card"),("&#128179;","Replace a lost or damaged card"),("&#9432;","Dispute a transaction")])
    return sb() + nav("Manage account") + f'''
<div class="content w">
  <div style="display:flex;gap:8px;padding:14px 16px 2px">{tri}</div>
  <div class="sec">CARD SETUP AND MAINTENANCE</div>
  <div class="rows">{''.join(r(x) for x in rows1)}</div>
  <div class="sec">SERVICES</div>
  <div class="rows">{''.join(r(x) for x in rows2)}</div>
</div>{tabbar(0)}{sb()}<div class="hi"></div>'''

def t_lock(locked=False):
    btn = "Unlock card" if locked else "Lock card"
    conf = '<div style="display:flex;align-items:center;gap:8px;margin:2px 16px 14px;font-size:14.5px"><span style="color:var(--ok);font-weight:700">&#10003;</span><b>You&rsquo;ve locked your card!</b></div>' if locked else ""
    return sb() + ('<div class="nav" style="border-bottom:1px solid var(--line)"><span class="bk" style="left:14px">'+back()+'</span><span class="t">Lock &amp; unlock your card</span></div>') + f'''
<div class="content w">
  <div style="padding:22px 22px 0;text-align:center">
    <h1 class="s" style="font-size:23px">Misplaced your card?</h1>
    <p class="body" style="margin-bottom:18px">Block new purchases and ATM withdrawals made with your card number. This won't block fees, credits, digital wallet purchases or repeating transactions. Previously authorized transactions will continue to be processed. If your card is lost or damaged, you can request a replacement.</p>
  </div>
  <div style="border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:0 0 16px">
    <div style="display:flex;align-items:center;padding:15px 16px">
      <b style="font-size:15px;flex:1">DEBIT/ATM CARD (&hellip;2208)</b>
      <span style="color:var(--ink2)">&#128274;</span>
    </div>
  </div>{conf}
  <div style="display:flex;justify-content:flex-end;padding:0 16px"><div style="background:var(--blue);color:#fff;border-radius:6px;height:46px;display:flex;align-items:center;justify-content:center;font-size:15.5px;font-weight:600;padding:0 26px">{btn}</div></div>
  <div style="padding:18px 16px 0;font-size:14px;color:var(--blue)">Questions? Read our FAQs &gt;</div>
  <div style="padding:22px 16px 0;font-size:16.5px;font-weight:700">Digital Wallet</div>
  <p class="body" style="padding:8px 16px 0;font-size:14px">Pay in stores, online and in merchant apps with your digital wallet even while your card is locked.</p>
  <div style="padding:12px 16px 0;font-size:14px;color:var(--blue)">Go to digital wallets &gt;</div>
</div>{sb()}<div class="hi"></div>'''.replace("{sb()}", sb())

def t_replace_reasons():
    return sb() + nav("Replace a card", action="Cancel") + '''
<div class="content w" style="background:#fff">
  <div style="height:4px;background:var(--line)"><div style="width:33%;height:4px;background:var(--blue)"></div></div>
  <div style="padding:20px 20px 0">
    <h1 class="s" style="text-align:center;font-size:22px">Tell us more about your situation</h1>
    <p class="body" style="text-align:center;margin-bottom:14px">We'll help protect and keep your accounts safe.</p>
    <div style="font-size:13px;font-weight:600;color:var(--ink2);margin-bottom:8px">Choose a reason</div>
    <div style="border:1.5px solid var(--blue);border-radius:12px;padding:13px 14px;margin-bottom:10px">
      <div style="display:flex;align-items:center;gap:10px"><b style="flex:1;font-size:15px">My card is lost</b><span style="width:19px;height:19px;border-radius:50%;border:6px solid var(--blue)"></span></div>
      <p class="body" style="font-size:12.5px;margin-top:9px">For your protection, we'll immediately cancel your current card and issue a replacement with a new card number.</p>
      <p class="body" style="font-size:12.5px;margin-top:6px">If you think someone used your card without your permission, call us right away at 1-800-935-9935, for help.</p>
    </div>
    <div style="border:1px solid var(--line);border-radius:12px;padding:13px 14px;margin-bottom:10px;display:flex;align-items:center;gap:10px"><b style="flex:1;font-size:15px">My card is damaged</b><span style="width:19px;height:19px;border-radius:50%;border:2px solid #b9bcc2"></span></div>
    <div style="border:1px solid var(--line);border-radius:12px;padding:13px 14px;display:flex;align-items:center;gap:10px"><b style="flex:1;font-size:15px">I never received my card in mail</b><span style="width:19px;height:19px;border-radius:50%;border:2px solid #b9bcc2"></span></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{sb()}<div class="hi"></div>'''.replace("{sb()}", sb())

def t_replace_shipping():
    return sb() + nav("Replace a card", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="height:4px;background:var(--line)"><div style="width:66%;height:4px;background:var(--blue)"></div></div>
  <div style="padding:20px 20px 0">
    <h1 class="s" style="font-size:22px">Shipping info</h1>
    <div class="lbl">Mailing address</div>
    <div style="border:1px solid var(--line);border-radius:8px;height:48px;display:flex;align-items:center;justify-content:space-between;padding:0 12px;font-size:15px;color:#c6c9cd;background:repeating-linear-gradient(45deg,#fafafa,#fafafa 6px,#f2f2f2 6px,#f2f2f2 12px)">&#9679;&#9679;&#9679;&#9679; <span style="color:var(--blue)">&#9432;</span></div>
    <div class="lbl" style="margin-top:18px">Shipping method</div>
    <div style="border:1.5px solid var(--blue);border-radius:12px;padding:13px 14px">
      <b style="font-size:15px">Regular delivery</b>
      <div style="font-size:13px;margin-top:5px">5 to 7 business days*</div>
      <div style="font-size:13px;margin-top:3px;color:var(--ink2)">No charge</div>
    </div>
    <p style="font-size:11.5px;color:var(--ink2);margin-top:10px">*Please allow additional time for cards shipped to PO boxes or international addresses.</p>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{sb()}<div class="hi"></div>'''

def t_replace_summary():
    return sb() + nav("Replace a card", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="height:4px;background:var(--blue)"></div>
  <div style="padding:18px 20px 0">
    <h1 class="s" style="font-size:22px">Does everything look OK?</h1>
    <div class="sec" style="padding:8px 0 4px">Card info</div>
    <div style="border-top:1px solid var(--line);padding:10px 0;border-bottom:1px solid var(--line)">
      <div style="display:flex;font-size:14px;padding:4px 0"><span style="width:130px;color:var(--ink2)">Cards to replace</span><b>DEBIT/ATM CARD (&hellip;2208)</b></div>
      <div style="display:flex;font-size:12px;padding:0 0 4px 130px;color:var(--ink2)">(New card will use (&hellip;2208))</div>
    </div>
    <div class="sec" style="padding:12px 0 4px">Reason</div>
    <div style="display:flex;font-size:14px;padding:4px 0 12px;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">My card is</span><b>damaged</b></div>
    <div class="sec" style="padding:12px 0 4px">Shipping info</div>
    <div style="display:flex;font-size:14px;padding:4px 0"><span style="width:130px;color:var(--ink2)">Mailing address</span><span style="color:#c6c9cd">&#9679;&#9679;&#9679;&#9679;</span></div>
    <div style="display:flex;font-size:14px;padding:4px 0"><span style="width:130px;color:var(--ink2)">Shipping method</span><span>Regular delivery</span></div>
    <div style="display:flex;font-size:14px;padding:0 0 4px 130px;color:var(--ink2)">5 to 7 business days*<br>No charge</div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Replace card</div></div>
</div>{sb()}<div class="hi"></div>'''

def t_activate(stage="expiry"):
    if stage=="ok":
        return sb() + ('<div class="nav"><span class="bk" style="left:14px">'+back()+'</span><span class="t">Activate card</span></div>') + f'''
<div class="content w" style="background:#fff">
  <div class="green-check"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:22px;font-weight:600;margin-top:14px">You're all set!</div>
  <p class="body" style="text-align:center;margin:8px 30px 16px">You've activated your new debit card and can start using it right away.</p>
  <div style="display:flex;align-items:center;gap:12px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:13px 16px;margin:0 0 16px">
    <span style="width:44px;height:32px;border-radius:5px;background:linear-gradient(135deg,#1557A5,#0A2E6E);flex:none"></span>
    <b style="font-size:14px">DEBIT/ATM CARD (&hellip;2208)</b>
  </div>
  <div style="font-size:16px;font-weight:600;margin:0 16px 4px">Here's what you can do next</div>
  <div class="rows" style="margin-top:8px">
    <div class="row" style="align-items:flex-start;min-height:62px"><div class="g"><b>Digital Wallet</b><div class="sub">Add your card to your digital wallet and use it in-store, online or in-app.</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="align-items:flex-start;min-height:62px"><div class="g"><b>Account alerts</b><div class="sub">Be the first to stay in touch with your account activity.</div></div><span class="chev">&rsaquo;</span></div>
    <div class="row" style="align-items:flex-start;min-height:62px"><div class="g"><b>Chase Credit Journey</b><div class="sub">Learn more about your credit and how to improve it.</div></div><span class="chev">&rsaquo;</span></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Done</div></div>
</div>{sb()}<div class="hi"></div>'''.replace("{sb()}", sb())
    return sb() + ('<div class="nav"><span class="bk" style="left:14px">'+back()+'</span><span class="t">Activate card</span><span class="act">Cancel</span></div>') + f'''
<div class="content w" style="background:#fff">
  <div style="padding:20px 20px 0;text-align:center">
    <div style="font-size:24px;font-weight:600">Your new debit card</div>
    <div style="font-size:15px;color:#3c4043;margin-top:6px">Confirm your details.</div>
    <div style="width:210px;height:132px;border-radius:12px;background:linear-gradient(150deg,#1B5FA8,#0A2E6E 75%);margin:20px auto 10px;position:relative;box-shadow:0 6px 18px rgba(0,0,0,.22)">
      <span style="position:absolute;left:12px;top:10px;color:#fff;font-weight:700;font-size:11px;letter-spacing:.5px;display:flex;align-items:center;gap:4px">CHASE {logo(12,"#ffffff")}</span>
      <span style="position:absolute;right:10px;top:10px">{logo(20,"#4A9FE8")}</span>
      <span style="position:absolute;right:12px;bottom:10px;color:#fff;text-align:right;line-height:1.1"><span style="font-size:7px;letter-spacing:1px;opacity:.85">DEBIT</span><br><b style="font-size:13px;font-style:italic">VISA</b></span>
    </div>
    <div style="font-size:15px;font-weight:700;color:var(--ink)">DEBIT/ATM CARD (&hellip;2208)</div>
  </div>
  <div style="padding:18px 20px 0">
    <p class="body" style="margin-bottom:16px">Tell us the expiration date on your new card.</p>
    <div style="font-size:17px;color:var(--ink2);border-bottom:2px solid var(--blue);padding-bottom:8px">xx/xx</div>
    <div style="font-size:12px;color:var(--ink2);margin-top:6px">MM/YY</div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Activate</div></div>
</div>{sb()}<div class="hi"></div>'''.replace("{sb()}", sb())

def t_dd():
    return sb() + nav("Direct Deposit", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:22px 20px 0">
    <div style="width:64px;height:64px;border-radius:14px;background:#E8F1FF;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;font-size:26px">&#128179;</div>
    <div style="font-size:21px;font-weight:600;line-height:1.3">Have your paychecks<br>sent here</div>
    <p class="body" style="margin-top:8px">Give your routing and account numbers to your employer to set up direct deposit.</p>
  </div>
  <div style="margin:18px 16px;border:1px solid var(--line);border-radius:12px;overflow:hidden">
    <div style="background:#E8F1FF;padding:10px 14px;font-size:14px;font-weight:600">Account details</div>
    <div style="padding:12px 14px;border-bottom:1px solid var(--line);font-size:13.5px;font-weight:600">TOTAL CHECKING (&hellip;4821)</div>
    <div style="display:flex;align-items:center;padding:12px 14px;border-bottom:1px solid var(--line)">
      <div style="flex:1"><div style="font-size:12px;color:var(--ink2)">Routing number</div><div style="font-size:15px;font-weight:600">111000614</div></div>
      <span style="color:var(--blue);font-weight:600;font-size:13.5px;margin-right:8px">Copy</span><span style="color:var(--ink2)">&#128203;</span>
    </div>
    <div style="display:flex;align-items:center;padding:12px 14px">
      <div style="flex:1"><div style="font-size:12px;color:var(--ink2)">Account number</div><div style="font-size:15px;font-weight:600;letter-spacing:1px">&bull;&bull;&bull;&bull;&bull;4821</div></div>
      <span style="color:var(--blue);font-weight:600;font-size:13.5px;margin-right:8px">Copy</span><span style="color:var(--ink2)">&#128203;</span>
    </div>
  </div>
  <div style="margin:0 16px;font-size:13.5px;line-height:1.5;color:#3c4043"><b>Need a form instead?</b><br>Download a prefilled <span class="lnk">Direct Deposit form (PDF)</span> to give to your employer.</div>
  <div style="margin:14px 16px 0;font-size:13.5px;line-height:1.5;color:#3c4043">Do you have government income such as Social Security or military pay? Visit <span class="lnk">GoDirect.gov</span>.</div>
</div>{sb()}<div class="hi"></div>'''

def t_show_details():
    rows = [("Available balance","$2,436.19 &#9432;","b"),("Present balance","$2,436.19 &#9432;","b"),
            ("Account number","&bull;&bull;&bull;&bull;&bull;4821","b"),("Routing number","111000614","b"),
            ("Interest rate","0.00%",""),("Interest in 2026","$0.00",""),("Last statement date","Jun 22, 2026","")]
    rr = "".join(f'<div style="display:flex;justify-content:space-between;font-size:13.5px;padding:7px 0"><span style="color:var(--ink2)">{a}</span><span>{b}</span></div>' for a,b,_ in rows)
    return sb() + nav("Total Checking (&hellip;4821)") + f'''
<div class="content w">
  <div style="padding:10px 20px 0">
    <div style="font-size:33px;font-weight:600">$2,436.19</div>
    <div style="font-size:13px;color:var(--ink2);margin-top:2px">Available balance</div>
  </div>
  <div style="margin:14px 16px;background:#fff;border-radius:12px;box-shadow:0 1px 3px rgba(0,0,0,.07);padding:12px 14px">
    <div style="font-size:15px;font-weight:600;margin-bottom:4px">Account details</div>{rr}
  </div>
  <div style="text-align:center;margin-top:2px"><span style="display:inline-block;border:1px solid var(--blue);color:var(--blue);border-radius:18px;padding:8px 16px;font-size:13.5px;font-weight:600">Hide details &#9652;</span></div>
  <div style="display:flex;gap:10px;padding:16px 20px 4px">
    <div style="flex:1;height:44px;border-radius:22px;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600">Pay</div>
    <div style="flex:1;height:44px;border-radius:22px;border:1px solid var(--blue);color:var(--blue);display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600">Transfer</div>
    <div style="flex:1;height:44px;border-radius:22px;border:1px solid var(--blue);color:var(--blue);display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600">More</div>
  </div>
</div>{tabbar(0)}{sb()}<div class="hi"></div>'''

def t_stmt_docs():
    return sb() + nav("Statements and Documents") + f'''
<div class="content w">
  <div class="rows" style="margin-top:12px">
    <div class="row"><div class="g">Statements</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g">Tax documents</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g">ATM &amp; branch receipts</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g">Notices and letters</div><span class="chev">&rsaquo;</span></div>
    <div class="row"><div class="g">Branch documents</div><span class="chev">&rsaquo;</span></div>
  </div>
  <p class="body" style="font-size:13px;margin:16px 18px">Don't see an account listed for your documents? If you don't see an account, statement or document, it may be hidden. You can update those in 'Show or hide accounts'.</p>
</div>{tabbar(0)}{sb()}<div class="hi"></div>'''

def t_stmts_page():
    years = "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:13px 14px;border-bottom:1px solid var(--line);font-size:14.5px;font-weight:600"><span>&#9656; {y}</span><span style="color:var(--ink3);font-size:12px">&#9662;</span></div>' for y in [2026,2025])
    return sb() + nav("Statements") + f'''
<div class="content w">
  <div style="padding:14px 18px 0">
    <div style="font-size:17px;font-weight:600">TOTAL CHECKING (&hellip;4821)</div>
    <p class="body" style="font-size:13px;margin-top:8px">You can view up to 7 years of bank statements. We'll usually post your paper statement 3-5 business days after your statement cycle ends.</p>
    <div style="background:#e9e9e9;color:#7c7c7c;border-radius:8px;height:42px;display:flex;align-items:center;justify-content:center;font-size:14.5px;font-weight:600;margin-top:12px">Paperless</div>
  </div>
  <div class="rows" style="margin-top:14px">{years}
    <div style="padding:13px 14px;border-bottom:1px solid var(--line);font-size:14.5px;font-weight:600">&#9662; 2024</div>
    <div style="padding:12px 14px;font-size:13.5px;color:var(--ink2);display:flex;gap:8px">&#9432; You have no statements available for this period.</div>
    {''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:13px 14px;border-bottom:1px solid var(--line);font-size:14.5px;font-weight:600"><span>&#9656; {y}</span><span style="color:var(--ink3);font-size:12px">&#9662;</span></div>' for y in [2023,2022,2021,2020,2019])}
  </div>
</div>{tabbar(0)}{sb()}<div class="hi"></div>'''

def t_paperless(stage="edit"):
    if stage=="ok":
        return sb() + nav("Paperless settings", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div class="green-check"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:21px;font-weight:600;margin-top:14px;line-height:1.3">You updated your<br>paperless settings</div>
  <p class="body" style="text-align:center;margin:10px 26px 0">Updates to your delivery preferences will take effect immediately in most cases. If we're already preparing your next statement or any other document types for which you changed preferences, you'll see your updates to following ones.</p>
  <div class="bbtns"><div class="btn" style="margin:0">Done</div></div>
</div>{sb()}<div class="hi"></div>'''
    return sb() + nav("Paperless settings", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 18px 0">
    <p class="body" style="font-size:13px">When you go paperless, we'll no longer send paper documents. Instead, you can access them anytime in your account on Chase.com or in the Chase Mobile&reg; app under Profile &amp; Settings or the more menu.</p>
    <p class="body" style="font-size:12.5px;margin-top:8px">Note: For notices and letters, we may send an email to the primary account holder only. You may still receive important information in the mail.</p>
    <div style="display:flex;font-size:13px;margin-top:10px"><b style="width:60px">Email to:</b><span>j.avery4821@example.com <span class="lnk">Edit &rsaquo;</span></span></div>
    <div style="font-size:12.5px;margin-top:8px">Questions? See our paperless <span class="lnk">FAQs &rsaquo;</span></div>
  </div>
  <div class="rows" style="margin-top:10px"><div class="row"><div class="g"><b>Statements &amp; documents</b><div class="sub">Access your documents online</div></div><span class="chev">&rsaquo;</span></div></div>
  <div class="sec" style="padding-left:0;padding-right:0">Choose paperless for all accounts</div>
  <div class="rows">
    <div class="row"><span style="width:20px;height:20px;border:2px solid #b9bcc2;border-radius:4px;margin-right:12px"></span><div class="g">All documents</div></div>
    <div class="row"><span style="width:20px;height:20px;border-radius:4px;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;margin-right:12px;font-size:13px">&#10003;</span><div class="g">All statements</div></div>
    <div class="row"><span style="width:20px;height:20px;border:2px solid #b9bcc2;border-radius:4px;margin-right:12px"></span><div class="g">All notices and letters</div></div>
    <div class="row"><span style="width:20px;height:20px;border:2px solid #b9bcc2;border-radius:4px;margin-right:12px"></span><div class="g">All tax documents</div></div>
  </div>
  <div class="bbtns" style="bottom:20px"><div class="btn" style="margin:0">Save</div></div>
</div>{sb()}<div class="hi"></div>'''

def t_qd(stage="agree"):
    if stage=="agree":
        return sb() + nav("Chase QuickDeposit&trade;", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:18px 20px 0">
    <div style="width:60px;height:60px;border-radius:14px;background:#E8F1FF;margin:0 auto 10px;display:flex;align-items:center;justify-content:center;font-size:24px">&#128196;</div>
    <div style="font-size:20px;font-weight:600;line-height:1.3">Start depositing checks with<br>Chase QuickDeposit&trade;</div>
  </div>
  <div style="margin:16px 20px 0;font-size:13.5px;line-height:1.6;color:#3c4043">
    <div style="display:flex;gap:10px;margin-bottom:10px"><span style="color:var(--blue)">&#9878;</span><span>Deposit your check in a few steps anytime and anywhere.</span></div>
    <div style="display:flex;gap:10px;margin-bottom:10px"><span style="color:var(--blue)">&#128274;</span><span>We don't save check info or photos on your device.</span></div>
    <div style="display:flex;gap:10px"><span style="color:var(--blue)">&#128197;</span><span>Hold onto your check for 2 business days after you deposit it, then you can destroy it.</span></div>
  </div>
  <div style="margin:14px 20px 0;font-size:12.5px;color:var(--ink2)">Chase QuickDeposit&trade; and J.P. Morgan QuickDeposit&trade; Agreement for Mobile &rsaquo;</div>
  <div style="display:flex;gap:10px;margin:14px 20px 0;align-items:flex-start"><span style="width:20px;height:20px;border-radius:4px;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:13px;flex:none">&#10003;</span><span style="font-size:13px">I agree to the Chase QuickDeposit&trade; and J.P. Morgan QuickDeposit&trade; Agreement for Mobile.</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Deposit a check</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="tips":
        return sb() + nav("QuickDeposit&trade;", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:20px 20px 0"><div style="width:58px;height:58px;border-radius:14px;background:#E8F1FF;margin:0 auto 10px;display:flex;align-items:center;justify-content:center;font-size:24px">&#128247;</div>
  <div style="font-size:20px;font-weight:600">Auto-capture tips</div></div>
  <div style="margin:16px 22px 0;font-size:14px;line-height:1.65;color:#3c4043">
    <div style="display:flex;gap:10px;margin-bottom:9px"><b>1.</b><span>Place the check on a well-lit surface with a plain, dark background.</span></div>
    <div style="display:flex;gap:10px;margin-bottom:9px"><b>2.</b><span>Place the check in horizontal orientation.</span></div>
    <div style="display:flex;gap:10px;margin-bottom:9px"><b>3.</b><span>Position the device's camera over the check, keeping all corners within the guide.</span></div>
    <div style="display:flex;gap:10px"><b>4.</b><span>Keep the camera still. We'll take the photo for you within 20 seconds.</span></div>
  </div>
  <div style="display:flex;gap:10px;margin:16px 20px 0;align-items:center"><span style="width:19px;height:19px;border:2px solid #b9bcc2;border-radius:4px"></span><span style="font-size:13.5px">Don't show this again.</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Get started</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="review":
        return sb() + nav("Review", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 20px 0;text-align:center">
    <div style="font-size:19px;font-weight:600">Does everything look OK?</div>
    <div style="font-size:12.5px;color:var(--ink2);margin-top:14px">Deposit amount</div>
    <div style="font-size:30px;font-weight:600">$30.00</div>
    <div style="display:flex;gap:14px;justify-content:center;margin:16px 0 6px">
      <div><div style="font-size:11.5px;color:var(--ink2);margin-bottom:4px">Front</div><div style="width:110px;height:66px;border-radius:6px;border:1.5px solid #2CA853;background:repeating-linear-gradient(45deg,#f4f6f8,#f4f6f8 5px,#eceff2 5px,#eceff2 10px)"></div></div>
      <div><div style="font-size:11.5px;color:var(--ink2);margin-bottom:4px">Back</div><div style="width:110px;height:66px;border-radius:6px;border:1.5px solid #2CA853;background:repeating-linear-gradient(45deg,#f4f6f8,#f4f6f8 5px,#eceff2 5px,#eceff2 10px)"></div></div>
    </div>
  </div>
  <div style="margin:10px 20px 0;font-size:13.5px">
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Deposit to</span><b>TOTAL CHECKING (&hellip;4821)</b></div>
    <div style="display:flex;padding:7px 0"><span style="width:120px;color:var(--ink2)">Deposit amount</span><span>$30.00</span></div>
  </div>
  <p class="body" style="font-size:12.5px;margin:12px 20px 0">The full amount is usually available by the next business day, but may take up to 7 business days if we need to review your deposit.</p>
  <div class="bbtns"><div class="btn" style="margin:0">Deposit</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="ok":
        return sb() + nav("Confirmation") + f'''
<div class="content w" style="background:#fff">
  <div class="green-check"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:21px;font-weight:600;margin-top:12px">We received your deposit.</div>
  <div style="text-align:center;font-size:30px;font-weight:600;margin-top:8px">$30.00</div>
  <div style="margin:16px 20px 0;font-size:13.5px">
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Deposit to</span><b>TOTAL CHECKING (&hellip;4821)</b></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Received on</span><span>Jun 30, 2026 1:18 PM ET</span></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Available now</span><span>$0.00</span></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Expected on</span><span>Jul 01, 2026 &#9432; &nbsp;<b>$30.00</b></span></div>
  </div>
  <div style="text-align:center;margin:14px 0 0;font-size:13.5px"><span class="lnk">&#9432; What should I do with my paper check?</span></div>
  <div class="bbtns" style="bottom:20px"><div class="btn" style="margin:0">Deposit another check</div><div class="btn gray" style="margin:10px 16px">Close</div></div>
</div>{sb()}<div class="hi"></div>'''
    # main deposit screen
    amt = "$30.00" if stage=="amount" else "$0.00"
    amtcolor = "" if stage=="amount" else "color:#c6c9cd"
    return sb() + nav("QuickDeposit&trade;", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div class="tabs"><div class="on">Deposit check</div><div>See activity</div></div>
  <div style="margin:12px 16px 0;background:#E8F1FF;border-radius:8px;padding:10px 12px;font-size:12px;line-height:1.45;color:#3c4043">If you deposit a check that isn't made out to you directly, we may not be able to accept it. <span class="lnk">Learn more about restricted checks</span></div>
  <div style="margin:12px 16px 0;border:1px solid var(--line);border-radius:10px;padding:11px 13px;display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--ink2)">Deposit to</span><span><b>TOTAL CHECKING (&hellip;4821)</b><br><span style="color:var(--ink2);font-size:12px">$2,436.19</span></span></div>
  <div style="text-align:center;margin-top:16px"><div style="font-size:12.5px;color:var(--ink2)">Deposit amount</div>
    <div style="font-size:31px;font-weight:600;margin-top:4px;{amtcolor}">{amt}</div>
    <div style="font-size:12px;color:var(--ink2);margin-top:8px">Your current mobile deposit limit is $7,500.00</div>
    <div style="font-size:12.5px;margin-top:6px"><span class="lnk">&#9432; Learn more</span></div></div>
  <div style="display:flex;gap:14px;justify-content:center;margin-top:18px">
    <div style="text-align:center"><div style="font-size:11.5px;color:var(--ink2);margin-bottom:5px">Front</div><div style="width:104px;height:64px;border-radius:6px;border:1.5px dashed #b9bcc2;display:flex;align-items:center;justify-content:center;color:var(--ink2);font-size:18px">&#128247;</div></div>
    <div style="text-align:center"><div style="font-size:11.5px;color:var(--ink2);margin-bottom:5px">Back</div><div style="width:104px;height:64px;border-radius:6px;border:1.5px dashed #b9bcc2;display:flex;align-items:center;justify-content:center;color:var(--ink2);font-size:18px">&#128247;</div></div>
  </div>
  <p class="body" style="font-size:11.5px;margin:14px 20px 0">Money transmitted by J.P.M ET on business days should be available on the next business day.</p>
</div>{sb()}<div class="hi"></div>'''

def t_pay_transfer():
    items = [("&#9635;","Pay bills"),("&#10148;","Send money with Zelle&reg;"),("&#127760;","Wires &amp; global transfers"),("&#8644;","Transfer"),("&#128438;","Deposit checks")]
    qa = "".join(f'<div style="flex:1;text-align:center;font-size:10.5px;color:#fff"><div style="width:44px;height:44px;margin:0 auto 5px;border-radius:50%;background:rgba(255,255,255,.16);display:flex;align-items:center;justify-content:center;font-size:17px">{i}</div>{n}</div>' for i,n in items)
    return sb(True) + f'''
<div style="position:absolute;top:0;left:0;right:0;height:150px;background:linear-gradient(160deg,#0B57C2,#0846A8)"></div>
<div style="position:absolute;top:52px;left:0;right:0;color:#fff">
  <div style="font-size:23px;font-weight:600;padding:4px 20px 10px">Pay &amp; Transfer</div>
  <div style="margin:0 16px 10px;background:rgba(255,255,255,.12);border-radius:10px;padding:9px 12px;font-size:12px">&#9888; You have 1 message that requires immediate action.</div>
  <div style="display:flex;padding:0 8px">{qa}</div>
</div>
<div style="position:absolute;top:212px;left:0;right:0;bottom:80px;background:var(--bg);border-radius:22px 22px 0 0"></div>
<div style="position:absolute;top:226px;left:0;right:0">
  <div class="rows" style="margin-top:0"><div class="row"><span class="ico">&#9776;</span><div class="g">See activity</div><span class="chev">&rsaquo;</span></div>
  <div class="row"><span class="ico">&#127760;</span><div class="g">Manage external accounts</div><span class="chev">&rsaquo;</span></div></div>
</div>{tabbar(1)}{sb(True)}<div class="hi lt"></div>'''

def t_xfer(stage="form"):
    filled = stage in ("filled","review")
    amt = "$5.00" if filled else "$0.00"
    frm = "<b>TOTAL CHECKING (&hellip;4821)</b> <span style='color:var(--ink2);font-size:12px'>$2,436.19</span>" if filled else "Choose an account"
    to = "<b>360 Performance Savings (&hellip;8535)</b>" if filled else "Choose an account"
    dm = "Real-time" if filled else ""
    if stage=="pick":
        return sb() + nav("Schedule a Transfer", action="Cancel") + f'''
<div style="position:absolute;top:99px;left:0;right:0;bottom:0;background:rgba(40,40,44,.45)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:22px 22px 0 0;padding:14px 18px 40px;z-index:49">
  <div style="display:flex;justify-content:space-between;align-items:center;font-size:17px;font-weight:600">Transfer from <span style="color:var(--ink2);font-size:15px">&#10005;</span></div>
  <div class="sec" style="padding-left:0">Internal accounts</div>
  <div style="padding:11px 0;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;font-size:14.5px"><b>TOTAL CHECKING (&hellip;4821)</b><span>$2,436.19</span></div>
  <div class="sec" style="padding-left:0">External accounts</div>
  <div style="padding:11px 0;border-bottom:1px solid var(--line);font-size:14.5px">360 Performance Savings (&hellip;8535)</div>
  <div style="display:flex;align-items:center;gap:8px;padding:13px 0;font-size:14.5px;color:var(--blue);font-weight:600">&#8862; Link an external account</div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="delivery":
        return sb() + nav("Schedule a Transfer", action="Cancel") + f'''
<div style="position:absolute;top:99px;left:0;right:0;bottom:0;background:rgba(40,40,44,.45)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:22px 22px 0 0;padding:14px 18px 30px;z-index:49">
  <div style="display:flex;justify-content:space-between;align-items:center;font-size:17px;font-weight:600">Choose a delivery method <span style="color:var(--ink2);font-size:15px">&#10005;</span></div>
  <div style="padding:13px 0;border-bottom:1px solid var(--line)">
    <div style="display:flex;align-items:center"><b style="flex:1;font-size:15px">Real-time</b><span style="width:19px;height:19px;border-radius:50%;border:6px solid var(--blue)"></span></div>
    <div style="font-size:12.5px;color:var(--ink2);margin-top:4px">Sent in moments</div>
    <div style="font-size:12.5px;color:var(--ink2)">&bull; Limited to $5,000 per transfer</div>
    <div style="font-size:12.5px;color:var(--ink2)">&bull; You aren't able to cancel same-day real-time transfers</div>
  </div>
  <div style="padding:13px 0">
    <div style="display:flex;align-items:center"><b style="flex:1;font-size:15px">Standard</b><span style="width:19px;height:19px;border-radius:50%;border:2px solid #b9bcc2"></span></div>
    <div style="font-size:12.5px;color:var(--ink2);margin-top:4px">Sent in 1-2 business days</div>
    <div style="font-size:12.5px;color:var(--ink2)">&bull; Higher maximum limits</div>
    <div style="font-size:12.5px;color:var(--ink2)">&bull; You can cancel most standard transfers</div>
  </div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="review":
        return sb() + nav("Review", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 20px 0;text-align:center;font-size:19px;font-weight:600">Does everything look OK?</div>
  <div style="margin:16px 20px 0;font-size:13.5px">
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Amount</span><b>$5.00</b></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Transfer from</span><b>TOTAL CHECKING (&hellip;4821)</b></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Transfer to</span><b>360 Performance Savings (&hellip;8535)</b></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Delivery method</span><span>Real-time</span></div>
    <div style="display:flex;padding:8px 0;border-bottom:1px solid var(--line)"><span style="width:130px;color:var(--ink2)">Transfer date</span><span>Jun 30, 2026</span></div>
  </div>
  <p class="body" style="font-size:12.5px;margin:14px 20px 0">Keep in mind, you can't cancel same-day real-time transfers. The terms of the Transfer Agreement apply to these transactions.</p>
  <div class="bbtns"><div class="btn" style="margin:0">Schedule transfer</div></div>
</div>{sb()}<div class="hi"></div>'''
    return sb() + nav("Schedule a Transfer", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 20px 0;text-align:center">
    <div style="font-size:12.5px;color:var(--ink2)">Amount</div>
    <div style="font-size:31px;font-weight:600;margin-top:4px;color:{'#1a1a1a' if filled else '#c6c9cd'}">{amt}</div>
    <div style="font-size:11.5px;color:var(--ink2);border-bottom:1px solid var(--line);padding-bottom:10px">Limited to $5,000.00 per transfer</div>
  </div>
  <div style="margin:14px 20px 0;font-size:13.5px">
    <div style="padding:10px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Transfer from</div><div style="margin-top:3px">{frm}</div></div>
    <div style="padding:10px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Transfer to</div><div style="margin-top:3px">{to}</div></div>
    <div style="padding:10px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Transfer on</div><div style="margin-top:3px">Today &#9662;</div></div>
    <div style="padding:10px 0"><div style="font-size:12px;color:var(--ink2)">Note to self (optional) <span style="color:var(--blue)">What's this for?</span></div><div style="margin-top:3px;color:#c6c9cd">24 of 32 characters remaining</div></div>
  </div>
  {'<div style="text-align:center;font-size:12.5px"><span class="lnk">Learn more about real-time transfers &#9432;</span></div>' if filled else ''}
  <div class="bbtns"><div class="btn" style="margin:0">{'Next' if not filled else 'Review'}</div></div>
</div>{sb()}<div class="hi"></div>'''

def t_wire(stage="intro"):
    if stage=="intro":
        return sb() + nav("Send Money", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:22px 24px 0">
    <div style="font-size:22px;font-weight:600">The Smart Way to Move Money</div>
    <p class="body" style="margin-top:8px">Sending money to a friend or relative? Or an employee or vendor?</p>
  </div>
  <div style="margin:22px 24px 0;text-align:center">
    <div style="margin-bottom:20px"><div style="font-size:24px;color:var(--blue)">&#127760;</div><b style="font-size:14.5px">Send money domestically &amp; worldwide</b><div class="body" style="font-size:13px">Schedule transactions 24/7</div></div>
    <div style="margin-bottom:20px"><div style="font-size:24px;color:var(--blue)">&#128737;</div><b style="font-size:14.5px">Security you've come to trust</b><div class="body" style="font-size:13px">We go above and beyond to keep your money safe</div></div>
    <div><div style="font-size:24px;color:var(--blue)">&#9878;</div><b style="font-size:14.5px">Transparent pricing</b><div class="body" style="font-size:13px">Know exactly how much you're going to pay</div></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="purpose":
        opts = ["Paying a friend, family or trusted person","Paying a bank, company or government agency","Paying a seller or service provider","Buying a property or investment","Investing in cryptocurrency","Something else"]
        o = "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:13px 0;border-bottom:1px solid var(--line);font-size:14.5px"><span style="flex:1">{x}</span><span style="width:19px;height:19px;border-radius:50%;border:2px solid #b9bcc2;flex:none"></span></div>' for x in opts)
        return sb() + nav("Choose Payment Purpose", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0"><h1 class="s" style="font-size:21px">Why are you sending money to this recipient?</h1>
  <p class="body" style="font-size:13.5px">This is to help keep you safe from scams.</p>
  <div style="font-size:12.5px;font-weight:600;color:var(--ink2);margin:14px 0 2px">Choose an option</div></div>
  <div style="margin:0 20px">{o}</div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="scam":
        return sb() + nav("Stay Safe from Scams") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:20px 24px 0"><div style="width:56px;height:56px;border-radius:50%;background:#7C2E8E;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;font-weight:700">!</div>
  <div style="font-size:20px;font-weight:600;line-height:1.3">Look out for romance and family impersonator scams</div></div>
  <div style="margin:16px 20px 0;background:#F4ECF8;border-radius:10px;padding:12px 14px;font-size:13px;line-height:1.5"><b>Before you send any money, consider these tips to protect yourself:</b>
  <div style="margin-top:8px">&bull; If a family member asked you for money online, first call to verify it's really them.</div>
  <div style="margin-top:5px">&bull; Impersonators may use a sense of urgency, like claiming they're in some sort of trouble.</div>
  <div style="margin-top:5px">&bull; People fall in love online - avoid giving money to anyone you haven't met in person.</div>
  <div style="margin-top:5px">&bull; Consider what you've shared online - scammers may use it to target you.</div></div>
  <div style="display:flex;gap:10px;margin:16px 20px 0;align-items:flex-start"><span style="width:19px;height:19px;border-radius:4px;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;flex:none">&#10003;</span><span style="font-size:12.5px">I understand the potential scam risks of scheduling this wire, and I understand that it's very unlikely I'll get my money back once it's sent.</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Continue</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="bank_ok":
        valid = '''<div style="margin:14px 20px 0;background:#E8F1FF;border-radius:10px;padding:12px 14px;font-size:13px;line-height:1.5"><b>The wire routing number you entered is registered with:</b><div style="margin-top:5px"><b>Bank of America, National Association</b></div><div style="margin-top:6px;color:var(--ink2)">If this bank doesn't match the bank on your wire instructions, confirm with your recipient.</div></div>'''
        fields = '''<div style="margin:16px 20px 0;font-size:13.5px">
          <div class="lbl" style="margin-top:0">Bank country</div><div class="field" style="justify-content:space-between"><span>United States of America</span><span>&#9662;</span></div>
          <div class="lbl">Wire routing number</div><div class="field" style="justify-content:space-between"><span>026009593</span><span style="color:var(--ink2);font-size:12px">9 of 9</span></div>
          <div class="lbl">Account number</div><div class="field" style="color:#c6c9cd">Enter account number</div></div>'''
        return sb() + nav("Step 1 of 3", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:18px 24px 0"><div style="width:52px;height:52px;border-radius:50%;background:#E8F1FF;margin:0 auto 10px;display:flex;align-items:center;justify-content:center;font-size:22px">&#128100;</div>
  <div style="font-size:20px;font-weight:600">Add recipient bank details</div>
  <p class="body" style="font-size:13px;margin-top:6px">Make sure these details match your recipient's bank records.</p></div>
  {fields}{valid}
</div>{sb()}<div class="hi"></div>'''
    if stage=="bank":
        return sb() + nav("Step 1 of 3", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:18px 24px 0"><div style="width:52px;height:52px;border-radius:50%;background:#E8F1FF;margin:0 auto 10px;display:flex;align-items:center;justify-content:center;font-size:22px">&#128100;</div>
  <div style="font-size:20px;font-weight:600">Add recipient bank details</div>
  <p class="body" style="font-size:13px;margin-top:6px">Make sure these details match your recipient's bank records.</p></div>
  <div style="margin:16px 20px 0;font-size:13.5px">
    <div class="lbl" style="margin-top:0">Bank country</div><div class="field" style="justify-content:space-between"><span>United States of America</span><span>&#9662;</span></div>
    <div class="lbl">Wire routing number</div><div class="field" style="color:#c6c9cd">Enter 9-digit wire routing number</div>
    <div class="lbl">Account number</div><div class="field" style="color:#c6c9cd">Enter account number</div>
    <div class="lbl">Verify account number</div><div class="field" style="color:#c6c9cd">Re-enter account number</div>
    <div class="lbl">Recipient account type</div><div class="field" style="justify-content:space-between"><span>Individual or business</span><span>&#9662;</span></div>
  </div>
  <div class="bbtns"><div class="btn gray" style="margin:0">Next</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="recipient":
        return sb() + nav("Step 2 of 3", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="text-align:center;padding:18px 24px 0"><div style="width:52px;height:52px;border-radius:50%;background:#E8F1FF;margin:0 auto 10px;display:flex;align-items:center;justify-content:center;font-size:22px">&#128100;</div>
  <div style="font-size:20px;font-weight:600">Add recipient details</div></div>
  <div style="margin:14px 20px 0;font-size:13.5px">
    <div class="lbl" style="margin-top:0">First name</div><div class="field">Joe</div>
    <div class="lbl">Last name</div><div class="field">Doe</div>
    <div class="lbl">Nickname</div><div class="field">Doe</div>
    <div class="lbl">Address</div><div class="field" style="height:auto;padding:10px 12px">123, House, Houston, TX 77380<br>United States of America &#127482;&#127480;</div>
  </div>
  <div style="display:flex;gap:10px;margin:14px 20px 0;align-items:flex-start"><span style="width:19px;height:19px;border-radius:4px;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;flex:none">&#10003;</span><span style="font-size:12px">I confirm that my recipient's account details match their bank records, and I understand that it's very unlikely I'll get my money back once it's sent.</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Add recipient</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="review":
        return sb() + nav("Step 3 of 3", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0"><h1 class="s" style="font-size:21px">Does everything look OK?</h1></div>
  <div style="margin:0 20px;font-size:13.5px">
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:150px;color:var(--ink2)">Wire routing number</span><b>026009593</b></div>
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:150px;color:var(--ink2)">Bank name</span><b>Bank of America, National Association</b></div>
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:150px;color:var(--ink2)">Account number</span><span>456789123456</span></div>
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:150px;color:var(--ink2)">Recipient account type</span><span>Individual</span></div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin:14px 20px 0;font-size:14px"><b>Recipient details</b><span class="lnk">&#9998; Edit</span></div>
  <div style="margin:6px 20px 0;font-size:13.5px;color:var(--ink2)">Joe Doe &middot; 123, House, Houston, TX 77380, United States of America</div>
  <div style="display:flex;gap:10px;margin:16px 20px 0;align-items:flex-start"><span style="width:19px;height:19px;border-radius:4px;background:var(--blue);color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;flex:none">&#10003;</span><span style="font-size:12px">I confirm that my recipient's account details match their bank records, and I understand that it's very unlikely I'll get my money back once it's sent.</span></div>
  <div class="bbtns"><div class="btn" style="margin:0">Add recipient</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="ok":
        return sb() + nav("You're all set") + f'''
<div class="content w" style="background:#fff">
  <div class="green-check"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>
  <div style="text-align:center;font-size:22px;font-weight:600;margin-top:12px">You're all set</div>
  <div style="text-align:center;font-size:13.5px;color:var(--ink2);margin-top:4px">You've added Joe as a recipient.</div>
  <div class="sec">Recipient bank details</div>
  <div style="margin:0 20px;font-size:13.5px">
    <div style="display:flex;padding:6px 0;border-bottom:1px solid var(--line)"><span style="width:150px;color:var(--ink2)">Wire routing number</span><span>026009593</span></div>
    <div style="display:flex;padding:6px 0;border-bottom:1px solid var(--line)"><span style="width:150px;color:var(--ink2)">Bank name</span><span>Bank of America, National Association</span></div>
    <div style="display:flex;padding:6px 0"><span style="width:150px;color:var(--ink2)">Account number</span><span>456789123456</span></div>
  </div>
  <div class="sec">Recipient details</div>
  <div style="margin:0 20px;font-size:13.5px;color:var(--ink2)">First name Joe &middot; Last name Doe &middot; 123, House, Houston, TX 77380, United States of America</div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="schedule":
        return sb() + nav("Schedule Transfer", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="margin:12px 20px 0;font-size:13.5px">
    <div style="padding:9px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Wire to</div><div style="margin-top:3px">Joe (&hellip;3456) &#9662;</div></div>
    <div style="padding:9px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Wire from</div><div style="margin-top:3px"><b>TOTAL CHECKING (&hellip;4821)</b> <span style="color:var(--ink2);font-size:12px">$2,436.19</span></div></div>
    <div style="padding:9px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Wire amount</div><div style="margin-top:3px;font-size:22px;font-weight:600;color:#c6c9cd">$0.00</div></div>
  </div>
  <div style="margin:8px 20px 0;font-size:12px;color:var(--ink2)">Your daily online wire limit is $25,000.00. If you need to send more, visit a Chase branch.</div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin:12px 20px 0;padding:9px 0;border-bottom:1px solid var(--line);font-size:13.5px"><span>Make this a repeating wire</span><span style="width:40px;height:24px;border-radius:12px;background:#d5d8dc;position:relative"><span style="position:absolute;top:2px;left:2px;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.2)"></span></span></div>
  <div style="margin:0 20px;padding:9px 0;border-bottom:1px solid var(--line);font-size:13.5px"><div style="font-size:12px;color:var(--ink2)">Wire date</div><div style="margin-top:3px">07/01/2026 &#128197;</div></div>
  <div style="margin:0 20px;padding:9px 0;border-bottom:1px solid var(--line);font-size:13.5px"><div style="font-size:12px;color:var(--ink2)">Payment purpose</div><div style="margin-top:3px">Paying a friend, family or trusted person &#9662;</div></div>
  <div style="margin:0 20px;font-size:13.5px">
    <div style="padding:9px 0;border-bottom:1px solid var(--line)"><div style="font-size:12px;color:var(--ink2)">Message to recipient (optional)</div><div style="margin-top:3px;color:#c6c9cd">140 characters remaining</div></div>
    <div style="padding:9px 0"><div style="font-size:12px;color:var(--ink2)">Memo (optional)</div><div style="margin-top:3px;color:#c6c9cd">100 characters remaining</div></div>
  </div>
  <div class="bbtns"><div class="btn" style="margin:0">Next</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="verify":
        return sb() + nav("Verify Sender", action="Cancel") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:14px 20px 0;text-align:center;font-size:19px;font-weight:600">Does everything look OK?</div>
  <div style="margin:14px 20px 0;font-size:13.5px">
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Wire to</span><b>Joe (&hellip;3456)</b></div>
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Wire from</span><b>TOTAL CHECKING (&hellip;4821)</b></div>
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Wire amount</span><b>$30.00</b></div>
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)">Wire transfer fee</span><span>$25.00</span></div>
    <div style="display:flex;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:120px;color:var(--ink2)"><b>Total</b></span><b>$55.00</b></div>
  </div>
  <p class="body" style="font-size:12px;margin:12px 20px 0">A $25.00 online wire fee applies. Additional charges for non-sufficient funds may apply. For same-day wires, you don't have the option to cancel once sent.</p>
  <div class="bbtns"><div class="btn" style="margin:0">Schedule wire</div></div>
</div>{sb()}<div class="hi"></div>'''
    if stage=="intl":
        return sb() + nav("Wires &amp; global transfers") + f'''
<div class="content w" style="background:#fff">
  <div style="padding:16px 20px 0;text-align:center"><div style="font-size:19px;font-weight:600;line-height:1.35">Send money safely for the payments that matter most</div></div>
  <div style="display:flex;margin:16px 20px 0;background:#EDEFF2;border-radius:10px;padding:4px">
    <div style="flex:1;text-align:center;padding:9px 0;font-size:13.5px;font-weight:600;color:var(--ink2);border-radius:8px">Domestic (U.S.)</div>
    <div style="flex:1;text-align:center;padding:9px 0;font-size:13.5px;font-weight:600;background:#fff;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,.15);outline:3px solid #FFB300;outline-offset:-3px">International</div>
  </div>
  <div class="sec">What to have ready</div>
  <div style="margin:0 20px;font-size:13px;line-height:1.6;color:#3c4043">&bull; Recipient's full name or business name<br>&bull; Recipient country and their bank details<br>&bull; For some countries, the recipient's SWIFT code or BIC</div>
  <div class="sec">Delivery time</div>
  <div style="margin:0 20px;font-size:13px;color:#3c4043">Most international wires arrive within 2 to 5 business days. You can check your status on the 'Payment activity' page.</div>
  <div class="sec">Daily limit</div>
  <div style="margin:0 20px 10px;font-size:13px;color:#3c4043">Your daily online wire limit is $25,000.00.</div>
</div>{tabbar(1)}{sb()}<div class="hi"></div>'''
    return t_wire("intro")
