# 03 · Strings

Exercises: [`exercises/ex03_strings.py`](exercises/ex03_strings.py)

There is no `char` type. A character is a string of length 1. Strings are immutable, like Java's `String`.

## Reading and slicing

Everything from lists works except mutation:

```python
s[0], s[-1], s[1:4], s[::-1], len(s)
for c in s: ...
for i, c in enumerate(s): ...
s[0] = "x"            # TypeError: strings are immutable
```

To edit characters, convert to a list, edit, join back:

```python
chars = list(s)
chars[0], chars[-1] = chars[-1], chars[0]
s = "".join(chars)
```

## Building strings

```python
parts = []
for ...:
    parts.append(piece)
result = "".join(parts)        # O(total length)
```

`result += piece` in a loop can be O(n²) because each `+=` may copy the whole string. CPython sometimes optimizes it, but don't rely on that in an interview; say "I'll collect pieces and join."

`", ".join(words)` puts the separator between items. Join only accepts strings: `"".join(map(str, nums))`.

## Character math

```python
ord("a")                   # 97
chr(98)                    # "b"
ord(c) - ord("a")          # 0..25, index into a 26-slot count array
counts = [0] * 26
for c in s:
    counts[ord(c) - ord("a")] += 1
```

## Methods you'll actually use

| Method | Does |
|---|---|
| `c.isalnum()`, `c.isalpha()`, `c.isdigit()`, `c.isspace()` | character tests |
| `s.lower()`, `s.upper()` | new string |
| `s.split()` | split on any run of whitespace, drops empty pieces |
| `s.split(",")` | split on exact separator, **keeps** empty pieces |
| `s.strip()` | trim whitespace both ends |
| `s.startswith(p)`, `s.endswith(p)` | prefix / suffix test |
| `s.find(t)` | index or **-1** |
| `s.index(t)` | index or **raises ValueError** |
| `s.count(t)`, `s.replace(a, b)` | |
| `str(42)`, `int("42")` | convert |

`"  a  b ".split()` gives `['a', 'b']`. `"  a  b ".split(" ")` gives `['', '', 'a', '', 'b', '']`. That difference decides Reverse Words in a String.

## Comparisons and sorting

Strings compare lexicographically with `<`, `==`, and so on. `==` compares contents (no `.equals()`).

`sorted(s)` returns a **list** of characters, so an anagram key is `"".join(sorted(s))` or `tuple(sorted(s))`.

## Predict the output

1. `print("abc" * 2, "abc"[::-1], "abc"[5:])`
2. `print(" hi  there ".split(" "))`
3. `print(sorted("cab"))`
4. `print("Hello".find("z"), "a,b,,c".split(","))`
5. `print(chr(ord("a") + 25), "Z" < "a")`

<details><summary>Answers</summary>

1. `abcabc cba` and an empty string (out-of-range slices don't raise)
2. `['', 'hi', '', 'there', '']`
3. `['a', 'b', 'c']`
4. `-1 ['a', 'b', '', 'c']`
5. `z True` (uppercase letters have smaller codes than lowercase)
</details>
