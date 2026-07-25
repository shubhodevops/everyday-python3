for i in range(1, 6):
    square = i * i
    print(square)


# Second Example


# printTable() prints table of number and takes
# 1 required value that is number of whose table to be printed
# and an optional input i whose default value is 1

"""
In this method, we pass i as an additional parameter with initial value as 1. We print n * i and then recursively call for i+1. We stop the recursion when i becomes 11 as we need to print only 10 multiples of given number and i.
"""


def printTable(n, i=1):

    if i == 11:  # base case
        return
    print(n, "*", i, "=", n * i)
    i += 1
    printTable(n, i)


if __name__ == "__main__":
    n = 5
    printTable(n)


# Python Program to print table of a number || another example of Printing Table


def printTable(n):

    for i in range(1, 11):

        # multiples from 1 to 10
        print("%d * %d = %d" % (n, i, n * i))


if __name__ == "__main__":
    n = 5
    printTable(n)
