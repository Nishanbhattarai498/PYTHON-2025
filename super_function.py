#super()=function used to give access to the parent or sibling class 
# return a temporary object of parent class when used 


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)  # Call the parent class constructor

    def area(self):
        return self.length * self.width

class Cube(Square):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        # Call the parent class constructor
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
    

square=Square(5, 5)
print("Area of square:", square.area())  # Output: Area of square: 25
cube=Cube(5, 5, 5)
print("Volume of cube:", cube.volume())  # Output: Volume of cube: 125

        