# 09 — Loops (for / while)

## Concept

Loops repeat a block of code, so you don't hand-write the same operation
over and over. Python has two: `for` (repeat once per item in a
collection) and `while` (repeat as long as a condition stays `True`).

### `for` — loop over a collection

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

```
apple
banana
cherry
```

Read `for fruit in fruits:` as "for each item in `fruits`, call it
`fruit`, and run the indented block." `fruit` is a new variable, created
fresh each pass through the loop — you don't declare it beforehand.

`for` works on any **iterable** — lists, strings (loops over characters),
tuples, dicts, and more (there's a formal definition in module
[22](../22-iterators-and-generators/README.md); for now, "things you can
put after `in`" is enough).

```python
for letter in "abc":
    print(letter)   # a, b, c on separate lines
```

### `range()` — looping a specific number of times

`range(n)` produces the numbers `0, 1, 2, ..., n-1` (n numbers total,
**not including** `n` — same "stop is exclusive" rule as slicing):

```python
for i in range(5):
    print(i)   # 0 1 2 3 4
```

`range(start, stop)` and `range(start, stop, step)` work too:

```python
for i in range(2, 10, 2):
    print(i)   # 2 4 6 8
```

### `enumerate()` — index and value together

When you need both the position and the item:

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

### `while` — loop until a condition is False

```python
count = 0
while count < 3:
    print(count)
    count += 1   # without this, the loop never ends!
```

Use `while` when you don't know in advance how many times you'll loop
(e.g. "keep asking the user until they type something valid") — that's
also exactly the shape the capstone projects at the end of this course
use for their main menu loop. Use `for` when you're processing a known
collection or a known count.

### `break` and `continue`

- `break` — exit the loop immediately, skipping anything left in it.
- `continue` — skip the rest of *this* pass and go to the next one.

```python
for n in range(10):
    if n == 5:
        break        # stops the loop entirely at 5
    print(n)         # 0 1 2 3 4

for n in range(10):
    if n % 2 == 0:
        continue     # skip even numbers, keep looping
    print(n)         # 1 3 5 7 9
```

### Infinite loops — a real risk with `while`

```python
while True:
    print("forever")   # never stops on its own — needs a break inside
```

`while True:` combined with an internal `break` is a common, intentional
pattern (again — this is exactly the shape of the "keep looping until the
user chooses quit" menu in the capstone projects). Writing `while` with a
condition that never becomes `False` **by accident** is a common bug — if
your program hangs and never prints anything, check for a missing
`+= 1` or similar update inside the loop.

## Common beginner mistakes

- **Forgetting to update the loop variable in a `while` loop** — causes
  an infinite loop. If your program freezes, Ctrl+C in the terminal stops
  it.
- **Off-by-one with `range()`.** `range(5)` gives `0..4`, not `1..5`. If
  you want 1 through 5 inclusive, use `range(1, 6)`.
- **Modifying a list while looping over it with `for`.** Removing items
  from a list during a `for item in my_list:` loop skips items
  unpredictably, because the indices shift underneath the loop. Loop over
  a copy (`for item in my_list.copy():`) if you need to remove things, or
  build a new list instead.
- **Using `break` when you meant `continue`, or vice versa.** `break`
  stops the whole loop; `continue` just skips to the next round. Easy to
  swap by accident when tired.

## Exercise

Open [`exercise.py`](exercise.py) and implement:

1. `sum_of_range(n)` — return the sum of all integers from `1` to `n`
   inclusive, using a `for` loop over `range()` (not the `sum()`
   shortcut, not the math formula — practice the loop).
2. `count_vowels(word)` — return how many characters in `word` are one
   of `a, e, i, o, u` (lowercase only), looping over the characters.
3. `first_negative(numbers)` — return the first negative number in
   `numbers`, or `None` if there isn't one. Use `break` once you find it.
4. `countdown(n)` — return a list counting down from `n` to `1`
   (inclusive), e.g. `countdown(3) == [3, 2, 1]`, built with a `while`
   loop.
5. `skip_multiples_of_three(n)` — return a list of every number from `1`
   to `n` inclusive, **except** multiples of 3. Use `continue` to skip
   them.

Run it to check yourself:

```bash
python3 python-for-beginner/09-loops/exercise.py
```
