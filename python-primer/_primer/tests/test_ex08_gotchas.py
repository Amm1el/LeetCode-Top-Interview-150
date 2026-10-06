"""Tests the lesson notebook calls with check(...). You never need to open this."""

from check import eq


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
