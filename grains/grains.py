
"""Module for calculating grains of wheat on a chessboard."""


def square(number):
    """Return grains in square."""
    if 0 < number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """Return total grains on board."""
    return sum(square(number) for number in range(1, 65))
