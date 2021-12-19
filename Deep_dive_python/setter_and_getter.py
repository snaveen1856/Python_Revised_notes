# class Rectangle(object):
#     def __init__(self, width, height):
#         self.width = width
#         self.heigth = height
    
#     def area(self):
#         return self.width * self.heigth
    
#     def perimeter(self):
#         return 2 * (self.width + self.heigth)

#     def __str__(self):
#         return f'Rectangle : width = {self.width}, height {self.heigth}'

#     def __repr__(self):
#         return f'Rectangle {self.width} {self.heigth}'
    
# r1 = Rectangle(10,20)
# str(r1)

############# Setter and Getter in Python ##############

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
    
    def area(self):
        return self.width * self.heigth
    
    def perimeter(self):
        return 2 * (self.width + self.heigth)

    def __str__(self):
        return f'Rectangle : width = {self.width}, height {self.heigth}'

    def __repr__(self):
        return f'Rectangle {self.width} {self.heigth}'
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

r1 = Rectangle(10,30)
print(r1)
