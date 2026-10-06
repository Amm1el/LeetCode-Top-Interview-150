# ══════════════════════════════════════════════════════════════════════
# LESSON 01 · BASICS
# Notes: ../01-basics.md
#
# 1. Write your code where each `raise NotImplementedError` is.
# 2. Ctrl+Shift+B runs the tests. Bottom panel: ok / FAIL / TODO.
# 3. Repeat until everything says ok.
#
# (Tests live in tests/test_ex01_basics.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════
# 1. reverse_int
# ──────────────────────────────────────────────────────────────────────
# Reverse the digits of x, keeping the sign. Return 0 if the result is
# outside the signed 32-bit range [-2**31, 2**31 - 1]. Use // and %,
# not strings. (Watch out: // and % on negatives don't behave like
# Java.)
#
#   reverse_int(123)   ->  321
#   reverse_int(-123)  ->  -321
#   reverse_int(120)   ->  21
# ══════════════════════════════════════════════════════════════════════
def reverse_int(x: int) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 2. max_and_min
# ──────────────────────────────────────────────────────────────────────
# Return (largest, smallest) without using max() or min(). Return
# (None, None) for an empty list.
#
#   max_and_min([3, -1, 7, 7, 0])  ->  (7, -1)
#   max_and_min([-5])              ->  (-5, -5)
#   max_and_min([])                ->  (None, None)
# ══════════════════════════════════════════════════════════════════════
def max_and_min(nums: list) -> tuple:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 3. fib
# ──────────────────────────────────────────────────────────────────────
# fib(0) = 0, fib(1) = 1. Iterative, O(1) space, using tuple
# assignment.
#
#   fib(0)   ->  0
#   fib(1)   ->  1
#   fib(10)  ->  55
# ══════════════════════════════════════════════════════════════════════
def fib(n: int) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 4. count_down_evens
# ──────────────────────────────────────────────────────────────────────
# All even numbers from n down to 0 inclusive, largest first, using a
# single range().
#
#   count_down_evens(7)  ->  [6, 4, 2, 0]
#   count_down_evens(8)  ->  [8, 6, 4, 2, 0]
#   count_down_evens(0)  ->  [0]
# ══════════════════════════════════════════════════════════════════════
def count_down_evens(n: int) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 5. first_index_of_zero
# ──────────────────────────────────────────────────────────────────────
# Index of the first 0 in nums, or None if there isn't one. Don't use
# .index(). Careful: the answer can be 0, which is falsy.
#
#   first_index_of_zero([0, 1, 0])  ->  0
#   first_index_of_zero([4, 5, 0])  ->  2
#   first_index_of_zero([1, 2])     ->  None
# ══════════════════════════════════════════════════════════════════════
def first_index_of_zero(nums: list):
    raise NotImplementedError


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
