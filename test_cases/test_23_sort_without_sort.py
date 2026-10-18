import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_basic_sort():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty_list():
    assert bubble_sort([]) == []


def test_single_item_list():
    assert bubble_sort([42]) == [42]


def test_original_list_is_not_modified():
    numbers = [7, 1, 3]
    result = bubble_sort(numbers)
    assert result == [1, 3, 7]
    assert numbers == [7, 1, 3]
