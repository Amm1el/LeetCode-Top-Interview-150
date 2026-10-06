"""08 · Gotchas. Every function below is BROKEN. Find the bug, fix it with the smallest
change, and write a one-line comment explaining what was wrong. Ctrl+Shift+B runs the tests.

Delete the `raise NotImplementedError` line in each function once you've fixed it."""
from collections import deque
import heapq
from _check import eq


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_zeros(nums: list) -> None:
    """Remove all zeros from nums in place, keeping order."""
    raise NotImplementedError
    nums = [x for x in nums if x != 0]


def all_paths(n: int) -> list:
    """Every binary string of length n as a list of ints, e.g. n=2 -> [[0,0],[0,1],[1,0],[1,1]]."""
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


def count_nodes_bfs(graph: dict, start) -> int:
    """Number of nodes reachable from start (including start)."""
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


def tree_sum(root) -> int:
    """Sum of node values in a binary tree given as nested tuples (val, left, right) or None."""
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


def merge_k_linked(heads: list) -> list:
    """Merge sorted linked lists (Node objects) and return the values as a Python list."""
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


def window_max_count(nums: list, k: int) -> int:
    """How many windows of size k have their maximum at the window's last position?
    (A deliberately simple brute force; the bug is not about efficiency.)"""
    raise NotImplementedError
    max = 0
    for i in range(k - 1, len(nums)):
        window = nums[i - k + 1:i + 1]
        if window[-1] == max(window):
            max += 1
    return max


def make_board(n: int) -> list:
    """n x n board of '.' strings where each row can be edited independently."""
    raise NotImplementedError
    return [["."] * n] * n


def contains(nums: list, target) -> bool:
    """Does nums contain target? (Written the long way on purpose.)"""
    raise NotImplementedError
    idx = None
    for i, x in enumerate(nums):
        if x == target:
            idx = i
            break
    return True if idx else False


def safe_lookup_count(words: list, queries: list) -> list:
    """For each query, how many times it appears in words. Must not add queries to the counts."""
    raise NotImplementedError
    from collections import defaultdict
    counts = defaultdict(int)
    for w in words:
        counts[w] += 1
    answer = [counts[q] for q in queries]
    assert len(counts) == len(set(words)), "queries leaked into counts"
    return answer


# ------------------------------------------------------------------ tests

def test_remove_zeros():
    a = [0, 1, 0, 3, 12]
    remove_zeros(a)
    eq(a, [1, 3, 12])


def test_all_paths():
    eq(all_paths(2), [[0, 0], [0, 1], [1, 0], [1, 1]])


def test_count_nodes_bfs():
    eq(count_nodes_bfs({1: [2, 3], 2: [4], 3: [4], 4: [], 5: [1]}, 1), 4)


def test_tree_sum():
    eq(tree_sum((1, (2, None, None), (3, (4, None, None), None))), 10)
    eq(tree_sum(None), 0)


def test_merge_k_linked():
    a = Node(1, Node(4))
    b = Node(1, Node(3))
    eq(merge_k_linked([a, b, None]), [1, 1, 3, 4])


def test_window_max_count():
    eq(window_max_count([1, 3, 2, 5, 4, 6], 2), 3)


def test_make_board():
    b = make_board(3)
    b[0][0] = "Q"
    eq([row[0] for row in b], ["Q", ".", "."])


def test_contains():
    eq(contains([5, 6], 6), True)
    eq(contains([5, 6], 5), True)
    eq(contains([5, 6], 9), False)


def test_safe_lookup_count():
    eq(safe_lookup_count(["a", "b", "a"], ["a", "z"]), [2, 0])


if __name__ == "__main__":
    from _check import run
    run(globals())
