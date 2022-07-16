import typing as t
from dataclasses import dataclass

from app.types.color import Color

Scalar: t.TypeAlias = int | float

BLACK_COLOR = Color(0, 0, 0)

PPM_MAX_LINE_LENGTH = 70


@dataclass
class Canvas:
    width: int
    height: int

    pixels: list = None

    def __post_init__(self):
        self.pixels = [
            [BLACK_COLOR for _ in range(self.width)]
            for _ in range(self.height)
        ]


    def write_pixel(self, x: int, y: int, color: Color):
        self.pixels[y][x] = color

    def get_pixel(self, x: int, y: int) -> Color:
        return self.pixels[y][x]


def write_pixel(canvas: Canvas, x: int, y: int, color: Color):
    canvas.write_pixel(x, y, color)


def pixel_at(canvas: Canvas, x: int, y: int) -> Color:
    return canvas.get_pixel(x, y)


def color_to_base(color: int, base=255) -> int:
    color = max(0, color)
    color = min(1, color)
    return int(color*255)


def canvas_to_ppm(canvas: Canvas) -> str:
    header = f"""P3
{canvas.width} {canvas.height}
255
"""

    pixel_data = ""
    for x_line in canvas.pixels:
        line = ""

        for color in x_line:
            if line != "":
                line += " "

            line_part = f"{color_to_base(color.red)} {color_to_base(color.green)} {color_to_base(color.blue)}"
            line += line_part

            if len(line) > PPM_MAX_LINE_LENGTH:
                head, tail = line.rsplit(" ", maxsplit=1)
                line = f"{head}\n"
                pixel_data += line
                line = tail
                continue

        pixel_data += f"{line.rstrip()}\n"

    return header + pixel_data
