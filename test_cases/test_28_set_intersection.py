import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_basic_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_empty_intersection():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_identical_sets():
    assert set_intersection({1, 2, 3}, {3, 2, 1}) == {1, 2, 3}


def test_non_overlapping_with_duplicates():
    assert set_intersection({1, 1, 2}, {2, 3, 4}) == {2}
