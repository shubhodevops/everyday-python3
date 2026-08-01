# Method A: Read the entire file as a single string
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Method B: Read line-by-line using a loop (Memory efficient for large files)
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # .strip() removes extra newlines

# Method C: Read all lines into a list of strings
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)


#Warning: Overwrites existing content if the file already exists.

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello World!\n")
    file.write("This is a new line.")

#Adds content to the end of the file safely.

with open("output.txt", "a", encoding="utf-8") as file:
    file.write("\nThis line is appended to the bottom.")

#To delete files, you must import the built-in os module.
import os

if os.path.exists("old_file.txt"):
    os.remove("old_file.txt")
else:
    print("The file does not exist")

#The exclusive creation mode ('x') acts as a safety guard to prevent you from accidentally overwriting existing data.

try:
    with open("new_report.txt", "x", encoding="utf-8") as file:
        file.write("This file is brand new!")
    print("File created successfully.")
except FileExistsError:
    print("Error: The file already exists. Choose a different name.")

#1. Reading a CSV File

import csv

# Option A: Reading as a list of strings
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skips and saves the first row (headers)
    print("Headers:", header)
    
    for row in reader:
        print(row)  # row[0] is the first column, row[1] is the second

# Option B: Reading as a dictionary (Recommended for scannability)
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])  # Access columns by header names


#2. Writing a CSV File
import csv

headers = ["Name", "Role", "Salary"]
data = [
    ["Alice", "Developer", "90000"],
    ["Bob", "Designer", "75000"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Writes a single row
    writer.writerows(data)    # Writes multiple rows at once


# csv.reader: Converts rows into Python lists.
# csv.DictReader: Converts rows into Python dictionaries.



