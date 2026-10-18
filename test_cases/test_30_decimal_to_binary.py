import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_basic_decimal_conversion():
    assert decimal_to_binary(10) == "1010"


def test_zero_value():
    assert decimal_to_binary(0) == "0"


def test_odd_number():
    assert decimal_to_binary(5) == "101"


def test_negative_number_raises_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-7)
