# ══════════════════════════════════════════════════════════════════════
# LESSON 02 · LISTS
# Notes: ../02-lists.md
#
# 1. Write your code where each `raise NotImplementedError` is.
# 2. Ctrl+Shift+B runs the tests. Bottom panel: ok / FAIL / TODO.
# 3. Repeat until everything says ok.
#
# (Tests live in tests/test_ex02_lists.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════
# 1. rotate_in_place                                        LeetCode 189
# ──────────────────────────────────────────────────────────────────────
# Rotate nums right by k steps IN PLACE. Return nothing. k can be
# larger than len(nums). One line with slice assignment is fine.
#
#   nums = [1, 2, 3, 4, 5, 6, 7]
#   rotate_in_place(nums, 3)
#   nums is now [5, 6, 7, 1, 2, 3, 4], and the function returns None
# ══════════════════════════════════════════════════════════════════════
def rotate_in_place(nums: list, k: int) -> None:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 2. make_grid
# ──────────────────────────────────────────────────────────────────────
# rows x cols grid where every row is an independent list.
#
#   make_grid(3, 2)  ->  [[0, 0], [0, 0], [0, 0]]
#   changing g[0][0] must not change g[1][0]
# ══════════════════════════════════════════════════════════════════════
def make_grid(rows: int, cols: int, fill=0) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 3. sort_people
# ──────────────────────────────────────────────────────────────────────
# people is a list of (name, age). Return a new list sorted by age
# descending, then name ascending. Use one sorted() call with a key.
#
#   sort_people([("bo", 30), ("al", 25), ("cy", 30)])
#     ->  [("bo", 30), ("cy", 30), ("al", 25)]
# ══════════════════════════════════════════════════════════════════════
def sort_people(people: list) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 4. prefix_sums
# ──────────────────────────────────────────────────────────────────────
# Return p with len(nums) + 1 entries where p[i] = sum(nums[:i]). Then
# sum(nums[i:j]) == p[j] - p[i]. Build it in O(n).
#
#   prefix_sums([])  ->  [0]
# ══════════════════════════════════════════════════════════════════════
def prefix_sums(nums: list) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 5. positive_positions
# ──────────────────────────────────────────────────────────────────────
# List of (index, value) for every value > 0, using enumerate in a
# comprehension.
#
#   positive_positions([0, 5, -2, 7])  ->  [(1, 5), (3, 7)]
# ══════════════════════════════════════════════════════════════════════
def positive_positions(nums: list) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 6. transpose
# ──────────────────────────────────────────────────────────────────────
# Transpose a rectangular matrix, returning a list of lists. Try
# zip(*matrix).
#
#   transpose([[1, 2, 3], [4, 5, 6]])  ->  [[1, 4], [2, 5], [3, 6]]
# ══════════════════════════════════════════════════════════════════════
def transpose(matrix: list) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 7. all_subsets_wrong_vs_right
# ──────────────────────────────────────────────────────────────────────
# Return every subset of nums (order of subsets: as produced below).
# Fill in the one line marked FIX so the result is correct.
#
#   all_subsets_wrong_vs_right([1, 2])  ->  [[1, 2], [1], [2], []]
# ══════════════════════════════════════════════════════════════════════
def all_subsets_wrong_vs_right(nums: list) -> list:
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


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
