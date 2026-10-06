"""01 · Basics. Replace each `raise NotImplementedError`. Ctrl+Shift+B runs the tests."""
from _check import eq


def reverse_int(x: int) -> int:
    """Reverse the digits of x, keeping the sign. Return 0 if the result is outside
    the signed 32-bit range [-2**31, 2**31 - 1]. Use // and %, not strings.
    (Watch out: // and % on negatives don't behave like Java.)"""
    raise NotImplementedError


def max_and_min(nums: list) -> tuple:
    """Return (largest, smallest) without using max() or min().
    Return (None, None) for an empty list."""
    raise NotImplementedError


def fib(n: int) -> int:
    """fib(0) = 0, fib(1) = 1. Iterative, O(1) space, using tuple assignment."""
    raise NotImplementedError


def count_down_evens(n: int) -> list:
    """All even numbers from n down to 0 inclusive, largest first, using a single range()."""
    raise NotImplementedError


def first_index_of_zero(nums: list):
    """Index of the first 0 in nums, or None if there isn't one. Don't use .index().
    Careful: the answer can be 0, which is falsy."""
    raise NotImplementedError


# ------------------------------------------------------------------ tests

def test_reverse_int():
    eq(reverse_int(123), 321)
    eq(reverse_int(-123), -321)
    eq(reverse_int(120), 21)
    eq(reverse_int(0), 0)
    eq(reverse_int(1534236469), 0, "overflow should return 0")


def test_max_and_min():
    eq(max_and_min([3, -1, 7, 7, 0]), (7, -1))
    eq(max_and_min([-5]), (-5, -5))
    eq(max_and_min([]), (None, None))


def test_fib():
    eq([fib(i) for i in range(10)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    eq(fib(90), 2880067194370816120)


def test_count_down_evens():
    eq(count_down_evens(7), [6, 4, 2, 0])
    eq(count_down_evens(8), [8, 6, 4, 2, 0])
    eq(count_down_evens(0), [0])


def test_first_index_of_zero():
    eq(first_index_of_zero([0, 1, 0]), 0)
    eq(first_index_of_zero([4, 5, 0]), 2)
    eq(first_index_of_zero([1, 2]), None)


if __name__ == "__main__":
    from _check import run
    run(globals())
