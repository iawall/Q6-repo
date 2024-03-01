from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        raise NotImplementedError("Subclasses must implement get_area method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def getArea(self):
        return 0.5 * self.base * self.height

class Pentagon(Shape):
    def __init__(self, sides):
        self.sides = sides

    def getArea(self):
        return (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * self * self) / 4

def main():
    side_length = 5
    pentagon = Pentagon.getArea(side_length)
    print(f"The area of the pentagon is {pentagon}")

if __name__ == "__main__":
    main()