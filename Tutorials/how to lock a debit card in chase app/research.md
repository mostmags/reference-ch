# Research: How to lock a debit card in the Chase app

## Platform determination
Mobile-only topic. Locking a debit card is performed in the Chase Mobile app (iOS) by selecting
the checking account the debit card is tied to. The same lock is also reachable on chase.com
(More dropdown > Account services > "Lock and unlock your card"), but this tutorial covers the
app flow end to end and never mixes platforms.

## Verified flow (A to Z)
1. Open the Chase Mobile app and sign in (username + password, blue "Sign in" button).
2. On the home dashboard, under "Bank accounts", tap "TOTAL CHECKING (...4821)" - the checking
   account the debit card is tied to (per Chase: "Debit Card: Select the checking account your
   debit card is tied to").
3. On the account screen, scroll down and tap "Manage account".
4. On the Manage account screen, tap "Lock & unlock card" (first of the three account-tools
   buttons, next to "Replace a lost or damaged card" and "Dispute a transaction").
5. The "Lock & unlock your card" screen opens with the heading "Misplaced your card?" and the
   disclosure: locking blocks new purchases and ATM withdrawals made with the card number, but
   does NOT block fees, credits, digital wallet purchases, or repeating transactions;
   previously authorized transactions continue to process.
6. Next to "DEBIT/ATM CARD (...2208)", tap the blue "Lock card" button.
7. Confirmation: the green line "You've locked your card." appears and the button becomes
   "Unlock card".
8. To unlock later, return to this screen and tap "Unlock card".

## Fees, limits, negative claims (verified)
- Locking and unlocking a card is free; there is no fee and no daily limit involved.
- Locking does NOT cancel recurring charges or digital-wallet purchases (Chase's own pro tip).
- Locking is not the same as reporting a card lost/stolen: "Replace a lost or damaged card"
  is a separate tool that cancels the card number and ships a new one.

## Sources
- Chase official video transcript, "Lock and unlock your card from the Chase Mobile App":
  https://www.chase.com/content/chase-ux/en/digital/customer-service/helpful-tips/credit-cards.transcript.html/6148059859001
- Chase debit card FAQ (Manage account > "Lock & unlock card"):
  https://www.chase.com/personal/personal-account/faqs/debit-atm-card
- Chase unauthorized-transactions FAQ (choose account, "Account services" > "Lock & unlock card"):
  https://www.chase.com/personal/personal-account/faqs/unauthorized-transactions
- Repo reference frames: references/mobile-ios/home-dashboard/home-account-screen.png,
  checking/account-screen.png, checking/manage-account.png,
  card-management/misplace-your-card.png, card-management/card-locked.png
- muse-agent-kit/DESIGN_RULES.md (canvas, persona, typography, palette)

## Reference coverage
All five flow screens after sign-in existed in the repo library; no internet reference hunting
was required and no new reference images were collected for this topic.

## Known deviations
- s01 (sign-in screen) has no reference anywhere in the repo (the website/ frames listed in
  REFERENCE_INDEX.md are not actually pushed to the repo), so it was reconstructed from
  DESIGN_RULES.md and the current app's known sign-in layout. Review it first.
- The Chase octagon logo and the Freedom Unlimited card graphic are hand-drawn approximations.
- Persona data (Jordan Avery) is used on every screen per DESIGN_RULES.md; no reference-frame
  personal data was carried over.
