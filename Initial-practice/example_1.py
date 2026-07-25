"""

1)Python Exercises, Practice, Solution
URL:https://www.w3resource.com/python-exercises

2)Practice Python Exercises and Challenges with Solutions
URL: https://pynative.com/python-exercises-with-solutions


3)Python Exercise with Practice Questions and Solutions
URL:https://www.geeksforgeeks.org/python/python-exercises-practice-questions-and-solutions

"""

import math

print("Example of Some Simple Calculations between two numbers")

a = float(input("Type any number for a: "))
b = float(input("Type any number for b: "))

# addition of two given numbers
result = a + b
print("And Your score of two given numbers(addition) : ", result)

# find square of two given numbers
square = a * b

# find average of two given numbers
average = (a + b) / 2

# find remainder of two given numbers
remainder = (a + b) % 2

# Square root of given two numbers
square_root = math.sqrt(a + b)

# find largest number of two given numbers
largest_number = max(a, b)

# find smallest number of two given numbers
small_number = min(a, b)

# applying conditional statement
if result >= 7.5 and result <= 9.99:

    if result == 8:  # nested if example
        print("You need extra effort")
    elif result == 8.5:
        print("do something , very important")

    else:
        print("You are going to overseas very soon")

elif result >= 4.5 and result <= 7.49:
    print("Try Hard for Next interview")
else:
    print("Expected result wasn't satisfactory")


print("Square of two given numbers : ", int(square))

print("average of two given numbers : ", float(average))

print("Remainder of two given numbers : ", float(remainder))

print("Square root of two given numbers : ", int(square_root))

print("Largest Number between two numbers:", int(largest_number))

print("Smallest Number between two numbers:", int(small_number))


# checking type of datatype for selected variables
print("Checking the type of Result Variable :", type(result))
print("Checking the type  of Square variable:", type(square))
