# Python for LeetCode: a two-day primer

The Python you need for Top Interview 150, and nothing else. Written for someone who already knows Java: it focuses on what's different and what bites.

**Hard stop: LeetCode starts no later than Friday, Oct 9, 2026.** Anything not covered here gets learned on real problems.

## Schedule

| | Lessons | Time |
|---|---|---|
| **Day 1** | [01 Basics](01-basics.md) · [02 Lists](02-lists.md) · [03 Strings](03-strings.md) · [04 Dicts and sets](04-dicts-sets.md) | ~3–4 h |
| **Day 2** | [05 deque, heapq, bisect](05-deque-heap-bisect.md) · [06 Functions, recursion, classes](06-functions-recursion-classes.md) · [07 Built-ins, math, bits](07-builtins-math-bits.md) · [08 Complexity and gotchas](08-complexity-gotchas.md) | ~3–4 h |
| **Exit test** | 10 rapid-fire questions from Claude, mixed across all eight lessons | 20 min |

## How to do each lesson

1. Read the lesson. Do the **Predict the output** section *before* opening the answers. Write your guesses down.
2. Open the matching file in [`exercises/`](exercises/), replace each `raise NotImplementedError`, and run it on your computer:
   ```
   cd python-primer/exercises
   python3 ex01_basics.py
   ```
   Each test prints `ok`, `FAIL`, or `TODO`. Get them all to `ok` without looking anything up beyond the lesson.
3. Push your work (or paste it to Claude). Claude reviews it for idiomatic Python, not just passing tests, then asks you a few questions about the lesson.
4. Tick the box below.

Exercise 08 is different: every function is already written and broken. Find the bug, fix it with the smallest change, and comment what was wrong.

## Checklist

- [ ] 01 Basics
- [ ] 02 Lists
- [ ] 03 Strings
- [ ] 04 Dicts and sets
- [ ] 05 deque, heapq, bisect
- [ ] 06 Functions, recursion, classes
- [ ] 07 Built-ins, math, bits
- [ ] 08 Complexity and gotchas
- [ ] Exit test (8/10 or better)

## Not covered on purpose

Classes beyond what LeetCode gives you, file I/O, exceptions beyond what you'll see in errors, async, typing beyond reading signatures, and third-party libraries (LeetCode doesn't have `sortedcontainers` everywhere; don't rely on it). The algorithm patterns themselves (two pointers, sliding window, DFS/BFS, DP) are learned through the problems and recorded in [PATTERNS.md](../PATTERNS.md).
