from typing import Final
import math

type Number = int | float
"""Represents a scalar number that is either an integer or float"""

# Constant for use in comparing floats within the ray tracer
EPSILON: Final[float] = 0.00001

def compare_float(x: Number, y: Number) -> bool:
    """Compares two numbers by checking that their absolute difference is
    less than or equal to epsilon = 0.00001
    """
    return abs(x - y) <= EPSILON

def clamp_number(number: Number, min: Number, max: Number):
    """Clamps a number to be in the range [min, max]"""
    if number >= max:
        return max
    elif number <= min:
        return min
    else:
        return number
