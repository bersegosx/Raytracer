import typing as t
from dataclasses import dataclass

Scalar: t.TypeAlias = int | float


@dataclass(frozen=True)
class Color:
    red: float
    green: float
    blue: float

    def __add__(self, other: 'Color') -> 'Color':
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue,
        )

    def __sub__(self, other: 'Color') -> 'Color':
        return Color(
            self.red - other.red,
            self.green - other.green,
            self.blue - other.blue,
        )

    def __mul__(self, other: Scalar) -> 'Color':
        return Color(
            self.red * other,
            self.green * other,
            self.blue * other,
        )

    def hadamard_product(self, other: 'Color') -> 'Color':
        return Color(
            self.red * other.red,
            self.green * other.green,
            self.blue * other.blue,
        )
