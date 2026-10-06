"""07 · Built-ins, itertools, math, bits. Replace each `raise NotImplementedError` and run:
python3 ex07_builtins_math_bits.py"""
import math
from itertools import accumulate, combinations, groupby
from _check import eq


def single_number(nums: list) -> int:
    """LeetCode 136: every value appears twice except one. O(n) time, O(1) space, XOR."""
    raise NotImplementedError


def hamming_weight(n: int) -> int:
    """LeetCode 191 for n >= 0, using the x & (x - 1) trick in a loop (no bin(), no bit_count())."""
    raise NotImplementedError


def is_power_of_two(n: int) -> bool:
    """LeetCode 231 in one line of bit logic. Careful with 0 and negatives."""
    raise NotImplementedError


def range_sums(nums: list, queries: list) -> list:
    """For each (i, j) in queries, the sum of nums[i..j] inclusive.
    Build the prefix array once with accumulate(..., initial=0); each query is O(1)."""
    raise NotImplementedError


def count_pairs_with_sum(nums: list, target: int) -> int:
    """Number of index pairs i < j with nums[i] + nums[j] == target, using combinations().
    (O(n^2); fine here. You'd use a hash map for big inputs.)"""
    raise NotImplementedError


def longest_run(s: str) -> tuple:
    """(char, length) of the longest run of identical consecutive characters, using groupby.
    Earliest run wins ties. Return ('', 0) for an empty string."""
    raise NotImplementedError


def gcd_of_list(nums: list) -> int:
    """GCD of all numbers in a non-empty list, using math.gcd."""
    raise NotImplementedError


def ceil_div(a: int, b: int) -> int:
    """Ceiling of a / b for a >= 0, b > 0 using only integer operations (no math.ceil, no /)."""
    raise NotImplementedError


def to_signed32(x: int) -> int:
    """Interpret the low 32 bits of x as a signed 32-bit integer.
    to_signed32(0xFFFFFFFF) == -1, to_signed32(5) == 5, to_signed32(2**32 + 7) == 7."""
    raise NotImplementedError


# ------------------------------------------------------------------ tests

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


if __name__ == "__main__":
    from _check import run
    run(globals())
