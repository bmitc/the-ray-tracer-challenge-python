import unittest
import math
from color import *

class TestColor(unittest.TestCase):

    def test_colors_are_tuples(self):
        color = Color(-0.5, 0.4, 1.7)
        self.assertEqual(color.red, -0.5)
        self.assertEqual(color.green, 0.4)
        self.assertEqual(color.blue, 1.7)

    def test_adding_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 + c2, Color(1.6, 0.7, 1.0))

    def test_subtracting_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 - c2, Color(0.2, 0.5, 0.5))

    def test_multiplying_a_color_by_a_scalar(self):
        self.assertEqual(2 * Color(0.2, 0.3, 0.4), Color(0.4, 0.6, 0.8))

    def test_multiplying_colors(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertEqual(c1 * c2, Color(0.9, 0.2, 0.04))

    # Additional tests not in book

    def test_multiplying_colors_is_the_hadamard_product(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertEqual(c1 * c2, hadamard_product(c1, c2))

    def test_color_enum(self):
        self.assertEqual(Colors.Blue.value, Color(0, 0, 1))

if __name__ == '__main__':
    unittest.main()
    