# 06 · Functions, recursion, and LeetCode's classes

Exercises: [`exercises/ex06_functions_recursion.py`](exercises/ex06_functions_recursion.py)

## What a LeetCode Python problem looks like

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ...
```

- `self` is required as the first parameter of every method. You never pass it yourself.
- `Optional[TreeNode]` means "a TreeNode or None". Type hints are documentation only.
- To call another method you wrote: `self.helper(x)`. Most people use a nested function instead (below).

The node classes LeetCode gives you:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

`__init__` is the constructor; `self.x = ...` creates fields. Build a node with `ListNode(3)`, no `new`.

## Linked list moves

```python
dummy = ListNode(0, head)      # dummy node: removes the "what if I delete the head" special case
cur = head
while cur:                     # stop after the last node
while cur and cur.next:        # stop at the last node (or for fast/slow pointers)
```

## Nested functions and `nonlocal`

The usual shape of a DFS:

```python
def diameterOfBinaryTree(self, root):
    best = 0

    def depth(node):
        nonlocal best                     # required because we ASSIGN to best below
        if not node:
            return 0
        l, r = depth(node.left), depth(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    depth(root)
    return best
```

Rules for the inner function:
- **Reading** an outer variable: works.
- **Mutating** an outer list/dict/set (`res.append(x)`, `seen.add(x)`): works.
- **Reassigning** an outer variable (`best = ...`, `count += 1`): needs `nonlocal best`, or you get `UnboundLocalError`.

## Recursion limits

Python's default recursion limit is about 1000 frames. A linked list or a skewed tree with 10⁴ nodes will crash a recursive solution with `RecursionError`. Options: rewrite iteratively with an explicit stack (best), or `sys.setrecursionlimit(10**5)` (works on LeetCode; mention the trade-off in an interview).

## Memoization with @cache

```python
from functools import cache

def climbStairs(self, n):
    @cache
    def ways(i):
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)
    return ways(n)
```

`@cache` remembers results per argument tuple, which turns exponential recursion into top-down DP. Arguments must be hashable (ints, strings, tuples; not lists). `@lru_cache(None)` is the same thing on older Python. Define the cached function **inside** the method so the cache doesn't leak between test cases.

## Backtracking skeleton

```python
res, path = [], []

def backtrack(start):
    res.append(path[:])               # snapshot, not path itself
    for i in range(start, len(nums)):
        path.append(nums[i])          # choose
        backtrack(i + 1)              # explore
        path.pop()                    # un-choose

backtrack(0)
```

## Lambdas and the mutable default trap

`key=lambda x: x[1]` is an inline one-expression function. Use it for sort keys; don't build logic in it.

```python
def f(path=[]):        # WRONG: the same list is reused across every call
def f(path=None):      # RIGHT
    if path is None:
        path = []
```

## Predict the output

1. ```python
   def outer():
       count = 0
       def inc():
           count += 1
       inc()
       return count
   outer()
   ```
2. ```python
   def add(x, acc=[]):
       acc.append(x)
       return acc
   add(1); print(add(2))
   ```
3. ```python
   res, path = [], [1]
   res.append(path)
   path.append(2)
   print(res)
   ```

<details><summary>Answers</summary>

1. `UnboundLocalError` (assigning `count` makes it local to `inc`; needs `nonlocal count`)
2. `[1, 2]`
3. `[[1, 2]]`
</details>
