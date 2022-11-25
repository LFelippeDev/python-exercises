"""Module for raindrops exercise"""


def convert(number):
    """Returns a string with the raindrop sounds"""
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    rain_drop = ""
    if number % 3 == 0:
        rain_drop += "Pling"
    if number % 5 == 0:
        rain_drop += "Plang"
    if number % 7 == 0:
        rain_drop += "Plong"
    return rain_drop
