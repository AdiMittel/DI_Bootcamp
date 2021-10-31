import math


class Circle():
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return self.radius/2*math.pi

    def area(self):
        return self.radius**2 * math.pi


circle = Circle(5)
print(circle.radius)
print(circle.perimeter())
print(circle.area())
