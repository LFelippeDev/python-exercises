"""Module responsible for Armstrong Numbers exercise solution."""


def is_armstrong_number(number):
    """Return True if number is an Armstrong number, False otherwise."""
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))
