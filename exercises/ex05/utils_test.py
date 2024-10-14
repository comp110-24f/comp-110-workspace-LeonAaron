"""Testing for utils.py"""

__author__ = "730741513"


# import functions
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_return_value() -> None:
    """only_evens should return a list containing the even values in input_list."""
    input: list[int] = [1, 2, 3, 4]
    assert only_evens(input) == [2, 4]


def test_only_evens_behavior() -> None:
    """only_evens should not change input_list."""
    input: list[int] = [1, 2, 3, 4]
    only_evens(input)
    assert input == [1, 2, 3, 4]


def test_only_evens_edge_case() -> None:
    """If and empty list is inputted, an empty list should be returned."""
    assert only_evens([]) == []


def test_sub_return_value() -> None:
    """sub should return a list from start_index to end_index - 1."""
    input: list[int] = [1, 3, 4, 5, 7]
    assert sub(input, 1, 4) == [3, 4, 5]


def test_sub_behavior() -> None:
    """sub should not alter input."""
    input: list[int] = [1, 2]
    sub(input, 0, 2)
    assert input == [1, 2]


def test_sub_edge_case() -> None:
    """When start index is larger then len(input), an empty list is output."""
    input: list[int] = [3, 5, 7, 2]
    assert sub(input, 7, 9) == []


def test_add_at_index_return_value() -> None:
    """add_at_index should return None"""
    assert add_at_index([1, 3], 0, 1) == None


def test_add_at_index_behavior() -> None:
    """add_at_index should put element into specified index in input_list."""
    input: list[int] = [1, 3]
    add_at_index(input, 2, 1)
    assert input == [1, 2, 3]


def test_add_at_index_edge_case() -> None:
    """If empty list is provided with valid index, output a single value list"""
    input: list[int] = []
    add_at_index(input, 3, 0)
    assert input == [3]
