import math
class Shape:

    def Area(self):
        print("Area = 0")

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def Area(self):
        print("Area of square is ", math.pow(self.length,2))

if __name__=='__main__':
    square = Square(5)
    square.Area()