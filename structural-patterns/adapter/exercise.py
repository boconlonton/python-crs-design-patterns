class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


# Wrong
class SquareToRectangleAdapter:
    def __init__(self, square: Square):
        self.width = self.height = square.side


# Correct
class SquareToRectangleAdapterCorrect:
    def __init__(self, square: Square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


sq = Square(11)
adapter = SquareToRectangleAdapter(sq)
print(calculate_area(adapter))
sq.side = 10
print(calculate_area(adapter))

sq = Square(11)
adapter = SquareToRectangleAdapterCorrect(sq)
print(calculate_area(adapter))
sq.side = 10
print(calculate_area(adapter))
