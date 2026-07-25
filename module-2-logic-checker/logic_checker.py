import string

print("\n---------------------------------------------------")
print("Welcome to Smart Eligibility & Performance Checker  ")
print("---------------------------------------------------")

#name = string.capwords(input("Enter your Name: "))
name=input("Enter your Name: ")

age=int(input("Enter your Age: "))
if age <18:
    print("You are not eligible due to age restrictions.")
    exit()
else:
    print("Age requirement passed.")

examScore=int(input("Enter an Exam score: "))
if not 0 <= examScore <= 100:
    print("Invalid score. It must be between 0 and 100. Try again!")
    exit()

monthlyIncome=float(input("Enter your monthly income: "))

if age >=18:
    if examScore >=60:
        print("You passed the program.")
    else:
        print("You failed the program.")  
else:
    print("Program access denied.")

grade ="" # Initialize an empty variable to hold the grade score status

if examScore>=90 and examScore<=100:
    grade="A"
elif examScore>=75:
    grade="B"
elif examScore>=60:
    grade="C"
else:
    grade="Fail"    

eligibleCheck="" # Initialize an empty variable to hold the eligibility check status

if monthlyIncome < 20000 and examScore > 75:
    eligibleCheck="Eligible for scholarship support."
   
else:
   eligibleCheck="Not eligible for scholarship."


print("\n----------------------------------------------")
print("                FINAL Summary                   ")
print("----------------------------------------------")
print(f"Name               :{string.capwords(name)}")
print(f"Age                :{age} years old")
print(f"Score              :{examScore}")
print(f"Grade              :{grade}")
print(f"Scholarship status :{eligibleCheck}")






