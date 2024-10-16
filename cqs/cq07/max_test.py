"""Unit test for find_and_remove_max function."""

__author__ = "730741513"

# Be sure to import correct file
from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return_value() -> None:
    """find_and_remove_max should return max value of input list"""
    assert find_and_remove_max([1, 2, 3, 4, 5]) == 5


def test_find_and_remove_max_behavior() -> None:
    """find_and_remove_max should remove all instances of max from input_list."""
    input: list[int] = [1, 1, 5, 5, 3, 5]
    find_and_remove_max(input)
    assert input == [1, 1, 3]


def test_find_and_remove_max_edge_case() -> None:
    """If empty list as input, return -1"""
    assert find_and_remove_max([]) == -1
