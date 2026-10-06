# ══════════════════════════════════════════════════════════════════════
# LESSON 08 · GOTCHAS: FIX THE BUGS
# Notes: ../08-complexity-gotchas.md
#
# Every function below is already written and BROKEN.
# 1. Delete the `raise NotImplementedError` line in a function.
# 2. Run the tests (Ctrl+Shift+B) and read the error.
# 3. Fix the bug with the smallest change, and add a one-line
#    comment saying what was wrong.
#
# (Tests live in tests/test_ex08_gotchas.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════

from collections import deque
import heapq


# Given (LeetCode defines this for you, don't change it)
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# ══════════════════════════════════════════════════════════════════════
# 1. remove_zeros
# ──────────────────────────────────────────────────────────────────────
# Remove all zeros from nums in place, keeping order.
#
#   nums = [0, 1, 0, 3, 12]
#   remove_zeros(nums)
#   nums should now be [1, 3, 12]
# ══════════════════════════════════════════════════════════════════════
def remove_zeros(nums: list) -> None:
    raise NotImplementedError
    nums = [x for x in nums if x != 0]


# ══════════════════════════════════════════════════════════════════════
# 2. all_paths
# ──────────────────────────────────────────────────────────────────────
# Every binary string of length n as a list of ints, e.g. n=2 ->
# [[0,0],[0,1],[1,0],[1,1]].
#
#   all_paths(2)  ->  [[0, 0], [0, 1], [1, 0], [1, 1]]
# ══════════════════════════════════════════════════════════════════════
def all_paths(n: int) -> list:
    raise NotImplementedError
    res, path = [], []

    def go():
        if len(path) == n:
            res.append(path)
            return
        for bit in (0, 1):
            path.append(bit)
            go()
            path.pop()

    go()
    return res


# ══════════════════════════════════════════════════════════════════════
# 3. count_nodes_bfs
# ──────────────────────────────────────────────────────────────────────
# Number of nodes reachable from start (including start).
#
#   count_nodes_bfs({1: [2, 3], 2: [4], 3: [4], 4: []}, 1)
#     ->  4
# ══════════════════════════════════════════════════════════════════════
def count_nodes_bfs(graph: dict, start) -> int:
    raise NotImplementedError
    seen = set()
    q = deque([start])
    count = 0
    while q:
        node = q.popleft()
        count += 1
        seen.add(node)
        for nxt in graph[node]:
            if nxt not in seen:
                q.append(nxt)
    return count


# ══════════════════════════════════════════════════════════════════════
# 4. tree_sum
# ──────────────────────────────────────────────────────────────────────
# Sum of node values in a binary tree given as nested tuples (val,
# left, right) or None.
#
#   tree_sum((1, (2, None, None), (3, (4, None, None), None)))  ->  10
#   tree_sum(None)                                              ->  0
# ══════════════════════════════════════════════════════════════════════
def tree_sum(root) -> int:
    raise NotImplementedError
    total = 0

    def dfs(node):
        if node is None:
            return
        val, left, right = node
        total += val
        dfs(left)
        dfs(right)

    dfs(root)
    return total


# ══════════════════════════════════════════════════════════════════════
# 5. merge_k_linked
# ──────────────────────────────────────────────────────────────────────
# Merge sorted linked lists (Node objects) and return the values as a
# Python list.
#
#   merge_k_linked([a, b, None])  ->  [1, 1, 3, 4]
# ══════════════════════════════════════════════════════════════════════
def merge_k_linked(heads: list) -> list:
    raise NotImplementedError
    h = []
    for node in heads:
        if node:
            heapq.heappush(h, (node.val, node))
    out = []
    while h:
        val, node = heapq.heappop(h)
        out.append(val)
        if node.next:
            heapq.heappush(h, (node.next.val, node.next))
    return out


# ══════════════════════════════════════════════════════════════════════
# 6. window_max_count
# ──────────────────────────────────────────────────────────────────────
# How many windows of size k have their maximum at the window's last
# position? (A deliberately simple brute force; the bug is not about
# efficiency.)
#
#   window_max_count([1, 3, 2, 5, 4, 6], 2)  ->  3
# ══════════════════════════════════════════════════════════════════════
def window_max_count(nums: list, k: int) -> int:
    raise NotImplementedError
    max = 0
    for i in range(k - 1, len(nums)):
        window = nums[i - k + 1:i + 1]
        if window[-1] == max(window):
            max += 1
    return max


# ══════════════════════════════════════════════════════════════════════
# 7. make_board
# ──────────────────────────────────────────────────────────────────────
# n x n board of '.' strings where each row can be edited
# independently.
#
#   b = make_board(3)
#   b[0][0] = "Q"
#   only row 0 should change: [row[0] for row in b] == ["Q", ".", "."]
# ══════════════════════════════════════════════════════════════════════
def make_board(n: int) -> list:
    raise NotImplementedError
    return [["."] * n] * n


# ══════════════════════════════════════════════════════════════════════
# 8. contains
# ──────────────────────────────────────────────────────────────────────
# Does nums contain target? (Written the long way on purpose.)
#
#   contains([5, 6], 6)  ->  True
#   contains([5, 6], 5)  ->  True
#   contains([5, 6], 9)  ->  False
# ══════════════════════════════════════════════════════════════════════
def contains(nums: list, target) -> bool:
    raise NotImplementedError
    idx = None
    for i, x in enumerate(nums):
        if x == target:
            idx = i
            break
    return True if idx else False


# ══════════════════════════════════════════════════════════════════════
# 9. safe_lookup_count
# ──────────────────────────────────────────────────────────────────────
# For each query, how many times it appears in words. Must not add
# queries to the counts.
#
#   safe_lookup_count(['a', 'b', 'a'], ['a', 'z'])  ->  [2, 0]
# ══════════════════════════════════════════════════════════════════════
def safe_lookup_count(words: list, queries: list) -> list:
    raise NotImplementedError
    from collections import defaultdict
    counts = defaultdict(int)
    for w in words:
        counts[w] += 1
    answer = [counts[q] for q in queries]
    assert len(counts) == len(set(words)), "queries leaked into counts"
    return answer


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
