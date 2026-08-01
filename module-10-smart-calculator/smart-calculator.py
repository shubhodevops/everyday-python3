# =============================================
# STEP 6: Global Scope Practice (Separate Task)
# =============================================
app_name = "Smart Calculator"

def print_app_name():
    """Function to demonstrate global scope"""
    print(f"Application Name: {app_name}")


# =============================================
# STEP 3: Calculator Functions
# =============================================
def addition(num1, num2):
    """Returns the sum of two numbers"""
    return num1 + num2

def subtraction(num1, num2):
    """Returns the difference of two numbers"""
    return num1 - num2

def multiplication(num1, num2):
    """Returns the product of two numbers"""
    return num1 * num2

def division(num1, num2):
    """Returns the quotient of two numbers"""
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

def modulus(num1, num2):
    """Returns the remainder of division"""
    if num2 == 0:
        return "Error: Cannot perform modulus with zero!"
    return num1 % num2

def power(num1, num2):
    """Returns num1 raised to the power of num2"""
    return num1 ** num2

def floor_division(num1, num2):
    """Returns the floor division result"""
    if num2 == 0:
        return "Error: Cannot perform floor division by zero!"
    return num1 // num2


# =============================================
# STEP 11: Advanced Calculator Functions
# =============================================
def percentage_calculator(num1, num2):
    """Calculates what percentage num1 is of num2"""
    if num2 == 0:
        return "Error: Cannot calculate percentage with zero as total!"
    return (num1 / num2) * 100

def square_root(num):
    """Returns the square root of a number"""
    if num < 0:
        return "Error: Cannot calculate square root of negative number!"
    return num ** 0.5

def cube(num):
    """Returns the cube of a number"""
    return num ** 3

def cube_root(num):
    """Returns the cube root of a number"""
    if num < 0:
        return -((-num) ** (1/3))
    return num ** (1/3)

def maximum_of_two(num1, num2):
    """Returns the maximum of two numbers"""
    return max(num1, num2)

def minimum_of_two(num1, num2):
    """Returns the minimum of two numbers"""
    return min(num1, num2)


# =============================================
# STEP 4: Calculator Menu
# =============================================
def display_menu():
    """Displays the main calculator menu"""
    print("\n" + "="*40)
    print("        SMART CALCULATOR")
    print("="*40)
    
    menu_items = [
        "Addition",
        "Subtraction", 
        "Multiplication",
        "Division",
        "Modulus",
        "Power",
        "Floor Division",
        "Advance Calculator",
        "Exit"
    ]
    
    for index, item in enumerate(menu_items, start=1):
        print(f"    {index}. {item}")
    
    print("="*40)

def display_advanced_menu():
    """Displays the advanced calculator menu"""
    print("\n" + "="*40)
    print("     ADVANCE CALCULATOR")
    print("="*40)
    
    advanced_items = [
        "Percentage Calculator",
        "Square Root",
        "Cube",
        "Cube Root",
        "Maximum of Two Numbers",
        "Minimum of Two Numbers",
        "Return to Main Calculator"
    ]
    
    for index, item in enumerate(advanced_items, start=1):
        print(f"    {index}. {item}")
    
    print("="*40)

def get_number(prompt="Enter a number: "):
    """Helper function to get valid number input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_two_numbers():
    """Helper function to get two numbers from user"""
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    return num1, num2

def perform_calculation(operation_func, num1, num2=None):
    """Performs calculation and displays result"""
    if num2 is not None:
        result = operation_func(num1, num2)
    else:
        result = operation_func(num1)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")

def main_calculator():
    """Main calculator program"""
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-9): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        # Exit
        if choice == 9:
            print("\nThank you for using Smart Calculator! Goodbye!")
            break
        
        # Main operations (1-7)
        elif 1 <= choice <= 7:
            num1, num2 = get_two_numbers()
            
            operations = {
                1: addition,
                2: subtraction,
                3: multiplication,
                4: division,
                5: modulus,
                6: power,
                7: floor_division
            }
            
            perform_calculation(operations[choice], num1, num2)
        
        # Advanced Calculator (8)
        elif choice == 8:
            advanced_calculator()
        
        # Invalid choice
        else:
            print("Invalid choice! Please select a number between 1 and 9.")

def advanced_calculator():
    """Advanced calculator sub-menu"""
    while True:
        display_advanced_menu()
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue
        
        # Return to main menu
        if choice == 7:
            break
        
        # Advanced operations
        elif choice == 1:  # Percentage
            num1, num2 = get_two_numbers()
            perform_calculation(percentage_calculator, num1, num2)
        
        elif choice == 2:  # Square Root
            num = get_number("Enter a number to find square root: ")
            perform_calculation(square_root, num)
        
        elif choice == 3:  # Cube
            num = get_number("Enter a number to cube: ")
            perform_calculation(cube, num)
        
        elif choice == 4:  # Cube Root
            num = get_number("Enter a number to find cube root: ")
            perform_calculation(cube_root, num)
        
        elif choice == 5:  # Maximum
            num1, num2 = get_two_numbers()
            perform_calculation(maximum_of_two, num1, num2)
        
        elif choice == 6:  # Minimum
            num1, num2 = get_two_numbers()
            perform_calculation(minimum_of_two, num1, num2)
        
        else:
            print("Invalid choice! Please select a number between 1 and 7.")


# =============================================
# STEP 7: Lambda Practice (Separate Task)
# =============================================
def lambda_practice():
    """Demonstrates lambda function for squaring numbers"""
    print("\n" + "="*40)
    print("        LAMBDA PRACTICE")
    print("="*40)
    
    square = lambda x: x ** 2
    
    try:
        num = float(input("Enter a number to square: "))
        print(f"The square of {num} is: {square(num)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


# =============================================
# STEP 8: Map Function Usage (Separate Task)
# =============================================
def map_practice():
    """Demonstrates map() with lambda function"""
    print("\n" + "="*40)
    print("        MAP PRACTICE")
    print("="*40)
    
    numbers = [5, 10, 15, 20, 25]
    print(f"Original list: {numbers}")
    
    # Increase every number by 10 using map with lambda
    increased_numbers = list(map(lambda x: x + 10, numbers))
    print(f"After adding 10: {increased_numbers}")


# =============================================
# STEP 9: Filter Function Usage (Separate Task)
# =============================================
def filter_practice():
    """Demonstrates filter() with lambda function"""
    print("\n" + "="*40)
    print("        FILTER PRACTICE")
    print("="*40)
    
    numbers = [5, 10, 15, 20, 25]
    print(f"Original list: {numbers}")
    
    # Keep only numbers greater than 15 using filter with lambda
    filtered_numbers = list(filter(lambda x: x > 15, numbers))
    print(f"Numbers greater than 15: {filtered_numbers}")


# =============================================
# STEP 2: Program Introduction
# =============================================
def main():
    """Main program entry point"""
    print("="*50)
    print("        Welcome to Smart Calculator")
    print("="*50)
    
    # STEP 6: Demonstrate global scope
    print_app_name()
    
    # Run the main calculator
    main_calculator()
    
    # STEP 7: Lambda practice
    lambda_practice()
    
    # STEP 8: Map practice
    map_practice()
    
    # STEP 9: Filter practice
    filter_practice()
    
    print("\n" + "="*50)
    print("        Thank you for using Smart Calculator!")
    print("="*50)


# =============================================
# Program Entry Point
# =============================================
if __name__ == "__main__":
    main()
