from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable
import operator
from ray_tracer_challenge.utilities import *
from functools import partial
import math


class ITuple(ABC):
    """Interface used to convert 3D tuple-like elements to and from a 4D tuple"""

    @property
    @abstractmethod
    def x1(self) -> Number:
        """The first element of the tuple-like element"""
        ...

    @property
    @abstractmethod
    def x2(self) -> Number:
        """The second element of the tuple-like element"""
        ...

    @property
    @abstractmethod
    def x3(self) -> Number:
        """The third element of the tuple-like element"""
        ...

    @abstractmethod
    def toTupleList(self) -> list[Number]:
        """Converts a 3D tuple-like element to a list of length four consisting of
        the three components plus a fourth component. The list is essentially the
        homogeneous coordinate representation of the tuple.
        """
        ...

    @abstractmethod
    def fromTupleList(self, tuple_list: list[float]) -> ITuple:
        """Creates a 3D tuple-like element from a tuple list"""
        ...


class Vector(ITuple):
    """Represents a 3D vector"""

    def __init__(self, i: Number, j: Number, k: Number) -> None:
        """Creates a vector from the three components"""
        self.i = i
        self.j = j
        self.k = k

    def __map_element_wise(self, operator: Callable[[float], float]) -> Vector:
        """Maps the operation to each element of the vector"""
        return Vector(operator(self.i), operator(self.j), operator(self.k))

    def __map_pair_wise(self, v: Vector, operator: Callable[[float, float], float]) -> Vector:
        """Maps the operation pairwise across two vectors"""
        return Vector(operator(self.i, v.i), operator(self.j, v.j), operator(self.k, v.k))

    def __add__(self, v: Vector | int | float) -> Vector:
        """Overloads the + operator for u + v where v is a vector or numeric constant"""
        if isinstance(v, int | float):
            return self.__map_element_wise(partial(operator.add, v))
        else:
            return self.__map_pair_wise(v, operator.add)

    def __radd__(self, v: Vector | int | float) -> Vector:
        """Overloads the + operator for v + u"""
        return self * v

    def __sub__(self, v: Vector | int | float) -> Vector:
        """Overloads the - operator for u - v where v is a vector or numeric constant"""
        if isinstance(v, int | float):
            return self.__map_element_wise(lambda x: x - v)
        else:
            return self.__map_pair_wise(v, operator.sub)

    def __rsub__(self, v: Vector | int | float) -> Vector:
        """Overloads the - operator for v - u"""
        return v + -self

    def __mul__(self, v: Vector | int | float) -> Vector:
        """Overloads the * operator for u * v where v is a vector or numeric constant"""
        if isinstance(v, int | float):
            return self.__map_element_wise(partial(operator.mul, v))
        else:
            return self.__map_pair_wise(v, operator.mul)

    def __rmul__(self, v: Vector | int | float) -> Vector:
        """Overloads the * operator for v * u where v is a vector or numeric constant"""
        return self * v

    def __truediv__(self, c: int | float) -> Vector:
        """Overloads the / operator for u / c where c is a numeric constant"""
        return self.__map_element_wise(lambda x: x / c)

    def __neg__(self) -> Vector:
        """Overloads the negation operator - for a vector, which negates each element"""
        return Vector(-self.i, -self.j, -self.k)

    def __eq__(self, other: object) -> bool:
        """Overloads the == operator for custom equality checking for vectors. The elements are
        compared pair-wise and within a given epsilon.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        else:
            return (
                compare_float(self.i, other.i)
                and compare_float(self.j, other.j)
                and compare_float(self.k, other.k)
            )

    def __str__(self) -> str:
        """Overloads the string conversion method to customize how a vector is
        converted to a string. This is helpful for printing a vector.
        """
        return f"vector({self.i}, {self.j}, {self.k})"

    @property
    def sum(self) -> float:
        """Sum of all elements of a vector"""
        return self.i + self.j + self.k

    @property
    def norm(self) -> float:
        """The norm of the vector, that is the square of the dot product"""
        return math.sqrt(dot_product(self, self))

    @property
    def magnitude(self) -> float:
        """The magnitude of the vector, that is the square of the dot product.
        This is equivalent to the norm of the vector.
        """
        return self.norm

    def normalize(self) -> Vector:
        """Normalize a vector by dividing it by its norm or magnitude"""
        return self / self.norm

    # Implements the ITuple interface methods to be treated like a tuple-like element
    @property
    def x1(self) -> Number:
        return self.i

    @property
    def x2(self) -> Number:
        return self.j

    @property
    def x3(self) -> Number:
        return self.k

    def toTupleList(self) -> list[Number]:
        return [self.i, self.j, self.k]

    def fromTupleList(self, tuple_list: list[Number]) -> ITuple:
        return Vector(tuple_list[0], tuple_list[1], tuple_list[2])


class Point(ITuple):
    """Represents a 3D point"""

    def __init__(self, x: Number, y: Number, z: Number) -> None:
        """Creates a point from the three components"""
        self.x = x
        self.y = y
        self.z = z

    def __map_element_wise(self, operator: Callable[[float], float]) -> Point:
        """Maps the operation to each element of the point"""
        return Point(operator(self.x), operator(self.y), operator(self.z))

    def __map_pair_wise(self, v: Point, operator: Callable[[float, float], float]) -> Point:
        """Maps the operation pairwise across two points"""
        return Point(operator(self.x, v.x), operator(self.y, v.y), operator(self.z, v.z))

    def __add__(self, q: Point | Vector | int | float) -> Point:
        """Overloads the + operator for p + q where q is a point, vector, or numeric constant"""
        if isinstance(q, Point):
            return self.__map_pair_wise(q, operator.add)
        elif isinstance(q, Vector):
            v = q
            return Point(self.x + v.i, self.y + v.j, self.z + v.k)
        elif isinstance(q, int | float):
            return self.__map_element_wise(partial(operator.add, q))

    def __radd__(self, q: Point | int | float) -> Point:
        """Overloads the + operator for q + p"""
        return self * q

    def __sub__(self, q: Point | Vector | int | float) -> Point | Vector:
        """Overloads the - operator for p - q where q is a point, vector, or numeric constant.
        In the case of subtracting a point from a point, a vector pointing from p to q is returned.
        """
        if isinstance(q, Point):
            return Vector(self.x - q.x, self.y - q.y, self.z - q.z)
        elif isinstance(q, Vector):
            v = q
            return Point(self.x - v.i, self.y - v.j, self.z - v.k)
        elif isinstance(q, int | float):
            return self.__map_element_wise(lambda x: x - q)

    def __rsub__(self, c: float) -> Point:
        """Overloads the - operator for q - p"""
        return c + -self

    def __mul__(self, v: Point | int | float) -> Point:
        """Overloads the * operator for u * v where v is a point or numeric constant"""
        if isinstance(v, int | float):
            return self.__map_element_wise(partial(operator.mul, v))
        else:
            return self.__map_pair_wise(v, operator.mul)

    def __rmul__(self, c: float) -> Point:
        return self * c

    def __truediv__(self, c: int | float) -> Point:
        """Overloads the / operator for u / c where c is a numeric constant"""
        return self.__map_element_wise(lambda x: x / c)

    def __neg__(self) -> Point:
        """Overloads the negation operator - for a point, which negates each element"""
        return Point(-self.x, -self.y, -self.z)

    def __eq__(self, other: object) -> bool:
        """Overloads the == operator for custom equality checking for points. The elements are
        compared pair-wise and within a given epsilon.
        """
        if not isinstance(other, Point):
            return NotImplemented
        else:
            return (
                compare_float(self.x, other.x)
                and compare_float(self.y, other.y)
                and compare_float(self.z, other.z)
            )

    def __str__(self) -> str:
        """Overloads the string conversion method to customize how a point is
        converted to a string. This is helpful for printing a point.
        """
        return f"point({self.x}, {self.y}, {self.z})"

    # Implements the ITuple interface methods to be treated like a tuple-like element

    @property
    def x1(self) -> Number:
        return self.x

    @property
    def x2(self) -> Number:
        return self.y

    @property
    def x3(self) -> Number:
        return self.z

    def toTupleList(self) -> list[Number]:
        return [self.x, self.y, self.z]

    def fromTupleList(self, tuple_list: list[Number]) -> ITuple:
        return Point(tuple_list[0], tuple_list[1], tuple_list[2])


def dot_product(u: Vector, v: Vector) -> float:
    """Compute the dot product of two vectors"""
    return (u * v).sum


def cross_product(u: Vector, v: Vector) -> Vector:
    """Compute the cross product of two vectors"""
    return Vector(u.j * v.k - v.j * u.k, v.i * u.k - u.i * v.k, u.i * v.j - v.i * u.j)


def reflect(vector: Vector, normal: Vector) -> Vector:
    """Calculates the reflection of the vector across the normal vector"""
    return vector - 2 * dot_product(vector, normal) * normal
