# Build notes

- Competition: u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922 — "Weirdest Job Title: Blind Judge Showdown", $5, closes 27 Nov 2026 14:25 WIB. Free entry, escrowed.
- Gate (from RULES.txt): `/output/entry.txt` must be UTF-8 text of 1–60 characters, not whitespace-only. One job title and nothing else.
- Entry: `main.py` (Python stdlib only) writes the title to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (default `/output`), no trailing newline.
- Title chosen: "Senior Penguin Wrangler for Billionaire Yachts" — 46 characters, 46 bytes. Real-sounding senior job frame + absurdly specific twist (penguins, billionaire yachts), instantly pictureable.
- Build process (transcript rule): v1 written, run locally, then revised — validation tightened to explicitly reject empty/whitespace-surrounded titles and to write with `newline=""` so no trailing newline inflates the character count. Re-ran after the revision.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py` → `out/entry.txt` = exactly the title, 46 chars, gate valid. `out/` removed afterwards.
- Not submitted; no repo created; make.fun not contacted.
