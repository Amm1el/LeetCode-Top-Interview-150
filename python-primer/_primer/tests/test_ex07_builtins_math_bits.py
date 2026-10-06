"""Tests the lesson notebook calls with check(...). You never need to open this."""

from check import eq


def test_single_number():
    eq(single_number([4, 1, 2, 1, 2]), 4)
    eq(single_number([-3]), -3)


def test_hamming_weight():
    eq(hamming_weight(11), 3)
    eq(hamming_weight(128), 1)
    eq(hamming_weight(0), 0)
    eq(hamming_weight(2**31 - 1), 31)


def test_is_power_of_two():
    eq([is_power_of_two(n) for n in (1, 16, 3, 0, -8)], [True, True, False, False, False])


def test_range_sums():
    eq(range_sums([-2, 0, 3, -5, 2, -1], [(0, 2), (2, 5), (0, 5)]), [1, -1, -3])


def test_count_pairs_with_sum():
    eq(count_pairs_with_sum([1, 5, 7, -1, 5], 6), 3)
    eq(count_pairs_with_sum([], 1), 0)


def test_longest_run():
    eq(longest_run("aabbbcdd"), ("b", 3))
    eq(longest_run("abcc"), ("c", 2))
    eq(longest_run("xxyy"), ("x", 2))
    eq(longest_run(""), ("", 0))


def test_gcd_of_list():
    eq(gcd_of_list([12, 18, 30]), 6)
    eq(gcd_of_list([7]), 7)


def test_ceil_div():
    eq([ceil_div(a, 3) for a in (0, 1, 3, 4, 9, 10)], [0, 1, 1, 2, 3, 4])


def test_to_signed32():
    eq(to_signed32(0xFFFFFFFF), -1)
    eq(to_signed32(5), 5)
    eq(to_signed32(2**32 + 7), 7)
    eq(to_signed32(0x80000000), -2**31)
