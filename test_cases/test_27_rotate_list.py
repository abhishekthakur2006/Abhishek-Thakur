import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_right_rotation():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_negative_k_rotates_left():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_large_k_wraps_around():
    assert rotate_list([1, 2, 3, 4, 5], 12) == [4, 5, 1, 2, 3]


def test_empty_list():
    assert rotate_list([], 3) == []
