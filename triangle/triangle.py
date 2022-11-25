"""Module return the type of triangle given the length of its sides."""


def is_valid_triangle(sides):
    """ Return True if the triangle is valid, False otherwise. """

    for side in sides:
        if side == 0:
            return False

    if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
        return False
    return True


def equilateral(sides):
    """ Return True if the triangle is equilateral, False otherwise. """
    if not is_valid_triangle(sides):
        return False

    for side in sides:
        if side != sides[0]:
            return False
    return True


def isosceles(sides):
    """ Return True if the triangle is isosceles, False otherwise. """
    if not is_valid_triangle(sides):
        return False

    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    return False


def scalene(sides):
    """ Return True if the triangle is scalene, False otherwise. """
    if not is_valid_triangle(sides):
        return False

    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    return False
