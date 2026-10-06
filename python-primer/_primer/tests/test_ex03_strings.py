"""Tests the lesson notebook calls with check(...). You never need to open this."""

from check import eq


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
