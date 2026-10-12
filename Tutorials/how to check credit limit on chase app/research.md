# Research: how to check credit limit on chase app

## Platform determination
Mobile-only topic, performed in the Chase Mobile app (iOS), start to finish on one platform.

## Verified flow
1. Open your chase app and sign in.  [s01.png]
2. On the home screen, tap your Freedom Unlimited credit card.  [s02.png]
3. Look at the card summary section on the account screen.  [s03.png]
4. "Credit limit" shows your total limit, here $5,000.00, with "Available credit" right above it.  [s03.png]
5. Your current balance, $418.77, shows next to your card at the top of the screen.  [s03.png]

## Facts, fees, and limits
Mobile topic. Credit limit sits in the card summary under the current balance on the credit card account screen; it also appears on statements (account summary section). No fee to view. Persona credit limit $5,000; available credit $4,581.23 = limit minus $418.77 balance.

## Sources
- https://www.creditkarma.com/credit-cards/i/how-to-increase-chase-credit-limit
- https://www.chase.com/personal/credit-cards/education/basics/credit-card-limit

## Reference coverage
Screens above map to repo reference frames per manifest.json. Where reference is null, the screen was reconstructed from muse-agent-kit/DESIGN_RULES.md and is flagged for review.

## Known deviations
- The Chase octagon logo, Freedom Unlimited card graphic, and debit card graphic are hand-drawn approximations.
- Persona data (Jordan Avery) is used on every screen per DESIGN_RULES.md; no reference-frame personal data was carried over.
