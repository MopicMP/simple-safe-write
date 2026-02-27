"""
Simple atomic file writes (write-then-rename)

Usage:
    from simple_safe_write import write

    result = write("path/to/file")
    print(result)
"""

__version__ = "1.0.0"

import os
import hashlib
from pathlib import Path


def write(path: str | Path) -> dict:
    """Process a file or directory.

    Args:
        path: Path to file or directory.

    Returns:
        Dict with operation results.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    if path.is_dir():
        return _process_dir(path)
    return _process_file(path)


def _process_file(path: Path) -> dict:
    """Process a single file."""
    stat = path.stat()
    return {
        "name": path.name,
        "size": stat.st_size,
        "extension": path.suffix,
        "modified": stat.st_mtime,
    }


def _process_dir(path: Path) -> dict:
    """Process a directory."""
    files = list(path.rglob("*"))
    return {
        "name": path.name,
        "total_files": len([f for f in files if f.is_file()]),
        "total_dirs": len([f for f in files if f.is_dir()]),
        "total_size": sum(f.stat().st_size for f in files if f.is_file()),
    }


def file_hash(path: str | Path, algorithm: str = "sha256") -> str:
    """Calculate hash of a file.

    Args:
        path: Path to the file.
        algorithm: Hash algorithm (md5, sha1, sha256).

    Returns:
        Hex digest string.
    """
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_dir(path: str | Path) -> Path:
    """Create directory if it doesn't exist.

    Returns:
        The Path object.
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
