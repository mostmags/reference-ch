# chase-tutorial-kit

Production kit for Chase tutorial screenshot generation, used by the Muse cloud agent.

- `muse-agent-kit/MUSE_MASTER_PROMPT.md` — the operating prompt (paste into Muse)
- `muse-agent-kit/REFERENCE_INDEX.md` — index of the collected reference frames
- `muse-agent-kit/DESIGN_RULES.md` — exact Chase UI fidelity rules
- `muse-agent-kit/QA_CHECKLIST.md` — per-screen acceptance gate
- `muse-agent-kit/WORKFLOW.md` — pipeline detail
- `references/` — 88+ verified reference frames of the current Chase Mobile iOS UI and chase.com desktop
- `research/` — verified knowledge base (navigation maps, design system, screen catalog, sources)
- `render/` — optional HTML template engine (used only on explicit request)

Muse fetches everything from this repo via raw URLs and compiles its output as
`chase-output-<date>.zip` (see MUSE_MASTER_PROMPT.md Step 7) for local import.
