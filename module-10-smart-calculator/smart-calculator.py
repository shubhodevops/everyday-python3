# Module-10 Assignment
# Author: Saif A Khan Shubho [01316345325]
# Date: 03 Aug 2026

# STEP 6: Global Scope Practice (Separate Task)

app_name = "Smart Calculator"

def print_app_name():
    #use of  global scope
    print(f"    \nApp Name: {app_name}")

# STEP 3: Calculator Functions

def addition(num1, num2):
   
    return num1 + num2

def subtraction(num1, num2):
  
    return num1 - num2

def multiplication(num1, num2):
    
    return num1 * num2

def division(num1, num2):
    
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

def modulus(num1, num2):
    
    if num2 == 0:
        return "Error: Cannot perform modulus with zero!"
    return num1 % num2

def power(num1, num2):
    
    return num1 ** num2

def floor_division(num1, num2):
    
    if num2 == 0:
        return "Error: Cannot perform floor division by zero!"
    return num1 // num2



# STEP 11: 

def percentage_calculator(num1, num2):
 
    if num2 == 0:
        return "Error: Cannot calculate percentage with zero as total!"
    return (num1 / num2) * 100

def square_root(num):

    if num < 0:
        return "Error: Cannot calculate square root of negative number!"
    return num ** 0.5

def cube(num):

    return num ** 3

def cube_root(num):

    if num < 0:
        return -((-num) ** (1/3))
    return num ** (1/3)

def maximum_of_two(num1, num2):

    return max(num1, num2)

def minimum_of_two(num1, num2):

    return min(num1, num2)


# STEP 4: Calculator Menu 

def display_menu():


    print("\nCALCULATOR MENU")
    print("="*18)
    
    menu_items = [
        "Addition",
        "Subtraction", 
        "Multiplication",
        "Division",
        "Modulus",
        "Power",
        "Floor Division",
        "Exit"
    ]
    
    # Using enumerate() to display menu with numbers
    for index, item in enumerate(menu_items, start=1):
        print(f"    {index}. {item}")
    
    print("="*40)

def display_advanced_menu():

  
    
    advanced_items = [
        "Percentage Calculator",
        "Square Root",
        "Cube",
        "Cube Root",
        "Maximum of Two Numbers",
        "Minimum of Two Numbers",
        "Exit Advanced Calculator"
    ]
    

    for index, item in enumerate(advanced_items, start=1):
        print(f"    {index}. {item}")
    
    print("="*40)

def get_number(prompt="Enter a number: "):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_two_numbers():

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    return num1, num2

def perform_calc(opt_, num1, num2=None):

    if num2 is not None:
        result = opt_(num1, num2)
    else:
        result = opt_(num1)
    
    # Check if result is an error message (string)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")

def advanced_calculator():
    #Advanced calculator sub menu
    while True:
        display_advanced_menu()
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue
        
        
        if choice == 7:
            print("\nExiting Advanced Calculator...")
            break
        
        # Advanced operations
        elif choice == 1:  # Percentage
            num1, num2 = get_two_numbers()
            perform_calc(percentage_calculator, num1, num2)
        
        elif choice == 2:  # Square Root
            num = get_number("Enter a number to find square root: ")
            perform_calc(square_root, num)
        
        elif choice == 3:  # Cube
            num = get_number("Enter a number to cube: ")
            perform_calc(cube, num)
        
        elif choice == 4:  # Cube Root
            num = get_number("Enter a number to find cube root: ")
            perform_calc(cube_root, num)
        
        elif choice == 5:  # Maximum
            num1, num2 = get_two_numbers()
            perform_calc(maximum_of_two, num1, num2)
        
        elif choice == 6:  # Minimum
            num1, num2 = get_two_numbers()
            perform_calc(minimum_of_two, num1, num2)
        
        else:
            print("Invalid choice! Please select a number between 1 and 7.")

def main_calculator():

    while True:
        display_menu()
        
        # Step 5: Input Validation for menu choice
        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
            continue
        
        # Step 4: Exit option
        if choice == 8:
            print("\nThank you for using Smart Calculator!")
            # Call Step 11: Advanced Calculator after exit
            
            print("\nADVANCED CALCULATOR MENU")
            print("="*25)
            advanced_calculator()
            
            break
        
        # Step 4: Main operations (1-7)
        elif 1 <= choice <= 7:
            num1, num2 = get_two_numbers()
            
            # Dictionary mapping choices to functions
            operations = {
                1: addition,
                2: subtraction,
                3: multiplication,
                4: division,
                5: modulus,
                6: power,
                7: floor_division
            }
            
            perform_calc(operations[choice], num1, num2)
        
        # Step 5: Invalid menu option
        else:
            print("Invalid choice! Please select a number between 1 and 8.")


# STEP 7: Lambda Practice

def lambda_practice():

    print("\n" + "="*40)
    print("        LAMBDA PRACTICE")
    print("="*40)
    
    # Lambda function to calculate square
    square = lambda x: x ** 2
    
    try:
        num = float(input("Enter a number to square: "))
        print(f"The square of {num} is: {square(num)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")



# STEP 8: Map Function 

def map_practice():

    print("\n" + "="*40)
    print("        MAP PRACTICE")
    print("="*40)
    
    numbers = [5, 10, 15, 20, 25]
    print(f"Original list: {numbers}")
    
    # Using map() with lambda to increase every number by 10
    increased_numbers = list(map(lambda x: x + 10, numbers))
    print(f"After adding 10: {increased_numbers}")



# STEP 9: Filter Function 

def filter_practice():

    print("\n" + "="*40)
    print("        FILTER PRACTICE")
    print("="*40)
    
    numbers = [5, 10, 15, 20, 25]
    print(f"Original list: {numbers}")
    
    # Using filter() with lambda to keep numbers greater than 15
    filtered_numbers = list(filter(lambda x: x > 15, numbers))
    print(f"Numbers greater than 15: {filtered_numbers}")



# STEP 2: Program Introduction

def program_introduction():
    """Display program introduction"""
    
    print("    Welcome to Calculator Functions Program")
    print("="*50) 

def main():

    
    # STEP 2: Program Introduction
    program_introduction()
    
    # STEP 6:  global scope 
    print_app_name()
    

    # MINI PROJECT: Steps 2-5 (Calculator)
   
    
    main_calculator()

    # SEPARATE TASKS: Steps 6-9
 
  
    print("\nSEPARATE PRACTICE TASKS")
    
    
    # STEP 6: Already used with print_app_name()
    # STEP 7: Lambda Practice
    lambda_practice()
    
    # STEP 8: Map Practice
    map_practice()
    
    # STEP 9: Filter Practice
    filter_practice()
    
    # Program completion message
    print("\n" + "="*50)
    print("        All tasks completed successfully!")
  



# Program Entry Point

if __name__ == "__main__":
    main()
