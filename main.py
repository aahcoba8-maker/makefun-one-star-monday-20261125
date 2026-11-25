"""One Star for Monday — writes a one-star restaurant review of Monday.

The entry text is a plain-text, single-line, 22-word review that reads as a
real diner's complaint: a table, a server who forgets the order, and a bill
for a full week of work before breakfast. Monday-specific, short, quotable.
"""

import os

ENTRY = "One star. The server sat me at a table, forgot my order, and billed me a full week of work before breakfast."

# Kit gate: entry.txt must be UTF-8 text of 1 to 180 characters and at most
# 25 words. Fail loudly here rather than shipping an invalid entry.
assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
assert len(ENTRY.split()) <= 25, "entry must be at most 25 words"
assert "\n" not in ENTRY, "entry must be a single line"


def output_path():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
