# 26 — Virtual Environments & pip

No `exercise.py` self-check for this one — it's tooling, best learned by
actually doing it once. Treat the "Do this now" section as the exercise;
there's no automated grader, but each step tells you what to check for
yourself.

## Concept

Every module before this one used only the **standard library** —
nothing to install, `import` and go. Real projects usually also need
**third-party packages**: code other people published that isn't part of
Python itself (a library to talk to a database, format dates fancily,
build a web app, and so on).

### `pip` — Python's package installer

```bash
pip install requests
```

This downloads the `requests` package (a popular one for making HTTP
web requests) and installs it so `import requests` works. `pip` comes
bundled with Python — no separate install needed.

### The problem: global installs step on each other

By default, `pip install` puts packages into your **one, shared, global**
Python installation. If Project A needs `requests` version 2.0 and
Project B needs version 3.0, installing globally means only one can be
satisfied at a time — they'd fight over the same installation.

### The fix: virtual environments

A **virtual environment** ("venv") is an isolated, self-contained Python
setup for a single project — its own installed packages, separate from
your system Python and from every other project's venv. This is close to
what `node_modules` gives you automatically per-project in JavaScript,
except Python doesn't do it automatically — you create and activate a
venv yourself, every project, every time.

```bash
python3 -m venv .venv          # creates a new venv in a folder called .venv
source .venv/bin/activate      # activate it (macOS/Linux)
# .venv\Scripts\activate       # activate it (Windows)
```

Once activated, your terminal prompt usually shows `(.venv)`, and from
that point on, `pip install` and `python3` both operate **inside** that
isolated environment, not your system-wide Python. `deactivate` turns it
off.

**This course's exercises never needed a venv** because they only used
the standard library. The moment a project needs a package that isn't
built in, creating and activating a venv first is the correct first
step, before running `pip install` anything.

### `requirements.txt` — recording what a project needs

```bash
pip freeze > requirements.txt     # writes every installed package + version to a file
pip install -r requirements.txt   # installs everything listed in that file
```

This is how a project shares its exact dependency list with anyone else
(or any other machine) running it — commit `requirements.txt` to your
project, don't commit the `.venv` folder itself (it's large, and
regenerable from `requirements.txt`).

## Do this now

1. In a **new scratch folder** (not this course folder — somewhere
   throwaway), create and activate a venv:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Confirm it worked: `which python3` should now point **inside** that
   `.venv` folder, not your system Python.

2. Install something small and harmless:

   ```bash
   pip install requests
   ```

3. Confirm it's importable:

   ```bash
   python3 -c "import requests; print(requests.__version__)"
   ```

4. Freeze your dependencies to a file, and look at what it wrote:

   ```bash
   pip freeze > requirements.txt
   cat requirements.txt
   ```

5. Deactivate, and confirm `requests` is no longer importable outside the
   venv:

   ```bash
   deactivate
   python3 -c "import requests"   # should fail now (unless you also have it installed globally)
   ```

6. Delete the scratch folder — you're done with it.

## Common beginner mistakes

- **`pip install`ing without an active venv.** Installs into your global
  Python, defeating the whole point, and on some modern systems raises
  an `externally-managed-environment` error specifically to stop you.
  Always activate a venv first.
- **Committing `.venv/` to version control.** It's large,
  machine-specific, and fully regenerable from `requirements.txt` — add
  it to `.gitignore` instead (this course's own `.gitignore` already
  does this).
- **Forgetting to activate the venv in a new terminal tab.** Activation
  is per-terminal-session — opening a fresh terminal window/tab means
  you need to `source .venv/bin/activate` again.

Once you've done this by hand in a scratch folder, set up the **real**
venv for this repo the same way — see
[`../../SETUP.md`](../../SETUP.md) for the exact commands and
troubleshooting, since it's what module
[27 — Testing Basics](../27-testing-basics/README.md) needs to run
(a venv with `pytest` installed in it).
