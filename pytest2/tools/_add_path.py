import sys
from pathlib import Path

def _add_path():
    file_dir: Path = Path(__file__).absolute().parent
    root_dir: Path = file_dir.parent.parent
    if str(root_dir) not in sys.path:
        sys.path.insert(0, str(root_dir))


_add_path()
