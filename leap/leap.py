"""Module to test leap year functionality"""


def leap_year(year):
    """year is a leap year if it is divisible by 4"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
