
#calculate area and perimeter of circle using class and object

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Store the radius

    
    def area(self):
        return math.pi* (self.radius**2)
        
        
          
   
    def perimeter(self):
        return 2 * math.pi * self.radius
       
       
       
radius = float(input("Enter Radius value:   ")) 


c1 = Circle(radius)
print(f"Area: {c1.area():.2f}")
print(f"Perimeter: {c1.perimeter():.2f}")

#--------------------------------------------------------------------------
#There are several other great ways to take input for multiple parameters

    #1. The Single-Line Approach (Using .split())


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Ask user to type values separated by a space (e.g., "5.5 10")
user_input = input("Enter width and height separated by a space: ")

# .split() breaks the text into a list of strings: ["5.5", "10"]
parts = user_input.split()

# Convert the pieces into floats
user_width = float(parts[0])
user_height = float(parts[1])

# Pass them into your class
r1 = Rectangle(user_width, user_height)
print(f"Area: {r1.area():.2f}")
print(f"Perimeter: {r1.perimeter():.2f}")

    #2. The Multiple Input Approach (Using Multiple input() Calls)

class Rectangle:
    # The __init__ method now accepts TWO parameters: width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)
       
    # Get multiple inputs from the user (one by one)
user_width = float(input("Enter Width value:  ")) 
user_height = float(input("Enter Height value: ")) 

    # Pass BOTH values as actual parameters into the object
r1 = Rectangle(user_width, user_height)

print(f"Area: {r1.area():.2f}")
print(f"Perimeter: {r1.perimeter():.2f}")


    #3. The List Approach (Using a List to Store Inputs)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an empty list to hold the inputs
dimensions = []

# Add the inputs into the list one by one
dimensions.append(float(input("Enter Width: ")))
dimensions.append(float(input("Enter Height: ")))

# Create the object by pulling values out of the list using their index positions
r1 = Rectangle(dimensions[0], dimensions[1])

# The * symbol unpacks the list automatically in order!
r2 = Rectangle(*dimensions)

print(f"Area of r1 instance: {r1.area():.2f}")

print(f"Area of r2 instance: {r2.area():.2f}")




    