"""Dictionary Exercise."""

__author__ = "730741513"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values from input dictionary."""
    inverted: dict[str, str] = {}

    for key in input:
        # Checks if the value is already a key in inverted
        if input[key] in inverted:
            raise KeyError
        else:
            inverted[input[key]] = key
    return inverted


def favorite_color(input: dict[str, str]) -> str:
    """Returns the color that appears the most frequently."""
    popular_color: str = ""
    max_count: int = 0

    # Nest for loops to go through values and then count them up
    for key in input:
        count: int = 0
        color: str = input[key]
        for key in input:
            if input[key] == color:
                count += 1
        # Only if the count is greater, max_count = count
        if count > max_count:
            max_count = count
            popular_color = color
    return popular_color


def count(input: list[str]) -> dict[str, int]:
    """Output dictionary with values representing count and keys repres."""
    output: dict[str, int] = {}

    # Determines whether key should be created or modifies
    for item in input:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1

    return output


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Output- each key is a unique letter in alphabet where each list begins."""
    output: dict[str, list[str]] = {}
    used_letters: list[str] = []

    for item in input:
        # Initiates variable for each letter
        lowercase_letter: str = item[0].lower()
        letter_list: list[str] = []

        # makes sure letter was not already used
        if lowercase_letter not in used_letters:
            # If the first letter is the same, add object to letter_list
            for object in input:
                if lowercase_letter == object[0].lower():
                    letter_list.append(object)

        output[lowercase_letter] = letter_list
    return output


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Modify input to add students to values of day."""

    # If the day already in dictionary, append value to the student list
    if day in input and student not in input[day]:
        input[day] += [student]
    else:
        # Make sure it student is shown as list
        input[day] = [student]

    return None
