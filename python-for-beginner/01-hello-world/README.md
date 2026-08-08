# 01 — Hello, World & Comments

## Concept

A **program** is just a list of instructions a computer runs, one at a
time, top to bottom (until you learn to make it jump around with
conditionals and loops later). Python reads your `.py` file and executes
each line in order.

### `print()`

`print()` is a **function** — a named, reusable chunk of code you can ask
Python to run by writing its name followed by parentheses. `print()`'s job
is to display text in the terminal. Whatever you put inside the
parentheses is shown on screen:

```python
print("Hello, World!")
```

Run that (save it as a `.py` file and run `python3 yourfile.py`) and you'll
see:

```
Hello, World!
```

The text `"Hello, World!"` is called a **string** — any text wrapped in
quotes (single `'...'` or double `"..."`, Python treats them the same; this
course uses double quotes). You'll cover strings properly in module
[04](../04-strings/README.md); for now just know: quotes mean "this is
text, not code."

### Multiple `print()` calls

Each `print()` call outputs on its own line:

```python
print("First line")
print("Second line")
```

```
First line
Second line
```

You can also put a newline **inside** one string using `\n` — a special
two-character sequence Python turns into an actual line break called an
**escape sequence**:

```python
print("First line\nSecond line")
```

Produces the same two-line output as above, from a single `print()` call.

### Comments

A **comment** is text in your code that Python ignores completely — it's
there for humans reading the code, not for the computer. Anything after a
`#` on a line is a comment:

```python
# This line explains what's below it
print("Hello, World!")  # this part is ignored by Python too
```

Use comments to explain **why** something is done a certain way, not to
restate what the code obviously says. `# print hello` above a
`print("hello")` adds nothing; `# users expect their name capitalized here`
adds real information.

### Running a file vs. typing into the REPL

You met both of these in [00-setup](../00-setup/README.md):

- `python3 somefile.py` — runs a saved file top to bottom. This is how
  real programs run, and how you'll run every exercise in this course.
- `python3` (no file) — opens the interactive REPL, one line at a time.
  Great for quick experiments, not for saving real programs.

### Indentation matters

Python uses **indentation** (spaces at the start of a line) to know which
lines of code belong together — unlike many languages that use `{ }` or
`end` keywords. You won't need indentation yet in this module (every line
here is at the same level), but keep it in mind: starting in module
[07](../07-conditionals/README.md), an extra or missing space will change
what your program does, and Python will refuse to run code with
inconsistent indentation (`IndentationError`).

## Common beginner mistakes

- **Forgetting quotes around text**: `print(Hello)` fails with a
  `NameError` — Python thinks `Hello` is the name of something it should
  already know about (a variable, covered next module), not literal text.
  You need `print("Hello")`.
- **Mismatched quotes**: `print("Hello')` (double quote opening, single
  quote closing) is a `SyntaxError`. Quotes must match.
- **Forgetting parentheses**: `print "Hello"` (no parentheses) is a
  `SyntaxError` in Python 3 — this was valid in the old Python 2, so old
  tutorials online sometimes show it. Always use `print(...)`.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `hello_world()` — return the exact string `"Hello, World!"`.
2. `say_hello(name)` — return a greeting for `name`, in the shape
   `"Hello, <name>!"` (e.g. `say_hello("Ava")` returns `"Hello, Ava!"`).
   Build it with string concatenation (`+`).
3. `two_lines()` — return a single string that, when printed, shows two
   lines: `"First line"` then `"Second line"`. Use the `\n` escape
   sequence.

Add at least one `#` comment of your own anywhere in the file explaining
what one of the functions does in your own words — not checked by the
grader, just practice.

Run it to check yourself:

```bash
python3 python-for-beginner/01-hello-world/exercise.py
```
