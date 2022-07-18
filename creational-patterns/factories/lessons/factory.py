from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()


p2 = Point.factory.new_polar_point(1, 2)
print(p2)
p3 = Point.factory.new_cartesian_point(1, 2)
print(p3)
