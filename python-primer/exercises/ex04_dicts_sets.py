# ══════════════════════════════════════════════════════════════════════
# LESSON 04 · DICTS AND SETS
# Notes: ../04-dicts-sets.md
#
# 1. Write your code where each `raise NotImplementedError` is.
# 2. Ctrl+Shift+B runs the tests. Bottom panel: ok / FAIL / TODO.
# 3. Repeat until everything says ok.
#
# (Tests live in tests/test_ex04_dicts_sets.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════

from collections import Counter, defaultdict


# ══════════════════════════════════════════════════════════════════════
# 1. two_sum                                                  LeetCode 1
# ──────────────────────────────────────────────────────────────────────
# Indices [i, j] with i < j and nums[i] + nums[j] == target. One pass,
# O(n).
#
#   two_sum([2, 7, 11, 15], 9)  ->  [0, 1]
#   two_sum([3, 2, 4], 6)       ->  [1, 2]
#   two_sum([3, 3], 6)          ->  [0, 1]
# ══════════════════════════════════════════════════════════════════════
def two_sum(nums: list, target: int) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 2. contains_duplicate                                     LeetCode 217
# ──────────────────────────────────────────────────────────────────────
# Solve it, with a set.
#
#   contains_duplicate([1, 2, 3, 1])  ->  True
#   contains_duplicate([1, 2, 3])     ->  False
#   contains_duplicate([])            ->  False
# ══════════════════════════════════════════════════════════════════════
def contains_duplicate(nums: list) -> bool:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 3. group_anagrams                                          LeetCode 49
# ──────────────────────────────────────────────────────────────────────
# Group words that are anagrams. Use a defaultdict(list) keyed by
# something hashable. Return groups in first-seen order, words in
# input order.
#
#   group_anagrams([''])  ->  [['']]
# ══════════════════════════════════════════════════════════════════════
def group_anagrams(words: list) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 4. first_unique_char                                      LeetCode 387
# ──────────────────────────────────────────────────────────────────────
# Index of the first character that appears exactly once, else -1.
#
#   first_unique_char('leetcode')      ->  0
#   first_unique_char('loveleetcode')  ->  2
#   first_unique_char('aabb')          ->  -1
# ══════════════════════════════════════════════════════════════════════
def first_unique_char(s: str) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 5. top_k_frequent                                         LeetCode 347
# ──────────────────────────────────────────────────────────────────────
# The k most frequent values, most frequent first (no ties in tests).
#
#   top_k_frequent([1, 1, 1, 2, 2, 3], 2)  ->  [1, 2]
#   top_k_frequent([4], 1)                 ->  [4]
# ══════════════════════════════════════════════════════════════════════
def top_k_frequent(nums: list, k: int) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 6. can_construct                                          LeetCode 383
# ──────────────────────────────────────────────────────────────────────
# Can ransom be built from magazine's letters (each used once)? Use
# Counter.
#
#   can_construct('aa', 'aab')  ->  True
#   can_construct('aa', 'ab')   ->  False
# ══════════════════════════════════════════════════════════════════════
def can_construct(ransom: str, magazine: str) -> bool:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 7. common_elements
# ──────────────────────────────────────────────────────────────────────
# Distinct values that appear in both lists, sorted ascending. Use set
# operations.
#
#   common_elements([4, 1, 2, 2], [2, 4, 4, 9])  ->  [2, 4]
#   common_elements([1], [2])                    ->  []
# ══════════════════════════════════════════════════════════════════════
def common_elements(a: list, b: list) -> list:
    raise NotImplementedError


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
