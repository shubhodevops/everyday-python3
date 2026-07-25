# Module-6 Assignment
# Author: Saif A Khan Shubho
# Date: 05 JuLY 2026

print("\n---------------------------------------------")
print("    Welcome to Student Score Tracker System    ")
print("---------------------------------------------")

student_name = []
student_score = []


#Step 3: Student Data Input

while True:
    try:
        no_of_students = int(input("How many students you want to enter?: "))
        if no_of_students > 0:
            break
        print("Please enter a number greater than zero")
    except ValueError:
        print("Please enter a valid whole number.")


for student in range(1, no_of_students + 1):
    print(f"\nScore Entry for the Student #{student}::")


    while True:
        name = input("\nEnter Student Name: ").strip().title()
        if name != "":
            break
        print("Student Name cannot be empty. Please try again.")


    while True:
        try:
            score = float(input("Enter Student Score: "))
            if 0 <= score <= 100:
                break
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Please enter a valid numeric value.")


    student_name.append(name)
    student_score.append(score)


#Step 4: Display All Scores
print(f"{'\nStudent Name':<25} Score")
print("-" * 32)
for n in range(no_of_students):
    print(f"{student_name[n]:<25} {student_score[n]}")
print("-" * 32)


# Step 5: Highest and Lowest Score
print(f"\nScore Summary:")
print(f"{'\tHighest' :<18}:{max(student_score)}")
print(f"{'\tLowest' :<18}:{min(student_score)}")


#Step 8: Average Score Calculation
print(f"{'\tAverage' :<18}:{sum(student_score)/len(student_score):.1f}%")


#Step 6: Convert Scores to Tuple
student_score_in_tuple = tuple(student_score)
print("\nScores in Tuple:", student_score_in_tuple)


#Step 7: Tuple Unpacking
#Store first three scores (if available) into variables using unpacking and print them.


if len(student_score_in_tuple) >= 3:

    score1, score2, score3, *remaining_scores = student_score_in_tuple
    print(f"First Score  : {score1}")
    print(f"Second Score : {score2}")
    print(f"Third Score  : {score3}")
else:
    print("\nAt least 3 student's score required for tuple unpacking!")

