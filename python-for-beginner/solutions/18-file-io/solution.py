"""Reference solution for Exercise 18: File I/O."""

import os
import tempfile
from pathlib import Path


def write_lines(path, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def read_lines(path):
    with open(path, "r") as f:
        return [line.strip() for line in f]


def append_line(path, line):
    with open(path, "a") as f:
        f.write(line + "\n")


def count_lines(path):
    return len(read_lines(path))


def file_exists(path):
    return Path(path).exists()


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

    write_lines(path, ["only line"])
    assert read_lines(path) == ["only line"]

    os.remove(path)
    os.rmdir(tmp_dir)

    print("All checks passed!")


if __name__ == "__main__":
    _check()
