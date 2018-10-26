import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def change_radius(self, new_radius):
        self.radius = new_radius


circle = Circle(7)

while True:
    radius = float(input("Circle radius: "))
    circle.change_radius(radius)
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())
