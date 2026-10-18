import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_basic_merge():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_empty_list_on_left():
    assert merge_sorted_lists([], [2, 4, 6]) == [2, 4, 6]


def test_duplicate_values_are_kept():
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_original_lists_are_not_modified():
    left = [1, 3]
    right = [2, 4]
    result = merge_sorted_lists(left, right)
    assert result == [1, 2, 3, 4]
    assert left == [1, 3]
    assert right == [2, 4]
