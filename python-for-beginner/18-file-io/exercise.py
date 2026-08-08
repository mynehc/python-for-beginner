"""
Exercise 18: File I/O

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""

import os
import tempfile
from pathlib import Path


def write_lines(path, lines):
    """Write each string in `lines` to the file at `path`, one per line ("w" mode)."""
    # TODO: implement
    raise NotImplementedError


def read_lines(path):
    """Read the file at `path`; return a list of its lines with "\\n" stripped."""
    # TODO: implement
    raise NotImplementedError


def append_line(path, line):
    """Add `line` as a new line at the END of the file at `path` ("a" mode)."""
    # TODO: implement
    raise NotImplementedError


def count_lines(path):
    """Return how many lines are in the file at `path`."""
    # TODO: implement
    raise NotImplementedError


def file_exists(path):
    """Return whether a file exists at `path`, using pathlib.Path."""
    # TODO: implement
    raise NotImplementedError


def _check():
    tmp_dir = tempfile.mkdtemp()
    path = os.path.join(tmp_dir, "notes.txt")

    assert file_exists(path) is False

    write_lines(path, ["first", "second", "third"])
    assert file_exists(path) is True
    assert read_lines(path) == ["first", "second", "third"]
    assert count_lines(path) == 3

    append_line(path, "fourth")
    assert read_lines(path) == ["first", "second", "third", "fourth"]
    assert count_lines(path) == 4

    # "w" mode must overwrite, not append
    write_lines(path, ["only line"])
    assert read_lines(path) == ["only line"]

    os.remove(path)
    os.rmdir(tmp_dir)

    print("All checks passed!")


if __name__ == "__main__":
    _check()
