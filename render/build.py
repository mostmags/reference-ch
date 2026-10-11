"""Route every guide step to a template and render all topics."""
import json, os, re, glob, subprocess
import chase_ui as C
import render_all as R
import desktop as D
import desktop as DD

OVERRIDES={
 "how-to-book-hyatt-with-chase-points": lambda i: [D.d_ur("signin"),D.d_ur("home"),D.d_ur("home_menu"),D.d_ur("partners",highlight="World of Hyatt"),D.d_ur("partners",highlight="World of Hyatt"),D.d_brand("Hyatt","Find hotels with points","Search World of Hyatt award nights with points. Sapphire Reserve transfers 1:1; Sapphire Preferred and Ink Business Preferred transfer at 4:3 since Oct 1, 2026. Award stays earn Hyatt elite credit."),D.d_brand("Hyatt","Compare hotel award results","Compare points-per-night across Room, Award and Points + Cash rates. Booking with Hyatt points earns elite night credit."),D.d_brand("Hyatt","Points calendar","Use the points calendar to find lower award pricing by date. Confirm the night you want before booking."),D.d_brand("Hyatt","Sign in to book","Sign in with your World of Hyatt account (name must match your Chase account) to complete the award booking.")][i],
 "how-to-buy-bitcoin-with-chase-bank": lambda i: [R.t_coinbase("link"),R.t_coinbase("link"),R.t_coinbase("accounts"),R.t_coinbase("accounts"),R.t_coinbase("accounts"),R.t_coinbase("buy"),R.t_coinbase("buy"),R.t_coinbase("buy"),R.t_coinbase("buy"),R.t_coinbase("buy"),R.t_coinbase("buy")][i],
 "how-to-add-a-chase-card-to-apple-pay": lambda i: [R.t_more(),R.t_digital_wallets(),R.t_wallet_link(),R.t_wallet_link(),R.t_wallet("device"),R.t_wallet("device"),R.t_wallet("adding"),R.t_wallet("terms"),R.t_wallet("terms"),R.t_wallet("adding"),R.t_wallet("default"),R.t_wallet("linked")][i],
 "how-to-add-chase-debit-card-to-apple-wallet": lambda i: [R.t_more(),R.t_digital_wallets(),R.t_wallet_link(),R.t_wallet_link(),R.t_wallet("device"),R.t_wallet("device"),R.t_wallet("adding"),R.t_wallet("terms"),R.t_wallet("terms"),R.t_wallet("adding"),R.t_wallet("default"),R.t_wallet("linked")][i],
 "how-to-cancel-a-check-deposit-chase": lambda i: [C.t_qd("ok"),R.t_contact(),R.t_more(),R.t_profile(),R.t_contact()][i],
 "how-to-cancel-a-chase-debit-card-on-app": lambda i: [C.t_home(),C.t_manage(),C.t_manage("Replace"),R.t_app_list("Replace a card",["Replace a card","DEBIT/ATM CARD (&hellip;2208)"],highlight="DEBIT"),C.t_replace_reasons(),C.t_replace_reasons()][i],
}
def route(slug, i, s, n):
    t0=(s.get("title","")+" "+s.get("instruction","")).lower()
    if "open the app and sign in" in t0: return C.t_home()
    if "open the website and sign in" in t0: return D.d_ur("signin")
    if slug in OVERRIDES:
        try: return OVERRIDES[slug](i)
        except IndexError: pass
    t=(s.get("title","")+" "+s.get("instruction","")).lower()
    def has(*ws): return any(w in t for w in ws)
    first = i==0; last = i==n-1
    # --- recurring tails (order matters) ---
    if has("open more","tap \"more\"","open the more","in chase mobile, open more","open more from"):
        return R.t_more(highlight="Contact us" if has("contact") else None)
    if has("profile & settings") and has("open","choose","go"):
        return R.t_profile()
    if has("contact us") and has("open","find"):
        return R.t_contact()
    # --- home / account ---
    if first and has("accounts dashboard","account list","tap total checking","open total checking","accounts screen","checking account from accounts","credit card account","open the freedom card","open the credit card"):
        if has("freedom","credit card"): return C.t_account()
        return C.t_home()
    if has("tap total checking") and first: return C.t_home()
    if has("open total checking from accounts","open your checking account from accounts","open the checking account from accounts","open the chase mobile account list","open the freedom card from accounts","open the credit card account","open your profile") and not has("more","profile & settings"): return C.t_home()
    if has("manage account") and has("tap","open") and not has("lock & unlock card","activate"):
        hl=None
        if has("lock"): hl="Lock"
        if has("activate"): hl="Activate your card"
        if has("digital wallet"): hl="digital wallets"
        if has("pin"): hl="Manage PIN"
        if has("replace"): hl=None
        return C.t_manage(highlight=hl)
    if has("on total checking, tap manage") or (has("manage account") and has("access tools")):
        return C.t_account()
    if has("got it"):
        return C.t_account()
    if has("show details") and not has("automatic"):
        return C.t_show_details()
    # --- card management ---
    if has("misplaced","lock & unlock your card","lock card","locked-card","locked your card","temporary-lock"):
        locked = ("locked your card" in t or "locked-card" in t or ("unlock card" in t and "lock & unlock card" not in t))
        return C.t_lock(locked=locked)
    if has("tell us more about your situation","choose a reason","select my card is lost","my card is lost"):
        return C.t_replace_reasons()
    if has("shipping info","shipping method","mailing address"):
        return C.t_replace_shipping()
    if has("does everything look ok") and has("replace","card info"):
        return C.t_replace_summary()
    if has("expiration","expiry") and has("debit card","card"):
        return C.t_activate("expiry")
    if has("you're all set","activated your new debit card","loading"):
        return C.t_activate("ok")
    if has("paycheck","direct deposit") and not has("cancel"):
        return C.t_dd()
    # --- statements / paperless ---
    if has("statements and documents","statements & documents") and has("open","categories"):
        return C.t_stmt_docs()
    if has("7 years","statements page","up to 7 years"):
        return C.t_stmts_page()
    if has("paperless"):
        return C.t_paperless("ok" if has("updated","confirmation") else "edit")
    # --- quickdeposit ---
    if has("auto-capture"): return C.t_qd("tips")
    if has("received your deposit"): return C.t_qd("ok")
    if has("does everything look ok") and has("deposit amount","front"): return C.t_qd("review")
    if has("quickdeposit") and has("agreement","i agree","start depositing"): return C.t_qd("agree")
    if has("quickdeposit","deposit check") and not has("cancel"): return C.t_qd("amount" if has("$30") else "main")
    if has("post-submission","paper check") and has("guidance","review"): return C.t_qd("ok")
    # --- pay & transfer / transfers ---
    if has("pay & transfer") and has("open","tap"): return C.t_pay_transfer()
    if has("see activity") and has("open"): return R.t_zelle("pending")
    if has("pending payment details") and has("open"): return R.t_zelle("pending")
    if has("pending payment details") and has("review"): return R.t_zelle("pending")
    if has("cancellation confirmation"): return R.t_zelle("cancel_ok")
    if has("verify the result"): return R.t_zelle("cancel_ok")
    if has("choose a delivery method"): return C.t_xfer("delivery")
    if has("transfer from") and has("choose your checking","in transfer from"): return C.t_xfer("pick")
    if has("does everything look ok") and has("schedule transfer","delivery method"): return C.t_xfer("review")
    if has("schedule a transfer","transfer and account transfers","schedule transfer") and not has("wire"):
        filled = has("transfer to","choose your savings","tap transfer","confirmation") or i>=2
        return C.t_xfer("filled" if (filled or i>=1) else "form")
    # --- wires ---
    if has("wires & global transfers","international"): return C.t_wire("intl")
    if has("smart way","send money safely") and not has("zelle"): return C.t_wire("intro")
    if has("payment purpose"): return C.t_wire("purpose")
    if has("stay safe from scams") and not has("zelle"): return C.t_wire("scam")
    if has("step 1 of 3","bank details") and not has("recipient"): return C.t_wire("bank_ok" if has("registered") else "bank")
    if has("step 2 of 3","add recipient details"): return C.t_wire("recipient")
    if has("step 3 of 3"): return C.t_wire("review")
    if has("you're all set") and has("recipient"): return C.t_wire("ok")
    if has("schedule transfer") and has("wire"): return C.t_wire("schedule")
    if has("verify sender"): return C.t_wire("verify")
    if has("can i cancel a wire"): return R.d_web("Can I cancel a wire?","Chase &rsaquo; Help &rsaquo; Wire transfers","<p><b>Domestic:</b> For same-day wires, you don't have the option to cancel. Future-dated domestic wires can be canceled until 11:59 PM ET the day before the send date.</p><p style='margin-top:10px'><b>International (personal accounts):</b> You have 30 minutes after you authorize the wire to cancel it.</p><p style='margin-top:10px'>Open Wire activity to find the <b>Cancel</b> button next to an eligible wire. Once a wire is sent, you can't cancel it.</p>")
    if has("how can i check the status"): return R.d_web("How can I check the status of my wire?","Chase &rsaquo; Help &rsaquo; Wire transfers","<p>Go to <b>Wire activity</b> to see your sent wires and their status: <b>Sent</b>, <b>In review</b> or <b>Completed</b>.</p><p style='margin-top:10px'>You can also call <b>1-800-935-9935</b>. If you sent money by mistake or to a scammer, call us immediately &mdash; recovery is very unlikely once a wire is sent.</p>")
    if has("cancellation rules") or (has("read the cancellation") or has("read both full routes")): return R.d_web("Wire transfer cancellation rules","Chase &rsaquo; Help &rsaquo; Wire transfers","<p><b>Same-day domestic wires:</b> no cancellation option.</p><p style='margin-top:8px'><b>Future-dated domestic:</b> cancel until 11:59 PM ET the day before the send date.</p><p style='margin-top:8px'><b>International:</b> 30 minutes after authorization.</p><p style='margin-top:8px'>You'll only see <b>Cancel</b> next to a wire if you're able to cancel it. Support: <b>1-800-935-9935</b>.</p>")
    # --- zelle ---
    if has("zelle") and has("stay safe","social media"): return R.t_zelle("safe")
    if has("zelle") and has("welcome"): return R.t_zelle("welcome")
    if has("one-time code","texted you"): return R.t_zelle("code")
    if has("zelle") and has("you're all set"): return R.t_zelle("ok")
    if has("qr","scan or share"): return R.t_zelle("qr")
    if has("add recipient") and has("zelle"): return R.t_zelle("add")
    if has("enter amount"): return R.t_zelle("amount")
    if has("sending your money now","siri"): return R.t_zelle("confirm")
    if has("pay bills & send money","payments due"): return R.t_zelle("home")
    if has("pending payment details","cancellation confirmation") or (has("zelle") and has("cancel","pending")):
        return R.t_zelle("cancel_ok") if has("verify the result","confirmation") else R.t_zelle("pending")
    # --- disputes ---
    if has("doesn't look right","report a problem") and has("scenario"): return C.t_dispute("options")
    if has("are you sure"): return C.t_dispute("sure")
    if has("please call us"): return C.t_dispute("call")
    if has("transaction") and has("report a problem"): return C.t_dispute("details")
    if has("transactions") and has("open","scroll") and not has("stored"): return C.t_account(txn=True)
    # --- pin / security ---
    if has("pin"): return R.t_pin()
    if has("security & privacy"): return C.t_secpriv()
    if has("2-step","update your settings","extra security"): return C.t_twofa()
    if has("password"): return C.t_password()
    # --- external accounts ---
    if has("financial institution"): return R.t_ext("find")
    if has("choose how you want"): return R.t_ext("how")
    if has("consent"): return R.t_ext("select")
    if has("choose an account you'd like","nickname"): return R.t_ext("nickname")
    if has("verified and added"): return R.t_ext("ok")
    # --- apple pay / wallet ---
    if has("digital wallets"): return R.t_digital_wallets() if not has("add to apple wallet") else R.t_wallet_link()
    if has("add to apple wallet"): return R.t_wallet_link()
    if has("select \"iphone\"","select the device"): return R.t_wallet("device")
    if has("adding card","contacts the issuer"): return R.t_wallet("adding")
    if has("terms and conditions") and has("apple","wallet"): return R.t_wallet("terms")
    if has("default-card","default card") and has("not now","tap"): return R.t_wallet("default")
    if has("linked"): return R.t_wallet("linked")
    if has("apple wallet") and has("tap"): return R.t_wallet_link()
    # --- profile-ish app screens ---
    if has("personal details") and (has("expand","open phone","edit")): return R.t_app_form("Personal details",[("Name","Jordan Avery"),("Phone","(713) 555-0142"),("Email","j.avery4821@example.com"),("Mailing address","1200 Smith St, Houston, TX 77002")],btn="Done")
    if has("phone") and has("edit","new number"):
        if has("save"): return R.t_app_form("Edit phone number",[("Old number","(713) 555-0142"),("New number","(713) 555-0188")],btn="Save",note="We may send a verification code to confirm this change.")
        return R.t_app_form("Phone number",[("Current number","(713) 555-0142")],btn="Edit")
    if has("enter your new number"): return R.t_app_form("Phone number",[("New number","(713) 555-0188")],btn="Save",note="We may send a verification code to your new number.")
    if has("update notice"): return C.t_paperless("ok")
    # --- stored cards / subscriptions ---
    if has("stored cards"): return R.t_stored_cards(0)
    if has("charge history","open a business"): return R.t_stored_cards(1)
    # --- credit journey ---
    if has("credit score","credit journey"): return R.t_creditjourney(2 if has("your score") else (1 if has("track your finances") else 0))
    # --- trade / investing ---
    if has("trade") and has("open"): return C.t_manage()
    if has("switch to dollars","trade ticket"): return R.t_trade(0)
    if has("preview"): return R.t_trade(1)
    if has("treasury"): return R.d_web("Fixed income & Treasury bills","Chase &rsaquo; Investing &rsaquo; Fixed income","<p>Treasury bills, notes and bonds are purchased inside a <b>J.P. Morgan Self-Directed Investing</b> brokerage account &mdash; not from your checking account.</p><p style='margin-top:10px'>Open the account, fund it, then choose <b>Trade &rsaquo; Fixed income</b> to search Treasuries by maturity and yield. Online fixed-income trades are $0 commission; Treasuries carry $0 per bond markup.</p>")
    # --- loans ---
    if has("pay over time","my chase loan"):
        if has("offer"): return R.t_loan(1)
        if has("amount","payment options","compare"): return R.t_loan(2)
        return R.t_loan(0)
    if has("open the freedom card","open the credit card"): return C.t_account()
    # --- autopay / cancel repeating ---
    if has("automatic payments") and has("edit","off"): return R.t_autopay(1 if has("edit") else 2)
    if has("show details") and has("automatic"): return R.t_autopay(0)
    # --- crypto ---
    if has("plaid"): return R.t_coinbase("link")
    if has("account list","connect the selected","data-sharing"): return R.t_coinbase("accounts")
    if has("buy crypto","preview buy","buy now","purchase-status","displayed status"): return R.t_coinbase("buy")
    if has("payment methods","us table","cash-like"): return R.d_web("Coinbase &mdash; US payment methods","coinbase.com &rsaquo; Help &rsaquo; Payment methods","<p>US funding options: <b>Bank account (ACH)</b>, <b>debit card</b>, <b>wire transfer</b>, and selected wallet options.</p><p style='margin-top:10px;color:#BF2155'>Credit-card funding is limited: since the 2025 Chase&ndash;Coinbase partnership, Chase credit cards may fund Coinbase, but most crypto purchases on credit cards are treated as cash-like transactions with fees and may be declined by other issuers.</p>")
    if has("cash-like"): return R.d_web("Cash-like transactions &mdash; sample card agreement","Chase &rsaquo; Card agreement","<p>Purchases of <b>cryptocurrency</b>, money orders, wire transfers and other cash-like transactions may be treated as <b>cash advances</b> under your card agreement, with no grace period and a higher APR.</p><p style='margin-top:10px'>Chase's 2025 Coinbase partnership allows Chase credit cards to fund Coinbase; treatment can still be cash-advance-like. Check your current card agreement.</p>")
    # --- ultimate rewards ---
    if has("choose united airlines") and ("book-" in slug or "transfer-chase-points" in slug): return R.d_ur("partners",highlight="United Airlines MileagePlus")
    if ("book-" in slug or "transfer-chase-points" in slug or "hotel" in slug) and has("ultimate rewards") and has("sign-in"): return R.d_ur("signin")
    if has("ultimate rewards") and has("travel menu"): return R.d_ur("home_menu")
    if has("ultimate rewards") and has("home"): return R.d_ur("home")
    if ("book-" in slug or "transfer-chase-points" in slug) and has("transfer-partner list","transfer points to partners"): return R.d_ur("partners",highlight=("World of Hyatt" if has("hyatt") else "British Airways Club" if has("british","ba") else "Aeroplan (Air Canada)" if ("book-" in slug) and has("aeroplan") else "United Airlines MileagePlus"))
    if ("book-" in slug or "transfer-chase-points" in slug) and (has("mileageplus number","points amount") or (has("united") and has("enter","continue"))): return R.d_ur("transfer")
    if ("book-" in slug or "transfer-chase-points" in slug) and has("transfer details and stop","continue after entering the points"): return R.d_ur("transfer")
    # --- brand searches ---
    if ("book-" in slug) and has("british airways","avios") and has("search"): return R.d_brand("BA","Book with Avios","Distance-based Avios pricing on American Airlines and Alaska award space. Short-haul AA domestic from about 7,500 Avios one-way. BA adds carrier surcharges on itineraries touching London.")
    if ("book-" in slug) and has("alaska") and has("reward result","chart","award prices"): return R.d_brand("Atmos","Alaska award space","Alaska (Atmos Rewards) is oneworld &mdash; book its award space with British Airways Avios. Verify saver space on ba.com before transferring any points; transfers are final.")
    if ("book-" in slug or "transfer-chase-points" in slug) and has("united") and has("award calendar","award search"): return R.d_brand("United","Award search","United MileagePlus shows all Star Alliance award space, including EVA Air and ANA. Search SFO-TPE business class to see EVA availability before transferring points.")
    if ("book-" in slug) and has("aeroplan"): return R.d_brand("Aeroplan","Star Alliance award search","Air Canada Aeroplan often prices EVA Air business class among the cheapest Star Alliance redemptions to Asia. Search partner flights, review the itinerary, then book with transferred points.")
    if ("book-" in slug) and has("hyatt") and has("search","compare","calendar","sign-in gate"): return R.d_brand("Hyatt","Find hotels with points","Search World of Hyatt award nights with points. Sapphire Reserve transfers 1:1; Sapphire Preferred and Ink Business Preferred transfer at 4:3 since Oct 1, 2026. Award stays earn Hyatt elite credit.")
    if ("book-" in slug) and has("tokyo","edition","hotel") and has("result","panel","stay details"): return R.d_brand("Chase Travel","Hotels &mdash; Tokyo","Book with points through Chase Travel. Points Boost applies on top-booked hotels (up to 2&cent;/point on Sapphire Reserve); non-boosted redemptions are about 1&cent;/point. Portal bookings do not earn hotel elite credit.")
    if ("book-" in slug) and has("eligibility rules","unlinking","finnair"): return R.d_web("Transfer partner eligibility","Chase &rsaquo; Ultimate Rewards &rsaquo; Transfers","<p>Your Chase account name must match your frequent-traveler program account. Transfers are <b>final</b> and typically process by the next business day (up to 7).</p><p style='margin-top:10px'>Confirm award space on the partner's site <b>before</b> transferring points.</p>")
    if ("book-" in slug) and (has("hyperlink") or has("historical")): return R.d_brand("BA","Award results","AA and Alaska award space via Avios. Transfers are final &mdash; confirm space first.")
    # --- business ---
    if has("chase for business","manage linked accounts","business relationship","profile icon") and has("business"): return R.d_bizweb(0 if has("profile icon") else 1 if has("account settings") else 2 if has("show my accounts","relationship") else 3)
    # --- misc web/info ---
    if has("fee disclosure","waiver condition","total checking in the fee","electronic deposits qualify"):
        return R.d_fee_table()
    if has("meeting","schedule a meeting","locator","branch search","zip","branch details","branch to start"): return R.d_locator(0 if has("open chase meeting","scheduling") else 1)
    if has("branch") and has("open the branch"): return R.d_locator(1)
    if has("application status") or (has("application") and has("status")): return R.d_web("Check your application status","Chase &rsaquo; Credit cards &rsaquo; Application status","<p><b>Phone:</b> 1-888-338-2586 (personal and business applications). Verify your identity and have the reference number from your confirmation email.</p><p style='margin-top:10px'><b>Online:</b> sign in at chase.com/personal/credit-cards/verify-credit-card. A decision usually arrives within 14 days; approved cards arrive within two weeks.</p><p style='margin-top:10px'>A letter saying you'll hear within 7-10 business days is a community signal of likely denial &mdash; not official Chase policy.</p>")
    if has("balance transfer"): return R.d_web("Balance transfers","Chase &rsaquo; Credit cards &rsaquo; Balance transfer","<p><b>0% intro APR for 15 months</b> on balance transfers from account opening; then variable APR applies. Fee: $5 or 3% per transfer in the first 60 days ($5 or 5% after).</p><p style='margin-top:10px'>Request online (card &rsaquo; account services &rsaquo; Transfer a balance), during application, or by phone. Transfers may not pay other Chase cards and cannot exceed $15,000 in any 30 days. Post in about a week, up to 21 days; transfers earn no rewards.</p>")
    if has("disney"): return R.d_web("Disney Rewards Cardmember Perks","disneydebit.com &rsaquo; Cardmember Perks","<p>Chase co-branded Disney&reg; Visa&reg; Debit Card designs are managed on the Disney perks site. Sign in with your Chase credentials to view available card designs and request a design change; the replacement arrives in 5&ndash;7 business days.</p><p style='margin-top:10px'>Design availability depends on your card. After the request, activate the replacement when it arrives and update any recurring payments.</p>")
    if has("gift card"): return R.d_web("Payment methods Chase accepts","Chase &rsaquo; Help","<p>Chase accounts cannot be funded with prepaid or gift cards: Zelle&reg; enrollment requires an eligible Chase checking account, external-account linking requires a real bank account, and mobile deposit requires a paper check.</p><p style='margin-top:10px'>Workarounds: add the gift card to a payment service that cashes out to your bank, or ask the issuer for a refund check.</p>")
    if has("languages","supported languages"): return R.d_web("Chase app languages","Chase &rsaquo; Help","<p>The Chase Mobile app follows your device language. There is no in-app language switcher. Spanish content is available at chase.com/espanol.</p><p style='margin-top:10px'>Change your device language: <b>Settings &rsaquo; General &rsaquo; Language &amp; Region</b>.</p>")
    if has("iphone settings","language & region","add a language","search for spanish","select spanish","primary language"): return R.t_settings_lang(0 if has("iphone settings") else 1 if has("language & region") else 2 if has("add a language") else 3)
    if has("name-change","name change"): return R.d_web("Change your name on your accounts","Chase &rsaquo; Help","<p>Update your name with the <b>SSA</b> first. Once SSA records are updated, you can digitally change your name on credit or deposit accounts at chase.com or in the app without extra documents.</p><p style='margin-top:10px'>If the digital change fails, use a secure message, phone, or branch with documents (certified marriage certificate, divorce decree, or court order).</p>")
    if has("limit schedule","purchase-limit row","contact personal banking"): return R.d_web("Debit card limits","Chase &rsaquo; Help &rsaquo; Debit card","<p>Typical limits: <b>ATM withdrawals</b> $500&ndash;$3,000/day; <b>purchases</b> $300&ndash;$7,500/day. Chase Private Client: up to $3,000/$7,500.</p><p style='margin-top:10px'>There is no self-service limit change in the US app. Call <b>1-800-935-9935</b> (number on your card) or visit a branch; temporary increases are possible.</p>")
    if has("stored cards"): return R.t_stored_cards(0)
    if has("beneficiary"): return R.d_web("Add a beneficiary","Chase &rsaquo; Help &rsaquo; Beneficiary","<p>A payable-on-death beneficiary <b>can only be added by visiting a Chase branch</b> &mdash; schedule a meeting in advance. Bring the beneficiary's first and last name, phone number and address.</p><p style='margin-top:10px'>Most personal checking, savings and CDs are eligible. Beneficiaries can't be added to business accounts, and credit cards have no beneficiary designation.</p>")
    if has("business line of credit"): return R.d_web("Chase Business Line of Credit","Chase &rsaquo; Business &rsaquo; Loans","<p><b>Credit lines up to $500,000</b> &middot; five-year revolving period and repayment term.</p><p style='margin-top:8px'>Annual fee: $200 or 0.25% of the approved line (whichever is greater) &mdash; waived with 40% average utilization. Eligibility: $100,000+ annual revenue, FICO&reg; 660+.</p><p style='margin-top:8px'>Apply at chase.com/business/banking/loans or at a branch.</p>")
    if has("ink business","legal business structure"): return R.d_web("Business credit card application &mdash; sole proprietors","Chase &rsaquo; Business &rsaquo; Credit cards","<p>Sole proprietors may provide an <b>SSN in place of an EIN</b>. Legal business name: your own full name; entity type: <b>Sole proprietorship</b>.</p><p style='margin-top:10px'>Other fields: industry, years in business (1 or less is selectable), annual revenue, employees (count yourself as 1).</p>")
    if has("borrow","loan") and has("offer"): return R.t_loan(1)
    # --- generic fallbacks ---
    if has("settings"): return R.t_profile()
    if has("review","check the") and last: return R.t_app_info(s.get("title",""), [s.get("instruction","")], cta="Done")
    et=[x for x in s.get("expectedText",[]) if len(x)<44]
    title = et[0] if et else ("Review" if len(s.get("title",""))>40 else s.get("title","Review"))
    rows = et[1:6] if et else [s.get("instruction","")[:80]]
    return R.t_app_list(title, rows)

def main():
    GUIDES="/Users/amanmaan/Documents/TOOLS/Screenshot Automator/cashgen-pipeline/guides"
    REQ=json.load(open(os.path.join(os.path.dirname(GUIDES),"chase-request-2026-10-07.json")))
    slugs=[t["slug"] for t in REQ["topics"]]
    pages={}
    for slug in slugs:
        g=json.load(open(os.path.join(GUIDES,slug+".json")))
        steps=g.get("screenshotSteps",[])
        shots=[]
        for i,s in enumerate(steps):
            DD.IS_DESKTOP=False
            try:
                inner=route(slug,i,s,len(steps))
            except Exception as e:
                DD.IS_DESKTOP=False
                inner=R.t_app_info(s.get("title",""),["Render error: "+str(e)[:80]])
            if DD.IS_DESKTOP:
                shots.append(f'<div class="shot desktop"><div class="dk">{inner}</div></div>')
            else:
                shots.append(f'<div class="shot"><div class="app">{inner}</div></div>')
            DD.IS_DESKTOP=False
        html=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{C.CSS}
        body{{margin:0;background:#3d4046}}
.board{{display:flex;flex-direction:column;align-items:center;gap:26px;padding:24px}}
.shot.desktop{{width:2880px;height:1800px}}
.dk{{transform:scale(2);transform-origin:top left;width:1440px;height:900px;position:relative;background:#fff;font-family:'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif;color:#1a1a1a}}</style></head>
        <body><div class="board">{ ''.join(shots) }</div></body></html>'''
        pages[slug]=html
    os.makedirs("pages",exist_ok=True)
    for slug,html in pages.items():
        open(f"pages/{slug}.html","w").write(html)
    print("built",len(pages),"pages")

if __name__=="__main__":
    main()
