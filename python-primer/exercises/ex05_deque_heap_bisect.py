# ══════════════════════════════════════════════════════════════════════
# LESSON 05 · DEQUE, HEAPQ, BISECT
# Notes: ../05-deque-heap-bisect.md
#
# 1. Write your code where each `raise NotImplementedError` is.
# 2. Ctrl+Shift+B runs the tests. Bottom panel: ok / FAIL / TODO.
# 3. Repeat until everything says ok.
#
# (Tests live in tests/test_ex05_deque_heap_bisect.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════

import bisect
import heapq
from collections import deque


# ══════════════════════════════════════════════════════════════════════
# 1. shortest_path_len
# ──────────────────────────────────────────────────────────────────────
# graph maps node -> list of neighbors (unweighted). Return the number
# of edges on the shortest path from start to goal, or -1 if
# unreachable. BFS with a deque.
#
#   shortest_path_len(g, 'a', 'e')  ->  3
#   shortest_path_len(g, 'a', 'a')  ->  0
#   shortest_path_len(g, 'a', 'z')  ->  -1
# ══════════════════════════════════════════════════════════════════════
def shortest_path_len(graph: dict, start, goal) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 2. level_sums
# ──────────────────────────────────────────────────────────────────────
# levels_graph maps a node (an int value) to its list of children (a
# tree). Return the sum of node values at each depth, root level
# first. Use the `for _ in range(len(q))` level-by-level loop.
#
#   level_sums(tree, 1)  ->  [1, 5, 15]
# ══════════════════════════════════════════════════════════════════════
def level_sums(levels_graph: dict, root) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 3. kth_largest                                            LeetCode 215
# ──────────────────────────────────────────────────────────────────────
# Solve it with a min-heap of size k. O(n log k). Don't sort.
#
#   kth_largest([3, 2, 1, 5, 6, 4], 2)           ->  5
#   kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)  ->  4
# ══════════════════════════════════════════════════════════════════════
def kth_largest(nums: list, k: int) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 4. merge_sorted_lists
# ──────────────────────────────────────────────────────────────────────
# Merge k sorted lists into one sorted list using a heap of (value,
# list_index, element_index) tuples.
#
#   merge_sorted_lists([[], [0]])  ->  [0]
#   merge_sorted_lists([])         ->  []
# ══════════════════════════════════════════════════════════════════════
def merge_sorted_lists(lists: list) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 5. last_stone_weight                                     LeetCode 1046
# ──────────────────────────────────────────────────────────────────────
# Repeatedly smash the two heaviest stones; if they differ, the
# difference goes back. Return the last stone or 0. Max-heap via
# negation.
#
#   last_stone_weight([2, 7, 4, 1, 8, 1])  ->  1
#   last_stone_weight([1, 1])              ->  0
# ══════════════════════════════════════════════════════════════════════
def last_stone_weight(stones: list) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 6. count_in_sorted
# ──────────────────────────────────────────────────────────────────────
# How many times x appears in sorted list a, in O(log n), using
# bisect.
#
#   count_in_sorted([1, 2, 2, 2, 5], 2)  ->  3
#   count_in_sorted([1, 2, 2, 2, 5], 3)  ->  0
# ══════════════════════════════════════════════════════════════════════
def count_in_sorted(a: list, x) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 7. search_insert                                           LeetCode 35
# ──────────────────────────────────────────────────────────────────────
# Solve it, written by hand with the [lo, hi) template (no bisect).
#
#   search_insert([1, 3, 5, 6], 5)  ->  2
#   search_insert([1, 3, 5, 6], 2)  ->  1
#   search_insert([1, 3, 5, 6], 7)  ->  4
# ══════════════════════════════════════════════════════════════════════
def search_insert(nums: list, target: int) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 8. count_components
# ──────────────────────────────────────────────────────────────────────
# Nodes are 0..n-1, edges are undirected pairs. Build an adjacency
# list with defaultdict(list), then count connected components using
# ITERATIVE DFS (a list as a stack). Must not hit the recursion limit
# on a 20,000-node chain.
#
#   count_components(5, [[0, 1], [1, 2], [3, 4]])                ->  2
#   count_components(3, [])                                      ->  3
#   count_components(20000, [[i, i + 1] for i in range(19999)])  ->  1
# ══════════════════════════════════════════════════════════════════════
def count_components(n: int, edges: list) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 9. RecentCounter  (class)                                 LeetCode 933
# ──────────────────────────────────────────────────────────────────────
# Ping(t) records a request at time t (strictly increasing) and
# returns how many requests happened in [t - 3000, t]. Keep a deque
# and drop old ones from the left.
#
#   rc = RecentCounter()
#   rc.ping(1)     ->  1
#   rc.ping(100)   ->  2
#   rc.ping(3001)  ->  3
#   rc.ping(3002)  ->  3      (the ping at time 1 is now too old)
# ══════════════════════════════════════════════════════════════════════
class RecentCounter:

    def __init__(self):
        raise NotImplementedError

    def ping(self, t: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
