# Research Source Index

All sources accessed 2026-10-10 unless noted.

## Primary video reference (frame extraction source)

| Source | Details | Freshness |
|---|---|---|
| YouTube `c_R-hxWqGuc` — "How to Use the Chase App \| Tutorial for Beginners" (~1h39m) | Downloaded in 4K (3840×2160). Phone-screen crops extracted at 88 timestamps (see `references/frame-manifest.csv`). App screens show the current Chase Mobile iOS UI (e.g., "Last sign in: Jun 29, 2026", June 2026 transfer dates, current bottom nav). | Current UI — consistent with official 2026 pages; treated as the app-UI ground truth |
| Apple Pay flow verification videos (transcripts analyzed, no frames): `6OnR83LCT0Q`, `35-lc4Fc94Q`, `8ONja8cAv-w`, `BZXxT846tPg` | 4 independent walkthroughs of "Add Chase card to Apple Pay"; consensus flow documented in `feature-apple-pay.md` | 2024–2026 era; consistent with each other and Chase pages |

## Official Chase pages (fetched live)

| URL | Used for |
|---|---|
| https://www.chase.com/digital/digital-payments/apple-pay | Official "How to add your card to Apple Pay" (Wallet app method), default-card steps, eligibility FAQ, no-fee FAQ, device compatibility |
| https://www.chase.com/digital/digital-payments | "Spend Instantly" in-app method wording (card → Account Services → Digital Wallets) |
| https://www.chase.com (homepage HTML/CSS, via research agent) | Public header/footer/nav labels, sign-in overlay, design tokens |
| chase.com CSS bundles (`/hp/_next/static/css/*`) | Verified colors (#0060F0 primary, #0846A8 brand), Open Sans, radius tokens — **disproves legacy #117ACA** |
| https://www.chase.com/digital/customer-service/helpful-tips/online-banking/desktop/transfer-money | Web transfer steps |
| https://www.chase.com/digital/direct-deposit | Web "More → Account services → Set up direct deposit form" |
| https://www.chase.com/personal/mobile-online-banking/login-paperless | Paperless / Statements & documents paths (app + web) |
| https://www.chase.com/personal/mobile-online-banking/login-alerts | Profile & settings / alerts paths |
| https://www.chase.com/digital/online-bill-pay | Web bill pay steps |
| https://www.chase.com/personal/checking/checkbook-orders | Check ordering (web/branch) |
| https://www.chase.com/personal/tax-statements/deposit | Tax documents |

## Apple official

| URL | Used for |
|---|---|
| https://support.apple.com/en-us/HT204506 | Wallet app add-card steps (verbatim), requirements |
| https://support.apple.com/en-us/HT208531 | Device compatibility (linked from Chase FAQ) |

## Third-party (used with lower confidence)

| Source | Notes |
|---|---|
| Chase Mobile App Store page (apps.apple.com, id298867247) screenshots | Official marketing renders of current app UI (angled, used for style only) — saved in `references/mobile-ios/app-store/` |
| GOBankingRates check-ordering guide (2025 update) | Corroborates web check-ordering flow |

## Access date
All web sources fetched and video frames extracted **2026-10-10**.
