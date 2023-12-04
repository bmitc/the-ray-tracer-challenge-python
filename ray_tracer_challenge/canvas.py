"""Provides a canvas type that contains color pixels at (x,y)-coordinates"""

from typing import Callable
from ray_tracer_challenge.color import Color, Colors


class Canvas:
    """Represents a 2D canvas of (x,y) pixels consisting of colors, where the origin (0,0) is at
    the top left, x increases to the right, and y increases down.
    """

    def __init__(self, width: int, height: int) -> None:
        """Creates a 2D canvas of pixels the given width and height, initializing every pixel
        to the black"""
        self.width = width
        self.height = height
        self.__array = [[Colors.BLACK.value for _x in range(width)] for _y in range(height)]

    def get_pixel(self, x: int, y: int) -> Color:
        """Get the pixel value at the given (x, y) position"""
        return self.__array[y][x]

    def set_pixel(self, x: int, y: int, color: Color) -> None:
        """Set the pixel value at the given (x, y) position"""
        self.__array[y][x] = color

    def update_pixels(self, update_fn: Callable[[int, int, Color], Color]) -> None:
        """Updates the canvas' pixels according to the given function"""
        for x in range(self.width):
            for y in range(self.height):
                self.__array[y][x] = update_fn(x, y, self.get_pixel(x, y))
