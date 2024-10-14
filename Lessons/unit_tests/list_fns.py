"""Functions for unit test."""


def get_first(input_list: list[str]) -> str:
    """Return first element of list."""
    if len(input_list) == 0:
        return ""
    return input_list[0]


def remove_first(input_list: list[str]) -> None:
    """Remove first element of list."""

    input_list.pop(0)


def get_and_remove_first(input_list: list[str]) -> str:
    """Returns and removes the first element of the list"""

    return input_list.pop(0)
