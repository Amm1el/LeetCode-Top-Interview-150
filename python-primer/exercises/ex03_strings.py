# ══════════════════════════════════════════════════════════════════════
# LESSON 03 · STRINGS
# Notes: ../03-strings.md
#
# 1. Write your code where each `raise NotImplementedError` is.
# 2. Ctrl+Shift+B runs the tests. Bottom panel: ok / FAIL / TODO.
# 3. Repeat until everything says ok.
#
# (Tests live in tests/test_ex03_strings.py. You don't need to open them.)
# ══════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════
# 1. is_palindrome_alnum                                    LeetCode 125
# ──────────────────────────────────────────────────────────────────────
# Ignoring case and non-alphanumeric characters, is s a palindrome? Do
# it with two indices moving inward, O(1) extra space (no building a
# cleaned copy).
#
#   is_palindrome_alnum('A man, a plan, a canal: Panama')  ->  True
#   is_palindrome_alnum('race a car')                      ->  False
#   is_palindrome_alnum(' ')                               ->  True
# ══════════════════════════════════════════════════════════════════════
def is_palindrome_alnum(s: str) -> bool:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 2. reverse_words                                          LeetCode 151
# ──────────────────────────────────────────────────────────────────────
# Reverse the order of words; collapse any extra spaces.
#
#   reverse_words('the sky is blue')   ->  'blue is sky the'
#   reverse_words('  hello world  ')   ->  'world hello'
#   reverse_words('a good   example')  ->  'example good a'
# ══════════════════════════════════════════════════════════════════════
def reverse_words(s: str) -> str:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 3. anagram_key
# ──────────────────────────────────────────────────────────────────────
# Return a string such that two words are anagrams iff their keys are
# equal.
#
#   anagram_key("listen") == anagram_key("silent")  ->  True
#   anagram_key("ab") == anagram_key("abb")         ->  False
# ══════════════════════════════════════════════════════════════════════
def anagram_key(word: str) -> str:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 4. letter_counts
# ──────────────────────────────────────────────────────────────────────
# s is lowercase a-z. Return a 26-element list of counts using ord().
#
#   letter_counts("abca")  ->  [2, 1, 1, 0, 0, ..., 0]   (26 numbers)
# ══════════════════════════════════════════════════════════════════════
def letter_counts(s: str) -> list:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 5. compress
# ──────────────────────────────────────────────────────────────────────
# Run-length encode: 'aaabcc' -> 'a3bc2' (counts of 1 are omitted).
# Build with a list of parts and one join.
#
#   compress('aaabcc')  ->  'a3bc2'
#   compress('abc')     ->  'abc'
#   compress('')        ->  ''
# ══════════════════════════════════════════════════════════════════════
def compress(s: str) -> str:
    raise NotImplementedError


# ══════════════════════════════════════════════════════════════════════
# 6. swap_first_last
# ──────────────────────────────────────────────────────────────────────
# Swap the first and last characters. Strings of length < 2 come back
# unchanged.
#
#   swap_first_last('hello')  ->  'oellh'
#   swap_first_last('a')      ->  'a'
#   swap_first_last('')       ->  ''
# ══════════════════════════════════════════════════════════════════════
def swap_first_last(s: str) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    from _check import run_tests
    run_tests(__file__)
