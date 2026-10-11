"""Desktop (chase.com / partner site) screens — 1440x900 design space, rendered @2x."""
import chase_ui as _c

def _logo(size=30, color="#0B4DA2"):
    return _c.logo(size, color)

FOOTER = ('<div style="position:absolute;bottom:0;left:0;right:0;background:#F6F6F6;border-top:1px solid #e3e3e3;'
          'padding:16px 60px;font-size:12.5px;color:#5f6368;display:flex;gap:26px;align-items:center">'
          '<span>&copy; 2026 JPMorgan Chase &amp; Co.</span><span>Member FDIC</span>'
          '<span>Equal Housing Opportunity</span>'
          '<span style="margin-left:auto">Privacy &nbsp;&middot;&nbsp; Security &nbsp;&middot;&nbsp; Terms of Use</span></div>')
IS_DESKTOP = False

def _d(head, body, cta=None):
    logo = ('<span style="display:flex;align-items:center;gap:10px">' + _logo(32) +
            '<span style="font-weight:700;font-size:23px;letter-spacing:.4px;color:#1a1a1a">CHASE</span></span>')
    c = ('<div style="margin:26px 0 90px;background:#0060F0;color:#fff;display:inline-block;'
         'padding:14px 34px;border-radius:4px;font-weight:600;font-size:16px">' + cta + '</div>') if cta else ""
    return ('<div style="position:absolute;inset:0;background:#fff"></div>'
            '<div style="position:absolute;inset:0;overflow:hidden">'
            '<div style="background:#fff;border-bottom:1px solid #e3e3e3;padding:14px 60px;'
            'display:flex;align-items:center;gap:16px;box-shadow:0 1px 4px rgba(0,0,0,.06)">' + logo +
            '<span style="margin-left:auto;display:flex;align-items:center;gap:22px">'
            '<span style="color:#5f6368;font-size:14px">&#9906; Search</span>'
            '<span style="color:#0060F0;font-weight:600;font-size:15.5px">Sign in</span></span></div>'
            '<div style="padding:26px 60px 0">' + head + body + c + '</div>' + FOOTER + '</div>')

def d_web(title, crumb, body, cta=None):
    global IS_DESKTOP; IS_DESKTOP = True
    head = ('<div style="font-size:13.5px;color:#5f6368">' + crumb + '</div>'
            '<div style="padding-top:8px;font-size:38px;font-weight:300;color:#1a1a1a">' + title + '</div>')
    return _d(head, '<div style="margin-top:18px;font-size:16.5px;line-height:1.65;color:#3c4043;max-width:880px">' + body + '</div>', cta)

def d_ur(stage="signin", highlight=None):
    global IS_DESKTOP; IS_DESKTOP = True
    if stage == "signin":
        return ('<div style="position:absolute;inset:0;background:#fff"></div>'
          '<div style="position:absolute;inset:0;overflow:hidden">'
          '<div style="background:#F6F6F6;border-bottom:1px solid #e3e3e3;padding:16px 60px;display:flex;align-items:center;gap:16px">'
          '<span style="font-weight:700;font-size:22px">CHASE <span style="display:inline-block;width:20px;height:20px;background:#0846A8;border-radius:4px;vertical-align:-3px"></span></span>'
          '<span style="margin-left:auto;font-size:14px;color:#5f6368">Easy to sign in &mdash; not enrolled? <span style="color:#0060F0;font-weight:600">Sign up now</span></span></div>'
          '<div style="width:460px;margin:44px auto 0;border:1px solid #e3e3e3;border-radius:8px;padding:30px 34px">'
          '<div style="font-size:30px;font-weight:300">Sign in</div>'
          '<div style="font-size:12.5px;color:#5f6368;margin:6px 0 14px">Ultimate Rewards&reg;</div>'
          '<div style="font-size:12.5px;color:#5f6368;margin-bottom:5px">Username</div><div class="field" style="height:44px">jordan.avery4821</div>'
          '<div style="font-size:12.5px;color:#5f6368;margin:12px 0 5px">Password</div><div class="field" style="height:44px;letter-spacing:2px">&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;</div>'
          '<div style="margin-top:18px;background:#0060F0;color:#fff;border-radius:4px;height:48px;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:15px">Sign in</div>'
          '<div style="margin-top:12px;font-size:13.5px;color:#0060F0;font-weight:600">Forgot username/password?</div></div></div>')
    if stage in ("home", "home_menu"):
        menu = ('<div style="position:absolute;top:64px;right:60px;width:280px;background:#fff;border:1px solid #e3e3e3;'
          'border-radius:8px;box-shadow:0 10px 30px rgba(0,0,0,.16);z-index:49;padding:6px 0">'
          '<div style="padding:12px 18px;font-size:15px">Book travel</div>'
          '<div style="padding:12px 18px;font-size:15px">Points details</div>'
          '<div class="hl" style="padding:12px 18px;font-size:15px"><b>Transfer points to partners</b>'
          '<div style="font-size:11.5px;color:#8a6d00;font-weight:400">TAP HERE</div></div>'
          '<div style="padding:12px 18px;font-size:15px">Combine points</div></div>') if stage == "home_menu" else ""
        cards = "".join('<div style="flex:1;border:1px solid #e3e3e3;border-radius:8px;padding:20px">'
                        '<b style="font-size:16px">' + t + '</b><div style="font-size:13.5px;color:#5f6368;margin-top:5px">' + s + '</div></div>'
                        for t, s in [("Book travel", "Flights, hotels, cars and more"),
                                     ("Transfer points", "Send points to airline and hotel partners"),
                                     ("Redeem for cash back", "Statement credit or deposit")])
        return ('<div style="position:absolute;inset:0;background:#fff"></div>'
          '<div style="position:absolute;inset:0;overflow:hidden">'
          '<div style="background:#fff;border-bottom:1px solid #e3e3e3;padding:14px 60px;display:flex;align-items:center;gap:14px">'
          + _logo(30) + '<span style="font-weight:600;font-size:16.5px;color:#1a1a1a">Ultimate Rewards&reg;</span>'
          '<span style="margin-left:auto;display:flex;align-items:center;gap:20px">'
          '<span style="font-size:14px;color:#0060F0;font-weight:600">Travel &#9662;</span>'
          '<span style="font-size:14px;color:#0060F0;font-weight:600">Redeem &#9662;</span>'
          '<span style="font-size:14px;color:#0060F0;font-weight:600">Earn &#9662;</span>'
          '<span style="width:34px;height:34px;border-radius:50%;background:#E8F1FF;display:flex;align-items:center;justify-content:center;color:#0B4DA2;font-weight:700;font-size:13px">JA</span></span></div>'
          '<div style="padding:30px 60px 0"><div style="font-size:16px;color:#5f6368">Ultimate Rewards&reg; points balance</div>'
          '<div style="font-size:52px;font-weight:300;margin-top:4px">85,000</div>'
          '<div style="display:flex;gap:16px;margin-top:26px">' + cards + '</div>'
          '<div style="display:flex;gap:16px;margin-top:26px">'
          '<div style="flex:1.3;border:1px solid #e3e3e3;border-radius:8px;padding:20px"><b style="font-size:15.5px">Recent activity</b>'
          '<div style="font-size:13.5px;color:#5f6368;margin-top:10px;display:flex;justify-content:space-between"><span>10,000 points transferred to United MileagePlus</span><span>Sep 28, 2026</span></div>'
          '<div style="font-size:13.5px;color:#5f6368;margin-top:8px;display:flex;justify-content:space-between"><span>2,500 points earned &mdash; dining</span><span>Sep 21, 2026</span></div>'
          '<div style="font-size:13.5px;color:#5f6368;margin-top:8px;display:flex;justify-content:space-between"><span>$50 statement credit redeemed</span><span>Sep 12, 2026</span></div></div>'
          '<div style="flex:1;border:1px solid #e3e3e3;border-radius:8px;padding:20px"><b style="font-size:15.5px">Ways to redeem</b>'
          '<div style="font-size:13.5px;color:#5f6368;margin-top:10px">&bull; Travel through Chase Travel&trade;</div>'
          '<div style="font-size:13.5px;color:#5f6368;margin-top:6px">&bull; Transfer to airline and hotel partners</div>'
          '<div style="font-size:13.5px;color:#5f6368;margin-top:6px">&bull; Cash back, gift cards and more</div></div></div></div>'
          + FOOTER + menu + '</div>')
    if stage == "partners":
        hl = highlight or "United Airlines MileagePlus"
        airlines = ["United Airlines MileagePlus", "British Airways Club", "Aeroplan (Air Canada)",
                    "Flying Blue (Air France-KLM)", "Iberia Club", "JetBlue TrueBlue", "KrisFlyer (Singapore)",
                    "AerClub (Aer Lingus)", "Rapid Rewards (Southwest)", "Virgin Atlantic Flying Club"]
        hotels = ["World of Hyatt", "Marriott Bonvoy", "IHG One Rewards", "Wyndham Rewards"]
        def lst(items):
            o = ""
            for a in items:
                hlstyle = ';outline:3px solid #FFB300;outline-offset:-3px' if a == hl else ''
                o += ('<div style="display:flex;align-items:center;gap:12px;padding:11px 16px;'
                      'border-bottom:1px solid #e3e3e3;font-size:14.5px' + hlstyle + '">'
                      '<span style="width:28px;height:28px;border-radius:50%;background:#E8F1FF;flex:none"></span>'
                      '<span style="flex:1">' + a + '</span><b style="font-size:12.5px;color:#5f6368">1:1</b></div>')
            return o
        return ('<div style="position:absolute;inset:0;background:#fff"></div>'
          '<div style="position:absolute;inset:0;overflow:hidden">'
          '<div style="background:linear-gradient(90deg,#123A80,#1C4C9C);color:#fff;padding:16px 60px;font-weight:600;font-size:17px">Transfer points to travel partners</div>'
          '<div style="display:flex;gap:40px;padding:26px 60px 0">'
          '<div style="flex:1.2"><div style="font-size:15px;font-weight:600;margin-bottom:10px">AIRLINE PARTNERS</div>'
          '<div style="border:1px solid #e3e3e3;border-radius:8px;overflow:hidden">' + lst(airlines) + '</div></div>'
          '<div style="flex:1"><div style="font-size:15px;font-weight:600;margin-bottom:10px">HOTEL PARTNERS</div>'
          '<div style="border:1px solid #e3e3e3;border-radius:8px;overflow:hidden">' + lst(hotels) + '</div></div></div>'
          '<div style="margin:16px 60px;font-size:12.5px;color:#5f6368">Points transfer in increments of 1,000. Transfers are final and cannot be reversed.</div></div>')
    if stage == "transfer":
        return ('<div style="position:absolute;inset:0;background:#fff"></div>'
          '<div style="position:absolute;inset:0;overflow:hidden">'
          '<div style="background:linear-gradient(90deg,#123A80,#1C4C9C);color:#fff;padding:16px 60px;font-weight:600;font-size:17px">Transfer to United Airlines MileagePlus</div>'
          '<div style="width:560px;margin:30px auto 0;border:1px solid #e3e3e3;border-radius:8px;padding:24px 28px">'
          '<div style="font-size:12.5px;color:#5f6368;margin-bottom:5px">Frequent flyer number</div><div class="field" style="height:44px">JH48219</div>'
          '<div style="font-size:12.5px;color:#5f6368;margin:14px 0 5px">Points to transfer</div><div class="field" style="height:52px;font-size:20px;font-weight:600;color:#1a1a1a">50,000</div>'
          '<div style="font-size:12px;color:#5f6368;margin-top:8px">In increments of 1,000 points. 1:1 transfer ratio. Transfers are final.</div>'
          '<div style="font-size:13.5px;color:#5f6368;margin-top:12px">Recipient: <b style="color:#1a1a1a">JORDAN AVERY</b> (name must match your program account)</div>'
          '<div style="margin-top:18px;background:#0060F0;color:#fff;border-radius:4px;height:48px;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:15px">Transfer points</div></div></div>')
    if stage == "done":
        return ('<div style="position:absolute;inset:0;background:#fff"></div>'
          '<div style="position:absolute;inset:0;overflow:hidden">'
          '<div style="width:600px;margin:60px auto 0;text-align:center">'
          '<div class="green-check" style="margin:0 auto"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M4 12.5 10 18 20 6"/></svg></div>'
          '<div style="font-size:30px;font-weight:300;margin-top:16px">Your transfer is submitted</div>'
          '<p style="font-size:16px;color:#3c4043;margin-top:12px">50,000 Ultimate Rewards&reg; points to <b>United Airlines MileagePlus</b>. Most transfers process by the next business day, but may take up to 7 business days. Transfers are final.</p></div></div>')
    return d_ur("home")

def d_brand(brand, title, body, cta="Search flights"):
    global IS_DESKTOP; IS_DESKTOP = True
    colors = {"BA": "#075AAA", "United": "#0B2C71", "Aeroplan": "#C8102E", "Hyatt": "#B22517",
              "Chase Travel": "#0846A8", "Atmos": "#0B3D5C"}
    c = colors.get(brand, "#333")
    return ('<div style="position:absolute;inset:0;background:#fff"></div>'
      '<div style="position:absolute;inset:0;overflow:hidden">'
      '<div style="background:' + c + ';color:#fff;padding:18px 60px;font-weight:700;font-size:22px">' + brand + '</div>'
      '<div style="padding:28px 60px 0;max-width:960px">'
      '<div style="font-size:32px;font-weight:600">' + title + '</div>'
      '<div style="margin-top:20px;display:flex;gap:14px">'
      '<div style="flex:1.4"><div style="font-size:12.5px;color:#5f6368;margin-bottom:5px">From - To</div>'
      '<div class="field" style="height:48px;justify-content:space-between"><span>New York (JFK) - Los Angeles (LAX)</span><span>&#8644;</span></div></div>'
      '<div style="flex:1"><div style="font-size:12.5px;color:#5f6368;margin-bottom:5px">Dates</div><div class="field" style="height:48px">Nov 12 - Nov 19</div></div></div>'
      '<div style="margin-top:22px;background:' + c + ';color:#fff;display:inline-block;padding:13px 30px;border-radius:4px;font-weight:600;font-size:15.5px">' + cta + '</div>'
      '<p style="margin-top:22px;font-size:15px;line-height:1.65;color:#3c4043;max-width:860px">' + body + '</p></div></div>')

def d_fee_table():
    global IS_DESKTOP; IS_DESKTOP = True
    body = ('<p>Chase Total Checking&reg; has a <b>$15 Monthly Service Fee</b> OR <b>$0</b> with any one of the following, each monthly statement period:</p>'
      '<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:15.5px;max-width:900px">'
      '<tr style="background:#F0F4FA"><td style="padding:12px 14px;border:1px solid #e3e3e3"><b>$500 or more</b> in qualifying electronic deposits (direct deposits)</td></tr>'
      '<tr><td style="padding:12px 14px;border:1px solid #e3e3e3"><b>$1,500 or more</b> balance at the beginning of each day</td></tr>'
      '<tr style="background:#F0F4FA"><td style="padding:12px 14px;border:1px solid #e3e3e3"><b>$5,000 or more</b> average beginning day balance (this account alone or with linked qualifying deposits/investments)</td></tr>'
      '<tr><td style="padding:12px 14px;border:1px solid #e3e3e3">Link a <b>qualifying Chase checking account</b></td></tr></table>'
      '<p style="margin-top:14px">The most popular option: set up <b>qualifying direct deposits of $500+</b>.</p>')
    return d_web("Chase Total Checking&reg; fees", "Chase &rsaquo; Checking &rsaquo; Chase Total Checking&reg;", body)

def d_locator(stage=0):
    global IS_DESKTOP; IS_DESKTOP = True
    if stage == 1:
        rows = [("Chase &mdash; Houston Main", "712 Main St, Houston, TX 77002 &middot; 0.4 mi", True),
                ("Chase &mdash; Capitol Street", "1018 Congress Ave, Houston, TX 77002 &middot; 0.8 mi", False),
                ("Chase &mdash; Bayou Place", "500 Texas St, Houston, TX 77002 &middot; 1.1 mi", False)]
        rr = ""
        for n, a, h in rows:
            hlstyle = ';outline:3px solid #FFB300;outline-offset:-3px' if h else ''
            rr += ('<div style="padding:16px 18px;border-bottom:1px solid #e3e3e3' + hlstyle + '">'
                   '<b style="font-size:15.5px">' + n + '</b><div style="font-size:13px;color:#5f6368;margin-top:3px">' + a + '</div>'
                   + ('<div style="font-size:13px;color:#0060F0;font-weight:600;margin-top:3px">Schedule a meeting &rsaquo;</div>' if h else '') + '</div>')
        return d_web("Branches near 77002", "Chase &rsaquo; Locator", '<div style="border:1px solid #e3e3e3;border-radius:8px;overflow:hidden;max-width:860px">' + rr + '</div>')
    body = ('<p>Meet with a banker or J.P. Morgan advisor &mdash; in person or virtually.</p>'
      '<div style="display:flex;gap:14px;margin-top:18px;max-width:640px">'
      '<div style="flex:1.4"><div style="font-size:12.5px;color:#5f6368;margin-bottom:5px">City or ZIP code</div><div class="field" style="height:48px">77002</div></div>'
      '<div style="flex:1"><div style="font-size:12.5px;color:#5f6368;margin-bottom:5px">Type</div><div class="field" style="height:48px;justify-content:space-between"><span>Branch</span><span>&#9662;</span></div></div></div>')
    return d_web("Schedule a meeting", "Chase &rsaquo; Locator", body, cta="Search")

def d_bizweb(stage=0):
    global IS_DESKTOP; IS_DESKTOP = True
    head = ('<div style="background:#0D2E6B;color:#fff;padding:16px 60px;display:flex;align-items:center;gap:14px;font-size:16px">'
            '<b>CHASE for Business</b><span style="margin-left:auto">&#128100; Jordan Avery</span></div>')
    if stage == 0:
        rows = [("Personal details", ""), ("Alerts", ""), ("Account settings", "hl"), ("Security preferences", "")]
        title = "Profile and settings"
    elif stage == 1:
        rows = [("Account display preferences", ""), ("Manage linked accounts", "hl"), ("Authorized signers", "")]
        title = "Account settings"
    elif stage == 2:
        rows = None
        title = "Manage linked accounts"
    else:
        rows = None
        title = "Accounts linked"
    if rows:
        rr = ""
        for n, c in rows:
            hlstyle = ';outline:3px solid #FFB300;outline-offset:-3px' if c == "hl" else ''
            inner = ('<b>' + n + '</b><div style="font-size:11.5px;color:#8a6d00;font-weight:600">TAP HERE</div>') if c == "hl" else n
            rr += ('<div style="padding:15px 18px;border-bottom:1px solid #e3e3e3' + hlstyle + '">' + inner + '</div>')
        body = ('<div style="font-size:32px;font-weight:300;margin-top:6px">' + title + '</div>'
                '<div style="margin:22px 0 0;border:1px solid #e3e3e3;border-radius:8px;overflow:hidden;max-width:760px;font-size:15.5px">' + rr + '</div>')
    elif stage == 2:
        body = ('<div style="font-size:32px;font-weight:300;margin-top:6px">' + title + '</div>'
          '<p style="margin-top:14px;font-size:15.5px;color:#3c4043">Choose how your accounts appear when you sign in.</p>'
          '<div style="margin-top:16px;border:1.5px solid #0060F0;border-radius:8px;padding:16px 18px;max-width:720px">'
          '<b style="font-size:15.5px">Show my accounts</b><div style="font-size:13.5px;color:#5f6368;margin-top:4px">Personal and business accounts appear together in one profile.</div></div>'
          '<div style="margin-top:12px;border:1px solid #e3e3e3;border-radius:8px;padding:16px 18px;max-width:720px;font-size:15.5px">Link a business relationship</div>'
          '<div style="margin-top:20px;background:#0060F0;color:#fff;display:inline-block;padding:13px 30px;border-radius:4px;font-weight:600;font-size:15px">Continue</div>')
    else:
        body = ('<div style="font-size:32px;font-weight:300;margin-top:6px">' + title + '</div>'
          '<div style="margin-top:18px;background:#EFF6EF;border:1px solid #BFE3C6;border-radius:8px;padding:18px 20px;max-width:760px;font-size:15.5px">'
          '<b>&#10003; Your business relationship was linked.</b>'
          '<div style="margin-top:6px;font-size:14px;color:#2E5E36">CHASE BUSINESS COMPLETE CHECKING (&hellip;3117) now appears with your personal accounts in Chase Mobile and on chase.com.</div></div>')
    return ('<div style="position:absolute;inset:0;background:#fff"></div>'
            '<div style="position:absolute;inset:0;overflow:hidden">' + head +
            '<div style="padding:22px 60px 0">' + body + '</div></div>')
