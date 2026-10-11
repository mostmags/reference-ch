# DESIGN_RULES.md — Chase UI fidelity rules (source of truth for generated screenshots)

> The live implementation of these rules is the HTML template library:
> `/Users/amanmaan/Pictures/CHASETT/chase-ui-research/render/chase_ui.py` (mobile) and
> `render/desktop.py` (website). When generating a new screen, extend those files — do not
> freelance styles.

## Canvas & chrome

| Kind | Size (pt) | Export (@2x) | Chrome |
|---|---|---|---|
| Chase Mobile (iOS) | 393×852 | 786×1704 px | iOS status bar (12:01, signal/WiFi/battery) + home indicator; full-bleed, SQUARE corners, no device frame |
| chase.com / partner sites | 1440×900 | 2880×1800 px | Website header + footer; no status bar, no phone frame |

Status bar (mobile): time "12:01" bold left; right: 4-bar cellular SVG, WiFi SVG, battery SVG
(~75%, with tip). Implemented in `chase_ui.py::sb()` — reuse it, never hand-draw.

## Colors

| Token | Value | Usage |
|---|---|---|
| Primary blue | `#0060F0` | Buttons, links, active nav |
| Brand navy | `#0846A8` (gradient `#1B449C→#153680` for home section bars) | Brand surfaces |
| Page background | `#F7F8FA` (home) / `#F6F6F6` (inner) | NOT white, NOT blue gradient |
| Cards | `#FFFFFF`, radius 12px, shadow `0 2px 8px rgba(0,0,0,.05–.07)` | Content groups |
| Text | `#1a1a1a` primary, `#5f6368` secondary, `#9aa0a6` chevrons | |
| Success / Error | `#2CA853` / `#BF2155` | Confirmations / warnings |
| Dividers | `#e3e3e3` | Row separators |

NEVER use `#117ACA` (legacy Chase blue). NEVER use blue gradients on the app home screen.

## Typography

Font stack: "Open Sans", "Helvetica Neue", Helvetica, Arial (closest to Chase Sans).
- Page/screen titles: 22–31px bold (700)
- Section headers (CARD SETUP AND MAINTENANCE style): 12.5px, 600, letter-spacing .4px, gray
- List rows: 15.5px regular; bold 600 for emphasis
- Body: 14–14.5px, line-height 1.5, color #3c4043
- Balance numerals: 28–33px regular (app home/detail screens)
- Captions/sublabels: 12–13.5px gray

## Components (exact behavior)

- **Navbar (inner screens):** 52px, white, bottom border #e3e3e3; back chevron left (with or
  without "Back" label per reference); centered 16px semibold title; optional right action
  (Cancel/Close in blue).
- **List rows:** white cards, radius 12px, 54px min-height, chevron › right, dividers between rows.
- **Primary button:** #0060F0, radius 6px, height 50px, 16px semibold white text, FLEX-centered
  (vertical + horizontal). Full-width on forms; right-aligned compact on the lock-card screen.
- **Pill buttons (account screen):** height 44px, radius 22px; Pay filled blue, Transfer/More outlined.
- **Circular action buttons:** 58px white circles, blue icon, blue 14px label below (account screen).
- **Home section bars:** navy gradient, white 16.5px semibold, radius 12px top corners; white
  content card below with radius 12px bottom corners.
- **Account names:** uppercase dark navy bold with "…" last-4 + › (e.g., TOTAL CHECKING (…4821) ›).
- **Balances:** right-aligned on home/account cards; caption below ("Available balance" /
  "Current balance").
- **Bottom navigation:** white, 80px, top divider; 5 tabs — Accounts (blue filled wallet when
  active), Pay & transfer (orbit arrows around $), Plan & track (document+pencil),
  Benefits & travel (star), More (hamburger). Active = blue icon + blue label.
- **Home top bar:** chat-bubbles icon + card-with-plus icon (left), Chase octagon logo centered
  (~34px, #0B4DA2), profile circle (right). Greeting 32px bold + date 15.5px below; then white
  pill quick actions (+, Pay bills, See bill activity, Credit Journey) with soft shadows.
- **Success screens:** 64px green circle (#2CA853) with white check, centered headline, summary
  rows, single bottom button (Done / Close / Deposit another check).
- **Review screens:** titled "Does everything look OK?" with label/value rows (+ Edit links) and
  one bottom primary button (Schedule transfer / Deposit / Replace card).

## Website (chase.com)

- Header: white, Chase octagon logo + "CHASE" wordmark left; "Search" + blue "Sign in" right;
  subtle bottom shadow. Authenticated UR header adds "Ultimate Rewards®" + Travel/Redeem/Earn
  menus + JA avatar.
- Content: crumb (13.5px gray) → page title (38px, weight 300) → body (16.5px/1.65, max-width
  ~880px) → blue CTA (#0060F0, radius 4px).
- Footer: #F6F6F6 strip — "© 2026 JPMorgan Chase & Co. · Member FDIC · Equal Housing Opportunity".
- Buttons radius 4px (web) — NOT the 6px mobile radius.

## Persona (fictional — always use, never render reference-frame data)

Jordan Avery · Total Checking "TOTAL CHECKING (…4821)" $2,436.19 available/present ·
"DEBIT/ATM CARD (…2208)" exp 08/29 · "CREDIT CARD (…7710)" (Freedom Unlimited) $418.77 ·
external "360 Performance Savings (…8535)".

## Prohibitions

- No invented rows/tabs/screens; no elements from other banking apps.
- No legacy #117ACA, no pill-shaped primary buttons, no blue home background.
- No device frames, rounded phone corners, watermarks, or annotations inside the image.
- No real person's name, account numbers, or balances from reference frames.
