# Python Practice

A personal Python learning repo. The main thing here is
**[python-for-beginner](python-for-beginner/README.md)** — a complete,
self-paced Python course for someone with **no prior programming
experience at all**, going from "hello world" through every core
language concept to three complete, terminal-based capstone projects.

## Repo structure

```
.
├── python-for-beginner/   # the course — start here (see its own README)
├── requirements.txt        # packages needed for module 27 (pytest)
├── SETUP.md                 # how to set up a virtual environment for this repo
└── .gitignore
```

## Getting started

1. **Install Python 3.10+** if you don't already have it.
2. **Set up a virtual environment** — see [SETUP.md](SETUP.md) for a
   full walkthrough (what it is, why it matters, step-by-step, and
   troubleshooting). Short version:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate     # Windows: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. **Start the course**: open
   [python-for-beginner/README.md](python-for-beginner/README.md) and
   follow it from [00-setup](python-for-beginner/00-setup/README.md)
   onward, in order.

Most of the course (modules 00–25, 28–30) needs nothing beyond a plain
Python install — no venv, no installed packages. The venv is only
required for module [27](python-for-beginner/27-testing-basics/README.md),
which uses `pytest`.

## Forking this repo & tracking your own progress

The course exercises are meant to be edited in place — you'll be filling
in `exercise.py` stubs as you go. The best way to keep your own copy and
build up a record of your progress is to **fork** this repo and commit
your work as you complete each module.

### 1. Fork it on GitHub

Go to **[github.com/BUMBAIYA/python-for-beginner](https://github.com/BUMBAIYA/python-for-beginner)**
and click **Fork** (top-right of the page). This creates your own
independent copy of the whole repo under your GitHub account —
`github.com/<your-username>/python-for-beginner` — that you can edit and
push to freely, without touching the original.

### 2. Clone your fork locally

```bash
git clone https://github.com/<your-username>/python-for-beginner.git
cd python-for-beginner
```

(Replace `<your-username>` with your actual GitHub username.)

### 3. (Optional) Track the original, so you can pull future updates

If you want to be able to pull in changes made to the original course
later (new modules, fixes, etc.), add it as a second remote called
`upstream`:

```bash
git remote add upstream https://github.com/BUMBAIYA/python-for-beginner.git
git remote -v   # confirm: origin = your fork, upstream = the original
```

Whenever you want to pull in updates:

```bash
git fetch upstream
git merge upstream/main
```

### 4. Set up your environment

Follow [SETUP.md](SETUP.md) to create your virtual environment and
install dependencies.

### 5. Commit as you complete each module

This is the actual "tracking your progress" part — a small commit after
each finished module turns `git log` into a timeline of what you've
learned and when, and lets you look back at how you solved something the
first time.

```bash
git add python-for-beginner/02-variables-and-data-types/exercise.py
git commit -m "Complete 02 - Variables & Data Types"
```

A few habits worth building:

- **Commit per module, not all at once.** One commit per finished
  exercise gives you a far more useful history than a single giant
  commit at the end.
- **Name commits after the module**, e.g. `"Complete 09 - Loops"` — makes
  `git log --oneline` read as a readable table of contents of your
  progress.
- **Check before you commit**: `git status` shows which files changed;
  `git diff` shows the exact lines you changed, so you're never
  committing something by accident.
- **Push regularly** so your progress is backed up on GitHub, not just
  sitting on your machine: `git push` (after the first `git push -u
  origin main`, plain `git push` is enough).

### 6. Git commands you'll use constantly

| Command | What it does |
|---|---|
| `git status` | Shows which files you've changed, added, or haven't tracked yet |
| `git diff` | Shows the exact line-by-line changes you've made, before committing |
| `git add <file>` | Stages a file's changes to go into the next commit |
| `git commit -m "message"` | Saves a snapshot of the staged changes with a description |
| `git log --oneline` | Shows your commit history, one line per commit — your progress timeline |
| `git push` | Uploads your commits to your fork on GitHub |

You don't need to be a git expert to use this — `status` → `add` →
`commit` → `push`, repeated after every module, is the entire workflow.

## What's in the course

- **Modules 01–27**: one concept per folder, each with a `README.md`
  (explained from scratch, with runnable examples), a self-checking
  `exercise.py`, and a reference solution.
- **Modules 28–30**: three open-ended, fully terminal-based capstone
  projects — a number guessing game, a JSON-backed contact book, and an
  expense tracker with spending summaries.

See the [course README](python-for-beginner/README.md) for the full
roadmap and progress checklist.
