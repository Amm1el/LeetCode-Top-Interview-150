# 08 · Complexity cheat sheet and gotchas

Exercises: [`exercises/ex08_gotchas.py`](exercises/ex08_gotchas.py)

When an interviewer asks "what's the complexity?", hidden costs of Python operations are where answers go wrong. Learn this table.

## Cost of common operations

| Operation | Cost | Note |
|---|---|---|
| `lst.append(x)`, `lst.pop()`, `lst[i]`, `len(lst)` | O(1) | |
| `lst.pop(0)`, `lst.insert(0, x)`, `del lst[i]` | O(n) | shifts elements; use `deque` |
| `x in lst`, `lst.index(x)`, `lst.count(x)`, `lst.remove(x)` | O(n) | |
| `lst[a:b]`, `lst[:]`, `lst[::-1]`, `lst + other` | O(k) | creates a new list |
| `lst.sort()`, `sorted(lst)` | O(n log n) | |
| `min`, `max`, `sum`, `reversed` iteration | O(n) | |
| `d[k]`, `d[k] = v`, `k in d`, `del d[k]` | O(1) avg | same for sets |
| `Counter(lst)`, `set(lst)`, `dict(...)` | O(n) | building costs n |
| `a \| b`, `a & b` on sets | O(len(a) + len(b)) / O(min) | |
| `deque.append/appendleft/pop/popleft` | O(1) | |
| `deque[i]` in the middle | O(n) | |
| `heappush`, `heappop` | O(log n) | |
| `heapify` | O(n) | not n log n |
| `bisect_left/right` | O(log n) | |
| `insort` | O(n) | the insert shifts |
| `"".join(parts)` | O(total length) | |
| `s += c` in a loop | up to O(n²) total | build a list and join |
| `s[a:b]`, `s.lower()`, `s.split()`, `s[::-1]` | O(n) | strings are copied |
| `t in s` (substring) | O(len(s) · len(t)) worst | |
| Recursion | O(depth) stack space | count it in space complexity |

## Gotchas, all in one place

1. `-7 // 2 == -4` and `-7 % 3 == 2`. Use `int(a / b)` for truncation.
2. `[[0] * c] * r` shares rows. Use `[[0] * c for _ in range(r)]`.
3. `nums = ...` inside a function doesn't modify the caller's list. Use `nums[:] = ...`.
4. `lst.sort()` returns `None`.
5. `res.append(path)` stores a reference. Use `path[:]`.
6. `if x:` is false for `0`. Use `if x is not None:` when 0 is valid.
7. `{}` is an empty dict. `set()` is an empty set.
8. Reading a missing `defaultdict` key inserts it.
9. Lists can't be dict keys or set members. Convert to a tuple.
10. Reassigning an outer variable in a nested function needs `nonlocal`.
11. `def f(acc=[])` shares one list across calls.
12. Recursion depth ~1000 by default.
13. Heap tuples with equal priorities compare the next element; add an index tiebreaker.
14. `heapq` is min-only; negate for max.
15. Ints never overflow; enforce 32-bit limits yourself when the problem asks.
16. Negative ints have infinite leading 1 bits; mask with `0xFFFFFFFF` for 32-bit bit problems.
17. Modifying a list, dict, or set while iterating over it. Iterate over a copy.
18. `s.split(" ")` keeps empty strings; `s.split()` doesn't.
19. Shadowing built-ins: naming a variable `list`, `dict`, `sum`, `min`, `max`, `id`, `str` breaks those functions for the rest of the function. Use `lst`, `total`, `lo`/`hi`.
20. `is` checks identity, `==` checks value. Use `is` only for `None`.

## Final self-test

Answer all of these out loud, then check. If you miss more than three, reread the lesson it came from.

1. What's the time complexity of this, and why?
   ```python
   while nums:
       x = nums.pop(0)
   ```
2. What's wrong here?
   ```python
   def dfs(i, path):
       if i == n:
           res.append(path)
       ...
   ```
3. Output? `print(sorted([3, 1, 2])[::-1][0])`
4. You need the 3 smallest of 10⁶ numbers. What's the cleanest one-liner and its complexity?
5. Why does `visited.add([r, c])` fail, and what's the fix?
6. Output?
   ```python
   a = [1, 2, 3]
   for x in a[:]:
       if x == 2:
           a.remove(x)
   print(a)
   ```

<details><summary>Answers</summary>

1. O(n²): each `pop(0)` is O(n). Use a deque and `popleft()`, or iterate by index.
2. It appends a reference to `path`; append `path[:]` (and make sure path is undone after recursing).
3. `3`
4. `heapq.nsmallest(3, nums)`, O(n log 3) which is O(n). Sorting would be O(n log n).
5. Lists aren't hashable. Use a tuple: `visited.add((r, c))`.
6. `[1, 3]` (safe, because it iterates over a copy)
</details>
