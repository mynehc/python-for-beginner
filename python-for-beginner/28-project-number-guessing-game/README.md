# 28 — Project: Number Guessing Game

No `exercise.py` stub, no `assert`-based grader — this is an open-ended
build using everything from modules 01–16. Build it, then check it
against the requirements yourself (that self-verification is part of the
exercise, same as it would be shipping a real feature). This is the
simplest of the three capstone projects — a good first "put it all
together" build before the two bigger ones.

## What to build

A terminal game: the computer picks a random number in a range, the
player guesses repeatedly, and the game says "too high" / "too low"
until they get it, then offers to play again.

```
Guess the number between 1 and 100!
Your guess: 50
Too low! Try again.
Your guess: 75
Too high! Try again.
Your guess: 62
🎉 Correct! You got it in 3 guesses.
Play again? (yes/no): no
Thanks for playing!
```

## Requirements

- Use `random.randint(1, 100)` (module 17) to pick the secret number at
  the start of each round.
- Use a `while` loop (module 09) that keeps asking for guesses until the
  player gets it right.
- Use `input()` and convert it to an `int` (module 05).
- Give feedback each guess: too high, too low, or correct.
- Count and report the number of guesses it took once they win.
- Handle bad input gracefully: if the player types something that isn't
  a number, catch the resulting error (module 16) and ask again instead
  of crashing.
- After a round ends, ask "Play again? (yes/no)" and either start a new
  round (new random number) or exit the program cleanly, using an outer
  `while True:` loop with a `break`.

## Stretch goals (optional)

- Track and display the player's **best score** (fewest guesses) across
  rounds within a single run — a plain variable is enough for this,
  no file needed.
- Persist the best score to a JSON file (module 18/24) so it survives
  between runs of the program.
- Add a difficulty menu at the start: "easy" (range 1–50, unlimited
  guesses), "medium" (1–100, 10 guesses max), "hard" (1–500, 7 guesses
  max) — use a dict or `if`/`elif` to configure the round based on the
  choice.
- Give a "warmer/colder" hint in addition to higher/lower, based on how
  close the previous guess was.
- Structure the game logic into functions (`play_round()`,
  `get_valid_guess()`, etc. — module 13) instead of one long block, so
  `main()` reads like a summary of the game's flow.

Suggested file layout inside this folder:

```
28-project-number-guessing-game/
  game.py         # entry point — run with: python3 game.py
  high_score.json # created at runtime if you build the stretch goal, gitignore-worthy
```
