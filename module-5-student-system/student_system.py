# Module-5 Assignment
# Author: Saif A Khan Shubho
# Date: 21 June 2026


print("\n--------------------------------------------------")
print(" Welcome to Smart Student Life Management System    ")
print("--------------------------------------------------")

# Step 2:
student_name = input("Enter student name: ").strip().title()
student_id = input("Enter student ID: ").strip()

try:

    study_hours = float(input("Enter daily study hours: "))
    if not (0 < study_hours <= 24):
        raise ValueError("Study hours must be between 1 and 24.")

    monthly_pocket_money = float(input("Enter monthly pocket money amount (BDT): "))
    if monthly_pocket_money < 0:
        raise ValueError("Pocket money cannot be a negative amount.")

except ValueError:
    print("\nError: Please enter a valid numerical value.")
    exit()

# ----Declare variables to avoid crash on exit----
attendance_percentage = 0
grade = "Not calculated"
total_expense = 0.0
remaining_money = monthly_pocket_money


# Step 3:
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Class Attendance Tracker")
    print("2. Study Session Manager")
    print("3. Exam Result Checker")
    print("4. Monthly Expense Tracker")
    print("5. Daily Problem Solver")
    print("6. Exit")

    menuOpt = int(input("\nChoose an option between 1 and 6: "))





# Step 4:
    if menuOpt == 1:
        print("\nClass Attendance Tracker:")
        try:
            total_classes = int(input("Enter number of total classes:   "))

            if total_classes <= 0:
                print("Error: Total classes must be greater than zero.")
            else:
                attended_classes = int(input("Enter number of attended classes: "))

                if attended_classes < 0 or attended_classes > total_classes:
                    print(
                        "Error: Attended classes cannot be negative or exceed total classes."
                    )
                else:
                    attendance_percentage = (attended_classes / total_classes) * 100

                    eligibility_check = "Eligible for exam" if attendance_percentage >= 75 else "Not eligible for exam"


                    print("\n-----------------------")
                    print(f"Attendance: {attendance_percentage:.1f}%")
                    print(eligibility_check)
                    print("-----------------------")



        except ValueError:
            print("Error: Please enter valid whole numbers.")






# Step 5:
    elif menuOpt == 2:
        print("\nStudy Session Manager:")
        subject_name = input("Enter a subject name: ").strip()

        try:
            study_sessions = int(input("Enter a number of study sessions: "))

            if study_sessions < 0:
                print("Error: Please enter a number greater than 0.")
            else:

                for session in range(1, study_sessions + 1):
                    print(f"{subject_name} Study Session {session} Completed")


                session_status = input("\nDid you complete all planned sessions? (yes/no): ").strip().lower()

                message = "Great consistency!" if session_status == "yes" else "Try to improve tomorrow."

                print("\n-------------------------")
                print(message)
                print("-------------------------")

        except ValueError:
            print("Error: Please enter a valid whole number for study sessions.")







# Step 6:
    elif menuOpt == 3:
        print("\nExam Result Checker:")
        while True:
            try:
                python_marks = float(input("Enter python Marks (0-100): "))
                if 0 <= python_marks <= 100:
                    break
                print("Enter a valid score between 0 and 100")
            except ValueError:
                print("Invalid input!, Enter Numbers only")

        while True:
            try:
                math_marks = float(input("Enter Math Marks (0-100): "))
                if 0 <= math_marks <= 100:
                    break
                print("Enter a valid score between 0 and 100")
            except ValueError:
                print("Invalid input!, Enter Numbers only")

        while True:
            try:
                english_marks = float(input("Enter English Marks (0-100): "))
                if 0 <= english_marks <= 100:
                    break
                print("Enter a valid score between 0 and 100")
            except ValueError:
                print("Invalid input!, Enter Numbers only")

        total_marks = python_marks + math_marks + english_marks
        average_mark = total_marks / 3

        

        if average_mark >= 80:
            grade = "A"
        elif average_mark >= 70:
            grade = "B"
        elif average_mark >= 60:
            grade = "C"
        else:
            grade = "Fail"

        print("\n-----------------------")
        print(f"Final Grade: {grade}")
        print("-----------------------")    





# Step 7:
    elif menuOpt == 4:
        print("\nMonthly Expense Tracker:")
        food = float(input("Enter Food expense: "))
        internet = float(input("Enter Internet expense: "))
        transport = float(input("Enter Transport expense: "))
        other = float(input("Enter Other expense: "))

        total_expense = food + internet + transport + other
        remaining_money = monthly_pocket_money - total_expense

        expense_tracker_txt ="Budget Limit Crossed." if total_expense > monthly_pocket_money else "You managed your expenses well."

        print("\n------------------------------")
        print(expense_tracker_txt)
        print("------------------------------")




# Step 8:
    elif menuOpt == 5:
        print("\nDaily Problem Solver Submenu:")

        showSubMenu="yes"

        while showSubMenu=="yes" or showSubMenu=="y":
            print("1. Even or Odd Checker")
            print("2. Largest Number Finder")
            print("3. Simple Sum Calculator")

            submenu_opt =int(input("\nChoose an Submenu option between 1 and 3: "))

            if submenu_opt ==1:
                print("\nEven or Odd Checker:")

                user_num = int(input("Enter number for checking even or odd: "))
                num_checker="Even Number" if user_num % 2 ==0 else "Odd Number"

                print("\n--------------------------")
                print(f"{user_num} is {num_checker}")
                print("--------------------------")


            elif submenu_opt==2:
                print("\nLargest Number Finder:")

                largest = 0
                counter = 0

                while counter < 3:
                    num = int(input(f"Enter a number of {counter + 1}: "))

                    if largest == 0 or num > largest:

                        largest = num

                    counter += 1

                print("\n---------------------------------")
                print(f"Largest number is {largest}       ")
                print("---------------------------------")


            elif submenu_opt == 3:
                print("\nSimple Sum Calculator:")

                total_sum=0

                for i in range(2):
                    calculate_num=int(input(f"Enter a number of {i+1}: "))
                    total_sum +=calculate_num

                print("\n---------------------------------")
                print(f"Sum of two numbers: {total_sum}   ")
                print("---------------------------------")

            else:
                print("\nInvalid choice! Choose an option between 1 and 3")
                continue
            showSubMenu = input("\nDo you want to solve another problem? (yes/no): ").lower().strip()




    elif menuOpt == 6:

#Step 9: Countdown Timer:

        countDown= int(input("\nEnter a countdown number: "))
        print("\n---Result---")
        while countDown>0:
            print(countDown)
            countDown-=1
        else:
            print("Session Finished Successfully.")


# Step 10:
        no_record_txt = "No class record found!" if attendance_percentage == 0 else f"{attendance_percentage:.1f}%"
        #-----------------------------------------

        print("\n========== FINAL SUMMARY ==========")
        print(f"Student Name        :{student_name.title()}")
        print(f"Student Id          :{student_id}")
        print(f"Attendance          :{no_record_txt}")
        print(f"Last Grade          :{grade}")
        print(f"Monthly Expense     :{total_expense:.2f}BDT")
        print(f"Remaining Balance   :{remaining_money:.2f}BDT")
        print("\nThank You For Using The System.")

        exit()

    else:
        print("\nInvalid choice! Choose an option between 1 and 6")
        continue





