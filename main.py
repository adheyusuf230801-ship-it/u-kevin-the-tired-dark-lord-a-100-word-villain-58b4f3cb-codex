import os
from pathlib import Path


MONOLOGUE = "I am Veyra Quill, queen of the Salt March. Nine years of candle tax bought the brass key; the fleet burned on its own wax, though the ledger lists their sons. Tonight I unpin the moon and lower it over the wells, so every town must pay me for light. The key is in the red box. No, blue; the red holds the treaty with Noll. Put it by the map. Where was I? The third knot, after the tide mark. Leave that for morning. Ring the harbor bell. If the moon answers, tell it the queen has stepped out."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(MONOLOGUE, encoding="utf-8")


if __name__ == "__main__":
    main()
