"""Concatenation"""

__author__ = "730741513"

# Globals
word1: str = "happy"
word2: str = "tuesday"


def concat(word1: str, word2: str) -> str:
    """Concatenate word1 and word2"""
    return word1 + word2


if __name__ == "__main__":
    # Function Call
    print(concat(word1, word2))
