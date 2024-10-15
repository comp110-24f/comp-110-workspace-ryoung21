"""EX05 - 'list' Utility Functions Unit Tests"""

__author__ = "730461441"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""only_evens Tests"""


def test_only_evens_output() -> None:
    """Tests if only_evens returns desired output."""
    assert only_evens(ints=[1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens_edge_case() -> None:
    """Test that only_evens works with empty list."""
    assert only_evens(ints=[]) == []


def test_only_evens_all_odds() -> None:
    """Tests that only_evens with all odds returns empty list."""
    assert only_evens(ints=[1, 3, 5]) == []


def test_only_evens_all_evens() -> None:
    """Tests that only_evens with all evens returns identical list."""
    assert only_evens(ints=[4, 4, 4]) == [4, 4, 4]


def test_only_evens_mutation() -> None:
    """Tests that only_evens does NOT mutate the list it takes as a parameter."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5, 6]


"""sub Tests"""


def test_sub_output() -> None:
    """Tests that sub gives the desired output when index is in range"""
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]


def test_sub_mutation() -> None:
    """Tests that sub does NOT mutate the list it takes as a parameter."""
    a: list[int] = [1, 2, 3, 4]
    sub(a, 1, 3)
    assert a == [1, 2, 3, 4]


def test_sub_output_out_of_range() -> None:
    """Tests that sub alters the start and end indicies when they're out of range."""
    assert sub([1, 2, 3, 4], -1, 6) == [1, 2, 3, 4]


def test_sub_edge_case() -> None:
    """Tests if sub works with empty list"""
    assert sub([], 1, 3) == []


"""add_at_index Tests"""


def test_add_at_index_output() -> None:
    """Tests if add_at_index returns desired output."""
    a: list[int] = [1, 2, 3, 5]
    add_at_index(a, 4, 3)
    assert a == [1, 2, 3, 4, 5]


def test_add_at_index_empty_list() -> None:
    """Tests if add_at_index can mutate an empty list."""
    b: list[int] = []
    add_at_index(b, 0, 0)
    assert b == [0]


def test_add_at_index_raises_index_error():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([], 1, 1)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
