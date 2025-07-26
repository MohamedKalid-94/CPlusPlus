import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
my_circle = Circle(radius=5)
print(f"The area of the circle is: {my_circle.area():.2f}")
