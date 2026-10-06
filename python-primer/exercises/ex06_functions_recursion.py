"""06 · Functions, recursion, classes. Replace each `raise NotImplementedError` and run:
python3 ex06_functions_recursion.py"""
from functools import cache
from typing import List, Optional
from _check import eq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_list(values: list) -> Optional[ListNode]:
    """Build a linked list from a Python list and return the head (None if empty).
    Use a dummy node."""
    raise NotImplementedError


def to_pylist(head: Optional[ListNode]) -> list:
    """Linked list -> Python list."""
    raise NotImplementedError


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """LeetCode 206, iteratively, O(1) space."""
        raise NotImplementedError

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """LeetCode 203: remove every node with node.val == val. Use a dummy node."""
        raise NotImplementedError

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """LeetCode 104, recursively."""
        raise NotImplementedError

    def countLeaves(self, root: Optional[TreeNode]) -> int:
        """Count leaves with a nested dfs() that increments an outer counter (needs nonlocal)."""
        raise NotImplementedError

    def climbStairs(self, n: int) -> int:
        """LeetCode 70 with a nested @cache function. Must handle n = 80 instantly."""
        raise NotImplementedError

    def combine(self, n: int, k: int) -> List[List[int]]:
        """LeetCode 77: all combinations of k numbers from 1..n, in lexicographic order.
        Backtracking with path.append / recurse / path.pop."""
        raise NotImplementedError


class MinStack:
    """LeetCode 155: push, pop, top, getMin, all O(1)."""

    def __init__(self):
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def getMin(self) -> int:
        raise NotImplementedError


class Trie:
    """LeetCode 208: insert, search (whole word), startsWith (prefix).
    Write a small TrieNode class (or use nested dicts)."""

    def __init__(self):
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError


class LRUCache:
    """LeetCode 146 using collections.OrderedDict. get returns -1 if missing.
    Both get and put count as a use; put evicts the least recently used key when over capacity."""

    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


# ------------------------------------------------------------------ tests

def _tree():
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    return TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))


def test_build_and_to_pylist():
    eq(to_pylist(build_list([1, 2, 3])), [1, 2, 3])
    eq(build_list([]), None)
    eq(to_pylist(None), [])


def test_reverse_list():
    eq(to_pylist(Solution().reverseList(build_list([1, 2, 3, 4]))), [4, 3, 2, 1])
    eq(Solution().reverseList(None), None)


def test_remove_elements():
    eq(to_pylist(Solution().removeElements(build_list([7, 1, 7, 2, 7]), 7)), [1, 2])
    eq(to_pylist(Solution().removeElements(build_list([7, 7]), 7)), [])


def test_max_depth():
    eq(Solution().maxDepth(_tree()), 3)
    eq(Solution().maxDepth(None), 0)


def test_count_leaves():
    eq(Solution().countLeaves(_tree()), 3)
    eq(Solution().countLeaves(None), 0)


def test_climb_stairs():
    eq(Solution().climbStairs(2), 2)
    eq(Solution().climbStairs(5), 8)
    eq(Solution().climbStairs(80), 37889062373143906)


def test_combine():
    eq(Solution().combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    eq(Solution().combine(1, 1), [[1]])


def test_min_stack():
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    eq(s.getMin(), -3)
    s.pop()
    eq(s.top(), 0)
    eq(s.getMin(), -2)
    s.push(-2)
    s.pop()
    eq(s.getMin(), -2, "duplicate minimums")


def test_trie():
    t = Trie()
    t.insert("apple")
    eq(t.search("apple"), True)
    eq(t.search("app"), False)
    eq(t.startsWith("app"), True)
    t.insert("app")
    eq(t.search("app"), True)
    eq(t.startsWith("b"), False)


def test_lru_cache():
    c = LRUCache(2)
    c.put(1, 1); c.put(2, 2)
    eq(c.get(1), 1)
    c.put(3, 3)                    # evicts 2 (1 was used more recently)
    eq(c.get(2), -1)
    c.put(4, 4)                    # evicts 1
    eq([c.get(1), c.get(3), c.get(4)], [-1, 3, 4])
    c.put(3, 30)                   # update counts as a use
    c.put(5, 5)                    # evicts 4
    eq([c.get(4), c.get(3)], [-1, 30])


if __name__ == "__main__":
    from _check import run
    run(globals())
