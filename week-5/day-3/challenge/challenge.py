import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius=radius

    def perimeter(self):
        return self.radius/2 * math.pi

    def area(self):
        return self.radius**2 *math.pi


#--------------------------------------------------

class MyCircle(Circle):
    def __init__(self,radius=None, diameter=None):
        if not radius and not diameter:
            raise Exception('This class cannot be instantiated without a diameter or radius')
        super().__init__(radius)
        if not self.radius:
            self.radius = diameter/2
            self.diameter = diameter
        else:
            self.diameter = radius * 2
    
    def __str__(self):
        return f'Circle with a radius of {self.radius}'

    def __repr__(self):
        return f'Circle object r={self.radius}'

    def __add__(self, other):
        if isinstance(other, MyCircle):
            return MyCircle(radius=self.radius+other.radius)
        elif isinstance(other, int):
            return self.radius + other
        else:
            raise TypeError('Can only be used with int or MyCircle objects')

    def __gt__(self,other):
        if isinstance(other, MyCircle):
            return self.radius > other.radius
        elif isinstance(other, int):
            return self.radius > other
        else:
            raise TypeError('Can only be used with int or MyCircle objects')
    def __int__(self):
        return self.radius
    def __eq__(self, other):
        if isinstance(other, MyCircle):
            return self.radius == other.radius
        elif isinstance(other, int):
            return self.radius == other
        else:
            raise TypeError('Can only be used with int or MyCircle objects')



c1 = MyCircle(diameter=3)
print(c1.radius)
print(c1.diameter)
c2 = MyCircle(radius=3)
print(c2.radius)
print(c2.diameter)
print(c1)
c3 = c1 + c2
print('is c3 bigger than c2?', c3 > c2)
print('is c3 equal to than c2?', c3 == c2)
print([c2, c1,c3])
print(sorted([c1,c2,c3]))