"""Tests the lesson notebook calls with check(...). You never need to open this."""

from check import eq


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
