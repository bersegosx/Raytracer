from pytest import approx

from app.types.color import Color


def test_add_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)

    assert c1 + c2 == Color(1.6, 0.7, 1.0)


def test_sub_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)

    assert c1 - c2 == Color(approx(0.2), 0.5, 0.5)


def test_mul_color_by_scalar():
    c1 = Color(0.2, 0.3, 0.4)

    assert c1 * 2 == Color(0.4, 0.6, 0.8)


def test_product():
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)

    assert c1.hadamard_product(c2) == Color(0.9, 0.2, approx(0.04))
