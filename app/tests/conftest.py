import pytest

from app.types.point import Point, Vector


@pytest.fixture
def point():
    return Point(1, 2, 3)


@pytest.fixture
def vector():
    return Vector(5, 6, 7)
