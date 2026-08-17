# অবস্ট্রাকশন (Abstraction) হলো অপ্রয়োজনীয় ও জটিল তথ্য লুকিয়ে রেখে শুধু প্রয়োজনীয় ফিচার বা কার্যকারিতা সামনে আনা। আর ইনহেরিটেন্স (Inheritance) হলো এমন একটি প্রক্রিয়া যার মাধ্যমে একটি নতুন ক্লাস পুরোনো কোনো ক্লাসের প্রপার্টি ও মেথড ব্যবহার করতে পারে। এই দুটি অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিংয়ের (OOP) প্রধান স্তম্ভ।  
# ## অবস্ট্রাকশন (Abstraction)

# * মূল কাজ: জটিলতা কমানোর জন্য ভেতরের কোড বা লজিক লুকিয়ে রাখা হয়।
# * বাস্তবায়ন: সাধারণত অ্যাবস্ট্রাক্ট ক্লাস (Abstract Class) এবং ইন্টারফেস (Interface) ব্যবহার করে এটি করা হয়।
# * সুবিধা: কোড সহজে পরিবর্তন করা যায় এবং ব্যবহারকারী শুধু কাজের অংশটি দেখতে পান। যেমন: গাড়ি চালানোর সময় ব্রেক বা এক্সিলারেটর কীভাবে কাজ করে না জেনেও শুধু তা ব্যবহার করা।  

# ## ইনহেরিটেন্স (Inheritance)

# * মূল কাজ: একটি প্যারেন্ট (Parent/Super) ক্লাস থেকে চাইল্ড (Child/Sub) ক্লাসে কোড বা বৈশিষ্ট্য আদান-প্রদান করা।
# * কোড রিইউজেবিলিটি: একই কোড বারবার না লিখে এক জায়গা থেকে বারবার ব্যবহার করা যায়।
# * সম্পর্ক তৈরি: ক্লাসগুলোর মধ্যে একটি Parent-Child বা Is-a সম্পর্ক তৈরি করে। যেমন: Car ক্লাসটি Vehicle ক্লাস থেকে ইনহেরিট করতে পারে। 

# ## মূল পার্থক্য

# * Abstraction: ফোকাস করে কী (What) কাজ করবে তার ওপর, কীভাবে (How) কাজ করবে তা লুকিয়ে রাখে।
# * Inheritance: ফোকাস করে কোডের পুনঃব্যবহার এবং সম্পর্ক তৈরির ওপর। 

# আপনি কি এই বিষয়গুলো কোনো নির্দিষ্ট প্রোগ্রামিং ভাষায় (যেমন Java, C++, Python) কোডসহ দেখতে চান?

# Here is the complete guide to Abstraction and Inheritance in Python, 
# explained using simple terms, clear examples, 
# and real-life analogies.

# 1. Abstraction (লুকিয়ে রাখা)Direct Answer: Abstraction means hiding the complex background details and showing only the essential features to the user. 
# It answers the question: "What does this object do?" without worrying about "How does it do it?" Real-Life Analogy: The Coffee MachineWhen you want coffee, you just press a button. 
# You do not need to know how the machine heats the water, grinds the beans, or pumps the liquid. 
# The internal mechanics are abstracted (hidden) from you. You only interact with the simple interface (the button).
# How it works in PythonPython uses the abc (Abstract Base Classes) module to create abstract classes.
# An Abstract Class is a blueprint that cannot be used to create objects directly.
# An Abstract Method is a method that is declared but has no code inside it. 
# The child classes must write the actual code for it

from abc import ABC, abstractmethod

# 1. Create an Abstract Class (The Blueprint)
class CoffeeMachine(ABC):
    
    @abstractmethod
    def brew_coffee(self):
        """This is an abstract method. No code inside here."""
        pass

# 2. Implement the details in a real class
class EspressoMachine(CoffeeMachine):
    
    def brew_coffee(self):
        # The complex details are written here
        print("Grinding beans...")
        print("Heating water to 90 degrees...")
        print("Pouring a rich shot of Espresso!")

# Using the code
my_machine = EspressoMachine()
my_machine.brew_coffee()  # The user just calls this, ignoring the details inside




# 2. Inheritance (উত্তরাধিকার)
# Direct Answer: Inheritance is a way to create a new class using the features of an existing class. The old class is called the Parent (or Base) Class, and the new one is the Child (or Derived) Class. It creates an "Is-A" relationship (e.g., a Car is a Vehicle). 
# Real-Life Analogy: Parents and Children
# Think of a parent passing down traits like eye color, height, or last name to their child. The child automatically gets these traits but can also learn new skills or have unique hobbies that the parents do not have. [1, 2]
# Key Benefits
#     • Code Reuse: You do not have to copy and paste the same code.
#     • Easy Maintenance: If you fix a bug in the parent class, it automatically fixes it for all child classes


# 1. Parent Class (General features)
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} engine is now running.")

# 2. Child Class (Inherits everything from Vehicle)
class ElectricCar(Vehicle):
    def __init__(self, brand, year, battery_capacity):
        # 'super()' links the child to the parent class
        super().__init__(brand, year) 
        self.battery_capacity = battery_capacity # Unique feature

    def charge_battery(self): # Unique action
        print(f"Charging the {self.brand}'s {self.battery_capacity}kWh battery.")

# Using the code
my_tesla = ElectricCar("Tesla", 2026, 75)

# The Child class can use Parent methods automatically
my_tesla.start_engine()  

# The Child class can also use its own unique methods
my_tesla.charge_battery() 



# Keywords:   ABC, @abstractmethod 
#             super(). 



# Multiple Inheritance is a feature in Python where a child class can inherit features (attributes and methods) from more than one parent class.
# It creates an "Is-A" relationship with multiple categories at the same time. For example, a FlyingCar is a Car, and it also is an Airplane.

# Real-Life Analogy: The Smartphone
# Think of a modern Smartphone. It inherits its features from multiple older inventions: 
#     1. From a Traditional Phone: It gets the ability to make voice calls.
#     2. From a Camera: It gets the ability to take high-quality photos.
#     3. From a Computer: It gets the ability to browse the internet. 
# Instead of reinventing the camera and phone mechanics from scratch, the Smartphone class simply inherits from both. 

# Python Code Example
# Here is how you can implement this in Python by passing multiple parent classes inside the parentheses () separated by commas:
# python
# Parent Class 1
class Camera:
    def take_photo(self):
        print("Click! Photo taken and saved.")

# Parent Class 2
class Phone:
    def make_call(self, number):
        print(f"Dialing {number}...")

# Child Class inheriting from BOTH Camera and Phone
class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("Opening web browser...")

# Using the Multiple Inheritance
my_phone = Smartphone()

# Accessing methods from both parents
my_phone.make_call("017XXXXXXXX")  # From Phone
my_phone.take_photo()               # From Camera

# Accessing its own method
my_phone.browse_internet()          # From Smartphone



# The Diamond Problem & MRO (Method Resolution Order)
# Multiple inheritance sounds great, but it can cause a famous confusion known as the Diamond Problem. 
# The Problem:
# What happens if Parent A and Parent B both have a method with the exact same name (e.g., start()), and the Child calls that method? Which parent's method will Python run?
# The Python Solution: MRO
# Python solves this using MRO (Method Resolution Order). It follows a strict left-to-right lookup rule. It will look for the method in: 
#     1. The Child class itself first.
#     2. The First Parent listed in the parentheses (left side).
#     3. The Second Parent listed (right side). 
# Code Example of MRO:


class ParentA:
    def greet(self):
        print("Hello from Parent A")

class ParentB:
    def greet(self):
        print("Hello from Parent B")

# ParentA is written first, so it has higher priority
class Child(ParentA, ParentB):
    pass

obj = Child()
obj.greet()  # Output: Hello from Parent A

# To see the exact lookup order, you can print the .__mro__ attribute
print(Child.__mro__)


# Summary Checklist
#     • Syntax: class Child(Parent1, Parent2):
#     • Use Case: When a class naturally fits into multiple categories.
#     • Warning: Use it carefully. Having too many parents can make your code messy and hard to debug. 
# Would you like to see how to use the super() function inside Multiple Inheritance, or should we try a quick practice challenge to test your understanding?


# super() function inside Multiple Inheritance, or should we try a quick practice challenge to test your understanding?
# Let us look at how super() works inside Multiple Inheritance. 
# It behaves differently than you might expect!

# The Surprise of super() in Multiple Inheritance
# In Single Inheritance, super() simply calls the parent class. But in Multiple Inheritance, super() does not just look at the direct parent. Instead, it follows the Method Resolution Order (MRO) line.
# When you call super() inside a method, Python looks at the MRO chain and calls the next class in line, even if that class is not the direct parent of the current class! This allows all parent classes to be initialized or called in a clean, cooperative order.
# Real-Life Analogy: The Assembly Line
# Think of an assembly line.
#     • Worker A adds the wheels, then passes the car to the next person in line (super()).
#     • Worker B adds the doors, then passes it to the next person in line (super()).
#     • No one needs to know who is next in line; they just trust the system to hand it over to the next station.

# Python Code Example: Cooperative Init
# Here is a classic example using __init__ to show how super() triggers all parent constructors in the correct order.
# python
class FirstParent:
    def __init__(self):
        print("1. FirstParent init started")
        super().__init__()  # This passes the control to the NEXT class in MRO!
        print("1. FirstParent init finished")

class SecondParent:
    def __init__(self):
        print("2. SecondParent init started")
        super().__init__()  # This passes control to the ultimate base class (object)
        print("2. SecondParent init finished")

# Combined class inheriting from both
class Child(FirstParent, SecondParent):
    def __init__(self):
        print("3. Child init started")
        super().__init__()  # Calls the first class in MRO (FirstParent)
        print("3. Child init finished")

# Let's run the code
my_child = Child()
# 
# What prints in the terminal?
# text
# 3. Child init started
# 1. FirstParent init started
# 2. SecondParent init started
# 2. SecondParent init finished
# 1. FirstParent init finished
# 3. Child init finished
# 
# Why did this happen?
# Look at the MRO chain for the Child class: Child → FirstParent → SecondParent → object.
#     1. Child.__init__ starts and calls super().
#     2. The system looks at the MRO. The next one is FirstParent.
#     3. FirstParent.__init__ starts. It calls super().
#     4. The system looks at the MRO. The next one after FirstParent is SecondParent!
#     5. SecondParent.__init__ runs, finishes, and then the code wraps backward like a nesting doll.


# Look at the code below. What will be the exact output printed in the terminal when player.speak() is executed?python

class Character:
    def speak(self):
        print("I am a game character.")

class Warrior(Character):
    def speak(self):
        print("I fight with honor!")
        super().speak()

class Mage(Character):
    def speak(self):
        print("I cast powerful spells!")
        super().speak()

class Spellblade(Warrior, Mage):
    pass

player = Spellblade()
player.speak()


# Use code with caution.Give it a guess! 
# What do you think will print out, and what order will the statements appear in


# No problem at all! Let us break it down step-by-step. It is tricky because super() does something very special here.The correct answer is that three lines will print out in this exact order:"I fight with honor!""I cast powerful spells!""I am a game character."

# Why does this happen? (The Step-by-Step Breakdown)
# To understand the output, we just need to look at the MRO (Method Resolution Order) chain for our Spellblade class.
# Python builds the lookup chain like this:Spellblade → Warrior → Mage → CharacterHere is exactly what happens when you run player.speak():
# 
# Step 1: Python looks for speak() inside Spellblade. It is not there.
# Step 2: It goes to the next class in the chain, which is Warrior. It runs Warrior.speak().🖨️ This prints: I fight with honor!
# Step 3: Inside Warrior.speak(), there is a super().speak() call. Remember, super() means "go to the next class in the MRO chain". The next class after Warrior is Mage!
# Step 4: It runs Mage.speak().🖨️ This prints: I cast powerful spells!
# Step 5: Inside Mage.speak(), there is another super().speak() call. The next class in the chain after Mage is Character.
# Step 6: It runs Character.speak().🖨️ This prints: I am a game character.

# Even though Warrior and Mage do not inherit from each other directly, 
# Python links them together in a chain using super(). 
# This ensures that every parent gets a turn to speak without skipping anyone!


