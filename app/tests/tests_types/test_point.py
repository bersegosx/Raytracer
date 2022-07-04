from dataclasses import astuple, is_dataclass

import pytest

from app.types.point import Point, Vector


def test_tuple_types(point, vector):
    assert astuple(point) == (1, 2, 3, 1)
    assert astuple(vector) == (5, 6, 7, 0)


def test_tuple_add(point, vector):
    p2 = Point(6, 1, 4)
    v2 = Vector(3, 5, 6)

    with pytest.raises(Exception):
        point + p2

    result = vector + v2
    assert is_dataclass(result)
    assert isinstance(result, Vector)
    assert astuple(result) == (8, 11, 13, 0)

    result = vector + point
    assert is_dataclass(result)
    assert isinstance(result, Point)
    assert astuple(result) == (6, 8, 10, 1)


def test_tuples_substracting(vector):
    p1, p2 = Point(3, 2, 1), Point(5, 6, 7)

    result = p1 - p2
    assert is_dataclass(result)
    assert isinstance(result, Vector)
    assert astuple(result) == (-2, -4, -6, 0)

    result = p1 - vector
    assert is_dataclass(result)
    assert isinstance(result, Point)
    assert astuple(result) == (-2, -4, -6, 1)


def test_approx_func():
    assert pytest.approx(2.3, 0.1) == 2.2
