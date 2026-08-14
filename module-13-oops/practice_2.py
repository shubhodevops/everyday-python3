
#example of instance method and static method
class Rectangle:

    def __init__ (self, l, h):
        self.length = l
        self.height = h
    def perimeter(self):
        return 2*(self.length + self.height)    
    
    @staticmethod
    def area_cal(length, height):
        return length* height

r1=Rectangle(10,5) # creating an object of class Rectangle
perimeter=r1.perimeter() # calling instance method using object name

print(f"Perimeter of rectangle is {perimeter}") # printing perimeter of rectangle

x=Rectangle.area_cal(10,9) # calling static method using class name and passing arguments to it

print(x)