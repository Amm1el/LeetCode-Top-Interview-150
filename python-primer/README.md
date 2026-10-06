# Python for LeetCode: a two-day primer

The Python you need for Top Interview 150, and nothing else. Written for someone who already knows Java: it focuses on what's different and what bites.

**Hard stop: LeetCode starts no later than Friday, Oct 9, 2026.** Anything not covered here gets learned on real problems.

## Where am I?

**Terminal > Run Task > Primer progress.** It shows every lesson's test count and tells you the exact file to open next. Start there every session.

## The loop for every lesson

1. **Open the lesson notes** (click the link below). They open formatted. Read top to bottom.
2. **Predict the output** at the bottom of the notes. Write your guesses before opening the answers.
3. **Click the "Exercises" link** at the top of the notes. The exercise file opens.
   Tip: drag the exercise tab to the right half of the window so the notes and the code are side by side.
4. **Write code** where each `raise NotImplementedError` is. Press **Ctrl+Shift+B** to run the tests. The bottom panel shows `ok`, `FAIL` (with what was expected), or `TODO`. Repeat until everything says `ok`.
5. **Push** (Source Control icon on the left: type a message, Commit, Sync), then tell Claude **"lesson NN done."**

Lesson 08 is different: every function is already written and broken. Find the bug, fix it with the smallest change, and comment what was wrong.

## Schedule

| Day | Lessons | Exercises | Time |
|---|---|---|---|
| **Tue** | [01 Basics](01-basics.md) · [02 Lists](02-lists.md) | 12 | ~2 h |
| **Wed** | [03 Strings](03-strings.md) · [04 Dicts and sets](04-dicts-sets.md) · [05 deque, heapq, bisect](05-deque-heap-bisect.md) | 22 | ~3 h |
| **Thu** | [06 Recursion and classes](06-functions-recursion-classes.md) · [07 Built-ins, math, bits](07-builtins-math-bits.md) · [08 Gotchas](08-complexity-gotchas.md) · exit test | 28 | ~3.5 h |
| **Fri** | Crash course "Arrays and strings," then #88 Merge Sorted Array | | |

Stuck more than 10 minutes on one exercise? Skip it, finish the lesson, come back, and bring it to Claude if it's still stuck. Running behind? Cut lesson 07's bit half first, then lesson 08's exercises. Never cut 02, 04, 05, or 06.

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

## Coverage: every Top 150 section

| Section | Python you need | Lesson |
|---|---|---|
| Array / String | indexing, slicing, in-place `nums[:] =`, string building, `ord`/`chr` | 01, 02, 03 |
| Two Pointers | `while lo < hi`, multiple assignment | 01, 02 |
| Sliding Window | dict/Counter of the window, `deque` | 04, 05 |
| Matrix | 2D grids, `zip(*m)`, neighbor loops | 02 |
| Hashmap | dict, set, Counter, defaultdict, hashable keys | 04 |
| Intervals | sort with `key=lambda` | 02 |
| Stack | list as stack, `int(a / b)` truncation | 01, 02 |
| Linked List | ListNode, dummy node, OrderedDict for LRU Cache | 06 |
| Binary Tree General / BFS / BST | TreeNode, recursion, `nonlocal`, level-order `deque` | 05, 06 |
| Graph General / BFS | adjacency from edge lists, BFS, iterative DFS | 05 |
| Trie | writing your own class with a children dict | 06 |
| Backtracking | append / recurse / pop, `path[:]` | 02, 06 |
| Divide & Conquer | recursion on index ranges (not slices) | 02, 06 |
| Kadane's Algorithm | running max with `float('-inf')` | 01 |
| Binary Search | `bisect`, the `[lo, hi)` template | 05 |
| Heap | `heapq`, max-heap by negation, tiebreakers | 05 |
| Bit Manipulation | bit ops, 32-bit masks | 07 |
| Math | `//`, `%`, `math`, no overflow | 01, 07 |
| 1D / Multidimensional DP | `@cache`, 2D tables | 02, 06 |
| Design problems (Min Stack, RandomizedSet, LRU) | classes, `self.`, `random.choice` | 06 |

## Not covered on purpose

Classes beyond what LeetCode gives you, file I/O, exceptions beyond what you'll see in errors, async, typing beyond reading signatures, and third-party libraries (LeetCode doesn't have `sortedcontainers` everywhere; don't rely on it). The algorithm patterns themselves (two pointers, sliding window, DFS/BFS, DP) are learned through the problems and recorded in [PATTERNS.md](../PATTERNS.md).
