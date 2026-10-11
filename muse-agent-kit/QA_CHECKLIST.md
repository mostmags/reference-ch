# QA_CHECKLIST.md — per-screen acceptance gate (all must pass)

Run this checklist on EVERY generated screenshot before marking a topic complete.
Compare against the reference frame (from `references/` or the topic's `references/` folder)
side-by-side at full resolution.

## 1. Text
- [ ] Every `expectedText` label present, verbatim (capitalization, ®/™, punctuation).
- [ ] No misspellings, no truncated words (unless the real screen truncates), no lorem/demo text.
- [ ] Font = Open Sans/SF-style sans; weights: titles 600–700, body 400, buttons 600.
- [ ] Text vertically centered inside buttons/rows; labels not clipped.

## 2. Layout
- [ ] Section order matches the reference frame exactly.
- [ ] Rows/elements aligned (left/right) as in the reference; chevrons › on the right.
- [ ] Spacing/gaps visually match the reference (no cramped or stretched sections).
- [ ] Nothing overlapping, nothing cut off that shouldn't be.

## 3. Chrome
- [ ] Mobile: status bar (12:01 + signal/WiFi/battery SVG) and home indicator present; square
      corners; full-bleed; no device frame.
- [ ] Desktop: chase.com header with octagon logo + CHASE wordmark + Sign in; footer present;
      NO status bar; 1440×900 proportions.

## 4. Color & style
- [ ] Primary #0060F0, brand #0846A8, background #F7F8FA/#F6F6F6, cards white.
- [ ] No legacy #117ACA, no blue home background, no pill-shaped primary buttons.
- [ ] Radii: cards 12px, mobile buttons 6px, web buttons 4px, account-screen pills 22px.

## 5. Icons
- [ ] Bottom nav icons match the real app (wallet / orbit-$ / document-pencil / star / hamburger).
- [ ] Status bar icons match (bars-wifi-battery), correct color for the background.
- [ ] Any content icons (trophy, lock, camera) match the reference's icon style.

## 6. Data integrity
- [ ] Only persona data (Jordan Avery, …4821, …2208, …7710, …8535) — never reference-frame
      real data, never invented accounts.
- [ ] Balances unchanged unless the step's action moves money.

## 7. Honesty
- [ ] If any element is a reconstruction (no real reference exists), it is recorded in
      `generated/manifest.json` → `assumptions`.
- [ ] `[UNVERIFIED]` labels from research are either verified on-screen or disclosed.

Fail → fix the template and re-render (max 2 attempts) → still failing → keep the best render
and record the discrepancy in `assumptions` (never silently ship).
