from pathlib import Path

class PathUtils:
    ROOT_DIR = Path(__file__).parent.parent

    @staticmethod
    def resolve_path(relative_path: str) -> Path:
        return PathUtils.ROOT_DIR / relative_path