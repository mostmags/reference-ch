# Muse Agent Kit — Chase tutorial screenshot pipeline

Everything Muse needs to run the same production pipeline I use:
**research topic → reference images (local library first, then internet) → build guide →
HTML-blueprint screenshots → element-by-element QA → install into Screenshot Automator.**

## What to give Muse

1. **Paste `MUSE_MASTER_PROMPT.md`** (the whole file) into Muse once per project/session.
2. Make sure Muse can read this project folder:
   `/Users/amanmaan/Pictures/CHASETT/chase-ui-research/` and the tool folder
   `/Users/amanmaan/Documents/TOOLS/Screenshot Automator/`.
   If Muse cannot access local folders, zip this `chase-ui-research/` folder, upload it, and add:
   *"Work on the uploaded folder; at the end, return the full folder with all changes as a zip."*
3. Then just send topics: `how to freeze a chase debit card` — one or a batch.

## Files in this kit

| File | Purpose |
|---|---|
| `MUSE_MASTER_PROMPT.md` | The paste-ready operating prompt (pipeline + rules + paths) |
| `WORKFLOW.md` | The detailed pipeline, file conventions, render commands, install steps |
| `DESIGN_RULES.md` | Exact UI fidelity rules: colors, fonts, sizes, chrome, components, persona, prohibitions |
| `REFERENCE_INDEX.md` | Index of the 88 collected reference frames (+ rules for adding new ones) |
| `QA_CHECKLIST.md` | The per-screen acceptance gate Muse must run before approving a screenshot |
| `TOPIC_TEMPLATE/` | Scaffold for each new topic pack (research.md, screenshot-prompts.md, video-guide.md, references/) |

## Existing assets Muse will reuse (already in the project)

- `references/mobile-ios/` — 88 verified 4K frames of the current Chase Mobile UI (+ website frames)
- `research/design-system.md`, `research/app-navigation.md`, `research/website-navigation.md`,
  `research/screen-catalog.md`, `research/feature-apple-pay.md`, `research/sources.md`
- `render/chase_ui.py` + `render/desktop.py` — the HTML template library (mobile + desktop)
- `render/build.py` — step→template router and page builder

## The two rules that make it work

1. **Reference library first, internet second** — and every newly found reference is saved back
   into the library (with source + date) so later topics find it automatically.
2. **QA gate before "complete"** — a screenshot ships only if it passes `QA_CHECKLIST.md`;
   otherwise it's fixed or disclosed in the manifest, never silently wrong.
