""""Practive with while loops to iterate through string"""

__author__ = "730741513"


def num_instances(phrase: str, search_char: str) -> int:
    """Returns the count of occurences in search_char in phrase"""

    # Initialize variables
    count: int = 0
    index: int = 0

    # Goes through all letters in phrase and checks if letter == search_char
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1

    # Returns the final count value
    return count
