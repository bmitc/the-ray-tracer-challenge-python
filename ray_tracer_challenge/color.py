"""Color type, color constants, and helper functions"""

from __future__ import annotations
from enum import Enum
from functools import partial
import operator
from typing import Callable
from ray_tracer_challenge.utilities import clamp_number, compare_float


class Color:
    """Represents a color in terms of its red, green, and blue components.
    A value of 1.0 means that the component is fully saturated (i.e., at 100%) and a
    value of 0.0 means that the color component is not present (i.e., at 0%), but the
    various values that a color component may take on are allowed to range beyond 0.0
    and 1.0, which is for calculations.
    """

    def __init__(self, red: int | float, green: int | float, blue: int | float) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __map_element_wise(self, op: Callable[[float], float]) -> Color:
        """Maps the operation to each element of the color"""
        return Color(op(self.red), op(self.green), op(self.blue))

    def __map_pair_wise(self, c: Color, op: Callable[[float, float], float]) -> Color:
        """Maps the operation pairwise across two colors"""
        return Color(
            op(self.red, c.red),
            op(self.green, c.green),
            op(self.blue, c.blue),
        )

    def __add__(self, c: Color | int | float) -> Color:
        """Overloads the + operator for self + c where c is a color or numeric constant"""
        if isinstance(c, int | float):
            return self.__map_element_wise(partial(operator.add, c))
        else:
            return self.__map_pair_wise(c, operator.add)

    def __radd__(self, c: Color | int | float) -> Color:
        """Overloads the + operator for self + c"""
        return self * c

    def __sub__(self, c: Color | int | float) -> Color:
        """Overloads the - operator for self - c where c is a color or numeric constant"""
        if isinstance(c, int | float):
            return self.__map_element_wise(lambda x: x - c)
        else:
            return self.__map_pair_wise(c, operator.sub)

    def __rsub__(self, c: Color | int | float) -> Color:
        """Overloads the - operator for c - self"""
        return c + -self

    def __mul__(self, c: Color | int | float) -> Color:
        """Overloads the * operator for self * c where c is a color or numeric constant"""
        if isinstance(c, int | float):
            return self.__map_element_wise(partial(operator.mul, c))
        else:
            return self.__map_pair_wise(c, operator.mul)

    def __rmul__(self, c: Color | int | float) -> Color:
        """Overloads the * operator for c * self where c is a color or numeric constant"""
        return self * c

    def __truediv__(self, c: int | float) -> Color:
        """Overloads the / operator for self / c where c is a numeric constant"""
        return self.__map_element_wise(lambda x: x / c)

    def __neg__(self) -> Color:
        """Overloads the negation operator - for a color, which negates each element"""
        return Color(-self.red, -self.green, -self.blue)

    def __eq__(self, other: object) -> bool:
        """Overloads the == operator for custom equality checking for colors. The elements are
        compared pair-wise and within a given epsilon.
        """
        if not isinstance(other, Color):
            return NotImplemented
        else:
            return (
                compare_float(self.red, other.red)
                and compare_float(self.green, other.green)
                and compare_float(self.blue, other.blue)
            )

    def __str__(self) -> str:
        """Overloads the string conversion method to customize how a color is
        converted to a string. This is helpful for printing a color.
        """
        return f"color({self.red}, {self.green}, {self.blue})"

    def __repr__(self) -> str:
        """Overloads the string conversion method to customize how a color is
        converted to a string. This is helpful for printing a color.
        """
        return f"Color({self.red}, {self.green}, {self.blue})"

    def clamp(self, minimum: int | float, maximum: int | float) -> Color:
        """Clamps a color's components to be in the range [minimum, maximum]"""
        return self.__map_element_wise(lambda x: clamp_number(x, minimum, maximum))

    def as_rgb_list(self) -> list[int]:
        """Converts the color to a list of RGB values, where each individual value
        runs from 0 to 255 instead of 0 to 1.
        """

        # Helper function to convert the values [0, 1] to [0, 255]
        def expand_to_byte(value: int | float) -> int:
            return round(float(value) * 255.0 / 255.0)

        return [expand_to_byte(self.red), expand_to_byte(self.green), expand_to_byte(self.blue)]


def hadamard_product(c1: Color, c2: Color) -> Color:
    """Computes the Hadamard (or Schur) product of the colors"""
    return c1 * c2


def blend(c1: Color, c2: Color) -> Color:
    """Blends two colors by averaging them together"""
    return (c1 + c2) / 2


class Colors(Enum):
    """Defines some common color constants"""

    BLACK = Color(0, 0, 0)
    WHITE = Color(1, 1, 1)
    RED = Color(1, 0, 0)
    GREEN = Color(0, 1, 0)
    BLUE = Color(0, 0, 1)
    LIGHT_GRAY = Color(211, 211, 211) / 255.0
    GRAY = Color(128, 128, 128) / 255.0
    VIO = Color(238, 130, 238) / 255.0
    SKY_BLUE = Color(135, 206, 235) / 255.0
    PALE_GREEN = Color(152, 251, 152) / 255.0
    PURPLE = Color(128, 0, 128) / 255.0
    ROYAL_BLUE = Color(65, 105, 225) / 255.0
    POWDER_BLUE = Color(176, 224, 230) / 255.0
    YELLOW = Color(255, 255, 0) / 255.0
    PINK = Color(255, 192, 203) / 255.0
    DEEP_PINK = Color(255, 20, 147) / 255.0
    HOT_PINK = Color(255, 105, 180) / 255.0
