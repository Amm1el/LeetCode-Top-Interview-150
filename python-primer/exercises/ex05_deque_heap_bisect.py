"""05 · deque, heapq, bisect. Replace each `raise NotImplementedError`. Ctrl+Shift+B runs the tests."""
import bisect
import heapq
from collections import deque
from _check import eq


def shortest_path_len(graph: dict, start, goal) -> int:
    """graph maps node -> list of neighbors (unweighted). Return the number of edges on
    the shortest path from start to goal, or -1 if unreachable. BFS with a deque."""
    raise NotImplementedError


def level_sums(levels_graph: dict, root) -> list:
    """levels_graph maps a node (an int value) to its list of children (a tree).
    Return the sum of node values at each depth, root level first.
    Use the `for _ in range(len(q))` level-by-level loop."""
    raise NotImplementedError


def kth_largest(nums: list, k: int) -> int:
    """LeetCode 215 with a min-heap of size k. O(n log k). Don't sort."""
    raise NotImplementedError


def merge_sorted_lists(lists: list) -> list:
    """Merge k sorted lists into one sorted list using a heap of
    (value, list_index, element_index) tuples."""
    raise NotImplementedError


def last_stone_weight(stones: list) -> int:
    """LeetCode 1046: repeatedly smash the two heaviest stones; if they differ, the
    difference goes back. Return the last stone or 0. Max-heap via negation."""
    raise NotImplementedError


def count_in_sorted(a: list, x) -> int:
    """How many times x appears in sorted list a, in O(log n), using bisect."""
    raise NotImplementedError


def search_insert(nums: list, target: int) -> int:
    """LeetCode 35, written by hand with the [lo, hi) template (no bisect)."""
    raise NotImplementedError


def count_components(n: int, edges: list) -> int:
    """Nodes are 0..n-1, edges are undirected pairs. Build an adjacency list with
    defaultdict(list), then count connected components using ITERATIVE DFS (a list as a stack).
    Must not hit the recursion limit on a 20,000-node chain."""
    raise NotImplementedError


class RecentCounter:
    """LeetCode 933: ping(t) records a request at time t (strictly increasing) and returns
    how many requests happened in [t - 3000, t]. Keep a deque and drop old ones from the left."""

    def __init__(self):
        raise NotImplementedError

    def ping(self, t: int) -> int:
        raise NotImplementedError


# ------------------------------------------------------------------ tests

def test_shortest_path_len():
    g = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": [], "z": []}
    eq(shortest_path_len(g, "a", "e"), 3)
    eq(shortest_path_len(g, "a", "a"), 0)
    eq(shortest_path_len(g, "a", "z"), -1)


def test_level_sums():
    tree = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [], 6: []}
    eq(level_sums(tree, 1), [1, 5, 15])


def test_kth_largest():
    eq(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
    eq(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


def test_merge_sorted_lists():
    eq(merge_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
    eq(merge_sorted_lists([[], [0]]), [0])
    eq(merge_sorted_lists([]), [])


def test_last_stone_weight():
    eq(last_stone_weight([2, 7, 4, 1, 8, 1]), 1)
    eq(last_stone_weight([1, 1]), 0)


def test_count_in_sorted():
    eq(count_in_sorted([1, 2, 2, 2, 5], 2), 3)
    eq(count_in_sorted([1, 2, 2, 2, 5], 3), 0)


def test_search_insert():
    eq(search_insert([1, 3, 5, 6], 5), 2)
    eq(search_insert([1, 3, 5, 6], 2), 1)
    eq(search_insert([1, 3, 5, 6], 7), 4)
    eq(search_insert([1, 3, 5, 6], 0), 0)


def test_count_components():
    eq(count_components(5, [[0, 1], [1, 2], [3, 4]]), 2)
    eq(count_components(3, []), 3)
    eq(count_components(20000, [[i, i + 1] for i in range(19999)]), 1)


def test_recent_counter():
    rc = RecentCounter()
    eq([rc.ping(t) for t in (1, 100, 3001, 3002)], [1, 2, 3, 3])


if __name__ == "__main__":
    from _check import run
    run(globals())
