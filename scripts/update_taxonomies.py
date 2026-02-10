from pathlib import Path
import re


def normalize_list_block(items: str) -> str:
    parts = [x.strip() for x in items.split(",") if x.strip()]
    return "\n".join(f"  - {p}" for p in parts)


def update_file(path: Path) -> None:
    text = path.read_text()
    text = re.sub(
        r"(?m)^categories:\s*\[(.*?)\]\s*$",
        lambda m: "categories:\n" + normalize_list_block(m.group(1)),
        text,
    )
    text = re.sub(
        r"(?m)^tags:\s*\[(.*?)\]\s*$",
        lambda m: "tags:\n" + normalize_list_block(m.group(1)),
        text,
    )
    path.write_text(text)


def main() -> None:
    root = Path("_prints")
    for path in root.glob("*.md"):
        update_file(path)
    print("Updated categories/tags in _prints")


if __name__ == "__main__":
    main()
