#create a class:

class Rectangle(): #create a class Rectangle
    
    def __init__(self, l,h): #constructor method to initialize the instance variables
        self.length = l # instance variable
        self.height = h #instance variable
    def area(self): #instance method must defined with self parameter as first parameter
        return self.length * self.height #return area of rectangle

    def perimeter(self):#instance method must defined with self parameter as first parameter
        return 2*(self.length + self.height) #return perimeter of rectangle

#create an object or instance of class

s=Rectangle(10,5) # instance of class Rectangle
area=s.area() #method call to area method of class Rectangle
perimeter=s.perimeter() #method call to perimeter method of class Rectangle

print(f"Rectangle area is {area}") #print rectangle area
print(f"Rectangle perimeter is {perimeter}") #print rectangle perimeter

#varibles of class can be accessed using object name and dot operator
print(f"Length of rectangle is {s.length}") #print length of rectangle  
print(f"Height of rectangle is {s.height}") #print height of rectangle  

# class is a blueprint of object and object is an instance of class
# variables in class can be three types: instance variable, class variable and local variable
# methods in class can be three types: instance method, class method and static method
# encapsulation is the concept of wrapping data and methods into a single unit called class
# instance variable is a variable that is defined inside the 
    #constructor method and is unique to each instance of the class
# abstraction is the concept of hiding the implementation details and showing only 
    # the functionality to the user
# data hiding is the concept of restricting access to the data members of a class from outside the class
# initialization is the process of assigning values to the instance variables of a class
# self is a reference to the current instance of the class and 
    #  is used to access the instance variables and methods of the class      
# constructor is a special method that is called when an object of the class is created and 
    # is used to initialize the instance variables of the class
# object is an instance of a class that has its own state and behavior
# object and instance are same thing and can be used interchangeably
# theory of object oriented programming is based on the concept of objects and classes
# object oriented programming is a programming paradigm that uses objects and classes to design and implement programs     