"""Tests for ex02_lists.py. Run the exercise file, not this one."""
from ex02_lists import *  # noqa: F401,F403
from _check import eq


def test_rotate_in_place():
    a = [1, 2, 3, 4, 5, 6, 7]
    same = a
    assert rotate_in_place(a, 3) is None, "should return None"
    assert a is same, "must modify the same list object"
    eq(a, [5, 6, 7, 1, 2, 3, 4])
    b = [1, 2]
    rotate_in_place(b, 5)
    eq(b, [2, 1], "k larger than n")
    c = [1]
    rotate_in_place(c, 0)
    eq(c, [1])


def test_make_grid():
    g = make_grid(3, 2)
    eq(g, [[0, 0], [0, 0], [0, 0]])
    g[0][0] = 9
    eq(g[1][0], 0, "rows must be independent")


def test_sort_people():
    people = [("bo", 30), ("al", 25), ("cy", 30), ("ab", 25)]
    eq(sort_people(people), [("bo", 30), ("cy", 30), ("ab", 25), ("al", 25)])
    eq(people[0], ("bo", 30), "don't modify the input")


def test_prefix_sums():
    p = prefix_sums([2, -1, 3, 4])
    eq(p, [0, 2, 1, 4, 8])
    eq(p[3] - p[1], -1 + 3)
    eq(prefix_sums([]), [0])


def test_positive_positions():
    eq(positive_positions([0, 5, -2, 7]), [(1, 5), (3, 7)])


def test_transpose():
    eq(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])


def test_all_subsets_wrong_vs_right():
    eq(all_subsets_wrong_vs_right([1, 2]), [[1, 2], [1], [2], []])
