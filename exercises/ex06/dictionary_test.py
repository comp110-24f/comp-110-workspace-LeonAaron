"""Test dictionary file."""

from exercises.ex06.dictionary import invert, count, alphabetizer


def test_invert_return_value() -> None:
    """Should invert the values and keys."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_count_return_value() -> None:
    """Output dictionery with keys from list items corresponding with values of their count."""
    assert count(["r", "r", "k"]) == {"r": 2, "k": 1}


def test_alphabetizer_return_value() -> None:
    """Should alphabetize list in dictionary with keys as letter and values in list."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {
        "c": ["cat", "car"],
        "a": ["apple", "angry"],
        "b": ["boy", "bad"],
    }
