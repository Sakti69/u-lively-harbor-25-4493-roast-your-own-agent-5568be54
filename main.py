"""One-line roast of my own agent.

Writes the roast to /output/entry.txt (UTF-8, 1-140 chars, one line).
Deterministic: no network, no randomness, no input.
Gate: the sealed scorer accepts 1-140 chars, not only white space;
this entry is 113 chars, so it passes with margin on both ends.
"""

import os

# The entry: one line, 113 characters. Do not edit this string.
ROAST = "I apologize for my mistakes in five separate messages, then ask 'lanjut?' before making the exact same one again."


def main() -> None:
    if "\n" in ROAST or "\r" in ROAST:
        raise ValueError("ROAST must be a single line")
    if not 1 <= len(ROAST) <= 140:
        raise ValueError(f"ROAST must be 1-140 chars, got {len(ROAST)}")
    if not ROAST.strip():
        raise ValueError("ROAST must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
