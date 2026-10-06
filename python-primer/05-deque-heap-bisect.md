# 05 · deque, heapq, bisect

Exercises: [`exercises/ex05_deque_heap_bisect.py`](exercises/ex05_deque_heap_bisect.py)

Three tools that replace Java's `ArrayDeque`, `PriorityQueue`, and `Collections.binarySearch`.

## deque: a queue that's fast at both ends

```python
from collections import deque

q = deque([start])
q.append(x)          # right, O(1)
q.appendleft(x)      # left, O(1)
q.pop()              # right, O(1)
q.popleft()          # left, O(1)   <- the reason to use it; list.pop(0) is O(n)
q[0], q[-1]          # peek both ends, O(1)
```

Indexing into the middle (`q[i]`) is O(n). Use a deque for queues, BFS, and sliding windows where things leave from the front.

**BFS template**, shortest distance in an unweighted graph:

```python
def bfs(graph, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in dist:          # mark when you ENQUEUE, not when you dequeue
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    return dist
```

Level by level (needed for many tree problems):

```python
while q:
    for _ in range(len(q)):              # len(q) is evaluated once, so this is exactly one level
        node = q.popleft()
        ...
```

## heapq: a min-heap on a plain list

```python
import heapq

h = []
heapq.heappush(h, 5)
heapq.heappop(h)          # smallest, O(log n)
h[0]                      # peek smallest, O(1)
heapq.heapify(nums)       # in place, O(n)
heapq.nlargest(k, nums)   # sorted list of the k largest
```

**Max-heap:** there isn't a simple flag. Push negatives and negate on the way out:

```python
heapq.heappush(h, -x)
largest = -heapq.heappop(h)
```

**Tuples** compare element by element, so `(priority, item)` works. If two priorities tie, Python compares the items, and that crashes for things like `ListNode`. Add a tiebreaker:

```python
heapq.heappush(h, (node.val, i, node))   # i is unique, so node is never compared
```

**Top-k pattern:** to keep the k *largest*, use a *min*-heap of size k and pop when it grows past k. The root is then the k-th largest. O(n log k).

## bisect: binary search on a sorted list

```python
import bisect

a = [1, 3, 3, 3, 7]
bisect.bisect_left(a, 3)    # 1: first index where 3 could go (first index with a[i] >= 3)
bisect.bisect_right(a, 3)   # 4: index just past the last 3 (first index with a[i] > 3)
bisect.bisect_left(a, 4)    # 4: insertion point when absent
bisect.insort(a, 5)         # inserts in sorted position: O(log n) search but O(n) insert
```

Count of `x` in a sorted list: `bisect_right(a, x) - bisect_left(a, x)`.

You still need to write binary search by hand, because the Binary Search section of Top 150 searches over answers and rotated arrays, not just sorted lists. The template that avoids off-by-one bugs:

```python
lo, hi = 0, len(a)              # search space [lo, hi)
while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] < target:         # condition that's False then True across the array
        lo = mid + 1
    else:
        hi = mid
return lo                       # first index where the condition flips; equals bisect_left
```

## Predict the output

1. ```python
   h = [5, 1, 4]
   heapq.heapify(h)
   print(h[0], heapq.heappop(h), h[0])
   ```
2. `print(bisect.bisect_left([1, 2, 4], 3), bisect.bisect_right([1, 2, 2, 2], 2))`
3. ```python
   q = deque([1, 2, 3])
   q.appendleft(0); q.pop()
   print(list(q))
   ```
4. `print(heapq.nlargest(2, [3, 9, 1, 9]))`

<details><summary>Answers</summary>

1. `1 1 4`
2. `2 4`
3. `[0, 1, 2]`
4. `[9, 9]`
</details>
