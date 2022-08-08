from abc import ABC


class Renderer(ABC):

    @property
    def render_triangle(self):
        return None


class VectorRenderer(Renderer):

    @property
    def render_triangle(self):
        return 'Drawing Triangle as lines'

    @property
    def render_square(self):
        return 'Drawing Square as lines'


class RasterRenderer(Renderer):

    @property
    def render_triangle(self):
        return 'Drawing Triangle as pixels'

    @property
    def render_square(self):
        return 'Drawing Square as pixels'


class Shape:

    def __init__(self, renderer):
        self.renderer = renderer


class Triangle(Shape):

    def __str__(self):
        return self.renderer.render_triangle


class Square(Shape):

    def __str__(self):
        return self.renderer.render_square


print(str(Triangle(RasterRenderer())))
