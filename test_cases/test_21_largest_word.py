import importlib

module = importlib.import_module("21_largest_word")
largest_word = module.largest_word


def test_basic_case():
    assert largest_word("I love programming") == "programming"


def test_punctuation_is_ignored():
    assert largest_word("Hello, world! Python is great.") == "Python"


def test_tie_returns_first_word():
    assert largest_word("cat dog") == "cat"


def test_empty_sentence_returns_empty_string():
    assert largest_word("") == ""
