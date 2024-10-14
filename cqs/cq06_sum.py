"""Summing the elements of a list using different loops"""

__author__ = "730741513"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all floats in list using while loop."""  # Initialize local variables
    index: int = 0
    result: float = 0.0

    while index < len(vals):
        result += vals[index]
        index += 1

    return result


def f_sum(vals: list[float]) -> float:
    """Returns sum of floats using for loop."""

    result: float = 0.0

    # Less code and accomplishes the same thing
    for i in vals:
        # i represents the item of the list
        result += i

    return result


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of floats using for loop with range."""

    result: float = 0.0

    # For all numbers between 0 and not including the len of the list
    for i in range(0, len(vals)):
        result += vals[i]

    return result
