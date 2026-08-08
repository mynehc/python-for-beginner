# 25 — Regular Expressions

## Concept

A **regular expression** (regex) is a pattern for matching text — far
more powerful than `"substring" in text` or `.startswith(...)` for
anything beyond an exact literal match. Python's regex support lives in
the `re` module.

### The basic functions

```python
import re

re.search(r"\d+", "order #42 shipped")   # a Match object (found "42"), or None
re.match(r"\d+", "42 items")               # matches only at the START of the string
re.findall(r"\d+", "a1 b22 c333")          # ["1", "22", "333"] — every match, as a list
re.sub(r"\d+", "#", "a1 b22 c333")         # "a# b# c#" — replace every match
```

- `re.search` — find the pattern **anywhere** in the string; returns a
  `Match` object (truthy) or `None` (falsy) — the standard way to check
  "does this text contain X shaped like this."
- `re.match` — like `search`, but only matches at the very **start** of
  the string.
- `re.findall` — return **every** match as a list of strings.
- `re.sub(pattern, replacement, text)` — replace every match.

The `r` before the pattern string (`r"\d+"`) makes it a **raw string** —
backslashes are left alone instead of being treated as escape sequences
(module 04). Regex patterns use backslashes constantly (`\d`, `\w`,
`\s`), so **always** write regex patterns as raw strings to avoid Python
trying to interpret them first.

### Pattern building blocks

| Pattern | Matches |
|---|---|
| `\d` | any single digit (`0-9`) |
| `\w` | any "word" character (letter, digit, underscore) |
| `\s` | any whitespace (space, tab, newline) |
| `.` | any character except newline |
| `+` | one or more of the previous thing |
| `*` | zero or more of the previous thing |
| `?` | zero or one of the previous thing (makes it optional) |
| `{3}` | exactly 3 of the previous thing |
| `[abc]` | any one of `a`, `b`, or `c` |
| `[^abc]` | any character **except** `a`, `b`, or `c` |
| `^` | start of the string |
| `$` | end of the string |
| `\|` | "or" — matches either side |

Combine them: `\d+` = "one or more digits," `\w+@\w+\.\w+` = a
(simplified) email shape, `^\d{3}-\d{4}$` = "the whole string must be
exactly 3 digits, a dash, 4 digits."

### Getting the matched text out

```python
match = re.search(r"\d+", "order #42 shipped")
if match:
    match.group()   # "42" — the matched text
```

Always check `if match:` before calling `.group()` — calling `.group()`
on `None` (no match found) raises `AttributeError`.

### Groups — capturing parts of a match

Parentheses `( )` in a pattern **capture** that piece separately:

```python
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2026-01-15")
match.group()    # "2026-01-15" — the whole match
match.group(1)   # "2026"        — first parenthesized group
match.group(2)   # "01"          — second group
match.group(3)   # "15"          — third group
```

### A word of caution

Regex is powerful but easy to overuse and hard to read once patterns get
long — a well-named helper function or even a couple of `str.split()`
calls is often clearer for simple cases. Reach for regex when you
genuinely need pattern matching (validating a shape, extracting a
variable substring), not as a default first tool for every string
problem.

## Common beginner mistakes

- **Forgetting the `r` prefix.** `"\d+"` (no `r`) happens to still work
  for `\d` since it's not a recognized Python escape sequence, but
  patterns using `\n`, `\t`, or similar get silently mangled before
  regex even sees them. Always use `r"..."` for patterns, no exceptions,
  so you never have to think about which sequences are "safe" without
  it.
- **Confusing `match` and `search`.** `re.match(r"\d+", "a1")` returns
  `None` because the string doesn't *start* with a digit — `re.search`
  would find the `1` anywhere in the string.
- **Calling `.group()` without checking for `None` first** —
  `AttributeError: 'NoneType' object has no attribute 'group'`.
- **Greedy vs matching too much/little** — `.+` grabs as much as
  possible by default, which can match further than intended on
  complex strings. Not something to worry about for the patterns in this
  module's exercise, but good to know exists once your patterns grow.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `contains_digit(text)` — return whether `text` contains at least one
   digit.
2. `extract_numbers(text)` — return a list of every run of digits in
   `text`, as strings, e.g. `extract_numbers("a1 b22 c333")` returns
   `["1", "22", "333"]`.
3. `mask_digits(text)` — return `text` with every run of digits replaced
   by `"#"`.
4. `is_valid_hex_color(text)` — return whether `text` is a valid hex
   color code: a `#` followed by exactly 6 hex digits (`0-9`, `a-f`,
   `A-F`), e.g. `"#1A2b3C"` is valid, `"1A2b3C"` (no `#`) and `"#12"`
   (too short) are not. Anchor the pattern with `^` and `$` so partial
   matches inside a longer string don't count.
5. `extract_date_parts(text)` — `text` contains a date shaped like
   `YYYY-MM-DD` somewhere in it; return a tuple `(year, month, day)` as
   strings using capture groups, or `None` if no date is found.

Run it to check yourself:

```bash
python3 python-for-beginner/25-regex/exercise.py
```
