
# Author: Saif A Khan' Shubho
# Date: 17May2026

#step:2

print("_____________________________________")
print("Welcome to Daily Life Tracker Program")
print("_____________________________________")

#Step:3

userName= input("Please Enter your Name:").capitalize()
availableHours= int(input("Enter your today's available hour:" ))
dailyBudget= float(input("Enter your daily budget:"))

#step:4

print("_____________________")
print("Daily Activity Input:")
print("_____________________")



studyingPython = int(input("Please enter hour of each day for studying python:"))
practicingCoding= int(input("Please enter hour of each day for practicing coding:"))
otherActivities= int(input("Please enter hour of each day for doing other activities:"))

totalActivityHours= studyingPython+practicingCoding+otherActivities

#step:5

print("____________________")
print("Daily Expense Input:")
print("____________________")


foodExpense= float(input("Please enter your daily food expense:"))
transportExpense=float(input("Please enter your daily transport expense:"))
otherExpenses=float(input("Please enter your daily other expenses:"))

totalDailyExpense= foodExpense+transportExpense+otherExpenses



#Step:6(Compare)


if totalActivityHours>availableHours:
    print("You have planned more hours than available.")

else:
    print("Your daily plan is realistic.")


#Step:7(Compare)


if totalDailyExpense>dailyBudget:
    print("You have exceeded your daily budget.")

else:
    print("You are within your daily budget.")



#Step:8(Final)

print("_______________________")
print("Summary of Daily Report")
print("_______________________")
print(f"Hello {userName}")
print(f"Total Planned Hours: {totalActivityHours} ")
print(f"Total Available Hours: {availableHours}")
print(f"Total Expense: {totalDailyExpense:.2f}")
print(f"Remaining Budget: {dailyBudget-totalDailyExpense:.2f}")