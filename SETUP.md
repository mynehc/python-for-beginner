# Setup Guide — Virtual Environments (venv)

This is the practical, "do this to get this repo running" guide. If you
want the conceptual explanation as part of the course curriculum, that's
[python-for-beginner/26-virtual-envs-and-pip](python-for-beginner/26-virtual-envs-and-pip/README.md)
— read this one first, it's shorter and gets you unblocked immediately.

You only need this once per machine, and then once per fresh clone of
this repo.

## What is a virtual environment?

Every Python installation on your machine has one shared place where
`pip install`ed packages live — call it the "global" Python. A **virtual
environment** ("venv") is a separate, private copy of that install
location, sitting in a folder (conventionally called `.venv`) inside a
single project. When it's active, `pip install` and `python3` both
operate on that private folder instead of your global Python.

Think of it like this: your global Python is a shared kitchen everyone
in the building uses. A venv is your own kitchen, just for this one
project — nothing you do in it affects anyone else's, and nothing they
do affects you.

## Why bother? (the actual reasons, not just "best practice")

- **Different projects need different package versions.** Project A
  might need `requests` version 2, Project B version 3. Installed
  globally, only one can win. Installed in separate venvs, both are
  happy at once.
- **Modern systems often *refuse* global installs anyway.** On a recent
  macOS/Linux system, running `pip install` outside a venv frequently
  fails with `error: externally-managed-environment` — Python itself is
  now built to push you toward venvs, not just convention pushing you
  there.
- **Reproducibility.** `requirements.txt` (in this repo's root) lists
  exactly what's needed. Anyone — including future you, on a different
  machine — runs one command and gets an identical set of packages.
  Without a venv, "works on my machine" installs get muddled with
  whatever else happens to be globally installed.
- **A clean way to start over.** If something in your Python environment
  gets into a weird state, you delete the `.venv` folder and rebuild it
  from `requirements.txt` in under a minute — no risk to your system
  Python, no risk to any other project.
- **This repo specifically needs it** for module
  [27-testing-basics](python-for-beginner/27-testing-basics/README.md),
  which uses `pytest` — a package that isn't part of the Python standard
  library and needs installing.

## Step-by-step setup

### 1. Check your Python version

```bash
python3 --version
```

You need **3.10 or newer**. If you're missing Python entirely, or on an
old version, see
[python-for-beginner/00-setup](python-for-beginner/00-setup/README.md#1-install-python)
first.

### 2. Create the venv

From the **root of this repo** (the folder this file is in):

```bash
python3 -m venv .venv
```

This creates a `.venv/` folder containing a private copy of Python and
an empty package install location. It takes a few seconds and only needs
doing once — you don't recreate it every time you work on the project,
only if it gets deleted or corrupted.

### 3. Activate it

Activation puts the venv's `python3` and `pip` first in your terminal's
search path, for the current terminal session only.

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

You'll know it worked because your terminal prompt now shows `(.venv)`
at the start of the line. Double check with:

```bash
which python3   # macOS/Linux — should print a path INSIDE this repo's .venv folder
where python3   # Windows
```

If that path does **not** point inside `.venv`, activation didn't take —
re-run the activate command. The commands above assume you're running
them from this repo's root folder (so `.venv/bin/activate` resolves
correctly); if you're elsewhere, use the full path to it instead.

### 4. Install this repo's dependencies

```bash
pip install -r requirements.txt
```

This reads [`requirements.txt`](requirements.txt) and installs exactly
what's listed (`pytest`, for module 27) into the active venv. You'll see
download/install progress, then a prompt back.

### 5. Verify it worked

```bash
python3 -m pytest --version
```

Should print a pytest version number. If instead you get
`No module named pytest`, either the venv isn't activated (redo step 3)
or step 4 didn't complete successfully (scroll up for errors and re-run
it).

### 6. Deactivate when you're done

```bash
deactivate
```

Returns your terminal to using the global Python. Doesn't delete
anything — just leaves the venv folder alone until you activate it
again.

## The everyday workflow, once this is done

- **Every new terminal window/tab**, if you're going to run anything
  that needs `pytest` (module 27) or any future third-party package:
  `source .venv/bin/activate` again first. Activation is per-terminal-
  session, not permanent — this trips up beginners constantly, so if a
  command that worked yesterday suddenly says `ModuleNotFoundError`,
  check whether you forgot to activate in this new terminal.
- **Everything else in this course** (modules 00–25, 28–30) uses only
  the Python standard library — no venv or install needed at all. You
  only need an active venv for module 27 and anything using `pytest`.
- **Adding a new package later**, if you ever extend this repo:
  `pip install <package>` while the venv is active, then update
  `requirements.txt` to match (either by hand, or `pip freeze >
  requirements.txt` to capture everything currently installed).

## Editor setup (VS Code)

1. Install the **"Python" extension** (by Microsoft).
2. Open this repo's folder in VS Code.
3. Open the interpreter picker: bottom-right corner of the window (it
   shows the currently selected Python), or Cmd/Ctrl+Shift+P →
   "Python: Select Interpreter".
4. Choose the one whose path includes `.venv` — VS Code usually detects
   and labels it `('.venv': venv)` automatically once the folder exists.
5. Now the built-in terminal, the "Run" button, and the testing panel
   all use the venv automatically — no manual `activate` needed inside
   VS Code's own integrated terminal (it does it for you), though you
   still need to activate manually in any **separate**, non-VS-Code
   terminal window.

## Troubleshooting

| Problem | Fix |
|---|---|
| `python3: command not found` | Python isn't installed, or not on your PATH — see [00-setup](python-for-beginner/00-setup/README.md). |
| `error: externally-managed-environment` on `pip install` | You're not inside an activated venv — this error exists specifically to stop global installs. Activate first (step 3). |
| Prompt doesn't show `(.venv)` after activating | You ran the activate command from the wrong folder, or used the wrong script for your OS/shell (see step 3's three variants). |
| `ModuleNotFoundError: No module named 'pytest'` | Either the venv isn't activated in *this* terminal, or `pip install -r requirements.txt` was never run (or failed) — redo steps 3–4. |
| PowerShell says running scripts is disabled | Run PowerShell as Administrator once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then retry activation. |
| VS Code still uses the wrong interpreter after selecting `.venv` | Reload the window (Cmd/Ctrl+Shift+P → "Developer: Reload Window") after selecting the interpreter. |
| Things feel broken / want a clean slate | Delete the folder and start over — it's fully disposable: `rm -rf .venv` (macOS/Linux) or delete the `.venv` folder in Explorer (Windows), then repeat steps 2–4. |

## FAQ

**Do I really need to activate every single terminal session?**
Yes. It's not remembered globally — that's the entire point, it's
scoped to keep this project's setup from leaking into (or being leaked
into by) anything else on your machine.

**Can I just commit `.venv/` so I never have to think about this?**
No — it's in [`.gitignore`](.gitignore) on purpose. It's large (hundreds
of megabytes once packages are installed), tied to your specific
operating system, and instantly regenerable from `requirements.txt`.
Committing it would bloat the repo for zero benefit.

**What if I'm not using VS Code?**
Everything here works identically from a plain terminal, regardless of
editor — the venv is just a folder and an activation script, nothing
VS-Code-specific about it.

**Is a venv the same as installing Python fresh?**
No — it reuses your already-installed Python interpreter, it just gives
it a private, empty package folder to install into. Nothing about your
system Python installation changes.
