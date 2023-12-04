from typing import Final

# TODO: Mypy currently does not support the `type` statement from PEP 695 which
# was added in Python 3.12. However, Mypy also does not support suppressing errors
# for this either. So currently, this line will generate a [valid-type] Mypy error.
# For more information, see GitHub issue https://github.com/python/mypy/issues/16607.
type Number = int | float
"""Represents a scalar number that is either an integer or float"""

# Constant for use in comparing floats within the ray tracer.
# Marking this as Final disallows any reassignment.
# See: https://docs.python.org/3/library/typing.html#typing.Final
EPSILON: Final[float] = 0.00001

def compare_float(x: Number, y: Number) -> bool:
    """Compares two numbers by checking that their absolute difference is
    less than or equal to epsilon = 0.00001
    """
    return abs(x - y) <= EPSILON

def clamp_number(number: Number, min: Number, max: Number) -> Number:
    """Clamps a number to be in the range [min, max]"""
    if number >= max:
        return max
    elif number <= min:
        return min
    else:
        return number
