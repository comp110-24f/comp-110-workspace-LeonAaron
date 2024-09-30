"""Coordinates display"""

__author__ = "730741513"


def get_coords(xs: str, ys: str) -> None:
    """Prints formatted pairs of each character inputed"""
    # Nested while loop (inner and outer index)

    x_index: int = 0
    while x_index < len(xs):
        coordinate1: str = xs[x_index]

        # Resets Y_index with every loop
        y_index: int = 0
        while y_index < len(ys):
            coordinate2: str = ys[y_index]
            # Output coordinates on terminal
            print(f"({coordinate1},{coordinate2})")

            # Incriment y_index
            y_index += 1

        x_index += 1
