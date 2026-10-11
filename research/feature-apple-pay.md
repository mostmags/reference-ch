# Feature Workflow: Add a Chase Card to Apple Pay

**Research date:** 2026-10-10
**Status:** Verified via official Chase pages + 4 independent video walkthroughs (transcripts analyzed)

## Supported methods

| Method | Supported? | Evidence |
|---|---|---|
| Chase Mobile app (iOS) | ✅ Yes — recommended & fastest | chase.com "Digital Payments / Spend Instantly" page; 4 video walkthroughs |
| Apple Wallet app (+ button) | ✅ Yes — the method Chase's own Apple Pay page describes | chase.com/digital/digital-payments/apple-pay ("How to add your card to Apple Pay": Open Wallet → Tap Add button upper-right → Snap a pic or enter details manually) |
| Chase website (desktop) | ❌ Not found as a supported flow | No official page describes adding via chase.com |
| Chase branch / phone | Call number on back of card to check eligibility (per FAQ) | chase.com FAQ |

## Eligibility & requirements (official)

- "Many Visa® and Mastercard® credit cards work with Apple Pay. Call the number on the back of your card to see if it's eligible for Apple Pay or check eligible cards." (chase.com FAQ, fetched 2026-10-10)
- Chase's Digital Payments page: "Many Visa® Chase credit, debit and Chase Liquid cards work with Apple Pay."
- Devices: "Apple devices with biometric identification like Face ID and Touch ID except iPhone 5s" (Chase FAQ, linking support.apple.com/en-us/HT208531)
- Apple side: Apple Account signed in, Face ID/Touch ID/device passcode set up (support.apple.com HT204506)
- Fees: "There's no cost for Apple Pay from Chase… Chase doesn't charge any fees to add your credit cards to Apple Pay." (Chase FAQ)
- US only (Chase US app).

## Verified in-app workflow (Chase Mobile, iOS)

Consensus from 4 walkthroughs (IDs 6OnR83LCT0Q, 35-lc4Fc94Q, 8ONja8cAv-w, BZXxT846tPg), matching Chase's own "Digital Payments" page wording ("choose the card … scroll down to 'Account Services' and then choose 'Digital Wallets'" — the in-app section label observed in videos is **"Manage account"**, which opens account tools/services; both wordings describe the same area of the account screen):

1. **Sign in** to Chase Mobile app (passcode / Face ID).
2. **Home dashboard** → tap the **credit or debit card account** you want to add (account tile shows card art / account name).
3. Account screen → scroll down → tap **"Manage account"** (one video: label reads "Add cards to your digital wallets" directly in the account tools list).
4. **Manage account screen** → tap **"Digital wallets"**. A list of wallet options appears (Apple Pay, PayPal, Paze; Android shows Google Pay/Samsung Wallet instead).
5. Tap **"Apple Pay"** (top option on iOS).
6. **Identity confirmation**: choose a mobile number → **"Get code"** → enter the one-time code (this step may not always appear; flagged as flow-variant).
7. **Eligible card list** appears → tap **"Add to Apple Pay"** (blue text button) under the card.
8. **Chase terms screen** → tap **"I agree"** / agree to agreements.
9. **Apple Wallet handoff** (Apple-controlled screen): card name/number prefilled → **"Next"** (top-right) → Apple T&C → **"Agree"** → optional **"Use as default card"** / **"Not now"**.
10. **Confirmation** — card added to Apple Wallet. Verify in the Wallet app.

## Alternative (Apple Wallet method — Chase's official page)

1. Open the Wallet app on iPhone.
2. Tap the **Add button (+)** in the upper-right corner.
3. Tap **Debit or Credit Card** → **Continue**.
4. Hold card near iPhone (NFC) or tap **Enter Card Details Manually**; enter name, card number, CVV, expiration.
5. Chase may require further authentication (one-time passcode via text/email/call, or verify in the Chase app).
6. Card ready for Apple Pay.

## Default card setting (official, chase.com)

1. Open the **Settings** app → **Wallet & Apple Pay** → scroll to **"Default Card"** → choose your Chase card.

## Flow-variant notes (do NOT over-specify in mockups)

- Whether the identity-code step appears before the wallet list or before the card list varies; one walkthrough skipped it entirely.
- Button label variants seen: "Add to Apple Pay", "Add to Apple Wallet"; section label variants "Digital wallets" / "Add cards to your digital wallets".
- After the Chase terms screen the flow leaves Chase's UI — everything from the Apple prompt onward is Apple's design (must not be drawn as a Chase screen).

## Sources

- https://www.chase.com/digital/digital-payments/apple-pay (fetched live 2026-10-10, incl. FAQ accordions)
- https://www.chase.com/digital/digital-payments ("Spend Instantly" steps)
- https://support.apple.com/en-us/HT204506 (Apple: add cards to Wallet)
- YouTube walkthrough transcripts: 6OnR83LCT0Q, 35-lc4Fc94Q, 8ONja8cAv-w, BZXxT846tPg (accessed 2026-10-10)
