"""Six Words, One Story — writes one six-word story to /output/entry.txt."""

import os

STORY = "Sold the lighthouse. Kept the light."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise SystemExit(f"story must be six words, got {len(words)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")
    print(f"wrote /output/entry.txt ({len(words)} words)")


if __name__ == "__main__":
    main()
