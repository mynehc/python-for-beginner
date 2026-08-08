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

## What's in the course

- **Modules 01–27**: one concept per folder, each with a `README.md`
  (explained from scratch, with runnable examples), a self-checking
  `exercise.py`, and a reference solution.
- **Modules 28–30**: three open-ended, fully terminal-based capstone
  projects — a number guessing game, a JSON-backed contact book, and an
  expense tracker with spending summaries.

See the [course README](python-for-beginner/README.md) for the full
roadmap and progress checklist.
