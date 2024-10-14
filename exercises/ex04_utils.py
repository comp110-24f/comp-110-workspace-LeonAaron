"""Practice utilizing lists."""

__author__ = "730741513"


def all(num_list: list[int], num: int) -> bool:
    """Shows if all the numbers in num_list are equal to num."""
    index: int = 0

    # Returns false if num != list item
    while index < len(num_list):
        if num_list[index] != num:
            return False
        index += 1

    # Returns false if empty list
    if len(num_list) == 0:
        return False

    return True


def max(num_list: list[int]) -> int:
    """Returns largert num in num_list."""
    # If list is empty, raise a value error
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")

    # Sets max as equal to first list value, start at index 1
    index: int = 1
    max_num: int = num_list[0]

    # Determines max of entire list
    while index < len(num_list):
        if num_list[index] > max_num:
            max_num = num_list[index]
        index += 1

    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if every element as every index is equal."""
    # Returns False if lists are different length
    if len(list1) != len(list2):
        return False

    index: int = 0

    # If values at same index are different return False
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Appends list2 to list1."""
    index: int = 0

    # Loops through list 2, appends all values to list 1
    while index < len(list2):
        list1.append(list2[index])
        index += 1

    return None
