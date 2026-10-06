# 02 · Lists

Exercises: [`exercises/ex02_lists.py`](exercises/ex02_lists.py)

A Python list is Java's `ArrayList`: a dynamic array. It's also your stack.

## The operations you'll use daily

```python
nums = [3, 1, 2]
len(nums)            # 3
nums[0], nums[-1]    # 3, 2        negative index counts from the end
nums.append(4)       # O(1)        push
nums.pop()           # O(1)        pop from the end, returns it
nums.pop(0)          # O(n)        shifts everything; use a deque instead
nums.insert(0, 9)    # O(n)        same problem
x in nums            # O(n)        linear scan; use a set for membership
nums.index(2)        # O(n)        raises ValueError if missing
[0] * n              # n zeros
stack[-1]            # peek
```

## Slicing

`nums[start:stop:step]`, stop exclusive, any part optional.

```python
nums[1:3]      # elements 1 and 2
nums[:k]       # first k
nums[-k:]      # last k
nums[::-1]     # reversed copy
nums[:]        # shallow copy
```

**Every slice is a new list and costs O(k).** `nums[1:]` inside a recursive call turns an O(n) algorithm into O(n²). Pass indices instead.

## "Modify nums in-place"

Many array problems check the list object you were given. Rebinding the name does nothing to the caller's list:

```python
def rotate(nums, k):
    nums = nums[-k:] + nums[:-k]     # WRONG: makes a new list, caller sees no change
    nums[:] = nums[-k:] + nums[:-k]  # RIGHT: overwrites the contents of the same list
```

Also: `nums.sort()` sorts in place and **returns `None`**. `nums = nums.sort()` sets nums to `None`. `sorted(nums)` returns a new list.

## Sorting with keys

```python
words.sort(key=len)                              # by length
pairs.sort(key=lambda p: p[1])                   # by second element
people.sort(key=lambda p: (-p[1], p[0]))         # age descending, then name ascending
intervals.sort()                                 # tuples/lists sort element by element
max(nums, key=abs)                               # key works on max/min too
```

Python's sort is stable and O(n log n). Negating a number in the key is the standard way to get descending order on one field.

## Iteration helpers

```python
for i, x in enumerate(nums):        # index and value, instead of range(len(nums))
for a, b in zip(xs, ys):            # walk two lists together, stops at the shorter
for x in reversed(nums):            # no copy
list(zip(*matrix))                  # transpose: rows become column tuples
```

## Comprehensions

```python
squares = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
```

## 2D grids, the classic trap

```python
grid = [[0] * cols for _ in range(rows)]   # RIGHT: each row is its own list
grid = [[0] * cols] * rows                 # WRONG: every row is the same list object
grid[0][0] = 1                             # with the wrong version, column 0 of every row becomes 1
```

Neighbors in a grid:

```python
for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    r2, c2 = r + dr, c + dc
    if 0 <= r2 < rows and 0 <= c2 < cols:
        ...
```

## Copies in backtracking

```python
res.append(path)       # WRONG: stores a reference; path keeps changing, so every entry ends up identical
res.append(path[:])    # RIGHT: stores a snapshot
```

## Predict the output

1. ```python
   a = [1, 2, 3]
   b = a
   b.append(4)
   print(a)
   ```
2. `print([1, 2, 3, 4, 5][1:-1])`
3. ```python
   g = [[0] * 2] * 2
   g[1][0] = 5
   print(g)
   ```
4. `print(sorted([(2, 'b'), (1, 'z'), (2, 'a')]))`
5. ```python
   nums = [3, 1, 2]
   print(nums.sort())
   ```

<details><summary>Answers</summary>

1. `[1, 2, 3, 4]` (`b = a` copies the reference, not the list)
2. `[2, 3, 4]`
3. `[[5, 0], [5, 0]]` (both rows are the same list)
4. `[(1, 'z'), (2, 'a'), (2, 'b')]`
5. `None`
</details>
