"""Tests for ex04_dicts_sets.py. Run the exercise file, not this one."""
from ex04_dicts_sets import *  # noqa: F401,F403
from _check import eq


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
