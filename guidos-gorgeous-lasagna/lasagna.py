"""Module providingFunctions for working with lasagna."""
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(actual_bake_time):
    """Return bake time remaining.
    This function takes the time spent and calculates
    how much time is remaining for baking the lasagna.
    """
    return EXPECTED_BAKE_TIME - actual_bake_time


def preparation_time_in_minutes(layers):
    """
    Return preparation time in minutes.
    This function takes one number representing the number of layers and calculates
    the total of preparation time in minutes.
    """
    return layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
