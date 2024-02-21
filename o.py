from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        print("Calculating the area of the shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius ** 2
        print(f"Circle area with radius {self.radius} is {area}")
        return area

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        area = self.side ** 2
        print(f"Square area with side {self.side} is {area}")
        return area

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        print(f"Rectangle area with length {self.length} and width {self.width} is {area}")
        return area

# New shape class Triangle

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        area = 0.5 * self.base * self.height
        print(f"Triangle area with base {self.base} and height {self.height} is {area}")
        return area

def main():
    shapes = [
        Circle(4),
        Square(5),
        Rectangle(6, 7),
        Triangle(8, 9)
    ]

    for shape in shapes:
        shape.get_area()

if __name__ == "__main__":
    main()
