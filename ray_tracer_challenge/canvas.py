"""Provides a canvas type that contains color pixels at (x,y)-coordinates"""

from typing import Callable
import matplotlib.pyplot as plot
from ray_tracer_challenge.color import Color, Colors


class Canvas:
    """Represents a 2D canvas of (x,y) pixels consisting of colors, where the origin (0,0) is at
    the top left, x increases to the right, and y increases down.
    """

    def __init__(self, width: int, height: int) -> None:
        """Creates a 2D canvas of pixels the given width and height, initializing every pixel
        to the color black"""
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
        """Updates each pixel in the canvas according to the given function"""
        for x in range(self.width):
            for y in range(self.height):
                self.__array[y][x] = update_fn(x, y, self.get_pixel(x, y))

    def show(self) -> None:
        """Opens an image window and displays the canvas"""
        # Initialize a new pixel array that we will pass to matplotlib
        pixel_array = [[[0, 0, 0] for _x in range(self.width)] for _y in range(self.height)]

        # For every pixel in the canvas, convert it to an RGB list
        for x in range(self.width):
            for y in range(self.height):
                pixel_array[y][x] = self.get_pixel(x, y).as_rgb_list()

        # Display the pixel array as an image using matplotlib. Hide all the
        # axis and grid portions of the image.
        plot.imshow(pixel_array)
        plot.grid(False)
        plot.axis("off")
        plot.show()
