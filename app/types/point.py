import typing as t
from dataclasses import dataclass

Tuple: t.TypeAlias = t.Union['Point', 'Vector']


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