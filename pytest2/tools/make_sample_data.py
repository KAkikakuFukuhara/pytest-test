import json
from pathlib import Path


if __name__ == "__main__":
    char2int = {c:v for v, c in enumerate("abcdefg") }
    text = json.dumps(char2int)

    file_dir: Path = Path(__file__).absolute().parent
    root_dir: Path = file_dir.parent.parent
    save_file: Path = root_dir.joinpath("data/samples/m5.json")
    save_file.parent.mkdir(parents=True)
    with save_file.open("w") as f:
        f.write(text)

