"""Weirdest Job Title: Blind Judge Showdown.

Writes a single original job title (<= 60 chars) to entry.txt.
Stdlib only. Respects MAKEFUN_OUTPUT_DIR, defaults to /output.
"""
import os

TITLE = "Senior Penguin Wrangler for Billionaire Yachts"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-60 chars, UTF-8, not whitespace-only, no trailing newline
    # (a trailing newline would count toward the 60-char gate).
    text = TITLE.strip()
    if not text or text != TITLE:
        raise ValueError("title must be non-empty with no surrounding whitespace")
    if len(text) > 60:
        raise ValueError(f"title length {len(text)} exceeds 60-char gate")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
