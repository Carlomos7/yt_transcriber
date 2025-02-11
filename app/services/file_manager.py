import pathlib
from app.config import settings

BASE_DIR = pathlib.Path(settings.output_dir)


def get_file_path(file_type: str, filename: str) -> str:
    """Returns the absolute path of a requested file."""
    folder = BASE_DIR / file_type
    file_path = folder / filename

    if file_path.exists():
        return str(file_path.resolve())

    return None
