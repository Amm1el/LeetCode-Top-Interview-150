"""03 · Strings. Replace each `raise NotImplementedError` and run: python3 ex03_strings.py"""
from _check import eq


def is_palindrome_alnum(s: str) -> bool:
    """LeetCode 125: ignoring case and non-alphanumeric characters, is s a palindrome?
    Do it with two indices moving inward, O(1) extra space (no building a cleaned copy)."""
    raise NotImplementedError


def reverse_words(s: str) -> str:
    """LeetCode 151: reverse the order of words; collapse any extra spaces."""
    raise NotImplementedError


def anagram_key(word: str) -> str:
    """Return a string such that two words are anagrams iff their keys are equal."""
    raise NotImplementedError


def letter_counts(s: str) -> list:
    """s is lowercase a-z. Return a 26-element list of counts using ord()."""
    raise NotImplementedError


def compress(s: str) -> str:
    """Run-length encode: 'aaabcc' -> 'a3bc2' (counts of 1 are omitted).
    Build with a list of parts and one join."""
    raise NotImplementedError


def swap_first_last(s: str) -> str:
    """Swap the first and last characters. Strings of length < 2 come back unchanged."""
    raise NotImplementedError


# ------------------------------------------------------------------ tests

def test_is_palindrome_alnum():
    eq(is_palindrome_alnum("A man, a plan, a canal: Panama"), True)
    eq(is_palindrome_alnum("race a car"), False)
    eq(is_palindrome_alnum(" "), True)
    eq(is_palindrome_alnum("0P"), False)


def test_reverse_words():
    eq(reverse_words("the sky is blue"), "blue is sky the")
    eq(reverse_words("  hello world  "), "world hello")
    eq(reverse_words("a good   example"), "example good a")


def test_anagram_key():
    eq(anagram_key("listen") == anagram_key("silent"), True)
    eq(anagram_key("ab") == anagram_key("abb"), False)
    assert isinstance(anagram_key("x"), str), "return a str"


def test_letter_counts():
    c = letter_counts("abca")
    eq(len(c), 26)
    eq(c[:3], [2, 1, 1])
    eq(sum(c), 4)


def test_compress():
    eq(compress("aaabcc"), "a3bc2")
    eq(compress("abc"), "abc")
    eq(compress(""), "")
    eq(compress("zzzzzzzzzzzz"), "z12")


def test_swap_first_last():
    eq(swap_first_last("hello"), "oellh")
    eq(swap_first_last("a"), "a")
    eq(swap_first_last(""), "")


if __name__ == "__main__":
    from _check import run
    run(globals())
