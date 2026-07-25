
print("----Welcome to Mini Project – Score Tracker----")

#শিক্ষার্থীর নাম ও নম্বর রাখার জন্য একটি এমটি লিস্ট

all_students_records =[]

# একক শিক্ষার্থীর জন্য প্রাথমিক ব্যবহারকারীর ইনপুট গ্রহণ প্রক্রিয়া
# name=input("Enter Student Name: ")
# quiz_marks = float(input("Enter Quiz Marks: "))
# assignment_marks=float(input("Enter Assignment Marks: "))
# live_test_marks=float(input("Enter Live Test Marks:"))


#একাধিক শিক্ষার্থীর তথ্য অন্তর্ভুক্ত করার জন্য প্রোগ্রামটি সম্প্রসারিত করা হয়েছে।
#ব্যবহারকারী ইনপুট গ্রহণ বন্ধ করার জন্য "quit" না এন্ট্রি করা পর্যন্ত একটি ইনফিনিট while লুপ এর ব্যবহার

while True:
    name = input("\nEnter Student Name(or type 'quit' to stop): ").lower().strip()
    #method.lower() and.strip() are used to eliminate white space (.strip()) and convert user-inputted text to lower case.
    #মেথড .lower() এবং .strip() হোয়াইট স্পেস (.strip()) বাদ দিতে এবং ব্যবহারকারীর দেওয়া টেক্সটকে লোয়ার কেসে রূপান্তর করতে ব্যবহৃত

    if name == "":
        print("Name can not empty")
        continue

    if name == "quit":
        break #ইনপুট হিসাবে "quit" হলে প্রোগ্রামটি while লুপ শেষ করে print স্টেটমেন্টে চলে যাবে।



    #যথাক্রমে বিষয়ভিত্তিক নম্বর জানতে চাওয়া প্রক্রিয়া
    while True:
        try:
            quiz_marks = float(input("Enter Quiz Marks: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            assignment_marks = float(input("Enter Assignment Marks: "))
            break
        except ValueError:
            print ("Please enter a valid number.")
    while True:
        try:


            live_test_marks = float(input("Enter Live Test Marks:"))
            break
        except ValueError:
            print ("Please enter a valid number.")
    #বিষয়গুলোর নম্বর টাপল ভেরিয়েবলে সংরক্ষণ প্রক্রিয়া
    score=(quiz_marks,assignment_marks,live_test_marks)

    #নাম এবং বিষয়ের নম্বর গুলি একটি একক টাপল ভেরিয়েবলে সংরক্ষণ প্রক্রিয়া
    student_record=(name,score)

    #প্রাথমিকভাবে নেওয়া লিস্ট ভেরিয়েবলে ভেলু যোগ করার জন্য .append() মেথড ব্যবহার
    all_students_records.append(student_record)


if not all_students_records:
    print("No students were entered.")
else:
    print("\n-----Result Card-----")

#প্রতিটি রেকর্ড পড়ার জন্য একটি লুপ
    for record in all_students_records:
        student_name=record[0]  #ইনডেক্স শুন্য রিড করার জন্য
        subject_scores=record[1] #ইনডেক্স 'এক' রিড করার জন্য

    #প্রতিটি স্টুডেন্ট এর মোট নম্বর এবং গড় নম্বর বের করার জন্য।
        total_marks = sum(subject_scores)

        average = total_marks / len(subject_scores)

        grade = ""  #গ্রেডের ভেলু ধারণ করার জন্য একটি খালি ভেরিয়েবল

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "Fail"

    #প্রাপ্ত গ্রেড অনুযায়ী বার্তা তৈরির জন্য টারনারী অপারেটর প্রয়োগ
        status_txt = "qualified for the upcoming session" if grade != "Fail" else "disqualified for the upcoming session"

        print(f"Student Name    :{student_name.title()}")
        print(f"Scores          :{subject_scores}")
        print(f"Total   :{total_marks}  | Average  :{average:.2f}%")
        print(f"Grade obtained  :{grade}")
        print(f"You are {status_txt}\n")


'''
#Your Score Tracker project is now in solid shape: input validation for empty names, retry loops for invalid marks, a no-students-entered check, and
#accurate grade calculation per student. Good debugging instinct too — running it with multiple students to verify was the right move rather than just assuming it worked.

#expansion features of existing program


#Add sorting functionality: Sort by name, average marks, or grade
#Add search functionality: Find a specific student
#Add validation for duplicate names: Warn if same name is entered twice




Ah, now I understand! Since you're working with **lists, tuples, and control flow** specifically, let me give you suggestions that align with what you've learned so far. Your current code is actually quite good for this level!

## ✅ **What You Did Well**

1. **Proper use of lists** - `all_students_records` list to store multiple students
2. **Proper use of tuples** - `score = (quiz_marks, assignment_marks, live_test_marks)` and `student_record = (name, score)`
3. **Good control flow** - `while` loops for input validation, `if-elif-else` for grading
4. **Good use of `.append()`** - Adding records to the list
5. **Good use of `break` and `continue`** - Proper loop control
6. **Good exception handling** - Using `try-except` for numeric input

## 🎯 **Improvements Within Your Current Knowledge**

### 1. **Use Loop to Collect Marks (Instead of Repetition)**

Your current code repeats the same pattern 3 times. Since you've learned about loops, use one!

```python
# Instead of this:
quiz_marks = float(input("Enter Quiz Marks: "))
assignment_marks = float(input("Enter Assignment Marks: "))
live_test_marks = float(input("Enter Live Test Marks:"))

# Do this:
subjects = ("Quiz", "Assignment", "Live Test")  # Tuple of subject names
scores = []  # List to store marks

for subject in subjects:  # Loop through each subject
    while True:
        try:
            marks = float(input(f"Enter {subject} Marks: "))
            scores.append(marks)  # Add to list
            break
        except ValueError:
            print("Please enter a valid number.")

score = tuple(scores)  # Convert list to tuple
```

### 2. **Better Grade Calculation with Tuple of Grades**

Since you've learned tuples, use them for grade thresholds:

```python
# Define grade thresholds as parallel tuples
grade_names = ("A", "B", "C", "Fail")
grade_thresholds = (80, 70, 60, 0)

# Calculate grade using a loop
grade = "Fail"
for i in range(len(grade_thresholds)):
    if average >= grade_thresholds[i]:
        grade = grade_names[i]
        break
```

### 3. **Add Statistics Using List Operations**

Since you have a list of records, you can use list operations:

```python
# Calculate class statistics using lists
if all_students_records:
    # Extract all totals using list comprehension
    all_totals = [record[1][0] + record[1][1] + record[1][2] for record in all_students_records]
    
    # Find max, min using list functions
    highest = max(all_totals)
    lowest = min(all_totals)
    class_average = sum(all_totals) / len(all_totals)
    
    print("\n----- Class Statistics -----")
    print(f"Total Students: {len(all_students_records)}")
    print(f"Class Average: {class_average:.2f}%")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
```

### 4. **Better Data Organization with Nested Tuples**

Instead of flat tuples, organize data hierarchically:

```python
# Instead of:
student_record = (name, score)  # score is (quiz, assignment, live_test)

# You could do (though your way is fine):
student_record = (name, (quiz_marks, assignment_marks, live_test_marks))
# Access: name = student_record[0], marks = student_record[1][0] for quiz
```

### 5. **Find Top/Bottom Students Using Loops**

Since you have a list of records, find the best and worst students:

```python
# Find student with highest total
if all_students_records:
    highest_record = all_students_records[0]
    highest_total = sum(highest_record[1])
    
    for record in all_students_records[1:]:  # Start from second record
        total = sum(record[1])
        if total > highest_total:
            highest_total = total
            highest_record = record
    
    print(f"\n🏆 Top Student: {highest_record[0].title()} with {highest_total} marks")
```

### 6. **Search for Student by Name (Using Tuple of Names)**

Create a separate tuple of all names for searching:

```python
# Create a tuple of all student names
all_names = tuple(record[0] for record in all_students_records)

# Search functionality
search_name = input("\nEnter student name to search: ").lower().strip()
if search_name in all_names:
    for record in all_students_records:
        if record[0] == search_name:
            print(f"Found: {record[0].title()} - Total: {sum(record[1])}")
            break
else:
    print("Student not found")
```

### 7. **Filter Students by Grade (List Comprehension)**

Since you have lists, use list comprehensions:

```python
# Create lists of students by grade
failed_students = [record for record in all_students_records if record[1][0] + record[1][1] + record[1][2] / 3 < 60]
passed_students = [record for record in all_students_records if record[1][0] + record[1][1] + record[1][2] / 3 >= 60]

print(f"\nPassed: {len(passed_students)} students")
print(f"Failed: {len(failed_students)} students")
```

### 8. **Complete Refactored Code (Using Only Lists, Tuples, Control Flow)**

Here's your code optimized while keeping it at your learning level:

```python
print("----Welcome to Mini Project – Score Tracker----")

all_students_records = []
subjects = ("Quiz", "Assignment", "Live Test")  # Tuple of subject names
grade_thresholds = (80, 70, 60)  # Tuple of grade thresholds
grade_names = ("A", "B", "C")    # Tuple of grade names

while True:
    # Get student name
    name = input("\nEnter Student Name (or type 'quit' to stop): ").lower().strip()
    
    if name == "":
        print("Name cannot be empty")
        continue
    
    if name == "quit":
        break
    
    # Collect marks using a loop
    scores = []  # Temporary list for this student
    for subject in subjects:
        while True:
            try:
                marks = float(input(f"Enter {subject} Marks: "))
                scores.append(marks)  # Add to list
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Convert to tuple and store
    score_tuple = tuple(scores)  # (quiz, assignment, live_test)
    student_record = (name, score_tuple)
    all_students_records.append(student_record)

# Display results
if not all_students_records:
    print("No students were entered.")
else:
    print("\n----- Result Cards -----")
    
    # Variables for statistics
    all_totals = []
    highest_record = None
    highest_total = 0
    passed_count = 0
    failed_count = 0
    
    # Process each student
    for record in all_students_records:
        student_name = record[0]
        scores = record[1]  # Tuple of 3 marks
        
        total_marks = scores[0] + scores[1] + scores[2]  # Sum manually (since you know tuple has 3 items)
        average = total_marks / len(scores)
        
        # Calculate grade using loop and tuples
        grade = "Fail"
        for i in range(len(grade_thresholds)):
            if average >= grade_thresholds[i]:
                grade = grade_names[i]
                break
        
        # Track statistics
        all_totals.append(total_marks)
        if total_marks > highest_total:
            highest_total = total_marks
            highest_record = record
        
        if grade == "Fail":
            failed_count += 1
        else:
            passed_count += 1
        
        # Display student result
        status_txt = "qualified" if grade != "Fail" else "disqualified"
        print(f"\nStudent Name    : {student_name.title()}")
        print(f"Scores          : {scores}")
        print(f"Total   : {total_marks}  | Average  : {average:.2f}%")
        print(f"Grade obtained  : {grade}")
        print(f"You are {status_txt} for the upcoming session")
    
    # Display class statistics
    if all_students_records:
        print("\n----- Class Statistics -----")
        print(f"Total Students: {len(all_students_records)}")
        print(f"Average Score: {sum(all_totals) / len(all_totals):.2f}")
        print(f"Highest Score: {max(all_totals)}")
        print(f"Lowest Score: {min(all_totals)}")
        print(f"Passed: {passed_count} students")
        print(f"Failed: {failed_count} students")
        
        # Show top student
        if highest_record:
            print(f"\n🏆 Top Student: {highest_record[0].title()} with {highest_total} marks")
```

## 📝 **Key Learning Points to Remember**

| Concept | What You Used | What You Can Improve |
|---------|--------------|---------------------|
| **Lists** | `all_students_records` for storing records | Use lists for temporary data collection (like scores) |
| **Tuples** | `score = (quiz, assignment, live_test)` | Use tuples for fixed data (subjects, grades) |
| **Control Flow** | `while`, `if-elif-else`, `break`, `continue` | Use loops to avoid repetition |
| **List Operations** | `.append()` | Try `max()`, `min()`, `sum()`, list comprehensions |
| **Tuple Access** | `record[0]`, `record[1]` | Use tuple unpacking: `name, scores = record` |

## 🎓 **Suggested Practice Exercises**

1. **Modify the program to allow editing a student's marks**
2. **Add a feature to remove a student by name**
3. **Sort students by total marks (using bubble sort with lists)**
4. **Create a tuple of passed students and a tuple of failed students**
5. **Add subject-wise highest marks using list operations**

Your code is already at a good level for your learning stage! These suggestions will help you practice what you've learned while making the code cleaner. Good luck with your project! 🚀

'''