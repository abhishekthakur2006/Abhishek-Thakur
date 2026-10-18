import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_basic_anagram():
    assert is_anagram("listen", "silent") is True


def test_case_and_spaces_are_ignored():
    assert is_anagram("A gentleman", "elegant man") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_different_lengths():
    assert is_anagram("abc", "abcd") is False
