"""Module responsible for Difference of Squares exercise solution."""


def square_of_sum(number):
    """ Return the square of the sum of the first N natural numbers.
    """
    return sum(range(1, number+1))**2


def sum_of_squares(number):
    """ Return the sum of the squares of the first N natural numbers.
    """
    return sum(digit**2 for digit in range(1, number+1))


def difference_of_squares(number):
    """ Return the difference between the square of the sum of the first N natural
    """
    return square_of_sum(number) - sum_of_squares(number)
