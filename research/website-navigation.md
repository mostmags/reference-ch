# Chase.com Website — Navigation Map

Sourced from live chase.com fetches (2026-10-10, via research agent), official Chase how-to pages, and the primary video's desktop segments (42:31–48:01, order-checks flow).

## Public site (not signed in)

```
chase.com
├── Utility row: [Personal | Business | Commercial] · Schedule a meeting · Customer service
│   (See help options / Make a payment / Find ATM or branch / Disaster assistance) · Español · Search
├── Header (light gray #F6F6F6): Chase octagon logo · [Sign in] (blue #0060F0, opens overlay)
│   └── Menu: Checking · Savings & CDs · Credit cards · Home loans · Auto
│       · Investing by J.P. Morgan · Education & goals · Travel
├── Sign-in overlay → secure.chase.com: Username · Password · [Sign in]
│   · "Passwordless sign in" · "Forgot username/password?" · "Not Enrolled? Sign Up Now."
└── Footer: Other Products & Services (Deposit Account Agreements, Mobile Banking, Online Banking,
    Student Center, Zelle®) · social · legal · bottom links (Customer Service … Accessibility)
```

## Authenticated online banking (post-login)

```
secure.chase.com dashboard
├── Top left: "Main Menu" icon → "Statements & documents" (all accounts' statements)
├── Top right: profile (person) icon → "Profile & settings"
├── Accounts overview: account tiles (e.g., Total Checking) with balance
│   └── Tile quick actions [E]: Statements · Paperless · Transfer money · More
│   └── Account tile → Account Activity page (payment/deposit info, present + available balance)
│       ├── Button row [E from video]: Statements · Paperless · Transfer money · [More ▾]
│       │   └── More ▾ dropdown: shortcuts incl. "Order checks and deposit slips",
│       │       "Account services" (expands: Track your card · Lock and unlock your card · Replace a card ·
│       │       Order checks and deposit slips · Stop payments on a check · Set up direct deposit …)
│       ├── "Show details" → account #, routing #, rate, last statement date  [E from video]
│       └── "Pay & transfer" area
│           ├── Money transfer / Transfer money → From/To → amount/date/memo → Next → Transfer money
│           ├── Pay bills → Schedule payment (payee, amount, Pay from, Send on/Deliver by) → confirmation receipt
│           │   └── Payment Activity → Automatic payments → "Set up an automatic payment"
│           └── Add an external checking or savings account (desktop browser flow)
└── Profile & settings (person icon)
    ├── Left nav: Account Settings → Paperless (checkboxes + Save; "Customize settings")
    ├── Alerts → Choose alerts · Alerts delivery · Pause alerts (Edit/Remove per email/phone)
    └── Settings → Personal Details (incl. Marketing email preferences)
        · "Sign-in preferences" and "Security and privacy" sections exist [U — third-party attested only]
```

## Website-exclusive or web-centric features

| Feature | Notes |
|---|---|
| Order personal checks | Official page documents web + branch; primary video: app cannot order checks. More → Order checks and deposit slips → "You're leaving Chase" popup → Deluxe orderpoint.thedeluxe.com (check preview right, customization left: Check and print / Check details (starting # 101) / Symbol; monogram +$5, base pack $30; Check type & quantity dropdowns; "confirm and next" → upsell designs incl. free "Forever Free" → confirm and checkout) |
| Apply for new accounts | Product pages + application flow ("Let's open your Chase Total Checking account", KYC steps, PIN creation, funding options incl. "We close accounts with zero balances after 60 days") |
| Tax Documents / Tax Center | 1099-INT etc., mailing-date tables |
| Statements & documents hub | Main Menu → Statements & documents; per-year browsing |
| Full Profile & settings management | Communication preferences, alerts center |

## Label differences app vs web (for tutorials)

| App (iOS) | Website |
|---|---|
| "Manage account" (account screen) | "More ▾" → "Account services" |
| "See statements" | "Statements" button / Main Menu → "Statements & documents" |
| Profile icon → "Profile & settings" | Same concept, top-right person icon |
| Bottom tabs | No bottom nav; top menu + tiles |
