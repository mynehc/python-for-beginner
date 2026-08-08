# Python for Beginners

A complete, self-paced Python course for someone who has **never written a
line of code before**. No prior programming experience assumed — every
module starts from "what is this and why would I use it" and builds up with
small, runnable examples.

This course assumes zero prior programming experience — if you already
know how to program in another language, most of the early modules will
feel slow; skim ahead to whichever module covers the first Python-specific
idea you don't already know.

## How to use this

Each module is a folder: `NN-topic-name/`

- **`README.md`** — the concept explained in plain language, small examples
  you can type and run yourself, a "common beginner mistakes" section, and
  **one exercise** at the end.
- **`exercise.py`** — a stub file with function signatures already written
  and a `# TODO: implement` + `raise NotImplementedError` where your code
  goes. Fill in each function, then run the file:

  ```bash
  python3 python-for-beginner/02-variables-and-data-types/exercise.py
  ```

  The bottom of the file checks your work automatically with `assert`
  statements and prints `All checks passed!` when everything is correct. If
  something is wrong, Python will show you an `AssertionError` pointing at
  the exact line that failed — that's normal and part of the process, not a
  sign you broke something.
- **`solutions/NN-topic-name/solution.py`** — a fully worked reference
  solution. Resist opening it until your own `exercise.py` prints
  `All checks passed!`, or until you've genuinely tried for a while and are
  stuck. Comparing your working answer to the reference afterward is where a
  lot of the learning happens — do it every time, even when you got it
  right, since there's often a cleaner way.

Work through the modules **in order, top to bottom**. This course is
cumulative — module 08 (Lists) assumes you're comfortable with everything in
modules 01–07, and so on all the way through. Don't skip around on a first
pass.

## Setup

Start with [00-setup](00-setup/README.md) — installing Python, using a
terminal, and running your first file. No exercise there, just getting your
machine ready.

## Roadmap

### Part 1 — Absolute basics
1. [Hello, World & Comments](01-hello-world/README.md)
2. [Variables & Data Types](02-variables-and-data-types/README.md)
3. [Numbers & Operators](03-numbers-and-operators/README.md)
4. [Strings](04-strings/README.md)
5. [Input, Output & Type Conversion](05-input-output-and-conversion/README.md)
6. [Booleans & Comparisons](06-booleans-and-comparisons/README.md)
7. [Conditionals (if / elif / else)](07-conditionals/README.md)

### Part 2 — Collections & control flow
8. [Lists](08-lists/README.md)
9. [Loops (for / while)](09-loops/README.md)
10. [Tuples](10-tuples/README.md)
11. [Dictionaries](11-dictionaries/README.md)
12. [Sets](12-sets/README.md)

### Part 3 — Writing reusable code
13. [Functions](13-functions/README.md)
14. [Scope & Recursion](14-scope-and-recursion/README.md)
15. [Comprehensions](15-comprehensions/README.md)
16. [Error Handling (try / except)](16-error-handling/README.md)
17. [Modules & Packages](17-modules-and-packages/README.md)
18. [File I/O](18-file-io/README.md)

### Part 4 — Object-oriented programming
19. [OOP Basics (classes & objects)](19-oop-basics/README.md)
20. [Inheritance & Dunder Methods](20-oop-inheritance/README.md)

### Part 5 — Thinking like a Pythonista
21. [Lambda & Functional Tools](21-lambda-and-functional-tools/README.md)
22. [Iterators & Generators](22-iterators-and-generators/README.md)
23. [Decorators](23-decorators/README.md)
24. [Standard Library Tour](24-stdlib-tour/README.md)
25. [Regular Expressions](25-regex/README.md)
26. [Virtual Environments & pip](26-virtual-envs-and-pip/README.md)
27. [Testing Basics](27-testing-basics/README.md)

### Part 6 — Capstone projects (fully terminal-based)
28. [Project: Number Guessing Game](28-project-number-guessing-game/README.md)
29. [Project: Contact Book](29-project-contact-book/README.md)
30. [Project: Expense Tracker](30-project-expense-tracker/README.md)

## Progress checklist

Copy this into your own notes and check things off as you go, or just
track it mentally.

- [ ] 00 Setup
- [ ] 01 Hello, World & Comments
- [ ] 02 Variables & Data Types
- [ ] 03 Numbers & Operators
- [ ] 04 Strings
- [ ] 05 Input, Output & Type Conversion
- [ ] 06 Booleans & Comparisons
- [ ] 07 Conditionals
- [ ] 08 Lists
- [ ] 09 Loops
- [ ] 10 Tuples
- [ ] 11 Dictionaries
- [ ] 12 Sets
- [ ] 13 Functions
- [ ] 14 Scope & Recursion
- [ ] 15 Comprehensions
- [ ] 16 Error Handling
- [ ] 17 Modules & Packages
- [ ] 18 File I/O
- [ ] 19 OOP Basics
- [ ] 20 Inheritance & Dunder Methods
- [ ] 21 Lambda & Functional Tools
- [ ] 22 Iterators & Generators
- [ ] 23 Decorators
- [ ] 24 Standard Library Tour
- [ ] 25 Regular Expressions
- [ ] 26 Virtual Environments & pip
- [ ] 27 Testing Basics
- [ ] 28 Project: Number Guessing Game
- [ ] 29 Project: Contact Book
- [ ] 30 Project: Expense Tracker

## Ground rules

- **Type the examples out by hand** instead of copy-pasting, at least the
  first time through a module. Typing code yourself is how the syntax
  becomes muscle memory — copy-pasting skips that step.
- **Run everything.** Reading code is not the same as running it. If a
  README shows a code snippet, open a terminal and actually try it before
  moving on.
- **Don't look at `solutions/`** until your own `exercise.py` prints
  `All checks passed!`, or you've been stuck for 15+ minutes and want a
  hint. Struggling a bit is normal and expected — that's the exercise
  working, not you failing it.
- **Errors are normal.** You will see `SyntaxError`, `TypeError`,
  `NameError`, and `IndexError` constantly while learning — every
  programmer does, forever, not just beginners. Read the last line of the
  error message first; it usually tells you exactly what's wrong and on
  which line.
- Use the official docs at [docs.python.org](https://docs.python.org/3/) as
  a reference whenever a module mentions a function you want to know more
  about — looking things up is a core programming skill, not cheating.
