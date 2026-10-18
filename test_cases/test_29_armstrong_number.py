import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_basic_armstrong_number():
    assert is_armstrong(153) is True


def test_non_armstrong_number():
    assert is_armstrong(123) is False


def test_zero_is_armstrong():
    assert is_armstrong(0) is True


def test_negative_number_is_false():
    assert is_armstrong(-153) is False
