# Chase Design System (2025/2026)

**Research date:** 2026-10-10
**Confidence legend:** [V] verified from live source/CSS · [E] estimated from video frames/App Store shots · [U] unverified

> ⚠️ Legacy warning: the widely-quoted "Chase blue" `#117ACA` is the OLD brand blue. Live chase.com CSS (fetched 2026-10-10) contains zero occurrences of it. Use the values below for current-interface mockups.

## Brand colors [V]

| Token | Hex | Usage |
|---|---|---|
| Brand background / info | **#0846A8** | Brand surfaces, headers on marketing pages, info states |
| Primary interactive (buttons/links) | **#0060F0** | Primary buttons ("Sign in", "Next", "Schedule transfer"), text links |
| Pressed state | #005EB8 | Button press |
| Hover | #0A4386 | Link/button hover |
| Input active border | rgb(11,110,253) ≈ #0B6EFD | Focused inputs |
| Secondary interactive tint | #0060F0 @ 8% alpha | Selected/tinted backgrounds |
| Success | rgb(44,168,83) ≈ #2CA853 | Success checkmarks, confirmations |
| Error | rgb(191,33,85) ≈ #BF2155 | Error text/borders |
| Warning | rgb(224,111,0) ≈ #E06F00 | Warnings |
| Disabled background | #E6E6E6 | Disabled buttons |

App-specific (from App Store shots + video frames [E]): the mobile app home header/hero uses a blue gradient (deep brand blue), white content cards, dark navy text (#1a1a1a–#333), green accents for positive amounts and the Credit Journey gauge, and the Chase octagon logo in white.

## Typography [V web / E app]

- **Font family: Open Sans** (self-hosted woff2; stack: "Open Sans", "Helvetica Neue", helvetica, arial, sans-serif). Note: the mobile app additionally uses JPMorgan's proprietary "Chase Sans"-style custom font in places — visually close to Open Sans/Inter. When mocking up the app, Open Sans or Inter is the closest safe choice. [V for web; E for app]
- Weights used: 300 (large light headlines), 400 (body), 600 (semibold emphasis/buttons).
- Web scale [E from CSS/frames]: H1 ~32–40px w300; H2 ~24–28px w300/600; H3 ~18–20px w600; body 16px w400; small 13–14px.
- App scale [E from frames]: page title ~22–24px semibold; section headers ~15–16px semibold; list rows 16px; secondary/caption 13px; account balances ~28–34px light (large thin numerals).

## Corner radii [V tokens]

xSmall 4px (secondary buttons, inputs) · small 8px (cards, small buttons) · medium 12px (primary buttons, modals) · large 24px (sheets) · round 999px (pills, chips, avatars).

Primary buttons in current web UI are modestly rounded (~4–12px), NOT pill-shaped.

## Components

### Buttons [V/E]
- **Primary:** #0060F0 background, white text, 600 weight, radius ~4–12px, height ~48px mobile / ~40–44px web. Full-width on mobile forms (e.g., "Activate card", "Schedule transfer").
- **Secondary/outline:** white bg, #0060F0 text + border, same metrics.
- **Text link:** #0060F0, sometimes with chevron ›.
- **Disabled:** #E6E6E6 bg, gray text.

### App bottom navigation [E — verified across video frames]
5 tabs [V from 4K frames]: **Accounts** (blue wallet icon), **Pay & transfer** (circular arrows + $), **Plan & track** (document/pencil), **Benefits & travel** (star), **More** (hamburger). Inactive: dark gray text+icon; active: blue filled icon + blue label. White bar, thin top divider, iOS home-indicator safe area.

### Forms [E]
- Inputs: white bg, 1px #767676-ish border, radius 4–8px, height ~48–52px, label above or floating; focused border #0B6EFD.
- Toggle switches: iOS-style, on = green (app) / blue (web).
- Checkboxes: blue filled check when selected.
- Review screens: titled "Does everything look okay?" with label/value rows and **Edit** links per row; blue action button at the very bottom.
- Success screens: large green check circle + headline ("You're all set", "We received your deposit") + summary rows + "Done"/"Close".

### Web (chase.com) [V]
- Header: very light gray **#F6F6F6**, NOT blue. Octagon logo left, blue "Sign in" button (#0060F0), menu: Checking / Savings & CDs / Credit cards / Home loans / Auto / Investing by J.P. Morgan / Education & goals / Travel.
- Content: white cards on light gray background, account tiles with balance + quick-action button row ("Statements", "Paperless", "Transfer money", "More").
- Radius: buttons 4px, cards 8px.

## iOS conventions observed in app screens [E]
- Status bar: white or blue-background variants; dark content on white screens.
- Back: "<" chevron top-left, sometimes with label of previous screen.
- Modals/popups: centered card, radius ~12–16px, dimmed backdrop, buttons full-width inside.
- Bottom sheets: radius 24px top corners.

## Do-not list (accuracy rules)
- Never use #117ACA as primary.
- Never draw pill-shaped primary buttons.
- Never invent account balances/names — use clearly fictional data (e.g., "Total Checking •••• 2964" pattern is fine as it's an account-type label; balances must be obviously fictional in final renders per project rules).
- Apple Wallet screens must follow Apple design, not Chase styling.
