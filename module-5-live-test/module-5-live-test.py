
# print("Module 5 Live Test : Print triangle from left")
# rows = int(input("Enter Number of rows: "))
# for i in range(1, rows+1):
#     print("*" * i)


#----------------------------------------------------------

# print("Module 5 Live Test: Print triangle from middle")
# rows = int(input("Enter Number of rows: "))
#
# for i in range(1, rows + 1):
#     # Calculate the number of spaces needed for alignment
#     spaces = " " * (rows - i)
#     # Calculate the odd number of asterisks for each row
#     asterisks = "*" * (2 * i - 1)
#
#     print(spaces + asterisks)

#alternative
print("Module 5 Live Test: Print triangle from middle: alternative Solution")
rows = int(input("Enter Number of rows: "))
max_width = 2 * rows - 1
for i in range(1, rows + 1):
    print(("*" * (2 * i - 1)).center(max_width))


'''
To print a triangle that expands from the middle outward (often called a pyramid), you need to account for leading spaces before the asterisks on each row.

As you go down the rows, the number of spaces decreases while the number of asterisks increases.

Here is how you can modify your code to achieve this:

Python
print("Module 5 Live Test: Print triangle from middle")
rows = int(input("Enter Number of rows: "))

for i in range(1, rows + 1):
    # Calculate the number of spaces needed for alignment
    spaces = " " * (rows - i)
    # Calculate the odd number of asterisks for each row
    asterisks = "*" * (2 * i - 1)
    
    print(spaces + asterisks)
How It Works
If you enter rows = 4, the loop breaks down like this:

Row (i)	Spaces (rows - i)	Asterisks (2 * i - 1)	Result
1	4−1=3	2(1)−1=1	*
2	4−2=2	2(2)−1=3	***
3	4−3=1	2(3)−1=5	*****
4	4−4=0	2(4)−1=7	*******
Alternative Shortcut: You can also use Python's built-in string centering method .center(), which handles the spacing math for you:

Python
max_width = 2 * rows - 1
for i in range(1, rows + 1):
    print(("*" * (2 * i - 1)).center(max_width))

'''