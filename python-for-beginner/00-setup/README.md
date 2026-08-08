# 00 — Setup

No exercise here — just get your computer ready. Do this once, carefully,
and everything after this is smooth.

## What you're installing and why

To write and run Python code you need two separate things:

1. **Python itself** — the program that reads your `.py` files and actually
   runs them. This is called "the interpreter."
2. **A place to write code** — a text editor. [VS Code](https://code.visualstudio.com/)
   (free) is the most common choice and what these instructions assume, but
   any code editor works.

You'll also be using the **terminal** (also called "command line" or
"shell") a lot — it's just a text-based way to run programs and move around
your computer's files, instead of clicking icons. Every exercise in this
course is run from the terminal.

## 1. Install Python

Check if you already have it:

```bash
python3 --version
```

If you see something like `Python 3.11.6` or higher, you're set — skip to
step 2. If you get an error, or the version starts with `2.`, install
Python 3 from [python.org/downloads](https://www.python.org/downloads/)
(macOS/Windows) or, on macOS with [Homebrew](https://brew.sh) installed:

```bash
brew install python@3.12
```

Aim for **3.10 or newer**. Older versions are missing some syntax used
later in this course (like the `match` statement).

## 2. Open a terminal

- **macOS**: open the "Terminal" app (Cmd+Space, type "Terminal").
- **Windows**: open "PowerShell" or use the terminal built into VS Code.
- **VS Code** (any OS): View → Terminal, or `` Ctrl+` ``.

You should see a prompt where you can type commands and press Enter to run
them.

## 3. Try the Python REPL

The REPL ("Read-Eval-Print Loop") is an interactive Python session — type
one line of code, press Enter, see the result immediately. Great for quick
experiments.

```bash
python3
```

You'll see something like `>>>` — that's the prompt, waiting for input.
Try:

```python
>>> print("hello")
hello
>>> 2 + 2
4
>>> exit()
```

`exit()` (or Ctrl+D) leaves the REPL and returns you to the normal
terminal.

## 4. Run a file instead of the REPL

The REPL is for quick experiments. Real programs live in `.py` files. Try
it:

1. Create a file called `test.py` (in your editor, or with
   `touch test.py` in the terminal) containing:

   ```python
   print("hello from a file")
   ```

2. Run it from the terminal, from the same folder the file is in:

   ```bash
   python3 test.py
   ```

   You should see `hello from a file` printed. This is the pattern you'll
   use for **every exercise in this course**:
   `python3 path/to/exercise.py`.

3. Delete `test.py` — it was just a test.

## 5. A note on virtual environments

Later (module [26](../26-virtual-envs-and-pip/README.md)) you'll learn about
**virtual environments** — isolated, per-project Python setups so that
installing a package for one project doesn't affect another. You don't need
this yet; everything through module 25 uses only Python's built-in
capabilities (the "standard library"), nothing to install. Just know the
name exists for now. When you do need one (module 27, which uses
`pytest`), this repo's [`../../SETUP.md`](../../SETUP.md) has the full
step-by-step walkthrough.

## 6. Editor setup (VS Code)

If you're using VS Code:

1. Install the **"Python" extension** (by Microsoft) from the Extensions
   panel (the four-squares icon on the left, or Cmd/Ctrl+Shift+X).
2. Open this course's folder in VS Code (File → Open Folder).
3. Open any `.py` file — VS Code will pick up the Python extension
   automatically and give you syntax highlighting, autocomplete, and a
   "Run" button.

## Checklist before moving on

- [ ] `python3 --version` prints `3.10` or higher.
- [ ] You can open a terminal and navigate into this course's folder
      (`cd path/to/python-for-beginner`).
- [ ] You created and ran a one-line `test.py` successfully.
- [ ] Your editor is open and ready.

Once all four are checked, move on to
[01 — Hello, World & Comments](../01-hello-world/README.md).
