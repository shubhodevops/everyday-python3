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

# knoledge of object oriented programming is important to understand the concept of classes and objects in python------------------------


# theory of object oriented programming is based on the concept of objects and classes
# object oriented programming is a programming paradigm that uses objects and classes to design 
# and implement  programs 

# class is a blueprint of object and object is an instance of class
# object is an instance of a class that has its own state and behavior
# object and instance are same thing and can be used interchangeably
# encapsulation is the concept of wrapping data and methods into a single unit called class
# abstraction is the concept of hiding the implementation details and showing only 
    # the functionality to the user
# data hiding is the concept of restricting access to the data members of a class from outside the class    



# variables in class can be three types: instance variable, class variable and local variable
# methods in class can be three types: instance method, class method and static method

# instance variable is a variable that is defined inside the constructor method 
# and is unique to each instance of the class
# instance method is a method that is defined inside the class and is unique to each instance of the class and # it takes self as first parameter which refers to the instance of the class itself

# class variable is a variable that is defined inside the class and is shared by all instances of the class
# class method is a method that is defined inside the class and is shared by all instances of the class and it # is defined using the @classmethod decorator and it takes cls as first parameter which refers to the class 
# itself

# local variable is a variable that is defined inside a method and is unique to that method and 
# it is not accessible outside the method

# static variable is a variable that is defined inside the class and is shared by all instances of 
# the class and it is defined using the @staticmethod decorator and 
# it does not take self or cls as first parameter and it can be called using the class name or object name

# static method is a method that is defined inside the class and is shared by all instances of the class 
# and it is defined using the @staticmethod decorator and it does not take self or cls as first parameter 
# and it can be called using the class name or object name


# self is a reference to the current instance of the class and is used to access 
# the instance variables and methods of the class      
# constructor is a special method that is called when an object of the class 
# is created and is used to initialize the instance variables of the class

# property method is used to access the instance variables of a class without using the dot operator and
# it is defined using the @property decorator and it is used to access the instance variables 
# of a class without using the dot operator.

# decorators are used to modify the behavior of a method or function and they are defined using 
# the @ symbol followed by the name of the decorator and they are used to modify the behavior 
# of a method or function.

# def__init__ is a special method that is called when an object of the class is created and is used to
#  initialize the instance variables of the class and it is defined using the def keyword followed by
#  the name of the method and it takes self as first parameter which refers to the instance of 
#  the class itself.





