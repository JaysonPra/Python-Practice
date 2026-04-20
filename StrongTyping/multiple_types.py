from pathlib import Path
from typing import TypeAlias

FileSource: TypeAlias = str | Path


def load_file(file_path: FileSource) -> None:
    print(f"File path type: {type(file_path)}")


root = Path(__file__).resolve().parent
file = root / "generics.py"
load_file(file_path=file)
