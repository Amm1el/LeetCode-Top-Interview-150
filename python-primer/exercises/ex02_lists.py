"""02 · Lists. Replace each `raise NotImplementedError` and run: python3 ex02_lists.py"""
from _check import eq


def rotate_in_place(nums: list, k: int) -> None:
    """Rotate nums right by k steps IN PLACE (LeetCode 189). Return nothing.
    k can be larger than len(nums). One line with slice assignment is fine."""
    raise NotImplementedError


def make_grid(rows: int, cols: int, fill=0) -> list:
    """rows x cols grid where every row is an independent list."""
    raise NotImplementedError


def sort_people(people: list) -> list:
    """people is a list of (name, age). Return a new list sorted by age descending,
    then name ascending. Use one sorted() call with a key."""
    raise NotImplementedError


def prefix_sums(nums: list) -> list:
    """Return p with len(nums) + 1 entries where p[i] = sum(nums[:i]).
    Then sum(nums[i:j]) == p[j] - p[i]. Build it in O(n)."""
    raise NotImplementedError


def positive_positions(nums: list) -> list:
    """List of (index, value) for every value > 0, using enumerate in a comprehension."""
    raise NotImplementedError


def transpose(matrix: list) -> list:
    """Transpose a rectangular matrix, returning a list of lists. Try zip(*matrix)."""
    raise NotImplementedError


def all_subsets_wrong_vs_right(nums: list) -> list:
    """Return every subset of nums (order of subsets: as produced below).
    Fill in the one line marked FIX so the result is correct."""
    res, path = [], []

    def backtrack(i):
        if i == len(nums):
            raise NotImplementedError  # FIX: record the current path correctly
            return
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
        backtrack(i + 1)

    backtrack(0)
    return res


# ------------------------------------------------------------------ tests

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


if __name__ == "__main__":
    from _check import run
    run(globals())
