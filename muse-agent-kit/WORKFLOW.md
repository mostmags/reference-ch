# WORKFLOW.md — Muse pipeline, file conventions, and commands

Per-topic pipeline (repeat for each topic; never skip the QA gate):

```
research → references (local first) → guide JSON → topic pack
        → HTML blueprints → render → QA gate → install → mark complete
```

## 0. Setup checks (once per session)

- Reference library present: `references/mobile-ios/` (~88 frames) + `references/website/`.
- Render engine works: `cd /Users/amanmaan/Pictures/CHASETT/chase-ui-research/render && python3 build.py`
  (serves via `python3 -m http.server 8734` from the `render/` folder; capture each `.shot`
  element: `.shot` = 786×1704, `.shot.desktop` = 2880×1800).
- Tool folders exist: `cashgen-pipeline/{guides,chase-research-packs}`, `~/Screenshot Workspace`,
  `~/Documents/Tutorial`.

## 1. Topic folder convention

```
topics/<slug>/
├── research.md              # A–Z workflow, facts, negative claims, sources
├── screenshot-prompts.md    # shared design system + one prompt per screen
├── video-guide.md           # 1:1 narration
├── references/              # frames used by THIS topic (copies)
├── generated/               # s01.png … outputs + manifest.json
```

Slug = lowercase-hyphenated topic title. Register the topic in
`chase-research-packs/GENERATION_STATE.json` (status "pending") when the pack is created.

## 2. Reference reuse & growth

- First search `muse-agent-kit/REFERENCE_INDEX.md` (88 frames indexed by screen).
- Frame files live in `references/mobile-ios/<folder>/<file>.png`; descriptions are in
  `references/frame-manifest.csv`.
- New captures: save to `references/mobile-ios/<new-folder>/` or `references/website/`,
  append to BOTH the index and the CSV (file, source, date, description). This is what makes
  future topics skip the internet search.
- If a fresh capture is impossible, build the screen from DESIGN_RULES.md + the closest sibling
  frame and record it as a reconstruction in the manifest assumptions.

## 3. Guide JSON requirements (schema-compatible with the tool)

- `topicSlug`, `topicName`, `primaryApp`, `contract{direction,startState,excludedSetup,
  successProof,actors}`, `premiseMap`, `sourceUrls`, `claims[]` (id/class/claim/sources/
  locator/status), `screenshotSteps[]` (id s01…, title, instruction, appId, fromState,
  expectedText, referencePath, sourceType), `videoSteps[]` (1:1), `introduction`,
  `accuracyNotes`, `narrationCount`.
- Opening steps are mandatory: app topics start at the home dashboard
  ("In Chase Mobile, open the app and sign in"); web-only topics start with
  "On chase.com, open the website and sign in".
- One action per screenshot. Final step = payoff/verification record.

## 4. Rendering

- Preferred: use the existing engine. Add the topic's steps to `render/build.py` routing
  (keyword rules map step titles → templates) or use the OVERRIDES dict for explicit control.
- Templates: `chase_ui.py` — home/account/manage/lock/replace/activate/dd/show-details/
  statements/paperless/quickdeposit/pay-transfer/transfers/wires/zelle/disputes/pin/profile/
  security/password/external-accounts/apple-wallet/credit-journey/stored-cards/trade/loan/
  autopay/bizweb + desktop.py — d_web/d_ur/d_brand/d_fee_table/d_locator/d_bizweb.
- New screen type → write a new template function modeled on the closest one + DESIGN_RULES.md,
  using the reference frame as the layout source.
- Capture: serve `render/` on `http://127.0.0.1:8734`, open `pages/<slug>.html`, screenshot each
  `.shot` element (viewport 900×1800 works), save as `s01.png…` into `topics/<slug>/generated/`
  AND `chase-research-packs/<slug>/generated/`.

## 5. QA gate (per screen — do not skip)

Checklist (also in QA_CHECKLIST.md): verbatim expectedText; layout vs reference frame; colors/
fonts/radii per DESIGN_RULES; status bar or desktop chrome; persona data only; buttons vertically
centered; nothing clipped; no invented UI. Fail → fix template → re-render (max 2 retries) →
else record in manifest `assumptions`.

## 6. Install & state

See MUSE_MASTER_PROMPT.md Step 6. Keep GENERATION_STATE.json as the single queue truth:
"pending" → "complete" (never touch "complete" topics without an explicit "redo").

## 7. Batch command examples for Muse

- Single topic: `research and generate screenshots for: how to freeze a chase debit card`
- Batch: `run the full pipeline for these topics: …` (process in order, skip completed)
- Redo: `redo topic <slug> — it was updated` (flip its status to "redo" first or say "redo").
