# 18 — File I/O

## Concept

So far every program has lost all its data the moment it finished
running. **File I/O** (input/output) is how a program reads and writes
files on disk, so data survives between runs.

### Opening a file

```python
f = open("notes.txt", "w")   # "w" = write mode (creates the file, or ERASES existing contents)
f.write("Hello, file!\n")
f.close()                     # always close what you open
```

Forgetting `.close()` can leave data un-flushed to disk, or leave the
file locked. There's a much safer pattern for this, next.

### The `with` statement — the pattern you should actually use

```python
with open("notes.txt", "w") as f:
    f.write("Hello, file!\n")
# f is automatically closed here, even if an error happened inside the block
```

`with` is a **context manager** — it guarantees cleanup (closing the
file) happens automatically when the indented block ends, even if
something inside raises an exception. Always prefer `with open(...)` over
manually calling `.close()` yourself — it's less code and strictly safer.
(You'll learn how `with` works under the hood, and how to write your own,
in the advanced modules beyond this course.)

### File modes

| Mode | Meaning |
|---|---|
| `"r"` | read (default) — error if the file doesn't exist |
| `"w"` | write — creates the file if missing, **erases** existing contents |
| `"a"` | append — creates the file if missing, adds to the end otherwise |
| `"r+"` | read and write, file must already exist |

### Reading a file

```python
with open("notes.txt", "r") as f:
    content = f.read()        # the WHOLE file as one string

with open("notes.txt", "r") as f:
    lines = f.readlines()     # a list of lines, each STILL ENDING IN "\n"

with open("notes.txt", "r") as f:
    for line in f:             # loop directly over the file object, one line at a time
        print(line.strip())    # .strip() removes the trailing "\n"
```

Looping directly over the file object (`for line in f:`) is the most
common pattern for processing a file line by line, and doesn't load huge
files entirely into memory at once the way `.read()` does.

### Writing multiple lines

```python
lines = ["first", "second", "third"]
with open("notes.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")   # write() does NOT add a newline for you
```

`f.write(...)` doesn't automatically add `"\n"` — unlike `print()`, which
does. Add it yourself if you want each write on its own line.

### Checking if a file exists

```python
from pathlib import Path

Path("notes.txt").exists()   # True / False
```

`pathlib.Path` is the modern way to work with file paths in Python —
worth knowing the name exists even though this module sticks mostly to
plain string paths with `open()`. `Path` also has convenience shortcuts:
`Path("notes.txt").read_text()` and `Path("notes.txt").write_text("...")`
open, read/write, and close a file in a single call, for simple cases.

### Common file errors

```python
open("does-not-exist.txt", "r")   # FileNotFoundError
```

Combine with error handling (module 16) when a missing file is an
expected possibility, not a bug:

```python
try:
    with open("config.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    content = ""   # sensible fallback
```

## Common beginner mistakes

- **Using `"w"` mode when you meant `"a"`.** `"w"` silently erases
  whatever was already in the file. Use `"a"` if you want to add to
  existing content instead of replacing it.
- **Forgetting `with`, and forgetting `.close()` too.** Leads to data not
  being fully written, or too many files left open. Always use `with`.
- **Forgetting `.strip()` when reading lines**, ending up with stray
  `"\n"` characters embedded in your data everywhere downstream.
- **Assuming a relative path is relative to the file** — it's actually
  relative to your current working directory in the terminal (wherever
  you ran `python3` from), not necessarily where the `.py` file lives.
  This surprises people the first time a script "can't find" a file that
  is clearly sitting right next to it — check with
  `print(Path.cwd())` if unsure.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `write_lines(path, lines)` — write each string in the `lines` list to
   the file at `path`, one per line (`"w"` mode — overwrite).
2. `read_lines(path)` — read the file at `path` and return a list of its
   lines, with the trailing newline stripped from each.
3. `append_line(path, line)` — add `line` as a new line at the **end** of
   the file at `path`, without erasing what's already there.
4. `count_lines(path)` — return how many lines are in the file at `path`.
5. `file_exists(path)` — return whether a file exists at `path`, using
   `pathlib.Path`.

The `_check()` function creates and cleans up a temporary file for you —
you don't need to worry about test files being left behind.

Run it to check yourself:

```bash
python3 python-for-beginner/18-file-io/exercise.py
```
