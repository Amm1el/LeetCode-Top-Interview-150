# ══════════════════════════════════════════════════════════════════════
# LESSON 07 · BUILT-INS, MATH, BITS
# Notes: ../07-builtins-math-bits.md
#
# 1. Write your code where each `raise NotImplementedError` is.
# 2. Ctrl+Shift+B runs the tests. Bottom panel: ok / FAIL / TODO.
# 3. Repeat until everything says ok.
#
# (Tests live in tests/test_ex07_builtins_math_bits.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════

import math
from itertools import accumulate, combinations, groupby


# ══════════════════════════════════════════════════════════════════════
# 1. single_number                                          LeetCode 136
# ──────────────────────────────────────────────────────────────────────
# Every value appears twice except one. O(n) time, O(1) space, XOR.
#
#   single_number([4, 1, 2, 1, 2])  ->  4
#   single_number([-3])             ->  -3
# ══════════════════════════════════════════════════════════════════════
def single_number(nums: list) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 2. hamming_weight                                         LeetCode 191
# ──────────────────────────────────────────────────────────────────────
# Solve it for n >= 0, using the x & (x - 1) trick in a loop (no
# bin(), no bit_count()).
#
#   hamming_weight(11)   ->  3
#   hamming_weight(128)  ->  1
#   hamming_weight(0)    ->  0
# ══════════════════════════════════════════════════════════════════════
def hamming_weight(n: int) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 3. is_power_of_two                                        LeetCode 231
# ──────────────────────────────────────────────────────────────────────
# Solve it in one line of bit logic. Careful with 0 and negatives.
#
#   is_power_of_two(16)  ->  True
#   is_power_of_two(3)   ->  False
#   is_power_of_two(0)   ->  False
# ══════════════════════════════════════════════════════════════════════
def is_power_of_two(n: int) -> bool:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 4. range_sums
# ──────────────────────────────────────────────────────────────────────
# For each (i, j) in queries, the sum of nums[i..j] inclusive. Build
# the prefix array once with accumulate(..., initial=0); each query is
# O(1).
#
#   range_sums([-2, 0, 3, -5, 2, -1], [(0, 2), (2, 5)])
#     ->  [1, -1]
# ══════════════════════════════════════════════════════════════════════
def range_sums(nums: list, queries: list) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 5. count_pairs_with_sum
# ──────────────────────────────────────────────────────────────────────
# Number of index pairs i < j with nums[i] + nums[j] == target, using
# combinations(). (O(n^2); fine here. You'd use a hash map for big
# inputs.)
#
#   count_pairs_with_sum([1, 5, 7, -1, 5], 6)  ->  3
#   count_pairs_with_sum([], 1)                ->  0
# ══════════════════════════════════════════════════════════════════════
def count_pairs_with_sum(nums: list, target: int) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 6. longest_run
# ──────────────────────────────────────────────────────────────────────
# (char, length) of the longest run of identical consecutive
# characters, using groupby. Earliest run wins ties. Return ('', 0)
# for an empty string.
#
#   longest_run('aabbbcdd')  ->  ('b', 3)
#   longest_run('abcc')      ->  ('c', 2)
#   longest_run('xxyy')      ->  ('x', 2)
# ══════════════════════════════════════════════════════════════════════
def longest_run(s: str) -> tuple:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 7. gcd_of_list
# ──────────────────────────────────────────────────────────────────────
# GCD of all numbers in a non-empty list, using math.gcd.
#
#   gcd_of_list([12, 18, 30])  ->  6
#   gcd_of_list([7])           ->  7
# ══════════════════════════════════════════════════════════════════════
def gcd_of_list(nums: list) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 8. ceil_div
# ──────────────────────────────────────────────────────────────────────
# Ceiling of a / b for a >= 0, b > 0 using only integer operations (no
# math.ceil, no /).
#
#   ceil_div(7, 3)  ->  3
#   ceil_div(9, 3)  ->  3
#   ceil_div(0, 3)  ->  0
# ══════════════════════════════════════════════════════════════════════
def ceil_div(a: int, b: int) -> int:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 9. to_signed32
# ──────────────────────────────────────────────────────────────────────
# Interpret the low 32 bits of x as a signed 32-bit integer.
# to_signed32(0xFFFFFFFF) == -1, to_signed32(5) == 5,
# to_signed32(2**32 + 7) == 7.
#
#   to_signed32(4294967295)   ->  -1
#   to_signed32(5)            ->  5
#   to_signed32(2 ** 32 + 7)  ->  7
# ══════════════════════════════════════════════════════════════════════
def to_signed32(x: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
