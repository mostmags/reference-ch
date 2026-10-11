# Chase Mobile App (iOS) — Navigation Map

Built from the primary reference video (c_R-hxWqGuc, "How to Use the Chase App | Tutorial for Beginners", ~1h39m, analyzed Oct 2026) cross-checked with official Chase pages. Timestamps = primary video. Verify labels against `references/mobile-ios/` frames before mocking up.

## Top-level structure

```
Chase Mobile (iOS)
├── Sign in (passcode / Face ID)
├── Home dashboard ("Accounts" tab)
│   ├── Blue hero: greeting, chat icon (top right), Today's Snapshot card
│   ├── Quick actions row: Send (Zelle) · Deposit checks · Pay bills · [+]
│   ├── Accounts list (grouped cards)
│   │   ├── Checking account tile → Account screen
│   │   │   ├── Balance header: "Available balance" + "Present balance" (details)
│   │   │   ├── Buttons: [Pay] [Transfer] [More]
│   │   │   ├── Action list ("Finish setting up your new account") — new accounts only
│   │   │   ├── Manage account  → Account tools
│   │   │   │   ├── [Lock and unlock card] [Replace a lost or damaged card] [Dispute a transaction]
│   │   │   │   ├── Card setup and maintenance
│   │   │   │   │   ├── Track your card
│   │   │   │   │   ├── Add cards to your digital wallets → Digital wallets (Apple Pay / PayPal / Paze)
│   │   │   │   │   ├── Activate your card → enter expiration date → Activate → success
│   │   │   │   │   └── Manage PIN → enter 16-digit card number → Request PIN (mailed)
│   │   │   │   └── Services: Stop payment on a check · Overdraft protection · Debit card coverage
│   │   │   │       · Order checks and deposit slips (web only per video) · Set up direct deposit form
│   │   │   ├── See all transactions → Transactions (newest first; pending items show "–" date)
│   │   │   │   └── Transaction → details → "Report a problem" (6 reasons; fraud option locks card)
│   │   │   ├── See statements → Statements & documents
│   │   │   │   └── Statements · Tax documents · ATM and branch receipts · Notices and letters · Branch documents
│   │   │   ├── Show details → account #, routing #, rate, last statement date (+ "?" popup with wire routing #)
│   │   │   └── Set up direct deposit → "Have your paycheck sent here" (routing/account + copy, prefilled form PDF)
│   │   └── Credit card tile → Card screen (same pattern)
│   └── [+] quick action → More options
├── Pay & transfer (bottom tab)
│   ├── Quick actions: Pay bills · Send money with Zelle · Wires and global transfers · Transfer and deposit checks
│   ├── Transfer → Schedule a transfer (amount, from, to, delivery method Real time/Standard, date, note) → review "Does everything look okay?" → Schedule transfer
│   ├── Manage external accounts → Add an external account → find FI (Yodlee) → sign-in consent → confirm & connect → nickname → verified
│   ├── Wires and global transfers
│   │   ├── [Domestic] "The smart way to move money" → identity code → payment purpose (6 options) → scam warning + checkbox
│   │   │   → 3-step recipient add (bank details w/ routing validation box · details · review) → "You're all set"
│   │   │   → Send money → schedule (amount, $25 fee shown, daily limit $25,000) → Verify sender → Schedule wire
│   │   └── [International] tabs Domestic US | International → add recipient (SWIFT/BIC + IBAN, currency EUR/USD,
│   │       fee $5 local < $5k / $40 USD, exchange rate shown, rate expires in 30 min) → schedule → review
│   ├── Manage recipients (saved list → "Send a wire" shortcut)
│   └── Zelle: Send money with Zelle → (first time) Welcome to Zelle → agree → pick Zelle ID (phone/email)
│       → OTP → "You're all set" (+ QR code, add more IDs) → Stay safe with Zelle → add recipient
│       → enter amount + message (required) + pay from → review → Send it now → confirmation
├── Deposit checks (home quick action)
│   └── First-time: agreement checkbox → "Deposit a check" → Quick deposit screen
│       (tabs: Deposit checks | See activity · Deposit to · Deposit amount + mobile deposit limit ·
│       Front/Back auto-capture boxes) → review "Does everything look okay?" → Deposit →
│       "We received your deposit" (amount available next business day, keep check 5 days, void + shred)
├── Profile & settings (profile icon, top right)
│   ├── Security and privacy
│   │   ├── Report fraud
│   │   ├── [Lock and unlock card] [Replace a card] [Request a new PIN]
│   │   └── Enhance your security: Manage passkeys · Enable two-step verification
│   │       → Update your settings (toggle "Use two-step verification every time you sign on on a browser",
│   │          toggle "Receive one-time codes by email")
│   ├── Personal details
│   ├── Sign-in preferences (expand): Username and password · Face ID and passcode · Delete digital profile
│   │   └── Username and password → password row → current/new/confirm → Save
│   └── Account settings (expand): Show or hide accounts · Set primary accounts · Nickname accounts
│       └── Paperless → email shown (Edit) · All accounts checkboxes (All documents/All statements/
│           All notices and letters/All tax documents) · per-account checkboxes → Save → confirmation
└── (Global) Lock card flows
    ├── Lock and unlock card → "Misplace your card" screen (blocks purchases+ATM, not fees/credits/
    │   digital wallets/recurring) → Lock card → green check "You've locked your card" (button becomes Unlock card)
    └── Replace a lost or damaged card → choose card → reason: My card is lost / My card is damaged /
        I never received my card in mail (lost & never-received = new number; damaged = same number)
        → Shipping info + Regular delivery (3–5 or 5–7 business days) → summary → Replace card
```

## Cross-cutting UI patterns (verified across video)

- **Review screens** are always titled "Does everything look okay?" with per-row **Edit** links.
- **Success screens**: green check circle + short headline + summary + single bottom button (Done / Close / Deposit another check).
- **Identity verification** before sensitive flows (wires): "Get a text" / "Get a call" → code entry → "Confirm identity".
- **Scam warnings** before wires and Zelle sends, requiring a checkbox acknowledgment.
- **Popups** for "You're leaving Chase" (third-party handoffs like Deluxe check ordering) and "Learn more" info (routing numbers).
- Bottom nav (verified from 4K frames): **Accounts / Pay & transfer / Plan & track / Benefits & travel / More**. Inactive: dark gray text+icon; active: blue filled icon + blue label. White bar, thin top divider.

## Feature availability (app vs website) — key notes

| Feature | iOS app | Website |
|---|---|---|
| Order checks & deposit slips | ✗ (per primary video: "You can't do this from the mobile app") | ✓ More → Order checks and deposit slips → Deluxe (orderpoint.thedeluxe.com) |
| Link external accounts | ✓ (video shows in-app; official page also documents desktop flow) | ✓ Pay & transfer → Transfer money → add external |
| Account opening | ✗ | ✓ chase.com product pages |
| Everything else in this map | ✓ | Mostly parallel (labels differ: app "Manage account" vs web "More → Account services") |

## Known label variants (choose per-screen evidence)

- "Manage account" (account screen) opens tools; the web equivalent is "More" → "Account services".
- Digital wallets entry verified in 4K frames as "Add card to digital wallets" (Manage account screen).
- "See all transactions" vs "Transactions"; "See statements" vs "Statements & documents".
