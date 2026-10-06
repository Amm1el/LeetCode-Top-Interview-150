# ══════════════════════════════════════════════════════════════════════
# LESSON 06 · FUNCTIONS, RECURSION, CLASSES
# Notes: ../06-functions-recursion-classes.md
#
# 1. Write your code where each `raise NotImplementedError` is.
# 2. Ctrl+Shift+B runs the tests. Bottom panel: ok / FAIL / TODO.
# 3. Repeat until everything says ok.
#
# (Tests live in tests/test_ex06_functions_recursion.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════

from functools import cache
from typing import List, Optional


# Given (LeetCode defines this for you, don't change it)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Given (LeetCode defines this for you, don't change it)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ══════════════════════════════════════════════════════════════════════
# 1. build_list
# ──────────────────────────────────────────────────────────────────────
# Build a linked list from a Python list and return the head (None if
# empty). Use a dummy node.
#
#   build_list([1, 2, 3])  ->  head of 1 → 2 → 3
#   build_list([])         ->  None
# ══════════════════════════════════════════════════════════════════════
def build_list(values: list) -> Optional[ListNode]:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 2. to_pylist
# ──────────────────────────────────────────────────────────────────────
# Linked list -> Python list.
#
#   to_pylist(1 → 2 → 3)  ->  [1, 2, 3]
#   to_pylist(None)       ->  []
# ══════════════════════════════════════════════════════════════════════
def to_pylist(head: Optional[ListNode]) -> list:
    raise NotImplementedError


# The methods below are inside LeetCode's `class Solution`, exactly
# like on the site. Call one as Solution().maxDepth(root).

class Solution:

    # ══════════════════════════════════════════════════════════════════════
    # 3. reverseList                                            LeetCode 206
    # ──────────────────────────────────────────────────────────────────────
    # Solve it, iteratively, O(1) space.
    #
    #   reverseList(1 → 2 → 3 → 4)  ->  4 → 3 → 2 → 1
    #   reverseList(None)           ->  None
    # ══════════════════════════════════════════════════════════════════════
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise NotImplementedError

    # ══════════════════════════════════════════════════════════════════════
    # 4. removeElements                                         LeetCode 203
    # ──────────────────────────────────────────────────────────────────────
    # Remove every node with node.val == val. Use a dummy node.
    #
    #   removeElements(7 → 1 → 7 → 2 → 7, val=7)  ->  1 → 2
    #   removeElements(7 → 7, val=7)              ->  None
    # ══════════════════════════════════════════════════════════════════════
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        raise NotImplementedError

    # ══════════════════════════════════════════════════════════════════════
    # 5. maxDepth                                               LeetCode 104
    # ──────────────────────────────────────────────────────────────────────
    # Solve it, recursively.
    #
    #        3
    #       / \
    #      9   20
    #         /  \
    #        15   7
    #
    #   maxDepth(root of the tree above)  ->  3
    #   maxDepth(None)                    ->  0
    # ══════════════════════════════════════════════════════════════════════
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        raise NotImplementedError

    # ══════════════════════════════════════════════════════════════════════
    # 6. countLeaves
    # ──────────────────────────────────────────────────────────────────────
    # Count leaves with a nested dfs() that increments an outer counter
    # (needs nonlocal).
    #
    #   countLeaves(the tree from maxDepth)  ->  3      (9, 15 and 7)
    #   countLeaves(None)                    ->  0
    # ══════════════════════════════════════════════════════════════════════
    def countLeaves(self, root: Optional[TreeNode]) -> int:
        raise NotImplementedError

    # ══════════════════════════════════════════════════════════════════════
    # 7. climbStairs                                             LeetCode 70
    # ──────────────────────────────────────────────────────────────────────
    # Solve it with a nested @cache function. Must handle n = 80
    # instantly.
    #
    #   climbStairs(2)   ->  2
    #   climbStairs(5)   ->  8
    #   climbStairs(80)  ->  37889062373143906
    # ══════════════════════════════════════════════════════════════════════
    def climbStairs(self, n: int) -> int:
        raise NotImplementedError

    # ══════════════════════════════════════════════════════════════════════
    # 8. combine                                                 LeetCode 77
    # ──────────────────────────────────────────────────────────────────────
    # All combinations of k numbers from 1..n, in lexicographic order.
    # Backtracking with path.append / recurse / path.pop.
    #
    #   combine(4, 2)  ->  [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
    #   combine(1, 1)  ->  [[1]]
    # ══════════════════════════════════════════════════════════════════════
    def combine(self, n: int, k: int) -> List[List[int]]:
        raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 9. MinStack  (class)                                      LeetCode 155
# ──────────────────────────────────────────────────────────────────────
# Push, pop, top, getMin, all O(1).
#
#   s = MinStack()
#   s.push(-2); s.push(0); s.push(-3)
#   s.getMin()  ->  -3
#   s.pop()
#   s.top()     ->  0
#   s.getMin()  ->  -2
# ══════════════════════════════════════════════════════════════════════
class MinStack:

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


# ══════════════════════════════════════════════════════════════════════
# 10. Trie  (class)                                         LeetCode 208
# ──────────────────────────────────────────────────────────────────────
# Insert, search (whole word), startsWith (prefix). Write a small
# TrieNode class (or use nested dicts).
#
#   t = Trie()
#   t.insert("apple")
#   t.search("apple")    ->  True
#   t.search("app")      ->  False   (only a prefix)
#   t.startsWith("app")  ->  True
# ══════════════════════════════════════════════════════════════════════
class Trie:

    def __init__(self):
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 11. LRUCache  (class)                                     LeetCode 146
# ──────────────────────────────────────────────────────────────────────
# Solve it using collections.OrderedDict. get returns -1 if missing.
# Both get and put count as a use; put evicts the least recently used
# key when over capacity.
#
#   c = LRUCache(2)
#   c.put(1, 1); c.put(2, 2)
#   c.get(1)  ->  1       (1 is now the most recently used)
#   c.put(3, 3)            (over capacity: evicts 2)
#   c.get(2)  ->  -1
# ══════════════════════════════════════════════════════════════════════
class LRUCache:

    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
