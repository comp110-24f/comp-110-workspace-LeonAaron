"""Finds max value of list."""

__author__ = "730741513"


def find_and_remove_max(input_list: list[int]) -> int:
    """Returns largest num in input_list and removes all instances of num."""

    # Checks if list is empty
    if len(input_list) == 0:
        return -1

    max: int = input_list[0]

    # Find max value
    for item in input_list:
        if item > max:
            max = item

    index: int = 0

    # Removes all instances of max:
    while index < len(input_list):
        if input_list[index] == max:
            input_list.pop(index)
        # Incriment index
        index += 1

    return max
