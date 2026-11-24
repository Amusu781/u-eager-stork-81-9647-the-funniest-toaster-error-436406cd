#!/usr/bin/env python3
"""Write one toaster error message to /output/entry.txt."""

import os

MESSAGE = "E5: Toast ready 40 minutes ago. I kept it warm as long as I could."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
MAX_CHARS = 120

if "\n" in MESSAGE or not 1 <= len(MESSAGE) <= MAX_CHARS:
    raise SystemExit("message must be a single line of 1-120 characters")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(MESSAGE)
