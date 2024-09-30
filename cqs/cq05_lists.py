"""Mutating Functions"""

__author__ = "730741513"

# Globals
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(input_list: list[int], append_num: int) -> None:
    """Appends append_num to input_list"""
    input_list.append(append_num)


def double(input_list: list[int]) -> None:
    """Multiplies every element in input_list by 2"""

    # initialize index
    index: int = 0

    while index < len(input_list):
        input_list[index] = input_list[index] * 2
        # incriment index
        index += 1


double(input_list=list_2)
print(list_1)
print(list_2)
