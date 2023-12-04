"""A collection of utility functions"""

from typing import Final

# Constant for use in comparing floats within the ray tracer.
# Marking this as Final disallows any reassignment.
# See: https://docs.python.org/3/library/typing.html#typing.Final
EPSILON: Final[float] = 0.00001


def compare_float(x: int | float, y: int | float) -> bool:
    """Compares two numbers by checking that their absolute difference is
    less than or equal to epsilon = 0.00001
    """
    return abs(x - y) <= EPSILON


def clamp_number(number: int | float, minimum: int | float, maximum: int | float) -> int | float:
    """Clamps a number to be in the range [minimum, maximum]"""
    if number >= maximum:
        return maximum
    elif number <= minimum:
        return minimum
    else:
        return number
