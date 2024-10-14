"""More list utility functions."""

__author__ = "730741513"


def only_evens(input_list: list[int]) -> list[int]:
    """Returns list of even values from input_list."""
    # Initialize empty list
    even_list: list[int] = []

    # Checks if item is even
    for item in input_list:
        if item % 2 == 0:
            even_list.append(item)

    return even_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates list between start and end index - 1."""

    output_list: list[int] = []

    # Prevents errors
    if start_index < 0:
        start_index = 0
    if end_index > len(input_list):
        end_index = len(input_list)

    # Return empty list in odd conditions
    if len(input_list) == 0 or start_index >= len(input_list) or end_index <= 0:
        return output_list

    # Use the range function to disinclued end_index
    for index in range(start_index, end_index):
        output_list.append(input_list[index])

    return output_list


def add_at_index(input_list: list[int], element: int, index: int) -> None:
    """Places emement at index, mutates list."""

    # Raises error if index out of range
    if index > len(input_list) or index < 0:
        raise IndexError("Index is out of bounds for the input list")

    second_half_list: list[int] = []

    # Separates list into two halves, only if index is less that input list length
    if index < len(input_list):
        for i in range(index, len(input_list)):
            second_half_list.append(input_list.pop(i))

    input_list.append(element)

    # Remerges lists
    for item in second_half_list:
        input_list.append(item)

    return None
