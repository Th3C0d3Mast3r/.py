# this is, assumingly, the same super() function as we have in Java
# although there is some DEPTH TO BE LEARNED FROM THIS. SO REFER DOCUMENTATIONS FOR THIS AGAINST

class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.breadth=width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
        

class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.length=length
        self.width=width
        self.height=height

square = Square(3, 3)
cube = Cube(3, 3, 3)

        

