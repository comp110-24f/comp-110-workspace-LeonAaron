"""Classes Challenge Question."""

from __future__ import annotations

__author__ = "730741513"


class Point:
    # List attributes
    x: float
    y: float

    # Include self for initialization, attribute values depend on input
    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Updates x and y attributes."""
        # Self.attribute
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creation of new object from class."""
        return Point(self.x * factor, self.y * factor)
