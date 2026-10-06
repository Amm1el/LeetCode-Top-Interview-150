"""Tests the lesson notebook calls with check(...). You never need to open this."""

from check import eq


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
