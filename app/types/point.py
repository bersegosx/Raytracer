from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float
    z: float
    w: int = 1

    def __add__(self, other):
        if other.w == 1:
            raise Exception('cant add 2 points')

        return Point(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z
        )


@dataclass(frozen=True)
class Vector(Point):
    w: int = 0

    def __add__(self, other):
        cls = Point if other.w == 1 else Vector
        return cls(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z,
            w=self.w + other.w
        )
