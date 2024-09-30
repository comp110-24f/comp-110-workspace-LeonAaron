"""Visualize"""

__author__ = "730741513"

# import statment
from cqs.cq04.coordinates import get_coords


# Globals
x: str = "123"
y: str = "abc"


# Include entire path when importing
from cqs.cq04.concatenation import concat


# Call function imported from different module
print(concat(word1=x, word2=y))
get_coords(xs=x, ys=y)
