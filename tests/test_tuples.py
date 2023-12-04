import unittest
import math
from ray_tracer_challenge.tuples import *


class TestTuples(unittest.TestCase):
    def test_point_creates_tuples(self):
        p = Point(4, -4, 3)
        self.assertEqual(p.x, 4)
        self.assertEqual(p.y, -4)
        self.assertEqual(p.z, 3)

    def test_vector_creates_tuples(self):
        v = Vector(4, -4, 3)
        self.assertEqual(v.i, 4)
        self.assertEqual(v.j, -4)
        self.assertEqual(v.k, 3)

    def test_adding_a_vector_to_a_point(self):
        self.assertEqual(Point(3, -2, 5) + Vector(-2, 3, 1), Point(1, 1, 6))

    def test_adding_a_vector_to_a_vector(self):
        u = Vector(1, 2, 3)
        v = Vector(4, 5.5, 6.5)
        self.assertEqual(u + v, Vector(5, 7.5, 9.5))

    def test_subtracting_two_points(self):
        self.assertEqual(Point(3, 2, 1) - Point(5, 6, 7), Vector(-2, -4, -6))

    def test_subtracting_a_vector_from_a_point(self):
        self.assertEqual(Point(3, 2, 1) - Vector(5, 6, 7), Point(-2, -4, -6))

    def test_subtracting_two_vectors(self):
        u = Vector(3, 2, 1)
        v = Vector(5, 6, 7)
        self.assertEqual(u - v, Vector(-2, -4, -6))

    def test_subtracting_a_vector_from_the_zero_vector(self):
        u = Vector(0, 0, 0)
        v = Vector(1, -2, 3)
        self.assertEqual(u - v, Vector(-1, 2, -3))

    def test_negating_a_vector(self):
        self.assertEqual(-Vector(1, -2, 3), Vector(-1, 2, -3))

    def test_negating_a_point(self):
        self.assertEqual(-Point(1, -2, 3), Point(-1, 2, -3))

    def test_multiplying_a_point_by_a_scalar(self):
        self.assertEqual(3.5 * Point(1, -2, 3), Point(3.5, -7, 10.5))

    def test_multiplying_a_vector_by_a_scalar(self):
        self.assertEqual(3.5 * Vector(1, -2, 3), Vector(3.5, -7, 10.5))

    def test_multiplying_a_point_by_a_fraction(self):
        self.assertEqual(0.5 * Point(1, -2, 3), Point(0.5, -1, 1.5))

    def test_multiplying_a_vector_by_a_fraction(self):
        self.assertEqual(0.5 * Vector(1, -2, 3), Vector(0.5, -1, 1.5))

    def test_dividing_a_point_by_a_scalar(self):
        self.assertEqual(Point(1, -2, 3) / 2, Point(0.5, -1, 1.5))

    def test_dividing_a_vector_by_a_scalar(self):
        self.assertEqual(Vector(1, -2, 3) / 2, Vector(0.5, -1, 1.5))

    def test_computing_the_magnitude_of_a_vector(self):
        self.assertEqual(Vector(1, 0, 0).magnitude, 1)
        self.assertEqual(Vector(0, 1, 0).magnitude, 1)
        self.assertEqual(Vector(0, 0, 1).magnitude, 1)
        self.assertEqual(Vector(1, 2, 3).magnitude, math.sqrt(14))
        self.assertEqual(Vector(-1, -2, -3).magnitude, math.sqrt(14))

    def test_normalizing_a_vector(self):
        self.assertEqual(Vector(4, 0, 0).normalize(), Vector(1, 0, 0))
        self.assertEqual(
            Vector(1, 2, 3).normalize(),
            Vector(1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14)),
        )

    def test_the_magnitude_of_a_normalized_vector(self):
        self.assertEqual(Vector(1, 2, 3).normalize().magnitude, 1)

    def test_the_dot_product_of_two_vectors(self):
        u = Vector(1, 2, 3)
        v = Vector(2, 3, 4)
        self.assertEqual(dot_product(u, v), 20)

    def test_the_cross_product_of_two_vectors(self):
        u = Vector(1, 2, 3)
        v = Vector(2, 3, 4)
        self.assertEqual(cross_product(u, v), Vector(-1, 2, -1))
        self.assertEqual(cross_product(v, u), Vector(1, -2, 1))

    def test_reflecting_a_vector_approaching_at_45_degrees(self):
        u = Vector(1, -1, 0)
        v = Vector(0, 1, 0)
        self.assertEqual(reflect(u, v), Vector(1, 1, 0))

    def test_reflecting_a_vector_off_a_slanted_surface(self):
        u = Vector(0, -1, 0)
        v = Vector(math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
        print(reflect(u, v))
        print(reflect(u, v) == Vector(1, 0, 0))
        self.assertEqual(reflect(u, v), Vector(1, 0, 0))


if __name__ == "__main__":
    unittest.main()
