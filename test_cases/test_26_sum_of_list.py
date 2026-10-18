import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_basic_sum():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_negative_values():
    assert sum_of_list([5, -2, 3]) == 6


def test_larger_set():
    assert sum_of_list([10, 20, 30]) == 60
