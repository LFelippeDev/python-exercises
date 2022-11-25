"""Module for perfect numbers."""


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")

    aliquot_sum = 0
    if number % 2 == 0:
        limit_range = (number / 2) + 1
    else:
        limit_range = (number / 2) - 0.5

    limit_range = int(limit_range)

    for divider in range(1, limit_range):
        if number % divider == 0:
            aliquot_sum += divider

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"
