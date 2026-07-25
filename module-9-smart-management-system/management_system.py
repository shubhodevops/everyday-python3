# =============================================
# VARIABLE INITIALIZATION - Setting up data storage
# =============================================

# Creates an empty list to store student names
student_names = list()
# Creates an empty list to store student scores (parallel to student_names)
student_scores = list()
# Creates an empty dictionary to store contacts (name: phone number)
contact_book = dict()
# Creates an empty set to store unique product categories (no duplicates allowed)
product_categories = set()
# Creates an empty dictionary to store voting results (candidate: vote count)
voting_results = dict()

# =============================================
# WELCOME MESSAGE - Program header
# =============================================

# Prints a decorative welcome banner with separator lines
print("\n==============================================================")
# Prints the main title of the application
print("  Welcome to Smart School Management & Voting Analysis System   ")
# Prints the closing decorative line
print("==============================================================\n")

# =============================================
# MAIN MENU - Primary navigation options
# =============================================

# Creates a tuple of menu options (immutable, ordered collection)
main_menu_options = ("Add Student Scores", "View Score Summary", "Manage Contacts", "Manage Inventory", "Run Voting System", "Searching Feature", "Student Performance Report", "Exit")

# =============================================
# MAIN PROGRAM LOOP - Continues until user exits
# =============================================

# Infinite while loop to keep the program running
while True:
    # Prints the MAIN MENU header
    print("\n--- MAIN MENU ---")

    # Loops through each menu option with its index (starting from 1)
    for index, option in enumerate(main_menu_options, start=1):
        # Prints the menu number and option name
        print(f"{index}. {option}")

    # Prompts user for choice and removes extra whitespace
    choice = input("\nEnter your choice (1-8): ").strip()

    # =============================================
    # OPTION 1: ADD STUDENT SCORES
    # =============================================
    
    # Checks if user selected option 1
    if choice == "1":
        # Prints section header
        print("\n--- Add Student Scores ---")
        
        # Input validation loop for number of students
        while True:
            try:
                # Tries to convert input to integer
                num_students = int(input("How many students to enter? "))
                # Checks if number is negative
                if num_students < 0:
                    print("Please enter a positive number.")
                    continue  # Restarts the loop
                break  # Exits loop if valid input
            except ValueError:
                # Handles non-integer input
                print("Invalid input. Please enter a valid integer.")

        # Loop to collect each student's details
        for i in range(num_students):
            # Shows which student number is being entered
            print(f"\nEntering details for student {i+1}:")

            # Gets student name and removes whitespace
            name = input("Enter student name: ").strip()

            # Validation loop for non-empty name
            while not name:
                print("Name cannot be empty.")
                name = input("Enter student name: ").strip()

            # Validation loop for score input
            while True:
                try:
                    # Gets score as float
                    score = float(input(f"Enter score for {name}: "))
                    # Validates score is between 0 and 100
                    if 0 <= score <= 100:
                        break  # Exits loop if valid
                    print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Adds validated name and score to respective lists
            student_names.append(name)
            student_scores.append(score)

        # Display all current student records
        print("\nCurrent Student Records:")
        # Iterates through students with index
        for s, s_name in enumerate(student_names):
            # Prints each student with their score
            print(f" - {s_name}: {student_scores[s]}")

        # Converts scores list to immutable tuple
        scores_tuple = tuple(student_scores)
        # Displays the tuple
        print(f"\nScore in Tuple: {scores_tuple}")

    # =============================================
    # OPTION 2: VIEW SCORE SUMMARY
    # =============================================
    
    elif choice == "2":
        print("\n--- Score Summary ---")

        # Checks if there are any scores to analyze
        if not student_scores:
            print("No student data available. Please add student scores first.")
            continue  # Skips to next loop iteration

        # Initialize variables with first score
        highest_score = student_scores[0]
        lowest_score = student_scores[0]
        total_score = 0

        # Loop through all scores to find min, max, and sum
        for score in student_scores:
            # Updates highest score if current is greater
            if score > highest_score:
                highest_score = score
            # Updates lowest score if current is smaller
            if score < lowest_score:
                lowest_score = score
            # Adds to total sum
            total_score += score

        # Calculates average (total divided by count)
        average_score = total_score / len(student_scores)

        # Displays statistics with formatting
        print(f"Highest Score: {highest_score}")
        print(f"Lowest Score : {lowest_score}")
        print(f"Average Score: {average_score:.2f}")  # 2 decimal places

    # =============================================
    # OPTION 3: MANAGE CONTACTS
    # =============================================
    
    elif choice == "3":
        # Sub-menu options for contact management
        contact_menu_options = ("Add Record", "Update Record", "Delete Record", "View All Records", "Return to Main Menu" )

        # Contact management sub-loop
        while True:
            print("\n--- Contact Book Menu ---")
            
            # Display contact menu options
            for i, opt in enumerate(contact_menu_options, start=1):
                print(f"  {i}. {opt}")

            # Get user's sub-choice
            sub_choice = input("Select an option (1-5): ").strip()

            # =============================================
            # CONTACT SUB-OPTION 1: ADD RECORD
            # =============================================
            
            if sub_choice == "1":
                # Get contact name
                name = input("Enter contact name: ").strip()
                
                # Check if contact already exists
                if name in contact_book:
                    print("Contact already exists. Use update option to change.")
                # Check if name is not empty
                elif name:
                    # Get phone number
                    phone = input("Enter phone number: ").strip()
                    # Add to dictionary
                    contact_book[name] = phone
                    print(f"Contact '{name}' added successfully.")
                else:
                    print("Name cannot be empty.")

            # =============================================
            # CONTACT SUB-OPTION 2: UPDATE RECORD
            # =============================================
            
            elif sub_choice == "2":
                # Get name to update
                name = input("Enter contact name to update: ").strip()
                
                # Check if contact exists
                if name in contact_book:
                    # Get new phone number
                    phone = input("Enter new phone number: ").strip()
                    # Update dictionary
                    contact_book[name] = phone
                    print(f"Contact '{name}' updated successfully.")
                else:
                    print("Contact not found.")

            # =============================================
            # CONTACT SUB-OPTION 3: DELETE RECORD
            # =============================================
            
            elif sub_choice == "3":
                # Get name to delete
                name = input("Enter contact name to delete: ").strip()
                
                # Check if contact exists
                if name in contact_book:
                    # Remove from dictionary
                    del contact_book[name]
                    print(f"Contact '{name}' deleted.")
                else:
                    print("Contact not found.")

            # =============================================
            # CONTACT SUB-OPTION 4: VIEW ALL RECORDS
            # =============================================
            
            elif sub_choice == "4":
                print("\n--- Contact List ---")
                
                # Check if contact book is empty
                if not contact_book:
                    print("[Contact book is empty]")
                else:
                    # Iterate through all contacts
                    for k, v in contact_book.items():
                        # Display each contact
                        print(f" Name: {k} - Phone Number: {v}")

            # =============================================
            # CONTACT SUB-OPTION 5: RETURN TO MAIN MENU
            # =============================================
            
            elif sub_choice == "5":
                break  # Exit contact sub-menu

            else:
                print("Invalid option. Try again.")

    # =============================================
    # OPTION 4: MANAGE INVENTORY
    # =============================================
    
    elif choice == "4":
        # Inventory sub-menu options
        inventory_menu_options = ("Add Unique Category", "Display Categories", "Math Operations (Union & Difference)", "Return to Main Menu")

        # Inventory management sub-loop
        while True:
            print("\n--- Inventory Category Management ---")
            # Display inventory menu
            for x, y in enumerate(inventory_menu_options, start=1):
                print(f"  {x}. {y}")

            # Get user's sub-choice
            sub_choice = input("Select an option (1-4): ").strip()

            # =============================================
            # INVENTORY SUB-OPTION 1: ADD CATEGORY
            # =============================================
            
            if sub_choice == "1":
                # Get category name
                cat = input("Enter unique product category: ").strip()
                
                # Check if category is not empty
                if cat:
                    # Add to set (automatically prevents duplicates)
                    product_categories.add(cat)
                    print(f"Category '{cat}' added to primary inventory set.")

            # =============================================
            # INVENTORY SUB-OPTION 2: DISPLAY CATEGORIES
            # =============================================
            
            elif sub_choice == "2":
                # Display current categories
                print(f"Unique Primary Categories: {product_categories}")

            # =============================================
            # INVENTORY SUB-OPTION 3: SET OPERATIONS
            # =============================================
            
            elif sub_choice == "3":
                print("\nLet's create a Secondary Set to compare with.")
                # Create new empty set
                secondary_set = set()

                # Input validation for number of items
                while True:
                    try:
                        num_items = int(input("How many items for secondary set? "))
                        # Check for non-negative number
                        if num_items >= 0:
                            break
                        print("Please enter a positive number.")
                    except ValueError:
                        print("Invalid input. Please enter an integer.")

                # Collect items for secondary set
                for i in range(num_items):
                    item = input(f"Enter item {i+1}: ").strip()
                    if item:  # Only add non-empty items
                        secondary_set.add(item)

                # Display both sets
                print(f"\nPrimary Set  : {product_categories}")
                print(f"Secondary Set  : {secondary_set}")

                # Perform set operations
                union_set = product_categories.union(secondary_set)  # All items from both sets
                diff_set = product_categories.difference(secondary_set)  # Items only in primary

                # Display results
                print(f"Union (All Items Combined)       : {union_set}")
                print(f"Difference (Primary - Secondary) : {diff_set}")

            # =============================================
            # INVENTORY SUB-OPTION 4: RETURN TO MAIN
            # =============================================
            
            elif sub_choice == "4":
                break  # Exit inventory sub-menu
            else:
                print("Invalid option. Try again.")

    # =============================================
    # OPTION 5: RUN VOTING SYSTEM
    # =============================================
    
    elif choice == "5":
        print("\n--- Run Voting System ---")
        
        # Input validation for number of voters
        while True:
            try:
                num_voters = int(input("Enter the total number of voters: "))
                # Check for non-negative number
                if num_voters >= 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # Check if there are voters
        if num_voters == 0:
            print("No voting can occur with 0 voters.")
            continue  # Go back to main menu

        # List to store all votes
        votes = []

        # Collect each voter's choice
        for i in range(num_voters):
            # Get candidate name
            vote = input(f"Voter {i+1} - Enter candidate name: ").strip()
            
            # Validate non-empty vote
            while not vote:
                vote = input(f"Voter {i+1} cannot be empty. Enter candidate name: ").strip()
            votes.append(vote)  # Add vote to list

        # Clear previous voting results
        voting_results.clear()

        # Count votes using dictionary
        for candidate in votes:
            # If candidate already exists, increment count
            if candidate in voting_results:
                voting_results[candidate] += 1
            # Otherwise, add new candidate with count 1
            else:
                voting_results[candidate] = 1

        # Display voting results
        print("\n--- Voting Summary Results ---")
        for cand, count in voting_results.items():
            print(f" Candidate '{cand}': {count} vote(s)")

        # Find winner
        winner = None
        max_votes = -1  # Initialize with -1 (since votes can't be negative)
        is_tie = False  # Flag for tie condition

        # Check each candidate's votes
        for cand, count in voting_results.items():
            if count > max_votes:  # Found new highest
                max_votes = count
                winner = cand
                is_tie = False  # Reset tie flag
            elif count == max_votes:  # Found equal votes
                is_tie = True  # Set tie flag

        # Display election result
        if is_tie:
            print(f"\nThe election ended in a Tie! Highest vote count was {max_votes}.")
        elif winner:
            print(f"\nWinner is Candidate: {winner}")

    # =============================================
    # OPTION 6: SEARCHING FEATURE
    # =============================================
    
    elif choice == "6":
        print("\n--- Searching Feature ---")
        # Get search term from user
        search_query = input("Enter search term (Student, Contact, or Candidate): ").strip()
        found = False  # Flag to track if found

        # Search in student records
        for s, s_name in enumerate(student_names):
            if s_name == search_query:
                print(f"Found in Student Tracker! '{search_query}' has a score of {student_scores[s]}.")
                found = True
                break  # Exit loop once found

        # Search in contact book
        if search_query in contact_book:
            print(f"Found in Contact Book! '{search_query}' phone number is: {contact_book[search_query]}.")
            found = True

        # Search in voting results
        if search_query in voting_results:
            print(f"Found in Voting Ledger! Candidate '{search_query}' received {voting_results[search_query]} votes.")
            found = True

        # If not found in any data structure
        if not found:
            print("Record not found")

    # =============================================
    # OPTION 7: STUDENT PERFORMANCE REPORT
    # =============================================
    
    elif choice == "7":
        print("\n--- Student Performance Report ---")

        # Dictionary to store student marks
        student_marks = {}

        # Loop to collect student data
        while True:
            # Get student name or exit command
            student_name = input("Enter student name (or type 'done' to finish): ").strip()

            # Check if user wants to finish
            if student_name.lower() == 'done':
                break

            # Validate non-empty name
            if not student_name:
                print("Student name cannot be empty. Please try again.")
                continue

            # Get number of subjects
            while True:
                try:
                    num_subjects = int(input(f"How many subject marks do you want to enter for {student_name}? "))
                    # Validate positive number
                    if num_subjects > 0:
                        break
                    print("Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid whole number.")

            # List to store marks for current student
            scores_list = []

            # Collect marks for each subject
            for i in range(num_subjects):
                while True:
                    try:
                        # Get individual subject mark
                        score = float(input(f"  Enter mark for Subject {i+1} (0-100): "))
                        # Validate score range
                        if 0 <= score <= 100:
                            scores_list.append(score)
                            break
                        print("Score must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            # Store marks with student name as key
            student_marks[student_name] = scores_list
            print(f"Successfully saved records for {student_name}.\n")

        # Display all student performance data
        if not student_marks:
            print("[No student records were entered.]")
        else:
            # Iterate through each student
            for student, marks in student_marks.items():
                print(f"Student: {student}")
                
                total_score = 0  # Reset total for each student
                print(" Subject Scores: ", end="")  # Print without newline
                
                # Display each mark
                for score in marks:
                    print(f"[{score}] ", end="")
                    total_score += score  # Sum up marks
                
                # Display total
                print(f"\n Total Combined Score: {total_score}")
                print("-" * 40)  # Separator line

    # =============================================
    # OPTION 8: EXIT PROGRAM
    # =============================================
    
    elif choice == "8":
        # Display farewell message
        print("\nThank you for utilizing the Smart School Management & Voting Analysis System.")
        break  # Exit the main loop, ending program

    # =============================================
    # INVALID INPUT HANDLING
    # =============================================
    
    else:
        print("Invalid input! Please enter a valid number (1-8).")
