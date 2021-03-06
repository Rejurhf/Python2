# Rejurhf
# 11.10.2018

class Shape:
    geometric_type = 'Generis Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.' .format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'
    def __init__(self, side):
        self.side = side

class RegularHexagon(Polygon):
    geometric_type = 'Regular Hexagon`'
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularHexagon):
    geometric_type = 'Square'
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        return self.side * self.side

hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75, 77))

square = Square(12)
print(square.area())
print(square.get_geometric_type())
square.plot(0.93, (74, 75))

print(square.__class__.mro())
