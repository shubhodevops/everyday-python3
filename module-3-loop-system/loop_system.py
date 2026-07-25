# Author: Saif A Khan Shubho
# Date: 13 June 2026

import string # module import for use of string.capwords()

print("\n-----------------------------------------")
print(" Welcome to Smart Task Repetition System   ")
print("-----------------------------------------")

taskName = input("Enter task name: ")
targetRepetitions = int(input(f"How often do you complete this task on today? ({string.capwords(taskName)}): "))
 #string.capwords()for displaying each word's first letter in uppercase.

for num in range(1, targetRepetitions +1 ):
    print(f"Task[{num}]: '{string.capwords(taskName)}' completed.")
   


countDown= int(input("Enter a count down number: "))
print("---Result---\n")
while countDown>0:
    print(countDown)
    countDown-=1


print("\nDaily Schedule:\n")

#Using For Loops:
for n in range(2):
    #Start Inner loop:
    for task in range(1, 4): # 3 times run for inner loops
        if n == 0:
            print(f"Morning Task {task}")
        else:
            print(f"Evening Task {task}")
else:
    print("\n--Using For Loop\n")


#using While loops:
num = 0 # Initialize outer loop counter (replaces range(2))
while num < 2:


    task = 1 # Initialize inner loop counter (replaces range(1, 4))
    while task < 4: # 3 times run for inner loops
        if num == 0:
            print(f"Morning Task {task}")
        else:
            print(f"Evening Task {task}")


        task += 1 # Increment inner counter so it moves from 1 to 2 to 3


    num += 1 # Increment outer counter so it moves from 0 to 1
else:
    print("\n--Using While Loop")
