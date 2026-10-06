"""04 · Dicts and sets. Replace each `raise NotImplementedError`. Ctrl+Shift+B runs the tests."""
from collections import Counter, defaultdict
from _check import eq


def two_sum(nums: list, target: int) -> list:
    """LeetCode 1: indices [i, j] with i < j and nums[i] + nums[j] == target. One pass, O(n)."""
    raise NotImplementedError


def contains_duplicate(nums: list) -> bool:
    """LeetCode 217, with a set."""
    raise NotImplementedError


def group_anagrams(words: list) -> list:
    """LeetCode 49: group words that are anagrams. Use a defaultdict(list) keyed by
    something hashable. Return groups in first-seen order, words in input order."""
    raise NotImplementedError


def first_unique_char(s: str) -> int:
    """LeetCode 387: index of the first character that appears exactly once, else -1."""
    raise NotImplementedError


def top_k_frequent(nums: list, k: int) -> list:
    """LeetCode 347: the k most frequent values, most frequent first (no ties in tests)."""
    raise NotImplementedError


def can_construct(ransom: str, magazine: str) -> bool:
    """LeetCode 383: can ransom be built from magazine's letters (each used once)? Use Counter."""
    raise NotImplementedError


def common_elements(a: list, b: list) -> list:
    """Distinct values that appear in both lists, sorted ascending. Use set operations."""
    raise NotImplementedError


# ------------------------------------------------------------------ tests

def test_two_sum():
    eq(two_sum([2, 7, 11, 15], 9), [0, 1])
    eq(two_sum([3, 2, 4], 6), [1, 2])
    eq(two_sum([3, 3], 6), [0, 1])


def test_contains_duplicate():
    eq(contains_duplicate([1, 2, 3, 1]), True)
    eq(contains_duplicate([1, 2, 3]), False)
    eq(contains_duplicate([]), False)


def test_group_anagrams():
    eq(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
       [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    eq(group_anagrams([""]), [[""]])


def test_first_unique_char():
    eq(first_unique_char("leetcode"), 0)
    eq(first_unique_char("loveleetcode"), 2)
    eq(first_unique_char("aabb"), -1)


def test_top_k_frequent():
    eq(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
    eq(top_k_frequent([4], 1), [4])


def test_can_construct():
    eq(can_construct("aa", "aab"), True)
    eq(can_construct("aa", "ab"), False)


def test_common_elements():
    eq(common_elements([4, 1, 2, 2], [2, 4, 4, 9]), [2, 4])
    eq(common_elements([1], [2]), [])


if __name__ == "__main__":
    from _check import run
    run(globals())
