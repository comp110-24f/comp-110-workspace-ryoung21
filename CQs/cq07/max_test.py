"""cq07 - find_and_remove_max unit test"""

__author__ = "730461441"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    ints: list[int] = [1, 2, 3, 4, 3, 4]
    assert find_and_remove_max(ints) == 4


def test_find_and_remove_max_mutation() -> None:
    ints: list[int] = [1, 2, 3, 4, 3, 4]
    find_and_remove_max(ints)  # have to call function first to see if it mutates
    assert ints == [1, 2, 3, 3]


def test_find_and_remove_max_edge_case() -> None:
    ints: list[int] = []
    assert find_and_remove_max(ints) == -1
