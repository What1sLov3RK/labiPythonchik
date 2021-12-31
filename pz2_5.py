# 1. Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods that calculate the perimeter and the area of the rectangle.
# Also, provide setter and getter for the length and width attributes. The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.
class Rectangle:
    def __init__(self,length=1,width=1):
        self.length=length
        self.width=width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, s):
        if not isinstance(s, int):
            raise TypeError("Length must be number!")
        elif s < 0:
            raise ValueError("Length cant be lesser than zero!")
        self.__length = s

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, s):
        if not isinstance(s, int):
            raise TypeError("width must be number!")
        elif s < 0:
            raise ValueError("width cant be lesser than zero!")
        self.__width = s

    def perimeter(self):
        return (self.length+self.width)*2

    def area(self):
        return self.length*self.width


rect = Rectangle(22,3)
print(rect.perimeter())
print(rect.area())