
#Mini Project – Score Tracker using list , tuple and loop

# Initialize an empty list to store all student records
all_students_scores = [] 
# data will be updated after all_students_scores.append() operation execute
# The Outer Layer (List of Tuples): 
# Finally, all_students_scores is a list that holds multiple of those student record tuples.

# Loop to add multiple students
while True:
    name = input("\nEnter student name (or type 'quit' to stop): ").strip()
    if name.lower() == 'quit':
        break
        
    math_score = float(input("Enter Math score: "))
    science_score = float(input("Enter Science score: "))
    english_score = float(input("Enter English score: "))
    
    # Store the individual student scores in an immutable tuple
    scores_tuple = (math_score, science_score, english_score)
  
    
    # Store the student's name and their score tuple as a single entry in the tuple
    student_record_tuple = (name, scores_tuple)

  

#1. What data type does student_record_tuple hold?The student_record_tuple variable holds data as a tuple.You created it using parentheses (name, scores_tuple), which defines a tuple in Python. Even though it contains a mix of text and another tuple, its outer container is strictly an immutable tuple.

#2. Is this called "tuple inside tuple" or "list inside list"?It is actually called a tuple inside a tuple, which is nested inside a list.Here is the exact structural breakdown of your data architecture from the inside out:
# 
# The Inner Layer (Tuple): scores_tuple is a tuple containing numbers: (1.0, 2.0, 3.0).
# 
# The Middle Layer (Tuple inside Tuple): student_record_tuple packages a string and that first tuple together: ('s', (1.0, 2.0, 3.0)). This is a tuple containing another tuple.
# 
# The Outer Layer (List of Tuples): Finally, all_students_scores is a list that holds multiple of those student record tuples.
# 
# If you look at the raw data structure of all_students_scores at the end of execution, it looks like this:python[ ('s', (1.0, 2.0, 3.0)), ('d', (2.0, 3.0, 5.0)) ]


    all_students_scores.append(student_record_tuple) # data inserted into list using append method

# Display the tracked scores
print("\n--- Final Score Tracker ---")
for x in all_students_scores: #reading from list using loop
    student_name = x[0] # first index
    subject_scores = x[1] # second index
    
    total=sum(subject_scores) #example sum(1.0, 2.0, 3.0)
    average = total / len(subject_scores) # len() functions identifies number of tuple element

    print(f"Student: {student_name}")
    print(f"  Scores: {subject_scores}")
    print(f"  Total: {total} | Average: {average:.2f}\n")
   

    #refernce:

    #https://www.google.com/search?client=firefox-b-lm&q=Mini+Project+%E2%80%93+Score+Tracker+using+list+%2C+tuple+and+loop&udm=50&fbs=ABfTbFVyMZGZf1hfvX9uKjN_-G8c4u0nXx4bEIpwm1lnNH832a9BVCEiB2iPJNekNderQwJGZIG7YID1eBGNWasq2rzBIURiSCrdR156KVg_RXap7nymj7qwomXHj_SiILyyw7Ta9Q-KE-MaWxqo7jHrqQyEW5GYd4Al-Ng6PS506BSWStYgV2V047447UIBRUyB2GwDFWjsD_zdq4DE4Jd0AqJizczSNg&aep=10&ntc=1&mstk=AUtExfD4Yp5w_lorcCutvjumY-DxUtll4nvmK7v9etPwXBBM65jsZgnoVgXwKm1KUNlxZ2aWArwH3zdN6de-ejOO5xf2PhOBzIfx42bWfLQdYUQWVjs2zYbEt88VJhGUyBBDz6eke3KM7t9bHlZkHsdg3WaOzjaEAaidxte1biw3RS1bGokjxMhw7OeiJqyeT9V5ZXweH7TNMS9JEqLvoK6vlcZPBHO_nrmLWmIFkIxK4V_qO27uETgjbiwSGX8INdX8x0tNzGBCYOB0rrVtAYgqZedH7kUFQVc13w5kGbPFe1HZI67V6usI2VNF7fmim7iKHnmsEOh4B4ENNQ&aioh=3&csuir=1&mtid=qPs_arjXO4GL4-EP1Pn4kA8
