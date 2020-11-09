print("Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number. Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.")
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point ({0}, {1})".format(self.x, self.y)


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Circle with center at ({0}, {1}) and radius {2}".format(self.center.x, self.center.y, self.radius)

instance = Circle(center=Point(150, 100), radius=75)

print(instance)
