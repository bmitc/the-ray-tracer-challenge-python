from typing import Final
import math

# Constant for use in comparing floats within the ray tracer
EPSILON: Final[float] = 0.00001

def compare_float(x: float, y: float) -> bool:
    return abs(x - y) <= EPSILON
