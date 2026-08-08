# 30 — Project: Expense Tracker

No `exercise.py` stub, no `assert`-based grader — this is the final,
most complete open-ended build, using everything from modules 01–27.
Build it, then check it against the requirements yourself.

## What to build

A terminal expense tracker, persisted to a JSON file, with an
interactive menu loop, that can summarize spending by category and by
month:

```
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. View summary by category
4. View summary by month
5. Delete expense
6. Quit
Choose an option: 1

Amount: 42.50
Category: Groceries
Date (YYYY-MM-DD, blank for today): 
Description: Weekly shop
Expense added!

Choose an option: 3

--- Summary by category ---
Groceries   $42.50
Transport   $15.00
------------------
Total       $57.50

Choose an option: 6
Goodbye!
```

## Requirements

- Represent each expense as a `@dataclass`-**style** plain class (module
  19 — a regular `class` with `__init__` is fine; `@dataclass` itself is
  beyond this course but the shape is the same): `amount: float`,
  `category: str`, `date: str` (`"YYYY-MM-DD"`), `description: str`.
- Persist expenses as JSON (modules 18/24) in a file (e.g.
  `expenses.json`) — load on startup, save after any add/delete.
- **Add**: prompt for amount, category, date, and description. If the
  date is left blank, default to today (`datetime.date.today()`, module
  24). Validate that amount converts to a positive number — reprompt on
  bad input (module 16) instead of crashing.
- **View all**: print every expense, numbered, most recent first.
- **Summary by category**: group all expenses by `category` and print
  the total per category, plus a grand total. `collections.Counter` or a
  plain dict with `.get(key, 0) +=` (module 11/24) both work well here.
- **Summary by month**: same idea, grouped by the `YYYY-MM` prefix of
  each expense's `date` (string slicing, module 04, is enough — no need
  for full date parsing to group by month).
- **Delete**: given an expense's number from the "view all" listing,
  remove it; save.
- Handle the "no expenses yet" case gracefully everywhere (empty view,
  empty summaries) — a clear message, not a crash or a blank screen with
  no explanation.
- Handle bad menu input the same way as the other capstones — reprompt,
  don't crash.

## Stretch goals (optional)

- Add a `--json` style flag or menu option to print a summary as raw
  JSON instead of a formatted table (useful if another program were ever
  going to consume this data).
- Add a monthly **budget** per category (a small config dict or a second
  JSON file) and flag categories that are over budget in the summary
  view.
- Sort the category summary from highest to lowest spend
  (`sorted(..., key=..., reverse=True)`, module 21).
- Export a category or month's expenses to a CSV file using the
  standard library's `csv` module (not covered in this course's modules
  — a good chance to practice reading unfamiliar docs, exactly the skill
  called out in this course's [top-level README](../README.md)).
- Write `pytest` tests (module 27) for the aggregation logic
  (category/month summaries) using a handful of fixture expenses,
  separate from the menu-loop code.

Suggested file layout inside this folder:

```
30-project-expense-tracker/
  tracker.py       # entry point — run with: python3 tracker.py
  expense.py       # the Expense class + summary functions
  expenses.json    # created at runtime, gitignore-worthy
```

## You've reached the end

If you've built all three capstones, you've gone from "never written a
line of code" through every core Python concept to shipping small but
complete, persisted, interactive command-line programs — that's a real
foundation. From here, natural next steps are digging into more advanced
topics (context managers, advanced exceptions, concurrency, async,
packaging) if you want to keep going deeper into Python specifically, or
picking a small idea of your own and building it, which is genuinely the
fastest way to keep improving from this point on.
