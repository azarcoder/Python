import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass
    
    @abc.abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return self.side * 4

sq = Square(5)
print("Area of square:", sq.area())
print("Perimeter of square:", sq.perimeter())


