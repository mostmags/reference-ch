# Known Gaps & Uncertainties

## Unverified screens/labels (flagged [U] — do not present as fact in tutorials)

1. **Digital wallets screens inside the Add-to-Apple-Pay flow** — the primary video never opens this flow, so these screens are reconstructions from other walkthroughs' narration, not frames:
   - "Digital wallets" wallet-picker screen (Apple Pay / PayPal / Paze rows) — row contents plausible but **exact layout unverified**.
   - Identity verification screen — title "Confirm it's you" is **invented**; walkthroughs confirm an SMS one-time-code step exists but not its exact wording.
   - Eligible-cards screen — "Add to Apple Pay" button label is corroborated by 3 walkthroughs; screen title/structure unverified.
   - Chase terms screen — "I agree" button label varies by walkthrough ("I agree" / "Accept and continue"); exact title unverified.
2. **Exact home-screen hero content** — the real home screen in the video has personal data; our mockup uses plausible sections (Today's Snapshot) but the exact card set varies by user. Style verified; contents are examples.
3. **Chase app "Chase Sans"-style custom font** — app font family not officially documented; Open Sans/Inter used as closest stand-in in mockups.
4. **Website authenticated dashboard tile quick-actions row** ("Statements / Paperless / Transfer money / More") — verified from the video's website segment (frame `website/website-account-page.png`), but only for a checking account page; other account types may differ.
5. **Website "Sign-in preferences" / "Security and privacy" menu structure** — attested only by third-party guides (agent research); not directly verified.
6. **Statement-history length web vs app** — no official comparison found.
7. **App "Order checks and deposit slips" row** — present in the app's Services list (frame `card-management/manage-account-top.png`) even though the narrator says ordering happens on the website. Likely deep-links to web; actual in-app behavior unverified.
8. **Android variants** — not researched in depth (Google Pay/Samsung Wallet replace Apple Pay rows; nav may differ).

## Conflicting evidence resolved

| Conflict | Resolution |
|---|---|
| Chase blue #117ACA vs #0060F0 | Live chase.com CSS (2026-10-10) uses #0060F0 primary / #0846A8 brand; #117ACA is legacy. Use current values. |
| In-app path "Account Services → Digital Wallets" (chase.com marketing copy) vs "Manage account" (video + walkthroughs) | Both describe the same account tools area; the observed in-app label is "Manage account" → "Add card to digital wallets". |
| App Store screenshot bottom nav ("Investments" tab) vs video ("Benefits & travel" + "More") | Video frames (June 2026 build) are newer; use video labels. |
| Narrator: app can't order checks vs app row exists | Follow narrator + official page for the workflow; note the row exists and likely hands off to web. |

## What would close the gaps

- Screen recordings of the real in-app Apple Pay flow (Digital wallets → terms → Wallet handoff).
- A logged-in chase.com session capture for the full Profile & settings menu tree.
- Official Chase app design-system documentation (if ever published).
