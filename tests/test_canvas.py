import unittest
from ray_tracer_challenge.canvas import *
from ray_tracer_challenge.color import *


class TestCanvas(unittest.TestCase):
    def test_creating_a_canvas(self):
        canvas = Canvas(10, 20)
        self.assertEqual(canvas.width, 10)
        self.assertEqual(canvas.height, 20)
        self.assertEqual(canvas.get_pixel(0, 0), Colors.BLACK.value)
        self.assertEqual(canvas.get_pixel(9, 19), Colors.BLACK.value)

    # Additional tests not in the book

    def test_updating_canvas_pixels(self):
        canvas = Canvas(10, 20)

        def update_fn(x, y, color):
            if x == 9 and y == 19:
                return Colors.BLUE.value
            else:
                return color

        canvas.update_pixels(update_fn)
        self.assertEqual(canvas.get_pixel(8, 10), Colors.BLACK.value)
        self.assertEqual(canvas.get_pixel(9, 19), Colors.BLUE.value)


if __name__ == "__main__":
    unittest.main()
