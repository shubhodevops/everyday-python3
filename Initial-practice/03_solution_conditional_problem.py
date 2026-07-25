print("\n------------------------------")
print("   Student Grade Calculator     ")
print("-------------------------------")

#business:
#implement very basic check user score input between 1  and 100
#zero or negetive number not allowed, program will be terminated
#score allowed only received intiger number

studentName= input("Enter a Student Name: ").strip().title()

try:
    score = int(input("Enter student's score number: "))

except ValueError:
    print("Invalid Input! Only Number Allowed, Score Number between 1 and 100")
    
    exit()   

gradeStatus ="" #initialize a varible to hold score grade result

if score <= 0:
    print("Invalid Input Number. Zero or negetive number not allowed, try once again!")
    exit()
elif score > 100:
    print("Invalid Input Number. Score Number between 1 and 100")    
    exit()
elif 90 <= score <= 100:
    gradeStatus="A"

elif 80 <= score <= 89:
    gradeStatus="B"

elif 70 <= score <= 79:
    gradeStatus="C"

elif 60 <= score <= 69:
    gradeStatus="D"

else:
    gradeStatus="Fail"


print("\n--------------------------")
print("   Student Result Card      ")
print("---------------------------")
print(f"Student Name :{studentName}")
print(f"Result       :Grade - {gradeStatus} (Score: {score})")




