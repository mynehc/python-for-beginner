# 29 — Project: Contact Book

No `exercise.py` stub, no `assert`-based grader — this is an open-ended
build using everything from modules 01–20 (classes included). Build it,
then check it against the requirements yourself.

## What to build

A terminal contact book, persisted to a JSON file, with an interactive
menu loop:

```
=== Contact Book ===
1. Add contact
2. View all contacts
3. Search contacts
4. Update contact
5. Delete contact
6. Quit
Choose an option: 1

Name: Ava Chen
Phone: 555-0142
Email: ava@example.com
Contact added!

Choose an option: 2

1. Ava Chen — 555-0142 — ava@example.com

Choose an option: 6
Goodbye!
```

## Requirements

- Represent each contact as a small class (module 19), e.g.:
  ```python
  class Contact:
      def __init__(self, name, phone, email):
          self.name = name
          self.phone = phone
          self.email = email
  ```
- Store contacts persisted as JSON (module 18/24) in a file (e.g.
  `contacts.json`) — load on startup, save after every change (add,
  update, delete). Since `json` can't serialize a `Contact` object
  directly, you'll need to convert to/from plain dicts when
  saving/loading (`contact.__dict__` is a quick way to get a dict from
  an object; building a `Contact(**data)` from a loaded dict is the
  reverse).
- Build the interactive loop with `while True:` and a numbered menu, like
  the sketch above — `break` out on "Quit."
- **Add**: prompt for name, phone, email; append a new contact; save.
- **View all**: print every contact, numbered.
- **Search**: prompt for a search term; print every contact whose name
  contains it (case-insensitive — `.lower()` both sides before
  comparing).
- **Update**: given a contact's number from the "view all" listing, let
  the user change its phone and/or email.
- **Delete**: given a contact's number, remove it; save.
- Handle bad menu input (non-numeric, or a number with no matching
  option) without crashing — reprompt instead (module 16).
- Handle "no contacts yet" gracefully everywhere it could come up (empty
  view, search with no results, update/delete with nothing to pick from)
  — a clear message, not a crash or silent nothing.

## Stretch goals (optional)

- Sort contacts alphabetically by name in the "view all" listing.
- Validate phone numbers and emails with a regex (module 25) before
  accepting them, reprompting on an invalid shape.
- Add a "duplicate name" check on add, warning the user (but still
  letting them proceed if they confirm) instead of silently allowing
  exact duplicates.
- Support exporting all contacts to a plain-text file, one per line.
- Write a few `pytest` tests (module 27) for the contact-storage logic
  (load/save/search), separate from the menu-loop code — this works best
  if you structure the storage logic as functions/methods that don't
  themselves call `input()`, so they're testable without simulating
  keyboard input.

Suggested file layout inside this folder:

```
29-project-contact-book/
  contact_book.py   # entry point — run with: python3 contact_book.py
  contact.py        # the Contact class
  contacts.json     # created at runtime, gitignore-worthy
```
