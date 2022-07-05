import typing as t
from dataclasses import dataclass

import numpy as np

Tuple: t.TypeAlias = t.Union['Point', 'Vector']
Scalar: t.TypeAlias = int | float


@dataclass(frozen=True)
class Point:
    x: float
    y: float
    z: float
    w: int = 1

    @classmethod
    def is_point(cls, value) -> bool:
        return value.w == 1

    def __add__(self, other: Tuple) -> Tuple:
        if Point.is_point(other):
            raise Exception('cant add 2 points')

        return Point(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z
        )

    def __sub__(self, other: Tuple) -> Tuple:
        cls: t.Type[Tuple] = Vector if Point.is_point(other) else Point
        return cls(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )

    def __neg__(self) -> Tuple:
        return self.__class__(
            x= -self.x,
            y= -self.y,
            z= -self.z,
            w= -self.w
        )

    def __mul__(self, other: Scalar) -> Tuple:
        return self.__class__(
            x=self.x * other,
            y=self.y * other,
            z=self.z * other,
            w=self.w * other,
        )

    def __truediv__(self, other: Scalar) -> Tuple:
        return self.__class__(
            x=self.x / other,
            y=self.y / other,
            z=self.z / other,
            w=self.w / other,
        )

    def magnitude(self) -> Scalar:
        np_array = np.array([self.x, self.y, self.z, self.w])
        return np.linalg.norm(np_array)

    def normalize(self) -> Tuple:
        np_array = np.array([self.x, self.y, self.z, self.w])
        np_normalized_array = np_array / self.magnitude()
        return self.__class__(*np_normalized_array)


@dataclass(frozen=True)
class Vector(Point):
    w: int = 0

    def __add__(self, other: Tuple) -> Tuple:
        cls = Point if Point.is_point(other) else Vector
        return cls(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z,
            w=self.w + other.w
        )

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )
