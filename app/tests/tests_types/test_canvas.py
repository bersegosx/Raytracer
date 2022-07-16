from app.types.canvas import Canvas, pixel_at, write_pixel, canvas_to_ppm
from app.types.color import Color


def test_write_pixel():
    canvas = Canvas(width=10, height=20)
    red_color = Color(1, 0, 0)

    write_pixel(canvas, 2, 3, red_color)

    assert pixel_at(canvas, 2, 3) == red_color


def test_ppm_header():
    canvas = Canvas(10, 20)
    ppm = canvas_to_ppm(canvas)

    ppm_lines = ppm.splitlines()
    header = ppm_lines[:3]

    assert header == """P3
10 20
255
""".splitlines()


def test_ppm_pixel_data():
    canvas = Canvas(5, 3)

    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)

    write_pixel(canvas, 0, 0, c1)
    write_pixel(canvas, 2, 1, c2)
    write_pixel(canvas, 4, 2, c3)

    ppm = canvas_to_ppm(canvas)
    ppm_lines = ppm.splitlines()

    pixel_data = ppm_lines[3:]

    assert [
        '255 0 0 0 0 0 0 0 0 0 0 0 0 0 0',
        '0 0 0 0 0 0 0 127 0 0 0 0 0 0 0',
        '0 0 0 0 0 0 0 0 0 0 0 0 0 0 255'
    ] == pixel_data


def test_ppm_long_lines():
    canvas = Canvas(10, 2)

    color = Color(1.0, 0.8, 0.6)

    for x in range(canvas.width):
        for y in range(canvas.height):
            write_pixel(canvas, x, y, color)

    ppm = canvas_to_ppm(canvas)
    ppm_lines = ppm.splitlines()
    pixel_data = ppm_lines[3:]

    assert [
        '255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204',
        '153 255 204 153 255 204 153 255 204 153 255 204 153',
        '255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204',
        '153 255 204 153 255 204 153 255 204 153 255 204 153',
    ] == pixel_data


def test_ppm_ends_with_newline():
    canvas = Canvas(5, 3)

    ppm = canvas_to_ppm(canvas)
    assert ppm.endswith('\n')
