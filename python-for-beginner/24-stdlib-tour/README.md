# 24 — Standard Library Tour

## Concept

You've already used a few standard library modules (`math`, `random` in
module 17). Python's standard library is enormous — this module is a
tour of a few more genuinely everyday ones. As always, `import` first.

### `datetime` — dates and times

```python
from datetime import date, datetime, timedelta

today = date.today()             # today's date, e.g. date(2026, 8, 8)
today.year, today.month, today.day  # 2026, 8, 8

d = date(2026, 1, 15)
d.strftime("%B %d, %Y")           # "January 15, 2026" — format a date as text

parsed = datetime.strptime("2026-01-15", "%Y-%m-%d")  # text -> datetime object
parsed.date()                                            # date(2026, 1, 15)

d2 = date(2026, 2, 1)
diff = d2 - d                     # a timedelta
diff.days                          # 17 — number of days between the two dates
```

`strftime` ("string format time") turns a date/datetime **into** text;
`strptime` ("string parse time") turns text **into** a date/datetime —
easy to mix up the names, remember "**f**ormat" makes text, "**p**arse"
reads text. Common format codes: `%Y` (4-digit year), `%m` (month
number), `%d` (day), `%B` (full month name), `%H:%M:%S` (time).

### `json` — reading and writing structured data

JSON (JavaScript Object Notation, but a plain data format, not tied to
JavaScript) is the standard way to save structured Python data
(dicts/lists/strings/numbers/bools/`None`) as text — used constantly for
config files, API responses, and simple data persistence (exactly what
this course's capstone projects use to save data between runs).

```python
import json

data = {"name": "Ava", "age": 30, "tags": ["admin", "verified"]}

text = json.dumps(data)              # dict -> JSON string
text = json.dumps(data, indent=2)    # same, pretty-printed for readability

parsed = json.loads(text)            # JSON string -> dict
parsed == data                        # True

# directly to/from a file (combines with module 18's file handling):
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)     # note: dump (to a file), not dumps (to a string)

with open("data.json", "r") as f:
    loaded = json.load(f)             # load (from a file), not loads (from a string)
```

`dumps`/`loads` ("dump/load **s**tring") work with strings already in
memory; `dump`/`load` (no `s`) work directly with an open file. Easy to
mix up — if you get a `TypeError` about the argument being a file object
instead of a string (or vice versa), check which one you meant.

### `collections.Counter` — counting made easy

You built a word-counting function by hand back in module 11. The
standard library already has exactly that:

```python
from collections import Counter

words = ["a", "b", "a", "c", "b", "a"]
counts = Counter(words)
counts             # Counter({'a': 3, 'b': 2, 'c': 1})
counts["a"]         # 3
counts.most_common(2)  # [('a', 3), ('b', 2)] — the 2 most common, most-first
```

`Counter` is a dict subclass — every dict operation from module 11 works
on it too, plus `.most_common()`.

### `os` and `pathlib` — the filesystem

You met `pathlib.Path` briefly in module 18. A couple more common
operations:

```python
from pathlib import Path

Path.cwd()                    # your current working directory
Path("data.json").exists()    # True/False
Path("data.json").name        # "data.json" — just the filename
Path("folder/data.json").parent  # Path("folder") — the containing directory
```

`os` is the older, lower-level equivalent (`os.getcwd()`,
`os.path.exists(...)`) — you'll see both styles in real code, but
`pathlib` is the modern, generally recommended one for new code.

## Common beginner mistakes

- **`json.dumps` vs `json.dump`** (and `loads` vs `load`) — mixing these
  up is extremely common; remember the `s` means "string."
- **Trying to `json.dumps()` something JSON can't represent** — a
  `datetime` object, for instance, raises `TypeError: Object of type date
  is not JSON serializable`. JSON only understands the handful of types
  listed above; convert dates to strings first (`d.isoformat()` is a
  handy one-liner: `"2026-01-15"`).
- **Wrong `strftime`/`strptime` format string** — if the format doesn't
  exactly match the text, `strptime` raises `ValueError: time data ...
  does not match format ...`. The format string has to describe the
  input exactly, characters and separators included.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `days_between(date1_text, date2_text)` — both are `"YYYY-MM-DD"`
   strings; parse them with `datetime.strptime` and return the absolute
   number of days between them (an `int`).
2. `format_pretty_date(year, month, day)` — return the date formatted as
   `"Month DD, YYYY"`, e.g. `format_pretty_date(2026, 1, 5)` returns
   `"January 05, 2026"`.
3. `to_json(data)` — return `data` (a dict/list) serialized as a JSON
   string.
4. `from_json(text)` — return the Python value parsed from the JSON
   string `text`.
5. `most_common_word(words)` — return the single most common word in the
   list `words`, using `collections.Counter`.

Run it to check yourself:

```bash
python3 python-for-beginner/24-stdlib-tour/exercise.py
```
