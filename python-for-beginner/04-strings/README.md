# 04 — Strings

## Concept

A **string** (`str`) is text: anything wrapped in `"double"` or
`'single'` quotes. Python treats both the same — pick one style and stay
consistent (this course uses double quotes, except when the string itself
contains a double quote, where single quotes avoid escaping).

```python
name = "Ava"
quote = 'She said "hi"'   # single quotes here avoid escaping the inner "
```

### Strings are sequences

A string is a sequence of characters, and you can access individual
characters by **index** — position, counting from `0`:

```python
word = "Python"
word[0]    # "P"  — first character
word[1]    # "y"
word[-1]   # "n"  — negative indices count from the end
len(word)  # 6    — number of characters
```

**Indexing starts at 0**, not 1 — this is true of lists and tuples too
(modules 08 and 10), and it's one of the most common early beginner
mistakes: the first item is `word[0]`, and the last is `word[len(word) - 1]`
or, more simply, `word[-1]`.

### Slicing — grabbing a chunk

`string[start:stop]` gives you a slice — from `start` up to (**not
including**) `stop`:

```python
word = "Python"
word[0:2]   # "Py"    — indices 0 and 1, not 2
word[2:]    # "thon"  — from index 2 to the end
word[:2]    # "Py"    — from the start to index 2
word[:]     # "Python" — the whole string (a copy)
```

### Strings are immutable

Once created, a string cannot be changed in place —
`word[0] = "J"` raises `TypeError: 'str' object does not support item
assignment`. Every string "modification" actually builds and returns a
**new** string:

```python
word = "Python"
word = word.upper()   # new string "PYTHON", word now points to it
```

### Concatenation and repetition

```python
"Py" + "thon"   # "Python"   — joins strings
"ab" * 3        # "ababab"   — repeats a string
```

### f-strings (formatted string literals)

You saw these briefly in module 02 — the standard way to build strings
from variables:

```python
name = "Ava"
score = 97.456
f"{name} scored {score}"          # "Ava scored 97.456"
f"{name} scored {score:.1f}"      # "Ava scored 97.5"  — format spec: 1 decimal place
f"{name.upper()}"                 # "AVA" — you can call methods inside { }
```

The `:.1f` part is a **format spec** — `.1f` means "fixed-point, 1 digit
after the decimal." You'll see `:.2f` a lot for money (2 decimal places).

### Common string methods

A **method** is a function that belongs to a value and is called with a
dot: `value.method()`. Strings have many built in:

```python
s = "  Hello, World!  "
s.strip()          # "Hello, World!"       — remove leading/trailing whitespace
s.lower()          # "  hello, world!  "   — lowercase
s.upper()          # "  HELLO, WORLD!  "   — uppercase
s.replace("l", "L")# "  HeLLo, WorLd!  "   — replace all occurrences
s.strip().split(", ")  # ["Hello", "World!"]  — split into a list on a separator
"-".join(["a", "b", "c"])  # "a-b-c"        — opposite of split: glue a list into a string
s.startswith("  H")  # True
s.strip().endswith("!")  # True
"world" in s.lower()  # True — membership check, works on any sequence
```

None of these change `s` itself — they all **return a new string**, since
strings are immutable. `s.upper()` alone (without `s = s.upper()`) throws
the result away.

### Escape sequences

Special characters inside a string, written with a backslash:

| Sequence | Meaning |
|---|---|
| `\n` | newline |
| `\t` | tab |
| `\"` | a literal double quote (in a double-quoted string) |
| `\\` | a literal backslash |

## Common beginner mistakes

- **Off-by-one errors with indexing/slicing.** `word[0:3]` gives the
  first **three** characters (indices 0, 1, 2) — `stop` is exclusive.
  This trips up everyone at first; there's no shortcut but practice.
- **Forgetting strings are immutable.** `s.upper()` does nothing to `s`
  unless you reassign it: `s = s.upper()`.
- **`+` between a string and a number.** `"Score: " + 97` raises
  `TypeError: can only concatenate str (not "int") to str`. Convert first:
  `"Score: " + str(97)`, or better, use an f-string: `f"Score: {97}"`.
  More on type conversion in module [05](../05-input-output-and-conversion/README.md).

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `first_and_last(word)` — return a tuple `(first_char, last_char)` of
   `word`, using indexing.
2. `reverse_string(word)` — return `word` reversed. Hint: slicing with a
   step, `word[::-1]`, reads the string backwards.
3. `shout(sentence)` — return `sentence` in uppercase with an extra `"!"`
   appended.
4. `clean_and_split(text)` — strip leading/trailing whitespace from
   `text`, then split it into a list of words on spaces.
5. `format_price(item, price)` — return an f-string in the shape
   `"<item>: $<price to 2 decimal places>"`, e.g.
   `format_price("Coffee", 3.5)` returns `"Coffee: $3.50"`.

Run it to check yourself:

```bash
python3 python-for-beginner/04-strings/exercise.py
```
